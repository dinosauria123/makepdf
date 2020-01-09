・プログラムの起動

makepdfフォルダ内のmakepdfgui.exeをダブルクリック。
コンソールとGUIが起動するはず。

・Google API KEYの取得

https://www.g104robo.com/entry/google-cloud-vision-api

を参照。configボタンでAPIキーを入力すること。
クレジットカードの登録が必要だが、1000枚/月まで無料。

・画像データ

.jpgファイルでサイズが1.5MB以下。縦横のピクセル数が1500以下（？）。

・testdata

キャノンフレックスの取説（抜粋）。

・使い方

Set pdf fileボタンを押してpdfファイルを作るフォルダを選択。
Set IMG dirボタンを押して画像ファイルのあるフォルダを選択。
Google Cloud Visionに画像を送信し、OCRをおこない検索可能pdfを生成する。
画像一枚のサイズが大きいと、一枚当たり分単位の時間がかかる。

・バグ

沢山あるので自己責任で。

・ソースコード
gcv2hocr.c：https://github.com/dinosauria123/gcv2hocr/blob/master/main.c
makepdfgui.py:自作
hocr-pdf.py:https://github.com/tmbdev/hocr-tools/blob/master/hocr-pdfより
gcvocr.py:https://www.g104robo.com/entry/google-cloud-vision-api掲載コードの一部を改変