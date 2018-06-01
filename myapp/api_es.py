from myapp import models

import json
import time
from rest_framework.views import APIView
from django.http import JsonResponse


#Es数据查询API，如传入ID无，则报错。id=all则返回所有数据
class PostEsSelectView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                # 获取参数数据
                # session_key = request.session.session_key
                # print(session_key)
                id = request.POST.get('id', '')
                # print(id)
                if id:
                    if id == "all":
                        x = models.Es()
                        context = {'status': 1, 'messages': x.Get_data_all(index='my-index', type='test')}
                        print(context)
                        return JsonResponse(context)
                    else:
                        try:
                            y = models.Es()
                            res = y.Get_data(index='my-index', type='test', id=id)
                            context = {'messages': json.dumps(res)}
                            return JsonResponse(context)
                        except KeyError:
                            context = {'status': 0, 'message': '查无数据'}
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


#Es搜索接口
class GetEsSearchView(APIView):
    # get 请求
    def get(self, request):
        try:
            if request.session['username']:
                # 获取参数数据
                search = request.GET.get('search', '')
                if search:
                    x = models.Es()
                    y = x.search_all(index='my-index', type='test', reque=search)
                    context = {'status': 1, 'messages': x.data_despose(data=y)}
                    return JsonResponse(context)
                else:
                    x = models.Es()
                    # 传输給html的必须是一个字典
                    context = {'status': 1, 'messages': x.Get_data_all()}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#Es数据添加接口
class PostEsAddView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    y = models.Es()
                    tagname = request.POST.get('tagname', '')
                    # 判断tagname是否已有，若有则不能添加
                    print(type(tagname))
                    if not tagname:
                        context = {'status': 2, 'message': '名称不可为空'}
                        return JsonResponse(context)
                    res = y.Get_data_tagname(index='my-index', type='test', tagname=tagname)
                    if res == 'True':
                        # print("test")
                        context = {'status': 0, 'message': '该名称已存在，不可重复添加'}
                        return JsonResponse(context)
                    cpu = request.POST.get('cpu', '')
                    memory = request.POST.get('memory', '')
                    ip = request.POST.get('ip', '')
                    systemd_version = request.POST.get('systemd_version', '')
                    kernel_version = request.POST.get('kernel_version', '')
                    tag = request.POST.get('tag', '')
                    i_ip = request.POST.get('i_ip', '')
                    e_ip = request.POST.get('e_ip', '')
                    # e_ip为外网ip,i_ip为内网ip
                    if (i_ip or e_ip):
                        if (i_ip and e_ip):
                            ip = i_ip + "/" + e_ip
                        elif i_ip:
                            ip = i_ip
                        else:
                            ip = e_ip
                    space = request.POST.get('space', '')
                    notes = request.POST.get('notes', '')
                    cost = request.POST.get('cost', '0')
                    stats = request.POST.get('stats', '')
                    hostname = request.POST.get('hostname', '')
                    port = request.POST.get('port', '')
                    username = request.POST.get('username', '')
                    password = request.POST.get('password', '')
                    auth = request.POST.get('auth', '1')
                    sudo = request.POST.get('sudo', '1')
                    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

                    message = {'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip': ip,
                               'systemd_version': systemd_version,
                               'kernel_version': kernel_version, 'tag': tag, 'create_time': create_time, 'space': space,
                               'stats': stats,
                               'notes': notes, 'cost': cost, 'auth': auth , 'sudo':sudo , 'port':port ,
                               'hostname' : hostname , 'username' : username , 'password': password }
                    print(message)
                    y.Create_data(index='my-index', type='test', body=message)
                    context = {'status': 1, 'message': '添加成功'}
                    return JsonResponse(context)
                except KeyError:
                    context = {'status': 0, 'message': '添加失败，KeyError'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#Es数据更新接口,根据tagname
class PostEsEditView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                y = models.Es()
                tagname = request.POST.get('tagname', '')
                # 判断tagname是否已有，若有则不能添加
                if not tagname:
                    context = {'status': 2, 'message': '名称不可为空'}
                    return JsonResponse(context)
                res = y.Get_data_tagname(index='my-index', type='test', tagname=tagname)
                if res == 'True':
                    cpu = request.POST.get('cpu', '')
                    memory = request.POST.get('memory', '')
                    ip = request.POST.get('ip', '')
                    systemd_version = request.POST.get('systemd_version', '')
                    kernel_version = request.POST.get('kernel_version', '')
                    tag = request.POST.get('tag', '')

                    message = {'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip': ip,
                               'systemd_version': systemd_version,
                               'kernel_version': kernel_version, 'tag': tag}
                    print(message)
                    y.update_data_tagname(index='my-index', type='test', tagname=tagname, data=message)
                    context = {'status': 1, 'message': '数据已更新！'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#Es数据更新接口,根据id(更新基础数据)
class PostEsEditidView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                y = models.Es()
                id = request.POST.get('id', '')
                print(id)
                # 判断tagname是否已有，若有则不能添加
                if id:
                    tagname = request.POST.get('tagname', '')
                    cpu = request.POST.get('cpu', '')
                    memory = request.POST.get('memory', '')
                    ip = request.POST.get('ip', '')
                    systemd_version = request.POST.get('systemd_version', '')
                    kernel_version = request.POST.get('kernel_version', '')
                    tag = request.POST.get('tag', '')
                    stats = request.POST.get('stats', '')

                    space = request.POST.get('space', '')
                    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    update_username = request.POST.get('update_username', '')
                    notes = request.POST.get('notes', '')
                    cost = request.POST.get('cost', '0')

                    message = {'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip': ip,
                               'systemd_version': systemd_version,
                               'kernel_version': kernel_version, 'tag': tag, 'stats': stats, 'update_time': update_time,
                               'update_username': update_username, 'space': space, 'notes': notes, 'cost': cost}
                    print(id, message)
                    res = y.update_data(index='my-index', type='test', id=id, body=message)
                    print(res)
                    context = {'status': 1, 'message': '数据更新成功！'}
                    return JsonResponse(context)
                else:
                    context = {'status': 0, 'message': '数据更新失败！'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#Es数据更新接口,根据id(更新认证数据)
class PostEdiAuthView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                y = models.Es()
                id = request.POST.get('id', '')
                print(id)
                # 判断tagname是否已有，若有则不能添加
                if id:
                    hostname = request.POST.get('hostname', '')
                    port = request.POST.get('port', '')
                    username = request.POST.get('username', '')
                    password = request.POST.get('password', '')
                    execmd = request.POST.get('execmd', '')
                    sudo = request.POST.get('sudo', '')
                    auth = request.POST.get('auth', '1')

                    message = {'auth': auth, 'execmd': execmd, 'sudo': sudo, 'password': password,
                               'username': username, 'port': port, 'hostname': hostname}
                    print(id, message)
                    res = y.update_data(index='my-index', type='test', id=id, body=message)
                    print(res)
                    context = {'status': 1, 'message': '数据更新成功！'}
                    return JsonResponse(context)
                else:
                    context = {'status': 0, 'message': '数据更新失败！'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#Es数据删除接口，需要传入tagname，根据tagname删除
class PostEsDeleteView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    # 前端未接入，需要将数据的tagname传输过来，即可删除。目前写死
                    tagname = request.POST.get('tagname', '')
                    if tagname:
                        # tagname = 'nginx1'
                        y = models.Es()
                        y.Rm_data_tagname(index='my-index', type='test', tagname=tagname)
                        context = {'status': 1, 'message': '删除成功！', 'messages': tagname}
                        return JsonResponse(context)
                    else:
                        context = {'status': 0, 'message': '删除失败，未接收参数！', 'messages': tagname}
                        return JsonResponse(context)
                except KeyError:
                    context = {'status': 0, 'message': '删除失败！', 'messages': tagname}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#Es数据删除接口，需要传入id，根据id删除
class PostEsRmidView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    # 前端未接入，需要将数据的tagname传输过来，即可删除。目前写死
                    id = request.POST.get('id', '')
                    if id:
                        y = models.Es()
                        y.Rm_data(index='my-index', type='test', id=id)
                        context = {'status': 1, 'message': '删除成功！', 'messages': id}
                        return JsonResponse(context)
                    else:
                        context = {'status': 0, 'message': '删除失败，未接收参数！', 'messages': id}
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




