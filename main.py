from url_functions import *
from helper_functions import *


#Only works with lists
def display_data(data):
    for item in data:
        for key in item:
            print('{}: '.format(key) + str(item[key]))
        print('')


def main():
    cryptos = coins_list_api()
    exchanges = exchanges_api()

    print(coins_id_api('bitcoin'))
    #display_data(global_api())




if __name__ == "__main__":
    main()