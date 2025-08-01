import nobitex



def get_available_coins(data, coins_in_buy_page):
    available_coins = []

    for coin in data.keys():
        for network in data[coin].keys():
            if data[coin][network]["withdrawal_fee"] != "DISABLE" and coin in coins_in_buy_page:
                available_coins.append((coin, network))

    return available_coins

def find_minimum_withdrawal_fee(coin_data, available_coins, coin_prices):
    tether_amount = []

    for coin, network in available_coins:
        withdrawal_fee = coin_data[coin][network]["withdrawal_fee"]
        coin_p = coin_prices[coin]
        tether = round(withdrawal_fee * coin_p, 14)
        tether_amount.append((coin, tether, network))
    
    tether_amount = sorted(tether_amount, key=lambda x: x[1])
    print(tether_amount)

nob_data = nobitex.get_nobitex_coin_data()

coin_prices = nobitex.get_all_coin_prices()

avail_coins = get_available_coins(nob_data, coin_prices.keys())


minimum = find_minimum_withdrawal_fee(nob_data, avail_coins, coin_prices)

nobitex.shutdown()