from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.gamesaien.com/game/fruit_box_a/")

time.sleep(3)

canvas = driver.find_element(By.ID, "canvas")


ActionChains(driver)\
    .move_to_element_with_offset(canvas, 300, 250)\
    .click()\
    .perform()
