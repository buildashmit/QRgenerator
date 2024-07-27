import segno

qrcode = segno.make_qr("https://www.youtube.com/playlist?list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_")
qrcode.save(
    "my_qrcode.png", 
    scale=10,
    dark="green",
)




