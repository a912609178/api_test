import re,configparser,os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror,error
# from common.logger import Logger
from common.file_path import REPORT_PATH,CONFIG_PATH

# logger = Logger(logger_name='Email').getlog()

class Email:
    def __init__(self):
        config_mail = configparser.ConfigParser()
        config_mail.read(os.path.join(CONFIG_PATH,'config.ini'))

        self.mail_title = config_mail.get('mail','title')
        self.mail_message = config_mail.get('mail', 'message')
        self.mail_receiver = config_mail.get('mail', 'receiver').split(',')
        self.mail_sender = config_mail.get('mail', 'sender')
        self.mail_password = config_mail.get('mail', 'password')
        self.msg = MIMEMultipart('related')
        report_htmls = os.listdir(REPORT_PATH)
        self.mail_report = os.path.join(REPORT_PATH,max(report_htmls))
        self.mail_server = config_mail.get('mail', 'server')


    def _attach_file(self,att_file):
        att = MIMEText(open('%s'%att_file,'rb').read(),'plain','utf-8')
        att['Content-Type'] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]',att_file)
        att['Content-Disposition'] = 'attachment;filename=%s'%file_name[-1]
        self.msg.attach(att)
        # logger.info('attach file{}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.mail_title
        self.msg['Form'] = self.mail_sender
        self.msg['To'] = ','.join(self.mail_receiver)

        if self.mail_message:
            self.msg.attach(MIMEText(self.mail_message))

        if self.mail_report:
            if isinstance(self.mail_report,list):
                for f in self.mail_report:
                    self._attach_file(f)
            elif isinstance(self.mail_report,str):
                self._attach_file(self.mail_report)

        try:
            smtp_server = smtplib.SMTP(self.mail_server)
        except (gaierror and error) as e:
            pass
            # logger.exception('发送邮件失败，无法连接到SMTP服务器，检查网络%s',e)
        else:
            try:
                smtp_server.login(self.mail_sender,self.mail_password)
            except smtplib.SMTPAuthenticationError as e:
                pass
                # logger.exception('用户名密码错误，登录失败！%s',e)
            else:
                smtp_server.sendmail(self.mail_sender,self.mail_receiver,self.msg.as_string())
            finally:
                smtp_server.quit()
                # logger.info('邮件发送成功{0}，收件人：{1}。如果没有收到邮件，请检查垃圾箱，同时检查收件人地址是否正确。'.format(self.mail_title,self.mail_receiver))