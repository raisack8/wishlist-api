# FRONTのリポジトリはこちら
https://github.com/raisack8/wishlist-front

cd .\fastapi\
.venv/Scripts/activate
uvicorn main:app --reload

### iphoneで動作確認するためにローカルネットワークを指定して起動
cd .\fastapi\
.venv/Scripts/activate
uvicorn main:app --reload --host 192.168.0.18 --port 8000
##### React側 URL : http://192.168.0.18:3000/

##### react側では下記のように.envファイルで環境変数を定義している
##### REACT_APP_API_BASE_URL = 'http://192.168.0.18:8000'

## タスクはこちらで管理
https://github.com/users/raisack8/projects/3/views/1



# レコード作成例。テストデータをこうやって追加しよう
ses.add(Shohin(shohin_no = 1, name='アイス', price=280))
ses.add(Shohin(shohin_no = 2, name='ケーキ', price=350))
ses.add(Shohin(shohin_no = 3, name='パフェ', price=780))
ses.add(Shohin(shohin_no = 4, name='モンブラン', price=420))

ses.add(Zaiko(shop_no = 1, shohin_no = 1, suryo = 30))
ses.add(Zaiko(shop_no = 1, shohin_no = 2, suryo = 20))
ses.add(Zaiko(shop_no = 1, shohin_no = 3, suryo = 15))
ses.add(Zaiko(shop_no = 2, shohin_no = 1, suryo = 40))
ses.add(Zaiko(shop_no = 2, shohin_no = 2, suryo = 10))
ses.add(Zaiko(shop_no = 2, shohin_no = 3, suryo = 25))
# コミット
ses.commit()

# black整形
```sh
black .
```