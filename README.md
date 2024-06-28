![image](https://github.com/Pythonpa/UniAnimate-GradioUI/assets/16030016/57c9abc6-162d-4e79-8c82-381342869fbf)
# 使用说明 [zh]
1. 项目基于[UniAnimate](https://github.com/ali-vilab/UniAnimate),我仅在此项目基础上做了Docker镜像的构建，以及借助Claude 3.5的共同协助，写了一个非完成体的WebUI脚本，您可以继续自行完善（例如：配置文件的修改保存方法）。
2. 如果你安装的是Windows版本，也可以使用该UI脚本，但是请确保你的各目录路径设置正确。从头部署项目建议用`pip install -r requirements2.txt`,该依赖适配于python=3.10, CUDA=12.1, pytorch=2.2.2 
3. Docker镜像上传中...
    
4. WebUI的进度条显示仅供参考，具体执行进度和步骤还是以后台命令行显示的为准。（其实是因为不太擅长用Gradio, ^_^）
![image-1](https://github.com/Pythonpa/UniAnimate-GradioUI/assets/16030016/16b7a35a-b27a-4a04-83d3-e845c5d35a85)

![image](https://github.com/Pythonpa/UniAnimate-GradioUI/assets/16030016/c0da755d-1cfa-434c-b45e-001d2cbb3af7)


6. 最终视频生成结果在`/outputs/UniAnimate_infer/`文件夹中，你也可以自行修改生成结果的保存路径。
7. 关于[模型下载官方说明](https://github.com/ali-vilab/UniAnimate?tab=readme-ov-file#2-download-the-pretrained-checkpoints).
   另外，项目运行时，模型加载时间可能较长，请耐心等待。
8. 如果你的显卡和内存硬件不够好（最好高于12G显存&16G内存），请选择用`[512,768]`的像素尺寸。
# 我的联系方式
我的抖音账号: [AI大师工作流](https://www.douyin.com/user/MS4wLjABAAAAviq9ixG7tShWv_AJNEvCqlwZXd8YRTyCygSNpZ7J0aQ)
[BiliBili](https://space.bilibili.com/10389026),[小红书](https://www.xiaohongshu.com/user/profile/6358ac17000000001802adac)，今日头条，快手等短视频平台均同号。

****************************

# Instructions for use [en]
1. The project is based on [UniAnimate](https://github.com/ali-vilab/UniAnimate). I only built the Docker image on this project and wrote a non-completed script of WebUI with the help of Claude 3.5. You can continue to improve it yourself (for example, the modification and saving method of the configuration file).
2. You can also use this UI script if you are installing the Windows version, but make sure that your directory paths are set correctly. It is recommended to use `pip install -r requirements2.txt` for the project to deploy from scratch, which is adapted to python = 3.10, CUDA = 12.1, pytorch = 2.2.2
3. Docker image is uploading...
4. The progress bar of webui is displayed for reference only. The specific execution progress and steps are subject to those displayed on the back command line. (In fact, I am not good at using Gradio ^_^)

![image-1](https://github.com/Pythonpa/UniAnimate-GradioUI/assets/16030016/16b7a35a-b27a-4a04-83d3-e845c5d35a85)

![image](https://github.com/Pythonpa/UniAnimate-GradioUI/assets/16030016/c0da755d-1cfa-434c-b45e-001d2cbb3af7)

5. The final video generation result is in`/outputs/UniAnimate_infer/`folder.
6. About[Models Downloading,follow the official instructions](https://github.com/ali-vilab/UniAnimate?tab=readme-ov-file#2-download-the-pretrained-checkpoints).The models will take a long time to load, please wait patiently.
7. If your graphics card and memory hardware are not good enough (Better than 12G VRAM & 16G RAM), please choose the pixel size of `[512,768]`.
# My social media
My social media account: [AI Master Workflow](https://www.douyin.com/user/MS4wLjABAAAAviq9ixG7tShWv_AJNEvCqlwZXd8YRTyCygSNpZ7J0aQ)  
[BiliBili](https://space.bilibili.com/10389026), and other short video platforms are all the same account.


# Disclaimer
This open-source model is intended for RESEARCH/NON-COMMERCIAL USE ONLY. We explicitly disclaim any responsibility for user-generated content. Users are solely liable for their actions while using the generative model. The project contributors have no legal affiliation with, nor accountability for, users' behaviors. It is imperative to use the generative model responsibly, adhering to both ethical and legal standards.
