import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time

# 앱 제목
st.title("알고리즘 시각화: 버블 정렬")

# 세션 상태 초기화
if 'array' not in st.session_state:
    st.session_state.array = []
if 'steps' not in st.session_state:
    st.session_state.steps = []

# 버블 정렬 함수
def bubble_sort(arr):
    steps = [arr.copy()]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    return steps

# 사용자 입력
st.subheader("배열 설정")
array_size = st.slider("배열 크기", 5, 20, 10)
if st.button("랜덤 배열 생성"):
    st.session_state.array = np.random.randint(10, 100, array_size).tolist()
    st.session_state.steps = bubble_sort(st.session_state.array.copy())

# 시각화
if st.session_state.steps:
    st.subheader("정렬 과정")
    step = st.slider("단계 선택", 0, len(st.session_state.steps) - 1, 0)
    
    # 현재 단계 시각화
    fig = go.Figure(data=[go.Bar(x=list(range(len(st.session_state.steps[step]))), 
                                 y=st.session_state.steps[step],
                                 marker_color='#636EFA')])
    fig.update_layout(title=f"버블 정렬 - {step + 1}단계",
                      xaxis_title="인덱스",
                      yaxis_title="값",
                      template="plotly_dark")
    st.plotly_chart(fig)

    # 애니메이션
    if st.button("애니메이션 재생"):
        placeholder = st.empty()
        for i in range(len(st.session_state.steps)):
            fig = go.Figure(data=[go.Bar(x=list(range(len(st.session_state.steps[i]))), 
                                         y=st.session_state.steps[i],
                                         marker_color='#636EFA')])
            fig.update_layout(title=f"버블 정렬 - {i + 1}단계",
                              xaxis_title="인덱스",
                              yaxis_title="값",
                              template="plotly_dark")
            placeholder.plotly_chart(fig)
            time.sleep(0.5)  # 애니메이션 속도 조절
