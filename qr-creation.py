import qrcode # pip install qrcode[pil]


def make_qrcode(data, qr_color, back_color, file_name):
    qr = qrcode.QRCode(
            version=1,
            box_size=15,
            border=2
            )
    qr.add_data(data)    
    qr.make(fit=True)
    img=qr.make_image(fill=qr_color, back_color=back_color)
    img.save(file_name)

make_qrcode(
        data='https://google.com/', # Адресс КуАр Кода
        qr_color='black', # Цвет самого кода
        back_color='white', # Цвет фона
        file_name='file.png' # Названия файла
        )
