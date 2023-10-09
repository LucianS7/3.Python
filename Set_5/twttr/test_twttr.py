from twttr import shorten

def test_shorten_upper_lower_case():
    assert shorten("testing my twitter") == "tstng my twttr"
    assert shorten("TESTING MY TWITTER") == "TSTNG MY TWTTR"
    assert shorten("TEsTing My TwItteR") == "TsTng My TwttR"

def test_shorten_numbers():
    assert shorten("12345678910") == "12345678910"

def test_shorten_punctuation():
    assert shorten(".,!?;") == ".,!?;"