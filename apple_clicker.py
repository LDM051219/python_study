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


        if not any(abs(center_x - x) < 10 and abs(center_y - y) < 10 for (x, y) in points_clicked):
            pyautogui.click(center_x, center_y)
            points_clicked.append((center_x, center_y))
            time.sleep(0.05)  

    return len(points_clicked)


print("3초 후 시작합니다. 창을 준비해주세요!")
time.sleep(3)

for i in range(1, 10):
    template_file = f'templates/{i}.png'
    if not os.path.exists(template_file):
        print(f"[경고] {template_file} 없음 — 스킵")
        continue

    count = find_and_click_all(template_file)
    print(f"{i} 사과 {count}개 클릭 완료")
    time.sleep(0.2)
