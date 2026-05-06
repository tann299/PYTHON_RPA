from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://phatnguoi.com/"

bienso = "51F-777.77"
print("\nĐang kiểm tra: " + bienso)

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

if "Không tìm thấy vi phạm" in page_text:
    print("   Không vi phạm")
else:
    print("   Có vi phạm")
    
    chi_tiet = ""
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    print("   Số dòng tìm thấy: " + str(len(rows)))
    
    for row_element in rows:
        cols = row_element.find_elements(By.TAG_NAME, "td")
        print("   Số cột: " + str(len(cols)))
        if len(cols) >= 3:
            chi_tiet = chi_tiet + "- Thời gian: " + cols[0].text + "\n"
            chi_tiet = chi_tiet + "  Địa điểm: " + cols[1].text + "\n"
            chi_tiet = chi_tiet + "  Lỗi: " + cols[2].text + "\n\n"
    
    if chi_tiet == "":
        chi_tiet = "(Không lấy được chi tiết)"
    
    print("\nChi tiết vi phạm:")
    print(chi_tiet)

input("\nNhấn Enter để đóng trình duyệt...")
driver.quit()
print("\nHoàn thành")
