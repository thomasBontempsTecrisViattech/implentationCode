from pdf2image import convert_from_path
import pytesseract
from PIL import Image
from implentationCode.variable import TESSERACT_CMD, FOLDER_IMAGE

# Get tesseract executeur
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

# 1. Convert PDF file into images via pypdfium2
def convert_pdf_to_images(file_path, scale=300/72):
    images = convert_from_path(file_path)
    for cpt, imgPdf in enumerate(images):
        imgPdf.save(FOLDER_IMAGE + '/' + str(cpt) +'.jpg', 'JPEG')
    return range(0,cpt+1)

# 2. Extract text from images via pytesseract
def extract_text_from_img(nb_img):
    text = ""
    for i in nb_img:
        image = Image.open(FOLDER_IMAGE + '/' + str(i) +'.jpg')
        text += pytesseract.image_to_string(image, lang='fra') + '\n'
        
    return text


# 3. Extract text from pdf
def extract_content_from_pdf(file_path: str):
    nb_img = convert_pdf_to_images(file_path)
    return extract_text_from_img(nb_img)
    
