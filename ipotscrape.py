from bs4 import BeautifulSoup as bs
import pandas as pd
import requests, time, pendulum, os
from db import insert_data
from time import ctime

datahead = ['time','price','open','high','low','avg','lot','change','b1','b2','b3','b4','b5','b6','bl1','bl2','bl3','bl4','bl5','bl6','o1','o2','o3','o4','o5','o6','ol1','ol2','ol3','ol4','ol5','ol6','btotal','ototal']
datahead_str = 'time,price,open,high,low,avg,lot,change,b1,b2,b3,b4,b5,b6,bl1,bl2,bl3,bl4,bl5,bl6,o1,o2,o3,o4,o5,o6,ol1,ol2,ol3,ol4,ol5,ol6,btotal,ototal'

def get_data(simbol):

    url = f'https://www.indopremier.com/ipotgo/newsSmartSearch.php?code={simbol}'
    page = requests.get(url)
    soup = bs(page.content,'html.parser')


    table_umum = soup.select_one('#main > section > div > div.row.mincol-8 > div.col.col-md-10.col-md-offset-1.col-lg-8.col-lg-offset-0 > div > div.col.col-sm-4.col-lg-4 > div > div.panel-collapse.pull.out > div > div.pr5.pt5 > table')
    df_umum = pd.read_html(str(table_umum))
    df_umum = df_umum[0]

    price = soup.select_one('#main > section > div > div.row.mincol-8 > div.col.col-md-10.col-md-offset-1.col-lg-8.col-lg-offset-0 > div > div.col.col-sm-4.col-lg-4 > div > div.panel-heading > div > table > tbody > tr > td:nth-of-type(2)')
    
    now = int(time.time())
    price = int(price.text.replace(',',''))
    open_data = int(df_umum.iloc[0,4])
    high = int(df_umum.iloc[1,4])
    low = int(df_umum.iloc[2,4])
    avg = int(df_umum.iloc[2,7])
    change = df_umum.iloc[2,1]
    check_lot = check_million(df_umum.iloc[0,7])
    lot = int(check_lot)


    dresult = [now,price,open_data,high,low,avg,lot,change,]

    table_deep = soup.select_one('#main > section > div > div.row.mincol-8 > div.col.col-md-10.col-md-offset-1.col-lg-8.col-lg-offset-0 > div > div.col.col-sm-4.col-lg-4 > div > div.panel-collapse.pull.out > div > table')
    df_deep = pd.read_html(str(table_deep))
    df_deep = df_deep[0]
    # cols = [0,5]
    # df_deep.drop(df_deep.columns[cols],axis=1,inplace=True)
    # print(df_deep)


    for i in range(6):
        data = df_deep.at[i,'Bid' ]
        dresult.append(int(data))

    for i in range(6):
        data = df_deep.at[i,'BidLot' ]
        dresult.append(int(data))

    for i in range(6):
        data = df_deep.at[i,'Offer' ]
        dresult.append(int(data))

    for i in range(6):
        data = df_deep.at[i,'OffLot' ]
        dresult.append(int(data))

    last = df_deep[-1:]
    btotal = last['BidLot'].values
    ototal = last['OffLot'].values

    # convert total if more than million
    btotal = check_million(btotal)
    ototal = check_million(ototal)

    dresult.append(int(btotal))
    dresult.append(int(ototal))

    return dresult

def check_million(data):
    if (isinstance(data[0], str)):
        string = data[0].replace(' M','')
        result = float(string) * 1000000
    else :
        result = data
    return result
    

def cek_jam_trading(holiday) :

    curTime = int(time.time())
    curTime = pendulum.from_timestamp(curTime, 'Asia/Jakarta')
    hari  = int(curTime.strftime('%w'))
    jam = int(curTime.strftime('%H%M'))
    tgl_bulan = int(curTime.strftime('%m%d'))
    
    if tgl_bulan in holiday :
        return False
    if hari > 0 and hari < 5 :
        if jam >= 900 and jam <= 1200 :
            return True
        elif jam >= 1330 and jam <= 1549 :
            return True
        else :
            return False

    elif hari == 5 :
        if jam >= 900 and jam <= 1130 :
            return True
        elif jam >= 1400 and jam <= 1549 :
            return True
        else :
            return False
    else:
        return False

def scrape_to_csv(symbol):
    file_ada = os.path.isfile(f'{symbol}.csv')
    if  file_ada == False :
        with open(f'{symbol}.csv', 'w') as f:
            f.write(datahead_str + '\n')

    result = get_data(symbol)
    with open(f'{symbol}.csv', 'a') as f:
        for sell in result:
            f.write(str(sell))
            if sell != result[-1]:
                f.write(',')
        f.write('\n')

def scrape_to_db(symbol):
    data = get_data(symbol)
    data = tuple(data)
    result = tuple(int(el) for el in data)
    insert_data(symbol, result)

def write_log(message) :
	with open('scraper.log', 'a') as f :
		now = ctime()
		f.writelines(now + '  -  '+ message + '\n')

def run_scraper(symbols, mode, check_market_time, holiday):
    if (check_market_time) :
        isTime = cek_jam_trading(holiday)
    else :
        isTime = True

    if (isTime) :
        try :
            for symbol in symbols :
                if(mode == 0) :
                    scrape_to_db(symbol)
                elif (mode == 1) :
                    scrape_to_csv(symbol)
                else :
                    write_log('wrong mode!')
            if (mode == 0) :    
                write_log('success scrape to db')
            elif (mode == 1) :
                write_log('success scrape to csv')

        except :
            write_log('Error!')

    else :
        write_log('market still close')
