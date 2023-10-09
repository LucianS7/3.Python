import sys
import requests
from PIL import Image
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica" , "B", 40)
        self.set_text_color(0, 0, 0)
        header_text = "CS50 Shirtificate"
        text_width = self.get_string_width(header_text)
        x = (self.w - text_width)/2
        self.text(x, 35,  txt=header_text)
        self.ln(20)

    def footer(self):
        self.set_font("times" , "I", 10)
        self.set_text_color(0, 0, 0)
        self.set_y(-15)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align = "C")

    def write_text_on_image(self, txt, image):
        self.set_font("helvetica", "", 25)
        self.set_text_color(255, 255, 255)
        align = "C"
        self.image(image, align, y=60, w=self.epw, link="https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", keep_aspect_ratio = False)
        text_width = self.get_string_width(f"{txt} took CS50")
        x = (self.w - text_width)/2
        y = self.h/2 - 20
        self.text(x, y, txt=f"{txt} took CS50")

def main():
    name = get_name("What's your name? ")
    image = get_image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png")
    create_PDF_file(name, image)

def get_name(s):
    return input(s)


def get_image(link):
    try:
        image = Image.open(requests.get(link, stream=True).raw)
        return image
    except FileNotFoundError:
        sys.exit("File not found")


def create_PDF_file(name, image):
    pdf_file = PDF()
    pdf_file.add_page()
    pdf_file.set_auto_page_break(True, margin=10)
    pdf_file.write_text_on_image(name, image)
    pdf_file.output("shirtificate_test.pdf")
    print("Done")


if __name__ == "__main__":
    main()