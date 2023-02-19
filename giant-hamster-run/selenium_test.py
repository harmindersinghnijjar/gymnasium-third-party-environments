# Import modules
from gym import Env
from gym.spaces import Discrete, Box
from mss import mss
from PIL import Image, ImageEnhance, ImageOps
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager
import cv2 as cv2
import getpass
import keyboard
import matplotlib.pyplot as plt
import numpy as np
import os
import pydirectinput
import pytesseract
import random
import tensorflow as tf                                                               
import time
import tqdm as tqdm

# Define PC user
user = getpass.getuser()

# Define tesseract path
pytesseract.pytesseract.tesseract_cmd = r'E:\Program Files\Tesseract-OCR\tesseract.exe'

# Create class for Selenium
class Selenium:
    def __init__(self, user_agent='default_user_agent'):
        self.user_agent = user_agent
        self.browser = None
    
    def close_all_chrome_instances(self):
        os_command = 'taskkill /im chrome.exe /f'
        os.system(os_command)
    
    def delay(self, seconds):
        time.sleep(seconds)
    
    def wait_until_visible(self, selector: str, timeout: int = 10):
        WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    
    def wait_until_clickable(self, selector: str, timeout: int = 10):
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    
    def browser_setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument(f'user-agent={self.user_agent}')
        options.add_argument('--headed')
        options.add_experimental_option('prefs', {'download.default_directory': f'C:\\Users\\{user}\\Downloads'})
        options.add_argument(f'--user-data-dir=C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
        options.add_argument(f'--profile-directory=Profile 1')
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return self.browser
    
    def get_to_game_screen(self):
        self.close_all_chrome_instances()
        self.browser_setup()
        self.browser.set_window_position(0, 0)
        self.browser.maximize_window()
        url = 'https://www.inboxdollars.com/games/gianthamsterrun'
        self.browser.get(url)
        self.wait_until_visible('#game-and-ad-wrapper')
        self.browser.switch_to.frame(self.browser.find_element(By.CSS_SELECTOR, '#game-window'))
    
    def screen_capture(self):
        with mss() as sct:
            monitor = {'top': 335, 'left': 510, 'width': 480, 'height': 480}
            screenshot = sct.grab(monitor)
            image = np.array(screenshot)
            plt.imshow(image)
            # User doesn't need to see the canvas
            # plt.show()
            cv2.imwrite('canvas.png', image)
            # plt.close()      
    
    def process_image(self):
        # Load the image
        img = cv2.imread('canvas.png')

        # # Resize the image
        # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)

        # Convert to grayscale
        gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Invert the image
        inv = cv2.bitwise_not(gry)
        
        # Apply OCR
        text = pytesseract.image_to_string(gry, lang='eng', config='--psm 6')
        text = text.replace("\n\x0c", "") 

        # Print the text
        print(text)
        return text

        # Save the processed image
        cv2.imwrite('processed.png', inv)

    def check_for_play_button(self):
        text = self.process_image()
        if text == 'Hamster Run':
            self.click_play_button()
            return True
        
    def click_play_button(self):
        pydirectinput.click(750, 800)
        time.sleep(5)        


    def close(self):
        self.browser.quit()

# Continously display  the processed image
def display_image():
    while True:
        if os.path.exists('processed.png'):
            image = cv2.imread('processed.png')
            cv2.imshow('image', image)
            cv2.waitKey(1)
            if cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
                break