from fpdf import FPDF
import PIL.Image as image

image = image.open('DSC00470.jpg')
width, height = image.size
print(width, height)
pxWidth = width * 0.26
pxHeight = height * 0.26
relation = pxWidth / pxHeight

margins = 48
max_pxWidth = 216 - margins
max_pxHeight = 279 - margins


if pxWidth > max_pxWidth:
    print('w')
    pxWidth = max_pxWidth
    pxHeight = pxWidth / relation

if pxHeight > max_pxHeight:
    print('h')
    pxHeight = max_pxHeigh
    pxWidth = pxHeight * relation

pdf = FPDF()
pdf.add_page()
pdf.image('DSC00470.jpg', w=pxWidth, h=pxHeight)
pdf.output('image.pdf')

