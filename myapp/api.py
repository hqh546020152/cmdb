from myapp import models
from myapp import views

import json
import time
from rest_framework.views import APIView
from django.http import JsonResponse

#status使用布尔表达，0为错误，非0值为正确。

#测试API
class GetTestView(APIView):
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

#登录API
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
            context = {'status': 0, 'message': '用户不存在'}
            return JsonResponse(context)
        # 判断用户输入的密码与数据库保存密码是否一致
        elif passwd == tty[0].passwd:
            print(usrname)

            request.session['username'] = usrname
            request.session.set_expiry(1800)
            print(request.session['username'])
            print(request.session.exists('usrname'))
            # print(type(ttx))
            context = {'status': 1, 'message': '登录成功'}
            return JsonResponse(context)
        else:
            context = {'status': 0, 'message': '密码错误'}
            return JsonResponse(context)

#注销API
# class GetLogoutView(APIView):
#     def get(self, request):
#         print("test")
#         username = request.GET.get('username', '')
#         try:
#             del request.session['username']
#             context = {'status': 1 ,'message': '请重新登录'}
#             return JsonResponse(context)
#         except KeyError:
#             return JsonResponse(context)



#Es数据查询API，如传入ID无，则报错。id=all则返回所有数据
class PostEsSelectView(APIView):
    def post(self, request):
        # 获取参数数据
        id = request.POST.get('id','')
        # print(id)
        if id :
            if id == "all":
                x = models.Es()
                context = {'status': 1,'messages': x.Get_data_all()}
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

#Es搜索接口
class GetEsSearchView(APIView):
    # get 请求
    def get(self, request):
        # 获取参数数据
        search = request.GET.get('search','')
        if search:
            x = models.Es()
            y = x.search_all(index='my-index', type='test', reque=search)
            context = {'status': 1,'messages': x.data_despose(data=y)}
            return JsonResponse(context)
        else:
            x = models.Es()
            # 传输給html的必须是一个字典
            context = {'status': 1,'messages': x.Get_data_all()}
            return JsonResponse(context)
#Es数据添加接口
class PostEsAddView(APIView):
    def post(self, request):
        try:
            y = models.Es()
            tagname = request.POST.get('tagname', '')
            # 判断tagname是否已有，若有则不能添加
            if not tagname:
                context = {'status': 2, 'message': '名称不可为空'}
                return JsonResponse(context)
            res = y.Get_data_tagname(index='my-index', type='test', tagname=tagname)
            if res == 'True':
                context = {'status': 0,'message': '该名称已存在，不可重复添加'}
                return JsonResponse(context)

            cpu = request.POST.get('cpu', '')
            memory = request.POST.get('memory', '')
            ip = request.POST.get('ip', '')
            systemd_version = request.POST.get('systemd_version', '')
            kernel_version = request.POST.get('kernel_version', '')
            tag = request.POST.get('tag', '')
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            message = {'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip': ip, 'systemd_version': systemd_version,
                       'kernel_version': kernel_version, 'tag': tag, 'create_time': create_time, 'status': 0}
            print(message)
            y.Create_data(index='my-index', type='test', body=message)
            context = {'status': 1, 'message': '添加成功'}
            return JsonResponse(context)
        except KeyError:
            context = {'status': 0, 'message': '添加失败，KeyError'}
            return JsonResponse(context)

#Es数据更新接口,根据tagname
class PostEsEditView(APIView):
    def post(self, request):
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
            context = {'status': 1,'message': '数据已更新！'}
            return JsonResponse(context)

#Es数据更新接口,根据id
class PostEsEditidView(APIView):
    def post(self, request):
        y = models.Es()
        id = request.POST.get('id', '')
        print(id)
        # 判断tagname是否已有，若有则不能添加
        if id :
            tagname = request.POST.get('tagname', '')
            cpu = request.POST.get('cpu', '')
            memory = request.POST.get('memory', '')
            ip = request.POST.get('ip', '')
            systemd_version = request.POST.get('systemd_version', '')
            kernel_version = request.POST.get('kernel_version', '')
            tag = request.POST.get('tag', '')
            status = request.POST.get('status', '')
            message = {'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip': ip,
                       'systemd_version': systemd_version,
                       'kernel_version': kernel_version, 'tag': tag , 'status': status }
            print(id,message)
            res = y.update_data(index='my-index', type='test',id=id , body=message)
            print(res)
            context = {'status': 1,'message': '数据更新成功！'}
            return JsonResponse(context)
        else:
            context = {'status': 0, 'message': '数据更新失败！'}
            return JsonResponse(context)


#Es数据删除接口，需要传入tagname，根据tagname删除
class PostEsDeleteView(APIView):
    def post(self, request):
        try:
            # 前端未接入，需要将数据的tagname传输过来，即可删除。目前写死
            tagname = request.POST.get('tagname', '')
            if tagname :
            # tagname = 'nginx1'
                y = models.Es()
                y.Rm_data_tagname(index='my-index', type='test', tagname=tagname)
                context = {'status': 1,'message': '删除成功！', 'messages': tagname}
                return JsonResponse(context)
            else:
                context = {'status': 0, 'message': '删除失败，未接收参数！', 'messages': tagname}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 0, 'message': '删除失败！', 'messages': tagname}
            return JsonResponse(context)

#Es数据删除接口，需要传入id，根据id删除
class PostEsRmidView(APIView):
    def post(self, request):
        try:
            # 前端未接入，需要将数据的tagname传输过来，即可删除。目前写死
            id = request.POST.get('id', '')
            if id :
                y = models.Es()
                y.Rm_data(index='my-index', type='test', id=id)
                context = {'status': 1,'message': '删除成功！', 'messages': id}
                return JsonResponse(context)
            else:
                context = {'status': 0, 'message': '删除失败，未接收参数！', 'messages': id}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 0, 'message': '删除失败！', 'messages': id}
            return JsonResponse(context)


#用户增删查改接口
class PostUserAddView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        # 判断用户是否已存在
        tty = models.DUser.objects.filter(user=(username))
        try:
            if tty[0].user == username:
                context = {'status': 0,'message': '该用户已存在，请重新输入！', 'messages': username}
                return JsonResponse(context)
            # 用户不存在时会报错
        except IndexError:
            # 密码MD5转换
            passwd = request.POST.get('passwd')
            x = models.Change_md5()
            x.setName(passwd)
            passwd = x.data

            status = request.POST.get('status')
            permissions = request.POST.get('permissions')

            print(username, passwd, status, permissions)
            # 添加数据
            models.DUser.objects.create(id='3', user=(username), passwd=(passwd), valid=(status), permission=(permissions))
            obj = models.DUser(id='3', user=(username), passwd=(passwd), valid=(status), permission=(permissions))
            obj.save()
            context = {'status': 1,'message': '添加成功！', 'messages': username}
            return JsonResponse(context)

#用户详情查询接口，未开发
# class PostUserSelectView(APIView):

#修改用户信息接口，修改密码
class PostUserAlterView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        passwd1 = request.POST.get('passwd1')
        passwd2 = request.POST.get('passwd2')
        if passwd1 != passwd2:
            context = {'status': 0,'message': '输入两次密码不一致，请重新输入！'}
            return JsonResponse(context)
        elif passwd1 == passwd:
            context = {'status': 0,'message': '修改密码与原密码一直，修改失败！'}
            return JsonResponse(context)
        else:
            x = models.Change_md5()
            x.setName(passwd1)
            passwd = x.data
            models.DUser.objects.filter(user=(username)).update(passwd=(passwd))
            context = {'status': 1,'message': '修改成功！'}
            return JsonResponse(context)

#删除用户接口，根据传入用户名称进行删除
class PostUserDeleteView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        tty = models.DUser.objects.filter(user=(username))
        try:
            if tty[0].user:
                models.DUser.objects.filter(user=(username)).delete()
                context = {'status': 1,'message': '删除成功！', 'messages': username}
                return JsonResponse(context)
            # 用户不存在时会报错
        except IndexError:
            context = {'status': 0,'message': '该用户不存在，删除！', 'messages': username}
            return JsonResponse(context)

#用户搜索接口，未开发
# class PostUserSearchView(APIView):


