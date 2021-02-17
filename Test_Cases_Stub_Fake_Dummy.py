#import Modal as dbHandler
import unittest
from Modal import Login

class Test_Login_App(unittest.TestCase):       

    def test_check_login_fake_pass(self):
        result=Login.check_login(self,"Prakash","Prakash123")
        self.assertEqual("Login Successful",result)

    def test_check_login_fake_fail(self):
        result=Login.check_login(self,"Prakashsh","Prakash123")
        self.assertEqual("Login Failed",result)

if __name__ == '__main__':
    unittest.main()