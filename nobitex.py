from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import defaultdict

options = Options()
options.add_argument("--headless")  
options.add_argument("--no-sandbox")
driver = None

def set_chrome():
    driver = webdriver.Chrome(options=options)

def set_firefox():
    driver = webdriver.Firefox(options=options)

def set_edge():
    driver = webdriver.Edge(options=options)

def set_safari():
    driver = webdriver.Safari(options=options)

def shutdown():
    driver.quit()

def get_nobitex_coin_data():



    dataset = defaultdict(dict)

    
    def pack_coin_data(datas:list[str]):
        coin_name = datas[0].split("\n")[1]
        network = ""
        withdrawal_fee = 0.0
        minimum_withdrawal = 0.0
        minimum_deposite = 0.0
        deposite_fee = 0.0
        for i in range(1, len(datas)):
            if i % 5 == 1:
                network = datas[i]
            if i % 5 == 2:

                withdrawal_fee = "DISABLE" if datas[i] == "تعلیق" else float(datas[i].split("\n")[1].replace(",",""))
            if i % 5 == 3:
                minimum_withdrawal = "DISABLE" if datas[i] == "تعلیق" else float(datas[i].split("\n")[1].replace(",",""))
            if i % 5 == 4:
                if datas[i] == "تعلیق":
                    deposite_fee = "DISABLE"
                elif datas[i] == "0":
                    deposite_fee = 0.0
                else:
                    deposite_fee = float(datas[i].split("\n")[1].replace(",",""))
            if i % 5 == 0:
                if datas[i] == "تعلیق":
                    minimum_deposite = "DISABLE"
                elif datas[i] == "":
                    minimum_deposite = 0.0
                else:
                    minimum_deposite = float(datas[i].split("\n")[1])
                dataset[coin_name][network] = {
                    "withdrawal_fee": withdrawal_fee,
                    "minimum_withdrawal": minimum_withdrawal,
                    "deposite_fee": deposite_fee,
                    "minimum_deposite": minimum_deposite
                }


                


    try:
        url = "https://nobitex.ir/pricing/"
        driver.get(url)

        timeout = 15
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, """/html/body/article/div/section[2]/table/tbody""")))

        tbody = driver.find_element(By.XPATH, """/html/body/article/div/section[2]/table/tbody""")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) < 5:
                continue 

            datas = [i.text for i in cols]
            pack_coin_data(datas)

    except Exception as e:
        print(e)               

    return dataset


def get_all_coin_prices():


    url = "https://nobitex.ir/buy/"

    driver.get(url)
    coin_prices = defaultdict()

    tether_btn = driver.find_element(By.XPATH, """/html/body/main/article/section[1]/div/div[2]/div[1]/div[1]/button[2]""")

    tether_btn.click()

    coin_list = driver.find_element(By.XPATH, """//*[@id="currency-data"]/div/div[4]/table[2]/tbody""")
    coins = coin_list.find_elements(By.TAG_NAME, "tr")

    for coin in coins:
        cols = coin.find_elements(By.TAG_NAME, "td")
        cols_text = [i.text for i in cols]
        coin_name = cols_text[0].split("\n")[0]
        coin_price = float(cols_text[1].split("\n")[0].removeprefix("USDT").replace(",", ""))
        coin_prices[coin_name] = coin_price

    return coin_prices

