# 🚨 SafeCityAI: Real-Time Traffic Monitor

A dual-model AI system designed to detect helmet violations and license plates from live mobile feeds or recorded video.

### 🛠️ Key Features
- **Sequential Inference:** Processes Helmet and Plate detection in a two-pass pipeline for high accuracy.
- **Mobile-Cloud Sync:** Deployed via Ngrok to allow field testing on smartphones.
- **Optimization:** Uses FFmpeg to ensure AI-processed video is viewable on mobile browsers.

### 🚀 How to Run
1. Clone this repo: `git clone https://github.com/yourusername/SafeCityAI.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

### 📊 Models Used
- YOLOv5s (Custom trained for Helmets)
- YOLOv5s (Custom trained for License Plates)
