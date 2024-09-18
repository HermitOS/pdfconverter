from importlib.metadata import entry_points
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfconverter", 
    version="1.0.1",
    author="Isabel Sandstrøm",
    author_email="isabel@hermit.no",
    description="Python command line program for converting different files to pdfs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HermitOS/pdfconverter/tree/main/package",
    packages=['pdfconverter'],
    install_requires=['fpdf>=1.7.2', 'pywin32>=303', 'pywin32-ctypes>=0.2.0', 'Pillow>=8.4.0'],
    entry_points={
        'console_scripts': [
            'convertimage = pdfconverter.convertimage:main', 
            'convertexcel = pdfconverter.convertexcel:main',
            'convertword = pdfconverter.convertword:main',
            'pdfconverter = pdfconverter.pdfconverter:main'
            ]        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)                                
