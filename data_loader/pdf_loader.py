## Load data from PDF to string/dict/list will figure it out ##

import fitz

def load_pdf_to_string('\Users\conorschweppe\Desktop\Downloaded_Notes\Calculus_Notes\23MS244R.pdf'):
open(pdf_path, 'rb') as file:
    pdf_document = fitz.open(file)
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text += page.get_text()
    return text