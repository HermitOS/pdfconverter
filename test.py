from fpdf import FPDF
import PIL.Image as image

image = image.open('DSC00470.jpg')
width, height = image.size
relation_px_mm = 0.26
mmWidth = width * relation_px_mm
mmHeight = height * relation_px_mm
relation = mmWidth / mmHeight

margins = 48
max_mmWidth = 216 - margins
max_mmHeight = 279 - margins

if mmWidth > max_mmWidth:
    mmWidth = max_mmWidth
    mmHeight = mmWidth / relation

if mmHeight > max_mmHeight:
    mmHeight = max_mmHeight
    mmWidth = mmHeight * relation

pdf = FPDF()
pdf.add_page()
pdf.image('DSC00470.jpg', w=mmWidth, h=mmHeight)
pdf.output('image.pdf')

