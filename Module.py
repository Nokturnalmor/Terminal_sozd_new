from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWinExtras import QtWin
import os
import time
from datetime import datetime as DT
import subprocess
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
import config
import sys
import FCN
import Cust_Functions as F

cfg = config.Config('Config\CFG.cfg') #файл конфига, находится п папке конфиг

proverka_list_puti = ['employee','Riba','Naryad','FiltrEmp','BD_Proect','Etapi','BDzhurnal','Filtr_rab','BDact']
proverka_list_znach = ['ogran_shir','Stile']



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.modal = 0
        #self.setFixedSize(1280, 720)
        self.setWindowTitle("Создание нарядов")
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.lineEdit_Nparol.setVisible(False)
        self.ui.lineEdit_Nparol2.setVisible(False)
        self.ui.pushButton_login.clicked.connect(self.log_in)
        self.ui.pushButton_login.setAutoDefault(True)  # click on <Enter>
        self.ui.lineEdit_parol.returnPressed.connect(self.ui.pushButton_login.click)  # click on <Enter>
        self.ui.pushButton_logout.clicked.connect(self.logout)
        #self.ui.tableWidget_vibpr_proekta.itemClicked.connect(self.tabl_vibor_proekta)




        self.ui.pushButton_create_nar.clicked.connect(self.sozd_naryad)
        #self.ui.tabWidget.tabBarClicked.connect(self.tab_click)
        tabl_vibor_nar = self.ui.tableWidget_vibor_nar_dlya_imen
        tabl_vibor_nar.itemClicked.connect(self.tabl_vibor_nar_dla_imen)
        F.ust_cvet_videl_tab(tabl_vibor_nar)
        tabl_vibor_nar.setSelectionBehavior(1)
        tabl_vibor_nar.setSelectionMode(1)

        self.ui.tableWidget_vibor_imeni_sla_nar.itemClicked.connect(self.tabl_vibor_fio_dla_imen)
        self.ui.pushButton_primen_imena.clicked.connect(self.primenit_imena)
        self.ui.radioButton_vse.clicked.connect(self.corr_vse)
        self.ui.radioButton_ne_nachatie.clicked.connect(self.corr_ne_nach)
        self.ui.radioButton_nachatie.clicked.connect(self.corr_nach)
        self.ui.radioButton_zavershonnie.clicked.connect(self.corr_zavershonnie)
        self.ui.pushButton_primen_correctirovky.clicked.connect(self.delete_naryad)
        self.ui.pushButton_primen_primenit_opovesh.clicked.connect(self.prim_opovesh)
        self.ui.pushButton_komplect.clicked.connect(self.komplektovano)
        self.ui.pushButton_Nekomplect.clicked.connect(self.nekomplekt)
        self.ui.pushButton_primen_corr_fio.clicked.connect(self.delete_fio)

        tabl_vib_mk = self.ui.tableWidget_vibor_mk
        tabl_vib_mk.setSelectionBehavior(1)
        tabl_vib_mk.setSelectionMode(1)
        F.ust_cvet_videl_tab(tabl_vib_mk)
        tabl_vib_mk.clicked.connect(self.vibor_mk_0)
        tabl_vib_mk.doubleClicked.connect(self.dblclk_sp_mk)

        tabl_vib_det = self.ui.tableWidget_vibor_det
        tabl_vib_det.setSelectionBehavior(1)
        tabl_vib_det.setSelectionMode(1)
        F.ust_cvet_videl_tab(tabl_vib_det)
        tabl_vib_det.clicked.connect(self.vibor_operacii)
        tabl_vib_det.doubleClicked.connect(self.dblclk_mk)
        tabl_vib_det.setFont(QtGui.QFont("Segoe UI", 8))

        tabl_vib_oper = self.ui.tableWidget_vibor_oper
        tabl_vib_oper.setSelectionBehavior(1)
        tabl_vib_oper.setSelectionMode(1)
        F.ust_cvet_videl_tab(tabl_vib_oper)
        tabl_vib_oper.clicked.connect(self.vvod_oper)

        line_kolvo = self.ui.lineEdit_cr_nar_kolvo
        line_kolvo.textChanged.connect(self.rasch_norm_vr)


        lineEdit_mk = self.ui.lineEdit_mk
        lineEdit_mk.textEdited.connect(self.poisk_mk)

        lineEdit_np = self.ui.lineEdit_np
        lineEdit_np.textEdited.connect(self.poisk_np)

        lineEdit_py = self.ui.lineEdit_py
        lineEdit_py.textEdited.connect(self.poisk_py)

        lineEdit_prim = self.ui.lineEdit_prim
        lineEdit_prim.textEdited.connect(self.poisk_prim)

        check_yprosh = self.ui.checkBox_min_rezhjim
        check_yprosh.clicked.connect(self.rezjim_mk)

        button_obnov = self.ui.pushButton_obnov_mk
        button_obnov.clicked.connect(self.vibor_mk_0)

        

        self.action_noviy_user = self.findChild(QtWidgets.QAction, "action_noviy_user")
        self.action_noviy_user.triggered.connect(self.Reg_new_user)
        self.action__change_pass = self.findChild(QtWidgets.QAction, "action__change_pass")
        self.action__change_pass.triggered.connect(self.Smena_Parol)
        self.ui.radioButton_ispoln1.setChecked(True)
        self.ui.checkBox.setCheckState(1)
        self.ui.checkBox_vecher.setCheckState(1)
        self.ui.checkBox_vneplan_rab.setTristate(False)
        self.ui.checkBox_vneplan_rab.stateChanged.connect(self.check_vneplan_rab)
        self.ui.lineEdit_cr_nar_nom_proect.setEnabled(False)
        self.ui.lineEdit_cr_nar_nomerPU.setEnabled(False)
        self.ui.lineEdit_cr_nar_norma.setEnabled(False)
        self.ui.lineEdit_cr_nar_pozicii.setEnabled(False)
        self.ui.plainTextEdit_zadanie.setEnabled(False)
        self.ui.pushButton_primen_correctirovky.setEnabled(False)
        self.ui.tableWidget_vibor_imeni_sla_nar.setSortingEnabled(True)

        tabl_kompl = self.ui.tableWidget_tabl_komplektovki
        tabl_kompl.setSortingEnabled(True)
        F.ust_cvet_videl_tab(tabl_kompl)
        tabl_kompl.setSelectionBehavior(1)
        tabl_kompl.setSelectionMode(1)


        self.ui.tableWidget_spispk_nar_dla_korrect.setSortingEnabled(True)
        # =====================================================проверка файлов
        for item in proverka_list_puti:
            if FCN.proverka_nalichie_puti(item) == False:
                self.showDialog("Не найден " + item)
                sys.exit(app.exec())
        for item in proverka_list_znach:
            if FCN.proverka_nalichie_znach(item) == False:
                self.showDialog("Не найден " + item)
                sys.exit(app.exec())
        # =====================================================


        with open(cfg['employee'] + '\\employee.txt', 'r', encoding='utf-8') as f:
            Stroki = f.readlines()
        with open(cfg['FiltrEmp'] + '\\FiltrEmp.txt', 'r') as f:
            Stroki_emp = f.readlines()
        Stroki_temp2 = Stroki.copy()
        with open(cfg['FiltrEmpDel'] + '\\FiltrEmpDel.txt', 'r') as f:
            Stroki_FiltrEmpDel = f.readlines()
        for item in Stroki_temp2:
            for iskl in Stroki_FiltrEmpDel:
                if iskl.strip() in item:
                    Stroki.remove(item)
                    break
        Stroki_temp2.clear()

        for line in Stroki:
            line = line.replace(',', '  ')
            line = line.replace('\n', '')
            if FCN.etap_po_fio(line, Stroki_emp) != "":
                line = line.encode('cp1251', errors='ignore').decode('cp1251')
                self.ui.comboBox_spis_users.addItem(line)
        with open(cfg['Etapi'] + '\\Etapi.txt', 'r') as f:
            Stroki = f.readlines()
        self.ui.comboBox_cr_nar_etap.addItem("")
        for item in Stroki:
            self.ui.comboBox_cr_nar_etap.addItem(item.strip())

        self.ui.lineEdit_parol.setText('2020')
        self.ui.comboBox_spis_users.setCurrentIndex(2)

    def keyReleaseEvent(self, e):
        # print(str(int(e.modifiers())) + ' ' +  str(e.key()))
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        tableWidget_tabl_komplektovki = self.ui.tableWidget_tabl_komplektovki
        if self.modal == 0:
            if e.key() == 16777220:
                if tabl_mk.hasFocus() == True:
                    self.ui.tabWidget_2.setCurrentIndex(2)
                    self.modal = 1
                if tabl_sp_mk.hasFocus() == True:
                    self.ui.tabWidget_2.setCurrentIndex(1)

                if tabl_sp_oper.hasFocus() == True:
                    if self.modal == 1:
                        self.modal = 0
                        return
                    self.sozd_naryad()
                if tableWidget_tabl_komplektovki.hasFocus() == True:
                    if tableWidget_tabl_komplektovki.item(tableWidget_tabl_komplektovki.currentRow(),7).text() == '':
                        self.komplektovano()
                    else:
                        self.nekomplekt()
        else:
            self.modal = 0

    def rezjim_mk(self):
        check_yprosh = self.ui.checkBox_min_rezhjim
        tabl_mk = self.ui.tableWidget_vibor_det
        if check_yprosh.checkState() == 0:
            for i in range(tabl_mk.rowCount()):
                tabl_mk.setRowHidden(i,False)
            for i in range(tabl_mk.columnCount()):
                if i != 6:
                    tabl_mk.setColumnHidden(i,False)
        else:
            for i in range(tabl_mk.rowCount()):
                flag_kompl = 0
                for j in range(11,tabl_mk.columnCount(),4):
                    if tabl_mk.item(i,j+1).text() != '' and 'Полный' not in tabl_mk.item(i,j+2).text():
                        flag_kompl = 1
                        break
                if flag_kompl == 0:
                    tabl_mk.setRowHidden(i,True)

            for j in range(11, tabl_mk.columnCount(), 4):
                flag_pust = 1
                for i in range(tabl_mk.rowCount()):
                    if tabl_mk.isRowHidden(i) == False:
                        if tabl_mk.item(i,j).text() != '':
                            flag_pust = 0
                            break
                if flag_pust == 1:
                    tabl_mk.setColumnHidden(j,True)
                    tabl_mk.setColumnHidden(j+1, True)
                    tabl_mk.setColumnHidden(j+2, True)
                    tabl_mk.setColumnHidden(j+3, True)
            for j in range(3,11):
                tabl_mk.setColumnHidden(j, True)


    def rasch_norm_vr(self):
        line_norma = self.ui.lineEdit_cr_nar_norma
        line_kolvo = self.ui.lineEdit_cr_nar_kolvo
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        if line_kolvo.text().strip() == "":
            return
        else:
            if F.is_numeric(line_kolvo.text().strip()) == False:
                self.showDialog('Не верно внесено кол-во')
                return
        kol = int(line_kolvo.text().strip())
        t_pz = F.valm(tabl_sp_oper.item(tabl_sp_oper.currentRow(),4).text().strip())
        t_sht = F.valm(tabl_sp_oper.item(tabl_sp_oper.currentRow(),5).text().strip())
        koid = F.valm(tabl_sp_oper.item(tabl_sp_oper.currentRow(),9).text().strip())
        if koid == 0:
            return 0
        vr = t_pz+t_sht*kol/koid
        line_norma.setText(str(round(vr/60,2)))
        return round(vr/60,2)




    def dblclk_mk(self):
        tabl_mk = self.ui.tableWidget_vibor_det
        r = tabl_mk.currentRow()
        k = tabl_mk.currentColumn()
        if k >10 and (k-11)%4==0:
            self.vigruz_tehkart(r,k)
        if k >10 and (k-12)%4==0:
            self.vigruz_tara(r,k)
        if k <4:
            self.ui.tabWidget_2.setCurrentIndex(2)


    def check_vneplan_rab(self):
        chek_vneplan = self.ui.checkBox_vneplan_rab
        if chek_vneplan.checkState() == 2:
            self.ui.lineEdit_cr_nar_norma.setEnabled(True)
            self.ui.plainTextEdit_zadanie.setEnabled(True)
        else:
            self.ui.lineEdit_cr_nar_norma.setEnabled(False)
            self.ui.plainTextEdit_zadanie.setEnabled(False)
            self.ui.lineEdit_cr_nar_nom_proect.clear()
            self.ui.lineEdit_cr_nar_nomerPU.clear()
            self.ui.lineEdit_cr_nar_norma.clear()
            self.ui.lineEdit_cr_nar_pozicii.clear()
            self.ui.plainTextEdit_zadanie.clear()

    def vvod_oper(self):
        '''
        3.вписать в МК все наряды по операциям этой детали.
            3.1 как определить что все опереации выполнены
        4. добавить внеплановые работы
        5.
        '''
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        line_nom_pr = self.ui.lineEdit_cr_nar_nom_proect
        line_nom_pu = self.ui.lineEdit_cr_nar_nomerPU
        line_kolvo = self.ui.lineEdit_cr_nar_kolvo
        line_norma = self.ui.lineEdit_cr_nar_norma
        line_dse = self.ui.lineEdit_cr_nar_pozicii
        text_zad = self.ui.plainTextEdit_zadanie
        chek_vneplan = self.ui.checkBox_vneplan_rab
        self.check_vneplan_rab()

        line_nom_pr.setText('')
        line_nom_pu.setText('')
        line_kolvo.setText('')
        line_norma.setText('')
        line_dse.setText('')
        text_zad.setPlainText('')
        chek_vneplan.setCheckState(0)

        if tabl_sp_oper.item(tabl_sp_oper.currentRow(),12).text().strip() == '2':
            return
        if tabl_mk.currentRow() == -1:
            self.showDialog('Не выбрана дсе')
            return
        if tabl_sp_mk.currentRow() == -1:
            self.showDialog('Не выбрана мк')
            return
        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(),0).text()
        id_dse = tabl_mk.item(tabl_mk.currentRow(), 6).text()
        nom_det = tabl_mk.item(tabl_mk.currentRow(), 1).text().strip()
        nom_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(), 1).text().strip()
        nom_pu = tabl_sp_mk.item(tabl_sp_mk.currentRow(),4).text()
        nom_pr = tabl_sp_mk.item(tabl_sp_mk.currentRow(),5).text()
        if nom_pr == None:
            nom_pr = '*'
        line_nom_pr.setText(nom_pr)
        line_nom_pu.setText(nom_pu)
        kolvo = self.summ_dost_det_po_nar(nom_mk, id_dse, nom_op)
        line_kolvo.setText(str(kolvo))
        norm_vr = self.rasch_norm_vr()

        line_dse.setText(nom_det)

        naim_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(),0).text().strip()
        nom_rc = tabl_sp_oper.item(tabl_sp_oper.currentRow(),2).text().strip()
        naim_ob = tabl_sp_oper.item(tabl_sp_oper.currentRow(),3).text().strip()
        docs = tabl_sp_oper.item(tabl_sp_oper.currentRow(),11).text().strip()
        materials = tabl_sp_oper.item(tabl_sp_oper.currentRow(),8).text().strip()
        if materials != '':
            materials = materials.split('; ')
        masgg = F.vpis(nom_op + ' ' + naim_op ,50,"","") + '\n'
        if docs != '':
            masgg += 'Документация: ' + docs + '\n'
        masgg+= nom_rc + ' ' + naim_ob + '\n'
        masgg += 'Время: ' + str(norm_vr) + 'час.' + '\n'
        masgg += '\n'
        for i in range(tabl_sp_oper.currentRow()+1, tabl_sp_oper.rowCount()):
            if tabl_sp_oper.item(i,12).text().strip() != '2':
                break
            nom_per = tabl_sp_oper.item(i, 1).text().strip()
            naim_per = tabl_sp_oper.item(i, 0).text().strip()
            masgg += nom_per + ' ' + naim_per + '\n'
            masgg += '\n'
            osnast= tabl_sp_oper.item(i, 9).text().strip()
            instr = tabl_sp_oper.item(i, 10).text().strip()
            if instr != "":
                masgg += "Инструмент: " + instr + '\n'

            if osnast != "":
                masgg += "Оснастка: " + osnast + '\n'
                masgg += '\n'
        if materials != '':
            masgg += 'Материалы: ' + '\n'
            for i in range(0,len(materials)):
                masgg += materials[i] + '\n'
        text_zad.setPlainText(masgg)
        return





    def vigruz_tara(self, r, k):
        tabl_mk = self.ui.tableWidget_vibor_det
        if tabl_mk.item(r, k).text() == "":
            return
        tabl_sp_mk = self.ui.tableWidget_vibor_mk

        id = tabl_mk.item(r, 6).text().strip()

        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
        bd_arh_tar = F.otkr_f(F.tcfg('arh_tar'), separ='|')
        s = ''
        for i in bd_arh_tar:
            if i[3] == nom_mk:
                sost = i[6]
                nom = i[0]
                marsh = i[9]
                nazv = i[5]
                det_tmp = F.otkr_f(F.scfg('bd_tara') + os.sep + nom + '.txt', separ='|')
                for i in range(0, len(det_tmp)):
                    if det_tmp[i][3].strip() == id:
                        s += sost + ' ' + nom + ' ' + nazv + '\n' + marsh.replace('$',' ') + '\n' + '\n'
        self.showDialog(s)
        return

    def vigruz_tehkart(self,r,k):
        tabl_mk = self.ui.tableWidget_vibor_det
        if tabl_mk.item(r, k).text() == "":
            return
        tmp = tabl_mk.item(r, k).text().split('Операции:')
        sp_op = tmp[-1].split(';')
        if F.nalich_file(F.tcfg('BD_dse')) == False:
            self.showDialog('Не найден BD_dse')
            return
        sp_dse = F.otkr_f(F.tcfg('BD_dse'), False, '|')
        naim = tabl_mk.item(r, 0).text().strip()
        nn = tabl_mk.item(r, 1).text().strip()
        nom_tk = ''
        for i in range(0, len(sp_dse)):
            if sp_dse[i][0] == nn and sp_dse[i][1] == naim:
                nom_tk = sp_dse[i][2]
                if nom_tk == '':
                    self.showDialog('Не найден номер ТК')
                    return
                break

        sp_tk = F.otkr_f(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn + '.txt', False, "|")
        if sp_tk == ['']:
            self.showDialog('Не найден файл ТК')
            return
        msgg = ''
        for o1 in sp_op:
            msgg += str(o1) + ': '
            for i in range(11, len(sp_tk)):
                if sp_tk[i][3].startswith('Т1-' + str(o1).strip()) == True:
                    if sp_tk[i][20] == '1':
                        msgg += sp_tk[i][0] + '\n' + ' Tп.з.=' + sp_tk[i][6] + ' Tшт.=' + sp_tk[i][7] + '\n'
                    else:
                        msgg += sp_tk[i][0] + '\n'
            msgg += '\n'
        self.showDialog(msgg)

    def vibor_operacii(self):
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        if tabl_mk.currentRow() == -1:
            return
        id_det = tabl_mk.item(tabl_mk.currentRow(), 6).text()
        naim_det = tabl_mk.item(tabl_mk.currentRow(), 0).text().strip()
        nn_det = tabl_mk.item(tabl_mk.currentRow(), 1).text().strip()
        sp_dse = F.otkr_f(F.tcfg('BD_dse'), False, '|')
        if sp_dse == ['']:
            self.showDialog('Не найден BD_dse')
            return
        nom_tk = F.naiti_v_spis(sp_dse,2,nn_det,naim_det)
        sp_tk = F.otkr_f(F.scfg('add_docs') + os.sep + nom_tk + '_' + nn_det + '.txt', False, "|",pickl=True)
        if sp_tk == ['']:
            self.showDialog('Не найден файл ТК')
            return
        sp_tk2 = []
        for i in range(11, len(sp_tk)):
            if len(sp_tk[i])>2 and 'Т1' in sp_tk[i][3]:
                sp_tk2.append(sp_tk[i])
        sp_tk2 = self.oform_tk_pod_form(sp_tk2)
        F.zapoln_wtabl(self,sp_tk2,tabl_sp_oper,0,0,'','',300,True,'')

        r = tabl_mk.currentRow()
        spis_mk = F.spisok_iz_wtabl(tabl_mk, "")

        for j in range(11, len(spis_mk[r]), 4):
            if spis_mk[r][j] != '' and 'олный к' not in spis_mk[r][j + 2]:
                arr_nom_op = spis_mk[r][j].split('\n')
                arr_nom_op2 = arr_nom_op[-1].split(';')
                nom_op = arr_nom_op2[0]
                break
        for i in range(tabl_sp_oper.rowCount()):
            if tabl_sp_oper.item(i,1).text() == nom_op:
                tabl_sp_oper.selectRow(i)
                break


    def udal_kol(self,s,nom):
        for i in range(0, len(s)):
            s[i].pop(nom)
        return s

    def oform_tk_pod_form(self,sp_tk2):
        sp_tk2.insert(0, ['Sod','','Nom','','rc','oborud','Тпз','Тшт','проф','кр','material','оснастка/КОИД','инструмент','документ','','','','','','','ur'])
        tmp_uadl = [1,2,12,12,12,12,12,12]
        for i in tmp_uadl:
            sp_tk2 = self.udal_kol(sp_tk2,i)

        for i in range(len(sp_tk2)):
            if i > 0:
                sp_tk2[i][0] = ' '*4*(int(sp_tk2[i][12])-1) + sp_tk2[i][0]
            for j in range(8,12):
                sp_tk2[i][j] = sp_tk2[i][j].replace('{','; ')
                sp_tk2[i][j] = sp_tk2[i][j].replace('$', ', ')
        return sp_tk2

    def dblclk_sp_mk(self):
        self.ui.tabWidget_2.setCurrentIndex(1)
        self.zapoln_tabl_mk()


    def vibor_mk_0(self):
        self.vibor_mk()
    def vibor_mk(self, old_strok = -1):
        stroka = old_strok
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        if tabl_sp_mk.currentRow() == -1:
            return
        nom = tabl_sp_mk.item(tabl_sp_mk.currentRow(),0).text()
        if F.nalich_file(F.scfg('mk_data') + os.sep + nom + '.txt') == False:
            self.showDialog('Не обнаружен файл')
            return
        sp = F.otkr_f(F.scfg('mk_data') + os.sep + nom + '.txt',False,'|')
        if sp == []:
            self.showDialog('Некорректное содержимое МК')
            return
        sp = self.oformlenie_sp_pod_mk(sp)
        F.zapoln_wtabl(self, sp, tabl_mk, 0, 0, '', '', 100, True, '', 40)
        self.oform_mk(sp,nom)
        tabl_mk.setCurrentCell(stroka,1)


    def oformlenie_sp_pod_mk(self,s):
        for j in s:
            for i in range(11, len(s[0]),4):
                if '$' in j[i]:
                    vrem, oper1, oper2 = [x for x in j[i].split("$")]
                    j[i] = vrem + '\n' + oper1 + '\n' + oper2
            for i in range(13, len(s[0]),4):
                if '$' in j[i]:
                    j[i] = j[i].replace('$','\n')
            for i in range(14, len(s[0]),4):
                if '$' in j[i]:
                    j[i] = j[i].replace('$','\n')
        return s

    def uroven(self,strok):
        n = 0
        for i in range(0,len(strok)):
            if strok[i] == " ":
                n+=1
            else:
                break
        return int(n/4)

    def oform_mk(self,sp,nom_mk):
        shag = 15
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        maxs = set()
        for i in range(1,len(sp)):
            maxs.add(self.uroven(sp[i][0]))
        maxc = max(maxs)
        for i in range(1,len(sp)):
            uroven = self.uroven(sp[i][0])
            for j in range(0, len(sp[i])):
                F.dob_color_wtab(tabl_mk,i-1,j,0,0,shag*maxc-shag*uroven)
        for i in range(1, len(sp)):
            for j in range(11, len(sp[i]),4):
                F.dob_color_wtab(tabl_mk, i - 1, j, 10, 10, 10)
                if sp[i][j] == '':
                    for k in range(1,4):
                        F.dob_color_wtab(tabl_mk, i - 1, j+k, 10, 10, 10)
        tabl_mk.setColumnHidden(6,True)
        #komplekt
        for i in range(1, len(sp)):
            for j in range(12, len(sp[i]), 4):
                if tabl_mk.item(i - 1,j).text() != '':
                    if '(полный' in tabl_mk.item(i - 1,j).text():
                        F.dob_color_wtab(tabl_mk, i - 1, j, 0, 127, 0)
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j, 37, 17, 0)
                if tabl_mk.item(i - 1, j + 1).text() != '':
                    arr = tabl_mk.item(i - 1, j + 1).text().strip().split('\n')
                    set_sost = set()
                    for k in range(len(arr)):
                        arr2 = arr[k].split(' ')
                        set_sost.add(arr2[1])
                    if 'компл.' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 1, 0, 127, 0)  # зеленый
                    elif len(set_sost) == 1 and 'Выдан' in set_sost:
                        pass
                    elif len(set_sost) == 1 and 'Создан' in set_sost:
                        pass
                    else:
                        F.dob_color_wtab(tabl_mk, i - 1, j+1, 37, 17, 0)# оранж
                if tabl_mk.item(i - 1, j + 2).text() != '':
                    arr = tabl_mk.item(i - 1, j + 2).text().strip().split('\n')
                    set_sost = set()
                    for k in range(len(arr)):
                        arr2 = arr[k].split(' ')
                        if len(arr2) == 1:
                            set_sost.add('')
                        else:
                            set_sost.add(arr2[1])
                    if len(set_sost) == 1 and 'Исправлен' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 0, 127, 0)  # зеленый
                    if 'Неисп-мый' in set_sost:
                        F.dob_color_wtab(tabl_mk, i - 1, j + 2, 200, 10, 10)  # красный
                    F.dob_color_wtab(tabl_mk, i - 1, j+2, 37, 17, 0)# оранж

    def poisk_mk(self):
        obr = self.ui.lineEdit_mk.text()
        self.poisk_strok(0,obr)
    def poisk_np(self):
        obr = self.ui.lineEdit_np.text()
        self.poisk_strok(5,obr)
    def poisk_py(self):
        obr = self.ui.lineEdit_py.text()
        self.poisk_strok(4,obr)
    def poisk_prim(self):
        obr = self.ui.lineEdit_prim.text()
        self.poisk_strok(5,obr)

    def poisk_strok(self, kol, obr):
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        if obr == "":
            return
        for i in range(0,tabl_sp_mk.rowCount()):
            if F.cells(i,kol,tabl_sp_mk).upper().startswith(obr.upper()) == True:
                tabl_sp_mk.selectRow(i)
                return

    def zapoln_tabl_mk(self):
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        if F.nalich_file(F.tcfg('bd_mk')) == False:
            self.showDialog('Не найден bd_mk')
            return
        sp = F.otkr_f(F.tcfg('bd_mk'), separ='|')
        F.zapoln_wtabl(self, sp, tabl_sp_mk, 0, 0, '', '', 200, True, '', 10)

    def nekomplekt(self):
        i = self.ui.tableWidget_tabl_komplektovki.currentRow()
        tmp_strok = i
        Nom_nar = self.ui.tableWidget_tabl_komplektovki.item(i, 0).text()
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'),False,'|')
        for i in range(0, len(Stroki_nar)):
            if Stroki_nar[i][0] == Nom_nar:
                Stroki_nar[i][15]=''
                Stroki_nar[i][16]=''
                break
        F.zap_f(F.tcfg('Naryad'),Stroki_nar,'|')
        self.showDialog('Наряд ' + Nom_nar + ' отмечен - некомплект')
        self.zap_tabl_komplektovki()
        self.zap_tabl_vibor_nar_dlya_imen()
        self.ui.tableWidget_tabl_komplektovki.selectRow(tmp_strok)
        return

    def komplektovano(self):
        i = self.ui.tableWidget_tabl_komplektovki.currentRow()
        tmp_strok = i
        Nom_nar = self.ui.tableWidget_tabl_komplektovki.item(i, 0).text()
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        for i in range(0, len(Stroki_nar)):
            if Stroki_nar[i][0] == Nom_nar:
                Stroki_nar[i][15] = self.windowTitle()
                Stroki_nar[i][16] = DT.today().strftime("%d.%m.%Y %H:%M:%S")
                break
        F.zap_f(F.tcfg('Naryad'), Stroki_nar, '|')
        self.showDialog('Наряд ' + Nom_nar + ' скомплектован под сборку')
        self.zap_tabl_komplektovki()
        self.zap_tabl_vibor_nar_dlya_imen()

        self.ui.tableWidget_tabl_komplektovki.selectRow(tmp_strok)


        return


    def delete_naryad(self):
        self.statusBar().showMessage(self.ui.tableWidget_spispk_nar_dla_korrect.currentItem().text())
        i = self.ui.tableWidget_spispk_nar_dla_korrect.currentRow()
        Nom_nar = self.ui.tableWidget_spispk_nar_dla_korrect.item(i, 0).text()
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        for i in range(0, len(Stroki_nar)):
            if Stroki_nar[i][0] == Nom_nar:
                nom_mk = Stroki_nar[i][1]
                id_dse = Stroki_nar[i][25]
                nom_op = Stroki_nar[i][24]
                Stroki_nar.pop(i)
                break
        F.zap_f(F.tcfg('Naryad'), Stroki_nar, '|')
        self.showDialog('Наряд ' + Nom_nar + ' удален')
        self.zap_prosm_nar()
        self.zapis_v_mk(nom_op, id_dse,str(nom_mk))
        self.vibor_mk()
        self.zap_tabl_komplektovki()
        return

    def delete_fio(self):
        self.statusBar().showMessage(self.ui.tableWidget_spispk_nar_dla_korrect.currentItem().text())
        i = self.ui.tableWidget_spispk_nar_dla_korrect.currentRow()
        Nom_nar = self.ui.tableWidget_spispk_nar_dla_korrect.item(i, 0).text()
        fio1 = ''
        fio2 = ''
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        for i in range(0, len(Stroki_nar)):
            if Stroki_nar[i][0] == Nom_nar:
                fio1 = Stroki_nar[i][17]
                fio2 = Stroki_nar[i][18]
                Stroki_nar[i][17] = ''
                Stroki_nar[i][18] = ''

                nom_mk = Stroki_nar[i][1]
                id_dse = Stroki_nar[i][25]
                nom_op = Stroki_nar[i][24]
                break
        F.zap_f(F.tcfg('Naryad'), Stroki_nar, '|')
        self.showDialog('ФИО в наряде ' + Nom_nar + ' удалены: ' + fio1 + '; '+ fio2)
        self.zap_tabl_vibor_nar_dlya_imen()
        self.zap_prosm_nar()
        self.zapis_v_mk(nom_op, id_dse,str(nom_mk))
        self.vibor_mk()
        self.zap_tabl_komplektovki()
        return

    def zap_prosm_nar(self):
        option_vse = self.ui.radioButton_vse
        option_ne_nachatie =self.ui.radioButton_ne_nachatie
        option_nachati =self.ui.radioButton_nachatie
        option_zavershonnie =self.ui.radioButton_zavershonnie
        self.ui.tableWidget_spispk_nar_dla_korrect.clear()
        if option_vse.isChecked() == True:
            self.corr_vse()
        elif option_ne_nachatie.isChecked() == True:
            self.corr_ne_nach()
        elif option_nachati.isChecked() == True:
            self.corr_nach()
        elif option_zavershonnie.isChecked() == True:
            self.corr_zavershonnie()


    def corr_vse(self):
        if self.windowTitle() == "Создание нарядов":
            return
        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
        ogr_shir = int(cfg['ogran_shir'])
        filtr_col = {0, 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 21}
        iskl_slov = {}
        self.zapoln_tabl(Stroki, self.ui.tableWidget_spispk_nar_dla_korrect, filtr_col, {}, [], iskl_slov, ogr_shir,True)
        self.ui.pushButton_primen_correctirovky.setEnabled(False)
        self.ui.pushButton_primen_corr_fio.setEnabled(False)

    def corr_nach(self):
        if self.windowTitle() == "Создание нарядов":
            return
        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
        ogr_shir = int(cfg['ogran_shir'])
        filtr_col = {0, 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 21}
        iskl_slov = {}
        with open(cfg['BDzhurnal'] + '\\BDzhurnal.txt', 'r') as f:
            Stroki_BDj = f.readlines()

        Set_nar = set()
        for item in Stroki:
            arr = item.split("|")
            Set_nar.add(arr[0])
        Set_zh = set()
        Set_zh.add("№")
        Set_zh_zav = set()
        for item in Stroki_BDj:
            arr = item.split("|")
            Set_zh.add(arr[2])
            if arr[7] == "Завершен":
                Set_zh_zav.add(arr[2])

        Set_zh= Set_zh-Set_zh_zav

        Set_nar = Set_zh
        Stroki_temp = Stroki.copy()
        for i in Stroki_temp:
            arr = i.split("|")
            if arr[0] not in Set_nar:
                Stroki.remove(i)
        Stroki_temp.clear()


        self.zapoln_tabl(Stroki, self.ui.tableWidget_spispk_nar_dla_korrect, filtr_col, {}, [], iskl_slov, ogr_shir,True)
        self.ui.pushButton_primen_correctirovky.setEnabled(False)
        self.ui.pushButton_primen_corr_fio.setEnabled(True)



    def corr_ne_nach(self):
        if self.windowTitle() == "Создание нарядов":
            return
        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
        ogr_shir = int(cfg['ogran_shir'])
        filtr_col = {0, 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 21}
        iskl_slov = {}

        with open(cfg['BDzhurnal'] + '\\BDzhurnal.txt', 'r') as f:
            Stroki_BDj = f.readlines()

        Set_nar = set()
        for item in Stroki:
            arr = item.split("|")
            Set_nar.add(arr[0])
        Set_zh = set()
        for item in Stroki_BDj:
            if item.count('|') < 8:
                self.showDialog('Некорректная строка ' + item + ' в BDzhurnal.txt')
                exit()
            arr = item.split("|")
            Set_zh.add(arr[2])

        Set_nar = Set_nar - Set_zh
        Stroki_temp = Stroki.copy()
        for i in Stroki_temp:
            arr = i.split("|")
            if arr[0] not in Set_nar:
                Stroki.remove(i)
        Stroki_temp.clear()

        self.zapoln_tabl(Stroki, self.ui.tableWidget_spispk_nar_dla_korrect, filtr_col, {}, [], iskl_slov, ogr_shir,True)
        self.ui.pushButton_primen_correctirovky.setEnabled(True)
        self.ui.pushButton_primen_corr_fio.setEnabled(True)

    def corr_zavershonnie(self):
        if self.windowTitle() == "Создание нарядов":
            return
        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
        ogr_shir = int(cfg['ogran_shir'])
        filtr_col = {0, 2, 3, 4, 6, 7, 8, 11, 12, 13, 14, 15, 17, 18, 21}
        iskl_slov = {}
        with open(cfg['BDzhurnal'] + '\\BDzhurnal.txt', 'r') as f:
            Stroki_BDj = f.readlines()

        Set_nar = set()
        for item in Stroki:
            arr = item.split("|")
            Set_nar.add(arr[0])
        Set_zh_zav = set()
        Set_zh_zav.add("№")
        for item in Stroki_BDj:
            arr = item.split("|")
            if arr[7] == "Завершен":
                Set_zh_zav.add(arr[2])

        Set_nar = Set_zh_zav
        Stroki_temp = Stroki.copy()
        for i in Stroki_temp:
            arr = i.split("|")
            if arr[0] not in Set_nar:
                Stroki.remove(i)
        Stroki_temp.clear()

        self.zapoln_tabl(Stroki, self.ui.tableWidget_spispk_nar_dla_korrect, filtr_col, {}, [], iskl_slov,ogr_shir, True)
        self.ui.pushButton_primen_correctirovky.setEnabled(False)
        self.ui.pushButton_primen_corr_fio.setEnabled(False)


    def prim_opovesh(self):
        body = self.ui.plainTextEdit_opovesh.toPlainText()
        arr = body.split('\n')
        with open(cfg['Opovesh'] + '\\Opovesh.txt', 'w') as f:
            for item in arr:
                f.write(item + '\n')
        self.showDialog('Обновлено')

    def prof_ispolnit(self,fio):
        sp_emp = F.otkr_f(F.tcfg('employee'),True,',')
        if sp_emp == ['']:
            self.showDialog('Не найден employee')
            return
        sp_bd_prof = F.otkr_f(F.scfg('bd_prof') + os.sep + 'bd_prof.txt',False,"|")
        if sp_bd_prof == ['']:
            self.showDialog('Не найден sp_bd_prof')
            return
        doljn_emp= ''
        for i in range(len(sp_emp)):
            fio_temp = " ".join(sp_emp[i])
            if fio == fio_temp:
                doljn_emp = sp_emp[i][3]
                break
        if doljn_emp == '':
            return None
        for i in range(len(sp_bd_prof)):
            if doljn_emp == sp_bd_prof[i][1]:
                return sp_bd_prof[i][0]
        return False

    def prof_po_bd(self,kod):
        sp_bd_prof = F.otkr_f(F.scfg('bd_prof') + os.sep + 'bd_prof.txt', False, "|")
        if sp_bd_prof == ['']:
            self.showDialog('Не найден sp_bd_prof')
            return
        for i in range(len(sp_bd_prof)):
            if kod == sp_bd_prof[i][0]:
                return sp_bd_prof[i][1]
        return None

    def prof_po_kod(self,kod):
        sp_bd_prof = F.otkr_f(F.scfg('bd_prof') + os.sep + 'bd_prof.txt', False, "|")
        if sp_bd_prof == ['']:
            self.showDialog('Не найден sp_bd_prof')
            return
        prof = F.naiti_v_spis_1_1(sp_bd_prof,0,kod,1)
        return prof

    def kod_po_prof(self, prof):
        sp_bd_prof = F.otkr_f(F.scfg('bd_prof') + os.sep + 'bd_prof.txt', False, "|")
        if sp_bd_prof == ['']:
            self.showDialog('Не найден sp_bd_prof')
            return
        kod = F.naiti_v_spis_1_1(sp_bd_prof, 1, prof, 0)
        return kod

    def primenit_imena(self):
        tabl_vib_nar = self.ui.tableWidget_vibor_nar_dlya_imen
        label_isp1 = self.ui.label_12_ispoln1
        label_isp2 = self.ui.label_13_ispoln2
        if self.windowTitle() == "Создание нарядов":
            return
        if self.ui.label_12_ispoln1.text() == '' and self.ui.label_13_ispoln2.text() == '':
            self.showDialog('Не выбраны имена')
            return
        if self.ui.label_10_vibr_nar.text() == '':
            self.showDialog('Не выбран наряд')
            return
        Stroki_nar = F.otkr_f(F.scfg('Naryad') + os.sep + 'Naryad.txt',False,'|')
        nom_nar = tabl_vib_nar.item(tabl_vib_nar.currentRow(), 0).text()
        nom_prof_nar = F.naiti_v_spis_1_1(Stroki_nar,0,nom_nar,26)
        kol_rab = int(F.naiti_v_spis_1_1(Stroki_nar, 0, nom_nar, 27))

        ima1 = label_isp1.text().replace('  ',' ')
        ima2 = label_isp2.text().replace('  ',' ')
        kol_rab_vib = 0
        if ima1 != "":
            kol_rab_vib += 1
        if ima2 != "" and ima2 != ima1:
            kol_rab_vib += 1
        if kol_rab != kol_rab_vib:
            self.showDialog('Количество работников должно быть ' + kol_rab )
            return
        if ima1 != '':
            nomer_porof_po_isp = self.prof_ispolnit(ima1)
            if nomer_porof_po_isp == False:
                self.showDialog('Не найден в sp_bd_prof')
                return
            if nomer_porof_po_isp == None:
                self.showDialog('Не найден в sp_emp')
                return
            if nom_prof_nar != nomer_porof_po_isp:
                ima_prof_po_bd = self.prof_po_bd(nom_prof_nar)
                if ima_prof_po_bd == None:
                    ima_prof_po_bd = 'другой'
                self.showDialog('Профессия ' + ima1 + ' должна быть ' + ima_prof_po_bd)
                return
        if ima2 != '':
            nomer_porof_po_isp = self.prof_ispolnit(ima2)
            if nomer_porof_po_isp == False:
                self.showDialog('Не найден в sp_bd_prof')
                return
            if nomer_porof_po_isp == None:
                self.showDialog('Не найден в sp_emp')
                return
            if nom_prof_nar != nomer_porof_po_isp:
                ima_prof_po_bd = self.prof_po_bd(nom_prof_nar)
                self.showDialog('Профессия ' + ima2 + ' должна быть ' + ima_prof_po_bd)
                return
        tmp_strok = tabl_vib_nar.currentRow()
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        for i in range(0, len(Stroki_nar)):
            if Stroki_nar[i][0] == self.ui.label_10_vibr_nar.text():
                Stroki_nar[i][17] = self.ui.label_12_ispoln1.text()
                Stroki_nar[i][18] = self.ui.label_13_ispoln2.text()
                nom_mk = Stroki_nar[i][1]
                id_dse = Stroki_nar[i][25]
                nom_op = Stroki_nar[i][24]
                break
        F.zap_f(F.tcfg('Naryad'), Stroki_nar, '|')
        self.zap_prosm_nar()
        self.zap_tabl_vibor_imeni_sla_nar()
        self.zap_tabl_vibor_nar_dlya_imen()
        self.zap_tabl_komplektovki()
        self.zapis_v_mk(nom_op, id_dse, str(nom_mk))
        self.vibor_mk()
        self.ui.label_10_vibr_nar.setText("-----")
        tabl_vib_nar.selectRow(tmp_strok)
        self.showDialog('Наряд ' + nom_nar + ' выдан на ' + ima1 + ' ' + ima2)
        self.tabl_vibor_nar_dla_imen()

    def obnovit_progress_imena(self):
        rows = self.ui.tableWidget_vibor_imeni_sla_nar.rowCount()
        cols = self.ui.tableWidget_vibor_imeni_sla_nar.columnCount()
        spisok_chasov = []
        max_summ = 0
        for st in range(0,rows):
            ima = self.ui.tableWidget_vibor_imeni_sla_nar.item(st,0).text()
            summ = FCN.summ_chasov_po_imeni(ima)
            if max_summ < summ:
                max_summ = summ
            spisok_chasov.append(summ)

        for item in range(0, len(spisok_chasov)):
            # Создаем QProgressBar
            progress = QtWidgets.QProgressBar()
            progress.setMinimum(0)
            progress.setMaximum(int(max_summ))

            # Формат вывода: 10.50%

            progress.setValue(int(spisok_chasov[item]))
            progress.setFormat('%v')
            progress.setTextVisible(False)
            #cellinfo2 = QtWidgets.QTableWidgetItem(spisok_chasov[item])
            #self.ui.tableWidget_vibor_imeni_sla_nar.setItem(item, 0, cellinfo2)
            # Добавляем виджет в ячейку.
            self.ui.tableWidget_vibor_imeni_sla_nar.setCellWidget(item, 2, progress)
            s = str(spisok_chasov[item])
            chislo = ' '*(4-len(s)) + s
            cellinfo = QtWidgets.QTableWidgetItem(chislo)
            self.ui.tableWidget_vibor_imeni_sla_nar.setItem(item, 1, cellinfo)
        self.ui.tableWidget_vibor_imeni_sla_nar.resizeColumnsToContents()
        self.ui.tableWidget_vibor_imeni_sla_nar.setColumnWidth(2, self.width() -\
        self.ui.tableWidget_vibor_imeni_sla_nar.columnWidth(0) - self.ui.tableWidget_vibor_imeni_sla_nar.columnWidth(1) - 65)
        self.ui.tableWidget_vibor_imeni_sla_nar.setHorizontalHeaderLabels(
            ('ФИО', 'Час.','Загрузка')
        )

        return


    def tabl_vibor_nar_dla_imen(self):
        if self.ui.tableWidget_vibor_nar_dlya_imen.currentItem() != None:
            self.statusBar().showMessage(self.ui.tableWidget_vibor_nar_dlya_imen.currentItem().text())
            i = self.ui.tableWidget_vibor_nar_dlya_imen.currentRow()
            self.ui.label_10_vibr_nar.setText(self.ui.tableWidget_vibor_nar_dlya_imen.item(i, 0).text())
        self.ui.label_12_ispoln1.clear()
        self.ui.label_13_ispoln2.clear()

    def tabl_vibor_fio_dla_imen(self):
        self.statusBar().showMessage(self.ui.tableWidget_vibor_imeni_sla_nar.currentItem().text())
        i = self.ui.tableWidget_vibor_imeni_sla_nar.currentRow()
        if self.ui.radioButton_ispoln1.isChecked():
            self.ui.label_12_ispoln1.setText(self.ui.tableWidget_vibor_imeni_sla_nar.item(i, 0).text())
        else:
            self.ui.label_13_ispoln2.setText(self.ui.tableWidget_vibor_imeni_sla_nar.item(i, 0).text())

    def zap_tabl_vibor_nar_dlya_imen(self):
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'),False,'|')
        for i in range(1,len(Stroki_nar)):
            if len(Stroki_nar[i]) >27:
                Stroki_nar[i][26] = self.prof_po_kod(Stroki_nar[i][26])
        filtr_col = {0,2,3,4,7,11,12,13,14,16,26,27}
        ogr_shir = int(cfg['ogran_shir'])
        iskl_slov = {16: "", 17: "*", 18: "*"}
        F.zapoln_wtabl(self,Stroki_nar,self.ui.tableWidget_vibor_nar_dlya_imen,filtr_col,0,'', iskl_slov,ogr_shir,True,'')

    def zap_tabl_vibor_imeni_sla_nar(self):
        with open(cfg['employee'] + '\\employee.txt', 'r', encoding='utf-8') as f:
            Stroki = f.readlines()
        with open(cfg['Filtr_rab'] + '\\Filtr_rab.txt', 'r') as f:
            Stroki_emp = f.readlines()
        Stroki_temp = []
        for line in Stroki:
            line = line.replace(',', '  ')
            line = line.replace('\n', '')
            if FCN.etap_po_fio(line, Stroki_emp) != "":
                line = line.encode('cp1251', errors='ignore').decode('cp1251')
                Stroki_temp.append(line)
        Stroki_temp2 = Stroki_temp.copy()
        with open(cfg['FiltrEmpDel'] + '\\FiltrEmpDel.txt', 'r') as f:
            Stroki_FiltrEmpDel = f.readlines()
        for item in Stroki_temp2:
            for iskl in Stroki_FiltrEmpDel:
                if iskl.strip() in item:
                    Stroki_temp.remove(item)
                    break
        Stroki_temp2.clear()
        filtr_col = {0, 1, 2}
        iskl_slov = {}
        self.zapoln_tabl(Stroki_temp, self.ui.tableWidget_vibor_imeni_sla_nar, filtr_col, {}, [], iskl_slov, 1500)
        self.obnovit_progress_imena()

    def zap_TextEdit_opovesh(self):
        with open(cfg['Opovesh'] + '\\Opovesh.txt', 'r') as f:
            Stroki_opov = f.readlines()
        body = "".join(Stroki_opov)
        self.ui.plainTextEdit_opovesh.setPlainText(body)

    def zap_tabl_komplektovki(self):
        Stroki_nar = F.otkr_f(F.tcfg('Naryad'), False, '|')
        filtr_col = {0, 3, 4, 11, 12, 14, 15, 16, 17, 18}
        iskl_slov = {17: "*", 18: "*"}
        F.zapoln_wtabl(self,Stroki_nar,self.ui.tableWidget_tabl_komplektovki,filtr_col,0,'', iskl_slov,200,True,'')
        #self.zapoln_tabl(Stroki_nar, self.ui.tableWidget_tabl_komplektovki, filtr_col, {}, [], iskl_slov, 500, True)



    def max_det_skompl(self,nom_op,id_dse):
        tabl_mk = self.ui.tableWidget_vibor_det
        for j in range(tabl_mk.rowCount()):
            if tabl_mk.item(j,6).text() == id_dse:
                for i in range(11,tabl_mk.columnCount(),4):
                    if tabl_mk.item(j, i).text().strip() != '':
                        obr = tabl_mk.item(j, i).text().strip().split('Операции:\n')
                        obr2 = obr[-1].split(";")
                        if str(nom_op) in obr2:
                            if tabl_mk.item(j, i+1).text().strip() == '':
                                return 0
                            kompl = tabl_mk.item(j, i+1).text().strip().split(' шт.')
                            return int(kompl[0])


    def summ_dost_det_po_nar(self,nom_mar,id_dse,nom_op,zakr=False):
        tabl_mk = self.ui.tableWidget_vibor_det
        sp_nar = F.otkr_f(F.tcfg('Naryad'),False,'|')
        sp_zhur = F.otkr_f(F.tcfg('BDzhurnal'),False,'|')
        if sp_nar == ['']:
            self.showDialog('Не найдена база с нарядами')
            return
        max_det = self.max_det_skompl(nom_op,id_dse)
        summ_det = 0
        for i in range(len(sp_nar)):
            if sp_nar[i][1] == nom_mar and sp_nar[i][25] == id_dse and sp_nar[i][24] == nom_op and sp_nar[i][21] == '':
                if zakr == True:
                    mn = []
                    flag = 1
                    for j in range(len(sp_zhur)):
                        if sp_zhur[j][2] == sp_nar[i][0]:
                            mn.append(sp_zhur[j][3])
                    if len(mn) > 0:
                        mn = set(mn)
                        mn = list(mn)
                        for j in range(len(sp_zhur)):
                            if sp_zhur[j][2] == sp_nar[i][0] and sp_zhur[j][7] == 'Завершен':
                                if sp_zhur[j][3] in mn:
                                    mn.remove(sp_zhur[j][3])
                            if len(mn) == 0:
                                flag = 0
                                break
                        if flag == 0:
                            summ_det+= F.valm(sp_nar[i][12].strip())
                else:
                    summ_det += F.valm(sp_nar[i][12].strip())
        if max_det - summ_det < 0:
            return 0
        return max_det - summ_det



    def sozd_naryad(self):
        tabl_mk = self.ui.tableWidget_vibor_det
        tabl_sp_oper = self.ui.tableWidget_vibor_oper
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        line_kolvo = self.ui.lineEdit_cr_nar_kolvo
        chek_vneplan = self.ui.checkBox_vneplan_rab
        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()

        nom_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(), 1).text().strip()
        kr_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(), 7).text().strip()
        koid_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(), 9).text().strip()
        id_dse = tabl_mk.item(tabl_mk.currentRow(), 6).text()

        if self.windowTitle() == "Создание нарядов":
            return
        if self.ui.checkBox_vecher.checkState() == 1:
            self.Migat(3, self.ui.checkBox_vecher, "Не указан тип")
            return
        if self.ui.lineEdit_cr_nar_kolvo.text() == "":
            self.Migat(3,self.ui.lineEdit_cr_nar_kolvo ,"Не заполнено количество")
            return
        if F.is_numeric(self.ui.lineEdit_cr_nar_kolvo.text().strip()) == False:
            self.Migat(3,self.ui.lineEdit_cr_nar_kolvo ,"Количество должно быть числом")
            return

        kol = int(line_kolvo.text().strip())
        vneplan = 'Внеплана'
        if chek_vneplan.checkState() == 0:
            vneplan = ''
            if kol == 0:
                self.showDialog('Количество не может быть 0')
                return
            if kol > self.summ_dost_det_po_nar(nom_mk, id_dse, nom_op):
                self.showDialog('Кол-во деталей превышет допустимое')
                return
            else:
                if tabl_sp_oper.currentRow() > 0:
                    for i in range(tabl_sp_oper.currentRow() - 1, -1, -1):
                        if tabl_sp_oper.item(i, 12).text().strip() != '2':
                            break
                    nom_op_p = tabl_sp_oper.item(i, 1).text().strip()
                    if self.zaversh_nar_po_pred_op(nom_mk, id_dse, nom_op_p) == False:
                        self.showDialog('Наряды по предыдущей операции еще не закрыты в полном обьеме')
                        return

        if self.ui.lineEdit_cr_nar_nom_proect.text() == "":
            self.Migat(3,self.ui.lineEdit_cr_nar_nom_proect ,"Не заполнен номер проекта")
            return
        if self.ui.lineEdit_cr_nar_nomerPU.text() == "":
            self.Migat(3,self.ui.lineEdit_cr_nar_nomerPU ,"Не заполнено номер заявки")
            return
        if self.ui.lineEdit_cr_nar_norma.text() == "":
            self.Migat(3, self.ui.lineEdit_cr_nar_norma, "Не заполнена норма времени")
            return
        self.ui.lineEdit_cr_nar_norma.setText(str(float(self.ui.lineEdit_cr_nar_norma.text().replace(',', '.'))))
        if float(self.ui.lineEdit_cr_nar_norma.text()) == 0:
            self.Migat(3, self.ui.lineEdit_cr_nar_norma, "Норма не может быть 0")
            return
        if FCN.is_digit(self.ui.lineEdit_cr_nar_norma.text()) == False:
            self.Migat(3, self.ui.lineEdit_cr_nar_norma, "Введено не число")
            return
        if self.ui.lineEdit_cr_nar_pozicii.text() == "":
            self.Migat(3,self.ui.lineEdit_cr_nar_pozicii ,"Не заполнены позиции")
            return
        if self.ui.comboBox_cr_nar_etap.currentText() == "":
            self.Migat(3,self.ui.comboBox_cr_nar_etap ,"Не выбран этап")
            return
        if self.ui.plainTextEdit_zadanie.toPlainText() == "":
            self.Migat(3,self.ui.plainTextEdit_zadanie ,"Не описано задание")
            return

        if ' ' in self.ui.lineEdit_cr_nar_pozicii.text():
            self.ui.lineEdit_cr_nar_pozicii.setText(self.ui.lineEdit_cr_nar_pozicii.text().strip())
            self.ui.lineEdit_cr_nar_pozicii.setText(self.ui.lineEdit_cr_nar_pozicii.text().replace('   ', ' '))
            self.ui.lineEdit_cr_nar_pozicii.setText(self.ui.lineEdit_cr_nar_pozicii.text().replace('  ', ' '))
            self.ui.lineEdit_cr_nar_pozicii.setText(self.ui.lineEdit_cr_nar_pozicii.text().replace(' ', ','))
            self.Migat(3, self.ui.lineEdit_cr_nar_pozicii, "Позиции указать через заяптую, исправлено.")
            return
        if self.ui.checkBox.checkState() == 1:
            self.Migat(3, self.ui.checkBox, "Не выбрано состояние")
            return
        nom_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(),1).text().strip()
        primechanie = ''
        for i in range(11, tabl_mk.columnCount(),4):
            if nom_op in tabl_mk.item(tabl_mk.currentRow(),i).text() and 'Операции' in tabl_mk.item(tabl_mk.currentRow(),i).text():
                primechanie = tabl_mk.item(tabl_mk.currentRow(),i+3).text()
                break
        if "Акт №" in primechanie and " по наряду №" in primechanie:
            primechanie = primechanie + ' '
        else:
            primechanie = ''

        sv_ur = ''


        with open(cfg['Naryad'] + '\\Naryad.txt', 'r') as f:
            Stroki = f.readlines()
        arr_item = [x.strip() for x in Stroki[-1].split("|")]
        nom = int(arr_item[0]) + 1
        if self.ui.checkBox.checkState() == 2:
            vid_narad = 'Последний'
        else:
            vid_narad = ''

        if self.ui.checkBox_vecher.checkState() == 2:
            tip_narad = 'Вечерка'
        else:
            tip_narad = 'День'
        nom_mk = tabl_sp_mk.item(tabl_sp_mk.currentRow(), 0).text()
        nom_pu = tabl_sp_mk.item(tabl_sp_mk.currentRow(),4).text()
        nom_pr = tabl_sp_mk.item(tabl_sp_mk.currentRow(),5).text()
        nom_op = tabl_sp_oper.item(tabl_sp_oper.currentRow(),1).text().strip()
        kod_prof = tabl_sp_oper.item(tabl_sp_oper.currentRow(), 6).text().strip()
        ves_det = F.valm(tabl_mk.item(tabl_mk.currentRow(),8).text()) * kol
        ves_det = round(ves_det,1)
        sp_BD_Proect = F.otkr_f(F.tcfg('BD_Proect'),False,'|')

        vid_pr = F.naiti_v_spis_2_1(sp_BD_Proect,1,nom_pu,0,nom_pr,2)

        id_dse = tabl_mk.item(tabl_mk.currentRow(),6).text()


        Stroki.append(str(nom) + "|" + str(nom_mk) + "|" + DT.today().strftime("%d.%m.%Y %H:%M:%S") + '|' +\
                      self.ui.lineEdit_cr_nar_nom_proect.text() + "$" +  self.ui.lineEdit_cr_nar_nomerPU.text() + \
                      "|" + primechanie + self.ui.plainTextEdit_zadanie.toPlainText().strip().replace('\n','{') +\
                      '|' + self.ui.lineEdit_cr_nar_norma.text() + \
                      '|' + sv_ur + '|' + self.windowTitle() + '|' + vid_narad + '|' + tip_narad + '|' + str(ves_det) + '|' + vid_pr +  \
                      '|' + self.ui.lineEdit_cr_nar_kolvo.text() + \
                      '|' + self.ui.lineEdit_cr_nar_pozicii.text() + '|' + self.ui.comboBox_cr_nar_etap.currentText() + \
                      '|||||||' + vneplan + '|||' + nom_op + '|' + id_dse + '|' + kod_prof + '|' + kr_op + '|' + koid_op + '|' + "\n")
        with open(cfg['Naryad'] + '\\Naryad.txt', 'w') as f:
            for item in Stroki:
                f.write(item)

        self.ui.lineEdit_cr_nar_kolvo.clear()
        self.ui.lineEdit_cr_nar_nom_proect.clear()
        self.ui.lineEdit_cr_nar_nomerPU.clear()
        self.ui.lineEdit_cr_nar_norma.clear()
        self.ui.lineEdit_cr_nar_pozicii.clear()
        self.ui.comboBox_cr_nar_etap.setCurrentIndex(0)
        self.ui.plainTextEdit_zadanie.clear()
        self.ui.checkBox.setCheckState(1)
        old_ind = tabl_mk.currentRow()
        self.zapis_v_mk(nom_op,id_dse,str(nom_mk))
        self.vibor_mk(old_ind)
        self.zap_prosm_nar()
        self.zap_tabl_komplektovki()
        self.ui.tabWidget_2.setCurrentIndex(1)
        self.showDialog('Безымянный наряд №' + str(nom) + " создан.")


    def zaversh_nar_po_pred_op(self, nom_mk, id_dse, nom_op_p):
        if F.nalich_file(F.scfg('mk_data') + os.sep + nom_mk + '.txt') == False:
            self.showDialog('Не обнаружен файл')
            return
        sp_tabl_mk  = F.otkr_f(F.scfg('mk_data') + os.sep + nom_mk + '.txt',False,'|')
        if sp_tabl_mk  == []:
            self.showDialog('Некорректное содержимое МК')
            return
        stroka = F.naiti_v_spis_1_1(sp_tabl_mk,6,id_dse)
        for i in range(11,len(sp_tabl_mk[stroka]),4):
            tmp = sp_tabl_mk[stroka][i].split('$')
            if nom_op_p in tmp[-1]:
                spis_nar = sp_tabl_mk[stroka][i+2].split('$')
                if spis_nar[0] == 'Полный компл.':
                    return True
        return False


    def spis_nar_po_mk_id_op(self,mk,id,spis_op):
        sp = []
        nar = F.otkr_f(F.tcfg('Naryad'),False,'|')
        for i in range(1,len(nar)):
            if nar[i][1].strip() == str(mk) and nar[i][25].strip() == str(id) and nar[i][24].strip() in spis_op:
                sost = 'Создан'
                if nar[i][17].strip() != '' or nar[i][18].strip() != '':
                    sost = 'Выдан'
                    sp_jur = F.otkr_f(F.tcfg('BDzhurnal'),False,'|')
                    fam = set()
                    for j in range(len(sp_jur)):
                        if sp_jur[j][2] == nar[i][0]:
                            fam.add(sp_jur[j][3])
                    fam = list(fam)
                    if len(fam) != 0:
                        sost = 'Начат'
                        for j in range(len(sp_jur)):
                            if sp_jur[j][2] == nar[i][0] and sp_jur[j][7] == 'Завершен':
                                fam.remove(sp_jur[j][3])
                                if len(fam) == 0:
                                    sost = 'Завершен'
                                    break
                sp.append(nar[i][0] + ' ' + sost)
        return sp
    
    def otmetka_v_mk(self,nom,spis_op,sp_nar,id,sp_tabl_mk):
        for j in range(1,len(sp_tabl_mk)):
            if sp_tabl_mk[j][6]==id:
                for i in range(11, len(sp_tabl_mk[0]), 4):
                    if sp_tabl_mk[j][i].strip() != '':
                        obr = sp_tabl_mk[j][i].strip().split('$')
                        obr2 = obr[-1].split(";")
                        if spis_op == obr2:
                            text = '$'.join(sp_nar)
                            sp_tabl_mk[j][i+2] = text
                            F.zap_f(F.scfg('mk_data') + os.sep + nom + '.txt',sp_tabl_mk,'|')
                            return

    def spis_op_po_mk_id_op(self,sp_tabl_mk,id,op):
        for j in range(1, len(sp_tabl_mk)):
            if sp_tabl_mk[j][6] == id:
                for i in range(11, len(sp_tabl_mk[0]), 4):
                    if sp_tabl_mk[j][i].strip() != '':
                        obr = sp_tabl_mk[j][i].strip().split('$')
                        obr2 = obr[-1].split(";")
                        if op in obr2:
                            return obr2
                return None

    def zapis_v_mk(self,nom_op, id_dse,nom_mk):
        id_det = id_dse
        n_op = nom_op
        if F.nalich_file(F.scfg('mk_data') + os.sep + nom_mk + '.txt') == False:
            self.showDialog('Не обнаружен файл')
            return
        sp_tabl_mk  = F.otkr_f(F.scfg('mk_data') + os.sep + nom_mk + '.txt',False,'|')
        if sp_tabl_mk  == []:
            self.showDialog('Некорректное содержимое МК')
            return
        spis_op = self.spis_op_po_mk_id_op(sp_tabl_mk,id_det,n_op)
        if spis_op == None:
            self.showDialog('Некорректное содержимое списка операций')
            return
        spis_nar_mk = self.spis_nar_po_mk_id_op(nom_mk,id_det,spis_op)
        self.otmetka_v_mk(nom_mk,spis_op, spis_nar_mk, id_det,sp_tabl_mk)



    def Migat(self, chislo, widhet, msg, koef=0.3):
        self.showDialog(msg)
        tepm2 = widhet.font().pointSize()
        tepm3 = widhet.font().styleName()
        tepm = widhet.styleSheet() + ";font: " + str(tepm2) + "pt " + tepm3

        for i in range(0,chislo):
            widhet.setStyleSheet("background-color: rgb(255, 144, 144)")
            time.sleep(koef)
            application.repaint()
            widhet.setStyleSheet(tepm)
            time.sleep(koef)
            application.repaint()
        return

    def logout(self):
        if self.windowTitle() == 'Создание нарядов':
            return
        self.setWindowTitle("Создание нарядов")
        self.ui.lineEdit_Nparol.setVisible(False)
        self.ui.lineEdit_Nparol2.setVisible(False)
        #self.ui.tableWidget_vibpr_proekta.clear()
        self.ui.lineEdit_cr_nar_kolvo.clear()
        self.ui.lineEdit_cr_nar_nom_proect.clear()
        self.ui.lineEdit_cr_nar_nomerPU.clear()
        self.ui.lineEdit_cr_nar_norma.clear()
        self.ui.lineEdit_cr_nar_pozicii.clear()
        self.ui.lineEdit_parol.clear()
        self.ui.comboBox_cr_nar_etap.setCurrentIndex(0)
        self.ui.comboBox_spis_users.setCurrentIndex(0)
        self.ui.plainTextEdit_zadanie.clear()
        self.ui.checkBox.setCheckState(1)
        self.ui.tableWidget_vibor_imeni_sla_nar.clear()
        self.ui.tableWidget_vibor_nar_dlya_imen.clear()
        self.ui.label_12_ispoln1.clear()
        self.ui.label_13_ispoln2.clear()
        self.ui.label_10_vibr_nar.clear()
        self.ui.tableWidget_spispk_nar_dla_korrect.clear()
        self.ui.pushButton_primen_correctirovky.setEnabled(False)
        return

    def Smena_Parol(self):
        if self.windowTitle() == "Создание нарядов":
            return
        if self.ui.lineEdit_Nparol.isVisible() == False:
            self.showDialog("Введи старый и новый пароль, потом еще раз через меню - сменить пароль")
            self.ui.lineEdit_Nparol.setVisible(True)
            self.ui.lineEdit_Nparol2.setVisible(True)
            return
        ima = self.windowTitle()
        ima = ima.replace('  ', ',')

        parol = FCN.Podtv_lich_parol(ima, self.ui.lineEdit_parol.text())
        if parol == None:
            self.showDialog("Не найден пользователь")
            return
        if parol == False:
            self.showDialog("Не верный пароль")
            self.ui.lineEdit_parol.clear()
            return
        if self.ui.lineEdit_Nparol.text() != self.ui.lineEdit_Nparol2.text():
            self.showDialog("Не совпадают новые пароли")
            return
        with open(cfg['Riba'] + '\\Riba.txt', 'r') as f:
            Stroki = f.readlines()
            flag_naid = 0
        for N_line in range(0, len(Stroki)):
            if FCN.shifr(ima.strip()) in Stroki[N_line].strip():
                flag_naid = 1
                Stroki[N_line] = FCN.shifr(ima.strip()) + '|' + FCN.shifr(self.ui.lineEdit_Nparol.text()) + '\n'
                break
        if flag_naid == 1:
            with open(cfg['Riba'] + '\\Riba.txt', 'w') as f:
                for item in Stroki:
                    f.write(item)
            self.ui.lineEdit_parol.setText('')
            self.ui.lineEdit_Nparol.setText('')
            self.ui.lineEdit_Nparol2.setText('')
            self.ui.lineEdit_Nparol.setVisible(False)
            self.ui.lineEdit_Nparol2.setVisible(False)
            self.setWindowTitle("Создание нарядов")
            self.showDialog("Пароль изменен, войди еще раз по новому паролю")
        else:
            self.showDialog("Не найден пользователь")
        return

    def log_in(self):
        if self.ui.lineEdit_parol.text() == "":
            return
        if self.windowTitle() != "Создание нарядов":
            self.showDialog('Нужно сначала выйти')
            return
        ima = self.ui.comboBox_spis_users.currentText()
        ima = ima.replace('  ', ',')
        parol = FCN.Podtv_lich_parol(ima, self.ui.lineEdit_parol.text())
        if parol == None:
            self.showDialog("Не зарегистрирован")
            return
        if parol == True:
            self.setWindowTitle(self.ui.comboBox_spis_users.currentText())
            self.ui.lineEdit_parol.clear()

        else:
            self.showDialog("Не верный пароль")
            self.ui.lineEdit_parol.clear()
            return

        self.zapoln_tabl_mk()
        self.zap_tabl_komplektovki()
        self.zap_tabl_vibor_imeni_sla_nar()
        self.zap_tabl_vibor_nar_dlya_imen()
        self.zap_TextEdit_opovesh()
        #self.tab_click()


    def zapoln_tabl(self, spisok, object, set_filtr_col_nomera, set_editeble_col_nomera, spis_filtr_row_imena = (), slovar_iskl_filtr_row_imena = (), ogr_shir_col = 200, isp_shapka = False):
        object.clear()
        Stroki_filt = list()
        if isp_shapka == True:
            nach = 1
            Stroki_filt.append(spisok[0])
        else:
            nach = 0
        for line in range(nach,len(spisok)) :
            if len(spis_filtr_row_imena) > 0:
                for item in spis_filtr_row_imena:
                    if item in spisok[line]:
                        Stroki_filt.append(spisok[line])
                        break
            else:
                Stroki_filt.append(spisok[line])
        if len(slovar_iskl_filtr_row_imena) > 0:
            nach_l = nach-1
            for line in range(nach,len(Stroki_filt)):
                nach_l +=1
                if Stroki_filt[nach_l].count('|') < 8:
                    self.showDialog('Некорректная строка ' + Stroki_filt[nach_l] + object.objectName())
                    exit()
                arr_line = [x for x in Stroki_filt[nach_l].split('|')]
                for item in slovar_iskl_filtr_row_imena.keys():
                    if slovar_iskl_filtr_row_imena[item] == '':
                        if len(arr_line[item]) == 0:
                            del Stroki_filt[nach_l]
                            nach_l -=1
                            break
                    if slovar_iskl_filtr_row_imena[item] == '*':
                        if len(arr_line[item]) > 0:
                            del Stroki_filt[nach_l]
                            nach_l -=1
                            break

                    if slovar_iskl_filtr_row_imena[item] != "" and slovar_iskl_filtr_row_imena[item] != "*" and \
                            slovar_iskl_filtr_row_imena[item] in arr_line[item]:
                        del Stroki_filt[nach_l]
                        nach_l -= 1
                        break

        isp_kol = set_filtr_col_nomera
        shapka = []
        #object.setColumnCount(FCN.max_kol(Stroki_filt))
        object.setColumnCount(len(isp_kol))
        object.setRowCount(len(Stroki_filt)-1)
        koef_shapka=0
        for line in range(0, len(Stroki_filt)):
            if len(shapka) == 0 and isp_shapka == True:
                koef_shapka=1
                arr_shapka = [x.strip() for x in Stroki_filt[line].split("|")]
                for i in range(0, len(arr_shapka)):
                    if i in isp_kol:
                        shapka.append(arr_shapka[i])
                object.setHorizontalHeaderLabels(shapka)
            else:
                arr_line_temp = [x.strip() for x in Stroki_filt[line].split("|")]
                line_temp =[]
                for i in range(0, len(arr_line_temp)):
                    if i in isp_kol:
                        line_temp.append(arr_line_temp[i])
                for kol in range(0, len(line_temp)):
                    cellinfo = QtWidgets.QTableWidgetItem(line_temp[kol])
                    if kol not in set_editeble_col_nomera:
                        # Только для чтения
                        cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    object.setItem(line-koef_shapka, kol, cellinfo)
        object.resizeColumnsToContents()
        for i in range(0, object.columnCount()+1):
            if object.columnWidth(i) > ogr_shir_col:
                object.setColumnWidth(i,ogr_shir_col)



    def Reg_new_user(self):
        flag_nalich = 0
        ima = self.ui.comboBox_spis_users.currentText()
        ima = ima.replace('  ', ',')
        with open(cfg['Riba'] + '\\Riba.txt', 'r') as f:
            Stroki = f.readlines()
        for line in Stroki:
            if FCN.shifr(ima.strip()) in line.strip():
                flag_nalich = line.strip()
                break
        if flag_nalich != 0:
            New_dannie = "Пользователь уже зарегистрирован " + flag_nalich
            self.showDialog(New_dannie)
            return

        New_dannie = FCN.shifr(self.ui.comboBox_spis_users.currentText().replace('  ', ',')) + "|" + FCN.shifr(DT.today().strftime("%Y")) + '\n'
        Stroki.append(New_dannie)
        with open(cfg['Riba'] + '\\Riba.txt', 'w') as f:
            for line in Stroki:
                f.write(line)
        self.showDialog("Новый пользователь зарегистрирован: " + '\n' + self.ui.comboBox_spis_users.currentText() + '\n' \
                        + FCN.shifr(self.ui.comboBox_spis_users.currentText().replace('  ', ',')))
        return

    def showDialog(self, msg):
        msgBox = QtWidgets.QMessageBox()
        self.modal = 1
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setText(msg)
        msgBox.setWindowTitle("Внимание!")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)  # | QtWidgets.QMessageBox.Cancel)
        msgBox.setWindowModality(QtCore.Qt.WindowModal)
        returnValue = msgBox.exec()
        #self.modal = 0
        # msgBox.buttonClicked.connect(msgButtonClick)
        # if returnValue == QtWidgets.QMessageBox.Ok:
        # print('OK clicked')

app = QtWidgets.QApplication([])


myappid = 'Powerz.BAG.SystCreateWork.1.0.3'                          #  !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons","tab.png")))


S = cfg['Stile'].split(",")
app.setStyle(S[0])
application = mywindow()
application.show()


sys.exit(app.exec())