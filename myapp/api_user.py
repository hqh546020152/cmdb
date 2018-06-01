from myapp import models
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

#登录API
class GetLoginView(APIView):
    queryset = models.DUser.objects.all()
    permission_classes = (AllowAny,)
    def post(self, request):
        # 获取参数数据
        usrname = request.POST.get('username', '')
        passwd = request.POST.get('passwd', '')
        # received_json_data = json.loads(request.body)
        # print(received_json_data)
        # req = request.raw_post_data
        # print(req)
        try:
            real_ip = request.META['HTTP_X_FORWARDED_FOR']
            regip = real_ip.split(",")[0]
        except:
            try:
                regip = request.META['REMOTE_ADDR']
            except:
                regip = ""
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
            request.session.set_expiry(6000)
            print("客户端登陆IP", regip)
            print("客户端登陆用户", usrname)
            context = {'status': 1, 'message': '登录成功'}
            return JsonResponse(context)
        else:
            context = {'status': 2, 'message': '密码错误'}
            return JsonResponse(context)

#注销API
class GetLogoutView(APIView):
    def get(self, request):
        username = request.GET.get('username', '')
        try:
            del request.session['username']
            context = {'status': 1 ,'message': '请重新登录'}
            return JsonResponse(context)
        except KeyError:
            return JsonResponse(context)


#获取用户列表（返回除密码外的所有数据）
class PostUserGainView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                tty = models.DUser.objects.all()
                sumshu = []
                for I in range(len(tty)):
                    message = { 'user': tty[I].user,
                                'permission': tty[I].permission,
                                'valid': tty[I].valid
                              }
                    sumshu.append(message)
                context = {'status': 1, 'messages': sumshu }
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!' }
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!' }
            return JsonResponse(context)

#用户添加接口
class PostUserAddView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                username = request.POST.get('username', '')
                passwd = request.POST.get('passwd', '')
                # 判断用户是否已存在
                tty = models.DUser.objects.filter(user=(username))
                if not username:
                    context = {'status': 2, 'message': '用户名不可为空'}
                    return JsonResponse(context)
                if not passwd:
                    context = {'status': 3, 'message': '密码不可为空'}
                    return JsonResponse(context)
                try:
                    if tty[0].user == username:
                        context = {'status': 0, 'message': '该用户已存在，请重新输入！', 'messages': username}
                        return JsonResponse(context)
                    # 用户不存在时会报错
                except IndexError:
                    # 密码MD5转换
                    x = models.Change_md5()
                    x.setName(passwd)
                    passwd = x.data

                    status = request.POST.get('status', '0')
                    permissions = request.POST.get('permissions', '0')

                    # print(username, passwd, status, permissions)
                    # 添加数据
                    models.DUser.objects.create(id='3', user=(username), passwd=(passwd), valid=(status),
                                                permission=(permissions))
                    # obj = models.DUser(id='3', user=(username), passwd=(passwd), valid=(status), permission=(permissions))
                    # obj.save()
                    context = {'status': 1, 'message': '添加成功！', 'messages': username}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#用户详情查询接口，未开发
# class PostUserSelectView(APIView):

#修改用户信息接口（包含密码）
class PostUserAlterView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                username = request.POST.get('username', '')
                passwd = request.POST.get('passwd', '')
                passwd1 = request.POST.get('passwd1', '')
                passwd2 = request.POST.get('passwd2', '')
                status = request.POST.get('status', '0')
                permission = request.POST.get('permission', '0')
                tty = models.DUser.objects.filter(user=(username))

                # 加密传输过来的原有密码，与数据库中信息做匹配
                x = models.Change_md5()
                x.setName(passwd)
                passwdts = x.data

                print("test")
                if not username:
                    context = {'status': 1, 'message': '用户名不许为空!'}
                    return JsonResponse(context)
                elif not passwd:
                    context = {'status': 5, 'message': '原密码为空!'}
                    return JsonResponse(context)
                elif passwd1 != passwd2:
                    context = {'status': 2, 'message': '输入两次密码不一致，请重新输入！'}
                    return JsonResponse(context)
                elif (passwd and passwd1):
                    if (passwd == passwd1):
                        context = {'status': 3, 'message': '修改密码与原密码一致，修改失败！'}
                        return JsonResponse(context)
                    elif (passwdts != tty[0].passwd):
                        context = {'status': 4, 'message': '原密码不正确，修改失败！'}
                        return JsonResponse(context)
                    else:
                        x.setName(passwd1)
                        passwden = x.data
                        models.DUser.objects.filter(user=(username)).update(passwd=(passwden))
                        models.DUser.objects.filter(user=(username)).update(valid=(status))
                        models.DUser.objects.filter(user=(username)).update(permission=(permission))
                        context = {'status': 0, 'message': '修改信息及密码成功！'}
                        return JsonResponse(context)
                else:
                    models.DUser.objects.filter(user=(username)).update(valid=(status))
                    models.DUser.objects.filter(user=(username)).update(permission=(permission))
                    context = {'status': 0, 'message': '修改信息成功！'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#修改用户修改密码接口(用于用户自助修改密码使用)
class PostUserAlterPasswdView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                username = request.POST.get('username')
                passwd = request.POST.get('passwd')
                passwd1 = request.POST.get('passwd1')
                passwd2 = request.POST.get('passwd2')
                if passwd1 != passwd2:
                    context = {'status': 0, 'message': '输入两次密码不一致，请重新输入！'}
                    return JsonResponse(context)
                elif passwd1 == passwd:
                    context = {'status': 0, 'message': '修改密码与原密码一直，修改失败！'}
                    return JsonResponse(context)
                else:
                    x = models.Change_md5()
                    x.setName(passwd1)
                    passwd = x.data
                    models.DUser.objects.filter(user=(username)).update(passwd=(passwd))
                    context = {'status': 1, 'message': '修改成功！'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#删除用户接口，根据传入用户名称进行删除
class PostUserDeleteView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                username = request.POST.get('username')
                tty = models.DUser.objects.filter(user=(username))
                try:
                    if tty[0].user:
                        models.DUser.objects.filter(user=(username)).delete()
                        context = {'status': 1, 'message': '删除成功！', 'messages': username}
                        return JsonResponse(context)
                    # 用户不存在时会报错
                except IndexError:
                    context = {'status': 0, 'message': '该用户不存在，删除！', 'messages': username}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)

#用户搜索接口，未开发
# class PostUserSearchView(APIView):


