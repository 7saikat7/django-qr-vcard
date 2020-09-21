import segno


qr = segno.make_qr('https://www.emencia.com/fr/', error = "H")
qr.save(out = 'emencia.png', kind = "png" , scale = 10, border=0) 
