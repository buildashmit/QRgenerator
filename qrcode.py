import segno

qrcode = segno.make_qr("https://www.youtube.com/playlist?list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_")
qrcode.save(
    "comp_networks.png", 
    scale=10,
    dark="green",
)




