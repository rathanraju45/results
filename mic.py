from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
driver = webdriver.Chrome("rajuenv/chromedriver")
driver.get("http://exams.mictech.ac.in/StdDashBoard.aspx")
lst=[]
stname=[]
sgpa1=[]
sgpa2=[]
cgpa1=[]
cgpa2=[]
credits1=[]
credits2=[]
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
    sname = driver.find_element(By.XPATH, '//*[@id="cBody_lblSname"]')
    stname.append(sname.text)
    sgpa = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_0")
    cgpa = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCGPA_0")
    credits = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCR_0")
    sgpa1.append(sgpa.text)
    cgpa1.append(cgpa.text)
    credits1.append(credits.text)
    sgpa_2 = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_1")
    cgpa_2 = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCGPA_1")
    credits_2 = driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCR_1")
    sgpa2.append(sgpa_2.text)
    cgpa2.append(cgpa_2.text)
    credits2.append(credits_2.text)
    driver.back()
dataset=pd.DataFrame()
dataset['name']=stname
dataset['sem-1 sgpa']=sgpa1
dataset['sem-1 cgpa']=cgpa1
dataset['sem-1 credits']=credits1
dataset['sem-2 sgpa']=sgpa2
dataset['sem-2 cgpa']=cgpa2
dataset['sem-2 credits']=credits2
dataset.to_excel("result.xlsx")