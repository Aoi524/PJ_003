# Pythonのベースイメージ
FROM python:3.13

# 作業ディレクトリを設定する
WORKDIR /app

# 必要なパッケージをインストールする
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時に実行するコマンドを設定する
CMD ["python", "app.py"]