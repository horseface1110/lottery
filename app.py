#from crypt import methods
from time import sleep
from tkinter import INSERT
from flask import Flask, redirect, url_for
from flask import render_template , request
from flask_bootstrap import Bootstrap
from sqlalchemy import false, null, true
from tomlkit import table
from tryy import hole
from tryy import login
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap(app)
account2 = ""
global friendListIsNull


########################SQlite#######################################

def sql():
    # connect to database
    conn = sqlite3.connect('sql.db')
 
    # create cursor object
    cursor = conn.cursor()
    friendListIsNull = null
    try:
        cursor.execute("SELECT * FROM " + account2 +";")      ###########account2
        records = cursor.fetchall()
        friendListIsNull = 1
        print('Table found!')

    except:
        friendListIsNull = 0
        print('Table not found!')

#########################送留言分頁###################################

@app.route('/message', methods=['GET', 'POST'])
def url():
    if request.method == 'POST':
        print('yes')
        if request.form.get('enter') == 'enter':
            print('yes2')
            print (request.form['url'] +'\n'+ request.form['number']+request.form['population']+request.form['message'])
            hole(request.form['url'] , int(request.form['number']) , int(request.form['population']) ,  request.form['message'] , int(request.form['ranking']))
        elif request.form.get('friend') =='friend':
            return redirect(url_for('add'))    ##幹到底三小
        
    return render_template('url.html')

#########################登入分頁######################################

@app.route('/' , methods=['GET' , 'POST'])
def loginweb():
    if request.method == 'POST':
        if request.form.get('enter') == 'enter':
            print("yes")
            try:
                print(request.form['account'] , request.form['password'] )
                login(request.form['account'] , request.form['password'] ) 
                loginisok = true
            except:
                loginisok = false
                return redirect(url_for('login' , fail = 'fail'))           ##兩個bug，登入尚未成功就跳下個分業，登入不成功跳出add
            if loginisok:
                global account2
                account2 = request.form['account'].replace('@' , '')
                account2 = account2.replace('.' , '')
                account2 = account2.replace('-' , '') 
                return redirect(url_for('url'))                           #為啥這裡是url而不是bootstrapmessage
    print(account2)       
    return render_template('login.html')

#########################好友表單分頁###################################


@app.route('/list', methods=['GET', 'POST'])
def add():
    # connect to database
    conn = sqlite3.connect('sql.db')
    # create cursor object
    cursor = conn.cursor()                             ################################
    try:                                                    
        cursor.execute("SELECT * FROM " + account2 +";")        
        data = cursor.fetchall()                         #####驗是否有表單#####
        friendListIsNull = 1          
        cursor.execute("SELECT max(rowid) from " + account2)
        friendNumber = cursor.fetchone()[0]                

    except:
        friendNumber = 0                                ################################

    if request.method == 'POST':
        if request.form.get('back') == 'back':
            return redirect(url_for('url'))
        if request.form.get('add') == 'add':                    
            name = request.form['name']
            # connect to database
            conn = sqlite3.connect('sql.db')
            # create cursor object
            cursor = conn.cursor()                             ################################
            try:                                                    
                cursor.execute("SELECT * FROM " + account2 +";")   
                data = cursor.fetchall()
                friendListIsNull = 1
                print('Table found!')                                  #####驗是否有表單#####
            except:
                friendListIsNull = 0
                print('Table not found!')      
            if friendListIsNull == 0:
                # Create table                                  ##################################
                cursor.execute( " CREATE TABLE " + account2 + "(id INTEGER NOT NULL PRIMARY KEY,friend TEXT NOT NULL);")
                print(name)
                print(account2)
            
            sql = """INSERT INTO """ + account2 + """(friend) VALUES ('""" + name + """')""" 
            #cursor.execute(sql)
            print(account2)
            cursor.execute("INSERT INTO " + account2 + " (friend) VALUES ('%s')" % (name))#添加變數的方式
            cursor.execute("SELECT max(rowid) from " + account2)
            friendNumber = cursor.fetchone()[0]
            data = cursor.fetchall()                        #取出人名
            conn.commit()
            cursor.close()
            return render_template('add.html' , friendNumber = friendNumber )

            
 
 
 
 
 
      
    return render_template('add.html' , friendNumber = friendNumber )

########################完結#################################

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)