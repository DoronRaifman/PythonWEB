from PIL import Image
# Pillow tutorials:
# https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html

origImage = Image.open("DoronOrig.jpg")
grayscale = origImage.convert('L')
grayscale.show()
grayscale.save('DoronResult.jpg')

