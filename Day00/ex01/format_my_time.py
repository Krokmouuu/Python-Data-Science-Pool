import datetime as dt

jan_1_1970 = dt.datetime(1970, 1, 1)
# Iniatialize a date
today = dt.datetime.today()
# Get today's date
seconds = (today - jan_1_1970).total_seconds()
# Get the difference in seconds

print('Seconds since January 1, 1970:', "{:,.4f}".format(seconds), end='')
print(' or ' + "{:.3}".format(seconds) + ' in scientific notation')
# "{:,}".format(seconds) formats the number with the parameter
print(today.strftime("%b %d %Y"))
# Print today's date
