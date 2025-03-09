# **딥러닝 기반 배경 제거 라이브러리 rembg**를 사용하여 옷의 배경을 제거하고,
# 배경이 투명한 PNG 파일로 저장하는 기능

from rembg import remove
from PIL import Image
import os

def remove_bg_rembg(image_path):
    
    """딥러닝 기반 rembg를 이용한 배경 제거"""
    
    # 한글 파일명을 지원하기 위해 절대 경로로 변경
    abs_image_path = os.path.abspath(image_path)
    
    # 이미지 로드
    image = Image.open(abs_image_path)

    # 배경 제거
    result = remove(image)

    # 저장할 경로 설정
    save_path = os.path.join(os.path.dirname(abs_image_path), "processed_clothing.png")
    
    # 배경이 투명한 PNG로 저장
    result.save(save_path, format="PNG")

    print("✅ 배경 제거 완료! 저장된 파일:", save_path)
    return save_path

# 실행 예제
remove_bg_rembg("바지 test.png")
