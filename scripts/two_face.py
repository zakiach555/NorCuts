import cv2
import mediapipe as mp
import numpy as np

def crop_and_maintain_ar(frame, face_box, target_w, target_h, zoom_out_factor=2.2):
    img_h, img_w, _ = frame.shape
    x, y, w, h = face_box

    cx = x + w // 2
    cy = y + h // 2

    face_size = max(w, h)
    req_h = face_size * zoom_out_factor

    target_ar = target_w / target_h
    crop_h = req_h
    crop_w = crop_h * target_ar

    if crop_w > img_w:
        crop_w = float(img_w)
        crop_h = crop_w / target_ar

    if crop_h > img_h:
        crop_h = float(img_h)
        crop_w = crop_h * target_ar

    crop_w = int(crop_w)
    crop_h = int(crop_h)

    x1 = int(cx - crop_w // 2)
    y1 = int(cy - crop_h // 2)

    if x1 < 0:
        x1 = 0
    elif x1 + crop_w > img_w:
        x1 = img_w - crop_w

    if y1 < 0:
        y1 = 0
    elif y1 + crop_h > img_h:
        y1 = img_h - crop_h

    x2 = x1 + crop_w
    y2 = y1 + crop_h

    cropped = frame[y1:y2, x1:x2]

    if cropped.size == 0 or cropped.shape[0] == 0 or cropped.shape[1] == 0:
        return np.zeros((target_h, target_w, 3), dtype=np.uint8)

    resized = cv2.resize(cropped, (target_w, target_h), interpolation=cv2.INTER_LINEAR)
    return resized

def crop_and_resize_two_faces(frame, face_positions, zoom_out_factor=2.2):
    target_w = 1080
    target_h = 960

    if len(face_positions) < 2:
        return np.zeros((1920, 1080, 3), dtype=np.uint8)

    face1_img = crop_and_maintain_ar(frame, face_positions[0], target_w, target_h, zoom_out_factor)
    face2_img = crop_and_maintain_ar(frame, face_positions[1], target_w, target_h, zoom_out_factor)

    return np.vstack((face1_img, face2_img))


def detect_face_or_body_two_faces(frame, face_detection, face_mesh, pose):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results_face_detection = face_detection.process(frame_rgb)
    results_face_mesh = face_mesh.process(frame_rgb)
    results_pose = pose.process(frame_rgb)

    face_positions_detection = []
    if results_face_detection.detections:
        for detection in results_face_detection.detections[:2]:
            bbox = detection.location_data.relative_bounding_box
            x_min = int(bbox.xmin * frame.shape[1])
            y_min = int(bbox.ymin * frame.shape[0])
            width = int(bbox.width * frame.shape[1])
            height = int(bbox.height * frame.shape[0])
            face_positions_detection.append((x_min, y_min, width, height))

    if len(face_positions_detection) == 2:
        return face_positions_detection

    face_positions_mesh = []
    if results_face_mesh.multi_face_landmarks:
        for landmarks in results_face_mesh.multi_face_landmarks[:2]:
            x_coords = [int(landmark.x * frame.shape[1]) for landmark in landmarks.landmark]
            y_coords = [int(landmark.y * frame.shape[0]) for landmark in landmarks.landmark]
            x_min, x_max = min(x_coords), max(x_coords)
            y_min, y_max = min(y_coords), max(y_coords)
            width = x_max - x_min
            height = y_max - y_min
            face_positions_mesh.append((x_min, y_min, width, height))

    if len(face_positions_mesh) == 2:
        return face_positions_mesh
        
    # If neither found 2, return what we found (prefer detection as it is bounding box optimized)
    if face_positions_detection:
        return face_positions_detection
    if face_positions_mesh:
        return face_positions_mesh

    if results_pose.pose_landmarks:
        x_coords = [lmk.x for lmk in results_pose.pose_landmarks.landmark]
        y_coords = [lmk.y for lmk in results_pose.pose_landmarks.landmark]
        x_min = int(min(x_coords) * frame.shape[1])
        x_max = int(max(x_coords) * frame.shape[1])
        y_min = int(min(y_coords) * frame.shape[0])
        y_max = int(max(y_coords) * frame.shape[0])
        width = x_max - x_min
        height = y_max - y_min
        return [(x_min, y_min, width, height)]

    return None
