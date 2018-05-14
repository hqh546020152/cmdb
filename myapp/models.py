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

#数据库-用户表操作，参考：https://www.cnblogs.com/fortunate/p/7109345.html
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
        # body = {
        #     "query": {
        #         "match_all": {}
        #     },
        #     "sort": {
        #         "create_time": {
        #             "order": "asc"
        #         }
        #     }
        # }
        # res = self.es.search(index='my-index', body= body )
        #获取查询命中次数
        total = res['hits']['total']
        sumshu = []
        for hit in res['hits']['hits']:
            id_data = hit['_id']
            ptk = hit['_source']
            ptk['id'] = id_data
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
    # def update_data(self, index, type, id, body=None):
    def update_data(self, index, type, id, body):
        body = { "doc": body }
        return self.es.update(index=index, doc_type=type, id=id, body=body)
    #根据更新，指定名称里的数据信息
    def update_data_tagname(self,index, type, tagname, data):
        qeury = {'query': {'match': {'tagname': tagname}},'script':{'params':{data}}}
        return self.es.update_by_query(index=index, doc_type=type,body = qeury)
    # def Rm_data_tagname(self,index, type, tagname):
    #     qeury = {'query': {'match': {'tagname': tagname }}}
    #     return self.es.delete_by_query(index=index, doc_type=type,body = qeury)
    #模糊搜索
    def search_all(self,index , type , reque , size=100 ):
        res = self.es.search(index = index , doc_type = type , q = reque , size = size)
        return res
    #查询完数据后，进行数据修饰，达到可展示
    def data_despose(self, data ):
        sumshu = []
        for hit in data['hits']['hits']:
            ptk = hit['_source']
            sumshu.append(ptk)
        return sumshu

# class Data_shift():
#     readme = 'Data shift'
#     def shift(self,data):
#         pass


class SSH_passwd():
    def sshclient_execmd(self, hostname , port , username ,password, execmd ):
        paramiko.util.log_to_file("paramiko.log") #打印执行日志
        s = paramiko.SSHClient()      #调用paramiko模块下的SSHClient()
        s.load_system_host_keys()     #加载本地的known_hosts文件，该文件是纪录连到对方时，对方给的 host key。每次连线时都会检查目前对方给>的 host key 与纪录的 host key 是否相同，可以简单验证连结是否又被诈骗等相关事宜。
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect( hostname = hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command (execmd)
        stdin.write("Y") # Generally speaking, the first connection, need a simple interaction.
        A = stdout.read()   #执行成功，将返回执行结果。执行失败则为空
        B = stderr.read()   #执行失败，将返回错误信息。执行成功则为空
        s.close()     #关闭连接
        if A :
            return A
        else:
            return B


