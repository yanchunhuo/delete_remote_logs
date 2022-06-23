## 使用方法
### 一、安装依赖库
- pip3 install -r requirements.txt

### 二、使用说明
- 根据实际情况修改config目录的配置文件
- python3 main.py 删除或清除远程服务器的日志
- 当前仅支持python3.6.8

### 三、注意
- 确保登录的账号有对日志文件操作的权限
- 尽可能不使用删除文件，避免误删或者影响程序的运行
- 操作目录内的文件，必须指定文件后缀，避免出现误操作
- 仅支持Linux服务器
- 确保日志所在服务器有ls、stat命令

### 四、支持操作的文件类型：
- regular empty file
- regular file
- directory 目录内的文件
- symbolic link

# [进交流群]()
![avatar](https://github.com/yanchunhuo/resources/blob/master/wechat.png)

[![Stargazers over time](https://starchart.cc/yanchunhuo/delete_remote_logs.svg)](https://starchart.cc/yanchunhuo/delete_remote_logs)




