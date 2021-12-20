import cbpro
import time
import numpy as np
import datetime
from datetime import timedelta
from pygame import mixer
import smtplib
from email.message import EmailMessage
import pandas as pd

mixer.init()
alert = mixer.Sound('bell.wav')

data = open('InfoCB.csv', 'r').read().splitlines()
secret_key_extract, public_key_extract, passphrase_extract = (data[0], data[1], data[2])
secret_key, public_key, passphrase = (secret_key_extract[8:], public_key_extract[7:], passphrase_extract[11:])
auth_client = cbpro.AuthenticatedClient(public_key, secret_key, passphrase)

product = 'USDT-GBP'
current_price_of_product = auth_client.get_product_ticker(product)['price']
current_bid_price = auth_client.get_product_ticker(product)['bid']
current_ask_price = auth_client.get_product_ticker(product)['ask']
bid_ask_spread = float(((float(current_ask_price) - float(current_bid_price)) / float(current_ask_price)) * 100)

# Amount to initially invest
accounts = auth_client.get_accounts()
gbp_account = next(item for item in accounts if item["currency"] == "GBP")
initInvestment = 10
funding = initInvestment


def get_account_id(currency_trading):
    for element in auth_client.get_accounts():
        if element['currency'] == currency_trading[:currency_trading.index("-")]:
            return element['id']


def get_accounts():
    extract = auth_client.get_accounts()
    gbp_account = next(item for item in extract if item["currency"] == "GBP")
    amount_in_account = float(gbp_account['balance'])
    return amount_in_account


def get_historic_data(currency, granularity):
    # Avoid API timeout:
    time_adjustment = granularity / 60
    start_time_1, end_time_1 = ((datetime.datetime.now() - timedelta(hours=time_adjustment, minutes=0)).isoformat(),
                                datetime.datetime.now().isoformat())
    start_time_2, end_time_2 = ((datetime.datetime.now() - timedelta(hours=2 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=time_adjustment, minutes=0)).isoformat())
    start_time_3, end_time_3 = ((datetime.datetime.now() - timedelta(hours=3 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=2 * time_adjustment, minutes=0)).isoformat())
    start_time_4, end_time_4 = ((datetime.datetime.now() - timedelta(hours=4 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=3 * time_adjustment, minutes=0)).isoformat())
    start_time_5, end_time_5 = ((datetime.datetime.now() - timedelta(hours=5 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=4 * time_adjustment, minutes=0)).isoformat())
    start_time_6, end_time_6 = ((datetime.datetime.now() - timedelta(hours=6 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=4 * time_adjustment, minutes=0)).isoformat())
    start_time_7, end_time_7 = ((datetime.datetime.now() - timedelta(hours=7 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=6 * time_adjustment, minutes=0)).isoformat())
    start_time_8, end_time_8 = ((datetime.datetime.now() - timedelta(hours=8 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=7 * time_adjustment, minutes=0)).isoformat())
    start_time_9, end_time_9 = ((datetime.datetime.now() - timedelta(hours=9 * time_adjustment, minutes=0)).isoformat(),
                                (datetime.datetime.now() - timedelta(hours=8 * time_adjustment, minutes=0)).isoformat())
    start_time_10, end_time_10 = ((datetime.datetime.now() - timedelta(hours=10 * time_adjustment, minutes=0))
                                  .isoformat(), (datetime.datetime.now() - timedelta(hours=9 * time_adjustment,
                                                                                     minutes=0)).isoformat())
    start_time_11, end_time_11 = ((datetime.datetime.now() - timedelta(hours=11 * time_adjustment, minutes=0))
                                  .isoformat(), (datetime.datetime.now() - timedelta(hours=10 * time_adjustment,
                                                                                     minutes=0)).isoformat())
    start_time_12, end_time_12 = ((datetime.datetime.now() - timedelta(hours=12 * time_adjustment, minutes=0))
                                  .isoformat(), (datetime.datetime.now() - timedelta(hours=11 * time_adjustment,
                                                                                     minutes=0)).isoformat())

    # position 0 recent, last position latest:
    historic_data_1 = auth_client.get_product_historic_rates(currency, start=start_time_1, end=end_time_1,
                                                             granularity=granularity)
    historic_data_2 = auth_client.get_product_historic_rates(currency, start=start_time_2, end=end_time_2,
                                                             granularity=granularity)
    historic_data_3 = auth_client.get_product_historic_rates(currency, start=start_time_3, end=end_time_3,
                                                             granularity=granularity)
    historic_data_4 = auth_client.get_product_historic_rates(currency, start=start_time_4, end=end_time_4,
                                                             granularity=granularity)
    historic_data_5 = auth_client.get_product_historic_rates(currency, start=start_time_5, end=end_time_5,
                                                             granularity=granularity)
    historic_data_6 = auth_client.get_product_historic_rates(currency, start=start_time_6, end=end_time_6,
                                                             granularity=granularity)
    historic_data_7 = auth_client.get_product_historic_rates(currency, start=start_time_7, end=end_time_7,
                                                             granularity=granularity)
    historic_data_8 = auth_client.get_product_historic_rates(currency, start=start_time_8, end=end_time_8,
                                                             granularity=granularity)
    historic_data_9 = auth_client.get_product_historic_rates(currency, start=start_time_9, end=end_time_9,
                                                             granularity=granularity)
    historic_data_10 = auth_client.get_product_historic_rates(currency, start=start_time_10, end=end_time_10,
                                                              granularity=granularity)
    historic_data_11 = auth_client.get_product_historic_rates(currency, start=start_time_11, end=end_time_11,
                                                              granularity=granularity)
    historic_data_12 = auth_client.get_product_historic_rates(currency, start=start_time_12, end=end_time_12,
                                                              granularity=granularity)

    # Open and Close data:
    historic_data_1_open, historic_data_2_open, historic_data_3_open, historic_data_4_open, \
        historic_data_5_open, historic_data_6_open, historic_data_7_open, historic_data_8_open, \
        historic_data_9_open, historic_data_10_open, historic_data_11_open, historic_data_12_open = \
        ([], [], [], [], [], [], [], [], [], [], [], [])
    historic_data_1_close, historic_data_2_close, historic_data_3_close, historic_data_4_close, \
        historic_data_5_close, historic_data_6_close, historic_data_7_close, historic_data_8_close, \
        historic_data_9_close, historic_data_10_close, historic_data_11_close, historic_data_12_close = \
        ([], [], [], [], [], [], [], [], [], [], [], [])
    historic_data_1_high, historic_data_2_high, historic_data_3_high, historic_data_4_high, \
        historic_data_5_high, historic_data_6_high, historic_data_7_high, historic_data_8_high, \
        historic_data_9_high, historic_data_10_high, historic_data_11_high, historic_data_12_high = \
        ([], [], [], [], [], [], [], [], [], [], [], [])
    historic_data_1_low, historic_data_2_low, historic_data_3_low, historic_data_4_low, \
        historic_data_5_low, historic_data_6_low, historic_data_7_low, historic_data_8_low, \
        historic_data_9_low, historic_data_10_low, historic_data_11_low, historic_data_12_low = \
        ([], [], [], [], [], [], [], [], [], [], [], [])

    for element_1 in historic_data_1:
        historic_data_1_low.append(element_1[1])
        historic_data_1_high.append(element_1[2])
        historic_data_1_open.append(element_1[3])
        historic_data_1_close.append(element_1[4])
    for element_2 in historic_data_2:
        historic_data_2_low.append(element_2[1])
        historic_data_2_high.append(element_2[2])
        historic_data_2_open.append(element_2[3])
        historic_data_2_close.append(element_2[4])
    for element_3 in historic_data_3:
        historic_data_3_low.append(element_3[1])
        historic_data_3_high.append(element_3[2])
        historic_data_3_open.append(element_3[3])
        historic_data_3_close.append(element_3[4])
    for element_4 in historic_data_4:
        historic_data_4_low.append(element_4[1])
        historic_data_4_high.append(element_4[2])
        historic_data_4_open.append(element_4[3])
        historic_data_4_close.append(element_4[4])
    for element_5 in historic_data_5:
        historic_data_5_low.append(element_5[1])
        historic_data_5_high.append(element_5[2])
        historic_data_5_open.append(element_5[3])
        historic_data_5_close.append(element_5[4])
    for element_6 in historic_data_6:
        historic_data_6_low.append(element_6[1])
        historic_data_6_high.append(element_6[2])
        historic_data_6_open.append(element_6[3])
        historic_data_6_close.append(element_6[4])
    for element_7 in historic_data_7:
        historic_data_7_low.append(element_7[1])
        historic_data_7_high.append(element_7[2])
        historic_data_7_open.append(element_7[3])
        historic_data_7_close.append(element_7[4])
    for element_8 in historic_data_8:
        historic_data_8_low.append(element_8[1])
        historic_data_8_high.append(element_8[2])
        historic_data_8_open.append(element_8[3])
        historic_data_8_close.append(element_8[4])
    for element_9 in historic_data_9:
        historic_data_9_low.append(element_9[1])
        historic_data_9_high.append(element_9[2])
        historic_data_9_open.append(element_9[3])
        historic_data_9_close.append(element_9[4])
    for element_10 in historic_data_10:
        historic_data_10_low.append(element_10[1])
        historic_data_10_high.append(element_10[2])
        historic_data_10_open.append(element_10[3])
        historic_data_10_close.append(element_10[4])
    for element_11 in historic_data_11:
        historic_data_11_low.append(element_11[1])
        historic_data_11_high.append(element_11[2])
        historic_data_11_open.append(element_11[3])
        historic_data_11_close.append(element_11[4])
    for element_12 in historic_data_12:
        historic_data_12_low.append(element_12[1])
        historic_data_12_high.append(element_12[2])
        historic_data_12_open.append(element_12[3])
        historic_data_12_close.append(element_12[4])

    historic_open_data = np.concatenate((historic_data_12_open, historic_data_11_open, historic_data_10_open,
                                         historic_data_9_open, historic_data_8_open, historic_data_7_open,
                                         historic_data_6_open, historic_data_5_open, historic_data_4_open,
                                         historic_data_3_open, historic_data_2_open, historic_data_1_open), axis=0)
    historic_close_data = np.concatenate((historic_data_12_close, historic_data_11_close, historic_data_10_close,
                                          historic_data_9_close, historic_data_8_close, historic_data_7_close,
                                          historic_data_6_close, historic_data_5_close, historic_data_4_close,
                                          historic_data_3_close, historic_data_2_close, historic_data_1_close), axis=0)
    historic_low_data = np.concatenate((historic_data_12_low, historic_data_11_low, historic_data_10_low,
                                        historic_data_9_low, historic_data_8_low, historic_data_7_low,
                                        historic_data_6_low, historic_data_5_low, historic_data_4_low,
                                        historic_data_3_low, historic_data_2_low, historic_data_1_low), axis=0)
    historic_high_data = np.concatenate((historic_data_12_high, historic_data_11_high, historic_data_10_high,
                                         historic_data_9_high, historic_data_8_high, historic_data_7_high,
                                         historic_data_6_high, historic_data_5_high, historic_data_4_high,
                                         historic_data_3_high, historic_data_2_high, historic_data_1_high), axis=0)

    return historic_open_data, historic_close_data, historic_low_data, historic_high_data, historic_open_data[-1], \
           historic_close_data[-1], historic_low_data[-1], historic_high_data[-1], historic_data_1, historic_data_2, \
           historic_data_3, historic_data_4, historic_data_5, historic_data_6, historic_data_7, historic_data_8, \
           historic_data_9, historic_data_10, historic_data_11, historic_data_12


def sma_indicator(prices, sma_step):
    data_close = pd.Series(prices)
    sma = data_close.rolling(window=sma_step, min_periods=sma_step)
    sma = sma.mean()
    sma = list(sma)
    sma = sma[sma_step - 1:]
    sma = np.asarray(sma)
    sma_recent = sma[0]
    sma_before = sma[1]
    return sma, sma_recent, sma_before


def check_if_increasing(input):
    result = all(i < j for i, j in zip(input[0:], input[5:]))
    return result


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    user = "detailretriever@gmail.com"
    msg['from'] = user
    password = "MachineBot_2021"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()


def test_colour(opendata, closedata, lowdata, highdata):
    if opendata[0] > closedata[0]:  # RED
        print("Current Red\n")
        return "Red"
    elif opendata[0] < closedata[0]:  # GREEN
        print("Current Green")
        return "Green"
    elif opendata[0] == closedata[0] == lowdata[0] == highdata[0]:  # LINE
        print("Line\n")
        return "Line"
    else:
        pass


specificID = get_account_id(product)
buy_counter = 0
buy_price = 0

while True:
    newData = auth_client.get_product_ticker(product_id=product)
    currentPrice = newData['price']
    currentPrice = format(float(currentPrice), '.5f')
    currentBuy = newData['ask']
    currentSell = newData['bid']
    possiblePurchase = (float(initInvestment)) / float(currentSell)
    owned = float(auth_client.get_account(specificID)['available'])
    possibleIncomeSell = float(currentSell) * owned

    # 1 - minute channel:
    (open_data_1m, close_data_1m, low_data_1m, high_data_1m, recent_open_1m, recent_close_1m, recent_low_1m,
     recent_high_1m, hist_data1_1m, hist_data2_1m, hist_data3_1m, hist_data4_1m, hist_data5_1m, hist_data6_1m,
     hist_data7_1m, hist_data8_1m, hist_data9_1m, hist_data10_1m, hist_data11_1m, hist_data12_1m) = \
        get_historic_data(product, 60)
    all_hist_data_1m = np.concatenate((hist_data1_1m, hist_data2_1m, hist_data3_1m, hist_data4_1m, hist_data5_1m,
                                       hist_data6_1m, hist_data7_1m, hist_data8_1m, hist_data9_1m, hist_data10_1m,
                                       hist_data11_1m, hist_data12_1m), axis=0)

    close_data_1m_update, open_data_1m_update, low_data_1m_update, previous_6lows, previous_6candles, \
        previous_6sma1m50, previous_6sma1m10, candle_sticks_1m, high_data_1m_update, previous_6highs = \
        ([], [], [], [], [], [], [], [], [], [])

    for element in all_hist_data_1m:
        candle_sticks_1m.append(element[1:5])
    for candles in candle_sticks_1m:
        close_data_1m_update.append(candles[3])
        open_data_1m_update.append(candles[2])
        high_data_1m_update.append(candles[1])
        low_data_1m_update.append((candles[0]))
    for candle in close_data_1m_update[0:5]:
        previous_6candles.append(candle)
    for i in low_data_1m_update[0:5]:
        previous_6lows.append(i)
    for j in high_data_1m_update[0:5]:
        previous_6highs.append(j)

    sma_1m_10, sma_1m_10_recent, sma_1m_10_before = sma_indicator(close_data_1m_update, 10)  # FASTER MOVEMENTS
    sma_1m_50, sma_1m_50_recent, sma_1m_50_before = sma_indicator(close_data_1m_update, 50)  # OVERALL TREND

    for j in sma_1m_50[0:5]:
        previous_6sma1m50.append(j)
    for k in sma_1m_10[0:5]:
        previous_6sma1m10.append(k)

    result = test_colour(open_data_1m_update, close_data_1m_update, low_data_1m_update, high_data_1m_update)

    if (previous_6lows[0] > previous_6sma1m50[0] and previous_6lows[0] > previous_6sma1m10[0]) and \
            (sma_1m_50_before > sma_1m_10_before and sma_1m_50_recent < sma_1m_10_recent and (result == 'Green' or (
                    result == 'Line' and open_data_1m_update[0] > (sma_1m_50_recent and sma_1m_10_recent)))):
        try:
            order = auth_client.place_market_order(product_id=product, side='buy', funds=str(funding))
            buy_price = currentBuy
            funding = 0
        except Exception as e:
            print(f"Error placing order: {e}")
            funding = initInvestment
        try:
            check = order['id']
            check_order = auth_client.get_order(order_id=check)
            print(check_order)
        except Exception as e:
            print(f"Unable to check order, may have been rejected: {e}")
            funding = initInvestment

        message_alert = f"A buy trigger has just been established. Current price: {current_price_of_product}." \
                        f"Current buy price: {currentBuy}. Current sell price: {currentSell}."
        email_alert("Buy Trigger", message_alert, "detailretriever@gmail.com")
        buy_counter += 1
    if float(currentSell) <= float(buy_price) - 0.0016:
        if owned > 0.0:
            auth_client.place_market_order(product_id=product, side='sell', size=str(owned))
            print("Stop Loss Triggered. Closing all positions now.")
            email_alert("Stop Loss Triggered", "Closing all positions now.", "detailretriever@gmail.com")
            funding = initInvestment
            buy_price = 0

    if float(currentSell) >= float(buy_price) + 0.0004:
        if owned > 0.0:
            auth_client.place_market_order(product_id=product, side='sell', size=str(owned))
            print("Take Profit Triggered. Closing all positions now.")
            email_alert("Take Profit Triggered", "Closing all positions now.", "detailretriever@gmail.com")
            funding = initInvestment
            buy_price = 0

    print(f"\nBuy triggers: {buy_counter}")
    print("Current price: ", current_price_of_product)
    print("My funds: £", funding)
    print("I own: ", owned, "USDT\n")
    print("----------------------------------------\n")

    time.sleep(1)

