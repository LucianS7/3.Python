import sys
import requests
from PIL import Image
from fpdf import FPDF

# Defining a new PDF class witch inherits from FPDF:
class PDF(FPDF):
    def header(self):
        # Setting font: helvetica Bold 50
        self.set_font("helvetica", "B", 40)
        # Get text width:
        text_width = self.get_string_width("CS50 Shirtificate")
        # Centering the text:
        x = (self.w- text_width)/2
        # Printing title:
        self.text(x, 35, txt="CS50 Shirtificate")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: courier italic 10
        self.set_font("helvetica", "I", 10)
        # Setting the text color:
        self.set_text_color(0,0,0)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def write_name_on_shirt(self, name, image):
        # Centering the image horizontally - x axis:
        align = "C"
        # Printing the image:
        self.image(image, align , y=60, w=self.epw, link='https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png', keep_aspect_ratio=False)
        # Setting the text color:
        self.set_font('helvetica', "", size=25)
        # Setting the text color to white:
        self.set_text_color(255,255,255)
        # Getting the text to be printed width:
        text_width = self.get_string_width(f"{name} took CS50")
        # Centering the text horizontally - x axis:
        x = (self.w - text_width)/2
        # Centering the text vertically - y axis:
        y = self.h/2
        self.text(x, y-20, txt=f"{name} took CS50")


# Main function:
def main ():
    name = get_name("What's your name? ")
    shirt_image = get_image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
    create_PDF_file(name, shirt_image)

# Get name function:
def get_name(s):
    return input(s)

#Gget image function:
def get_image(link):
    try:
        image = Image.open(requests.get(link, stream=True).raw)
        return image
    except FileNotFoundError:
        sys.exit("Image not found")

#Creating the pdf file function:
def create_PDF_file(name, shirt_image):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(True, margin=10)
    pdf.write_name_on_shirt(name, shirt_image)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()