import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
import testframe.Tools.tools
import time

# 运行tools里面的建立报告
testframe.Tools.tools

# 第一步：连接到smtp服务器
smtp = smtplib.SMTP_SSL(host='smtp.163.com', port=465)

# 第二步：登录smtp服务器
smtp.login(user='ztbanbo@163.com', password='')

# 第三步构建一封带附件的邮件
# 创建一封多组件的邮件
msg = MIMEMultipart()
# 添加发件人
msg['From'] = "ztbanbo@163.com"
# 添加收件人
msg['To'] = "80442009@qq.com"
# 添加主题
msg['Subject'] = Header("测试报告", charset='utf8')
# 添加邮件文本内容
# 创建邮件文件内容对象
text_content = MIMEText("这封邮件是用来发送自动化测试报告的，邮件中添加了测试报告的附件", _charset='utf8')
# 把邮件的文本内容，添加到多组件的邮件中
msg.attach(text_content)


# 获取报告文档里面最新的报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    print(('最新测试结果' + lists[-1]))
    file_new = os.path.join(testreport, lists[-1])
    return file_new


# 添加附件
now = time.strftime('%Y-%m-%d_%H:%M')
newreport = new_report('G:/PycharmProjects/pyjiaoben/testframe/Report')
f_msg = open(newreport, 'rb').read()
app = MIMEApplication(f_msg)
app.add_header('content-disposition', 'attachment', filename=now + '自动化测试报告结果.html')
msg.attach(app)

# 发送邮件
smtp.send_message(msg=msg, from_addr="ztbanbo@163.com", to_addrs=["793294597@qq.com","80442009@qq.com"])

