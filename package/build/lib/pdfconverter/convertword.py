from win32com import client
import sys
import os

def main():
    filename = sys.argv[1]
    outputpdfname = sys.argv[2]
    convert_word(os.path.abspath(filename), os.path.abspath(outputpdfname))

def convert_word(file_path: str, outputpdf_path: str):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(file_path)
    word.Documents(1).Activate
    word.ActiveDocument.ExportAsFixedFormat('C:/Users/Isabel/Documents/Hermit/FileToPDF/outputword.pdf', 17)
    word.Application.Quit()


if __name__ == main:
    main()