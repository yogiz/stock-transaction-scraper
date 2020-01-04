from ipotscrape import run_scraper

mode = 0 			# mode 0 save to db, mode 1 save to csv 
symbols = ['adhi','adro','akra','antm','asii','asri','bbca','bbni','bbri','bbtn','bksl','bmri','bsde','cpin','elsa','excl','ggrm','hmsp','icbp','inco','indf','indy','inkp','intp','itmg','jsmr','klbf','lpkr','lppf','medc','mncn','pgas','ptba','ptpp','scma','smgr','sril','ssms','tlkm','tpia','untr','unvr','wika','wsbp','wskt','jast']

check_market_time = False

run_scraper(symbols, mode, check_market_time)
