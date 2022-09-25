import os
import datetime
import requests
import urllib
import pytz
import datetime as dt
from re import search
import sched, time
import subprocess

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    localtz=pytz.timezone('Asia/Kuala_Lumpur')
    now = dt.datetime.now()
    now= localtz.localize(now)
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    url = 'https://www.lazada.com.my/products/pre-order-delivery-in-14-days-enhanced-touch-n-go-card-to-be-released-by-batches-i3175099305-s16072707014.html?clickTrackInfo=undefined&search=1&spm=a2o4k.searchlistbrand.list.i23.48bd7e73Sd6gx9'
    url_response = urllib.request.urlopen(url)
    url_contents = url_response.read()
    content_out_of_stock = url_contents[269300:270000].decode("utf-8")

    substring = "Out of stock"
    result = ""
    counter = 0

    if search(substring, content_out_of_stock):
        result = "No Stock!"
        print ("No Stock!")
        counter = 0
    else:
        result = "Got Stock"
        print (">>>>>>>>>>>>>>>>>>>>> Got Stock >>>>>>>>>>>>>>>>>>>>>>>")
        if(counter <= 5):
            counter += 1
    
    f = open(r"./log.txt","a")
    f.writelines(date_time + '[info]: ' + result + " " + content_out_of_stock + '\n')
    f.close()
    print('bye')

while(1):
    s.enter(60, 1, do_something, (s,))
    s.run()


# subprocess.Popen(r'explorer /select,"C:\"')

# "><div class="pdp-cart-concern"><button class="add-to-cart-buy-now-btn full-btn pdp-button pdp-button_type_text pdp-button_theme_gray pdp-button_size_xl"><span class="pdp-button-text"><svg class="lazadaicon lazada-icon svgfont button-inner-icon" aria-hidden="true">
# "><div class="pdp-cart-concern"><button class="add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_yellow pdp-button_size_xl"><span class="pdp-button-text"><span class="">Buy Now</span></span></button><button class="add-to-cart-buy-now-btn  pdp-button pdp-button_type_text pdp-button_theme_orange pdp-button_size_xl"><span class="pdp-button-text"><span class="">Add to Cart</span></span></button><form method="post" action=""><input type="hidden" name="buyParams" 
