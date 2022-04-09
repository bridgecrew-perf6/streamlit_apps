# 02_interactive_widget.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#
st.title('02 インタラクティブなウィジェット')
# refer API reference "Input Widget" : https://docs.streamlit.io/library/api-reference/widgets
#
# checkboxの利用
"""
## checkboxの利用
- checkboxは`st.checkbox(...)`でinput要素が追加される
  - `if checkbox(): ... `とするとチェックすると表示できる
  - 画像の表示の例：
```
if st.checkbox('Display Image'):
  image = Image.open('images/sunrise.png')
  st.image(image, caption='Sunrise by the mountains', use_column_width=True)
```
"""
#
if st.checkbox('Display Image'):
  image = Image.open('images/sunrise.png')
  st.image(image, caption='Sunrise by the mountains', use_column_width=True)
#
#
st.markdown('---')
#
# セレクトボックスの利用
"""
## セレクトボックスの利用
- セレクトボックスは、`list`データをもとにinput要素を作る
  - `st.selectbox([リストデータ])`で定義して返り値に選択した値が帰る
  - 例）
```
st.write('選択してください。')
option = st.selectbox(
  '好きな数字を教えてください。',
  #[1,2,3,4]
  list(range(1,11))
)
st.write('あなたの好きな数字は、',option,'です')
```
"""
st.write('選択してください。')
option = st.selectbox(
  '好きな数字を教えてください。',
  #[1,2,3,4]
  list(range(1,11))
)
st.write('あなたの好きな数字は、',option,'です')
#
#
st.markdown('---')
#
# テキスト入力
"""
## テキスト入力
- テキスト入力は、`st.text_input('ラベル')`でinput要素が作成される
  - 返り値に入力値が返る
  - 例）
```
text = st.text_input('あなたの好きなもの・事を教えてください')
st.write('あなたのモノ・事：',text)
```
"""
text = st.text_input('あなたの好きなもの・事を教えてください')
st.write('あなたのモノ・事：',text)
#
#
st.markdown('---')
#
# スライダー
"""
## スライダー入力：
- スライダーは、`st.slider('ラベル', 最小値, 最大値, 初期値)`で指定する
  - スライダー風のdiv要素が作成され、選択した場所の値が返る
  - 例：
```
condition = st.slider('今日のコンディションは？',0,100,50)
# st.write('コンディション：',condition)
'コンディション：',condition
```
"""
condition = st.slider('今日のコンディションは？',0,100,50)
# st.write('コンディション：',condition)
'コンディション：',condition
#
#
st.markdown('---')
#
# EOF
