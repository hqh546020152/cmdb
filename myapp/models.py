from django.db import models
import hashlib
#pip install elasticsearch
from elasticsearch import Elasticsearch

import json

#将数据转化为MD5
class Change_md5():
    readme = 'change-md5'
    def setName(self,data):
        hl = hashlib.md5()
        hl.update(data.encode(encoding='utf-8'))
        self.data = hl.hexdigest()# This is an auto-generated Django model module.

#数据库-用户表操作
class DUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=16)
    passwd = models.CharField(max_length=32, blank=True, null=True)
    valid = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'd_user'

#elasticsearch数据操作---类
class Es():
    #参考https://github.com/YHYR/ElasticSearchUtils/blob/master/utils/elasticsearchUtil.py
    readme = 'operation elasticsearch'
    def __init__(self):
        self.es = Elasticsearch(['hqh-study-python.com:9298'])
        # Elasticsearch(['xxx.xxx.xxx.xxx'],http_auth = ('elastic', 'passwd'),port = 9200)
        if self.es.indices.exists(index='my-index') is not True:
            self.es.indices.create(index='my-index')
    #新增数据函数
    def Create_data(self, index, type, body, id=None):
        return self.es.index(index=index, doc_type=type, body=body, id=id)
    #根据tagname查看是否已存在,返回True表示已存在，返回False表示不存在
    def Get_data_tagname(self,index, type, tagname):
        body = {"query": {'term': {'tagname': tagname}}}
        res = self.es.search(index=index, doc_type=type, body=body )
        if res['hits']['hits']:
            # judge = 'True'
            return 'True'
        else:
            # judge = 'False'
            return 'False'
    #根据tagname删除数据
    def Rm_data_tagname(self,index, type, tagname):
        qeury = {'query': {'match': {'tagname': tagname }}}
        return self.es.delete_by_query(index=index, doc_type=type,body = qeury)
    #根据ID查询数据函数
    def Get_data(self, index, type, id):
        return self.es.get(index = index, doc_type = type , id = id)
    #根据ID删除数据
    def Rm_data(self, index, type, id):
        return self.es.delete(index=index, doc_type=type, id=id)
    #查询所有数据函数
    def Get_data_all(self):
        res = self.es.search(index='my-index', body={"query": {"match_all": {}}})
        sumshu = []
        for hit in res['hits']['hits']:
            ptk = hit['_source']
            sumshu.append(ptk)
        return sumshu
    #删除索引下所有的数据
    def Rm_data_all(self, index, type=None):
        # try:
        query = {'query': {'match_all': {}}}
        return self.es.delete_by_query(index=index, body=query, doc_type=type)
        # except Exception, e:
        #     return str(e) + ' -> ' + index
    #查找index下所有符合条件的数据
    def searchDoc(self, index=None, type=None, body=None):
            # '''
            # 查找index下所有符合条件的数据
            # :param index:
            # :param type:
            # :param body: 筛选语句,符合DSL语法格式
            # :return:
            # '''
        return self.es.search(index=index, doc_type=type, body=body)
    #根据更新指定ID里的数据信息
    def update_data(self, index, type, id, body=None):
        return self.es.update(index=index, doc_type=type, id=id, body=body)

# class Data_shift():
#     readme = 'Data shift'
#     def shift(self,data):
#         pass



