# Virtual Glasses Try-On using OpenCV

This project allows users to try on different glasses in real-time using their webcam. It detects the user's face and eyes using Haar Cascade classifiers and overlays transparent PNG images of glasses on the face. Built using **Python** and **OpenCV**, it's a fun and interactive computer vision project.

---

##  Features

- Real-time face and eye detection
- Transparent overlay of glasses
- Multiple glasses selection by the user (keyboard switch)
- Easy to extend with more designs

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- Haar Cascade Classifiers (for face and eye detection)

---

## 📁 Folder Structure

 VirtualTryOn/
│
├── glass_image/ # Contains transparent PNG glasses
│ ├── glasses_01.png
│ ├── glasses_02.png
│ └── ...
│
├── models/ # Haarcascade XML files
│ ├── haarcascade_eye.xml
│ └── haarcascade_frontalface_alt.xml
│
├── virtual_try_on/
│ └── virtual_try_on.py # Main Python script


---

##  How to Run

### 1. Clone the Repository


git clone https://github.com/PittuVaishnavi6/Virtual-Glasses-Try-On-using-OpenCV.git
cd Virtual-Glasses-Try-On-using-OpenCV

2. Install Requirements
Install OpenCV using pip:

pip install opencv-python

3. Run the App
python virtual_try_on/virtual_try_on.py

How to Use
Press keys 1, 2, 3, etc. to switch between different glasses (based on your code).

Press Q to quit the application.

Make sure your face is clearly visible to the camera for accurate detection.

Adding More Glasses
To add new styles:

Place your PNG glasses with transparent background in the glass_image/ folder.

Make sure they are in the correct format (RGBA) and named properly (glasses_05.png, etc.).

Update the image-loading logic in virtual_try_on.py if needed.




