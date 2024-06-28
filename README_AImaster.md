# 使用说明 [zh]
1. 项目基于[UniAnimate](https://github.com/ali-vilab/UniAnimate),我仅在此项目基础上做了Docker镜像的构建，以及借助Claude 3.5的共同协助，写了一个非完成体的WebUI脚本，您可以继续自行完善（例如：配置文件的修改保存方法）。
2. [上传中，未完成]Docker的基础镜像是基于[pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime](https://hub.docker.com/layers/pytorch/pytorch/2.2.2-cuda12.1-cudnn8-runtime/images/sha256-923f687790bec78081c357e71dcd5dcef80b0cc00f6c34484902a5e83362c854?context=explore)这个官方镜像的，你也可以自行选择其他版本的pytorch和CUDA。另外，镜像默认挂载卷`D:\PythonProject\UniAnimate:/workspace/UniAnimate`，你可以在启动容器时，自行修改挂载卷的路径。
    - 拉取镜像
    ```shell
    docker pull UniAnimate:webui
    ```
    
    - 启动容器
    ```shell
    docker run --gpus all -p 7860:7860 --name UniAnimate-webui -v D:\PythonProject\UniAnimate:/workspace/UniAnimate  -d UniAnimate:webui  cd /workspace/UniAnimate/ python3 -m webui

    ```
    
3. webui的进度条显示仅供参考，具体执行进度和步骤还是以后台命令行显示的为准。（其实是因为不太擅长用Gradio, ^_^）

![alt text](image.png)
![alt text](image-1.png)

4. 最终视频生成结果在`/outputs/UniAnimate_infer/`文件夹中，你也可以自行修改生成结果的保存路径。
5. 模型加载时间较长，请耐心等待。
6. 如果你的显卡和内存硬件不够好（低于12G显存&16G内存），请选择用`[512,768]`的像素尺寸。
# 我的联系方式
我的抖音账号: [AI大师工作流](https://www.douyin.com/user/MS4wLjABAAAAviq9ixG7tShWv_AJNEvCqlwZXd8YRTyCygSNpZ7J0aQ)
[BiliBili](https://space.bilibili.com/10389026),[小红书](https://www.xiaohongshu.com/user/profile/6358ac17000000001802adac)，今日头条，快手等短视频平台均同号。

****************************

# Instructions for use [en]
1. The project is based on [UniAnimate](https://github.com/ali-vilab/UniAnimate). I only built the Docker image on this project and wrote a non-completed script of WebUI with the help of Claude 3.5. You can continue to improve it yourself (for example, the modification and saving method of the configuration file).
2. Docker's basic image is based on the official image [pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime](https://hub.docker.com/layers/pytorch/pytorch/2.2.2-cuda12.1-cudnn8-runtime/images/sha256-923f687790bec78081c357e71dcd5dcef80b0cc00f6c34484902a5e83362c854?context=explore). You can also choose other versions of pytorch and CUDA. In addition, the default mount volume of the mirror is `D:\PythonProject\UniAnimate:/workspace/UniAnimate`. You can modify the path of the mount volume when starting the container.
3. The progress bar of 3. webui is displayed for reference only. The specific execution progress and steps are subject to those displayed on the back command line. (In fact, I am not good at using Gradio ^_^)

![alt text](image.png)
![alt text](image-1.png)

4. The final video generation result is in`/outputs/UniAnimate_infer/`folder.
5. The models will take a long time to load, please wait patiently.
6. If your graphics card and memory hardware are not good enough (less than 12G video memory & 16G memory), please choose the pixel size of `[512,768]`.
# My social media
My social media account: [AI Master Workflow](https://www.douyin.com/user/MS4wLjABAAAAviq9ixG7tShWv_AJNEvCqlwZXd8YRTyCygSNpZ7J0aQ)  
[BiliBili](https://space.bilibili.com/10389026), and other short video platforms are all the same account.


# Disclaimer
This open-source model is intended for RESEARCH/NON-COMMERCIAL USE ONLY. We explicitly disclaim any responsibility for user-generated content. Users are solely liable for their actions while using the generative model. The project contributors have no legal affiliation with, nor accountability for, users' behaviors. It is imperative to use the generative model responsibly, adhering to both ethical and legal standards.
