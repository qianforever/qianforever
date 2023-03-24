import smtplib
from email.mime.text import MIMEText
from email.header import Header

import pymysql


def e_mail(text, e, zt):
    mail_host = "smtp.qiye.aliyun.com"  # 设置服务器
    mail_user = "qianyh@yuantsing.com"  # 用户名
    mail_pass = "ytt@2019"  # 口令

    sender = 'qianyh@yuantsing.com'
    receivers = e  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("钱永恒", 'utf-8')
    message['To'] = Header("", 'utf-8')

    subject = zt
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def dict_1(key):
    dict1 = {
        '钱原吉': 'qianyj@yuantsing.com',
        '孙建平': 'sunjp@yuantsing.com',
        '刘蕙瑜': 'liuhy@yuantsing.com',
        '颜晗': 'jbjvuc@live.com',
        '袁国贤': '540346961@qq.com',
        '程星宇': '617463845@qq.com',
        '谈盈': '452322060@qq.com',
        '郁秋龙': '13862239475@163.com',
        '焦盛': '18915276789@189.cn',
        '靳浩天': 'jinht@yuantsing.com',
        '朱倩': '469405962@qq.com',
        '姜跃英': '1017420875@qq.com',
        '冯泽林': '365193657@qq.com',
        '林荣强': '1783995239@qq.com',
        '缪美芳': '64697759@qq.com',
        '沈佳栋': '852892043@qq.com',
        '施长青': '410124018@qq.com',
        '李文浩': '981019427@qq.com',
        '周家炟': '1213787164@qq.com',
        '严军': '13646138835@163.com',
        '缪佳浩': '1164374059@qq.com',
        '吴笛': '2492660232@qq.com',
        '蒋嘉炜': '1187186304@qq.com',
        '李亮': '1834088335@qq.com',
        '卢茜': '420627033@qq.com',
        '李微明': 'liwm@yuantsing.com',
        '管庆伟': '1039540296@qq.com',
        '唐凯': '646868027@qq.com',
        '周涛': '771507153@qq.com',
        '周赟': '260155347@qq.com',
        '黄成': 'huangcheng850@163.com',
        '周琪': 'zhouq@yuantsing.com',
        '刘斐': '726818621@qq.com',
        '孙竞': 'Sunj@yuantsing.com',
        '郭敏怡': '1378390767@qq.com',
        '牛鑫磊': '173306693@qq.com',
        '王鑫': '495268807@qq.com',
        '冯强': '940781221@qq.com',
        '黄军立': 'huangjl@yuantsing.com',
        '叶骐珲': '349578271@qq.com',
        '朱全斌': '1466101301@qq.com',
        '蒋程涛': '1565897782@qq.com',
        '缪许栩': 'miaoxuxu@vip.qq.com',
        '陈建军': '1558747912@qq.com',
        '胡晓荣': '469811915@qq.com',
        '张瑞武': 'zhangrw@yuantsing.com',
        '叶雷': '19881252@qq.com',
        '蒋恋伟': '3044337006@qq.com',
        '叶静娇': '847223305@qq.com',
        '王斐': 'wangfei20131979@163.com',
        '黄轲': '1079013012@qq.com',
        '管宏杰': '515553537@qq.com',
        '陈星元': '3080281497@qq.com',
        '许盛': '1767326877@qq.com',
        '郑剑林': 'zjl2008511@126.com',
        '秦棨烨': 'qinqy@yuantsing.com',
        '房海涛': 'haitaofang@yeah.net',
        '葛逸飞': '13812541994@163.com',
        '冯乙': '2942522437@qq.com',
        '王振宇': '1553711985@qq.com',
        '黄认': 'a529321176@163.com',
        '敖一杭': '2695645110@qq.com',
        '于大利': '807742273@qq.com',
        '晏海丽': '772534701@qq.com',
        '尤佩': '354744191@qq.com',
        '吴红': '496462256@qq.com',
        '陈永康': '1621674206@qq.com',
        '顾聪': '1373392595@qq.com',
        '申杰': '401385227@qq.com',
        '张志峰': 'zhzf99@hotmail.com',
        '吕新成': '2694353940@qq.com',
        '刘宇': '3241583378@qq.com',
        '吴迪': '1826030262@qq.com',
        '霍元浩': '1490034416@qq.com',
        '熊兴乐': '763718847@qq.com',
        '丁烨彪': '2364082821@qq.com',
        '杨鹏': '807085112@qq.com',
        '郎明明': '4',
        '马晓慧': '961686675@qq.com',
        '杨永鹏': '1210684423@qq.com',
        '张泽清': '2233925410@qq.com',
        '钱永恒': 'qianyh@yuantsing.com',
        '孙政': '5',
        '陈晓旦': '806663909@qq.com',
    }
    return dict1.get(key)


def con():
    connect = pymysql.connect(host='192.168.100.221',
                              user='root',
                              password='123456',
                              db='qian',
                              charset='utf8')  # 服务器名,账户,密码,数据库名
    cur = connect.cursor()
    return cur
