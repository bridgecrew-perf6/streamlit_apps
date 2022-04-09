# 01_streamlit_basic.py
import streamlit as st
import numpy as np
import pandas as pd
#
st.title('01 Streamlit Basic')
#
# show import packages
st.write('import packages')
"""
```
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#
st.markdown("## st.write and st.dataframe")
# show p tag of strings by st.write
st.markdown("- how to use st.write")
st.markdown("`st.write('DataFrame')`")
st.write('DataFrame')
# show a table of dataframe
# - define DataFrame
st.markdown("- define DataFrame. and use st.dataframe")
st.markdown("`df = pd.DataFrame({'row1': [1,2,3,4],  'row2': [10,20,30,40]})`")
df = pd.DataFrame({
  'row1': [1,2,3,4],
  'row2': [10,20,30,40]
})
st.markdown("`st.write(df)`")
st.write(df)
st.markdown("`st.dataframe(df)`")
st.dataframe(df)
#
# show by st.dataframe method
st.markdown("## show by st.dataframe method")
st.markdown('- show tiny table')
st.markdown("`st.dataframe(df, width=100, height=100)`")
st.dataframe(df, width=100, height=100)
# show with high_light
st.markdown('- show with high_light max')
st.markdown("`st.dataframe(df.style.highlight_max(axis=0))`")
st.dataframe(df.style.highlight_max(axis=0))
# 
# show by st.table method which can not sort
st.markdown("- show by st.table method which can not sort")
st.markdown("`st.table(df)`")
st.table(df)
#
# markdown with magic command
# show by st.metric
"""
- st.metrics
  - Usage : `st.metric(label, value, delta=None, delta_color="normal")`
```
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
```
"""
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
#
"""
- st.metric looks especially nice in combination with st.columns:
```
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
```
"""
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
#
st.markdown("---")
# how to use chart methods
# - refer : https://docs.streamlit.io/library/api-reference/charts
st.markdown("## show some kind of charts")
st.markdown("`st.line_chart(df)`")
st.line_chart(df) # show df chart
#
# - re-define DataFrame
st.markdown("- re-define DataFrame")
st.markdown("`df = pd.DataFrame(np.random.rand(20, 3),columns=['a','b','c'])`")
df = pd.DataFrame(
  np.random.rand(20, 3),
  columns=['a','b','c']
)
# show dataframe
st.markdown("`st.dataframe(df) `")
st.dataframe(df) 
# show line chart
st.markdown("`st.line_chart(df) `")
st.line_chart(df) 
# show area chart
st.markdown("`st.area_chart(df) `")
st.area_chart(df) 
# show bar chart
st.markdown("`st.bar_chart(df) `")
st.bar_chart(df) 
#
#
st.markdown("---")
# how to use map method
# - refer : https://docs.streamlit.io/library/api-reference/charts/st.map
"""
## how to use map method
- usage : st.map(data=None, zoom=None, use_container_width=True)
  - 緯度経度データを使って地図上にプロットする
```
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
st.map(df)
```
"""
df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
st.map(df)
#
# 
"""
- 新宿付近の地図にプロットしてみる
  - 緯度=35.69、経度=139.70の周辺(+0.02度の範囲)にプロットしてみる
"""
#
df = pd.DataFrame(
  # np.random.rand(100,2),
  np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
st.dataframe(df)
st.map(df)
#
#
st.markdown("---")
# how to Display image
# - refer : https://docs.streamlit.io/library/api-reference/media/st.image
# - use pillow package
"""
- how to display image
```
from PIL import Image
image = Image.open('sunrise.png')
st.image(image, caption='Sunrise by the mountains')
```
"""
#
from PIL import Image
image = Image.open('images/sunrise.png')
# st.image(image, caption='Sunrise by the mountains')
st.image(image, caption='Sunrise by the mountains', use_column_width=True)
# img = Image.open('sample.jpg')
# st.image(img, caption='Kihei', use_column_width=True)
#
# EOF