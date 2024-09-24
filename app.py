from flask import Flask, url_for, render_template, jsonify, request

app = Flask("__name__")

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/work")
def work():
    
    workNum = request.args.get("id")
    print(workNum)
    workData = {
        "name":"一目でわかる全国天気",
        "skill":"HTML、CSS、JavaScript",
        "API":"OpenWeatherAPI",
        "topImage":"work1.png",
        "detail":"""
                    <p>初めて自分で作った作品です。</p>
                    <p>制作した理由は、学校の授業で習ったHTML、CSS、JavaScriptを復習するために何か作れるものはないかと考えたときに全国の天気マップを思いついたからです。</p>
                    <p>1分ごとに自動更新される仕組みにしてリアルタイムで全国に天気を表示します。</p>
                """
    }
    return render_template("work.html", workData = workData)
    
    

if __name__ == "__main__":
    app.run(debug=True)