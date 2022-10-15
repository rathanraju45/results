from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome("rajuenv/chromedriver")
driver.get("http://exams.mictech.ac.in/StdDashBoard.aspx")
lst=[]
stname=[]
sgpa1=[]
cgpa1=[]
credits1=[]
for i in range(1,67):
    if (i == 16):
        continue
    if (i < 10):
        i = "0"+str(i)
    lst.append(i)
for j in range(0, len(lst)):
    driver.refresh()
    usr = driver.find_element(By.ID, "ContentPlaceHolder1_txtUsername")
    pwd = driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword")
    usr.send_keys("21H71A05{}".format(lst[j]))
    pwd.send_keys("21H71A05{}".format(lst[j]))
    pwd.send_keys(Keys.RETURN)
    stname.append("21H71A05{}".format(lst[j]))
    sgpa = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_0")
    cgpa = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCGPA_0")
    credits = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCR_0")
    sgpa1.append(sgpa.text)
    cgpa1.append(cgpa.text)
    credits1.append(credits.text)
    driver.back()
dataset=pd.DataFrame()
dataset['name']=stname
dataset['sgpa']=sgpa1
dataset['cgpa']=cgpa1
dataset['credits']=credits
dataset.to_excel("result.xlsx")