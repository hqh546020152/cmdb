from myapp import models
from myapp import views

import json
import time
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class PostTaskSelectView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                # 获取参数数据
                id = request.POST.get('id', '')
                # print(id)
                if id:
                    if id == "all":
                        x = models.Es()
                        context = {'status': 1, 'messages': x.Get_data_all(index='my-task', type='task')}
                        return JsonResponse(context)
                    else:
                        try:
                            y = models.Es()
                            res = y.Get_data(index='my-task', type='task', id=id)
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


class PostTaskAddView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    y = models.Es()
                    task = request.POST.get('task', '')
                    # 判断tagname是否已有，若有则不能添加
                    if not task:
                        context = {'status': 2, 'message': '任务不可为空'}
                        return JsonResponse(context)
                    res = y.Get_data_tagname(index='my-task', type='task', tagname=task)
                    if res == 'True':
                        context = {'status': 0, 'message': '任务已存在，不需要重复添加'}
                        return JsonResponse(context)

                    status = request.POST.get('status', '')
                    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                    message = {'status': status, 'task': task, 'create_time': create_time}
                    print(message)
                    y.Create_data(index='my-task', type='task', body=message)
                    print("test")
                    context = {'status': 1, 'message': '添加成功'}
                    return JsonResponse(context)
                except KeyError:
                    context = {'status': 3, 'message': '添加失败，KeyError'}
                    return JsonResponse(context)
            else:
                context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
                return JsonResponse(context)
        except KeyError:
            context = {'status': 7, 'messages': '会话已失效，请重新登录!'}
            return JsonResponse(context)



#Es-task数据删除接口，需要传入id，根据id删除
class PostTaskRmidView(APIView):
    def post(self, request):
        try:
            if request.session['username']:
                try:
                    id = request.POST.get('id', '')
                    if id:
                        y = models.Es()
                        y.Rm_data(index='my-task', type='task', id=id)
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
