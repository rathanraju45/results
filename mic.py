from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://exams.mictech.ac.in/StdDashBoard.aspx")
sgpa = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_0")
cgpa = driver.find_elements(By.Id, "cBody_gvSGPA_CGPA_lblCGPA_0")
print(sgpa.text)
for i in cgpa:
    print(i.text,end="")




