## Load data from PDF to string/dict/list will figure it out ##

import fitz

doc = fitz.open("data_loader/sample.pdf")
pages = doc.page_count

first_page = doc.load_page(0)
pages_text = []
for i in range(pages):
    page = doc.load_page(i)
    pages_text.append(page.get_text())  
print(pages_text)