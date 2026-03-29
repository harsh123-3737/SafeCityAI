import streamlit as st
import torch
import numpy as np
import os
from PIL import Image

st.set_page_config(page_title="SafeCityAI Hub", layout="wide")
st.title("🚨SafecityAI: Universal monitor")

#here we are loading the models
@st.cache_resource
def load_models():
  h_model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/drive/MyDrive/SafeCityAI_Models/helmet_best.pt')
  p_model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/drive/MyDrive/SafeCityAI_Models/plate_best.pt')
  return h_model, p_model

h_model, p_model = load_models()

#we are creating the tabs for Image and video
tab1, tab2 = st.tabs(["📸 Image Inference", "📹 Video Inference"])

#---logic for tab1---
with tab1:
  st.header("Single Photo Scan")
  img_file = st.camera_input("Take a photo of a rider")
  if img_file:
    img = Image.open(img_file)
    img_array = np.array(img)
    h_model.conf = 0.6
    p_model.conf = 0.6

    results = h_model(img_array)

    df = results.pandas().xyxy[0]
    if df.empty:
      st.success("✅ No Violations or helemets detected in this photo")
    else:
      st.image(np.squeeze(results.render()), caption="Scan Result")

      p_results = p_model(img_array)
      st.image(np,squeeze(p_results.render()), caption="Plate Scan")

#--logic for tab2---
with tab2:
    st.header("30-Second Video Processing")
    video_file = st.file_uploader("Upload street footage", type=['mp4', 'mov', 'avi'])

    if video_file:
        input_path = "/content/input_video.mp4"
        with open(input_path, "wb") as f:
            f.write(video_file.getbuffer())
        
        st.info("🔄 Running Double-Pass AI (Helmets then Plates)...")
        
        # Paths
        h_weights = "/content/drive/MyDrive/SafeCityAI_Models/helmet_best.pt"
        p_weights = "/content/drive/MyDrive/SafeCityAI_Models/plate_best.pt"
        
        # PASS 1: Detect Helmets
        st.write("🕵️‍♂️ Scanning for Helmets...")
        os.system(f"python /content/yolov5/detect.py --weights {h_weights} --source {input_path} --project /content/runs --name step1 --exist-ok --conf 0.4")
        
        step1_video = "/content/runs/step1/input_video.mp4"
        
        if os.path.exists(step1_video):
            # PASS 2: Detect Plates on the already processed video
            st.write("🕵️‍♂️ Scanning for License Plates...")
            os.system(f"python /content/yolov5/detect.py --weights {p_weights} --source {step1_video} --project /content/runs --name step2 --exist-ok --conf 0.4")
            
            step2_video = "/content/runs/step2/input_video.mp4"
            
            if os.path.exists(step2_video):
                st.write("📱 Optimizing for mobile...")
                os.system(f"ffmpeg -y -i {step2_video} -vcodec libx264 -f mp4 /content/final_demo.mp4")
                st.success("✅ Both models applied successfully!")
                st.video("/content/final_demo.mp4")
            else:
                st.error("Plate detection failed in second pass.")
        else:
            st.error("Helmet detection failed in first pass.")
