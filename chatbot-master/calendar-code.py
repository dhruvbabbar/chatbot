#import calendar
#
#c=calendar.TextCalendar(calendar.SUNDAY)
#str=c.formatmonth(2018,1)
#print(str)

import calendar
myCal = calendar.HTMLCalendar(calendar.SUNDAY)
print myCal.formatmonth(2009, 7)
print(type(myCal))