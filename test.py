import streamlit as st
import random

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️", layout="centered")

st.title("🍽️ 오늘 뭐 먹지? 추천기")
st.write("👉 기분이나 상황을 골라보세요, 혹은 그냥 랜덤으로 오늘의 메뉴를 뽑아볼 수도 있어요!")

# 카테고리별 대표 음식
food_options = {
    "🥗 가볍게": "샐러드",
    "🍲 든든하게": "삼겹살",
    "⏱️ 빨리": "햄버거",
    "🎉 특별하게": "스시",
    "🤑 가성비 있게": "김치찌개",
    "💸 플렉스하게": "스테이크",
    "👥 여럿이서": "치킨",
    "🏠 집에서 간단히": "토스트",
    "🌍 외국 느낌 내기": "파스타",
    "😴 피곤할 때": "국밥"
}

# 보너스 멘트 미리 정의 (두 버튼에서 공유)
comments = [
    "행복한 돼지가 되세요! 😍"
]

# 라디오 버튼 UI
choice = st.radio("오늘 상황은? 👇", list(food_options.keys()))

# 선택한 카테고리 추천 버튼
if st.button("추천 받기 🚀"):
    food = food_options[choice]
    st.success(f"👉 오늘은 **{food}** 어때요? 😋")
    st.write(random.choice(comments))

# 랜덤 추천 버튼
if st.button("🎲 그냥 랜덤으로 뽑기!"):
    food = random.choice(list(food_options.values()))
    st.success(f"👉 오늘은 **{food}** 어때요? 😋")
    st.write(random.choice(comments))
