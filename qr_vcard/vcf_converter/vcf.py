


def vcfWriter(organization, first_name, last_name,
              phone_pers, phone_pro, email_pers,
              email_pro, web_site, logo):
    
    name = first_name + ' ' + last_name
    
    vcfLines = []
    vcfLines.append('BEGIN:VCARD')
    vcfLines.append('VERSION:4.0')
    vcfLines.append(f'FN:{name}')
    vcfLines.append(f'EMAIL;TYPE=work:{email_pro}')
    vcfLines.append(f'EMAIL;TYPE=home:{email_pers}')
    vcfLines.append(f'TEL;TYPE=work:{phone_pro}')
    vcfLines.append(f'TEL;TYPE=home:{phone_pers}')
    vcfLines.append(f'ORG:{organization}')
    vcfLines.append(f'URL:{web_site}')
    vcfLines.append(f'LOGO:{logo}')
    vcfLines.append(f'END:VCARD')
    vcfString = ''.join(vcfLines) + '\n'
    
    return vcfString

with open(f'{first_name}-{last_name}-{organization}.vcf',
          'w', newline='') as f:
    f.write(vcfWriter("db_data_vcard"))