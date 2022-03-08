from win32com import client

def convert_pdf(file_path: str):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(file_path)
    word.Documents(1).Activate
    word.ActiveDocument.ExportAsFixedFormat('C:/Users/Isabel/Documents/Hermit/FileToPDF/outputword.pdf', 17)
    word.Application.Quit()

convert_pdf('C:/Users/Isabel/Documents/Hermit/FileToPDF/hei.docx')