import datetime
# Enter your code here. Read input from STDIN. Print output to STDOUT
month,day,year = map(int,input().split())
a = datetime.date(year,month,day)
b = a.strftime("%A")
print(b.upper())

