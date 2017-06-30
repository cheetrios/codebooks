"""
__authors__     = Yash, Erica, Peter
__description__ = Given the subimage corresponding to the code, determine
what the text in the image is. This retains/modifies formatting to
ensure the code can be directly analyzed/executed downstream
__name__        = extract.py
"""

from PIL import Image
import pytesseract