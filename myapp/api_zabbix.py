from myapp import models_zabbix
from rest_framework.views import APIView
from django.http import JsonResponse

#Zabbix官方接口文档：https://www.zabbix.com/documentation/3.2/manual/api
#获取全部已接入Zabbix主机信息接口
class PostZbSelectView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                #逻辑处理部分
                id = request.POST.get('id', '')
                if id:
                    if id == "all":
                        x = models_zabbix.Zabbix()
                        length = len(x.Get_data())
                        context = {'status': 1, 'messages': x.Get_data(), 'length' : length }
                        return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#获取所有组群及ID接口
class PostZbGroupView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                x = models_zabbix.Zabbix()
                length = len(x.Get_group())
                context = {'status': 1, 'messages': x.Get_group(), 'length': length}
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#获取模板及ID 接口
class PostZbTempView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                x = models_zabbix.Zabbix()
                length = len(x.Get_templateID())
                context = {'status': 1, 'messages': x.Get_templateID(), 'length': length}
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)
#添加Zabbix主机接口
class PostZbAddView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                name = request.POST.get('name', '')
                ip = request.POST.get('ip', '')
                port = request.POST.get('port', '10050')
                groupid = request.POST.get('groupid', '')
                templateid = request.POST.get('templateid', '')
                if (not name or not port or not ip or not groupid):
                    context = {'status': 0, 'messages': '输入有误'}
                    return JsonResponse(context)
                else:
                    x = models_zabbix.Zabbix()
                    if templateid:
                        templateid_list = templateid.strip(',').split(',')
                    else:
                        templateid_list = []
                    print(name,ip,port,groupid,templateid_list)
                    #此处传入的templateid还未处理
                    y = x.Create_host(name=name,ip=ip,port=port,groupid=groupid,templateid=templateid_list)
                    if y:
                        context = {'status': 1, 'messages': y }
                    else:
                        context = {'status': 2, 'messages': "This data cannot be added to Zabbix"}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#删除Zabbix主机接口
class PostZbDelView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                hostid = request.POST.get('hostid', '')
                if hostid:
                    #此处需要把hostid转化为数组类型，再去调用函数
                    hostid_list = hostid.strip(',').split(',')
                    x = models_zabbix.Zabbix()
                    y = x.Del_host(hostid=hostid_list)
                    if y:
                        context = {'status': 1, 'messages': y}
                    else:
                        context = {'status': 2, 'messages': "This data cannot be added to Zabbix"}
                    return JsonResponse(context)
                else:
                    context = {'status': 0, 'messages': '输入有误'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

