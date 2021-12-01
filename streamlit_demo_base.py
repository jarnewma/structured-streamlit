# To run use
# $ streamlit run yolor_streamlit_demo.py
from yolor import * 
import tempfile
import cv2 

import streamlit as st

def main():
    st.title('YOLOR Dashboard')

    st.sidebar.title("Settings")

    st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{width: 400px;}
    [data-testid="stSidebar"][aria-expanded="falst"] > div:first-child{width: 400px; margin-left: -400px}
    </style>
    """,
    unsafe_allow_html=True,
    )

    confidence = st.sidebar.slider("Confidence", min_value = 0.0, max_value = 1.0, value = 0.25)
    st.sidebar.markdown("---")

    # checkboxes
    save_image = st.sidebar.checkbox("Save Video")
    enable_GPU = st.sidebar.checkbox("Enable GPU")

    custom_classes = st.sidebar.checkbox("Use Custom Classes")
    assigned_class_id = []

    # custom classes
    if custom_classes:
        assigned_class = st.sidebar.multiselect("Select Custom Classes", list(names), default = 'person')
        for each in assigned_class:
            assigned_class_id.append(names.index(each))

    # upload out video
    video_file_buffer = st.sidebar.file_uploader("Upload a Video", type = ["mp4", "mov", "avi", "asf", "m4v"])
    DEMO_VIDEO = 'test.mp4'
    tfflie = tempfile.NamedTemporaryFile(suffix = '.mp4', delete = False)

    if not video_file_buffer:
        vid = cv2.VideoCapture(DEMO_VIDEO)
        tfflie.name = DEMO_VIDEO
        dem_vid = open(tfflie.name,'rb')
        demo_bytes = dem_vid.read()

        st.sidebar.text("Input Video")
        st.sidebar.video(demo_bytes)
    else:
        tfflie.write(video_file_buffer.read())
        dem_vid = open(tfflie.name,'rb')
        demo_bytes = dem_vid.read()

        st.sidebar.text("Input Video")
        st.sidebar.video(demo_bytes)

    print(tfflie.name)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass