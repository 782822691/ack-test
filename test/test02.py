chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# user_zo_mon = int(input("请输入您的月份:"))
# user_zo_day = int(input("请输入您的日期:"))
#
# user_date = (user_zo_mon,user_zo_day)

dic = {}
for i in chinese_zodiac:
    dic[i] = chinese_zodiac
print(dic)

dic2 = {i:0 for i in chinese_zodiac}
print(dic2)