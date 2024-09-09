from PIL import Image, ImageFilter

img = Image.open("./Pokedex")
filtered_img = img.convert("L")
filtered_img.save(img)
filtered_img.show()
