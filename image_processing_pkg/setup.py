from setuptools import setup, find_packages

setup(
    name='image_processing_pkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    author='Seu Nome',
    description='Pacote simples para processamento de imagens',
    url='https://github.com/seu_usuario/image_processing_pkg',
    python_requires='>=3.7',
)
