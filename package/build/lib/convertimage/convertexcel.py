# https://docs.microsoft.com/en-us/office/vba/api/excel.workbook
# https://pbpython.com/windows-com.html
# https://docs.microsoft.com/en-us/office/vba/api/excel.pagesetup.fittopageswide
# https://www.geeksforgeeks.org/convert-excel-to-pdf-using-python/

from win32com import client
import sys
import os

excel_formats = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xml', '.xlam', '.xla', '.xlw', '.xlr']

def main():
    if len(sys.argv) < 3:
        print('Usage:\n\nconvertexcel inputfile outputfile\n\n\
where the inputfile is the name of the file you want to convert and has to be one of the formats .xlsx, .xlsm, .xlsb, .xltx, .xltm, .xls, .xlt, .xml, .xlam, .xla, .xlw or .xlr, and the outputfile is the name of the pdf.')
        exit()

    filename = sys.argv[1]
    outputpdfname = sys.argv[2]

    # checks that the filename is in one of the accepted formats 
    boolean = False
    for string in excel_formats:
        if filename.endswith(string):
            boolean = True
            break

    if boolean == False:
        print('The file you are trying to convert is not in the rigth format. The acceptable formats is : {}'.format(excel_formats))
        exit()

    # checks if the output name is in the right format
    if outputpdfname.endswith('.pdf') == False:
        print('The name for the output pdf is not in the right format x.pdf')
        exit()

    convert_excel(os.path.abspath(filename), os.path.abspath(outputpdfname))

def convert_excel(file_path: str, outputpdf_path: str):  
    excel = client.Dispatch("Excel.Application")

    # opens the file
    try:
        sheets = excel.Workbooks.Open(file_path)
    except:
        print('Error {} occured when trying to open the file {}. Please check that the file exist in this folder'.format({sys.exc_info()[0]}, os.path.relpath(file_path)))
        excel.Application.Quit()
        exit()

    # set the formatations for the excel file
    ## sets landscape orientation
    sheets.ActiveSheet.PageSetup.Orientation = 2
    ## makes the excel sheet fit on one pdf sheet       
    sheets.ActiveSheet.PageSetup.Zoom = False
    sheets.ActiveSheet.PageSetup.FitToPagesWide = 1
    sheets.ActiveSheet.PageSetup.FitToPagesTall = 1

    worksheets = sheets.Worksheets[0]

    # export the excel sheet to a pdf
    try:
        worksheets.ExportAsFixedFormat(0, outputpdf_path)
    except:
        print('Error {} occured when trying to convert the file {} to pdf'.format({sys.exc_info()[0]}, os.path.relpath(file_path)))
        excel.Application.Quit()    
        exit()

    excel.Application.Quit()


if __name__ == '__main__':
    sys.exit(main())
