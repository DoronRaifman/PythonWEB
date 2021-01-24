from PIL import Image, ImageFilter
# Pillow tutorials:
# https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html

orig_image = Image.open("DoronOrig.jpg")
grayscale = orig_image.convert('L')
# grayscale.show()
grayscale.save('DoronGray.jpg')
blur_image = orig_image.filter(ImageFilter.GaussianBlur)
blur_image.save('DoronBlur.jpg')
contour_image = orig_image.filter(ImageFilter.CONTOUR)
contour_image.save('DoronContour.jpg')
