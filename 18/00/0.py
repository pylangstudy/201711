import time
print(time.strftime('%a, %A'))#曜日名
print(time.strftime('%b, %B'))#月名
print(time.strftime('%c'))#日時名
print(time.strftime('%H'))#時(0-23)
print(time.strftime('%I'))#時(0-11)
print(time.strftime('%j'))#年中の日にち(1-366)
print(time.strftime('%Y-%m-%d'))#年月日
print(time.strftime('%H:%M:%S.%f'))#時分秒マイクロ秒
print(time.strftime('%p %I:%M'))#%p=ロケールの AM もしくは PM
print(time.strftime('%U'))#年の初めから何週目か(日曜〜)
print(time.strftime('%W'))#年の初めから何週目か(月曜〜)
print(time.strftime('%w'))#曜日
print(time.strftime('%x'))#ロケールの日付
print(time.strftime('%X'))#ロケールの時間
print(time.strftime('%y'))#西暦の下2桁
print(time.strftime('%Y'))#西暦
print(time.strftime('%z'))#タイムゾーン＋時差
print(time.strftime('%Z'))#タイムゾーン名
print(time.strftime('%%'))#'%'

print(time.strftime('%Y-%m-%d %H:%M:%S.%f', time.gmtime()))#class time.struct_time
print(time.strftime('%Y-%m-%d %H:%M:%S.%f', time.localtime()))#class time.struct_time
#print(time.gmtime())#time.struct_time(tm_year=2017, tm_mon=11, tm_mday=18, tm_hour=0, tm_min=20, tm_sec=36, tm_wday=5, tm_yday=322, tm_isdst=0)
#print(time.strftime('%Y-%m-%d %H:%M:%S.%f', time.mktime(time.gmtime())))
#print(time.strftime('%Y-%m-%d %H:%M:%S.%f', time.mktime(tuple(2017, 11, 18, 0, 20, 36, 5, 322, 0))))
#print(time.strftime('%Y-%m-%d %H:%M:%S.%f', calendar.timegm(tuple)))
