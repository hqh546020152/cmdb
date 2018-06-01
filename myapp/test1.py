import json
from urllib import request, parse

ZABBIX_URL =  'http://zabbix.devops.yihuivip.cn'
ZABBIX_USERNAME = "admin"
ZABBIX_PASSWORD = "EtHHeEraz9O5CzU04OZ1"

#登陆
url = "{}/api_jsonrpc.php".format(ZABBIX_URL)
header = {"Content-Type": "application/json"}
# auth user and password
data = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": ZABBIX_USERNAME,
        "password": ZABBIX_PASSWORD
    },
    "id": 1,
}
# 由于API接收的是json字符串，故需要转化一下
value = json.dumps(data).encode('utf-8')

# 对请求进行包装
req = request.Request(url, headers=header, data=value)

# 验证并获取Auth ID
try:
    # 打开包装过的url
    result = request.urlopen(req)
except Exception as e:
    print("Auth Failed, Please Check Your Name And Password:", e)
else:
    response = result.read()
    # 上面获取的是bytes类型数据，故需要decode转化成字符串
    page = response.decode('utf-8')
    # 将此json字符串转化为python字典
    page = json.loads(page)
    result.close()
    # print("Auth Successful. The Auth ID Is: {}".format(page.get('result')))
    print(page.get('result'))

# #请求查看所有主机
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": [
#             "hostid",
#             "host"
#         ],
#         "selectInterfaces": [
#             "interfaceid",
#             "ip"
#         ]
#     },
#     "id": 2,
#     "auth": page.get('result')
# }
#
# value = json.dumps(data).encode('utf-8')
# req = request.Request(url, headers=header, data=value)
# try:
#     result = request.urlopen(req)
# except Exception as e:
#     print("Auth Failed, Please Check Your Name And Password:", e)
# else:
#     response = result.read()
#     page = response.decode('utf-8')
#     #转化为字典
#     page = json.loads(page)
#     result.close()
#     print(page)

# #获取所有组群及ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": page.get('result'),
#     "id": 1
# }
# value = json.dumps(data).encode('utf-8')
# req = request.Request(url, headers=header, data=value)
# try:
#     result = request.urlopen(req)
# except Exception as e:
#     print("Auth Failed, Please Check Your Name And Password:", e)
# else:
#     response = result.read()
#     page = response.decode('utf-8')
#     #转化为字典
#     page = json.loads(page)
#     result.close()
#     print(page)


#获取模板ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 "Template App Zabbix Server"
#             ]
#         }
#     },
#     "auth": page.get('result'),
#     "id": 1
# }
# value = json.dumps(data).encode('utf-8')
# req = request.Request(url, headers=header, data=value)
# try:
#     result = request.urlopen(req)
# except Exception as e:
#     print("Auth Failed, Please Check Your Name And Password:", e)
# else:
#     response = result.read()
#     page = response.decode('utf-8')
#     #转化为字典
#     page = json.loads(page)
#     result.close()
#     print(page.get('result')[0].get('templateid'))

# #删除主机,传入hostid
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10128","10129"
#     ],
#     "auth": page.get('result'),
#     "id": 1
# }
# value = json.dumps(data).encode('utf-8')
# req = request.Request(url, headers=header, data=value)
# try:
#     result = request.urlopen(req)
# except Exception as e:
#     print("Auth Failed, Please Check Your Name And Password:", e)
# else:
#     response = result.read()
#     page = response.decode('utf-8')
#     #转化为字典
#     page = json.loads(page)
#     result.close()
#     print(page)

#更新主机接口
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.update",
#     "status": 0,
#     "params": {
#         "hostid": "10130",
#         "templates_clear": [
#             {
#                 "templateid": "10001"
#             }
#         ]
#
#     },
#     "auth": page.get('result'),
#     "id": 1
# }
# value = json.dumps(data).encode('utf-8')
# req = request.Request(url, headers=header, data=value)
# try:
#     result = request.urlopen(req)
# except Exception as e:
#     print("Auth Failed, Please Check Your Name And Password:", e)
# else:
#     response = result.read()
#     page = response.decode('utf-8')
#     #转化为字典
#     page = json.loads(page)
#     result.close()
#     print(page)


#添加主机
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Linux server4",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.3.1",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "4"
            }
        ],
        "templates": [
            {
                "templateid": "10001"

            },
            {
                "templateid": "10047"

            }
        ],
        "inventory_mode": 0,
    },
    "auth": page.get('result'),
    "id": 1
}
value = json.dumps(data).encode('utf-8')
req = request.Request(url, headers=header, data=value)
try:
    result = request.urlopen(req)
except Exception as e:
    print("Auth Failed, Please Check Your Name And Password:", e)
else:
    response = result.read()
    page = response.decode('utf-8')
    #转化为字典
    page = json.loads(page)
    result.close()
    print(page)


