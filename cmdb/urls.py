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

urlpatterns = [
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
    # url(r'^test/$', views.GetMessageView.as_view(), name='GetMessageView'),


    url(r'^api/test/$', api.GetTestView.as_view(), name='GetMessageView'),
    url(r'^api/login/$',api.GetLoginView.as_view(), name='GetLoginViewView'),
    #url(r'^api/logout/$',api.GetLogoutView.as_view(), name='GetLogoutView'),
    url(r'^api/es-select/$',api.PostEsSelectView.as_view(), name='PostEsSelectView'),
    url(r'^api/es-search/$',api.GetEsSearchView.as_view(), name='GetEsSearchView'),
    url(r'^api/es-add/$',api.PostEsAddView.as_view(), name='PostEsAddView'),
    url(r'^api/es-delete/$',api.PostEsDeleteView.as_view(), name='PostEsDeleteView'),
    url(r'^api/es-delete-id/$',api.PostEsRmidView.as_view(), name='PostEsRmidView'),
    url(r'^api/es-update/$',api.PostEsEditView.as_view(), name='PostEsEditView'),
    url(r'^api/es-update-id/$',api.PostEsEditidView.as_view(), name='PostEsEditidView'),

    url(r'^api/user-add/$',api.PostUserAddView.as_view(), name='PostUserAddView'),
    url(r'^api/user-alter/$',api.PostUserAlterView.as_view(), name='PostUserAlterView'),
    url(r'^api/user-alter-passwd/$',api.PostUserAlterPasswdView.as_view(), name='PostUserAlterPasswdView'),
    url(r'^api/user-delete/$',api.PostUserDeleteView.as_view(), name='PostUserDeleteView'),
    url(r'^api/user-gain/$',api.PostUserGainView.as_view(), name='PostUserGainView'),
    # url(r'^api/user-add/$',api.PostUserAddView.as_view(), name='PostUserAddView'),



]
