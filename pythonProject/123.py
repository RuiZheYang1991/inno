# l=[1,0,2]
# ans=0
# for i in l:
#     ans+=i
#     idx=i%len(l)
#     l[idx]+=i
#     l=l[:-1]
# print(ans)

# class demo:
#     i=0
#     def __init__(self):
#         self.i=5
# my_cls=demo
#
# print(my_cls)
# print(demo.i)

# def aaa(string):
#     l=[]
#     for i in string:
#         cnt=string.count(i)
#         s=(cnt,i)
#         l.append(s)
#     s=set(l)
#     sorted_l = sorted(s, key=lambda t: t[0])
#     le=len(sorted_l)-3
#     return sorted_l[le:]
# print(aaa("DRGERGRDGFDFDGDFDSDSDSDSDSDSDEFEFHMMDFG"))
#

# l=[3,5,9,12,18]
#
#
# def variance(l):  # 平方的期望-期望的平方
#     s1 = 0
#     s2 = 0
#     for i in l:
#         s1 += i ** 2
#         s2 += i
#     return round(float(s1) / len(l) - (float(s2) / len(l)) ** 2,2)
#
# print(variance(l))
# class A:
#     def print(self):
#         print("itsA")
# class B:
#     def print(self):
#         print("its B")
# b=B()
# b.print()
# A.print(B)

x=[0,1,2,3]
x.append(x)
x[2]=4
print(x)
print(x[-1][1:][:-1][-2])