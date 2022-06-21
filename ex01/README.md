# 第1回
## 文字あてクイズ(ex01/alphabet.py)
### 遊び方
* コマンドラインでalphabet.pyを実行すると,標準出力に問題が表示される.
* 標準入力から欠損文字数を入力する.
* 正解なら「正解です。それでは、具体的に欠損文字を１つずつ入力してください」と表示される．
* 標準入力から答えを入力する.
* 正解なら「正解です。おめでとうございます！」と表示される．
* 不正解なら「不正解です。またチャレンジしてください」と表示される．
* 不正解の場合指定された回数まで繰り返し出題される.
### プログラム内の解説
* main関数：クイズプログラムの全体の流れを担当する．
* shutudai関数：ランダムに選んだアルファベットを出題し，解答をmain関数に返す．
* kaitou関数：回答と正解をチェックし，結果を出力する．