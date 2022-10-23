# shiny for Python

R語言的 shiny 套件可以建立跨平台的互動式網頁，今年（2022）RStudio 研討會宣佈 shiny for Python, 表示在 Python 環境亦可執行 shiny 建立互動式網頁。

PyPI shiny: https://pypi.org/project/shiny/

# 執行結果

![image](https://github.com/rwepa/shiny_python/blob/main/imgs/shiny_python.png)

# Youtube 說明

![image](https://github.com/rwepa/shiny_python/blob/main/imgs/shiny_python_youtube.png)

https://youtu.be/s2fgEAa6lq0

# PDF講義

1. RWEPA 簡介
2. 資料分析架構APC方法
3. 資料分析與視覺化應用
4. shiny 簡介
5. shiny for Python 實作篇1 - my_app
6. shiny for Python 實作篇2 – 01_hello 
7. 結論

https://github.com/rwepa/shiny_python/blob/main/shiny_python_tutorial.pdf

# Python 程式

https://github.com/rwepa/shiny_python/blob/main/pyshiny_01_hello.py

# 檔案架構

+ shiny 一般以資料夾方式儲存, 本例為 pyshiny_01_hello 資料夾

+ Python 主程式: pyshiny_01_hello.py, 程式名稱不一定是 app.py

+ Python 主程式路徑: D:\shinydemo\pyshiny_01_hello\pyshiny_01_hello.py

# 執行方式

+ Windows 開啟命令提示字元，輸入以下內容

+ d:

+ cd shinydemo

+ shiny run --reload pyshiny_01_hello/pyshiny_01_hello.py

+ 瀏覽器: http://localhost:8000/ 

![image](https://github.com/rwepa/shiny_python/blob/main/imgs/shiny_python_cmd.png)

###### \#end
