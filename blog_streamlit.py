import streamlit as st
from utils import Chatbot


with st.sidebar:
    st.session_state['chatbot'] = Chatbot('text-davinci-003', 0.5, 2048)
    with st.form('cahtbot_gpt3'):
        st.title('Chat with GPT3')
        ask = st.text_input('Input')
        if st.form_submit_button("Ask"):
            answer = st.session_state['chatbot'].chat(ask)
            st.text(answer)
        #elif st.form_submit_button('New Conversation'):
        #    st.session_state['chatbot'].new_conversation()
    audio_file = open('Documents/最伟大的作品.wav', 'rb')
    audio_bytes = audio_file.read()
    st.write('正在播放最伟大的作品-周杰伦 :musical_note:')
    st.audio(audio_bytes, format='audio/wav')
        
        
tab1, tab2, tab3 = st.tabs(['爬虫', '算法', '数据分析及可视化'])
with tab1:
    st.text('')
with tab2:
    tab2_1, tab2_2, tab2_3 = st.tabs(['推荐', '视觉', '文本'])
    with tab2_1:
        with st.expander('深度学习案例'):
            st.subheader('基金产品个性化推荐')
            st.text('目标：在与用户交互的过程中进行个性化兴趣捕捉，进而推荐更好的产品，提高产品点击率')
            st.text('实：')
        with st.expander('机器学习案例'):
            st.subheader('运营商流失预测')
            st.text('目标：')
            st.text('实验记录：')
    with tab2_2:
        st.subheader('基于计算机视觉的射击类游戏自动瞄准')
        st.text('目标：通过AI建模实时检测游戏画面中的人物模型，实现自动移动准心到人物中心。')
        st.write('经过：深入yolov5检测代码，植入计算中心点以及自瞄逻辑，多次改进优化代码，提高单次识别跟踪等响应效率。')
    with tab2_3:
        st.subheader('品牌名称纠错')
        st.write('目标：识别数据库中具有相同名称但不属于同一个公司的品牌，如晨光牛奶与晨光文具，大疆无人机与大疆家具等。')
        st.write('实验方案：将品牌下所有类目作为词依次排列，作为描述该品牌的句子，按此方法构建文档，利用word2vec学习上下文的能力来训练词向量（类目向量），再通过计算类目间的相似度差异来识别某一品牌是否具有迥异的类目。')
        st.write('后学习图神经网络后才发现，此处思路与metapath2vec算法思路有异曲同工之妙！')
with tab3:
    st.text('')