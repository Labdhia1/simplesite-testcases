import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

class assignmentTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://mystifying-beaver-ee03b5.netlify.app/")
        self.driver.implicitly_wait(10)
        print("Title of page is:"+ self.driver.title)
        
    def tearDown(self):
        self.driver.close()

    def test_sort_on_complexity(self):
        complexity_map = {"low" : 0, "medium" : 1, "high" : 2}
        ele = self.driver.find_element_by_id("sort-select")
        drp = Select(ele)
        drp.select_by_value("complexity")
        time.sleep(5)
        elements = self.driver.find_elements_by_css_selector(".table-data.data-complexity")
        contents = []
        sorted_content = []
        for element in elements:
            #print(element.text)
            contents.append(complexity_map[element.text])
            sorted_content.append(complexity_map[element.text])
        
        contents.sort()
        self.assertEqual(contents, sorted_content)

    def test_sort_on_avg_impact(self):
        ele = self.driver.find_element_by_id("sort-select")
        drp = Select(ele)
        drp.select_by_value("averageImpact")   
        time.sleep(5)
        elements = self.driver.find_elements_by_css_selector(".table-data.data-averageImpact")
        avg_impact = []
        avg_sorted_impact = []
        for element in elements:
            #print(element.text)
            avg_impact.append(float(element.text))
            avg_sorted_impact.append(float(element.text))
        
        avg_impact.sort()
        self.assertEqual(avg_impact, avg_sorted_impact)

    def test_filter_by_capitalText(self):
        elements = self.driver.find_elements_by_css_selector("div.table-data.data-name")
        before_filter = []
        for element in elements:
            before_filter.append(element.text)
        filter_text = before_filter[0].upper()    
        filter_input = self.driver.find_element_by_id("filter-input")
        filter_input.clear()
        filter_input.send_keys(filter_text)
        time.sleep(10)
        elements = self.driver.find_elements_by_css_selector("div.table-data.data-name")
        after_filter_data = []
        for element in elements:
            after_filter_data.append(element.text)
        #print(before_filter, after_filter_data)    
        self.assertEqual(before_filter, after_filter_data)  

    def test_filter_by_smallText(self):
        elements = self.driver.find_elements_by_css_selector("div.table-data.data-name")
        before_filter = []
        for element in elements:
            before_filter.append(element.text)
        filter_text = before_filter[0].lower()    
        filter_input = self.driver.find_element_by_id("filter-input")
        filter_input.clear()
        filter_input.send_keys(filter_text)
        time.sleep(10)
        elements = self.driver.find_elements_by_css_selector("div.table-data.data-name")
        after_filter_data = []
        for element in elements:
            after_filter_data.append(element.text)
        self.assertNotEqual(before_filter, after_filter_data)      

    




if __name__ == '__main__':
    unittest.main()