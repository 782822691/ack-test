def a(b=0):
    x = 0
    #print('使用了a函数')
    def count():
        nonlocal x
        x += 1
        print(x)
        return x
    return count
m1 = a()
print(m1())
print(m1())
#
# a()()
# a()()
# a(1)()
# a()()
# import time
# def tips(func):
#     x = 0
#     def count(a):
#         nonlocal x
#         func(a)
#         x = a
#         x += 1
#         return x
#     return count
# @tips
# def jia(a):
#     time.sleep(1)
#
# nun1 = jia(0)
# print(nun1)
# print(jia(5))
# print(nun1)

