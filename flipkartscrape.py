from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
mobilename=[]
price=[]

productslink=[]
#description=[]
driver= webdriver.Chrome()

driver.get("https://www.flipkart.com/search?q=mobile%20under%2010000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
time.sleep(4)

for d in range(1,11):
    time.sleep(2)
    box=driver.find_element(By.CLASS_NAME,"QSCKDh")
    time.sleep(3)

    k=box.find_elements(By.CLASS_NAME,"RG5Slk")

    for n in k:
        mobilename.append(n.text)
    #print(len(mobilename))


    p=box.find_elements(By.CLASS_NAME,"hZ3P6w")
    for c in p:
        price.append(c.text)
    #print(len(price))

    productlink=box.find_elements(By.CLASS_NAME,"k7wcnx")

    for l in productlink:
        productslink.append(l.get_attribute("href"))
    #print(len(productslink))
    

    c=box.find_element(By.XPATH,"""//*[@id="container"]/div/div[3]/div[1]/div[2]/div[26]/div/div/nav/a[11]""").click()
    
    time.sleep(5)
#d=box.find_elements(By.CLASS_NAME,"MKiFS6")

#for q in d:
#    ratings.append(q.text)
#print(len(ratings))

#g=box.find_elements(By.CLASS_NAME,"DTBslk")

#for u in g:
#    description.append(u.text)
#print(len(description))


df=pd.DataFrame({
    "Mobile":mobilename,
    "Price":price,
    "Productlink":productslink,
   # "Description":description
})

df.to_csv("flipkar_scrape.csv",index=False)
print(df)





driver.quit()






















