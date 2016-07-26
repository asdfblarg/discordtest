from PIL import Image
from PIL import ImageFont, ImageDraw

image = Image.open("C:/Users/Zeng/PycharmProjects/test 1/cu.jpg")
im = Image.open("C:/Users/Zeng/PycharmProjects/test 1/cu.jpg")
im3 = Image.open("C:/Users/Zeng/PycharmProjects/discordtest/twitch_emotes/3.0/OSkomodo.png")
im1 = Image.open("C:/Users/Zeng/PycharmProjects/discordtest/twitch_emotes/3.0/MingLee.png")
im2 = Image.open("C:/Users/Zeng/PycharmProjects/discordtest/twitch_emotes/3.0/OSkomodo.png")

draw = ImageDraw.Draw(image)
# use a truetype font
font = ImageFont.truetype("C:/Windows/Fonts/arialnb.ttf", 30)
# draw.text((10, 10), "hello", font=font, fill='blue')
# draw.text((10, 25), "world", font=font, fill='blue')
draw.text((350, 40), "Ayy", font=font, fill='blue')
draw.text((350, 70), "jimethn", font=font, fill='blue')
draw.text((350, 100), ":D", font=font, fill='blue')
# image.show()

# draw = ImageDraw.Draw(im)
# draw.line((0, 0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=128)
# del draw
# im.show()


# images = [image,im,im3]
# # images = [im1,im2,im3]
# max_width = max(image.size[0] for image in images)
# max_height = max(image.size[1] for image in images)
#
# image_sheet = Image.new("RGBA", (max_width * len(images), max_height))
#
# for (i, image) in enumerate(images):
#     centered_width = int(max_width * i + (max_width - image.size[0]) / 2)
#     centered_height = int(max_height * 0 + (max_height - image.size[1]) / 2)
#     image_sheet.paste(image, (centered_width,centered_height))
#
#
# image_sheet.show()
# image_sheet.save("test.png")
#
# # convert png with transparent background to jpg
# png = Image.open("test.png")
# png.load() # required for png.split()
#
# background = Image.new("RGB", png.size, (255, 255, 255))
# background.paste(png, mask=png.split()[3]) # 3 is the alpha channel
#
# background.save('foo.jpg', 'JPEG', quality=80)
