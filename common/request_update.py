# -*- coding: utf-8 -*-
import json,re



#从一个json中获取某个键的值
def get_target_value(key, dic, tmp_list):
    """
    :param key: get_param 依赖以前的key值
    :param dic: 从日志中获取到的依赖的case的响应信息 json从这里面去取值
    :param tmp_list: 用于存储获取的数据
    :return: list
    """

    if not isinstance(dic, dict) or not isinstance(tmp_list, list):
        print('argv[1] not an dict or argv[-1] not an list')
        return None

    if key in dic.keys() and dic[key]!=None:
        if key != 'data':
            tmp_list.append(dic[key])
        else:
            tmp_list.append(dic['data']['data'])
    else:
        for value in dic.values():
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)
    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)

if __name__ == "__main__":
    tmplist = []
    dic = {'data': {'data': 16224, 'success': True}, 'success': True, 'traceId': '68510bea927d4e60845a1a021b087da8'}
    a = get_target_value(key='data', dic=dic, tmp_list=tmplist)
    print(a)

