from PIL import Image, ImageFilter

image = Image.open("./Pokedex/pikachu.jpg")
filter_image = image.filter(ImageFilter.BLUR)
filter_image.save("blur.png", "png")
