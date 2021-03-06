# pdfconverter

Python command line program for converting different files to pdf. You can convert word documents, excel documents and images with the three different commands `convertword`, `convertexcel` and `convertimage`.

## `convertword`
### Usage:
```
convertword inputfile outputfile
```
where the inputfile is the name of the file you want to convert and has to be one of the formats `.doc`, `.docm`, `.docx`, `.dot`, `.dotm`, `.dotx`, `.odt`, `.rtf`, `.txt`, `.wps`, `.xml` or `.xps`, and the outputfile is the name of the pdf.

### Example:
```
convertword document.doc outputfile.pdf
```

## `convertexcel`
### Usage:
```
convertexcel inputfile outputfile
```
where the inputfile is the name of the file you want to convert and has to be one of the formats `.xlsx`, `.xlsm`, `.xlsb`, `.xltx`, `.xltm`, `.xls`, `.xlt`, `.xml`, `.xlam`, `.xla`, `.xlw` or `.xlr`, and the outputfile is the name of the pdf.

### Example:
```
convertexcel document.xlsx outputfile.pdf
```

## `convertimage`
### Usage:
```
convertimage inputfile outputfile
```
where the inputfile is the name of the file you want to convert and has to be one of the formats `jpeg`, `jpg`, `png` or `gif`, and the outputfile is the name of the pdf.

### Example:
```
convertimage image.jpg outputfile.pdf
```