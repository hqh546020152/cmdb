from myapp import models

import json
from rest_framework.views import APIView
from django.http import JsonResponse

#选择主机使用接口，筛选出已添加认证信息的服务器
class PostAutoSelectView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                # 获取参数数据
                auth = request.POST.get('auth', '')
                if auth:
                    if auth == "0":
                        x = models.Es()
                        context = {'status': 1, 'messages': x.Get_data_all(index='my-index', type='test',body = {"query": {'term': { "auth":"0" }}} )}
                        return JsonResponse(context)
                    else:
                        context = {'status': 0, 'messages': "input error" }
                        return JsonResponse(context)
                else:
                    context = {'status': 0, 'message': '查无数据'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#选择主机使用接口，筛选出已添加认证信息的服务器
class PostSelectScriptView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                # 获取参数数据
                id = request.POST.get('id', '')
                if id:
                    if id == "all":
                        x = models.Es()
                        context = {'status': 1, 'messages': x.Get_data_all(index='my-script', type='script') }
                        return JsonResponse(context)
                    else:
                        context = {'status': 0, 'messages': "input error" }
                        return JsonResponse(context)
                else:
                    context = {'status': 0, 'message': '查无数据'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#添加脚本
class PostAddScriptView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                tagname = request.POST.get('tagname', '')
                # dir = request.POST.get('dir', '')
                name = request.POST.get('name', '')
                stats = request.POST.get('stats', '')
                notes = request.POST.get('notes', '')
                x = models.Es()
                #部署到生产环节时需要修改此处的绝对路径，存放脚本
                dir = r'C:\Users\Administrator\Desktop\cmdb\myapp\script'
                message = {'tagname': tagname, 'dir': dir,
                           'name': name, 'stats': stats, 'notes': notes }
                print(message)
                x.Create_data(index='my-script', type='script', body=message)
                context = {'status': 1, 'messages': '添加成功'}
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#Es数据删除接口，需要传入id，根据id删除
class PostDelScriptView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    id = request.POST.get('id', '')
                    print(id)
                    if id:
                        y = models.Es()
                        y.Rm_data(index='my-script', type='script', id=id)
                        context = {'status': 1, 'message': '删除成功！', 'messages': id }
                        return JsonResponse(context)
                    else:
                        context = {'status': 0, 'message': '删除失败，未接收参数！', 'messages': id }
                        return JsonResponse(context)
                except KeyError:
                    context = {'status': 0, 'message': '删除失败！', 'messages': id}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#批处理，执行脚本
class PostExecuteView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                host = request.POST.get('host', '')
                script = request.POST.get('script', '')
                stats = request.POST.get('stats', '')
                #将字符串转化为列表
                host_list = host.strip(',').split(',')
                script_list = script.strip(',').split(',')
                # print(host_list,script_list)
                # print(host,script,stats)
                for  host in host_list :
                    if ( not host ):
                        context = {'status': 0, 'messages': '输入有误'}
                        return JsonResponse(context)
                    x = models.Es()
                    ttx = x.Get_data(index='my-index', type='test', id=host)
                    hostname = ttx['_source']['hostname']
                    port = ttx['_source']['port']
                    username = ttx['_source']['username']
                    password = ttx['_source']['password']
                    # if (not hostname or not port or not username or not password):
                    #                     #     context = {'status': 0, 'messages': '输入有误'}
                    #                     #     return JsonResponse(context)
                    for script in script_list :
                        tty =  x.Get_data(index='my-script', type='script', id=script)
                        # print(tty['_source']['dir'])
                        # print(tty['_source']['name'])
                        #服务器存储脚本路径
                        local_path = tty['_source']['dir'] + '\\' + tty['_source']['name']
                        print(local_path)
                        #上次至服务器路径
                        remote_path = r'/tmp/' + tty['_source']['name']
                        print(remote_path)
                        pty = models.SSH_passwd()
                        ttt = pty.put_file(hostname=hostname, port=port, username=username, password=password,
                                           local_path=local_path, remote_path=remote_path)
                        execmd = 'sh /tmp/' + tty['_source']['name']
                        ttp = pty.sshclient_execmd(hostname=hostname, port=port, username=username, password=password,
                                                   execmd=execmd)
                        ttl = eval(ttp)
                context = {'status': 1, 'messages': ttl }
                # context = {'status': 1, 'messages': 'env execmd succeed!'}
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)