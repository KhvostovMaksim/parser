import time
import datetime
string=input('enter your string: ')
string=string.partition(" ")
MESSAGE={'STATUS':'SUCCESS', 'DATE':{'YEAR':None,'MONTH':None,'DAY':None,'HOUR':None,'MINUTE':None}, 'TEXT':"None"}


if  'завтра' in string:
    from datetime import date, timedelta, datetime
    tommorow=date.today()+timedelta(days=1)
    print(tommorow)
if  'послезавтра' in string:
    from datetime import date, timedelta, datetime
    aftertommorow=date.today()+timedelta(days=2)
    print(aftertommorow)
aftertommorow = str(date.today()+timedelta(days=2))
aftertommorow = aftertommorow.split("-")
print(aftertommorow)
MESSAGE['DATE']['YEAR'] = aftertommorow[0]
MESSAGE['DATE']['MONTH'] = aftertommorow[1]
MESSAGE['DATE']['DAY'] = aftertommorow[2]
if ('в понедельник' or 'каждый понедельник' or 'понедельник' or 'Понедельник' or 'по понедельникам') in string:
    day = 'Monday'

if ('во вторник' or 'каждый вторник' or 'вторник' or 'Вторник' or 'по вторникам') in string:
    day = 'Tuestday'

if ('в среду' or 'каждую среду' or 'среда' or 'Среда' or 'по средам') in string:
    day = 'Wednsday'

if ('в четверг' or 'каждый четверг' or 'четверг' or 'Четверг' or 'по четвергам') in string:
    day = 'Thursday'

if ('в пятницу' or 'каждую пятницу' or 'пятница' or 'Пятница' or 'по пятницам') in string:
    day = 'Friday'

if ('в субботу' or 'каждую субботу' or 'суббота' or 'Суббота' or 'по субботам') in string:
    day = 'Saturday'

if ('в воскресенье' or 'каждое воскресенье' or 'воскресенье' or 'Воскресенье' or 'по воскресеньям') in string:
    day = 'Sunday'

if 'через неделю' in string:
    from datetime import date, timedelta, datetime
    week = date.today() + timedelta(days=7)
    print(week)

if 'через месяц' in string:
    month+=1

if 'через полгода' in string:
    month+=6

if 'через год' in string:
    year+=1

print(MESSAGE)


