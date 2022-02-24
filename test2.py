from win32com import client

def convert_excel(file_path: str):
    excel = client.Dispatch("Excel.Application")
    sheets = excel.Workbooks.Open(file_path)
    sheets.ActiveSheet.PageSetup.Orientation = 2
    sheets.ActiveSheet.PageSetup.Zoom = False
    sheets.ActiveSheet.PageSetup.FitToPagesWide = 1
    sheets.ActiveSheet.PageSetup.FitToPagesTall = 1

    worksheets = sheets.Worksheets[0]
    worksheets.ExportAsFixedFormat(0, 'C:/Users/Isabel/Documents/Hermit/FileToPDF/output.pdf')
    excel.Application.Quit()


convert_excel('C:/Users/Isabel/Documents/Hermit/FileToPDF/testfil2.xlsx')