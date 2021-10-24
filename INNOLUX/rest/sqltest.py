#
# sdate='20210625183913'
# def str_toDate(sdate):
#     from datetime import datetime as dt
#     Y=sdate[0:4]
#     m=sdate[4:6]
#     d=sdate[6:8]
#     H=sdate[8:10]
#     M=sdate[10:12]
#     S=sdate[12:14]
#     st=f'{Y}-{m}-{d}-{H}'
#     print(st)
#
#     date=dt.strptime(st,'%Y-%m-%d-%H')
#     return date
# str_toDate(sdate)
#
# def str_toDay(sdate):
#     from datetime import datetime as dt
#     Y=sdate[0:4]
#     m=sdate[4:6]
#     d=sdate[6:8]
#     st=f'{Y}-{m}-{d}'
#     #print(st)
#
#     date=dt.strptime(st,'%Y-%m-%d')
#     return date
# print(str_toDay(sdate))
#
#
l=set()
l.add(1)
l.add(1)

print(1 in l)

