from PIL import Image

img = Image.open("monro.jpeg")
print(img.mode)

# test convert cmyk to rgb

img2 = Image.open("cmyk.jpg")
print(img2.mode)
img2rgb = img2.convert("RGB")
print(img2rgb.mode)

red, green, blue = img.split()

# red channel

new_red = red

coordinates_red = (100, 0, new_red.width, new_red.height)
cropped_red = new_red.crop(coordinates_red)

coordinates2_red = (50, 0, red.width - 50, red.height)
cropped2_red = red.crop(coordinates2_red)

image_red = Image.blend(cropped_red, cropped2_red, 0.5)  # image_red - red channel

# blue channel

new_blue = blue

coordinates_blue = (0, 0, new_blue.width - 100, new_blue.height)
cropped_blue = new_blue.crop(coordinates_blue)

coordinates2_blue = (50, 0, blue.width - 50, blue.height)
cropped2_blue = blue.crop(coordinates2_blue)

image_blue = Image.blend(cropped_blue, cropped2_blue, 0.5)  # image_blue - blue channel

# green channel

coordinates_green = (50, 0, green.width - 50, red.height)
image_green = green.crop(coordinates_green)  # cropped_green - green channel

final_effect = Image.merge("RGB", (image_red, image_green, image_blue))

print(final_effect.width, final_effect.height)
final_effect.thumbnail((80, 70))
final_effect.show()
final_effect.save("final.jpg", format="JPEG")
