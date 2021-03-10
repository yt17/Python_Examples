from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
lst=[]
#driver.get("https://eksisozluk.com/cecilia-zandalasini--5393965")

for i in range(1,5):
    lnk="https://eksisozluk.com/fenerbahce--33409?p=" + str(i)
    print(lnk);
    driver.get(lnk)
    time.sleep(5)
    #driver.close()
    elements=driver.find_elements_by_class_name("content")

    for x in elements:
        lst.append(x.text)
        lst.append("---------")
        #print(x.text)
        #print("----------------------")


driver.close()
text_file = open("test.txt", "w")


#for x in lst:
#    print(x)    
#    print("--------")
    

with open("entry.txt","w",encoding="UTF-8") as file:
    for x in lst:
        file.write(str(x)+".\n")






