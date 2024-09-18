from fpdf import FPDF
import PIL.Image as Image
import PIL
import sys

def main():
    if len(sys.argv) < 3:
        print('Usage:\n\nconvertimage inputfile outputfile\n\n\
where the inputfile is the name of the file you want to convert and has to be on one of the formats jpeg, jpg, png or gif, and the outputfile is the name of the pdf.')
        exit()

    filename = sys.argv[1]
    pdfname = sys.argv[2]
    convertimage(filename, pdfname)    

def convertimage(filename: str, pdfname: str):
    # open the image
    try:
        image = Image.open(filename)

    except FileNotFoundError:
        print('The file {} is not found in the folder'.format(filename))
        exit()
    
    except PIL.UnidentifiedImageError:
        print('The file {} is in the wrong format. It should be jpeg, jpg, png or gif.'.format(filename))

    except:
        print('Error {} occured when trying to open the image {}'.format(sys.exc_info()[0], filename))
        exit()

    # checks that the pdfname is in the right format
    if pdfname.endswith('.pdf') != True:
        print('The name for the pdf output has to be on the format x.pdf')

    # get the size of the image in px
    width, height = image.size

    # close the image
    image.close()

    # convert the size from px to mm
    relation_px_mm = 0.26
    mmWidth = width * relation_px_mm
    mmHeight = height * relation_px_mm
    relation = mmWidth / mmHeight

    # the size of a a4 pdf file, aka the max size for the image
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
    try:
        pdf.image(filename, w=mmWidth, h=mmHeight)
    except:
        print('Error {} occured when trying to open image {} with FPDF'.format({sys.exc_info()[0]}, filename))
        exit()
    
    try:
        pdf.output(pdfname)
    except:
        print('Error {} occured when trying to convert image to pdf {}'.format({sys.exc_info()[0]}, pdfname))
        exit()


if __name__ == '__main__':
    sys.exit(main())