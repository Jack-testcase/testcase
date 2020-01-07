# -*- coding: utf-8 -*-
'''
作为页面类的基类，封装了其他的方法，其他页面必须为该类的子类
'''
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #模拟键盘
import os


class BasePage(object):
    """description of class"""

    # webdriver instance
    def __init__(self, browser='ff'):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)

        # 获取工程根目录路径
        self.file = os.getcwd()

    def findElement_1(self, element):
        '''
        Find element

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElement(element)
        参数：element，含有两个元素的列表，其原始数据封装在Model这个包里面
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def findElements(self, element):
        '''
        Find elements

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElements(element)
        作为多元素查找，同类型元素比较多的时候进行查找：比如下拉选择框中的ID基本都是一样的
        参数：element，作为一个列表输入，其原始数据封装在Model这个包里面
        '''

        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_elements_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_elements_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_elements_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_elements_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    '''
    判断该元素在当前dom中是否存在，如果存在则返回True，不存在返回False，
    '''

    def element_is_visible(self, element):
        try:
            self.findElement_1(element)
            flag = True
        except:
            flag = False
        return flag

    '''
    重写一个查询元素的操作,先查找该元素是否存在，如果不存在就报错
    '''

    def findElement(self, element):
        if self.element_is_visible(element=element):
            return self.findElement_1(element=element)
        else:
            print('该元素未找到，其{0}为{1}'.format(element[0], element[1]))

    '''
    
    '''

    def clear(self, element):
        self.findElement_1(element).clear()

    def open(self, url):
        '''
        Open web url

        Usage:
        self.open(url)
        参数：url，网址，一般为测试的网址
        '''
        if url != "":
            self.driver.get(url)
        else:
            raise ValueError("please provide a base url")

    def type(self, element, text):
        '''
        Operation input box.

        Usage:
        self.type(element,text)
        参数：element，表示已经定位到该元素;
        参数：text，需要输入的文字
        eg:
        username=self.findElement(username)   #先找到username元素的位置
        type_username=self.type(username,'123456')  #在username输入框中输入'123456'

        '''
        element.send_keys(text)

    def enter(self, element_name):
        '''
        Keyboard: hit return

        Usage:
        self.enter(element)
        参数：element，表示已经定位到该元素;
        '''
        element = self.findElement_1(element_name)
        element.send_keys(Keys.RETURN)

    def TAB(self, element_name):
        '''
        点击TAB按键
        :param element_name:
        :return:
        '''
        element = self.findElement_1(element_name)
        element.send_keys(Keys.TAB)

    def click(self, element):
        '''
        Click page element, like button, image, link, etc.
        参数：element，表示已经定位到该元素;
        '''
        element.click()

    def quit(self):
        '''
        Quit webdriver
        退出浏览器
        '''
        self.driver.quit()

    def close(self):
        '''
        Close webdriver
        关闭浏览器，但不退出driver
        '''
        self.driver.close()

    def getAttribute(self, element, attribute):
        '''
        Get element attribute
        参数：element：已经定位到的元素
        参数：attribute:元素的属性，dom里面该元素的属性，eg：<input id="productInfo.productCode" class="np " type="text" generatedby="1425347867641295" name="productInfo.productCode" title="00611" style="width: 300px;">
            那么元素属性就有：id,class,type,generatedby,name,title,stytle
        '''
        return element.get_attribute(attribute)

    def getText(self, element):
        '''
        Get text of a web element  ；text：表示在html中标签对之间的文本
        参数：element：已经定位到的元素
        '''
        return element.text

    def getTitle(self):
        '''
        Get window title
        获取当前网页的title
        '''
        return self.driver.title

    def getCurrentUrl(self):
        '''
        Get current url
        获取当前网页的url
        '''
        return self.driver.current_url

    def getScreenshot(self, targetpath):
        '''
        Get current screenshot and save it to target path
        截取当前页面的图片
        参数：targetpath：表示截图存放的路径，一般保存在专门的截图文件夹里面：D:\TestForTest\testforsmart\截图\图片名称
            targetpath:默认选择为：'D:\\TestForTest\\testforsmart\\截图\\*.png'
        '''
        self.driver.get_screenshot_as_file(targetpath)

    def maximizeWindow(self):
        '''
        Maximize current browser window
        把窗口最大化
        '''
        self.driver.maximize_window()

    def back(self):
        '''
        Goes one step backward in the browser history.
        浏览器后退
        '''
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        浏览器前进
        """
        self.driver.forward()

    def getWindowSize(self):
        """
        Gets the width and height of the current window.
        获取当前窗口大小
        """
        return self.driver.get_window_size()

    def refresh(self):
        '''
        Refresh current page
        '''
        self.driver.refresh()
        self.driver.switch_to()

    def switch_frame(self, frame_name):
        '''
        切换frame框架
        '''
        self.driver.switch_to.frame(frame_name)

    def switch_current_frame(self):
        self.driver.switch_to.default_content()

    def switch_parent_frame(self):
        '''
        回到上一个框架中
        '''
        self.driver.switch_to.parent_frame()

    # def move_to(self,element):
    #     '''
    #     鼠标悬停
    #     :param element:需要鼠标悬停的元素
    #     '''
    #     move_to = self.findElement(element)
    #     ActionChains(self).move_to_element(move_to).perform()

    def get_page_source(self):
        return self.driver.page_source

    def excute_script(self, js2):
        return self.driver.execute_script(js2)

    '''
    获取当前窗口的句柄，用来切换窗口
    '''

    def get_window(self):
        return self.driver.current_window_handle

    '''
    进入某个句柄的窗口
    '''

    def go_to_windows(self, window):
        self.driver.switch_to.window(window)

    '''
    截图功能
    '''

    def get_windows_img(self):
        self.logger = logging.getLogger(__name__)
        file_path = 'E:\\auto_test\\Reports\\img'  # 图片地址
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + '\\' + rq + '.png'
        print("%s picture_end" % screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            # self.logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            # self.logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()


if __name__ == '__main__':
    a = BasePage()
    print(a.file)
