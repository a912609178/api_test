import json
import os
import re
from common.update_json import update_target_value
from common.get_target_value import get_target_value
from common.file_path import LOG_PATH

class Update_all():
    def __init__(self):
        self.logs = os.listdir(LOG_PATH)
        self.num = ':'

    def get_index_values(self,num):
        if num:
            self.num = num

    def get_associate_id(self,api_xls, id):
        for list in api_xls:
            if str(list[0]) == id and str(list[5]) != "":
                return str(list[5])

    def get_content(self,id,log_name,type,what):
        log_list = []
        for name in self.logs:
            if log_name in name:
                log_list.append(name)
        if what=='修改':
            current_log=os.path.join(LOG_PATH, max(log_list))
        else:
            try:
                current_log=os.path.join(LOG_PATH, log_list[len(log_list)-1])
            except Exception as e:
                print(e)
        with open(current_log, 'rb') as f:
            while True:
                line = f.readline().decode("utf-8").strip()
                a = "case_id" + id + type
                if a in line:
                    content = line.split("case_id" + id + type)[1]
                    content = re.sub('\'', '\"', content)
                    content = re.sub('None', 'null', content)
                    content = eval(content)
                    return content
                if not line:
                    return ""

    def update_all(self,log_name,id,data,get_param,set_param):
        get_param_list = get_param.split(',')
        set_param_list = set_param.split(',')
        id_list=str(id).split(',')
        if len(id_list) == 1:
            content = self.get_content(id_list[0], log_name, "出参", "修改")
            if not isinstance(content,dict):
                try:
                    content = eval(content)
                except Exception as e:
                    print(e)
            for get_param, set_param in zip(get_param_list, set_param_list):
                    global value
                    result_list = []
                    try:
                        value = get_target_value(get_param, content, result_list)[0]
                        if str(value) == "None":
                            content1 = self.get_content(id,log_name, "入参","修改")
                            try:
                                value = get_target_value(get_param, content1, result_list)[0]
                            except:
                                pass

                    except:
                        content1 = self.get_content(id,log_name, "入参","修改")
                        try:
                            value = get_target_value(get_param, content1, result_list)[0]
                        except:
                            pass
                    if isinstance(data, dict):
                        update_target_value(set_param, data, value)
                    else:
                        data=json.loads(data)
                        update_target_value(set_param, data, value)
        else:
            for id, get_param, set_param in zip(id_list,get_param_list, set_param_list):
                content = self.get_content(id,log_name, "出参", "修改")
                result_list = []
                # global value
                try:
                    value = get_target_value(get_param, content, result_list)[0]
                    if str(value) == "None":
                        content1 = self.get_content(id,log_name, "入参", "修改")
                        try:
                            result_list = []
                            value = get_target_value(get_param, content1, result_list)[0]
                        except:
                            pass

                except:
                    content1 = self.get_content(id,log_name, "入参", "修改")
                    try:
                        value = get_target_value(get_param, content1, result_list)[0]
                    except:
                        pass
                if isinstance(data, dict):
                    update_target_value(set_param, data, value)
                else:
                    data = json.loads(data)
                    update_target_value(set_param, data, value)


        return data


if __name__ == '__main__':
    up = Update_all()
    data = {"requestAddBaseDto":{"empName":"yg8","idType":"1","idCode":"110101199002073632","gender":"1","nation":"156","birthDate":"1990-02-07","mobile":"18235329282","email":"912609178@qq.com","entryDate":"2019-06-21","sendBeginDate":"2019-06-01","addConEmpFlag":"2","cityId":"1415688","execType":"1","costCenter":"","remark":"","pdSetFlag":"2","custContId":"CCT_0000001983","custId":"CI_010000001402","quoId":"CCQ_0000002469","sendCorp":"SIF_010000001201","sendType":1},"requestInsAndAccuDto":{"insDecWage":5000,"accuDecWage":5000,"insPayFlag":"2","insGrpId":"ILP_010000003625","accuPayFlag":"2","accuGrpId":"ALP_010000002001","insWageList":[]},"requestPdInfo":[],"requestInsInfo":[],"empLaborContDto":{},"insSetFlag":2,"isAssSetFlag":"2","isInsWageFlag":"2","isSerSetFlag":"2","pdSetFlag":"2"}
    b = up.update_all(log_name='api',id=str(3.0),data=data,get_param='quoId',set_param='quoId')
    print(b)