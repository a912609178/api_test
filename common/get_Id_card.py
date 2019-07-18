import jpype
import os
jarpath = os.path.join(os.path.abspath('.'),'/Users/yangliu/Downloads/idCard.jar')
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" %(jarpath))
JDclass=jpype.JClass("com.shenfen.IdCardGenerator")
ss = JDclass.getIdCard()
# id_card_list=[]
# # for i in range(100):
#     ss = JDclass.getIdCard()
#     if ss not in id_card_list:
#         id_card_list.append(ss)
# print(id_card_list)
jpype.shutdownJVM()

def get_card_id():
    return ss
