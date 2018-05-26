def get_value_key_int(str_key):
    if str_key == 'bloque_38':
        return 0
    if str_key == 'biblioteca':
        return 1
    if str_key == 'agora':
        return 2
    if str_key == 'dogger':
        return 3
    if str_key == 'admisiones':
        return 4
    if str_key == 'auditorio':
        return 5
    if str_key == 'bloque_18':
        return 6
    if str_key == 'administracion':
        return 7
    if str_key == 'idiomas':
        return 8
    if str_key == 'bloque_19':
        return 9
    return 10

def get_value_key_str(int_key):
    if int_key == 0:
        return 'bloque_38'
    if int_key == 1:
        return 'blioteca'
    if int_key == 2:
        return 'agora'
    if int_key == 3:
        return 'dogger'
    if int_key == 4:
        return 'admisiones'
    if int_key == 5:
        return 'auditorio'
    if int_key == 6:
        return 'bloque_18'
    if int_key == 7:
        return 'administracion'
    if int_key == 8:
        return 'idiomas'
    if int_key == 9:
        return 'bloque_19'
    return 'Ningun lugar'
