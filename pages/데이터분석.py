import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 정의
data = {
    'name': ['lee', 'park', 'kim'],
    'grade': [2, 2, 2],
    'number': [1, 2, 3],
    'kor': [90, 88, 99],
    'eng': [91, 89, 99],
    'math': [81, 77, 99],
    'info': [100, 100, 100]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# Streamlit 앱 시작
st.title("학생 성적 시각화 웹앱")
st.subheader("Plotly Express를 이용한 성적 분석")

# 시각화할 과목 선택
subject_options = ['kor', 'eng', 'math', 'info']
selected_subjects = st.multiselect("시각화할 과목을 선택하세요", subject_options, default=subject_options)

# 시각화 타입 선택
chart_type = st.selectbox("차트 종류 선택", ['Bar Chart', 'Line Chart', 'Scatter Plot', 'Box Plot'])

# 그래프 그리기
if selected_subjects:
    df_long = df.melt(id_vars=['name'], value_vars=selected_subjects,
                      var_name='subject', value_name='score')
    
    if chart_type == 'Bar Chart':
        fig = px.bar(df_long, x='name', y='score', color='subject', barmode='group',
                     title='과목별 성적 (막대 그래프)')
    elif chart_type == 'Line Chart':
        fig = px.line(df_long, x='subject', y='score', color='name', markers=True,
                      title='학생별 과목 성적 (라인 그래프)')
    elif chart_type == 'Scatter Plot':
        fig = px.scatter(df_long, x='subject', y='score', color='name', symbol='name',
                         title='학생별 과목 성적 (산점도)')
    elif chart_type == 'Box Plot':
        fig = px.box(df_long, x='subject', y='score', points='all',
                     title='과목별 성적 분포 (박스 플롯)')

    st.plotly_chart(fig)
else:
    st.warning("하나 이상의 과목을 선택하세요.")

# 데이터 테이블 보기 옵션
with st.expander("🔍 원본 데이터 보기"):
    st.dataframe(df)
