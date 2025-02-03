# Virtual-Fitting

우선 목표 - 컴퓨터 비전 기능 사용해서 가상 피팅 서비스 개발 + 배포는 웹앱
최종 목표 - AR 기능 추가

FE - React.js
BE - FastAPI / OpenCV + Mediapipe
DB - MySQL
Cloud

1. 사용자 관리 시스템 - BE
회원가입, 로그인/ 로그아웃

2. 이미지 업로드 및 저장 - BE
사용자가 옷 이미지 업로드

3. 의류 이미지 추출 - AI
OpenCV, Mediapipe (or TensorFlow) 통해 의류 이미지 배경 분리

4. 가상 피팅 합성 - AI
의류 이미지를 실시간 카메라 화면에 합성

5. 사용자 인터페이스 - FE
직관적이고 사용자 친화적인 웹 UI

6. 테스트 및 배포
