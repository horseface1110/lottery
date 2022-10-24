from cgitb import text
import email
from email import message
from lib2to3.pgen2 import driver
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3

 

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")    #block咚咚
#options.add_argument('--headless')                 #屋頭模式


####################初始化#############################


#acount = input("your acount")
#password = input("your password")
#url = input("url of the article")
#message = input("what to 留言:")
#times = input("how many times in a message")
#total = input("how many message you want to leave")
accountworld = ''
url = "https://www.facebook.com/permalink.php?story_fbid=pfbid0vPcY5QY4oe29z4xv2CnhrEf65B6gKdcmGbeChMULrYjy3VT5s5HFK7qp25aoVK7kl&id=100013014283308"
message_ = "哭哭哭哭眼淚是珍珠"
times = 2
total = 2


#####################登入臉書###########################

def login(account , password_ ):
    # connect to database
    conn = sqlite3.connect('sql.db')
    # create cursor object
    cursor = conn.cursor()
    global driver
    driver = webdriver.Chrome(chrome_options=options , executable_path='./chromedriver')
    #global driver
    #driver = webdriver.Chrome(chrome_options=options )
    driver.get("https://www.facebook.com/")
    email = driver.find_element_by_name("email")
    email.send_keys(account)
    password = driver.find_element_by_name("pass")
    password.send_keys(password_)
    login = driver.find_element_by_name("login").click()
    # login.onclick()
    global accountworld 
    accountworld = account.replace('@' , '')
    accountworld = accountworld.replace('.' , '')
    accountworld = accountworld.replace('-' , '')
    print(accountworld)
    
    
######################新的###############################
    
def hole(url , total , times , message_ , numberName):
    #####################獲取id最大值#######################
    # connect to database
    conn = sqlite3.connect('sql.db')
    # create cursor object
    cursor = conn.cursor()
    #driver = webdriver.Chrome(chrome_options=options , executable_path='./chromedriver')
    cursor.execute("SELECT MAX(id) FROM " + accountworld)
    rows = cursor.fetchall()

    for row in rows:
        maxNumberName = row[0]
        
    print(maxNumberName)
    #####################進入貼文###########################
    driver.get(url)
    sleep(1)

    textbox = driver.find_elements_by_css_selector("[aria-label='留言']")[1]   #因為有兩個 所以加s 然後用陣列的感覺
    
    
    for i in range(0,total ):
        for j in range(0,times):
            try:
                cursor.execute("SELECT * FROM "+ accountworld +" WHERE id = " + str(numberName) )
                #print("numberName =" + str(numberName)) 
            except:
                print("fail2")
            try:
                rows = cursor.fetchall()
            except:
                print("fail")
            textbox.send_keys("@")
            for row in rows:
                textbox.send_keys(row[1])
                print(row[1])
            sleep(2)
            textbox.send_keys(Keys.ENTER)    
            #print("numberName +=" + str(numberName))
            numberName +=1
            if maxNumberName == 2 and numberName == 3:
                numberName = 1
            elif numberName == maxNumberName:
                numberName==1        
            elif numberName == 2 and maxNumberName == 1 :
                numberName = 1     
            
        textbox.send_keys(" " + message_)
        #print(message_)
        textbox.send_keys(Keys.ENTER)


    
    
    sleep(10)
    


#####################進入貼文###########################



    
    

#textbox.send_keys("@")
#textbox.send_keys("念誠")
#sleep(2)
#textbox.send_keys(Keys.ENTER)
#Stextbox.send_keys(Keys.ENTER)
#textbox.send_keys(Keys.ARROW_RIGHT)


##################住解######################

#textbox.send_keys(Keys.ENTER)   #enter 輸入
#for i in range(0,total):
#        for j in range(0,times):
#            textbox.send_keys("@")
#            textbox.send_keys("吳仲倫")
#            sleep(2)
#            textbox.send_keys(Keys.ENTER)    
#        textbox.send_keys(" " + message_)
#        textbox.send_keys(Keys.ENTER)







