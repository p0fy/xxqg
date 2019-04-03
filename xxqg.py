import time
import base64
from selenium import webdriver

class XXQGBot:
    def __init__(self):
        opts = webdriver.ChromeOptions()
        # opts.add_argument('headless')
        # opts.add_argument('disable-gpu')
        opts.add_argument('no-sandbox')
        opts.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"')
        self.d = webdriver.Chrome(chrome_options=opts)
        self.d.maximize_window()
        self.qrcode = 'code.png'
        self.article_num = 6

    def login(self):
        self.d.get('https://pc.xuexi.cn/points/login.html?ref=https://www.xuexi.cn/')
        time.sleep(2)
        self.d.switch_to_frame('ddlogin-iframe')
        b64 = self.d.find_element_by_xpath('//div[@id="qrcode"]/img').get_attribute('src')
        with open(self.qrcode, 'wb')as f:
            f.write(base64.b64decode(b64.split(',')[-1]))
        print('qrcode saved!')

    def wait_for_logged(self):
        while 1:
            if 'login' not in self.d.current_url:
                break
            time.sleep(2)
        print('Login successfully!')

    def to_homepage(self):
        if self.d.current_url != 'https://www.xuexi.cn/':
            self.d.get('https://www.xuexi.cn/')
            time.sleep(2)

    def read_article(self):
        self.wait_for_logged()
        self.to_homepage()
        articles = self.d.find_elements_by_xpath('//div[@class="word-item"]')[:self.article_num]
        main_handle = self.d.current_window_handle
        for article in articles:
            article.click()
            time.sleep(2)
            handles = self.d.window_handles
            for handle in handles:
                if handle != main_handle:
                    self.d.switch_to_window(handle)
                    break
            print('reading ', self.d.current_url)
            height = self.d.execute_script('return document.body.scrollHeight;')
            avg_height = height / self.article_num
            for i in range(self.article_num):
                print('reading part', i+1)
                self.d.execute_script('window.scrollTo(0, {})'.format((i+1)*avg_height))
                time.sleep(60)
            self.d.close()
            self.d.switch_to_window(main_handle)
            
    # def watch_video(self):
    #     self.wait_for_logged()
    #     self.to_homepage()
    #     self.d.find_element_by_link_text(u'').click()
    #     # videos = self.d.find_elements_by_xpath('//div[starts-with(@id, "swing_")]/ul/li/img')
    #     for video in videos:


if __name__ == '__main__':
    zz = XXQGBot()
    zz.login()
    zz.read_article()

    