from win32com import client
import sys
import os

word_formats = ['.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx', '.odt', '.rtf', '.txt', '.wps', '.xml', '.xps']

def main():
    if len(sys.argv) < 3:
        print('Usage:\n\nconvertword inputfile outputfile\n\n\
where the inputfile is the name of the file you want to convert and has to be one of the formats .doc, .docm, .docx, .dot, .dotm, .dotx, .odt, .rtf, .txt, .wps, .xml or .xps, and the outputfile is the name of the pdf.')
        exit()

    filename = sys.argv[1]
    outputpdfname = sys.argv[2]

    # checks that the filename is in one of the acceptable formats
    boolean = False
    for string in word_formats:
        if filename.endswith(string):
            boolean = True
            break

    if boolean == False:
        print('The file you are trying to convert is not in the rigth format. The acceptable formats is : {}'.format(word_formats))
        exit()

    # checks that the pdf name is on the right format
    if outputpdfname.endswith('.pdf') == False:
        print('The name for the output pdf is not in the right format x.pdf')
        exit()

    convert_word(os.path.abspath(filename), os.path.abspath(outputpdfname))


def convert_word(file_path: str, outputpdf_path: str):
    word = client.Dispatch("Word.Application")
    # opens the word document
    try:
        word.Documents.Open(file_path)
    except:
        print('Error {} occured when trying to open the file {}. Please check that the file exist in this folder'.format({sys.exc_info()[0]}, os.path.relpath(file_path)))
        exit()

    word.Documents(1).Activate

    # exports the word documet to pdf
    try:
        word.ActiveDocument.ExportAsFixedFormat(outputpdf_path, 17)
    except:
        print('Error {} occured when trying to convert the file {} to pdf'.format({sys.exc_info()[0]}, os.path.relpath(file_path)))
        exit()
    
    word.Application.Quit()


if __name__ == '__main__':
    sys.exit(main())