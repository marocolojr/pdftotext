import PyPDF2


with open('C:\\Users\\maroc\\Documentos\\CODE\\pdftotext\\DA.pdf', 'rb') as pdf_file:


    pdf_reader = PyPDF2.PdfReader(pdf_file)

   
    num_pages = len(pdf_reader.pages)


    text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        text += page_text

    # show text
    print(text)
