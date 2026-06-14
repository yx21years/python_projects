#字符串格式化
# %s将内容转化为字符串
# %d将内容转换为整数
# %f将内容转化为浮点型
'''
name="杨晓彤"
age=21
print("我的名字是：%s"%name)
print("我的名字是：%s,我的年龄是：%d"%(name,age))
print(f"我的名字是：{name}")
'''


''' 
字符串格式化-数字精度控制
%m.nd
%m.nf
若m比数字本身宽度还小则m不生效。
m:宽度，n:精度。四舍五入。小数的小数点和小数部分也算宽度
'''
# num1=10
# num2=10.123
# print("数字10宽度限制5，结果是：%5d"%num1)
# print("数字10宽度限制1，结果是：%1d"%num1)
# print("数字10.123宽度限制7，小数精度2，结果是：%7.2f。"%num2)
# print("数字10.123不限制宽度，小数精度2，结果是：%.2f"%num2)



#对表达式进行格式化
# print(f"1*1={1*1}")
# print("5/3的结果是：%.2f"%(5/3))
# print("字符串在python里的类型名是：%s"%type("字符串"))


#股价计算练习：定义变量，格式化输出
# name="sheep计算机"
# stock_price=10
# stock_code="003032"
# stock_price_daily_growth_factor=1.2
# growth_days=7
# finally_stock_price=stock_price *stock_price_daily_growth_factor**growth_days
# print("公司：%s,股票代码：%s,当前股价：%d"%(name,stock_code,stock_price))
# print(f"每日增长系数是：{stock_price_daily_growth_factor},经过{growth_days}的增长后，股价达到了：{finally_stock_price}")


#输入练习
# name=input("您好，请输入你的用户名:")
# stage=input("请输入您的身份：")
# age=input("请输入您的年龄：")
# print(f"尊敬的{name}，您好！请验证您的{stage}身份和年龄：{age}。")


#成年人判断if
# age=int(input("请输入您的真实年龄："))
# if age>=18:
#     print("您的年龄不满足优惠条件，请补票10元")
# else:
#     print("恭喜您满足学生票优惠，祝您旅行愉快！")


#if_elif_else练习：猜猜心里数
#多个elif条件是互斥的，满足按顺序的某一个条件执行该条件，且不会执行剩余条件。
#在判断条件中可以直接写input，节省代码量。
# num1=200546
# if int(input("猜中有奖哦！请输入猜想数字："))==num1:
#     print("猜对啦！")
# elif int(input("不对，再猜一次："))==num1:
#     print("猜对啦！")
# elif int(input("不对，再猜最后一次："))==num1:
#     print("猜对啦！")
# else:
#     print("猜错啦，下次加油哦！")

#判断语句：定义一个随机数，用户有三次机会猜数字。
# import random
# num=random.randint(1,10)
# guess_num=int(input("您只有三次机会，这是第一次，请输入一个整数："))
# if guess_num!=num:
#     if guess_num>num:
#         print("您输入的数字太大啦，试着猜小点吧。")
#     else:
#         print("您输入的数字太小啦，试着猜大点吧。")
#     guess_num = int(input("这是第二次输入："))
#     if guess_num==num:
#         print("恭喜您答对咯")
#     else :
#         if guess_num>num:
#             print("太大了")
#         else:
#             print("太小了")
#         guess_num=int(input("注意这是最后一次输入："))
#         if guess_num==num:
#                 print("游戏结束，恭喜您猜对啦！")
#         else:
#                 if guess_num>num:
#                     print("太大啦，游戏结束。")
#                 else:
#                     print("太小啦，游戏结束。")
#
# else :
#     print("恭喜您猜对咯！")










