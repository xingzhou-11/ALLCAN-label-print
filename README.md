# ALLCAN-label-print
ALLCAN标签打印工具

# 环境介绍
- 硬件：
    - orangepi3 LTS（ubuntu系统）
    - canable(适配linux的固件)
    - GPIO16控制LED指示灯
    - GPIO12接收按钮信号

# 服务配置
- 安装 `Can-utils` 
    ```
    sudo apt-get update
    sudo apt-get -y install can-utils
    ```

- 插上canable自动启动can服务
    - 在 `/etc/systemd/network` 下添加文件 `can0.network`（.network结尾就可以）
    - 文件中添加内容：
        ```
        [Match]
        Name=can0

        [CAN]
        BitRate=1M
        RestartSec=100ms
        ```
    - 管理 `network` 服务的是 `systemd-networkd`, 使用命令 `sudo systemctl enable systemd-networkd` 设置为开机自启
        - sudo systemctl status systemd-networkd 查看状态
        - sudo systemctl start systemd-networkd 启动
        - sudo systemctl stop systemd-networkd 停止
        - sudo systemctl disable main 取消开机启动

- 主程序配置为开机启动
    - 由于需要root权限运行，需要在root环境下安装所需要的python包
        ```
        su root

        pip3 install canopen
        ```
    - 在 `/etc/rc.local` 文件中添加
    - 文件中添加内容
        ```
        sudo /usr/bin/python3 /home/orangepi/ALLCAN-label-print/main.py
        exit 0
        ```
        
# 注意事项
- 运行调试代码需要使用root权限
- sudo 命令会导致程序在另外一片空间运行，导致找不到库（库都已经放在了文件夹下）
- sudo -E 命令能够使程序强制跑在当前的空间，即可正常运行