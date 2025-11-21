AI Behavior Rules for AY-Knowledge-Graph

あなたは AY-Knowledge-Graph の構築を支援するAIアシスタントです。
コードの生成や修正を行う際は、以下のルールを厳守してください。

🚫 禁止事項 (Critical Rules)

index.ttl を絶対に編集しないこと

このファイルは scripts/generate_index.py によって自動生成されます。

あなたが手動でリンクを追加する必要はありません。

PRに index.ttl の変更が含まれていたら、それは誤りです。除外してください。

既存の自動化スクリプトを壊さないこと

scripts/ フォルダ内のコードは、ユーザーからの明示的な指示がない限り変更しないでください。

✅ 推奨される行動 (Best Practices)

新しい知識は新規ファイルとして作成する

既存のファイルに追記するのではなく、新しい .ttl ファイルを作成することを優先してください。

ファイル名の形式: knowledge/<category>/<name>.ttl または inbox/<name>.ttl

Turtle形式 (.ttl) を守る

常に以下のプレフィックスを含めてください：

@prefix ex: [http://example.com/aykg#](http://example.com/aykg#) .
@prefix schema: [http://schema.org/](http://schema.org/) .
@prefix rdf: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](http://www.w3.org/1999/02/22-rdf-syntax-ns#) .
@prefix rdfs: [http://www.w3.org/2000/01/rdf-schema#](http://www.w3.org/2000/01/rdf-schema#) .


曖昧なときは Inbox へ

保存場所に迷う知識やメモは、inbox/ フォルダに保存してください。

🔍 コンテキストの理解

このリポジトリは「GitHub Actions」によって管理されています。

ユーザーがファイルをPushすると、自動的にインデックスが更新される仕組みになっています。
