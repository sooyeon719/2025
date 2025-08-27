import streamlit as st   # Streamlit 라이브러리 불러오기
import random            # 랜덤 선택을 위한 라이브러리 불러오기

# 웹페이지 기본 설정 (제목, 아이콘, 레이아웃)
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️", layout="centered")

# 앱 제목과 안내 문구 출력
st.title("🍽️ 오늘 뭐 먹지? 추천기")
st.write("👉 기분이나 상황을 골라보세요, 혹은 그냥 랜덤으로 오늘의 메뉴를 뽑아볼 수도 있어요!")

# 카테고리별 대표 음식 (딕셔너리 형태: 상황 → 음식)
food_options = {
    "🥗 가볍게": "샐러드",
    "🍲 든든하게": "국밥",
    "⏱️ 빨리": "햄버거",
    "🎉 특별하게": "스시",
    "🤑 가성비 있게": "김치찌개",
    "💸 플렉스하게": "스테이크",
    "👥 여럿이서": "치킨",
    "🏠 집에서 간단히": "샌드위치",
    "🌍 외국 느낌 내기": "파스타",
    "😴 피곤할 때": "잠봉뵈르"
}

# 보너스 멘트
comments = [
    "행복한 돼지가 되세요! 😍"
]

# 라디오 버튼: 사용자가 상황 선택할 수 있도록 UI 생성
choice = st.radio("오늘 상황은? 👇", list(food_options.keys()))

# [추천 받기 🚀] 버튼 클릭 시 동작
if st.button("추천 받기 🚀"):
    food = food_options[choice]  # 사용자가 고른 상황에 맞는 음식 가져오기
    st.success(f"👉 오늘은 **{food}** 어때요? 😋")  # 결과를 초록색 박스로 보여주기
    st.write(random.choice(comments))  # 보너스 멘트 중 하나 랜덤 출력

# [🎲 그냥 랜덤으로 뽑기!] 버튼 클릭 시 동작
if st.button("🎲 그냥 랜덤으로 뽑기!"):
    food = random.choice(list(food_options.values()))  # 모든 음식 중 하나를 무작위로 선택
    st.success(f"👉 오늘은 **{food}** 어때요? 😋")  # 결과 출력
    st.write(random.choice(comments))  # 보너스 멘트 출력
