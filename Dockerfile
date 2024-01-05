# ベースイメージを指定
FROM python:3.10.6

# 作業ディレクトリを設定
WORKDIR /app

# 依存パッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# FastAPIアプリケーションのコードをコピー
COPY . .

# FastAPIアプリケーションを実行
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
