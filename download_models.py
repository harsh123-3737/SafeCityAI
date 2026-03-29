import os
import requests

def download_file(url, save_path):
    print(f"Downloading {save_path}...")
    response = requests.get(url, stream=True)
    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print("Done!")

# Replace these with your PUBLIC Google Drive direct links
models = {
    "models/helmet_best.pt": "https://drive.google.com/file/d/1wNt4vqc6D2RM3ox3-l8EjvaYywBN59bB/view?usp=sharing",
    "models/plate_best.pt": "https://drive.google.com/file/d/1CAN98YPmxTOBtMx0Wg2-yCb1HKomsgQn/view?usp=sharing"
}

os.makedirs("models", exist_ok=True)
for path, url in models.items():
    download_file(url, path)
