# -*- encoding: UTF-8 -*-
import os
import sys
from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import speak
import rec

def main():
    #发送者默认设置
    FROM='你的邮箱地址'
    password = "授权码"
    smtp_server = "smtp服务器地址"

    #根据语音提示输入音频，识别并返回结果
    speak.say('to.wav')
    start=rec.rec(10)
    speak.say('toe.wav')
    end=rec.rec(5).lower()
    TO=start+'@'+end+'.com'
    print(TO)                #由于不能识别特殊符号，所以就把接收邮箱内容分割输入
    speak.say('toname.wav')
    name=rec.rec(5)
    speak.say('tosub.wav')
    SUBJECT=rec.rec(5)
    speak.say('totext.wav')
    text=rec.rec(10)
    
    
    def _format_addr(s):
    # 这个函数的作用是把一个标头的用户名编码成utf-8格式的，如果不编码原标头中文用户名，用户名将无法被邮件解码
        name, addr = parseaddr(s)
        return formataddr((Header(name, "utf-8").encode(), addr))
        # Header().encode(splitchars=';, \t', maxlinelen=None, linesep='\n')
            # 功能：编码一个邮件标头，使之变成一个RFC兼容的格式
    
    
    # 接下来定义邮件本身的内容
    msg = MIMEMultipart()
    msg["From"] = _format_addr("CC <%s>" % FROM)
    msg["To"] = _format_addr("%s <%s>" % (name,TO))
    msg["Subject"] = Header(SUBJECT, "utf-8").encode()
    # 定义邮件正文
    msg.attach(MIMEText(text, "plain", "utf-8"))

    
    
    
    # 接下来定义发送文件
    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.login(FROM, password)
        server.sendmail(FROM, [TO], msg.as_string())
        server.quit()
        speak.say('success.wav')
    except Exception,e:
        speak.say('faild.wav')
        print str(e)
    
