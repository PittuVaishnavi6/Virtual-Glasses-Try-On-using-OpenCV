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

```
VirtualTryOn/  
│  
├── glass_image/                # Contains transparent PNG glasses  
│   ├── glasses_01.png  
│   ├── glasses_02.png  
│   ├── glasses_03.png  
│   └── ...                     # Add more glasses as needed  
│  
├── models/                     # Haarcascade XML files  
│   ├── haarcascade_eye.xml  
│   └── haarcascade_frontalface_alt.xml  
│  
├── virtual_try_on/  
│   └── virtual_try_on.py       # Main Python script  
│  
└── README.md                   # Project documentation  
```



---

##  How to Run


### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PittuVaishnavi6/Virtual-Glasses-Try-On-using-OpenCV.git
cd Virtual-Glasses-Try-On-using-OpenCV
```

---

### 2️⃣ Install Requirements

Install OpenCV using pip:

```bash
pip install opencv-python
```

---

### 3️⃣ Run the App

```bash
python virtual_try_on/virtual_try_on.py
```

---

##  How to Use

- Press **1, 2, 3, etc.** to switch between different glasses (based on your code).
- Press **Q** to quit the application.
- Ensure your **face is clearly visible** to the camera for accurate detection.

---

##  Adding More Glasses

Want to try new styles? Follow these steps:

1. Add your transparent PNG glasses into the `glass_image/` folder.
2. Ensure each image:
   - Has a transparent background
   - Is in **RGBA** format
   - Is named properly, e.g., `glasses_05.png`, `glasses_06.png`, etc.
3. Update the image-loading logic in `virtual_try_on.py` if needed to support more images.





