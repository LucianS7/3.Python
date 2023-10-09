import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if html := re.search(r"src=\"https?://(?:www\.)?youtube.com/embed/(.+)\"", s):
        url = "https://youtu.be/" + html.group(1)
        return url
    else:
        return None


if __name__ == "__main__":
    main()
    