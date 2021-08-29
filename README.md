# UCAS-CampusNetwork-AutoLogin
中国科学院大学(国科大)校园网自动登录脚本

## 简介
支持Windows, Linux
每隔20s监测网络连通状态，如果断开自动登录校园网
## 运行环境
Windows, Linux
Python 3+
与本机chrome版本匹配的chromedriver
外部依赖库：selenium
## 使用方法
可执行文件运行
python main.py -username USERNAME -password PASSWORD
其中username(学号), password(密码)为必填参数

代码如有bug请提交issue或联系QQ1491775988
