import datetime
import time

jan_1_1970 = datetime.datetime(1970, 1, 1) # Iniatialize a date
today = datetime.datetime.today() # Get today's date
seconds = (today - jan_1_1970).total_seconds() # Get the difference in seconds

print('Seconds since January 1, 1970:', "{:,.4f}".format(seconds) + ' or ' + "{:.3}".format(seconds) + ' in scientific notation') # "{:,}".format(seconds) formats the number with the parameter
print(today.strftime("%b %d %Y"))    # Print today's date