# 🚨 SafeCityAI: Real-Time Traffic Monitor

A dual-model AI system designed to detect helmet violations and license plates from live mobile feeds or recorded video.

### 🛠️ Key Features
- **Sequential Inference:** Processes Helmet and Plate detection in a two-pass pipeline for high accuracy.
- **Mobile-Cloud Sync:** Deployed via Ngrok to allow field testing on smartphones.
- **Optimization:** Uses FFmpeg to ensure AI-processed video is viewable on mobile browsers.

  **run these two commands in their terminal:**

git clone https://github.com/ultralytics/yolov5 (This gives them the detection script).

pip install -r yolov5/requirements.txt

### 🚀 How to Run
1. Clone this repo: `git clone https://github.com/yourusername/SafeCityAI.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

### 📊 Models Used
- YOLOv5s (Custom trained for Helmets)
- YOLOv5s (Custom trained for License Plates)

** run the download_models.py script  When a you  runs that script, it will automatically download .pt models files from my drive and  put them inside the models folder and try the working of safecity ai**

 **demo link that i have tried you can check the video **
 https://drive.google.com/file/d/119bAIVB0WIvt23twKe-neNiod3RZ9Iry/view?usp=drive_link
 
