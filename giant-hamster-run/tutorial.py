# Import selenium-test
from selenium_test import Selenium

# Define user-agents
PC_USER_AGENTS = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
MOBILE_USER_AGENTS = 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36'


if __name__ == '__main__':
    selenium = Selenium(PC_USER_AGENTS)
    selenium.get_to_game_screen()
    while True:
        selenium.screen_capture()
        selenium.process_image()
        # Wait for 10 seconds before checking for play button
        selenium.delay(10)
        if selenium.check_for_play_button:
            selenium.click_play_button()
        

       