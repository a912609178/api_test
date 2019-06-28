import requests
from urllib3 import encode_multipart_formdata
from common.readconfig import ReadConfig

s = requests.session()
s.cookies.clear()
r1 = s.get("http://10.0.75.38/ssoApi/baselogin/captcha")


class ConfigHttp:
    def __init__(self,name=''):
        global url,timeout,header
        header={}
        config = ReadConfig()
        url = config.get_config_value('apiDomain','domain')
        timeout = config.get_config_value('apiDomain','timeout')
        self.headers = config.get_config_section_dict('HEADERS')
        self.data = {}
        self.json = {}
        self.url = None
        self.files = {}
        self.cookies = None
        self.filename = ""
        self.filepath = ""


    def set_url(self, para_api):
        """url拼接方法"""
        self.url = url+para_api
        return self.url

    def set_url2(self, para_api):
        self.url = para_api
        return self.url

    def set_headers(self):
        return self.headers

    def set_headers2(self, headers={}):
        self.headers = headers
        return self.headers

    def set_data(self, data):
        self.data = data
        return self.data

    def set_json(self, json):
        self.json = json

    def set_files(self, file):
        self.files = file


    def get(self):
        try:
            response = s.get(self.url, headers=self.headers, params=None, timeout=float(timeout))
            return response
        except TimeoutError:
            # pass
            self.logger.error('TIME OUT %s .'%self.url)

    def post(self):
        try:
            response = s.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            # pass
            self.logger.error('TIME OUT %s .'%self.url)

    def post_files(self,filename,filepath):
        header = {}
        data = self.data
        data['file'] = (filename, open(filepath, 'rb').read())
        encode_data = encode_multipart_formdata(data)
        data = encode_data[0]
        print('编码后的data',data)
        header['Content-Type'] = encode_data[1]
        try:
            response = s.post(url=self.url, headers=header, data=data)
            return response
        except TimeoutError:
            self.logger.error('TIME OUT %s .'%self.url)




