import hashlib
import config
import os

cfg = config.Config('Config\CFG.cfg') #файл конфига, находится п папке конфиг

def proverka_nalichie_znach(item):
    if cfg[item] != '':
        return True
    else:
        return False

def proverka_nalichie_puti(item):
    if os.path.exists(cfg[item] + '\\' + item + '.txt') == False:
        return False
    else:
        return True

def nomer_proekt_po_nom_nar(nn,kol):
    with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
        Stroki = f.readlines()
    for line in Stroki:
        if line.startswith(nn + '|') == True:
            arr = [x for x in line.split('|')]
            return arr[kol]
    return ''

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

def etap_po_fio(fio,massiv):
    line = fio.replace('\n', '')
    *fio, Dolgn = [x for x in line.split('  ')]
    for item in massiv:
        if Dolgn in item.strip():
            fio, etap = [x for x in item.split('|')]
            return etap.strip()
    return ''

def Podtv_lich_parol(FIO,Pred_parol):
    parol = None
    with open(cfg['Riba'] + '\\Riba.txt', 'r') as f:
        Stroki = f.readlines()
    for line in Stroki:
        if shifr(FIO.strip()) in line.strip():
            arr = [x for x in line.split('|')]
            parol = arr[len(arr) - 1]
            parol = parol.replace('\n', '')
            break
    if parol == None:
        return None
    if parol == shifr(Pred_parol):
        return True
    else:
        return False

def shifr(password):
    pass_hash= hashlib.md5(password.encode('utf-8')).hexdigest()
    return pass_hash

def max_kol(spisok):
    maxk = 0
    for item in spisok:
        k = item.count("|") +1
        if k > maxk:
            maxk = k
    return maxk

def parametr_iz_akta(sroka,ima):
    arr_br = [x for x in sroka.split(ima)]
    if '|' in arr_br[1]:
        arr_br2 = [x for x in arr_br[1].split('|')]
        rez = arr_br2[0]
    else:
        rez = arr_br[1]
    return rez

def summ_chasov_po_imeni(ima):
    arr_ima = ima.split("  ")
    arr_ima.pop()
    ima = "  ".join(arr_ima)
    ima2 = " ".join(arr_ima)
    summ = 0
    with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
        Stroki_nar = f.readlines()
    with open(cfg['BDzhurnal'] + '\\BDzhurnal.txt', 'r') as f:
        Stroki_Zhur = f.readlines()
    for line in Stroki_nar:
        if ima in line or ima2 in line:
            arr = line.split('|')
            nom_nar = arr[0]
            flag_zakr = 0
            for line_z in Stroki_Zhur:
                if nom_nar in line_z and "|Завершен|" in line_z:
                    flag_zakr = 1
                    break
            if flag_zakr == 0:
                summ += float(arr[5].replace(',','.'))
    return int(round(summ))

