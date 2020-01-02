from ipotscrape import scrape_to_csv, scrape_to_db

mode = 0 			# mode 0 save to db, mode 1 save to csv 
symbols = ['adhi','adro','akra','antm','asii','asri','bbca','bbni','bbri','bbtn','bksl','bmri','bsde','cpin','elsa','excl','ggrm','hmsp','icbp','inco','indf','indy','inkp','intp','itmg','jsmr','klbf','lpkr','lppf','medc','mncn','pgas','ptba','ptpp','scma','smgr','sril','ssms','tlkm','tpia','untr','unvr','wika','wsbp','wskt','jast']

for symbol in symbols :
	if(mode == 0) :
		scrape_to_db(symbol)
	elif (mode == 1) :
		scrape_to_csv(symbol)
	else :
		print('wrong mode!')
