# -*- coding: utf-8 -*-
from common.readconfig import ReadConfig
import paramiko,psycopg2
from common.logger import Logger

readconfig=ReadConfig()


class database():
    def __init__(self, name=''):
        self.logger = Logger(logger_name='test_reverse',name=name).getlog()
        self.linux_data = readconfig.get_config_section_dict('linux')
        self.sql_data = readconfig.get_config_section_dict('sql')




    def con_linux(self):#连接服务器执行shell
        con=paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(hostname=self.linux_data['ip'],username=self.linux_data['user'],password=self.linux_data['password'])
        for shell in str(self.linux_data['shell']).split(','):
            stdin, stdout, stderr=con.exec_command(shell)
            result=stdout.read()
        # return result
        con.close()


    # def get_sql(self):#连接数据库查询sql
    #     con=psycopg2.connect(database=self.sql_data['database'],user=self.sql_data['username'],password=self.sql_data['password'],host=self.sql_data['ip'],port=self.sql_data['port'])
    #     cur=con.cursor()
    #     cur.execute(self.sql_data['sql'])
    #     data=cur.fetchall()
    #     con.commit()
    #     cur.close()
    #     con.close()
    #     if len(data) != 3:
    #         self.logger.info('数据库更新失败')
    #         quit()
    #     else:
    #         self.logger.info('数据库已更新')



# if __name__ == '__main__':
#     database=database().con_linux()