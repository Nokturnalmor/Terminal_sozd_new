import hashlib
import config
import os
from datetime import datetime as DT
import Cust_Functions as F

cfg = config.Config('Config\CFG.cfg') #файл конфига, находится п папке конфиг

def proverka_nalichie_znach(item):
    if cfg[item] != '':
        return True
    else:
        return False

def proverka_nalichie_puti(item):
    if os.path.exists(cfg[item] + '\\' + item + '.txt') == True or os.path.exists(cfg[item] + '\\' + item + '.db') == True:
        return True
    else:
        return False

def nomer_proekt_po_nom_nar(nn,kol,Stroki = False):
    if Stroki == False:
        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
    for line in Stroki:
        if line.startswith(nn + '|') == True:
            arr = [x for x in line.split('|')]
            return arr[kol]

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


def max_kol(spisok):
    maxk = 0
    for item in spisok:
        k = item.count("|") +1
        if k > maxk:
            maxk = k
    return maxk

def parametr_iz_akta(sroka,ima):
    arr_br = sroka.split('|')
    flag = 0
    for i in arr_br:
        if ima in i:
            flag = 1
            rez = i.replace(ima,"")
    if flag == 1:
        return rez
    else:
        return ""

def now():
    return DT.today().strftime("%d.%m.%Y %H:%M:%S")

def date(god=2):
    if god == 4:
        return DT.today().strftime("%d.%m.%Y")
    else:
        return DT.today().strftime("%d.%m.%y")

def summ_chasov_po_imeni_new(ima,Stroki_nar):
    summ = 0
    nom_kol_ФИО = F.nom_kol_po_im_v_shap(Stroki_nar,'ФИО')
    nom_kol_ФИО2 = F.nom_kol_po_im_v_shap(Stroki_nar, 'ФИО2')
    nom_kol_Время_час = F.nom_kol_po_im_v_shap(Stroki_nar, 'Время_час')
    for i in range(1,len(Stroki_nar)):
        if Stroki_nar[i][nom_kol_ФИО] == ima:
            if Stroki_nar[i][nom_kol_ФИО2] != "":
                summ += F.valm(Stroki_nar[i][nom_kol_Время_час])/2
            else:
                summ += F.valm(Stroki_nar[i][nom_kol_Время_час])
    for i in range(1,len(Stroki_nar)):
        if Stroki_nar[i][nom_kol_ФИО2] == ima:
            if Stroki_nar[i][nom_kol_ФИО] != "":
                summ += F.valm(Stroki_nar[i][nom_kol_Время_час])/2
            else:
                summ += F.valm(Stroki_nar[i][nom_kol_Время_час])
    return round(summ,2)

def summ_chasov_po_imeni(ima,Stroki_nar,Stroki_Zhur):
    #arr_ima = ima.split("  ")
    #arr_ima.pop()
    #ima = "  ".join(arr_ima)
    sp_nar = []
    summ = 0
    dl = len(Stroki_nar)
    for i in range(dl-1,dl-dl//3,-1):
        #if Stroki_nar[i][2].count('.') == 2 and Stroki_nar[i][2].count(':') == 2:
            #delta = (DT.now() - DT.strptime(Stroki_nar[i][2],"%d.%m.%Y %H:%M:%S")).days
            #if delta < 10:
        if ima == Stroki_nar[i][17] or ima == Stroki_nar[i][18]:
            sp_nar.append([Stroki_nar[i][0],Stroki_nar[i][5]])
    for i in range(len(sp_nar)):
        flag_zakr = 0
        for z in range(len(Stroki_Zhur)-1,0,-1):
            if  sp_nar[i][0] == Stroki_Zhur[z][2] and "Завершен" == Stroki_Zhur[z][7] and ima == Stroki_Zhur[z][3]:
                flag_zakr = 1
                break
        if flag_zakr == 0:
            tmp = sp_nar[i][1].replace(',','.')
            summ +=  float(tmp)
    return int(round(summ))
