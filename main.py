from PIL import Image, ImageDraw

bottom_image = Image.open('./scr/106044_benefit.jpg')
top_image = Image.open('./scr/benefit.png')
mask = Image.new("L", top_image.size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle((790, 0, 0, 130), fill=150)
output = bottom_image.copy()
output.paste(top_image, (0, 0), mask)
output.save('./scr/output_image.jpg', quality=95)


