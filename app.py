from flask import Flask, url_for, render_template, jsonify, request
# import requests

app = Flask("__name__")


# def discord_notify(url, message):
#     """
#     Discord send message.

#     Args:
#         url (str): discord webhook url.
#         message (str): message.
#     """
#     if url:
#         requests.post(url,
#                     data={'content': message})


def workData():
    workData = [{
        "type": "サイト",
        "url": "work?id=0",
        "name": "一目でわかる全国天気",
        "skill": "HTML/CSS/JavaScript/OpenWeatherMap",
        "topImage": "work1.png",
        "workTime": "2日",
        "detail": """
                    <p>初めて自分で作った作品です。</p>
                    <p>制作した理由は、学校の授業で習ったHTML、CSS、JavaScriptを復習するために何か作れるものはないかと考えたときに全国の天気マップを思いついたからです。</p>
                    <p>1分ごとに自動更新される仕組みにしてリアルタイムで全国に天気を表示します。</p>
                """,
        "images": [],
        "detailText": """
        <div class="detailImage">
            <img src="static/images/work/top/work1.png" alt="">
        </div>
        <div class="comment">
            <ul>
                <li>・全国の現在の天気を見ることができます。</li>
                <li>・一分ごとにページの更新が行われ、最新の天気に変わります。</li>
            </ul>
        </div>
        """
    }, {
        "type": "サイト",
        "url": "work?id=1",
        "name": "洋服のECサイト「SHEEP」",
        "skill": "HTML/CSS/JavaScript/JQuery/Python/Flask/MySQL/GmailAPI",
        "topImage": "work2.png",
        "workTime": "3カ月",
        "detail": """
                    <p>学校の進級制作展というイベントに出展したグループ作品です。</p>
                    <p>リーダーに人生で初めて選ばれ、ドラフト形式で取ったメンバーでグループ制作をしました。</p>
                    <p>かなりつらい期間でしたが、Flaskの基礎を超えた部分やSQL文の書き方など詰め込んだりと、学校生活で一番成長をした期間になりました。</p>
                    <p>また、出展の際は既に存在しているECサイトなどから画像をダウンロードして表示していましたが、そのままポートフォリオサイトにサイトの画像を載せると著作権違反になるのでフリー画像に差し替えています。</p>
                    <p>画像提供:<a href='https://loosedrawing.com'>Loose Drawing様</a></p>
                """,
        "images": [
            "work10", "work11", "work12", "work14", "work15", "work16"
        ],
        "detailText": """
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
                        <li>・個数の変更、購入する商品を選ぶことができます。</li>
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
    }, {
        "type": "アプリ",
        "url": "work?id=2",
        "name": "ローマ字を打たなくても検索できる50音キーボード",
        "skill": "Python/Tkinter/SQLite/pyaudio/SpeechRecognition",
        "topImage": "work3.png",
        "workTime": "1カ月",
        "detail": """
                        <p>U-22プログラミングコンテスト2024に出した作品です。</p>
                        <p>ローマ字がわからなくても押して文字が打てるようにというコンセプトで作りました。</p>
                        <p>更に文字の場所を変更できる機能や音声入力の機能を作りました。</p>
                        <p初めてのTkinterを使ったアプリ開発だったのでとても苦戦しました。</p>
                    """,
        "images": [
                "work10", "work11", "work12", "work14", "work15", "work16"
        ],
        "detailText": """
                    <h2>キーボード画面</h2>
                    <div class="detailImage">
                        <img src="static/images/work/top/work3.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work20.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work21.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work22.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・検索エンジンを選ぶことができます。</li>
                            <li>・検索の横のボタンを押すと音声読み取りになります。</li>
                            <li>・平仮名、カタカナ、英語、記号のキーボードがあります。</li>
                            <li>・下のボタンでキーボードを変えたり、配置を変える画面を出したりすることができます。</li>
                        </ul>
                    </div>
                    <h2>音声読み取り画面</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work23.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work24.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・Pyaudioでマイクから音声を読み取り、音声ファイルを一時保存してSpeechRecognitionで音声ファイルを解析して文字起こしをしています。</li>
                        </ul>
                    </div>
                    <h2>ボタン配置入れ替え画面</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work25.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work26.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・1回目に押したボタンと2回目に押したボタンの配置を入れ替えることができます。</li>
                            <li>・2枚目の画像は「×」と空白の場所を入れ替えた後の画像です。</li>
                        </ul>
                    </div>
                    
                    """
    }, {
        "type": "サイト",
        "url": "work?id=3",
        "name": "クッションのECサイト「softNest」",
        "skill": "Python/Django/MySQL",
        "topImage": "work4.png",
        "workTime": "2週間",
        "detail": """
                        <p>Djangoを学んだのでアウトプットをしてみようと思って作ったサイトです。</p>
                        <p>Djangoのフォルダやファイル、コードなどは調べながら書いたりすることができたのですが、データベースの操作のコードがSQL文ではなく独特なものでとても難しかったです。
                        <p>サイトは今回見やすさを重視しようと思ったのでシンプルなデザインで作ってみました。</p>
                    """,
        "images": [
                "work10", "work11", "work12", "work14", "work15", "work16"
        ],
        "detailText": """
                    <h2>トップページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/top/work4.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work30.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work33.png" alt="">
                    </div>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work34.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・各ページに飛ぶことができます。</li>
                        </ul>
                    </div>
                    <h2>商品一覧ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work31.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・人気順や登録日付順、値段順にソートをすることができます。</li>
                            <li>・ヘッダーの虫眼鏡を押すと検索バーが上から出てくるようにしました。</li>
                        </ul>
                    </div>
                    <h2>商品ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work32.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・ハートマークを押すとお気に入りリストに追加することができます。</li>
                            <li>・色とサイズを選んでカートに入れたり、購入することができます。選ばずにカートに入れたり購入しようとすると「選択してください」とアラートが出るようになっています。</li>
                            <li>・在庫切れの状態だとボタンを押せないようにしました。</li>
                        </ul>
                    </div>
                    <h2>カートページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work35.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・ハートマークを押すとお気に入りリストに追加することができます。</li>
                            <li>・色とサイズを選んでカートに入れたり、購入することができます。選ばずにカートに入れたり購入しようとすると「選択してください」とアラートが出るようになっています。</li>
                            <li>・在庫切れの状態だとボタンを押せないようにしました。</li>
                        </ul>
                    </div>
                    <h2>購入履歴ページ</h2>
                    <div class="detailImage">
                        <img src="static/images/work/subImage/work36.png" alt="">
                    </div>
                    <div class="comment">
                        <ul>
                            <li>・購入した商品を日付ごとに見ることができます。</li>
                        </ul>
                    </div>
                    """
    }, {
        "type": "サイト",
        "url": "work?id=4",
        "name": "今日見た夢を投稿しあうSNSサイト「dreamDiary」",
        "skill": "HTML/CSS/JavaScript/React/Python/Flask/MySQL",
        "topImage": "work5.png",
        "workTime": "？",
        "detail": """
                        <p>Reactに興味があり、Reactを使ってサイトを作ってみたくなり、このSNSサイトを作り始めました。</p>
                        
                    """,
        "detailText": """
                    <p class="comment">制作中...</p>
                    """
    },
    ]
    return workData


@app.route("/")
def home():
    page = "home"
    # discord_notify("https://discord.com/api/webhooks/1289073253171859540/DUonHHnEJezOg0VxMIA9TeqsYJobm9IPkFs8c8IMO4MhoviYV_M7Una0tYu3BWBgVzCC", 'ポートフォリオサイトにアクセスがあったよ！')
    return render_template("index.html", workData=workData(), page=page)


@app.route("/work")
def work():
    page = "work"
    workNum = int(request.args.get("id"))
    print(workNum)
    return render_template("work.html", workData=workData()[workNum], page=page)


if __name__ == "__main__":
    app.run(debug=True)
