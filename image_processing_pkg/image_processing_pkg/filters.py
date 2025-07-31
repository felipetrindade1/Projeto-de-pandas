from PIL import Image, ImageFilter

def grayscale(image: Image.Image) -> Image.Image:
    """Converte a imagem para tons de cinza."""
    return image.convert('L')

def blur(image: Image.Image, radius: int = 2) -> Image.Image:
    """Aplica desfoque gaussian blur na imagem."""
    return image.filter(ImageFilter.GaussianBlur(radius))
