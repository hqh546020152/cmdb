from elasticsearch import Elasticsearch
# import urllib
# import urllib2
import json
import time
import datetime
from myapp import models



#过滤查询用户输入的用户，返回类型列表
usrname = "test"
tty = models.DUser.objects.filter(user=(usrname))
# tty = models.DUser.objects.all()
print(tty)




es = Elasticsearch(['hqh-study-python.com:9298'])
if es.indices.exists(index='my-index') is not True:
    es.indices.create(index='my-index')


# a = es.get(index='my-index', doc_type='test', id=2)
# print(a)

#获取所有数据，并加以解析打印出来
# res = es.search(index='my-index', doc_type='test', body={"query":{"match_all":{}}})
# print(res)
# sumshu = []
# # cont = []
# total = res['hits']['total']
# print(total)
# for hit in res['hits']['hits']:
#     id_data = hit['_id']
#     print(id_data)
#     ptk = hit['_source']
#     ptk['id'] = id_data
#     print(ptk)
#     sumshu.append(ptk)
    # print(hit['_source'])

#查询指定数据 => 查看详情单条数据
txt = 'logic1'
# res3 = es.search(index='my-index', doc_type='test', body={"query":{'term': {'tagname': txt}}})
# res6 = res3['hits']['hits']
# if res6:
#     print('True')
# else:
#     print('False')
# res4 = json.dumps(res3)

#删除指定数据
# txt1 = '2018-05-12 00:42:58'
# qeury = {'query': {'match': {'create_time': txt1 }}}
# es.delete_by_query(index='my-index', doc_type='test',body = qeury)
#
# #闪
# index=None
# type=None
# body=None
# print(es.search(index=index, doc_type=type, body=body))



# res1 = es.search(index="test-index", body={'query':{'match':{'cpu':'8'}}})
# print(res1)



class Es():
    readme = 'operation elasticsearch'
    def __init__(self):
        es = Elasticsearch(['hqh-study-python.com:9298'])
        # Elasticsearch(['xxx.xxx.xxx.xxx'],http_auth = ('elastic', 'passwd'),port = 9200)
        if es.indices.exists(index='my-index') is not True:
                es.indices.create(index='my-index')
    #新增数据函数
    def Create_data(self,data):
        es = Elasticsearch(['hqh-study-python.com:9298'])
        #es.index(index='my-index', doc_type='test', body=data, refresh=True, id=3)
        es.index(index='my-index', doc_type='test', body=data, refresh=True)
    #查询指定数据函数
    def Get_data(self,id):
        # es = Elasticsearch(['hqh-study-python.com:9298'])
        z = es.get(index='my-index', doc_type='test', id=id)
        return z
    #删除数据函数
    def rm_data(self,id):
        es = Elasticsearch(['hqh-study-python.com:9298'])
        es.delete(index='my-index', doc_type='test', id=id)
    #查询所有数据函数
    def Get_data_all(self):
        es = Elasticsearch(['hqh-study-python.com:9298'])
        res = es.search(index='my-index', body={"query": {"match_all": {}}})
        sumshu = []
        for hit in res['hits']['hits']:
            ptk = hit['_source']
            sumshu.append(ptk)
        return sumshu



# x = Es()
# y = x.Get_data(3)
# k = y['_source']
# print(k)
#
# # 编码数据,获得str类型
# f = json.dumps(k)
# print(f)
# print(type(f))
# # 解析json格式,解出来是一个字典
# t = json.loads(f)
# print(t)
# print(type(t))
#
# print(t.get('create_time'))
