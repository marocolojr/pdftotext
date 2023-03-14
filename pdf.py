import PyPDF2

# abrir o arquivo pdf em modo de leitura binária
with open('Documents\\PDF_PHyton\\DA.pdf', 'rb') as pdf_file:
    # criar um objeto de leitura de PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # obter o número de páginas no PDF
    num_pages = len(pdf_reader.pages)

    # iterar sobre cada página e extrair o texto
    text = ''
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        text += page_text

    # exibir o texto extraído
    print(text)
