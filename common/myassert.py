import sys
from common.request_update import Update_all
update_all=Update_all()
sys.setrecursionlimit(10000)


def get_log_content(key_list,id,log_name):
    """获取log文件出参"""
    content=update_all.get_content(id,log_name,'出参','删除')
    del_content(key_list,content)
    return content


def del_content(key_list,data):
    """删除key"""
    if key_list==None:
        return data
        # return get_content_list(data, data_list=[])
    else:
        key_list=key_list.split(',')
        for key in key_list:
            if isinstance(data, dict):
                if key in data.keys():
                    del data[key]
                    del_content(key, data)
                else:
                    for value in data.values():
                        del_content(key, value)
            elif isinstance(data, list):
                for value in data:
                    del_content(key, value)
    return data









