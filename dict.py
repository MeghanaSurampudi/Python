d={101:'python',201:'java',301:'c',401:'c++'}
print(d)
print(type(d))
print("*****************************************************")
print(d[101])
print(d[201])
print(d[301])
print(d[401])
d[501]='sql'
print("*****************************************************")
print(d)
d[101]='flutter'
print("*****************************************************")
print(d)
del d[301]
print(d)