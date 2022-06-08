'''
- if closing of a candle will be greater than opening of it it will be green and if closing will be lower than opening the candle will be red
- ShadowDown in green candles= openPrice - lowPrice
- ShadowDown in red candles= closeprice-lowPrice
-ShadowUp in green candles = highprice-closePrice
-shadowUp in red candles = highprice-openPrice
-red candle is when open is bigger than close
-green candle is when close is bigger than open
if shadow down / (shadowup+shadowbody+shadowdown)> 0.4 its hammer 
if shadow up / whole candle >0.4 its inverted hammer
'''

eth_close=[1826,1814,1817,1821,1880,1938,1930,1929,1941,1934]
eth_open=[1814,1817,1821,1880,1938,1930,1929,1941,1934,1988]
eth_low=[1802,1805,1763,1807,1879,1924,1913,1927,1934,1925]
eth_high=[1837,1835,1843,1880,1972,1944,1945,1958,1959,1999]

counter=int(input("Enter candle position: "))
green_shadow_down = eth_open[counter] -eth_low[counter]
red_shadow_down=eth_close[counter]-eth_low[counter]
green_shadow_up=eth_high[counter]-eth_close[counter]
red_shadow_up=eth_high[counter]-eth_open[counter]
green_body=eth_close[counter]-eth_open[counter]
red_body=eth_open[counter]-eth_close[counter]
if eth_close[counter]>eth_open[counter]:
    if green_shadow_down / (eth_high[counter]-eth_low[counter])>0.4:
        print("candle is green Hammer and its buy position")
    elif green_shadow_up / (eth_high[counter]-eth_low[counter])>0.4:
        print("Candle is green inverted hammer sell position ")
if eth_close[counter]<eth_open[counter]:
    if red_shadow_down / (eth_high[counter]-eth_low[counter])>0.4:
        print("candle is red Hammer and its buy position")
    if red_shadow_up / (eth_high[counter]-eth_low[counter])>0.4:
        print("Candle is red inverted hammer sell position ")
    else:
        print("none")









































# if eth_close[counter]>eth_open[counter] and  :
    
# shadowDown=eth_open[counter]-eth_low[counter]
# shadowUp=ethH10Days[counter]-ethO10Days[counter]
# if shadowDown > shadowUp:
#     print("Buy")
# elif shadowUp > shadowDown :
#         print("sell")
# else:
#     print("no trade")
        
