## Docker 使って python 環境構築してみる
#### 前提
 - windows 環境では GitBash を使用
 - Mac 環境では標準の terminal を使用

#### docker image をビルド-> コンテナ起動の場合
 ```
 docker build --rm -t sample:0.6 . # ビルド
 winpty docker run --rm -it -v $PWD:/home/python --name python_container sample:0.2 //bin/bash # 起動
 ```

#### docker-compose.yml 使用の場合
 ```
 docker-compose up -d # ビルド(バックグラウンドで実行？)
 winpty docker exec -it python_env //bin/sh -c "[ -e //bin/bash ] && //bin/bash || //bin/sh" (ログイン)
 ```

#### 実現したいこと
 - vscode などエディタで開発
 - シェルには docker が起動していて、そこで実行できる
 - ホスト側のディレクトリをマウントし、全体を git 管理してデスクトップでもノート PC でも同じように開発できる
 - スピーディーに build できる

#### やり方
 - VSCode で 'remote-container' をインストール
 - Remote-Containers: Open Folder in Container... を選択