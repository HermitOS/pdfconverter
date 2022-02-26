# https://docs.microsoft.com/en-us/office/vba/api/excel.workbook
# https://pbpython.com/windows-com.html
# https://docs.microsoft.com/en-us/office/vba/api/excel.pagesetup.fittopageswide
# https://www.geeksforgeeks.org/convert-excel-to-pdf-using-python/

from win32com import client
import sys
import os

def main():
    filename = sys.argv[1]
    outputpdfname = sys.argv[2]
    convert_excel(os.path.abspath(filename), os.path.abspath(outputpdfname))

def convert_excel(file_path: str, outputpdf_path: str):
    excel = client.Dispatch("Excel.Application")
    sheets = excel.Workbooks.Open(file_path)
    sheets.ActiveSheet.PageSetup.Orientation = 2
    sheets.ActiveSheet.PageSetup.Zoom = False
    sheets.ActiveSheet.PageSetup.FitToPagesWide = 1
    sheets.ActiveSheet.PageSetup.FitToPagesTall = 1

    worksheets = sheets.Worksheets[0]
    worksheets.ExportAsFixedFormat(0, outputpdf_path)
    excel.Application.Quit()


if __name__ == main:
    main()
