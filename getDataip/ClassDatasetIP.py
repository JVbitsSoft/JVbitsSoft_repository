from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request
from datetime import datetime
import time

class DatasetIP():
    def __init__(self):
        self.external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('window-size=1920x1480')
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.headless = False
    def get_external_ipv4(self):
        ip = self.external_ip
        now = datetime.now()
        return f"External IPv4 Address: {ip} {now.strftime('[%d/%m/%Y %H:%M:%S]')}"
    def get_dataset_without_api(self, ip=None, countdown=10):
        self.chrome_browser = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=self.options)
        self.chrome_browser.get('https://ipstack.com/')
        
        if ip != None:
            self.ip_w0 = ip
            self.countdown = countdown

            #<label for="ipcheck_submit">Look Up</label>
            self.chrome_browser.find_element_by_xpath('//label[@for="ipcheck_submit"]').click()

            #<input type="text" name="iptocheck" placeholder="Enter an IP Address" value="exemple_ip">
            self.chrome_browser.find_element_by_xpath('//input[@placeholder="Enter an IP Address"]')
            enter_ip = self.chrome_browser.find_element_by_xpath('//input[@name="iptocheck"]')
            enter_ip.click()
            enter_ip.send_keys(Keys.CONTROL + 'a')
            enter_ip.send_keys(Keys.DELETE)
            enter_ip.send_keys(self.ip_w0)
            enter_ip.send_keys(Keys.ENTER)
            time.sleep(self.countdown)

        #<div class="rows"><div class="row string" data-object="ip"><i></i> ...//... </span></div></div></div></div>
        html = self.chrome_browser.page_source
        
        self.chrome_browser.close()

        part = len('</span></div></div></div></div>')
        raw_elements = html[html.find('<div class="rows"><div class="row string" data-object="ip"><i></i>ip: <span>'): (html.find('</span></div></div></div></div>')+part)]

        dict_elements = {
            'ip: ': None, 
            'type: ': None,
            'continent_code: ': None,
            'continent_name: ': None,
            'country_code: ': None,
            'country_name: ': None,
            'region_code: ': None,
            'region_name: ': None,
            'city: ': None,
            'zip: ': None,
            'latitude: ': None,
            'longitude: ': None,
            'location: ': None,
                'geoname_id: ': None,
                'capital: ': None,
                'languages: ': None,
                    'code: ': None,
                    'name: ': None,
                    'native: ': None,
                'country_flag: ': None,
                'country_flag_emoji: ': None,
                'country_flag_emoji_unicode: ': None,
                'calling_code: ': None,
                'is_eu: ': None,
            'time_zone: ': None,
                'id: ': None,
                'current_time: ': None,
                'gmt_offset: ': None,
                'code: ': None,
                'is_daylight_saving: ': None,
            'currency: ': None,
                'code: ': None,
                'name: ': None,
                'plural: ': None,
                'symbol: ': None,
                'symbol_native: ': None,
            'connection: ': None,
                'asn: ': None,
                'isp: ': None,
            'security: ': None,
                'is_proxy: ': None,
                'proxy_type: ': None,
                'is_crawler: ': None,
                'crawler_name: ': None,
                'crawler_type: ': None,
                'is_tor: ': None,
                'threat_level: ': None,
                'threat_types: ': None}

        for element_key in dict_elements:
            element_span = element_key+'<span>'
            raw_elements = raw_elements[raw_elements.find(element_span)+len(element_span):]
            dict_elements[element_key] = raw_elements[:raw_elements.find('<')]

        limit = False
        b = True
        while b:
            var = html.find('<div class="i_body error rate_limit_exceeded"></div>')
            if var != -1:
                b = False
                limit = True
            else:
                b = False
                
        if limit:
            return 'Limit exceeded, use of VPN recommended ...'
        else:
            return dict_elements
    def get_dataset_with_api(self, email, password, ip=None, hostname=None, time_zone=None, currency=None, security=None):
        self.chrome_browser = webdriver.Chrome(executable_path=r'./chromedriver.exe', chrome_options=self.options)
        self.chrome_browser.get('https://ipstack.com/login')

        b = True
        while b:
            pass
            try:
                #<input id="email" type="email" name="email_address" value="">
                email_element = self.chrome_browser.find_element_by_id('email')
                email_element.click()
                self.email = email
                email_element.send_keys(self.email)

                #<input id="password" type="password" name="password" value="">
                password_element = self.chrome_browser.find_element_by_id('password')
                password_element.click()
                self.password = password
                password_element.send_keys(self.password)

                password_element.send_keys(Keys.ENTER)
                b = False
            except Exception as e:
                pass

        b = True
        while b:
            pass
            try:
                #<div class="alert_inner fw_400">2160fba24a3961009eda1540e4fd9091</div>
                access_key = self.chrome_browser.find_element_by_xpath('//div[@class="alert_inner fw_400"]').text
                #<a class="small_and_fat blue_link no_deco" href="/usage"> &nbsp;API Usage</a>
                api_usage = self.chrome_browser.find_element_by_xpath('//a[@class="small_and_fat blue_link no_deco"]')
                api_usage.click()
                b = False
            except Exception as e:
                pass
        
        b = True
        while b:
            pass
            try:
                #<span class="updated_note update statistics">42 / 10,000</span>
                count = self.chrome_browser.find_element_by_xpath('//span[@class="updated_note update statistics"]').text
                b = False
            except Exception as e:
                pass
        
        self.chrome_browser.close()

        dict_modules = {'-h': '&hostname=1', '-tz': '&time_zone=1', '-c': '&currency=1', '-s': '&security=1', None: ''}
        if ip != None:
            self.ip_w1 = ip
        else:
            self.ip_w1 = self.external_ip
        self.hostname = hostname
        self.time_zone = time_zone
        self.currency = currency
        self.security = security

        url = f'http://api.ipstack.com/{self.ip_w1}?access_key={access_key}{dict_modules[self.hostname]}{dict_modules[self.time_zone]}{dict_modules[self.currency]}{dict_modules[self.security]}&format=1'
        dict_elements = urllib.request.urlopen(url).read().decode('utf8')

        return count, dict_elements
