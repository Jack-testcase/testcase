from testframe.Page.BasePage import BasePage
from testframe.Modle.Login import Target as t
class LoginPage(BasePage):
    def __init__(self, browser='chrome'):
        super().__init__(browser)
        
    def login(self,username='null',password='null'):
        self.open('http://www.baidu.com')
        self.maximizeWindow()
        self.findElement(t.input_usename).send_keys(username)
        self.findElement(t.input_password).send_keys(password)
        self.findElement(t.btn_login).click()


