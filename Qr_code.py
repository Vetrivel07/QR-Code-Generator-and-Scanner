import qrcode
from PIL import Image, ImageDraw, ImageFont

linkedin_url = "https://www.linkedin.com/in/vetrivel-maheswaran/"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(linkedin_url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

text = "Scan for My LinkedIn Profile"
font = ImageFont.load_default()

img_width, img_height = qr_img.size
text_height = 30
new_img = Image.new("RGB", (img_width, img_height + text_height), "white")
new_img.paste(qr_img, (0, 0))

draw = ImageDraw.Draw(new_img)
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0] 
text_height = bbox[3] - bbox[1]

draw.text(((img_width - text_width) / 2, img_height + 5), text, font=font, fill="black")

new_img.save("my_qrcode.png")

