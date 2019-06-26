from PIL import Image

img = Image.open("monro.jpeg")

red, green, blue = img.split()

first_crop = 100
second_crop = 50

new_red = red
coordinates_red = (first_crop, 0, new_red.width, new_red.height)
cropped_red = new_red.crop(coordinates_red)
coordinates2_red = (second_crop, 0, red.width - second_crop, red.height)
cropped2_red = red.crop(coordinates2_red)
image_red = Image.blend(cropped_red, cropped2_red, 0.5)

new_blue = blue
coordinates_blue = (0, 0, new_blue.width - first_crop, new_blue.height)
cropped_blue = new_blue.crop(coordinates_blue)
coordinates2_blue = (second_crop, 0, blue.width - second_crop, blue.height)
cropped2_blue = blue.crop(coordinates2_blue)
image_blue = Image.blend(cropped_blue, cropped2_blue, 0.5)

coordinates_green = (second_crop, 0, green.width - second_crop, red.height)
image_green = green.crop(coordinates_green)

size = (80, 80)
your_image = Image.merge("RGB", (image_red, image_green, image_blue))
your_image.thumbnail(size)
your_image.show()
your_image.save("your_image.jpg", format="JPEG")
