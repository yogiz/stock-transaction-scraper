from ipotscrape import ipot_scrape
import time

i = 0
while True :
	ipot_scrape('bbca')
	i = i + 1
	print(i)
	time.sleep(300)