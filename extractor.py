from bs4 import BeautifulSoup as bs
from env import _id, _password
from selenium import webdriver

class CrawlBrowser:
    # browser = None
    option = None
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        self.browser = webdriver.Chrome('chromedriver', chrome_options=options)
        self.data = {}
        
    # def __del__(self):
        # self.browser.close()
        # print ("browser closed")

        

    def login(self):
        self.url = "https://apply.likelion.org/accounts/login/"
        self.browser.get(self.url)

        self.browser.find_element_by_name('username').send_keys(_id)
        self.browser.find_element_by_name('password').send_keys(_password)

        self.browser.find_element_by_xpath("/html/body/main/div[2]/div/div/div/form/div[3]/button").click()
        self.browser.implicitly_wait(2)
    
    def get_list(self):
        self.url = "https://apply.likelion.org/apply/univ/20"
        self.browser.get(self.url)
        
        html = self.browser.page_source
        soup = bs(html, 'html.parser')
        selections = soup.select("#likelion_num > div.applicant_page > a")
        
        for idx , val in enumerate(selections):
            url = val['href']
            name = val.find('p','user_name').text
            year = val.find('p','user_profile').text.split(' ')[0]
            department = val.find('p','user_profile').text.split(' ')[1]
            self.data[idx] = {
                'url': url,
                'name': name,
                'year': year,
                'department': department
                }
        self.browser.implicitly_wait(2)


    def get_detail(self, idx):
        self.url = "https://apply.likelion.org"+self.data[idx]['url']
        self.browser.get(self.url)

        html = self.browser.page_source
        soup = bs(html, 'html.parser')
        selections = soup.select("div.user_information")

        phone = selections[0].find('div','s_mt').find_all('p')[0].text
        email = selections[0].find('div','s_mt').find_all('p')[2].text
        github = selections[1].find('p').text
        file = str(selections[2].find('a'))

        self.data[idx].update({
            'phone' : phone,
            'email' : email,
            'github': github,
            'file'  : file
        })

        selections = soup.select("div.answer_view > div.applicant_detail_page > div > div.m_mt > div.answer-font")

        for i, v in enumerate(selections):
            self.data[idx].update({
                "Q"+str(i) : v.text
            })

        