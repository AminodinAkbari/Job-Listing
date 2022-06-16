import datetime
today = datetime.datetime.now().date()
# a define for counting days until advertisiment(param in this define) expired
def Advertisement_time_left(param):
	ad_date = str(param.expired_in)
	ad_date = ad_date[:19]
	time = datetime.datetime.strptime(ad_date, '%Y-%m-%d %H:%M:%S').date()
	time_left = (time-today).days
	return time_left
