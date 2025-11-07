# Next.js + FastAPI Starter Application

Next.js フロントエンドと FastAPI バックエンドを連携させた学習用アプリケーションです。

## 📁 プロジェクト構成

```
Derapp_Starter/
├── backend/              # バックエンド（APIサーバー）
│   ├── app.py           # メインファイル（APIのコードを書くところ）
│   ├── requirements.txt # 必要なライブラリのリスト
│   ├── index.html       # 超Want課題①用HTMLファイル
│   ├── sample.csv       # 超Want課題②用サンプルデータ
│   └── 請求書.png        # 超Want課題②の参考画像
│
└── frontend/            # フロントエンド（画面）
    ├── src/
    │   └── app/
    │       ├── page.jsx      # メイン画面のコード
    │       ├── layout.jsx    # 全体のレイアウト
    │       └── globals.css   # デザイン（スタイル）
    └── package.json     # フロントエンドで使うライブラリのリスト
```

## 🎯 課題一覧

### ✅ Must 課題（必須）

#### Must 課題 ① 簡易メッセージ API

- **内容**: 自分の氏名を返す API を作る
- **エンドポイント**: `GET /api/hello`
- **やること**: "Hello! 氏名" の形でレスポンスする
- **注意**: 🚫 生成 AI を使わずに自力で実装！

#### Must 課題 ②-1 割り算 API

- **内容**: 数値を 2 で割る API を作る
- **エンドポイント**: `GET /api/divide/{数値}`
- **やること**: 送られた数値を 2 で割って返す（整数除算）
- **例**: `/api/divide/10` → `{"divided_value": 5}`
- **注意**: 🚫 生成 AI を使わずに自力で実装！

### 🌟 Want 課題（挑戦）

#### Want 課題 ①-1 文字数カウント API

- **内容**: 文字列の長さをカウントする API を作る
- **エンドポイント**: `GET /api/count/{文字列}`
- **やること**: 送られた文字列の文字数を返す
- **ヒント**: `len()` 関数を使う
- **例**: `/api/count/hello` → `{"count_text": 5}`
- **注意**: 🚫 生成 AI を使わずに自力で実装！

### 🚀 超 Want 課題（発展）

#### 超 Want 課題 ① HTML をレスポンスする

- **内容**: `index.html` を表示する API を作る
- **ヒント**: Jinja2Templates ライブラリを使うと便利

#### 超 Want 課題 ② 簡単な業務効率化アプリ

- **内容**: CSV ファイルを請求書形式に変換
- **使用ファイル**: `sample.csv`
- **参考**: `請求書.png` を見てイメージを掴む

#### 超 Want 課題 ③ 自身の業務効率化アプリ作成

- **内容**: 自分の業務で使えるアプリを自由に作成
- **例**: CSV から取引先別に PDF 請求書を作成するなど

#### 超 Want 課題 ④ フィードバックをもらう

- **内容**: 作ったアプリを社内の誰かに使ってもらう
- **方法**: 社内 LAN で公開してアクセスしてもらう
- **詳細**: 「Starter 補足資料」の【参考】FastAPI アプリを社内公開する方法を参照

## 🚀 セットアップ方法

### 必要なもの

- Python 3.8 以上
- Node.js 18 以上
- npm（Node.js に付属）

### ステップ 1: バックエンドの起動

```bash
# backendフォルダに移動
cd backend

# 必要なライブラリをインストール
pip install -r requirements.txt

# サーバーを起動
python app.py
```

✅ `http://0.0.0.0:8000` で起動したら OK！

### ステップ 2: フロントエンドの起動

**別のターミナル（コマンドプロンプト）を開いて**

```bash
# frontendフォルダに移動
cd frontend

# 必要なライブラリをインストール（初回のみ）
npm install

# 開発サーバーを起動
npm run dev
```

✅ `http://localhost:3000` で起動したら OK！

### ステップ 3: ブラウザで確認

ブラウザで `http://localhost:3000` を開くと画面が表示されます！

## 📖 API の使い方

### 実装済み API 一覧

| メソッド | URL                | 説明                      | レスポンス例                    |
| -------- | ------------------ | ------------------------- | ------------------------------- |
| GET      | `/`                | 動作確認用                | `{"message": "FastAPI hello!"}` |
| GET      | `/api/hello`       | 氏名を返す（Must①）       | `{"message": "Hello! Kaori!"}`  |
| GET      | `/api/multiply/10` | 2 倍にする                | `{"doubled_value": 20}`         |
| GET      | `/api/divide/10`   | 2 で割る（Must②-1）       | `{"divided_value": 5}`          |
| GET      | `/api/count/hello` | 文字数カウント（Want①-1） | `{"count_text": 5}`             |
| POST     | `/api/echo`        | メッセージをそのまま返す  | `{"message": "echo: Hello"}`    |

### API の試し方

#### 方法 1: ブラウザで確認（GET のみ）

ブラウザのアドレスバーに以下を入力：

```
http://localhost:8000/api/hello
```

#### 方法 2: curl コマンドで確認

```bash
# GETリクエスト
curl http://localhost:8000/api/hello

# 数値を2で割る
curl http://localhost:8000/api/divide/10

# 文字数をカウント
curl http://localhost:8000/api/count/hello

# POSTリクエスト
curl -X POST http://localhost:8000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello"}'
```

#### 方法 3: フロントエンドのボタンで確認

`http://localhost:3000` の画面からボタンをクリック！

## 💡 コードの見方・変更方法

### バックエンド（app.py）の基本構造

```python
# APIのエンドポイントを作る基本形
@app.get("/api/hello")  # ← GETリクエストを受け付ける
def hello_world():      # ← 関数名（何でもOK）
    return {"message": "Hello! Kaori!"}  # ← レスポンスするデータ
```

### パス変数の使い方

```python
@app.get("/api/divide/{id}")  # ← {id}の部分に数値が入る
def divide(id: int):          # ← id: int で整数型を指定
    divided_value = id // 2   # ← 整数除算（割り切り）
    return {"divided_value": divided_value}
```

### 型について

- `int` = 整数（例: 1, 2, 3, 100）
- `str` = 文字列（例: "hello", "こんにちは"）

### よく使う関数

- `len(文字列)` = 文字数を数える
- `//` = 整数除算（割り切り）
- `*` = 掛け算

## 🔧 技術スタック

### フロントエンド（画面側）

- **Next.js** 15.1.3 - React のフレームワーク
- **React** 19.0.0 - UI 作成ライブラリ
- **Tailwind CSS** 3.4.1 - デザイン用

### バックエンド（API 側）

- **FastAPI** 0.115.6 - Python 製の API フレームワーク
- **Uvicorn** 0.34.0 - サーバー起動用
- **Pydantic** - データ検証用

## ❓ よくあるトラブルと解決方法

### Q1: `npm install` でエラーが出る

```bash
# キャッシュをクリアして再インストール
npm cache clean --force
npm install
```

### Q2: ポートが既に使われている

```bash
# 別のポートで起動
# バックエンド: app.py の port=8000 を port=8001 に変更
# フロントエンド:
npm run dev -- -p 3001
```

### Q3: CORS エラーが出る

フロントエンドが `http://localhost:3000` で起動しているか確認してください。

### Q4: バックエンドにアクセスできない

以下を確認：

1. `python app.py` が実行中か
2. エラーメッセージが出ていないか
3. `http://localhost:8000` にブラウザでアクセスできるか

### Q5: FastAPI のドキュメントを見たい

ブラウザで以下にアクセス：

```
http://localhost:8000/docs
```

自動生成された API 仕様書が見られます！

## 📚 学習のポイント

1. **まずはコードを動かしてみる** - 完璧に理解しなくて OK
2. **少しずつ変更してみる** - 数値や文字列を変えて試す
3. **エラーを恐れない** - エラーメッセージをよく読む
4. **Must 課題は自力で** - 既存コードをアレンジして書く
5. **わからない時は** - ドキュメントや補足資料を参照

## 📝 開発の進め方

### Must 課題の進め方

1. `backend/app.py` を開く
2. Must 課題 ① または ② のコメント部分を見る
3. 上にある既存のエンドポイントを参考にする
4. 少しずつコードを変更して試す
5. `python app.py` で再起動して確認

### デバッグのコツ

```python
# print文でデバッグ
@app.get("/api/divide/{id}")
def divide(id: int):
    print(f"受け取った値: {id}")  # ← ターミナルに表示される
    divided_value = id // 2
    print(f"計算結果: {divided_value}")
    return {"divided_value": divided_value}
```

## 🎓 次のステップ

1. Must 課題を完了させる
2. Want 課題にチャレンジ
3. 超 Want 課題で実践的なアプリを作る
4. 自分だけの業務効率化アプリを考える

## 📄 ライセンス

このプロジェクトは学習用のサンプルアプリケーションです。
