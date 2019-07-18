import json,re


#更新一个json
#target_value为None，删除目标key：value；不为空，则修改
def update_target_value(keys, dic, target_value):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param target_value: 用于更新的数据
    """
    if not isinstance(dic, dict):  # 对传入数据进行格式校验
        return 'argv[1] not an dict '

    if keys in dic.keys():
        #有的关联接口的出参与这里的入参格式可能不同，需要判断
        if isinstance(dic[keys], list) and not isinstance(target_value, list):
            dic[keys] = [target_value]
        elif not isinstance(dic[keys], list) and isinstance(target_value,list):
            dic[keys] = target_value[0]
        else:
            dic[keys] = target_value  # 更新数据
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                update_target_value(keys, value, target_value)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                for val in value:
                    # print(val)
                    update_target_value(keys, val, target_value)
    return dic

def list_to_update_dict(keys, dic, target_value):
    if "insAddDets" in dic.keys():
        for i in range(len(target_value)):
            dic['insAddDets'][i][keys] = target_value[i]
    elif "matFullFlag" in dic.keys():
        for i in range(len(target_value)):
            dic['matSubmitInfos'][i][keys] = target_value[i]
    return dic

if __name__ == "__main__":
    content = {"asss":[],"serId":"EEI_020000000042","matFullFlag":"1","entryInfo":{"mkupPayFlag":2},"matSubmitInfos":[{"elementArr":[],"inpVal":"1","fileList":[],"reqFlag":1,"matName":"养老参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001530","matId":"MI_000000582","dictItems":[{"itemCode":"1","itemName":"新参保"},{"itemCode":"2","itemName":"居民转职工"}]},{"elementArr":[],"inpVal":"1","fileList":[],"reqFlag":1,"matName":"生育参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001531","matId":"MI_000000583","dictItems":[{"itemCode":"1","itemName":"新参保"},{"itemCode":"2","itemName":"居民转职工"}]},{"elementArr":[],"inpVal":"1","fileList":[],"reqFlag":1,"matName":"失业参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001532","matId":"MI_000000584","dictItems":[{"itemCode":"1","itemName":"新参保"},{"itemCode":"2","itemName":"居民转职工"}]},{"elementArr":[],"inpVal":"1","fileList":[],"reqFlag":1,"matName":"医疗参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001533","matId":"MI_000000585","dictItems":[{"itemCode":"1","itemName":"新参保"},{"itemCode":"2","itemName":"居民转职工"}]},{"elementArr":[],"inpVal":"1","fileList":[],"reqFlag":1,"matName":"工伤参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001534","matId":"MI_000000586","dictItems":[{"itemCode":"1","itemName":"新参保"},{"itemCode":"2","itemName":"居民转职工"}]},{"elementArr":[],"inpVal":"6","fileList":[],"reqFlag":1,"matName":"公积金参保类型","inpType":"4","relBusiType":"2","openFlag":1,"pageDetailId":"MPPD_020000001535","matId":"MI_000000587","dictItems":[{"itemCode":"6","itemName":"新增"},{"itemCode":"7","itemName":"启封"}]}],"ordHdlRemark":{},"mkupPayDets":[]}
    print(content['matSubmitInfos'][0]['pageDetailId'])
    print(content['matSubmitInfos'][1]['pageDetailId'])