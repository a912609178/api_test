# -*- coding: utf-8 -*-
#!usr/bin/python
import unittest
import json
import time
import ddt
from common.logger import Logger
from common.confighttp import ConfigHttp
from common import base_api
from common.request_update import Update_all



#申明类、公共参数
sheet_name='main_flow'
logger =Logger(logger_name='test_reverse',name=sheet_name).getlog()
api_xls = base_api.get_xls('test.xlsx', sheet_name)
update_all = Update_all()
LocalConfigHttp=ConfigHttp(sheet_name)




@ddt.ddt
class TestReverse(unittest.TestCase):
    '''参数化'''
    def setParameters(self,case_id,description,interface,method,headers,data,filename,filepath,associate_id,get_param,set_param,assert_key,message):
        self.case_id = str(case_id)
        self.description = str(description)
        self.interface = str(interface)
        self.method = str(method)
        self.headers = str(headers)
        self.data = str(data)
        self.filename = str(filename)
        self.filepath = str(filepath)
        self.associate_id = str(associate_id)
        self.get_param = str(get_param)
        self.set_param = str(set_param)
        self.assert_key = str(assert_key)
        if message.isdigit():
            self.message = int(message)
        else:
            self.message = message

    @classmethod
    def setUpClass(self):
        pass
        #数据库还原
        #database.con_linux()
        #验证数据库是否还原
        #database.get_sql()

    @classmethod
    def tearDownClass(self):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass




    @ddt.data(*api_xls)
    @ddt.unpack
    def testReverse(self,id,description,interface,method,headers,data,filename,filepath,associate_id,get_param,set_param,assert_key,message):
        self.setParameters(id,description,interface,method,headers,data,filename,filepath,associate_id,get_param,set_param,assert_key,message)
        if data:
            datas = json.loads(self.data)
            print(type(datas),'json_data',datas)
        else:
            datas = {}

        if self.associate_id != "":
            datas = update_all.update_all(sheet_name, self.associate_id, self.data, self.get_param, self.set_param)

        api_url = self.interface
        LocalConfigHttp.set_data(datas)

        if 'http'in api_url:
            LocalConfigHttp.set_url2(api_url)
        else:
            LocalConfigHttp.set_url(api_url)


        if self.headers:
            LocalConfigHttp.set_headers2(self.headers)
        else:
            LocalConfigHttp.set_headers()


        start_time=time.time()
        if self.method == 'post':
            self.response = LocalConfigHttp.post()
        elif self.method == 'get':
            self.response = LocalConfigHttp.get()
        elif self.method == 'post_files':
            self.response = LocalConfigHttp.post_files(self.filename,self.filepath)
        self.content = self.response.json()
        print(self.content)
        end_time=time.time()
        post_time=end_time-start_time

        global assert_value
        assert_value = self.content[self.assert_key]

        #日志
        logger.info("case_id" + str(self.case_id)+'请求时间为'+str(post_time))
        logger.info("case_id" + str(self.case_id) + "入参" + str(datas))
        logger.info("case_id" + str(self.case_id) + "出参" + str(self.content))
        self.checkResult()

    #断言
    def checkResult(self):
        self.assertEqual(str(assert_value), self.message)


if __name__ == '__main__':
    unittest.main()
