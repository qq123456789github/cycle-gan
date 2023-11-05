# import math
# def f(a,b):
#     a=a*0.01745
#     print(10e5*math.sin(a)/300)
#     print("{}%".format(100*((abs(math.sin(a)/300)*1000000-b)/b)))
# f(7.5025,435.83)
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.figure(figsize=(10,7))
# y1=[0,0.034,0.065,0.098,0.131,0.164,0.194,0.227,0.258]
# x1=list(range(0,9))
# x=np.arange(0,9)
# y=x*1*10e-7/(2*3.14159*0.0000057)
# print(y)
# ax1 = plt.subplot(121)
# ax1.set_title('长直导线电流变化曲线')
# ax1.set_xticks(range(0,9))
# ax1.set_yticks(np.arange(0.,0.3,0.03))
# ax1.set_xlabel("I/A", fontdict={'size': 16})
# ax1.set_ylabel("B/mT", fontdict={'size': 16})
# ax1.scatter(x1, y1, c='red', s=20)
# ax1.plot(x,y)
#
#
# x2 = np.array([5.7,6.7,7.7,8.7,10.7,14.7,17.7,21.7,26.7,37.7,55.7])
# y2 = [0.238,0.234,0.223,0.204,0.154,0.108,0.086,0.067,0.051,0.031,0.017]
# yy=(8*10e-1)/(2*3.14159*x2)
# ax2 = plt.subplot(122)
# ax2.set_title('长直导线距离变化曲线')
# ax2.set_xticks(np.arange(5.7,55.7,5))
# ax2.set_yticks(np.arange(0.,0.3,0.03))
# ax2.set_xlabel("r/mm", fontdict={'size': 16})
# ax2.set_ylabel("B/mT", fontdict={'size': 16})
# ax2.scatter(x2, y2, c='red', s=20)
#
# ax2.plot(x2,yy)
# print(x2,yy)
#
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
#
# years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# turnovers = [0.5, 9.36, 52, 191, 350, 571, 912, 1027, 1682, 2135, 2684]
# plt.figure(figsize=(10, 15), dpi=100)
# plt.scatter(years, turnovers, c='red', s=100, label='成交额')
# plt.xticks(range(2008, 2020, 1))
# plt.yticks(range(0, 3200, 200))
# plt.xlabel("年份", fontdict={'size': 16})
# plt.ylabel("成交额", fontdict={'size': 16})
# plt.title("历年天猫双11总成交额", fontdict={'size': 20})
# plt.legend(loc='best')
# plt.show()
import math
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(10,7))
y1=np.array([0,0.015,0.023,0.040,0.0479,0.060,0.075,0.097,0.113])
x1=np.arange(0,9,1)
ax1 = plt.subplot(221)
ax1.set_title('圆圈导线电流变化曲线')
ax1.set_xticks(range(0,9))
ax1.set_yticks(np.arange(0.,0.3,0.03))
ax1.set_xlabel("I/A", fontdict={'size': 16})
ax1.set_ylabel("B/mT", fontdict={'size': 16})
ax1.scatter(x1, y1, c='red', s=20)
y=x1*1*10e-7/(2*0.00004)
print('理论值',y)
ax1.plot(x1,y)



I=80000
R=40
x2 = np.array([-10,-7.5,-5,-4,-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,4,5,7.5,10])
yy2=[0.001,0.004,0.021,0.038,0.058,0.072,0.083,0.098,0.110,0.119,0.123,0.120,0.111,0.099,0.084,0.070,0.050,0.035,0.020,0.015,0.010]
y2 = [0.001,0.007,0.025,0.040,0.058,0.079,0.080,0.098,0.115,0.119,0.123,0.120,0.111,0.099,0.084,0.072,0.062,0.040,0.024,0.019,0.017]
mu0 = 4 * np.pi * 1e-6  # 真空中的磁导率（单位：N/A^2）
magnetic_field = (mu0 * I * R ** 2) / (2 * (R ** 2 + x2 ** 2) ** (3 / 2))


ax2 = plt.subplot(222)
ax2.set_title('圆环导线距离变化曲线')
# ax2.set_xticks(np.arange(-10,10,1))
# ax2.set_yticks(np.arange(0,0.123,0.003))
ax2.set_xlabel("x/cm", fontdict={'size': 16})
ax2.set_ylabel("B/mT", fontdict={'size': 16})
ax2.scatter(x2, y2, c='red', s=20)
#
ax2.plot(x2,yy2)
print(magnetic_field)
#
plt.tight_layout()





plt.show()