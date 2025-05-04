import pyautogui
import cv2
import numpy as np
import time
import os

# 이미지 인식 및 클릭 함수 (모든 위치 클릭)
def find_and_click_all(template_path, confidence=0.95):
    screenshot = pyautogui.screenshot()
    screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= confidence)

    w, h = template.shape[1], template.shape[0]

    points_clicked = []
    for pt in zip(*loc[::-1]):
        center_x, center_y = pt[0] + w // 2, pt[1] + h // 2

        # 중복 클릭 방지 (근처 좌표 무시)
        if not any(abs(center_x - x) < 10 and abs(center_y - y) < 10 for (x, y) in points_clicked):
            pyautogui.click(center_x, center_y)
            points_clicked.append((center_x, center_y))
            time.sleep(0.05)  # 너무 빠르면 클릭이 씹힐 수 있음

    return len(points_clicked)

# 실행 전 대기
print("3초 후 시작합니다. 창을 준비해주세요!")
time.sleep(3)

# 1~9 사과 순서대로 클릭
for i in range(1, 10):
    template_file = f'templates/{i}.png'
    if not os.path.exists(template_file):
        print(f"[경고] {template_file} 없음 — 스킵")
        continue

    count = find_and_click_all(template_file)
    print(f"{i} 사과 {count}개 클릭 완료")
    time.sleep(0.2)
