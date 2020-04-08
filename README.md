## 使用方法
### 一、安装依赖库
- pip3 install -r requirements.txt

### 二、使用说明
- 根据实际情况修改Info文件
- python3 runRemoteDelLogs.py 删除或清除远程服务器的日志

### 三、注意
- Info文件的数据以双管道符"||"拼接：IP||username||passwd||dirs||regexs||howmanydays||isRemoveFile||isRemoveDirs

```
IP：      远程服务器的IP地址
username：远程服务器的登录名
passwd：  远程服务器的密码
dirs：    需要扫描的目录
regexs：  正则表达式，以逗号隔开
howmanydays：删除/清除几天前的日志
isRemoveFile：是否删除文件，不删除则清空。1代表删除，0代表是清空
isRemoveDirs：是否删除目录内的内容，若设置删除，则regexs、isRemoveFile参数均无效。1代表删除
```

# [打赏]()
![avatar](https://github.com/yanchunhuo/resources/blob/master/Alipay.jpg)