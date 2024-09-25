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
                    <p>リーダーに人生で初めて選ばれ、ドラフト形式で取ったメンバーでグループ制作をしました。</p>
                    <p>グループ作品なのですが、メンバーに「Flaskを書くことができない」や「データベースを書きたくない」と言われたり、期限を守らない人が出てきたりしたので、穴埋めをしていたらいつの間にかフロントエンドのほとんど、バックエンドすべてを僕が担当していました。</p>
                    <p>かなりつらい期間でしたが、それだけではなくFlaskの基礎を超えた部分やSQL文の書き方など詰め込んだりと、学校生活で一番成長をした期間になりました。</p>
                    <p>また、出展の際は既に存在しているECサイトなどから画像をダウンロードして表示していましたが、そのままポートフォリオサイトにサイトの画像を載せると著作権違反になるのでフリー画像に差し替えています。</p>
                    <p>画像提供:<a href='https://loosedrawing.com'>Loose Drawing様</a></p>
                """,
        "images":[
            "work10","work11","work12","work14","work15","work16"
        ],
        "detailText":"""
                <h2>Topページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/top/work2.png" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・サイトの各ページに飛べます。</li>
                        <li>・スライドショーは人気TOP30になっています。</li>
                        <li>・サイトの管理者は羊のロゴを押すとサイトデータが見れるページに飛べるようになっています。</li>
                    </ul>
                </div>
                <h2>商品一覧ページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work10.png') }}" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・商品を検索できます。</li>
                        <li>・左サイドで性別、服の種類で絞ることができます。</li>
                        <li>・右上の絞り込みからソートができます。</li>
                    </ul>
                </div>
                <h2>商品一覧ページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work11.png" alt="">
                </div>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work12.png" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・商品の色、サイズを選んだ後カートに入れる、購入ができます。。</li>
                        <li>・ハートマークを押すことでお気に入りリストに入れることができます。</li>
                        <li>・レビューを送信することができます。</li>
                    </ul>
                </div>
                <h2>カートページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work13.png" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・カートに入れた商品を購入することができます。</li>
                        <li>・個数の変更、購入する商品をwラブことができます。</li>
                        <li>・登録されている住所はアカウント作成時に入力をした住所、お届け先指定の場合は入力することができます。</li>
                    </ul>
                </div>
                <h2>SHEEP管理ページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work14.png" alt="">
                </div>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work15.png" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・サイトの訪問者数や全体の売上データ、コンバージョン率を見ることができます。</li>
                        <li>・他にもユーザーの管理や商品管理、送られてきたお問い合わせもみることはできますが、デザインが間に合いませんでした。</li>
                        <li>・お知らせ更新はhtmlファイルを送信してお知らせのページを追加したり、追加したページの表示非表示もできるようにしました。</li>
                    </ul>
                </div>
                <h2>ユーザーの売上管理ページ</h2>
                <div class="detailImage">
                    <img src="static/images/work/subImage/work16.png" alt="">
                </div>
                <div class="comment">
                    <ul>
                        <li>・自分で出品した商品の売り上げを見たり、商品の在庫を増やしたりできます。</li>
                    </ul>
                </div>
                
                """
            },{
            "name":"ローマ字を打たなくても検索できる50音キーボード",
            "skill":"Python/Tkinter/SQLite/pyaudio/SpeechRecognition",
            "topImage":"work3.png",
            "workTime":"1カ月",
            "detail":"""
                        <p>U-22プログラミングコンテスト2024に出した作品です。</p>
                        <p>ローマ字がわからなくても押して文字が打てるようにというコンセプトで作りました。</p>
                        <p>更に文字の場所を変更できる機能や音声入力の機能を作りました。</p>
                        <p初めてのTkinterを使ったアプリ開発だったのでとても苦戦しました。</p>
                    """,
            "images":[
                "work10","work11","work12","work14","work15","work16"
            ],
            "detailText":"""
                    <h2>キーボード画面</h2>
                    <div class="detailImage">
                        <img src="static/images/work/top/work2.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・サイトの各ページに飛べます。</li>
                            <li>・スライドショーは人気TOP30になっています。</li>
                            <li>・サイトの管理者は羊のロゴを押すとサイトデータが見れるページに飛べるようになっています。</li>
                        </ul>
                    </div>
                    <h2>商品一覧ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work10.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・商品を検索できます。</li>
                            <li>・左サイドで性別、服の種類で絞ることができます。</li>
                            <li>・右上の絞り込みからソートができます。</li>
                        </ul>
                    </div>
                    <h2>商品一覧ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work11.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work12.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・商品の色、サイズを選んだ後カートに入れる、購入ができます。。</li>
                            <li>・ハートマークを押すことでお気に入りリストに入れることができます。</li>
                            <li>・レビューを送信することができます。</li>
                        </ul>
                    </div>
                    <h2>カートページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work13.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・カートに入れた商品を購入することができます。</li>
                            <li>・個数の変更、購入する商品をwラブことができます。</li>
                            <li>・登録されている住所はアカウント作成時に入力をした住所、お届け先指定の場合は入力することができます。</li>
                        </ul>
                    </div>
                    <h2>SHEEP管理ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work14.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work15.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・サイトの訪問者数や全体の売上データ、コンバージョン率を見ることができます。</li>
                            <li>・他にもユーザーの管理や商品管理、送られてきたお問い合わせもみることはできますが、デザインが間に合いませんでした。</li>
                            <li>・お知らせ更新はhtmlファイルを送信してお知らせのページを追加したり、追加したページの表示非表示もできるようにしました。</li>
                        </ul>
                    </div>
                    <h2>ユーザーの売上管理ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work16.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・自分で出品した商品の売り上げを見たり、商品の在庫を増やしたりできます。</li>
                        </ul>
                    </div>
                    
                    """
            },
            
                ]
    return render_template("work.html", workData = workData[workNum])
    
    

if __name__ == "__main__":
    app.run(debug=True)