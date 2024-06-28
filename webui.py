import gradio as gr
import yaml
import subprocess
import os
import shutil
import json
import traceback
from gradio import Progress
import glob
import time

def update_yaml(ref_image, drive_video, resolution, max_frames, seed):
    with open('configs/UniAnimate_infer.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    config['resolution'] = eval(resolution)
    config['max_frames'] = max_frames
    config['seed'] = seed
    
    ref_name = os.path.basename(ref_image)
    drive_name = os.path.splitext(os.path.basename(drive_video))[0]
    config['test_list_path'] = [[2, f"data/images/{ref_name}", f"data/saved_pose/{drive_name}"]]
    
    with open('configs/UniAnimate_infer.yaml', 'w') as file:
        yaml.dump(config, file)

def get_latest_video(directory):
    list_of_files = glob.glob(f'{directory}/*.mp4')  # 获取所有.mp4文件
    if not list_of_files:  # 如果没有找到文件
        return None
    latest_file = max(list_of_files, key=os.path.getctime)  # 获取最新创建的文件
    return latest_file

def process_video(ref_image, drive_video, resolution, max_frames, seed, progress=gr.Progress()):
    try:
        ref_path = f"data/images/{os.path.basename(ref_image.name)}"
        drive_path = f"data/videos/{os.path.basename(drive_video.name)}"
        os.makedirs(os.path.dirname(ref_path), exist_ok=True)
        os.makedirs(os.path.dirname(drive_path), exist_ok=True)
        
        shutil.copy(ref_image.name, ref_path)
        shutil.copy(drive_video.name, drive_path)
        
        update_yaml(os.path.basename(ref_image.name), os.path.basename(drive_video.name), resolution, max_frames, seed)
        
        drive_name = os.path.splitext(os.path.basename(drive_video.name))[0]
        
        progress(0, desc="Aligning pose")
        subprocess.run([
            "python", "run_align_pose.py",
            "--ref_name", ref_path,
            "--source_video_paths", drive_path,
            "--saved_pose_dir", f"data/saved_pose/{drive_name}"
        ], check=True)
        
        progress(0.5, desc="Generating video")
        subprocess.run([
            "python", "inference.py",
            "--cfg", "configs/UniAnimate_infer.yaml"
        ], check=True)
        
        progress(1, desc="Complete")
        
        # 等待一小段时间，确保文件已经完全写入
        time.sleep(2)
        
        output_dir = "outputs/UniAnimate_infer"
        latest_video = get_latest_video(output_dir)
        
        if latest_video:
            return latest_video, None
        else:
            return None, f"在 {output_dir} 中未找到生成的视频文件"
    except Exception as e:
        error_msg = f"发生错误：{str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return None, error_msg

def save_config(ref_image, drive_video, resolution, max_frames, seed):
    config = {
        "resolution": resolution,
        "max_frames": max_frames,
        "seed": seed
    }
    with open("user_config.json", "w") as f:
        json.dump(config, f)
    return "配置已保存"

def load_config():
    try:
        with open("user_config.json", "r") as f:
            config = json.load(f)
        return config["resolution"], config["max_frames"], config["seed"], "配置已加载"
    except FileNotFoundError:
        return "[768, 1216]", 32, 11, "未找到保存的配置，使用默认值"

with gr.Blocks() as demo:
    gr.Markdown("# UniAnimate Video Generator")
    
    with gr.Row():
        with gr.Column(scale=1):
            ref_image = gr.File(label="上传参考图片", file_types=[".jpg", ".png", ".jpeg"])
            drive_video = gr.File(label="上传驱动视频", file_types=[".mp4", ".avi", ".mov"])
        
        with gr.Column(scale=1):
            resolution = gr.Dropdown(choices=["[512, 768]", "[768, 1216]"], label="分辨率", value="[768, 1216]")
            max_frames = gr.Slider(minimum=1, maximum=64, step=1, label="最大帧数", value=32)
            seed = gr.Number(label="随机种子", value=11)
            generate_btn = gr.Button("生成视频")
    
    with gr.Tabs():
        with gr.TabItem("输出"):
            output_video = gr.File(label="生成的视频")
            error_output = gr.Textbox(label="错误信息", visible=False)
        with gr.TabItem("配置"):
            save_btn = gr.Button("保存配置")
            load_btn = gr.Button("加载配置")
            config_status = gr.Textbox(label="配置状态")
    
    def on_process_complete(video_path, error):
        if error:
            return gr.update(visible=True, value=error), gr.update(visible=False)
        else:
            return gr.update(visible=False), gr.update(visible=True, value=video_path)
    
    generate_btn.click(
        process_video,
        inputs=[ref_image, drive_video, resolution, max_frames, seed],
        outputs=[output_video, error_output]
    ).then(
        on_process_complete,
        inputs=[output_video, error_output],
        outputs=[error_output, output_video]
    )
    
    save_btn.click(save_config, inputs=[ref_image, drive_video, resolution, max_frames, seed], outputs=config_status)
    load_btn.click(load_config, outputs=[resolution, max_frames, seed, config_status])

demo.launch(server_name="0.0.0.0", server_port=7860)