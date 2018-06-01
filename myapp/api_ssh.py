from myapp import models
from rest_framework.views import APIView
from django.http import JsonResponse

#远程执行命令接口
class PostSSHView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                hostname = request.POST.get('hostname', '')
                port = request.POST.get('port', '')
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                if (not hostname or not port or not username or not password):
                    context = {'status': 0, 'messages': '参数有误'}
                    return JsonResponse(context)
                # execmd = request.POST.get('execmd', '')
                # hostname = 'hqh-study-python.com'
                # port = 2222
                # username = 'admin'
                # password = '3XtgCvWliZJ7WdKJ1QrZ'
                # execmd = "cat /etc/redhat-release"
                execmd = 'cat /proc/cpuinfo| grep "processor"| wc -l'
                pty = models.SSH_passwd()
                ttt = pty.sshclient_execmd(hostname=hostname, port=port, username=username, password=password,
                                           execmd=execmd)
                context = {'status': 1, 'messages': ttt}
                return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)


#上次文件接口
class PostDetectView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                hostname = request.POST.get('hostname', '')
                port = request.POST.get('port', '')
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                auth = request.POST.get('auth', '1')
                sudo = request.POST.get('sudo', '1')
                if (not hostname or not port or not username or not password):
                    context = {'status': 0, 'messages': '输入有误'}
                    return JsonResponse(context)
                else:
                    local_path = r'C:\Users\Administrator\Desktop\cmdb\myapp\detect.sh'
                    remote_path = r'/tmp/detect.sh'
                    pty = models.SSH_passwd()
                    #上次脚本至服务器
                    ttt = pty.put_file(hostname=hostname, port=port, username=username, password=password,
                                       local_path=local_path, remote_path=remote_path)
                    execmd = 'sh /tmp/detect.sh'

                    ttx = pty.sshclient_execmd(hostname=hostname, port=port, username=username, password=password,
                                               execmd=execmd)
                    # shell返回为srt类型，需要转换为dict
                    # print(ttx)
                    # print(type(ttx))
                    # context = {'status': 1, 'messages': eval(ttx)}
                    # return JsonResponse(context)
                    ttp = eval(ttx)
                    ttp['auth'] = auth
                    if ( auth == '0' ) :
                        ttp['sudo'] = sudo
                        ttp['hostname'] = hostname
                        ttp['port'] = port
                        ttp['username'] = username
                        ttp['password'] = password
                        context = {'status': 1, 'messages': ttp }
                        return JsonResponse(context)
                    else:
                        context = {'status': 1, 'messages': ttp }
                        return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)







