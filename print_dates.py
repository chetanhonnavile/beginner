from datetime import date,timedelta

d1 = date(2018,1,1)
d2 = date(2018,10,1)
d3 = d2-d1
print d3.days
for i in range(d3.days):
    print d1+timedelta(days=i)
