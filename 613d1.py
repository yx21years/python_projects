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

#求1-100的累计和，通过while循环
# sum=0
# i=1
# while i<=100:
#     sum+=i
#     i+=1
# print(f"1-100的累计和为{sum}")

#练习：猜数字无限次机会，猜中为止，提示大小，记录次数
# import random
# num=random.randint(1,100)
# i=1
# guess_num=int(input("请输入猜测数字："))
# while guess_num!=num:
#     if guess_num>num:
#         print("太大啦")
#     else:
#         print("太小啦")
#     guess_num=int(input("请输入数字："))
#     i+=1
# print(f"你猜对啦，正确答案是{num},你一共猜测了{i}次。")


#练习：while循环，输出九九乘法表
# count=1
# i=1
# j=1
# while count<=9:
#     while i<=j:
#         if i==j:
#             print(f"{i}*{j}={i*j}")
#             i+=1
#         else:
#             print(f"{i}*{j}={i*j}\t",end=" ")
#             i+=1
#     j+=1
#     count+=1
#     i=1

#老师的解法
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={i*j}\t",end="") #制表符\t end=" "控制字符串不换行
#         j+=1
#     i+=1
#     print()#全部输出完之后再换行


#for循环(无法定义循环条件)
# name="asdfg"
# for i in name:
#     print(i,name[1],sep=",",end="\t")

#for循环练习：遍历字符串，统计英文字母a。
# name="itheima is a brand of itcast"
# count=0
# for i in name:
#     if i=="a":
#         count+=1
# print(f"在{name}中字母a有{count}个")


#range：获取一个从0开始，到num结束的数字序列（不包含num本身）。
# for i in range(2):
#     print(i,end=" ")

#range（num1，num2）：从num1开始，到num2结束的数字序列（包含num1，但不含num2本身）。
# for i in range(4,6):
#     print(i,end=" ")

#range（num1，num2，step）：从num1开始，到num2结束,步长为step的数字序列（包含num1，但不含num2本身）。
# for i in range(1,10,3):
#     print(i,end=" ")

#for循环写九九乘法表
# for i in range(1,10):
#     for j in range(1,10):
#         if i>=j:
#             print(f"{j}*{i}={i*j}\t",end=" ")
#     print()

#老师版
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i * j}\t", end=" ")
#     print()

#continue:中断它所在的本次循环，直接进行下一次循环,break：直接结束整个循环。均无法对上层循环起作用。
#案例：发工资。账户共1w元，给20人发工资。1-20编号依此领工资，每人1000元，
# 随机生成绩效分1-10分，如果低于五不发工资，下一个直到工资发完。
# import random
# sum=10000
# for i in range(1,21):
#     score=random.randint(1,10)
#     if sum>=1000:
#         if score>=5:
#             sum-=1000
#             print(f"向员工{i}发放1000元，账户余额还剩{sum}")
#         else:
#             print(f"员工{i},绩效{score},低于5，不发工资，下一位。")
#     else:
#         print("工资发完了")
#         break


