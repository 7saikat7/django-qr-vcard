import segno
from segno import helpers
from PIL import Image


organization = "emencia"
name_first = "samy"
name_last = "saad"
mobile_pers = '0695653201'
mobile_pro = '0312456987'
mail_pers = "samysaad01@gmail"
mail_pro = "samy@emencia.com"
web_site = "www.emencia.com"   
logo = ""

qrurl = segno.make_qr('https://www.emencia.com/fr/', error = "H")
qrurl.save(out = 'django-qr-vcard/qr_vcard/--generate_qr/qr_emencia_url-only.png', kind = "png", compresslevel = 9, scale = 10, border = 5)

# Now open that png image to put the logo
img = Image.open('/home/sam/Bureau/QRcard/django-qr-vcard/qr_vcard/--generate_qr/qr_emencia_url-only.png')
width, height = img.size

# How big the logo we want to put in the qr code png
logo_size = 100

# Open the logo image
un_logo = Image.open('/home/sam/Bureau/QRcard/django-qr-vcard/qr_vcard/--generate_qr/logo.png')

# Calculate xmin, ymin, xmax, ymax to put the logo at the center of the qrcode
xmin = ymin = int((width / 2) - (logo_size / 2))
xmax = ymax = int((width / 2) + (logo_size / 2))

# resize the logo as calculated
un_logo = un_logo.resize((xmax - xmin, ymax - ymin))

# put the logo in the qr code
img.paste(un_logo, (xmin, ymin, xmax, ymax))

# save the qr_code
img.save('/home/sam/Bureau/QRcard/django-qr-vcard/qr_vcard/--generate_qr/qr_emencia_url_logo.png')

qr_vcard = helpers.make_vcard(name = f'{name_last};{name_first}',
                              displayname = f'{name_first};{name_last}',
                              email = (mail_pro, mail_pers),
                              url = (web_site),
                              phone = (mobile_pro, mobile_pers),
                              org = organization,
                              photo_uri = logo,
                              )

qr_vcard.save(out = 'django-qr-vcard/qr_vcard/--generate_qr/qr_vcard.png', kind = "png", compresslevel = 9, scale = 10,border = 5)