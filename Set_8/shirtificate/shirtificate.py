import sys
import requests
from PIL import Image
from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 40)
        text_width = self.get_string_width("CS50 Shirtificate")
        x = (self.w- text_width)/2
        self.text(x, 35, txt="CS50 Shirtificate")
        self.ln(20)


    def write_name_on_shirt(self, name, image):
        align = "C"
        self.image(image, align , y=60, w=self.epw)
        self.set_font('helvetica', "", size=25)
        self.set_text_color(255,255,255)
        text_width = self.get_string_width(f"{name} took CS50")
        x = (self.w - text_width)/2
        y = self.h/2
        self.text(x, y-20, txt=f"{name} took CS50")


def main ():
    name = get_name("What's your name? ")
    shirt_image = get_image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
    create_PDF_file(name, shirt_image)


def get_name(s):
    return input(s)


def get_image(link):
    try:
        image = Image.open(requests.get(link, stream=True).raw)
        return image
    except FileNotFoundError:
        sys.exit("Image not found")


def create_PDF_file(name, shirt_image):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_auto_page_break(True, margin=10)
    pdf.write_name_on_shirt(name, shirt_image)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()