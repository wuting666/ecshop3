# import time
#
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# def open_browser(browser="chrome"):
#     if browser=="chrome":
#         driver=webdriver.Chrome()
#     elif browser=="firefox":
#         driver=webdriver.Firefox()
#     elif browser=="ie":
#         driver=webdriver.Ie()
#     else:
#         driver=None
#         print("请输入正确的浏览器")
#     return driver
# class Base():
#     def __init__(self,driver):
#         self.driver=driver
#     #打开网址
#     def open_url(self,url):
#         self.driver.get(url)
#         self.driver.maximize_window()
#     def find_element(self,locator,timeout=10):
#         #定位单个元素
#         element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
#         return element
#     def find_elements(self, locator, timeout=10):
#         element = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
#         return element
#     def click(self,locator,timeout=10):
#         #输入
#         element=self.find_element(locator=locator,timeout=timeout)
#         element.click()
#     def send_keys(self,locator,text,timeout=10):
#         #输入数据
#         element=self.find_element(locator=locator,timeout=timeout)
#         element.send_keys(text)
#     def is_text_in_element(self,text,locator,timeout=10):
#         #查看文本是否在元素中
#         try:
#             result=WebDriverWait(self.driver,timeout=timeout).until(EC.text_to_be_present_in_element(locator,text))
#             return result
#         except:
#             return False
#     def is_value_in_element(self,locator,test,timeout=10):
#         try:
#             result=WebDriverWait(self.driver,timeout=timeout).until(EC.text_to_be_present_in_element_value(locator,test))
#             return result
#         except:
#             return False
#     def close_browser(self):
#         self.driver.quit()
#
# if __name__ == '__main__':
#     #打开浏览器
#     driver=open_browser()
#     #打开网址
#     base=Base(driver)
#     url="http://www.baidu.com/"
#     base.open_url(url)
#     #定位百度输入框
#     locator_input=("id","kw")
#     #输入数据
#
#     base.send_keys(locator=locator_input,text='python')
#     #定位点击按钮
#     locator_button=("id","su")
#     base.click(locator_button)
#     time.sleep(5)
#     #关浏览器
#     base.close_browser()
#
#
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#打开浏览器
def open_browser(browser='chrome'):
     if browser=="chrome":
        driver=webdriver.Chrome()
     elif browser=="firefox":
         driver=webdriver.Firefox()
     elif browser=="ie":
         driver=webdriver.Ie()
     else:
         driver=None
         print("请输入正确的浏览器")
     return driver
class Base():
    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
        #浏览器窗口最大化
        self.driver.maximize_window()
    def find_element(self,locator,timeout=10):
        #定位单个元素
        elemnet=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return elemnet
    def find_elemnets(self,driver,timeout=10):
        #定位多个元素
        element=WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(driver))
        return element
    def send_keys(self,locator,text,timeout=10):
        element=self.find_element(locator,timeout)
        element.clear()
        element.send_keys(text)

    def click(self,locator,timeout=10):
        #点击操作
        element=self.find_element(locator,timeout) #定位元素
        element.click() #点击
    def is_text_in_element(self,locator,text,timeout=10):
        #判断文本是否在元素中
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False
    def is_value_in_element(self,locator,text,timeout=10):
        #判断属性值是否在元素中
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,text))
            return result
        except:
            return False
    def close_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    #打开浏览器
    driver=open_browser()
    #实例化类
    base=Base(driver)
    #打开百度网址
    url="http://www.baidu.com"
    base.open_url(url)
    #定位百度输入框,在输入python
    locator_input=("id","kw")
    base.send_keys(locator_input,text='python')
    time.sleep(3)
    #点击百度一下
    locator_button=("id","su")
    base.click(locator_button)
    #关闭浏览器
    base.close_browser()