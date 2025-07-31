from PIL import Image
from image_processing_pkg import grayscale, blur

def test_grayscale():
    img = Image.new('RGB', (100, 100), color='red')
    gray_img = grayscale(img)
    assert gray_img.mode == 'L'

def test_blur():
    img = Image.new('RGB', (100, 100), color='red')
    blurred_img = blur(img, radius=5)
    assert blurred_img is not None
