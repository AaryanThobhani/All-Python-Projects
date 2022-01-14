# Program for applying Box Blur to an image
# By Aaryan Thobhani
# GitHub:  https://github.com/AaryanThobhani

# Importing Libs
from PIL import ImageFilter, Image

# Variables
# Opening existing image
OriginalImg = Image.open()
OriginalImg.show()

# Applying Blur filter
blurredImage = OriginalImg.filter(ImageFilter.BoxBlur(30))
blurredImage.show()
