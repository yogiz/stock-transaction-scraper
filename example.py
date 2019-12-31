from ipotscrape import scrape_to_csv, scrape_to_db

mode = 0 			# mode 0 save to db, mode 1 save to csv 
symbols = ['bbca', 'ggrm', 'jast']

for symbol in symbols :
	if(mode == 0) :
		scrape_to_db(symbol)
	elif (mode == 1) :
		scrape_to_csv(symbol)
	else :
		print('wrong mode!')