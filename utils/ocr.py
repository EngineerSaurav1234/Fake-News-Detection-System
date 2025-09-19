from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ASUS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text
