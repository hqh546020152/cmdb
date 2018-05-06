from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
#载入应用的models
from myapp import models
import time
import json

from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.

#检查用户的session是否过期，过期则让其重新登录
def session_check(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/index.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#注销功能，删除其session
def logout(request):
    try:
        del request.session['username']
        context = {'logout_messages':'请重新登录'}
    except KeyError:
        pass
    return render(request, "login/login.html" , context)

#注销功能，删除其session
def login(request):
    return render(request, "login/index.html")

#登录认证、验证其登录信息是否正确
def login_auth(request):
    #只接受POST请求
    try:
        if request.method == "POST":
            #获取用户输入的信息
            usrname = request.POST.get('username', '')
            passwd = request.POST.get('passwd', '')

            #将密码转化为MD5格式
            x = models.Change_md5()
            x.setName(passwd)
            passwd = x.data

            #过滤查询用户输入的用户，返回类型列表
            tty = models.DUser.objects.filter(user=(usrname))
            if not tty:
                # 下列值将给前端使用
                context = {'error_id': 1, 'error': '用户不存在'}
                return render(request, "login/login.html", context)
            # 判断用户输入的密码与数据库保存密码是否一致
            elif passwd == tty[0].passwd:
                request.session['username'] = usrname
                request.session.set_expiry(1800)
                x = models.Es()
                #传输給html的必须是一个字典
                context = {'messages': x.Get_data_all()}
                return render(request, "cmdb/index.html" , context)
            else:
                print('密码错误')
                context = {'error_id':2, 'error': '密码错误'}
                return render(request, "login/login.html", context)
        else:
            return render(request, "login/login.html")
    except ValueError:
        return render(request, "login/login.html")

#用户管理信息界面渲染
def user_manage(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/user.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#主页渲染，用户其他页面操作返回后将验证其session是否过期
def index_return(request):
    try:
        if request.session['username']:
            x = models.Es()
            # 传输給html的必须是一个字典
            context = {'messages': x.Get_data_all()}
            return render(request, "cmdb/index.html", context)
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#服务器资产信息添加界面渲染
def data_add(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/data_add.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#服务器资产信息查看界面渲染
def data_look(request):
    try:
        if request.session['username']:
            #从前端传来一个值-欠缺;从前端传输回来某条数据的id
            appip = '3'
            y = models.Es()
            res = y.Get_data(index='my-index', type='test', id= appip)
            context = { 'messages':json.dumps(res) }
            return render(request, "cmdb/data_look.html" ,context)
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#服务器资产信息修改界面渲染
def data_alter(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/data_alter.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

#服务器资产信息删除界面渲染
def data_delete(request):
    try:
        if request.session['username']:
            #前端未接入，需要将数据的tagname传输过来，即可删除。目前写死
            tagname = 'nginx1'
            y = models.Es()
            y.Rm_data_tagname(index='my-index', type='test', tagname=tagname)
            context = {'messages': '删除成功！', 'messages_tagname': tagname }
            return render(request, "cmdb/data_delete.html",context)
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")


#获取用户填写信息，并数据提交給models进行处理
def add_message(request):
    try:
        if request.method == "POST":
            y = models.Es()
            tagname = request.POST.get('tagname', '')
            #判断tagname是否已有，若有则不能添加
            res = y.Get_data_tagname(index='my-index', type='test', tagname = tagname)
            if res == 'True':
                context = { 'add_messages' : '该名称已存在，不可重复添加' }
                return render(request, "cmdb/data_add.html",context)

            cpu = request.POST.get('cpu', '')
            memory = request.POST.get('memory', '')
            ip = request.POST.get('ip', '')
            systemd_version = request.POST.get('systemd_version', '')
            kernel_version = request.POST.get('kernel_version', '')
            tag = request.POST.get('tag', '')
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            message = { 'cpu': cpu, 'tagname': tagname, 'memory': memory, 'ip':ip, 'systemd_version':systemd_version, 'kernel_version': kernel_version, 'tag' : tag , 'create_time' : create_time , 'status' : 0 }
            # print(message)
            y.Create_data(index='my-index', type='test', body = message)
            return render(request, "cmdb/data_add.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

def user_alter(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/user_alter.html")
        else:
            return render(request, "login/index.html")
    except KeyError:
        return render(request, "login/index.html")


def user_add(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/user_add.html")
        else:
            return render(request, "login/index.html")
    except KeyError:
        return render(request, "login/index.html")


def user_add_get(request):
    username = request.POST.get('username')

    #判断用户是否已存在
    tty = models.DUser.objects.filter(user=(username))
    try:
        if tty[0].user == username:
            context = {'messages': '该用户已存在，请重新输入！', 'messages_tagname': username}
            return render(request, "cmdb/user_add.html", context)
        #用户不存在时会报错
    except IndexError:
        #密码MD5转换
        passwd = request.POST.get('passwd')
        x = models.Change_md5()
        x.setName(passwd)
        passwd = x.data

        status = request.POST.get('status')
        permissions = request.POST.get('permissions')

        print(username,passwd,status,permissions)
        #添加数据
        models.DUser.objects.create(id='3',user=(username), passwd=(passwd), valid=(status), permission=(permissions))
        obj = models.DUser(id='3', user=(username), passwd=(passwd), valid=(status), permission=(permissions))
        obj.save()


        context = {'messages': '添加成功！', 'messages_tagname': username}
        return render(request, "cmdb/user_add.html",context)


def user_add_alter(request):
    username = request.POST.get('username')
    passwd = request.POST.get('passwd')
    passwd1 = request.POST.get('passwd1')
    passwd2 = request.POST.get('passwd2')
    if passwd1 != passwd2:
        context = {'messages': '输入两次密码不一致，请重新输入！'}
        return render(request, "cmdb/user_alter.html",context)
    elif passwd1 == passwd:
        context = {'messages': '修改密码与原密码一直，修改失败！'}
        return render(request, "cmdb/user_alter.html", context)
    else:
        x = models.Change_md5()
        x.setName(passwd1)
        passwd = x.data
        models.DUser.objects.filter(user=(username)).update(passwd=(passwd))
        context = {'messages': '修改成功！'}
        return render(request, "cmdb/user_alter.html", context)

def user_delete(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/user_delete.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")

def user_add_delete(request):
    if request.method == "POST":
        username = request.POST.get('username')
        tty = models.DUser.objects.filter(user=(username))
        try:
            if tty[0].user :
                models.DUser.objects.filter(user=(username)).delete()
                context = {'messages': '删除成功！', 'messages_tagname': username}
                return render(request, "cmdb/user_delete.html", context)
            # 用户不存在时会报错
        except IndexError:
            context = {'messages': '该用户不存在，删除！', 'messages_tagname': username}
            return render(request, "cmdb/user_delete.html",context)

def data_search(request):
    search = request.GET.get('search','')
    if search :
        x = models.Es()
        y = x.search_all(index='my-index', type='test', reque = search )
        context = {'messages': x.data_despose( data=y ) }
        return render(request, "cmdb/index.html", context)
    else:
        x = models.Es()
        # 传输給html的必须是一个字典
        context = {'messages': x.Get_data_all()}
        return render(request, "cmdb/index.html", context)




def test(request):
    try:
        if request.session['username']:
            return render(request, "cmdb/test.html")
        else:
            return render(request, "login/login.html")
    except KeyError:
        return render(request, "login/login.html")


def ssh(request):

    hostname = 'hqh-study-python.com'
    port = 2222
    username = 'admin'
    password = '3XtgCvWliZJ7WdKJ1QrZ'
    execmd = "cat /etc/redhat-release"

    pty = models.SSH_passwd()
    ttt = pty.sshclient_execmd(hostname = hostname,port = port , username = username , password = password , execmd = execmd )
    print(ttt)
    x = models.Es()
    # 传输給html的必须是一个字典
    context = {'messages': x.Get_data_all()}
    return render(request, "cmdb/index.html", context)

#接口Dome
#参考：https://www.jianshu.com/p/9064ffe0f720



# class GetMessageView(APIView):
#     # get 请求
#     def get(self, request):
#         # 获取参数数据
#         a = request.GET.get('a','')
#         b = request.GET.get('b','')
#         print(a,b)
#         if a :
#         # 返回信息
#             d = {
#                 'status': 1,
#                 'message': 'success',
#                 }
#             return JsonResponse(d)
#         else:
#             d = {
#                 'status': 0,
#                 'message': 'error',
#             }
#             return JsonResponse(d)


# class GetLoginView(APIView):
#     # get 请求
#     def get(self, request):
#         # 获取参数数据
#         a = request.GET.get
#         if a :
#         # 返回信息
#             d = {
#                 'status': 1,
#                 'message': 'success',
#                 }
#             return JsonResponse(d)
#         else:
#             d = {
#                 'status': 0,
#                 'message': 'error',
#             }
#             return JsonResponse(d)


