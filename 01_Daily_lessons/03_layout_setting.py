# 03_layout_setting.py
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#
st.title('03 レイアウトを整える')
# refer API reference "Input Widget" : https://docs.streamlit.io/library/api-reference/widgets
#
# サイドバー
"""
## サイドバー
- `st.sidebar.<作成要素>`で左側に開閉するsection要素が作成される
  - 例）
```
# 下はサイドバーに作成される
# st.sidebar.text_input('あなたの趣味を教えてください')
text = text = st.sidebar.text_input('あなたの趣味を教えてください',value="ほげ")
condition = st.sidebar.slider('今日の調子は？',0,100,50)
# 下はメイン（常時表示）に作成される
'あなたの趣味：', text
'コンディション：', condition
```
"""
# 下はサイドバーに作成される
text = st.sidebar.text_input('あなたの趣味を教えてください',value="ほげ")
condition = st.sidebar.slider('今日の調子は？',0,100,50)
# 下はメイン（常時表示）に作成される
'あなたの趣味：', text
'コンディション：', condition
#
st.markdown('---')
#
# ２カラムレイアウト
# refer : https://docs.streamlit.io/library/api-reference/layout/st.columns
"""
## カラムレイアウト：
- 横に並べるときは、`st.columns(列数)`で前処理をする
  - refer : https://docs.streamlit.io/library/api-reference/layout/st.columns
  - 例）
```
# left_column, right_column = st.beta_columns(2) # at old version
left_column, right_column = st.columns(2)
left_button = left_column.button('右カラムに表示')
if left_button:
  with right_column: 
    st.write('あなたの趣味：', text)
```
"""
# left_column, right_column = st.beta_columns(2) # at old version
left_column, right_column = st.columns(2)
left_button = left_column.button('右カラムに表示')
if left_button:
  with right_column: 
    st.write('あなたの趣味：', text)
#
#
st.markdown('---')
#
# エクスパンダ―
# - refer : https://docs.streamlit.io/library/api-reference/layout/st.expander
"""
## エクスパンダ―：折り畳みのレイアウト表現
- `st.expander('ラベル')`で作成した要素に、内容を作成できる
  - 例）
```
expander = st.expander('問合せ：')
expander.text_input('問合せを書く',value="ほげほげ")
```
"""
text = st.text_input('問合せを書く',value="ほげほげ")
expander1 = st.expander('問合せ１：')
expander1.write('問合せ内容１：foo ' + text)
expander1.write('問合せ回答１：bar')
expander2 = st.expander('問合せ２：')
expander2.write('問合せ内容２：foofoo')
expander2.write('問合せ回答２：barbar')

#
st.markdown('---')
#
# EOF