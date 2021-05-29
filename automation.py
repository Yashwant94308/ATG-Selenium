from selenium import webdriver
from time import sleep


class ATG:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("C:\\Users\\asus\\Desktop\\web_scapping\\chromedriver_win32\\chromedriver.exe")

        # Username and password
        self.username = username
        self.password = password

        self.driver.get("https://www.atg.party/")
        sleep(1)  # 1 Second Wait
        self.driver.maximize_window()

        self.driver.find_element_by_link_text('Login').click()

        sleep(1)
        self.driver.find_element_by_id('email').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password)

        # Clicks on Log In Button
        self.driver.find_element_by_xpath('//*[@id="frm_landing_page_user_login"]/div[3]/button').click()
        sleep(2)

        self.driver.get('https://www.atg.party/article')
        sleep(1)
        Title = "Books"
        detail = "books are best for students"
        self.driver.find_element_by_id('title').send_keys(Title)
        self.driver.find_element_by_xpath('//*[@id="description"]/div/div[1]/div/div/div').send_keys(detail)
        sleep(1)
        # self.driver.find_element_by_id('cover-image-container').send_keys("G://Flickr/book.jpg")
        # sleep(5)

        self.driver.find_element_by_xpath('//*[@id="hpost_btn"]').click()
        sleep(30)



ATG('wiz_saurabh@rediffmail.com', 'Pass@123')
