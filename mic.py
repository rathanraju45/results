from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pandas as pd
options = webdriver.ChromeOptions()
options.add_argument('--headless'),options.add_argument('--disable-gpu')
driver = webdriver.Chrome("rajuenv/chromedriver",options=options)
driver.get("http://exams.mictech.ac.in/StdDashBoard.aspx")
rolls=["21H71A0502","21H71A0503","21H71A0504","21H71A0505","21H71A0506","21H71A0507","21H71A0508","21H71A0509","21H71A0510","21H71A0511","21H71A0512","21H71A0513","21H71A0514","21H71A0515","21H71A0517","21H71A0518","21H71A0519","21H71A0520","21H71A0521","21H71A0522","21H71A0523","21H71A0524","21H71A0525","21H71A0526","21H71A0527","21H71A0528","21H71A0529","21H71A0530","21H71A0531","21H71A0532","21H71A0533","21H71A0534","21H71A0535","21H71A0536","21H71A0538","21H71A0539","21H71A0540","21H71A0541","21H71A0542","21H71A0543","21H71A0544","21H71A0545","21H71A0546","21H71A0547","21H71A0548","21H71A0549","21H71A0550","21H71A0551","21H71A0552","21H71A0553","21H71A0554","21H71A0555","21H71A0556","21H71A0557","21H71A0558","21H71A0559","21H71A0560","21H71A0561","21H71A0562","21H71A0563","21H71A0564","21H71A0565","21H71A0566",]
stname,sgpa1,sgpa2,sgpa3,cgpa=[],[],[],[],[]
for i in rolls:
    usr,pwd= driver.find_element(By.ID, "ContentPlaceHolder1_txtUsername"),driver.find_element(By.ID, "ContentPlaceHolder1_txtPassword")
    usr.clear(),usr.send_keys(i),pwd.send_keys(i),pwd.send_keys(Keys.RETURN)
    sname,sgpa_1,sgpa_2,sgpa_3,cgpa1= driver.find_element(By.XPATH, '//*[@id="cBody_lblSname"]'),driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_0"),driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_1"),driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblSgap_2"),driver.find_element(By.ID, "cBody_gvSGPA_CGPA_lblCGPA_2")
    stname.append(sname.text),sgpa1.append(sgpa_1.text),sgpa2.append(sgpa_2.text),sgpa3.append(sgpa_3.text),cgpa.append(cgpa1.text)
    driver.back()
driver.close()
dataset=pd.DataFrame()
dataset['Name'],dataset['Regd.No'],dataset['s1-gpa'],dataset['s2-gpa'],dataset['s3-gpa'],dataset['cgpa']=stname,rolls,sgpa1,sgpa2,sgpa3,cgpa
dataset.to_excel("result.xlsx")
