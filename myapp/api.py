from myapp import models
from myapp import views

import json
from rest_framework.views import APIView
from django.http import JsonResponse

class GetMessageView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        a = request.GET.get('a','')
        b = request.GET.get('b','')
        print(a,b)
        if a :
        # 返回信息
            d = {'status': 1,'message': 'success',}
            return JsonResponse(d)
        else:
            d = {'status': 0,'message': 'error',}
            return JsonResponse(d)

class GetLoginView(APIView):
    # get 请求
    def post(self, request):
        # 获取参数数据
        # usrname = requestge.GET.get('username', '')
        # passwd = request.GET.t('passwd', '')
        usrname = request.POST.get('username', '')
        passwd = request.POST.get('passwd', '')

        x = models.Change_md5()
        x.setName(passwd)
        passwd = x.data

        tty = models.DUser.objects.filter(user=(usrname))
        if not tty:
            # 下列值将给前端使用
            context = {'status': 1, 'message': '用户不存在'}
            return JsonResponse(context)
        # 判断用户输入的密码与数据库保存密码是否一致
        elif passwd == tty[0].passwd:
            # request.session['username'] = usrname
            # request.session.set_expiry(1800)
            # x = models.Es()
            # context = {'status': 0,'messages': x.Get_data_all()}
            context = {'status': 0, 'message': '登录成功'}
            return JsonResponse(context)
        else:
            context = {'status': 2, 'message': '密码错误'}
            return JsonResponse(context)


class GetSelectView(APIView):
    def post(self, request):
        # 获取参数数据
        id = request.POST.get('id','')
        print(id)
        if id :
            if id == "all":
                x = models.Es()
                context = {'status': 0,'messages': x.Get_data_all()}
                return JsonResponse(context)
            else:
                try:
                    y = models.Es()
                    res = y.Get_data(index='my-index', type='test', id=id)
                    context = {'messages': json.dumps(res)}
                    return JsonResponse(context)
                except KeyError:
                    context = {'status': 1, 'message': '查无数据'}
                    return JsonResponse(context)
        else:
            context = {'status': 1, 'message': '查无数据'}
            return JsonResponse(context)


