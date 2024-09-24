from flask import Flask, url_for, render_template, jsonify, request

app = Flask("__name__")

@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/work")
def work():
    
    workNum = int(request.args.get("id"))
    print(workNum)
    workData = [{
        "name":"一目でわかる全国天気",
        "skill":"HTML/CSS/JavaScript/OpenWeatherMap",
        "topImage":"work1.png",
        "workTime":"2日",
        "detail":"""
                    <p>初めて自分で作った作品です。</p>
                    <p>制作した理由は、学校の授業で習ったHTML、CSS、JavaScriptを復習するために何か作れるものはないかと考えたときに全国の天気マップを思いついたからです。</p>
                    <p>1分ごとに自動更新される仕組みにしてリアルタイムで全国に天気を表示します。</p>
                """,
        "images":[],
        "detailText":""
            }, {
        "name":"洋服のECサイト「SHEEP」",
        "skill":"HTML/CSS/JavaScript/JQuery/Python/Flask/MySQL/GmailAPI",
        "topImage":"work2.png",
        "workTime":"3カ月",
        "detail":"""
                    <p>学校の進級制作展というイベントに出展したグループ作品です。</p>
                    <p>リーダーに人生で初めて選ばれ、ドラフト形式で取ったメンバーでグループ制作をしました。
                    <p>グループ作品なのですが、メンバーに「Flaskを書くことができない」や「データベースを書きたくない」と言われたり、期限を守らない人が出てきたりしたので、穴埋めをしていたらいつの間にかフロントエンドのほとんど、バックエンドすべてを僕が担当していました。</p>
                    <p>かなりつらい期間でしたが、それだけではなくFlaskの基礎を超えた部分やSQL文の書き方など詰め込んだりと、学校生活で一番成長をした期間になりました。</p>
                    <p>また、出展の際は既に存在しているECサイトなどから画像をダウンロードして表示していましたが、そのままポートフォリオサイトにサイトの画像を載せると著作権違反になるのでフリー画像に差し替えています。</p>
                    <p>画像提供:<a href='https://loosedrawing.com'>Loose Drawing様</a></p>
                """,
        "images":[
            "work10","work11","work12","work14","work15","work16"
        ],
        "detailText":"""
                <h1>サイト構成</h1>
                
                """
            }
                ]
    return render_template("work.html", workData = workData[workNum])
    
    

if __name__ == "__main__":
    app.run(debug=True)