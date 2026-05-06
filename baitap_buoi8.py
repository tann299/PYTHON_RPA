from bs4 import BeautifulSoup
import requests
import pandas

dict = []

for page in range(1,6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_book = soup.find_all("article", class_="product_pod")

    for i_book in product_book:
        name = i_book.h3.a["title"]
        # print(name)
        price = i_book.find("p","price_color").text
        # print(price)
        rating = i_book.find("p", "star-rating")["class"][1]
        # print(rating)
        stock = str(i_book.find("p","instock availability").text).replace("\n","").strip()
        # print(stock)

        data = {
            "Name":name,
            "Price":price,
            "Rating":rating,
            "Stock":stock
        }
        dict.append(data)
df = pandas.DataFrame(dict)
print(df)

file_name = "Du_Lieu_Sach.xlsx"
ten_sheet = "Danh sách Sách"

df.to_excel(file_name, sheet_name=ten_sheet, index=False)
