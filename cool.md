# 酷酷邏輯
 * ```
   while isRun:
    
    cursor.execute('SELECT * FROM `try`;')
    records = cursor.fetchall()
    
    for r in records:
        print(r)
    
    ctrl = input(appDesc)
    if ctrl == '0':
        isRun = False
    elif ctrl == '1':
        pass
    elif ctrl == '2':
        pass
    elif ctrl == '3':
        pass   
   ```
   做一個可以改動條件的無窮迴圈，令一個變數為TRUE確保迴圈繼續，再依照輸入調整變數的值，視狀況結束迴圈


# 連線到splite
 * ```
   # connect to database
   con = sqlite3.connect('資料庫名稱.db')
 
   #create cursor object
    cur = con.cursor()
   ```