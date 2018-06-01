import json
from urllib import request

class Zabbix():
    #参数初始化
    def __init__(self):
        #配置Zabbix
        self.ZABBIX_URL = ""
        self.ZABBIX_USERNAME = ""
        self.ZABBIX_PASSWORD = ""
        self.url = "{}/api_jsonrpc.php".format(self.ZABBIX_URL)
        self.header = {"Content-Type": "application/json"}
        self.authID = self.User_login()
    #相同操作抽取为一个函数，减少代码冗余
    def RequestFun(self,data):
        value = json.dumps(data).encode('utf-8')
        req = request.Request(self.url, headers=self.header, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            return page
    # 操作接口、获取auth认证信息
    def User_login(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.ZABBIX_USERNAME,
                "password": self.ZABBIX_PASSWORD
            },
            "id": 1,
        }
        message = self.RequestFun(data)
        #获取返回信息，并将auto值提取出来，作为返回结果
        return message.get('result')
    #获取全部主机信息，以数组结果返回，包括interfaceid、IP、host、hostid
    def Get_data(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 2,
            "auth": self.authID
        }
        message = self.RequestFun(data)
        return message.get('result')
    #获取所有组群及ID,以数组结果返回，包括name、flags、internal、groupid
    def Get_group(self):
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": "extend",
                "filter": {
                    "name": [
                        "Zabbix servers",
                        "Linux servers",
                        "Templates",
                        "Hypervisors",
                        "Discovered hosts",
                        "Virtual machines"
                    ]
                }
            },
            "auth": self.authID,
            "id": 1
        }
        message = self.RequestFun(data)
        return message.get('result')
    #以模板名称，获取模板ID，以数组结果返回，将返回模板内信息信息，其他模板ID参数为：templateid
    def Get_templateID(self):
        data = {
            "jsonrpc": "2.0",
            "method": "template.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": [
                        "Template OS Linux",
                        "Template App Zabbix Server",
                        "Template App MySQL",
                        "Template App SSH Service"
                    ]
                }
            },
            "auth": self.authID,
            "id": 1
        }
        message = self.RequestFun(data)
        return message.get('result')
    # 删除主机,传入hostid;注意：传入hostid必须为数组(类型)
    def Del_host(self,hostid):
        data = {
            "jsonrpc": "2.0",
            "method": "host.delete",
            "params": hostid,
            "auth": self.authID,
            "id": 1
        }
        message = self.RequestFun(data)
        return message.get('result')
    # 更新主机接口
    def Update_host(self,hostid):
        data = {
            "jsonrpc": "2.0",
            "method": "host.update",
            "status": 0,
            "params": {
                "hostid": hostid,
                "templates_clear": [
                    {
                        "templateid": "10001"
                    }
                ]

            },
            "auth": self.authID,
            "id": 1
        }
        message = self.RequestFun(data)
        return message.get('result')
    #添加主机,需要传入名称、客户端ip、客户端端口、群组ID、模板ID
    def Create_host(self,name,ip,port,groupid,templateid):
        temp = []
        for test in templateid:
            mes = { "templateid" : test }
            temp.append(mes)
        print(temp)
        data = {
            "jsonrpc": "2.0",
            "method": "host.create",
            "params": {
                "host": name,
                "interfaces": [
                    {
                        "type": 1,
                        "main": 1,
                        "useip": 1,
                        "ip": ip,
                        "dns": "",
                        "port": port
                    }
                ],
                "groups": [
                    {
                        "groupid": groupid
                    }
                ],
                "templates": temp ,
                "inventory_mode": 0,
            },
            "auth": self.authID,
            "id": 1
        }
        message = self.RequestFun(data)
        print(message)
        return message.get('result')

#功能调试
# #调用获取全部主机信息
# x = Zabbix()
# print(x.Get_data())
# print(len(x.Get_data()))
#获取所有组群及ID
# x = Zabbix()
# print(x.Get_group())
# #以模板名称，获取模板ID
# x = Zabbix()
# print(x.Get_templateID())
# #调用删除
# x = Zabbix()
# y = x.Del_host(hostid=["10130"])
# print(y)
# #更新操作，移除指定主机的模板
# x =  Zabbix()
# y = x.Update_host(hostid="10132")
# print(y)
#添加主机
    # 备注：templateid=10001为OS Linux默认模板、10047为App Zabbix Server模板
# x = Zabbix()
# templateid_list = ['']
# y = x.Create_host(name="Linux server4",ip="192.168.3.1",port="10050",groupid="4",templateid=templateid_list )
# print(y)
# if y:
#     print("1")
# else:
#     print("2")