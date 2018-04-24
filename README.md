## 使用方法
### 一、安装依赖库
- pip install -r requirements.txt

### 一、使用说明
- 根据实际情况修改Info文件
- python runRemoteDelLogs.py 删除或清除远程服务器的日志

### 二、注意
- Info文件的数据以双管道符“||”拼接：IP||username||passwd||dirs||regexs||howmanydays||isRemove

```
IP：      远程服务器的IP地址
username：远程服务器的登录名
passwd：  远程服务器的密码
dirs：    需要扫描的目录
regexs：  正则表达式，以逗号隔开
howmanydays：删除/清除几天前的日志
isRemove：是否删除文件，不删除则清空。0是删除，1是清除
```
