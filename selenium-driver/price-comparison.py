from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source1 = "https://www.flipkart.com/search?q=iphone+14+pro+max&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone+14+pro+max%7CMobiles&requestId=2fb9b490-76c7-48d7-ba8d-d5cc1a95ff49&as-backfill=on"
source2 = "https://www.amazon.in/s?k=iphone+14+pro+max&crid=OBSRBJT9JTBA&sprefix=iphone+14%2Caps%2C591&ref=nb_sb_ss_ts-doa-p_3_9"
source3 = "https://www.croma.com/search/?q=iphone%2014%20pro%20max%3Arelevance%3AZAStatusFlag%3Atrue%3AexcludeOOSFlag&text=iphone%2014%20pro%20max"

# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
wd = webdriver.Chrome(r'D:\chromedriver\chromedriver.exe',options=CO)
print ("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")

print ("Connecting to Flipkart")
wd.get(source1)
wd.implicitly_wait(wait_imp)
f_price = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
pr_name = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product = pr_name.text
r_price = f_price.text
# print (r_price[1:])
print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
wd.get(source2)
wd.implicitly_wait(wait_imp)
# a_price = wd.find_element_by_id("priceblock_ourprice")
a_price = wd.find_element_by_xpath("/html/body/div[4]/div[2]/div[4]/div[10]/div[12]/div/table/tbody/tr[2]/td[2]/span[1]")
raw_p = a_price.text
# print (raw_p[2:8])
print (" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)

print("Connecting to Croma")
wd.get(source3)
wd.implicitly_wait(wait_imp)
c_price = wd.find_element_by_xpath("/html/body/main/div[5]/div[1]/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/div/div/span")
raw_c = c_price.text
# print (raw_c[1:7])
print (" ---> Successfully retrieved the price from Croma\n")
time.sleep(2)

# Final display
print ("#------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+r_price[1:])
print("  Price available at Amazon is: "+raw_p[2:8])
print("   Price available at Croma is: "+raw_c[1:7])
