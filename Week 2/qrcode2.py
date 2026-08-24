import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

vid = 'https://youtube.com/shorts/UcwxiALUIHY?si=wCrLz0iCtyXTAwFO'
qr.add_data(vid)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="red")

img.save("youtube_vid.png")

qr.make_image()
