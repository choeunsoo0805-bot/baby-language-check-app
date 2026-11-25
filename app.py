import streamlit as st

check_12 = ["'안 돼' 하면 잠깐 멈춘다", "빠이빠이 하며 손을 흔든다", "엄마, 아빠처럼 특정한 사람을 부른다"]
check_24 = ["엄마 우유처럼 두 단어를 붙여 말한다", "그림책에서 물어본 사물을 가리킨다", "간단한 지시를 이해하고 따른다"]
check_36 = ["두 번 이상 말을 주고받는다", "누구야, 뭐야, 어디 같은 질문을 한다", "가족이 아닌 사람도 아이 말을 대부분 알아듣는다"]


def check_language(checked_count, total):
    rate = checked_count / total * 100
    if rate >= 80:
        message = "또래 수준이에요"
        tip = "💡 **추천 육아 팁:** 지금처럼 아이와 다정한 눈빛으로 대화하고 그림책을 자주 읽어주세요."
    elif rate >= 50:
        message = "관찰이 필요해요"
        tip = "💡 **추천 육아 팁:** 아이가 말을 할 때 충분히 기다려주고, 일상 속 사물의 이름을 자주 들려주세요."
    else:
        message = "전문가 상담을 권장해요"
        tip = "💡 **추천 육아 팁:** 너무 걱정하지 마시고, 가까운 소아청소년과나 발달센터에서 전문적인 상담을 받아보세요."
    return message, rate, tip


st.title("우리 아이 언어발달 체크")
month = st.slider("아이 개월 수", 12, 48)

if month <= 18:
    items = check_12
elif month <= 30:
    items = check_24
else:
    items = check_36

results = []
checked_count = 0
for item in items:
    if st.checkbox(item):
        checked_count += 1
        results.append({"항목": item, "체크 여부": "✓"})
    else:
        results.append({"항목": item, "체크 여부": "✗"})

if st.button("결과 보기"):
    message, rate, tip = check_language(checked_count, len(items))
    if rate >= 80:
        st.success(message)
    elif rate >= 50:
        st.warning(message)
    else:
        st.error(message)
    st.info(tip)
    st.table(results)
    st.metric("달성률", f"{rate:.0f}%")
    st.caption("발달에는 개인차가 있으며, 걱정되면 전문가와 상담하세요. (진단이 아닌 참고용)")
