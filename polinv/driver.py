import os
import shutil
import requests
import pyautogui

import undetected_chromedriver as uc
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.proxy import Proxy, ProxyType
#from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = 'chromedriver.exe'
TEMP_PROFILES_PATH = '.polinv-temp'

class Driver(uc.Chrome):

    def __init__(self, profile: str, version_main: int = 126, show_images: bool = True, corner: int = -1, rowspan: bool = False,
                maximize_window: bool = False, headless: bool = False, clear_dir: bool = False):

        self.profile = profile
        self.user_data_dir = os.path.join(TEMP_PROFILES_PATH, profile)

        if clear_dir and os.path.exists(self.user_data_dir): shutil.rmtree(self.user_data_dir)

        os.makedirs(self.user_data_dir, exist_ok=True)

        opts = uc.ChromeOptions()
        if not show_images: opts.add_argument('--blink-settings=imagesEnabled=false')

        super().__init__(user_data_dir=self.user_data_dir, version_main=version_main, driver_executable_path=CHROME_DRIVER_PATH, options=opts, headless=headless)

        if not headless and corner != -1:
            screen_width, screen_height = pyautogui.size()
            self.set_window_size(screen_width // 2, screen_height // 2)
            if   corner == 0: self.set_window_position(0, 0)
            elif corner == 1: self.set_window_position(screen_width // 2, 0)
            elif corner == 2: self.set_window_position(0, screen_height // 2)
            elif corner == 3: self.set_window_position(screen_width // 2, screen_height // 2)

        if not headless and rowspan: self.set_window_size(screen_width // 2, screen_height)
        if not headless and maximize_window: self.maximize_window()

    def save_cookies(self, cookies_jar: requests.cookies.CookieJar):
        cookies = self.get_cookies()
        for cookie in cookies: cookies_jar.set_cookie(requests.cookies.create_cookie(**cookie))
        return cookies_jar

    def load_cookies(self, domain: str, cookie_jar):
        domain = domain.replace('https://', '')
        for cookie in cookie_jar:
            if not domain in cookie.domain: continue
            cookie_dict = { 'name': cookie.name, 'value': cookie.value, 'domain': cookie.domain, 'secure': cookie.secure }
            if cookie.expires: cookie_dict['expiry'] = cookie.expires
            if cookie.path_specified: cookie_dict['path'] = cookie.path
            self.add_cookie(cookie_dict)

        self.refresh()