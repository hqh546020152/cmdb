from elasticsearch import Elasticsearch
# import urllib
# import urllib2
import json
import time
import datetime
# import paramiko

# # 接口标准格式
# class PostZbSelectView(APIView):
#     def post(self, request):
#         try:
#             if request.session['username']:
#                 #逻辑处理
#                 pass
#             else:
#                 context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
#                 return JsonResponse(context)
#         except KeyError:
#             context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
#             return JsonResponse(context)

es = Elasticsearch(['hqh-study-python.com:9298'])
# index = "my-index"
# type = "test"
id ="AWO0CbGxQqGng7R8yuaJ"
print(type(id))
es.delete(index='my-script', type='script', id=id)

# body = {"query": {'term': { "auth":"0" }}}
# tty = es.search(index=index, doc_type=type, body=body)
# sumshu = []
# for hit in tty['hits']['hits']:
#     ptk = hit['_source']
#     sumshu.append(ptk)
# print(sumshu)
import base64
# from Crypto.Cipher import AES
# from Crypto.Hash import SHA256
# # from Crypto import Random
# hash = SHA256.new()
# hash.update('你好'.encode('utf-8'))
# print(hash.digest())
# print(hash.hexdigest())
#
# obj = AES.new('This is a key456',AES.MODE_ECB)
# message = "The answer is no"
# ciphertext = obj.encrypt(message)
# print('AES加密密文：',ciphertext)
#
# obj2 = AES.new('This is a key456',AES.MODE_ECB)
# detext=obj2.decrypt(ciphertext)
# print('AES解密密文：',detext.decode())
#
# print("test")
# try:
#     if request.session['username']:
#
#     else:
#         context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
#         return JsonResponse(context)
# except KeyError:
#     context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
#     return JsonResponse(context)

# class SSH_passwd():
#     def sshclient_execmd(self, hostname , port , username ,password, execmd ):
#         paramiko.util.log_to_file("paramiko.log") #打印执行日志
#         s = paramiko.SSHClient()      #调用paramiko模块下的SSHClient()
#         s.load_system_host_keys()     #加载本地的known_hosts文件，该文件是纪录连到对方时，对方给的 host key。每次连线时都会检查目前对方给>的 host key 与纪录的 host key 是否相同，可以简单验证连结是否又被诈骗等相关事宜。
#         s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         s.connect( hostname = hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = s.exec_command (execmd)
#         stdin.write("Y") # Generally speaking, the first connection, need a simple interaction.
#         A = stdout.read()   #执行成功，将返回执行结果。执行失败则为空
#         B = stderr.read()   #执行失败，将返回错误信息。执行成功则为空
#         s.close()     #关闭连接
#         if A :
#             # 将字节对象decode将获得一个str对象
#             s2 = bytes.decode(A)
#             return s2
#         else:
#             return B
#     def put_file(self, local_path, remote_path, hostname, username, password, port=22):
#         print(local_path, remote_path, hostname, username, password, port)
#         t = paramiko.Transport(hostname, port)
#         t.connect(username , password)
#         sftp = paramiko.SFTPClient.from_transport(t)
#         sftp.put(local_path, remote_path)
#         ttt = t.close()
#         return ttt


# hostname = 'hqh-study-python.com'
# port = 2222
# username = 'admin'
# password = '3XtgCvWliZJ7WdKJ1QrZ'
# execmd = "cat /etc/redhat-release"
# local_path = r'C:\Users\Administrator\Desktop\cmdb\myapp\detect.sh'
# remote_path = r'/tmp/test.sh'
# # print(type(hostname),type(port))
# transport = paramiko.Transport((hostname,port))
# transport.connect(username=username,password=password)
# sftp = paramiko.SFTPClient.from_transport(transport)
# sftp.put( local_path , remote_path )
# tty =transport.close()
# print(tty)



# pty = SSH_passwd()
# pushfile = pty.put_file( local_path= local_path , remote_path = remote_path , hostname = hostname , username=username , password=password , port =port )
# print(pushfile)
# ttt = pty.sshclient_execmd(hostname = hostname,port = port , username = username , password = password , execmd = execmd )
# print(ttt)

# 传输給html的必须是一个字典
# context = {'messages': ttt}
# return render(request, "cmdb/index.html", context)

#pip3 install pycrypto
import base64
# from Crypto.Cipher import AES
# from Crypto import Random
# from Crypto.Hash import SHA256

class Compute():
    readme = '加密解密'
    def __init__(self):
        pass
    def Encode(self, data, key):
        obj = AES.new( key , AES.MODE_ECB)
        ciphertext = obj.encrypt(data)
        print('AES加密密文：', ciphertext )
        return ciphertext
    def Decode(self, data, key):
        obj = AES.new(key , AES.MODE_ECB)
        detext = obj.decrypt(data)
        print('AES解密密文：', detext.decode())
        return detext.decode()