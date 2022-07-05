#from crypt import methods
from tkinter import INSERT
from flask import Flask, redirect, url_for
from flask import render_template , request
from flask_bootstrap import Bootstrap
from sqlalchemy import null
from tomlkit import table
from tryy import hole
from tryy import login
import sqlite3

app = Flask(__name__)
bootstrap = Bootstrap(app)
account = "oloomb6@gmail.com"         #############  account 記得要切掉非字母數字的東西
account2 = "oloomb6gmailcom"
password_ = "omwarbuc34"

########################SQlite#######################################

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
        if request.form.get('enter') == 'enter':
            print (request.form['url'] +'\n'+ request.form['number'])
            hole(request.form['url'] , int(request.form['number']) , int(request.form['population']) ,  request.form['message'] )
        elif request.form.get('friend') =='friend':
            return redirect(url_for('add'))
        
    return render_template('url.html')

#########################登入分頁######################################

@app.route('/' , methods=['GET' , 'POST'])
def loginweb():
    if request.method == 'POST':
        if request.form.get('enter') == 'enter':
            print(request.form['account'] , request.form['password'] )
            login(request.form['account'] , request.form['password'] )    
            return render_template('url.html')
    return render_template('login.html')

#########################好友表單分頁###################################


@app.route('/list', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if request.form.get('back') == 'back':
            return redirect(url_for('url'))
        if request.form.get('add') == 'add':                    
            name = request.form['name']
            # connect to database
            conn = sqlite3.connect('sql.db')
            # create cursor object
            cursor = conn.cursor()
            friendListIsNull = null                              ################################
            try:                                                    
                cursor.execute("SELECT * FROM " + account2 +";")        
                records = cursor.fetchall()
                friendListIsNull = 1
                print('Table found!')                                  #####驗是否有表單#####
            except:
                friendListIsNull = 0
                print('Table not found!')      
            if friendListIsNull == 0:
                # Create table                                  ##################################
                cursor.execute( " CREATE TABLE " + account2 + "(id INTEGER NOT NULL PRIMARY KEY,friend TEXT NOT NULL);")
                print(name)
            
            sql = """INSERT INTO """ + account2 + """(friend) VALUES ('""" + name + """')""" 
            count = cursor.execute(sql)
            conn.commit()
            cursor.close()
            
            
 
 
 
 
 
      
    return render_template('add.html')

########################完結#################################

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)