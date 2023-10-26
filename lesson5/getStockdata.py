import requests
import pprint
url="https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha"

header={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',


'Cookie':
's=ay12o2jyxr; xq_a_token=e2f0876e8fd368a0be2b6d38a49ed2dd5eec7557; xq_r_token=2a5b753b2db675b4ac36c938d20120660651116d; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTcwMDY5OTg3NSwiY3RtIjoxNjk4MjYzNzY0MDY3LCJjaWQiOiJkOWQwbjRBWnVwIn0.icNVNcEpONehCpZq5JQNa8VQZVde7a_vSnQ8APzfzDkmFgZqtilb56EQCcpA0JyqDNULWvgholpYhXB3PoSmmqojtwv4_C3XtTgz2ehiKIbsBkiwU9azQdJnIyDG0g_wRjSs634QPHxXUetqzJibyUsR8-8b7CD-4wbFNWZIjCEcv28ckRWHBAHiRgWhJt96uUVm6O5Y4GY8B3jYjgK6Oh9YH_WRGGHHaM8s0FxHK1TDXu3oG_dMPWh1XktonTbv8cLdjVpLr9Fs-kZ0zZyJ1-_PJz-vgI45dsONV_82R9Ee9bSoZ8802uSmUnQzqsqjVQbLSfuVzDnXnyMXScdnpw; cookiesu=181698263817425; u=181698263817425; device_id=c103b7452621a65bc7c85d9a2f7df372; Hm_lvt_1db88642e346389874251b5a1eded6e3=1698263820; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1698263820'

}

response=requests.get(url=url,headers=header)
json_data=response.json()
#print(json_data)
# pprint.pprint(json_data)
data_list=json_data['data']['list']
for data in data_list:

    # print(data)
    data1=data['symbol']
    data2=data['name']
    data3=data['current']
    data4=data['chg']
    if data4:
        if float(data4)>0:
            data4='+'+str(data4)
        else:
            data4=str(data4)

    data5=str(data['percent'])+'%'
    data6=data['current_year_percent']
    #data7=data['percent']
    data7=data['volume']
    data8=data['amount']
    data9=data['turnover_rate']
    data10=data['pe_ttm']
    data11=data['dividend_yield']
    if data11:
        data11=str(data['dividend_yield'])+'%'
    data12=data['market_capital']
    print(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12)
    data_tict={'sysbol':data1,'name':data2,'current':data3,'chg':data4,'':data1,,'':data1,'':data1,'':data1,'':data1,'':data1,'':data1,}
    



