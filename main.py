import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구원"],
    "INFJ": ["작가", "상담가", "교사"],
    "ENTP": ["기업가", "마케터", "방송인"],
    "ESFP": ["연예인", "이벤트 플래너", "영업"],
    "ISTJ": ["회계사", "변호사", "공무원"],
    "ENFP": ["광고 기획자", "심리학자", "예술가"],
    "ESTP": ["스포츠 코치", "세일즈 매니저", "경찰관"],
    "INFP": ["작곡가", "상담심리사", "사회복지사"]
}

# 앱 제목
st.title("🌱 MBTI 기반 진로 추천 사이트")
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# 사용자 입력 (Selectbox)
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요",
    options=list(mbti_jobs.keys())
)

# 직업 추천 결과 출력
if selected_mbti:
    st.subheader(f"🔎 {selected_mbti} 유형에 어울리는 직업 추천")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
