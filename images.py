from PIL import Image, ImageFilter

image = Image.open("./Pokedex/pikachu.jpg")
filter_image = image.convert("L")
crooked = filter_image.rotate(180)
resize = filter_image.resize((300, 300))
box = (100, 100, 400, 400)
region = filter_image.crop(box)
region.save("region.png", "png")
