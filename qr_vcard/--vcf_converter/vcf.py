organization = "emencia"

name_first = "samy"

name_last = "saad"

mobile_pers = '0695653201'

mobile_pro = '0312456987'

mail_pers = "samysaad01@gmail"

mail_pro = "samy@emencia.com"

web_site = "www.emencia.com"   

logo = ""


def get_full_name():
    return name_first+' '+name_last
    
def get_file_name():
    return name_first+'-'+name_last+'-'+organization

def vcfWriter():

    vcfLines = [
        'BEGIN:VCARD',
        'VERSION:4.0',
        f'FN:{get_full_name()}',
        f'EMAIL;TYPE=work:{mail_pro}',
        f'EMAIL;TYPE=home:{mail_pers}',
        f'TEL;TYPE=work:{mobile_pro}',
        f'TEL;TYPE=home:{mobile_pers}',
        f'ORG:{organization}',
        f'URL:{web_site}',
        f'LOGO:{logo}',
        'END:VCARD',
        ]
    with open(f'{get_file_name()}.vcf',
              'w') as f:
        for elt in vcfLines:
            f.write(elt)
            f.write('\n')

get_full_name()
get_file_name()
vcfWriter()