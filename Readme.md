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


# 環境搭建
* pip install Flask-SQLAlchemy
* pip install tomlkit
* https://chromedriver.storage.googleapis.com/index.html?path=107.0.5304.62/
* 要有chrome
* pip install selenium
* <font color = "dd0000">find_element_By_Name -> find_element ( By.Name , " " ) </font>
   需先```from selenium.webdriver.common.by import By```
   詳細請參考網頁：https://www.selenium.dev/documentation/webdriver/elements/finders/



# flask
url_for()裡面放的是py函式名稱。

# 連線到splite
 * ```
   # connect to database
   con = sqlite3.connect('資料庫名稱.db')
 
   #create cursor object
    cur = con.cursor()
   ```

# Bootstrap教學
* https://www.youtube.com/watch?v=hKR3Wu6ARSg&list=PLqivELodHt3jq3oWBZfdhMu0GE7774HBW&index=2&ab_channel=CSScoke
*  採用Bootatrap 5
## 安裝方式
### 簡易版 CDN
1. Docs -> 右側 Start template
2. 將整個程式碼複製並儲存
3. 簡單方式就完成了
4. 檢視是否完成：新增一個按鈕
   ```
   <a href = "#" class = "btn btn-info">按鈕</a>
   ```
### 複雜版

1. 進官網Download頁面
2. 下載Css and js
3. 將下載的東西解壓縮放在html檔同一個資料夾
4. 將簡易版的Bootstrap Css的link置換
   ```
   <link rel = "stylesheet" type = "text/css" href="css/bootstrap.min.css">
   ```
5. 第二個script置換
   ```
   <script src="js/bootstrap.min.js"></script>
   ```
6. 到第一個script的url，另存網頁新檔，放在剛剛的js檔裡面
7. 第一個script置換
   ```
   <script src="js/popper.min.js"></script>
   ```
## 格線系統
1. 之後說

# Boottrap 實作
 基礎模板  
https://www.youtube.com/watch?v=YX6KZIcUeY8&list=PLqivELodHt3jq3oWBZfdhMu0GE7774HBW&ab_channel=CSScoke
```
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link rel = "stylesheet" type = "text/css" href="css/bootstrap.min.css">
 
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <a href = "#" class = "btn btn-info">按鈕</a>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <!--<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    -->
    <!-- Option 2: Separate Popper and Bootstrap JS -->
    
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```
## 輸入框(每一個都付有button及預設文字的)
1. 小知識:html檔用.abc可快速寫出class
2. 輸入框 https://getbootstrap.com/docs/5.0/forms/input-group/
3. 先建立class="container" class="row"
4. 最大欄位12，col-6設欄位為6，mx-auto置中，my-5留一些空位
```
<div class="col-6 mx-auto my-5">
```
5. 輸入框提示在placeholder

## 表單(可用於登入介面的那種)
1. 連結 https://getbootstrap.com/docs/5.0/forms/overview/
2. 有挑選功能，下拉選單協助輸入功能，唯讀、禁用
3. bootstrap 水平分割線 https://www.twblogs.net/a/5c9587f1bd9eee491b61fc42
4. row 容器置中 https://campus-xoops.tn.edu.tw/modules/tad_book3/html.php?tbdsn=937 
```
<div class="row align-items-center">

```

## 按鈕
1. 一般按鈕
   https://getbootstrap.com/docs/5.0/components/buttons/ 

   按鈕組件
   https://getbootstrap.com/docs/5.0/components/button-group/

## 表單table
1. table https://bootstrap5.hexschool.com/docs/5.0/content/tables/
2. 或是list group https://getbootstrap.com/docs/5.0/components/list-group/
3. 基礎格式
```
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```
4. 灰白相間做法
```
<table class="table table-striped">
```
5. 帶顏色作法
```
<table class="table table-success table-striped">
```
# bootstrap 與 flask 融合方式
```
<head>
<link rel = "stylesheet" type = "text/css" href="/static/css/bootstrap.min.css">
</head>
<body>
<script src="/static/js/popper.min.js"></script>
<script src="/static/js/bootstrap.min.js"></script>
</body>
```
## 小提醒
要讓html回傳資料，
```
<form method='post' action="#"> 
```

# Sqlite 
* 查詢表單行數
```
cursor.execute("SELECT max(rowid) from " + account2)
            friendNumber = cursor.fetchone()[0]
```
