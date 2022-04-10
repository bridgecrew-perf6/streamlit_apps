# 04_progress_bar.py
import streamlit as st
import time
#
st.title("04 プログレスバーの表示")
#
'Start'
#
#
#
latest_iteration = st.empty()
bar = st.progress(0)
#
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i +1 )
    # time.sleep(0.1)
    # time.sleep(0.2)
    time.sleep(0.05)
#
# left_column, right_column = st.beta_columns(2)
left_column, right_column = st.columns(2)

button = left_column.button("右カラムにボタンを表示")
if button:
    right_column.write('ここは右カラムです')

# expander = st.beta_expander('問い合わせ1')
expander = st.expander('問い合わせ1')
expander.write('問い合わせ1の内容')
# expander2 = st.beta_expander('問い合わせ2')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容')
# expander3 = st.beta_expander('問い合わせ3')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容')
#
st.markdown('---')
#
st.write('問い合わせ内容を書く')
post_text = st.text_input('問合せ内容：',value="ここに記入してください")
left_column, right_column = st.columns(2)
post_button = right_column.button('投稿')
if post_button:
  st.write(post_text)
#
st.markdown('---')
#
# EOF