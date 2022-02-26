from lib2to3.pytree import convert
from fpdf import FPDF
import PIL.Image as Image
import sys

def main():
    filename = sys.argv[1]
    pdfname = sys.argv[2]
    convertimage(filename, pdfname)    

def convertimage(filename: str, pdfname: str):
    # get the size of the picture, in px
    image = Image.open(filename)
    width, height = image.size

    # change the size from px to mm
    relation_px_mm = 0.26
    mmWidth = width * relation_px_mm
    mmHeight = height * relation_px_mm
    relation = mmWidth / mmHeight

    # the size of a a4 pdf file
    margins = 48
    max_mmWidth = 216 - margins     
    max_mmHeight = 279 - margins

    # changes the size of the image if it is bigger than the pdf, while keeping the realtion of the picture
    if mmWidth > max_mmWidth:
        mmWidth = max_mmWidth
        mmHeight = mmWidth / relation

    if mmHeight > max_mmHeight:
        mmHeight = max_mmHeight
        mmWidth = mmHeight * relation

    # convert the image to a pdf with the sizes we found in mm
    pdf = FPDF()
    pdf.add_page()
    pdf.image(filename, w=mmWidth, h=mmHeight)
    pdf.output(pdfname)


if __name__ == main:
    main()