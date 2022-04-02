import streamlit as st
import time

st.title("streamlit超入門")

st.write("プログレスバーの表示")
'Start'



latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i +1 )
    time.sleep(0.1)

left_column, right_column = st.beta_columns(2) 

button = left_column.button("右カラムにボタンを表示")
if button:  
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ内容を書く')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の内容を書く')
expander.write('問い合わせ内容を書く')

# text = st.text_input("あなたの趣味を教えてください")
# "あなたの趣味",text

# condition = st.slider("あなたの今の調子は？",0,100,50)
# "コンディション：",condition

# if st.checkbox("Show Image"):
# img = Image.open("20210228-_R5I1393.jpg")
# st.image(img, caption = "Sho Kamio", use_column_width=True)




#df = pd.DataFrame(
#    np.random.rand(100,2)/[50, 50] + [35.69, 139.70], 
#    columns=["lat","lon"]
#    )
#st.dataframe(df.style.highlight_max(axis=0))
#st.dataframe(df)
#st.map(df)
