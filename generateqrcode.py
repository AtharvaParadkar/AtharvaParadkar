import qrcode

qr_code = qrcode.make('https://www.youtube.com/watch?v=kJQP7kiw5Fk&ab_channel=LuisFonsiVEVO')

qr_code.save('myQRcode.png')

qr_code.show()
