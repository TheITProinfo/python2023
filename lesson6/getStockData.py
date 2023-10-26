# https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha
import requests
import pprint
import csv


file=open('stockdata.csv',mode='a',encoding='utf-8',newline='')
csv_write=csv.DictWriter(file,fieldnames=['symbol','name','current','chg','percent','current_year_percent','volume','amount','turnover_rate','pe_ttm','dividend_yield','market_capital'])

csv_write.writeheader() # wite csv file header

for page in range(1,58):

    print('++++++++++++++++++++++++++++++ it is processing data on page {}'.format(page))
    url='https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page={}&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha'.format(str(page))

    header={'User-Agent':
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36',

    'Cookie':
    'xq_a_token=e2f0876e8fd368a0be2b6d38a49ed2dd5eec7557; xqat=e2f0876e8fd368a0be2b6d38a49ed2dd5eec7557; xq_r_token=2a5b753b2db675b4ac36c938d20120660651116d; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwMDY5OTg3NSwiY3RtIjoxNjk4Mjc0Njc2Njc4LCJjaWQiOiJkOWQwbjRBWnVwIn0.Pay7MdzxV26gjL4WBvYx4YnVOsoZaP1XbNQZHpcGHr_8OdGe_8IpA8Qo8i9SXQRAikZeSDhIH4fzRoP-iVMhoV6rMwxxQ3GlHnNn4L66HzQnn7uAUAo6uFKnJK2Khr9RqlZyFO-shHgRZFDPAUH7BI4NLlroJqnVquo_oMPgXRlasRT35ghTz12G7emD8xjfcEt1nFYNModjVS14b1-y3-VOfwpiSTJc51EIwbQs_3-_QZMfa_P2CrTAJleGzAltqOVgTZ5nabUyely7GfX9yeyUCDHnxTExxcaIt6eRP13Ksx-bByb5iS_IoLlIL36ban1CWqny0DNrKkfEb4XEyQ; cookiesu=271698274727558; u=271698274727558; device_id=b53f5a9e29be59da244425ab29555242;'

    }
    data_dict={}
    ## encapusaltion head and url
    response=requests.get(url=url,headers=header)
    #print(response)
    # get Jaon object
    json_data=response.json()
    #print(json_data)
    #pprint.pprint(json_data)

    # get list data
    data_list=json_data['data']['list']
    #pprint.pprint(data_list)
    for data in data_list:
        data_dict={}
        data1=data['symbol']
        data2=data['name']
        data3=data['current']
        data4=data['chg']
        if data4:
            if(float(data4))>0:
                data4='+'+ str(data4)
            else:
                data4=str(data4)    
        data5=str(data['percent'])+'%'
        data6=str(data['current_year_percent'])+'%'
        data7=data['volume']
        data8=data['amount']
        data9=str(data['turnover_rate'])+'%'
        data10=data['pe_ttm']
        data11=data['dividend_yield']
        if data11:
            data11=str(data['dividend_yield'])+'%'
        else:
            data11=None
        data12=data['market_capital']
        #print(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12)
        data_dict={'symbol':data1,'name':data2,'current':data3,'chg':data4,'percent':data5,'current_year_percent':data6,'volume':data7,'amount':data8,'turnover_rate':data9,'pe_ttm':data10,'dividend_yield':data11,'market_capital':data12}
        #print(data_dict)
        csv_write.writerow(data_dict)
