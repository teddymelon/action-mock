from flask import Flask

app = Flask(__name__) 
app.config["DEBUG"] = True #會啟動Flask的Debug模式
app.config["JSON_AS_ASCII"] = False #解決Flask中文亂碼的問題


@app.route("/", methods=["GET"])
def index():
    print("Hello World")

    return "Hello World-1111"


if __name__ == "__main__": #如果以主程式執行
    app.run(host="0.0.0.0", port=2000) #則立刻啟動伺服器 #run是Flask的Function，後面可以接host跟port。
