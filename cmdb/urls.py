"""cmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url ,include

#引入myapp应用的渲染
from myapp import views
from myapp import api
from myapp import api_task,api_user,api_es,api_ssh,api_env,api_zabbix

urlpatterns = [
    #前后端未分离使用的路由
    path('admin/', admin.site.urls),
    #path('login/index/', views.login, name='index'),
    url(r'^login/index/', views.login, name='login'),
    url(r'^login/logout/', views.logout, name='logout'),
    url(r'^login/login/', views.session_check, name='login_check'),
    
    url(r'^cmdb/index/', views.login_auth, name='login_auth'),
    url(r'^cmdb/index_return/', views.index_return, name='index_return'),
    url(r'^cmdb/data_add/', views.data_add, name='data_add'),
    url(r'^cmdb/data_look/', views.data_look, name='data_look'),
    url(r'^cmdb/data_alter/', views.data_alter, name='data_alter'),
    url(r'^cmdb/data_delete/', views.data_delete, name='data_delete'),
    url(r'^cmdb/add_message/', views.add_message, name='add_message'),
    url(r'^cmdb/data_search/', views.data_search, name='data_search'),

    url(r'^cmdb/user/', views.user_manage, name='user_manage'),
    url(r'^cmdb/user_add/', views.user_add, name='user_add'),
    url(r'^cmdb/user_alter/', views.user_alter, name='user_alter'),
    url(r'^cmdb/user_add_get/', views.user_add_get, name='user_add_get'),
    url(r'^cmdb/user_add_alter/', views.user_add_alter, name='user_add_alter'),
    url(r'^cmdb/user_delete/', views.user_delete, name='user_delete'),
    url(r'^cmdb/user_add_delete/', views.user_add_delete, name='user_add_delete'),
    url(r'^cmdb/test/', views.test, name='test'),

    #API接口测试路由
    url(r'^api/test/$', api.GetTestView.as_view(), name='GetMessageView'),

    #服务器资源相关路由
    url(r'^api/es-select/$',api_es.PostEsSelectView.as_view(), name='PostEsSelectView'),
    url(r'^api/es-search/$',api_es.GetEsSearchView.as_view(), name='GetEsSearchView'),
    url(r'^api/es-add/$',api_es.PostEsAddView.as_view(), name='PostEsAddView'),
    url(r'^api/es-delete/$',api_es.PostEsDeleteView.as_view(), name='PostEsDeleteView'),
    url(r'^api/es-delete-id/$',api_es.PostEsRmidView.as_view(), name='PostEsRmidView'),
    url(r'^api/es-update/$',api_es.PostEsEditView.as_view(), name='PostEsEditView'),
    url(r'^api/es-update-id/$',api_es.PostEsEditidView.as_view(), name='PostEsEditidView'),
    url(r'^api/es-update-auth/$',api_es.PostEdiAuthView.as_view(), name='PostEdiAuthView'),


    #用户操作相关路由
    url(r'^api/login/$',api_user.GetLoginView.as_view(), name='GetLoginViewView'),
    url(r'^api/logout/$',api_user.GetLogoutView.as_view(), name='GetLogoutView'),
    url(r'^api/user-add/$',api_user.PostUserAddView.as_view(), name='PostUserAddView'),
    url(r'^api/user-alter/$',api_user.PostUserAlterView.as_view(), name='PostUserAlterView'),
    url(r'^api/user-alter-passwd/$',api_user.PostUserAlterPasswdView.as_view(), name='PostUserAlterPasswdView'),
    url(r'^api/user-delete/$',api_user.PostUserDeleteView.as_view(), name='PostUserDeleteView'),
    url(r'^api/user-gain/$',api_user.PostUserGainView.as_view(), name='PostUserGainView'),

    #待办事项功能相关路由
    url(r'^api/es-task-add/$', api_task.PostTaskAddView.as_view(), name='PostTaskAddView'),
    url(r'^api/es-task-select/$', api_task.PostTaskSelectView.as_view(), name='PostTaskSelectView'),
    url(r'^api/es-task-delete-id/$', api_task.PostTaskRmidView.as_view(), name='PostTaskRmidView'),

    #ssh相关路由
    url(r'^api/ssh-extract/$', api_ssh.PostSSHView.as_view(), name='PostSSHView'),
    url(r'^api/ssh-detect/$', api_ssh.PostDetectView.as_view(), name='PostDetectView'),

    #批处理相关路由
    url(r'^api/auth-select/$', api_env.PostAutoSelectView.as_view(), name='PostAutoSelectView'),
    url(r'^api/script-select/$', api_env.PostSelectScriptView.as_view(), name='PostSelectScriptView'),
    url(r'^api/script-add/$', api_env.PostAddScriptView.as_view(), name='PostAddScriptView'),
    url(r'^api/script-del/$', api_env.PostDelScriptView.as_view(), name='PostDelScriptView'),
    url(r'^api/execute-script/$', api_env.PostExecuteView.as_view(), name='PostExecuteView'),

    #Zabbix相关路由
    url(r'^api/zabbix-select/$', api_zabbix.PostZbSelectView.as_view(), name='PostZbSelectView'),
    url(r'^api/zabbix-add/$', api_zabbix.PostZbAddView.as_view(), name='PostZbAddView'),
    url(r'^api/zabbix-del/$', api_zabbix.PostZbDelView.as_view(), name='PostZbDelView'),
    url(r'^api/zabbix-group/$', api_zabbix.PostZbGroupView.as_view(), name='PostZbGroupView'),
    url(r'^api/zabbix-temp/$', api_zabbix.PostZbTempView.as_view(), name='PostZbTempView'),


]
