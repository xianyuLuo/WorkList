import smtplib
import os
from email.mime.text import MIMEText
from job.models import user, job, level

#设置服务器所需信息
mail_host = os.environ.get('MAIL_HOST', 'smtp.163.com')
mail_user = os.environ.get('MAIL_USER', 'yyyyy')
mail_pass = os.environ.get('MAIL_PASS', 'xxxxx')
sender = mail_user
receivers = ['luojiahao@dragonest.com']

#设置email信息
#邮件内容设置
message = MIMEText('content','plain','utf-8')
#邮件主题
message['Subject'] = 'JOB通知'
#发送方信息
message['From'] = sender
#接受方信息
message['To'] = receivers[1]

#登录并发送邮件
try:
    smtpObj = smtplib.SMTP()
    #连接到服务器
    smtpObj.connect(mail_host,25)
    #登录到服务器
    smtpObj.login(mail_user,mail_pass)
    #发送
    smtpObj.sendmail(
        sender,receivers,message.as_string())
    #退出
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error',e) #打印错误