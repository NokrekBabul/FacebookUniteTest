import time
import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\theda\\PycharmProjects\\NewUniteTest\\drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_GoogleSearch_01(cls):
        cls.driver.get("https://google.com/")
        cls.driver.find_element_by_name("q").send_keys("Luie")
        cls.driver.find_element_by_name("btnK").click()
        time.sleep(5)
        x = cls.driver.title
        print(x)
        cls.assertEqual(x, "Lui - Google Search")

#Software Developer
#Javascript
#Bootstrap

    def test_GoogleSearch_02(cls):
        cls.driver.get("https://google.com/")
        cls.driver.find_element_by_name("q").send_keys("Luie")
        cls.driver.find_element_by_name("btnK").click()
        time.sleep(5)
        x = cls.driver.title
        print(x)
        cls.assertEqual(x, "Luie - Google Search")

    def test_GoogleSearch_03(cls):
        cls.driver.get("https://google.com/")
        cls.driver.find_element_by_name("q").send_keys("uie")
        cls.driver.find_element_by_name("btnK").click()
        time.sleep(5)
        x = cls.driver.title
        print(x)
        cls.assertEqual(x, "Lui - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print(" Test Successfully completed")

if __name__ == '__main__':
    unittest.main(verbosity=2)
