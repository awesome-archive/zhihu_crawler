# -*- coding: UTF-8 -*-
from zhihu.client import Client

# 所有程序的入口
client = Client()
# 直接使用用户名和密码登录
client.login(username='+8615555555555', password='password', load_token=False)
# 不使用参数,根据命令行输入
# client.login()

# 登录后获取个人信息
myself = client.myself()

# 打印个人信息,json 格式
print(myself.info())

