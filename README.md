# UCAS-CampusNetwork-AutoLogin
中国科学院大学(国科大)校园网自动登录脚本

## 简介
- 支持Windows, Linux
- 每隔20s监测网络连通状态，如果断开自动登录校园网
## 运行环境
- Windows, Linux
- Python 3+
- 与本机chrome版本匹配的chromedriver
- 外部依赖库：selenium
## 使用方法
### 命令行版本(须在命令行里输入参数：账号，密码)
- python autologin_cli.py -username USERNAME -password PASSWORD
- 其中username(账号), password(密码)为必填参数
### 直接运行版本(账号密码加密存储在配置文件中）
- 需要在autologin.py中手动填写加密方式、密钥、Iv
- 在代码同目录下新建config.txt文件，写入加密后的账号和密码
- 运行python autologin.py

## 代码如有bug请提交issue或联系QQ1491775988
