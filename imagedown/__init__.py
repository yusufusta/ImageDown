import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import parse_qs, urlparse
from requests import get
import os

class ImageDown():
    def Google(self, *args):
        return GoogleSearch(*args)

    def Yandex(self, *args):
        return YandexSearch(*args)

class GoogleSearch():
    KEYWORD = ''
    LIMIT = 5
    URLS = []

    def __init__(self, keyword, limit = 5, domain = None):
        try:
            chromedriver_autoinstaller.install()
        except:
            raise Exception('Chromedriver error')
        self.KEYWORD = keyword
        self.LIMIT = limit
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")      

        self.DRIVER = webdriver.Chrome(options=chrome_options)
        if domain == None:
            self.DRIVER.get(f'https://www.google.com/search?q={keyword}&tbm=isch')
        else:
            self.DRIVER.get(f'https://www.google.com.{domain}/search?q={keyword}&tbm=isch')
        self.URLS = []

    def get_urls(self, baslangic = 1):
        urls = []
        for i in range(baslangic, (self.LIMIT + 1)):
            if i == (self.LIMIT + 1):
                break

            try:
                Div = self.DRIVER.find_element(
                        By.XPATH, f'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/div[{i}]/a[1]'
                    )
                
                Click = ActionChains(self.DRIVER)
                Click.context_click(Div).perform()
                url = parse_qs(urlparse(Div.get_attribute('href')).query)['imgurl'][0]
                urls.append(url)
            except NoSuchElementException:
                break
        self.URLS = urls
        return urls

    def download(self, folder = './imagedown/', gifs = False, paths_errors = False, timeout = 5):
        if not os.path.exists(folder):
            os.makedirs(folder)
        paths = []
        if self.URLS == []:
            raise Exception('no url found')
        for num, url in enumerate(self.URLS):
            try:
                Req = get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
                }, timeout=timeout)
            except:
                if paths_errors:
                    paths.append(False)
                    continue
            Type = Req.headers["content-type"]

            if Type.startswith('image/'):
                Extension = Type.split("image/")[1]
                
                try:
                    if Extension == 'gif' and gifs:
                        open(f'{folder}{self.KEYWORD}-{num}.{Extension}', 'wb').write(Req.content)
                    elif not Extension == 'gif':
                        open(f'{folder}{self.KEYWORD}-{num}.{Extension}', 'wb').write(Req.content)
                    paths.append(f'{folder}{self.KEYWORD}-{num}.{Extension}')
                except:
                    if paths_errors:
                        paths.append(False)
            else:
                if paths_errors:
                    paths.append(False)
        return paths


class YandexSearch():
    KEYWORD = ''
    LIMIT = 5
    URLS = []

    def __init__(self, keyword, limit = 5):
        try:
            chromedriver_autoinstaller.install()
        except:
            raise Exception('Chromedriver error')
        self.KEYWORD = keyword
        self.LIMIT = limit
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")      

        self.DRIVER = webdriver.Chrome(options=chrome_options)
        self.DRIVER.get(f'https://yandex.com/images/search?text={keyword}')
        self.URLS = []

    def get_urls(self, baslangic = 1):
        urls = []
        for i in range(baslangic, (self.LIMIT + 1)):
            if i == (self.LIMIT + 1):
                break

            try:
                Div = self.DRIVER.find_element(
                        By.XPATH, f'/html/body/div[5]/div[1]/div[1]/div[1]/div/div[{i}]/div/a'
                    )
                
                url = parse_qs(urlparse(Div.get_attribute('href')).query)['img_url'][0]
                urls.append(url)
            except NoSuchElementException:
                break
        self.URLS = urls
        return urls

    def download(self, folder = './imagedown/', gifs = False, paths_errors = False, timeout = 5):
        if not os.path.exists(folder):
            os.makedirs(folder)
        paths = []
        if self.URLS == []:
            raise Exception('no url found')
        for num, url in enumerate(self.URLS):
            try:
                Req = get(url, headers={
                    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
                }, timeout=timeout)
            except:
                if paths_errors:
                    paths.append(False)
                    continue
            Type = Req.headers["content-type"]

            if Type.startswith('image/'):
                Extension = Type.split("image/")[1]
                
                try:
                    if Extension == 'gif' and gifs:
                        open(f'{folder}{self.KEYWORD}-{num}.{Extension}', 'wb').write(Req.content)
                    elif not Extension == 'gif':
                        open(f'{folder}{self.KEYWORD}-{num}.{Extension}', 'wb').write(Req.content)
                    paths.append(f'{folder}{self.KEYWORD}-{num}.{Extension}')
                except:
                    if paths_errors:
                        paths.append(False)
            else:
                if paths_errors:
                    paths.append(False)
        return paths
