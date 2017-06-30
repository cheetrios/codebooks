"""
__authors__     = Yash, Erica, Peter
__description__ = Given the subimage corresponding to the code, determine
what the text in the image is. This retains/modifies formatting to
ensure the code can be directly analyzed/executed downstream
__name__        = extract.py
"""

from PIL import Image
import pytesseract

import settings as s

def extract_text(img_fn):
    base_text = pytesseract.image_to_string(
        Image.open(img_fn), lang="eng")
    return base_text

if __name__ == "__main__":
    text = extract_text("{}/test.png".format(s.INPUT_DIR))
    print(text)