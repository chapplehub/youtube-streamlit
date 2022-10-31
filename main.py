import streamlit as st
import time

st.title("Streamlit 超入門")

st.write("DisplayImage")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!!"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ解答1")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ解答2")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ解答3")

# text = st.text_input("あなたの趣味を教えてください。")
# condition = st.slider("あなたの今の調子は？", 0, 100, 50)

# "あなたの趣味：",text,
# "コンディション：",condition,



# このコードだけでセレクトボックスの表示とその値の取得までできる。
# option = st.selectbox(
#     "あなたが好きな数字を教えてください。",
#     list(range(1,11))
# )
# "あなたの好きな数字は、", option, "です。"

# このコードだけで、チェックボックスの配置とその値の取得。さらに、条件分岐で画像を表示するかどうかまで表現できる。
# if st.checkbox("Show Image"):
#     img = Image.open("CA_rule110s.png")
#     st.image(img, caption="rule110", use_column_width=True)



# df = pd.DataFrame({
#     "1列目":[1,2,3,4],
#     "2列目":[10,20,30,40]
# })

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0)) # 静的なテーブルが作成できる。（ソートできない）

# マークダウンという文章の記述方法がある
# """
# # 章
# ## 節
# ### 項
# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# 20行3列の行列を作成する
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a','b','c']
# )
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# 東京新宿付近の緯度経度を１００地点作成
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# 地図に緯度経度の地点をマッピングする
# st.map(df)














