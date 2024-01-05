# FRONTのリポジトリはこちら
https://github.com/raisack8/wishlist-front

.venv/Scripts/activate

uvicorn main:app --reload

### iphoneで動作確認するためにローカルネットワークを指定して起動
uvicorn main:app --reload --host 192.168.0.18 --port 8000

##### react側では下記のように.envファイルで環境変数を定義している
##### REACT_APP_API_BASE_URL = 'http://192.168.0.18:8000'

## タスクはこちらで管理
https://github.com/users/raisack8/projects/3/views/1
