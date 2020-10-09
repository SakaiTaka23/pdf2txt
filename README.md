# PDF2TXT

## 現時点での実行手順

1. automaterでpdfを１ページずつjpegファイルに変換

2. cut-img.pyを実行

   input_cut_imgにjpegファイルを配置→cutted_imageに切られた画像を出力

3. imx2txt.pyを実行

   cutted_imageのファイルを読んで文字で返す→output_txtにphpを出力

4. get-all-name.pyを実行

   名前をshort_name.txtに書き込み→連番で書かれたファイルを全てall_name.txtに出力

   **すでにエラーを正したもの(連続したページがある場合の処理をしたもの)を入力として想定** 

   sample2-{1~3}.php →sample2-1.php sample2-2.php sample2-3.php

   {}で番号を入れて ~で範囲を区切る

5. change-name.pyを実行

   input_change_nameから番号順でファイルを読み込み、all_name.txtの行に対応する名前に変更






## 実装手順

* pdfを全て画像に変換
* 文字に変換
* それらをファイルキーワードで分ける(phpやどこが変わるか、を受け取る)

→これらのデータはログファイルに出力

* 切られたファイルごとに出力



## ページ分割アルゴリズム

1. 一行ごとに配列に入れる

2. .phpの文字列があればそれまでも文字列をpagesに登録

   なければそれをpageの文章として登録



## djangoでの着地点

* 入力された写真のtxtを出力させる
* 写真の座標を出力させる




## メモ

* pdfを画像に変換した時の画質が悪く精度に影響している



##  考えられる変化

* 必ずしもファイル名が各ページの先頭に来るとは限らない



## 試したこと

* automaterでpdfを画像に変換→再度pdfに変換・結合→テキストファイル化
* pdfを画像に変換した後行番号、ファイル名を切り取る







## 環境構築

* tesseractの日本語学習データを入れる



## 環境

python 3.8.5

tesseract 4.1.1