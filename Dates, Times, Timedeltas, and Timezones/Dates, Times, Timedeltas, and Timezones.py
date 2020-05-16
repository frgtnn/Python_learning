# d = datetime.date(date which we want to have printed out)
# print(d)
# tday = datetime.date.today()
# print(tday) (prints out actual date where we are)
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7) # print(tday + tdelta) - it gives us a date a week later from a todays date, I can also use - to makes a week before
# print(tday.weekday()) # Monday is 0, Sunday is 6
# print(tday.isoweekday()) #Monday is 1, Sunday is 7
# date2 = date1 + timedelta
# timedelta = date1 + date2
# bday = datetime.date(2020, 7, 1)
# till_bday = bday - tday
# print(till_bday.total_seconds())      #calculaction how many days till my bday
# t = datetime.datetime - gives us acess to years, months, days, hours, minutes, seconds, and microseconds
# dt = datetime.datetime(2020, 5, 16, 18, 20, 45, 100000)
# tdelta = datetime.timedelta(hours=12)
# print(dt + tdelta)            #we are adding in this situation a twelve hours to our current hour which we give in datetime.datetime()
#
# dt_today= datetime.datetime.today()
# dt_now= datetime.datetime.now()
# dt_utcnow= datetime.datetime.utcnow()
#
# for tz in pytz.all_timezones:
#     print(tz) #shows all timezones
#
# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn) #prints out the time of US Moutain and gives us a difference between our time and time in US Moutain
#
# import datetime
# import pytz
# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# # print(dt_utcnow)
#
# dt_mtn = datetime.datetime.now(tz)
# mtn_tz = pytz.timezone('US/Mountain')
#
# dt_mtn = mtn_tz.localize(dt_mtn)
#
# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)
# # print(dt_mtn)

import datetime
import pytz

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'May 16, 2020'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

#strftime - Datetime to String
#strptime - String to Datetime