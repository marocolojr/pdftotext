import PyPDF2


with open('Documents\\PDF_PHyton\\DA.pdf', 'rb') as pdf_file:

    pdf_reader = PyPDF2.PdfReader(pdf_file)

   
    num_pages = len(pdf_reader.pages)


    text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        text += page_text

    print(text)
