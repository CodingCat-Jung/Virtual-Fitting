# import cv2
# import mediapipe as mp
# import numpy as np
# import os

# # MediaPipe Pose 모델 초기화
# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # 배경 제거된 옷 이미지 로드
# clothing_path = "processed_clothing.png"
# if not os.path.exists(clothing_path):
#     print("❌ 배경 제거된 옷 이미지가 없습니다! 먼저 remove_bg_rembg() 실행하세요.")
#     exit()

# clothing = cv2.imread(clothing_path, cv2.IMREAD_UNCHANGED)

# # 카메라 실행
# cap = cv2.VideoCapture(0)

# def overlay_image(background, overlay, x, y, scale=1.2):
#     """배경 제거된 옷을 신체 위치에 맞게 합성하는 함수"""
#     h, w, _ = overlay.shape
#     h = int(h * scale)
#     w = int(w * scale)

#     overlay_resized = cv2.resize(overlay, (w, h))

#     # ROI 설정
#     roi = background[y:y+h, x:x+w]

#     # 알파 채널 분리 (투명도 적용)
#     overlay_rgb = overlay_resized[:, :, :3]
#     mask = overlay_resized[:, :, 3] / 255.0

#     for c in range(3):
#         roi[:, :, c] = (1 - mask) * roi[:, :, c] + mask * overlay_rgb[:, :, c]

#     background[y:y+h, x:x+w] = roi
#     return background

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ 카메라 프레임을 가져올 수 없습니다!")
#         break

#     frame = cv2.flip(frame, 1)  # 좌우 반전 (거울 효과)
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = pose.process(frame_rgb)

#     if results.pose_landmarks:
#         landmarks = results.pose_landmarks.landmark

#         # 어깨 좌표 가져오기
#         left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
#         right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

#         # 픽셀 좌표 변환
#         left_x, left_y = int(left_shoulder.x * frame.shape[1]), int(left_shoulder.y * frame.shape[0])
#         right_x, right_y = int(right_shoulder.x * frame.shape[1]), int(right_shoulder.y * frame.shape[0])

#         # 옷 크기 조정
#         clothing_width = right_x - left_x
#         clothing_height = int(clothing.shape[0] * (clothing_width / clothing.shape[1]))

#         # 옷 배치 위치 (어깨 아래)
#         x = left_x
#         y = left_y

#         # 오버레이
#         frame = overlay_image(frame, clothing, x, y, scale=1.2)

#     cv2.imshow("Virtual Fitting", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
print("OpenCV 버전:", cv2.__version__)
print("cv2.VideoCapture 지원 여부:", hasattr(cv2, "VideoCapture"))



# import cv2

# cap = cv2.VideoCapture(0)  # 카메라 열기

# if not cap.isOpened():
#     print("❌ 카메라를 열 수 없습니다! 다른 카메라를 시도해보세요.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ 카메라 프레임을 읽을 수 없습니다!")
#         break

#     cv2.imshow("Camera Test", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
