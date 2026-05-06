from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


df = pd.read_excel(r"D:\DAU\ky_2_25_26\RPA\python\BTVN\data.xlsx", header=None)
df.columns = ["bienso"]

print("Khởi động Chrome...")
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://phatnguoi.com/"

for index, row in df.iterrows():
    bienso = str(row["bienso"]).strip()
    print("\nĐang kiểm tra: " + bienso)
    
    try:
        driver.get(url)
        time.sleep(3)
        
        element_option = driver.find_element(By.ID, "loaixe")
        element_option.click()
        element_select = driver.find_element(By.XPATH, "//option[text()='Ô tô']")
        element_select.click()
        
        element_bienso = driver.find_element(By.ID, "bsxinput")
        element_bienso.clear()
        element_bienso.send_keys(bienso)
        
        element_tracuu = driver.find_element(By.ID, "submit-btn")
        element_tracuu.click()
        
        time.sleep(5)
        
        page_text = driver.page_source
        
        if "chưa phát hiện lỗi vi phạm" in page_text:
            print("   Không vi phạm")
        else:
            print("   Có vi phạm")
            
            body_text = driver.find_element(By.TAG_NAME, "body").text
            
            chi_tiet = ""
            rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
            for row_element in rows:
                cols = row_element.find_elements(By.TAG_NAME, "td")
                if len(cols) >= 3:
                    chi_tiet = chi_tiet + "- Thời gian: " + cols[0].text + "\n"
                    chi_tiet = chi_tiet + "  Địa điểm: " + cols[1].text + "\n"
                    chi_tiet = chi_tiet + "  Lỗi: " + cols[2].text + "\n\n"
            
            if chi_tiet == "":
                chi_tiet = body_text[:500]
            
            print("\n   Chi tiết vi phạm:")
            print("   " + chi_tiet.replace("\n", "\n   "))
    
    except Exception as e:
        print("   Lỗi: " + str(e))

driver.quit()
print("\nHoàn thành")
