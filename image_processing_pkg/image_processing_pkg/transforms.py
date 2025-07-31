from PIL import Image

def resize(image: Image.Image, width: int, height: int) -> Image.Image:
    """Redimensiona a imagem para a largura e altura dadas."""
    return image.resize((width, height))

def rotate(image: Image.Image, degrees: float) -> Image.Image:
    """Roda a imagem pelo ângulo especificado (graus)."""
    return image.rotate(degrees, expand=True)
