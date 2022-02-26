from gettext import install
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfconverter", 
    version="0.9.1",
    author="Isabel Sandstrøm",
    author_email="isabel@hermit.no",
    description="Python command line program for converting different files to pdfs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['pdfconverter'],
    install_requires=['fpdf>=1.7.2'],
    entry_points={'console_scripts': ['convertimage = pdfconverter.convertimage:main'], 'console_scripts': ['convertexcel = pdfconverter.convertexcel:main'], 'console_scripts': ['convertword = pdfconverter.convertword:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)                                
