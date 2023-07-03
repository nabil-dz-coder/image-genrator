from PIL import Image, ImageDraw, ImageFont

# Minimum required dimensions
minimum_width =5000
minimum_height =7000

# Create the image with transparent background
img = Image.new("RGBA", (minimum_width, minimum_height), color=(0,0,0,0))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", size=400)
text = "   Cat logic:\nKnock things\n off shelves ".upper()

# Get the width and height of the text
text_width, text_height = draw.textsize(text.upper(), font=font)

# Calculate the coordinates to place the text at the center
x = (img.width - text_width) // 2
y = (img.height - text_height) // 2

draw.text((x, y), text, fill=(255, 255, 255, 255), font=font)  # Set fill color with alpha=255 for opaque text

# Save the image to your computer
img.save("output_image.png", format="PNG")
