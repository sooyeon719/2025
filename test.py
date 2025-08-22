import streamlit as st
import random

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️", layout="centered")

st.title("🍽️ 오늘 뭐 먹지? 추천기")
st.write("👉 기분이나 상황을 골라보세요. 오늘의 메뉴를 추천해드릴게요!")

# 카테고리별 대표 음식 + 이미지
food_options = {
    "🥗 가볍게": ("샐러드", "https://cdn.pixabay.com/photo/2017/01/19/15/05/salad-1999477_1280.jpg"),
    "🍲 든든하게": ("삼겹살", "https://cdn.pixabay.com/photo/2017/07/16/11/51/korean-bbq-2507100_1280.jpg"),
    "⏱️ 빨리": ("햄버거", "https://cdn.pixabay.com/photo/2014/10/19/20/59/hamburger-494706_1280.jpg"),
    "🎉 특별하게": ("스시", "https://cdn.pixabay.com/photo/2017/06/19/21/25/sushi-2429067_1280.jpg"),
    "🤑 가성비 있게": ("김치찌개", "https://cdn.pixabay.com/photo/2017/03/10/13/48/kimchi-stew-2135132_1280.jpg"),
    "💸 플렉스하게": ("스테이크", "https://cdn.pixabay.com/photo/2017/04/23/20/24/steak-2256466_1280.jpg"),
    "👥 여럿이서": ("치킨", "https://cdn.pixabay.com/photo/2017/03/27/14/56/chicken-2178728_1280.jpg"),
    "🏠 집에서 간단히": ("토스트", "https://cdn.pixabay.com/photo/2017/05/07/08/56/toast-2297903_1280.jpg"),
    "🌍 외국 느낌 내기": ("파스타", "https://cdn.pixabay.com/photo/2014/12/21/23/28/recipe-575434_1280.png"),
    "😴 피곤할 때": ("국밥", "https://cdn.pixabay.com/photo/2021/07/05/07/02/korean-food-6387961_1280.jpg")
}

# 라디오 버튼 UI
choice = st.radio("오늘 상황은? 👇", list(food_options.keys()))

if st.button("추천 받기 🚀"):
    food, img_url = food_options[choice]
    st.success(f"👉 오늘은 **{food}** 어때요? 😋")
    st.image(img_url, width=400)

    # 보너스 멘트
    comments = [
        "먹고 나면 행복해질걸요? 😍",
        "오늘은 그냥 이거 가야죠!",
        "다이어트는 내일부터… 🤭",
        "맛있게 먹으면 0칼로리!"
    ]
    st.write(random.choice(comments))
