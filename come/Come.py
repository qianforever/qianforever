import pymysql
import streamlit as st
from E_mail import e_mail, dict_1

# 链接数据库
connect = pymysql.connect(host='192.168.100.221',
                          user='root',
                          password='123456',
                          db='qian',
                          charset='utf8')  # 服务器名,账户,密码,数据库名
cur = connect.cursor()

st.set_page_config(page_title="来访申请表")
st.header("来访申请表")


dw = st.text_input(
    '来访单位',
)
rs = st.text_input(
    '来访人数',
)
xm = st.text_input(
    '来访者姓名(填写所有来访人员)',
)
id = st.text_input(
    '填写身份证号码',
)
phone = st.text_input(
    '来访者电话(填写一个即可)',
)
car_id = st.text_input(
    '随行车牌号码',
)

bfz_xm = st.text_input(
    '被访者姓名(请写全称)',
)
bfz_phone = st.text_input(
    '被访者电话',
)
date = st.date_input(
    '请选择来访日期'
)
time = st.time_input(
    '请选择来访时间'
)
t = "来访单位:{}\n来访人数:{}\n来访者姓名:{}\n身份证号码:{}\n来访者电话:{}\n随行车辆车牌:{}\n来访日期:{}\n来访时间:{}\n被访者姓名:{}".format(dw, rs, xm, id, phone, car_id, date, time, bfz_xm)
if st.button('提交'):
    sql = "INSERT INTO lfsq VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param = (dw, rs, xm, id, phone, car_id, bfz_xm, bfz_phone, date, time)
    cur.execute(sql, param)
    connect.commit()
#     # st.write('')
    st.success('提交成功')
#     connect.close()
#     cur.close()
# else:
#     st.write('提交失败')
    st.balloons()
    e_mail(t, dict_1(bfz_xm), "来访申请")
    st.success('申请已发送给被访者')
