import streamlit as st
from log_to_sheet import log_checkin

st.set_page_config(page_title="체크인 폼")
st.title("✅ 아동안전지킴이 체크인 폼")

# 🗂️ 조별 멤버 매핑
group_members = {
    "1조": ["이기용", "최영자"],
    "2조": ["안규삼", "도경순"],
    "3조": ["황종의", "김현숙"],
    "4조": ["문명식", "정미자"],
    "5조": ["이경숙", "정병진"],
    "6조": ["권옥주", "이태현"],
    "7조": ["노영희", "최석천"]
}

# 🏫 초등학교 목록
school_list = [
    "일원초등학교", "영희초등학교", "대청초등학교",
    "대진초등학교", "개포초등학교", "양전초등학교", "대모초등학교"
]

# ✅ 조 선택 (콤보박스)
selected_group = st.selectbox("👥 근무 조를 선택하세요:", ["선택하세요"] + list(group_members.keys()))

# ✅ 이름 선택
if selected_group != "선택하세요":
    selected_name = st.selectbox("👮‍♀️ 본인의 이름을 선택하세요:", ["선택하세요"] + group_members[selected_group])
else:
    selected_name = "선택하세요"

# ✅ 초등학교 선택
selected_school = st.selectbox("🏫 근무하는 초등학교를 선택하세요:", ["선택하세요"] + school_list)

# ✅ 체크인
if st.button("📌 체크인"):
    if selected_group != "선택하세요" and selected_name != "선택하세요" and selected_school != "선택하세요":
        full_name = f"{selected_group} {selected_name}"
        log_checkin(full_name, selected_school)
        st.success(f"🎉 {full_name}님의 체크인이 완료되었습니다!")
    else:
        st.error("⚠️ 조, 이름, 초등학교를 모두 선택해주세요.")
