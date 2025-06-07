import cv2
import numpy as np
import os

# Load face and eye models
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_alt.xml")
eye_cascade = cv2.CascadeClassifier("models/haarcascade_eye.xml")

# Load all glasses from the folder
glass_folder = "glass_image"
glass_images = [cv2.imread(os.path.join(glass_folder, f), cv2.IMREAD_UNCHANGED)
                for f in sorted(os.listdir(glass_folder)) if f.endswith(".png")]

current_glass_index = 0  # Start with the first glasses

def overlay_transparent(background, overlay, x, y):
    bg_h, bg_w = background.shape[:2]
    if x >= bg_w or y >= bg_h:
        return background

    h, w = overlay.shape[:2]
    if x + w > bg_w:
        w = bg_w - x
        overlay = overlay[:, :w]
    if y + h > bg_h:
        h = bg_h - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [overlay, np.ones((overlay.shape[0], overlay.shape[1], 1), dtype=overlay.dtype) * 255], axis=2
        )

    overlay_img = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] + mask * overlay_img
    return background

cap = cv2.VideoCapture(0)
last_position = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        if len(eyes) >= 2:
            eye_1, eye_2 = eyes[0], eyes[1]
            eye_center_1 = (x + eye_1[0] + eye_1[2] // 2, y + eye_1[1] + eye_1[3] // 2)
            eye_center_2 = (x + eye_2[0] + eye_2[2] // 2, y + eye_2[1] + eye_2[3] // 2)

            if eye_center_1[0] > eye_center_2[0]:
                eye_center_1, eye_center_2 = eye_center_2, eye_center_1

            glass_img = glass_images[current_glass_index]
            glasses_width = int(2.5 * abs(eye_center_2[0] - eye_center_1[0]))
            scale_factor = glasses_width / glass_img.shape[1]
            new_glass_height = int(glass_img.shape[0] * scale_factor)
            resized_glasses = cv2.resize(glass_img, (glasses_width, new_glass_height), interpolation=cv2.INTER_AREA)

            x_offset = eye_center_1[0] - int(0.28 * glasses_width)
            y_offset = eye_center_1[1] - int(0.5 * new_glass_height)

            last_position = (resized_glasses, x_offset, y_offset)

        if last_position:
            frame = overlay_transparent(frame, *last_position)

    cv2.putText(frame, f'Press 1-{len(glass_images)} to change glasses', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow('Virtual Try-On', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif ord('1') <= key <= ord(str(len(glass_images))):
        current_glass_index = key - ord('1')

cap.release()
cv2.destroyAllWindows()
