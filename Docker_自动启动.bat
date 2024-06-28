@echo off

:: 作者: AI大师工作流
:: 请关注我: 抖音、B站、小红书、今日头条、快手等平台均为此号。
:: 版权声明: 本脚本由AI大师工作流编写，未经许可，不得转载或用于商业用途。不可用于从事违反中华人民共和国各项法律法规的行为。

chcp 65001 >nul 2>&1  &&  (echo Code page set to UTF-8.) || (chcp 437 >nul & echo Failed to set code page to UTF-8, using default.)
setlocal EnableDelayedExpansion

REM 定义检查和安装状态的变量
set "git_installed=0"
set "cuda_installed=0"
set "docker_installed=0"

REM 检查Git是否安装
echo Checking Git installation...
for /f "tokens=2 delims=:" %%i in ('git --version 2^>nul') do (
    set "git_installed=1"
    echo 已安装Git
)

REM 检查CUDA是否安装
echo Checking CUDA installation...
for /f "tokens=2 delims=:" %%i in ('nvcc --version 2^>nul') do (
    set "cuda_installed=1"
    echo 已安装CUDA
)

REM 检查Docker是否安装
echo Checking Docker installation...
for /f "tokens=3 delims=," %%i in ('docker --version 2^>nul ^| find "Docker version"') do (
    set "docker_installed=1"
    echo 已安装Docker
)

REM 检查所有软件是否都已安装
if !git_installed! equ 0 echo 缺失Git else if !cuda_installed! equ 0 echo 缺失CUDA else if !docker_installed! equ 0 echo 缺失Docker else (
    echo 所有软件已安装，开始执行下一步...

    REM 克隆Git仓库
    echo Cloning Git repository...
    git clone https://github.com/Pythonpa/UniAnimate-GradioUI.git "D:\PythonProject\UniAnimate-GradioUI"

    REM 拉取Docker镜像
    echo Pulling Docker image...
    docker pull aimaster104/unianimate:webui

    REM 运行Docker容器
    echo Running Docker container...
    docker run --gpus all -p 7860:7860 --name UniAnimate-webui -v D:\PythonProject\UniAnimate-GradioUI:/workspace/
