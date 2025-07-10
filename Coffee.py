import streamlit as st

st.set_page_config(
    page_title="☕하실래예?",
    page_icon="☕",
    layout="centered",
)

st.title("☕너무 심심해서 만듦")

st.subheader("당첨되셨습니다. 🎉")

col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://i.namu.wiki/i/2FkQDgCweiWOKpwzL5JJCv27WnVJ2H_5QPzfyV2HcXAf2ElTH96tcyc6PccT1maSMMf-XgEg2iP_Q6O-6QqXSTmgr9E-dSyhK5Bwcm85zZRbLBNKjjDUzcxwJI4xT68iLe8fxET8pLvTCRm29oSkjw.webp",
        caption="Awesome Image",
        use_container_width=True,
    )

with col2:
    st.write("""
        **축하합니다!**  
        당첨 되셨습니다.  
        점심 후에 커피를 마실 수 있어요
        
        - Coffee?
        - Non Coffee?
    """)

# 버튼 추가
if st.button("안마시고 싶으시면 누르세요"):
    st.success("사실 안되요^^")

# 진행 바
import time

st.write("Progress bar example:")
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)

st.balloons()
