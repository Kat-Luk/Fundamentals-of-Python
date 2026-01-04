# You're part of a startup company that develops software. Your team holds a daily stand-up meeting on weekdays only (Monday–Friday). You need a little utility that, given a start date (string in the DD.MM.YYYY format) and an integer N, returns the next N stand-up dates (as a list of strings in the DD.MM.YYYY format), including the start date, if applicable.
# Create a function next_standup_dates( start_date, n ) that does exactly that.

from datetime import datetime, timedelta
def next_standup_dates(start_date, n):
        dates=[]
        start = datetime.strptime(start_date,"%d.%m.%Y")
        week = start.strftime("%w")
        i = 0
        while (i != n):
            if week == "0" or week == "6":
               start = start+timedelta(days=1)
            else:
                dates.append(start.strftime("%d.%m.%Y"))
                start = start+timedelta(days=1)
                i += 1
            week = start.strftime("%w")
        return dates 