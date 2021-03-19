from url_functions import *
from helper_functions import *

#Returns dict
#Customizable coins/{id}/history API call
def coins_id_history_api(id, date, localization='true'):
    url = ('https://api.coingecko.com/api/v3/coins/' + id +
          '/history?date=' + date +
          '&localization=' + localization)

    data = request_url(url)
    return data

#Returns dict
#Customizable coins/{id}/market_chart API call
def coins_id_market_chart_api(id, vs_currency, days='1', interval='hourly'):
    url = ('https://api.coingecko.com/api/v3/coins/' + id +
          '/market_chart?vs_currency=' + vs_currency +
          '&days=' + days +
          '&interval=' + interval)

    data = request_url(url)
    return data

#Returns dict
#Customizable coins/{id}/market_chart/range API call
def coins_id_market_chart_range_api(id, vs_currency, from_unix, to_unix):
    url = ('https://api.coingecko.com/api/v3/coins/' + id +
          '/market_chart/range?vs_currency=' + vs_currency +
          '&from=' + from_unix +
          '&to=' + to_unix)

    data = request_url(url)
    return data


#Only works with lists
def display_data(data):
    for item in data:
        for key in item:
            print('{}: '.format(key) + str(item[key]))
        print('')


def main():
    cryptos = coins_list_api()
    exchanges = exchanges_api()


def get_market_date():
    date_input = input("Enter a date in MM-DD-YYYY format:")

    history_date = '31-12-2018'
    return coins_id_history_api('bitcoin', history_date)

#Call coins_id_market_chart_range_api to get data in range
def get_market_range():
    pass

#Call coins_id_market_chart_api to get the last 7d, 30d, 1y, max, etc.
def get_market_recent():
    pass


    #print(coins_id_api('bitcoin'))
    #display_data(global_api())




if __name__ == "__main__":
    main()