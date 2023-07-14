import copy

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWinExtras import QtWin
import os
import user_mange as userm
# import subprocess
import project_cust_38.Cust_Qt as CQT
import copy as CPY
CQT.conver_ui_v_py()
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
#import config
import sys
import project_cust_38.Cust_Functions as F
import pprint
import project_cust_38.Cust_mes as CMS
import project_cust_38.Cust_SQLite as CSQ
import project_cust_38.Cust_Excel as CEX
import compare_files as compare
#import traceback


cfg = F.load_cfg(False)  # файл конфига, находится п папке конфиг

#F.test_path()

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.versia = '1.5.3'
        # ===========================================connects
        # ==================BTN
        self.ui.btn_login.clicked.connect(lambda _, x=self: userm.log_in(x))
        self.ui.btn_logout.clicked.connect(lambda _, x=self: userm.logout(x))
        self.ui.btn_create_nar.clicked.connect(self.create_naryd)
        self.ui.btn_select_all.clicked.connect(self.select_all_dse)
        self.ui.btn_invers.clicked.connect(self.select_invers_dse)
        self.ui.btn_unselect_all.clicked.connect(self.unselect_all_dse)
        self.ui.btn_komplect.clicked.connect(self.otmeka_komplekt)
        self.ui.btn_primen_imena.clicked.connect(self.primen_imena)
        self.ui.btn_poz_kol_add.clicked.connect(self.poz_kol_add)
        self.ui.btn_poz_kol_minus.clicked.connect(self.poz_kol_minus)
        self.ui.btn_edit_clear_fio.clicked.connect(self.edit_clear_fio)
        self.ui.btn_edit_delete_naruad.clicked.connect(self.edit_delete_naruad)
        self.ui.btn_edit_check_naruad.clicked.connect(self.edit_check_naruad)
        self.ui.btn_edit_check_vneplan.clicked.connect(self.edit_check_vneplan)
        self.ui.btn_anal_load_txt_erp.clicked.connect(lambda _, x=self: compare.load_txt(x))
        self.ui.btn_anal_load_txt_mes.clicked.connect(lambda _, x=self: compare.load_txt_mes(x))
        self.ui.btn_anal_start.clicked.connect(lambda _, x=self: compare.anal_start(x))
        self.ui.btn_open_zayavky.clicked.connect(self.open_zayavk)
        self.ui.btn_edit_time_jur.clicked.connect(self.edit_time_jur_btn)
        self.ui.btn_prosm_edit_time_clear_fio.clicked.connect(lambda _, x='ФИО': self.btn_prosm_edit_time_clear_fio(x))
        self.ui.btn_prosm_edit_time_clear_fio2.clicked.connect(lambda _, x='ФИО2': self.btn_prosm_edit_time_clear_fio(x))
        self.ui.btn_reload_list_mk.clicked.connect(self.reload_list_mk)
        self.ui.btn_dse_sh_tree.clicked.connect(self.btn_dse_sh_tree)
        self.ui.btn_dse_sh_filtr.clicked.connect(self.btn_dse_sh_filtr)
        self.ui.btn_dse_sh_elems.clicked.connect(self.btn_dse_sh_elems)
        self.ui.btn_dse_info.clicked.connect(self.btn_dse_info)
        # ==================lines
        self.ui.le_Nparol.setVisible(False)
        self.ui.le_Nparol2.setVisible(False)
        # ==================TABLES
        self.ui.tableWidget_vibor_mk.doubleClicked.connect(self.open_papka_chpy)
        self.ui.tableWidget_vibor_mk.clicked.connect(self.tbl_mk_click)
        self.ui.tableWidget_vibor_mk.setSelectionBehavior(0)
        self.ui.tbl_dse.clicked.connect(self.tbl_dse_click)
        self.ui.tbl_dse.itemSelectionChanged.connect(self.tbl_dse_select)
        self.ui.tbl_dse.currentItemChanged.connect(self.raschet_naruada_time_tmp)
        self.ui.tbl_prosmotr_nar.cellChanged[int, int].connect(self.edit_koeff_nar_tbl)
        self.ui.tbl_red_zhur.cellChanged[int, int].connect(self.edit_red_zhur_koef_sl)
        self.ui.tbl_red_zhur.clicked.connect(self.tbl_red_zhur_click)
        self.ui.tbl_dse.doubleClicked.connect(self.tbl_dse_dblclick)
        self.ui.tbl_vibor_nar_rasp.clicked.connect(self.tbl_nar_raspr_click)
        self.ui.tbl_vibor_rabotn_rasp.clicked.connect(self.tbl_rabotn_raspr_click)
        self.ui.tbl_komplektovka.clicked.connect(self.tbl_komplektovka_click)
        self.ui.tbl_komplektovka_view.clicked.connect(self.tbl_komplektovka_view_click)
        self.ui.tbl_prosmotr_nar.clicked.connect(self.tbl_prosmotr_nar_click)
        self.ui.tbl_brak.doubleClicked.connect(self.dblclick_brak)
        self.ui.tbl_prosmotr_nar_jurnal.clicked.connect(self.tbl_prosmotr_nar_jurnal_clk)
        self.ui.tableWidget_vibor_mk.horizontalScrollBar().valueChanged.connect(
            self.ui.tbl_filtr_mk.horizontalScrollBar().setValue)
        self.ui.tbl_dse.horizontalScrollBar().valueChanged.connect(
            self.ui.tbl_filtr_dse.horizontalScrollBar().setValue)
        self.ui.tbl_select_marsh.horizontalScrollBar().valueChanged.connect(
            self.ui.tbl_select_marsh_filtr.horizontalScrollBar().setValue)
        self.ui.tbl_select_marsh.clicked.connect(self.tbl_select_marsh_clk)
        self.ui.tbl_select_marsh.doubleClicked.connect(self.tbl_select_marsh_dblclk)
        # ==================TABS
        self.ui.tabWidget_2.currentChanged[int].connect(self.tab2_clcik)
        self.ui.tabWidget.currentChanged[int].connect(self.tab_clcik)
        # ===================CHECKBOX
        self.ui.checkBox_min_rezhjim.stateChanged[int].connect(self.min_rejim)
        self.ui.checkBox_vneplan_rab.stateChanged[int].connect(self.click_vneplan)
        self.ui.checkBox_full_dse.stateChanged.connect(self.check_box_load_full)
        self.ui.chk_progress.stateChanged.connect(self.zapoln_tabl_mk)
        # ===================COMBOBOX
        self.ui.cmb_prof_rasp.activated[int].connect(self.select_prof_raspr)
        self.ui.cmb_etapi.activated[int].connect(self.select_etap_dse)
        self.ui.cmb_mat.activated[int].connect(self.select_etap_mat)
        self.ui.cmb_prof.activated[int].connect(self.select_prof)
        self.ui.cmb_current_rc.activated[int].connect(self.select_current_rc)
        self.ui.cmb_list_marsh.activated[int].connect(self.select_dse_po_marsh)
        self.ui.cmb_vid_inf_marsh.activated[int].connect(self.fill_tbl_select_marsh)
        # ===================RADIOBOX
        self.ui.radioButton_ispoln1.clicked.connect(self.clear_radio_isp)
        self.ui.radioButton_ispoln2.clicked.connect(self.clear_radio_isp)
        # ===================QSlider
        self.ui.hs_edit_time_jur.valueChanged.connect(self.edit_time_jur_time_change)
        # ==================== CALENDAR
        self.ui.cal_edit_time_jur.selectionChanged.connect(self.edit_date_jur_time_change)
        # ++++++++++++++++++++++++++++++++++++++++++++
        self.db_naryd = F.bdcfg('Naryad')
        self.db_act = F.scfg('BDact') + F.sep() + 'BDact.db'
        self.bd_users = F.bdcfg('BD_users')
        self.db_resxml = F.bdcfg('db_resxml')
        self.db_dse = F.bdcfg('BD_dse')
        self.db_nomen = F.bdcfg('nomenklatura_erp')
        self.db_files = F.bdcfg('BD_files')
        self.db_kplan = F.bdcfg('DB_kplan')
        # ==== GLOBALS
        self.SPIS_EMPLOEE = []
        self.glob_login = ''
        self.glob_ima = ''
        self.glob_nom_mk = 0
        self.glob_res = []
        self.glob_etap = []
        self.metka_resize = ''
        self.TIME_DEAL = 5
        self.CORT_DOP_ZN_PRIM_REZKA_MK = ('вырезан','разложен','режется')
        # ======ACTIONS
        self.ui.action_noviy_user.triggered.connect(lambda _, x=self: userm.reg_new_user(x))
        self.ui.action_change_pass.triggered.connect(lambda _, x=self: userm.change_user_pass(x))
        self.ui.action_load_csv.triggered.connect(self.load_csv)
        self.ui.action_peresilniy.triggered.connect(self.create_peresilniy)
        self.ui.actionexcel.triggered.connect(self.export_table)
        self.ui.action_txt.triggered.connect(self.export_table_txt)
        self.ui.action_reset_pass.triggered.connect(lambda _, x=self: userm.reset_user_pass(x))
        # =======loads
        self.app_icons()
        CQT.load_icons(self,24)
        userm.load_users(self)
        self.setWindowTitle('Создание нарядов')
        # ====== фильтр операций по должностям формирование списка
        self.SPIS_OPER = []
        if F.nalich_file(F.scfg('Filtr_rab') + F.sep() + 'filtr_oper.txt'):
            spis_dost_oper_tmp = F.load_file(F.scfg('Filtr_rab') + F.sep() + 'filtr_oper.txt')
            for i in range(len(spis_dost_oper_tmp)):
                users = spis_dost_oper_tmp[i][1].split(';')
                users_fio = []
                for user in users:
                    users_fio.append(' '.join(user.split(',')[:3]))
                self.SPIS_OPER.append([spis_dost_oper_tmp[i][0], users_fio])
            del spis_dost_oper_tmp
        else:
            CQT.msgbox('Не найден список операций')
            # quit()
            # ================================
        DICT_OPER = CSQ.zapros(self.db_naryd, f"""SELECT * FROM operacii""", rez_dict=True)
        self.DICT_OPER = F.raskrit_dict(DICT_OPER, 'kod')
        # ===================== словарь этапов ===================
        self.DICT_ETAPI = dict()
        for item in DICT_OPER:
            self.DICT_ETAPI[item['name']] = item['dopust_prof'].split(',')

        # =========================================================
        spis_rc = CSQ.zapros(self.bd_users, f'SELECT * FROM rab_c', rez_dict=True)
        self.DICT_RC = dict()
        for i in range(len(spis_rc)):
            if spis_rc[i]['Примечание'] == "":
                self.DICT_RC[spis_rc[i]['Код']] = spis_rc[i]['Имя']
            else:
                self.DICT_RC[spis_rc[i]['Код']] = f'{spis_rc[i]["Имя"]}({spis_rc[i]["Примечание"]})'
        self.DICT_RC_FULL = F.raskrit_dict(spis_rc,'Код')

        dict_tip = CSQ.zapros(self.db_naryd, """SELECT * FROM Тип_мк""", rez_dict=True)
        self.DICT_TIP_MK = F.raskrit_dict(dict_tip, 'Имя')

        spis_status = CSQ.zapros(self.db_naryd, f'SELECT DISTINCT jurnal.Статус FROM jurnal', shapka=False )
        self.ui.cmb_edit_time_jur.addItems([ i[0] for i in spis_status])


        # ============DB
        # ====ВРЕМЕННО
        # self.ui.lbx_spis_sotr.setCurrentIndex(8)
        # self.ui.le_parol.setText('2022')
        # userm.log_in(self)
        # self.zaversh_naruad()
        self.ui.tab_4.setEnabled(False)
        self.ui.tab_11.setEnabled(True)
        self.DICT_KATEG_VNEPLAN = F.raskrit_dict(
            CSQ.zapros(self.db_naryd, 'SELECT * FROM kategor_vnepl', rez_dict=True), 'value')
        self.DICT_PROFESSIONS = dict()
        CMS.dict_professions(self, self.bd_users)

        self.ui.cmb_kat_vnepl.addItems(list(self.DICT_KATEG_VNEPLAN.keys()))
        self.ui.cmb_vid_rab_vnepl.addItem('')
        self.ui.cmb_vid_rab_vnepl.addItems(list(self.DICT_VID_RABOT.keys()))
        self.ui.tbl_prosmotr_nar_jurnal.setSelectionBehavior(1)
        self.ui.tbl_prosmotr_nar_jurnal.setSelectionMode(1)

        CQT.ust_cvet_videl_tab(self.ui.tbl_prosmotr_nar_jurnal)
        #CQT.ust_cvet_videl_tab(self.ui.tbl_dse)

        CQT.load_css(self)
        self.ui.fr_dse_filtrs.setHidden(True)
        #=====================временно
        #OFFself.write_date_podtv()

    def write_date_podtv(self):
        query = f"""SELECT jurnal.Дата, jurnal.ФИО, jurnal.Статус, 
        naryad.ФИО as Нар_ф, naryad.ФИО2  as Нар_ф2,
        naryad.Фвремя as Нар_фв, naryad.Фвремя2  as Нар_фв2,
        naryad.Пномер  from jurnal INNER JOIN naryad
         ON naryad.Пномер == jurnal.Номер_наряда WHERE Статус == 'Завершен'"""
        rez = CSQ.zapros(self.db_naryd,zapros=query,rez_dict=True)
        set_double = set()
        list_dates = []
        for nar in rez:
            if nar['Нар_ф'] != '' and nar['Нар_ф2'] != '' and nar['Нар_фв'] != '' and nar['Нар_фв2'] != '':
                set_double.add((nar['Пномер'],nar['Нар_ф'],nar['Нар_ф2']))
            if nar['Нар_ф'] != '' and nar['Нар_ф2'] == '':

                list_dates.append([nar['Дата'],nar['Пномер']])
            if nar['Нар_ф'] == '' and nar['Нар_ф2'] != '':

                list_dates.append([nar['Дата'],nar['Пномер']])
        list_double = list(set_double)

        for nar_nom, fio1, fio2 in list_double:
            data = ''
            flag = {fio1:1,fio2:1}
            for nar in rez:
                if flag[fio1] == 0 and flag[fio2] == 0:
                    break
                if nar['Пномер'] == nar_nom:
                    flag[nar['ФИО']] = 0
                    if data == '':
                        data = F.strtodate(nar['Дата'])
                    else:
                        if F.strtodate(nar['Дата']) > data:
                            data = F.strtodate(nar['Дата'])
            list_dates.append([F.datetostr(data), nar_nom])
        CSQ.zapros(self.db_naryd, f"""UPDATE naryad SET Подтвержд_вып_дата = ? WHERE Пномер = ?""",
                   spisok_spiskov=list_dates)



    @CQT.onerror
    def zamena_filtr(self):
        tbl = self.ui.tbl_filtr_dse
        r = tbl.currentRow()
        c = tbl.currentColumn()
        if r == -1 or c == -1:
            return
        text = tbl.item(r, c).text()
        text = text.replace('/', '|')
        text = text.replace('?', '&')
        tbl.item(r, c).setText(text)
        CMS.primenit_filtr(self, self.ui.tbl_filtr_dse, self.ui.tbl_dse)


    @CQT.onerror
    def keyReleaseEvent(self, e):
        if e.key() == 67 and e.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            if CQT.focus_is_QTableWidget():
                CQT.copy_bufer_table(QtWidgets.QApplication.focusWidget())
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        if self.ui.tbl_select_marsh_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_select_marsh_filtr, self.ui.tbl_select_marsh)
        if self.ui.tbl_red_zhur.hasFocus():
            if e.key() == 16777220:
                if self.ui.tbl_red_zhur.currentColumn() == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Коэфф_сложности'):
                    self.edit_red_zhur_koef_sl(self.ui.tbl_red_zhur.currentRow(), self.ui.tbl_red_zhur.currentColumn())
                if self.ui.tbl_red_zhur.currentColumn() == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Твремя'):
                    self.edit_red_zhur_koef_sl(self.ui.tbl_red_zhur.currentRow(), self.ui.tbl_red_zhur.currentColumn())
                if self.ui.tbl_red_zhur.currentColumn() == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Примечание'):
                    self.edit_red_zhur_koef_sl(self.ui.tbl_red_zhur.currentRow(), self.ui.tbl_red_zhur.currentColumn())
            if e.key() == 16777268:
                self.ui.tbl_red_zhur_filtr.setFocus()
                self.load_table_korr_naruad(False)
        if e.key() == 67 and e.modifiers() == (QtCore.Qt.ControlModifier | QtCore.Qt.ShiftModifier):
            if CQT.focus_is_QTableWidget():
                CQT.copy_bufer_table(QtWidgets.QApplication.focusWidget())
        if self.ui.tbl_prosmotr_nar.hasFocus():
            if e.key() == 16777268:
                self.get_plan_proj()
                self.load_table_prosm_nar(False)
            if e.key() == 16777220:
                tbl = self.ui.tbl_prosmotr_nar
                row = tbl.currentRow()
                column = tbl.currentColumn()
                self.edit_koeff_nar_tbl(row, column)
        if self.ui.tbl_anal_rez_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_anal_rez_filtr, self.ui.tbl_anal_rez)
        if self.ui.tbl_anal_mk_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_anal_mk_filtr, self.ui.tbl_anal_mk)
        if self.ui.tbl_prosm_nar_oper_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_prosm_nar_oper_filtr, self.ui.tbl_prosm_nar_oper)
        if self.ui.tbl_prosmotr_nar_jurnal_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_prosmotr_nar_jurnal_filtr, self.ui.tbl_prosmotr_nar_jurnal)
        if self.ui.tbl_prosm_nar_zadan_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_prosm_nar_zadan_filtr, self.ui.tbl_prosm_nar_zadan)
        if self.ui.tbl_dse.hasFocus():
            if e.key() == 16777220:
                if self.ui.tbl_dse.currentColumn() == CQT.nom_kol_po_imen(self.ui.tbl_dse, 'В работу,шт.'):
                    self.raschet_naruada_time_tmp()
            if e.key() == 32:
                self.select_dse(0)
        if self.ui.tbl_red_zhur_filtr.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_red_zhur_filtr, self.ui.tbl_red_zhur)
        if self.ui.tbl_filtr_prosmotr_nar.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_filtr_prosmotr_nar, self.ui.tbl_prosmotr_nar)
        if self.ui.tbl_filtr_vibor_nar_rasp.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_filtr_vibor_nar_rasp, self.ui.tbl_vibor_nar_rasp)
        if self.ui.tbl_filtr_dse.hasFocus():
            if e.key() == 16777220:
                if e.modifiers() == QtCore.Qt.AltModifier:
                    self.zamena_filtr()
                CMS.primenit_filtr(self, self.ui.tbl_filtr_dse, self.ui.tbl_dse)
                self.fill_tbl_select_marsh()
        if self.ui.le_parol.hasFocus():
            if e.key() == 16777220:
                userm.log_in(self)
        if self.ui.tbl_filtr_komplektovka.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_filtr_komplektovka, self.ui.tbl_komplektovka)
        if self.ui.tbl_filtr_mk.hasFocus():
            if e.key() == 16777220:
                CMS.primenit_filtr(self, self.ui.tbl_filtr_mk, tabl_sp_mk)
                nk_mass = CQT.nom_kol_po_imen(self.ui.tableWidget_vibor_mk, 'Вес')
                summ = 0
                for i in range(self.ui.tableWidget_vibor_mk.rowCount()):
                    if not self.ui.tableWidget_vibor_mk.isRowHidden(i):
                        if F.is_numeric(self.ui.tableWidget_vibor_mk.item(i,nk_mass).text()):
                            summ+= F.valm(self.ui.tableWidget_vibor_mk.item(i,nk_mass).text())
                self.ui.lbl_for_summ.setText(f' Сумма {round(summ)} кг.')
        if tabl_sp_mk.hasFocus():
            if e.key() == 16777268:
                self.reload_list_mk()
            if e.key() == 16777220:
                if tabl_sp_mk.currentColumn() == CQT.nom_kol_po_imen(tabl_sp_mk, "Статус_ЧПУ"):
                    self.open_papka_chpy()
                if tabl_sp_mk.currentColumn() == CQT.nom_kol_po_imen(tabl_sp_mk, "Прим_резка"):
                    row, col = CQT.nomer_vibr_cell_r_c(tabl_sp_mk)
                    if tabl_sp_mk.item(row, col).text() in self.CORT_DOP_ZN_PRIM_REZKA_MK:
                        query = f'''
                                UPDATE zagot SET Прим_резка = "{tabl_sp_mk.item(row, col).text()}" 
                                WHERE Ном_МК == {int(tabl_sp_mk.item(row, CQT.nom_kol_po_imen(tabl_sp_mk, "Пномер")).text())};
                                '''
                        CSQ.zapros(self.db_naryd, query)
                    else:
                        tabl_sp_mk.item(row, col).setText('')
                        CQT.msgbox(f'ошибка! допустимые значения: {self.CORT_DOP_ZN_PRIM_REZKA_MK}')

                if tabl_sp_mk.currentColumn() == CQT.nom_kol_po_imen(tabl_sp_mk, "Дата_компл_загот"):
                    row, col = CQT.nomer_vibr_cell_r_c(tabl_sp_mk)
                    now_str = F.now("%Y-%m-%d %H:%M:%S")
                    query = f'''
                            UPDATE zagot SET Дата_компл_загот = "{now_str}" 
                            WHERE Ном_МК == {int(tabl_sp_mk.item(row, CQT.nom_kol_po_imen(tabl_sp_mk, "Пномер")).text())};
                            '''
                    tabl_sp_mk.item(row,col).setText(now_str)
                    CSQ.zapros(self.db_naryd, query)


    def reload_list_mk(self):
        if self.glob_login != '':
            self.zapoln_tabl_mk()

    @CQT.onerror
    def app_icons(self):
        self.ui.btn_reload_list_mk.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload)))
        self.ui.checkBox_min_rezhjim.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogHelpButton)))
        self.ui.checkBox_full_dse.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogResetButton)))
        self.ui.btn_login.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogYesButton)))
        self.ui.btn_login.setIconSize(QtCore.QSize(16, 16))
        self.ui.btn_logout.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogNoButton)))
        self.ui.btn_logout.setIconSize(QtCore.QSize(16, 16))
        self.ui.btn_select_all.setIcon(QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ToolBarVerticalExtensionButton)))
        self.ui.btn_select_all.setIconSize(QtCore.QSize(16, 16))
        self.ui.btn_invers.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_TitleBarShadeButton)))
        self.ui.btn_invers.setIconSize(QtCore.QSize(16, 16))
        self.ui.btn_create_nar.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogApplyButton)))
        self.ui.btn_create_nar.setIconSize(QtCore.QSize(16, 16))
        self.ui.btn_primen_imena.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload)))
        self.ui.btn_primen_imena.setIconSize(QtCore.QSize(64, 64))
        self.ui.btn_komplect.setIcon(
            QtGui.QIcon(QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogApplyButton)))
        self.ui.btn_komplect.setIconSize(QtCore.QSize(16, 16))
        self.ui.tabWidget_2.setTabIcon(0, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_FileDialogDetailedView)))
        self.ui.tabWidget_2.setTabIcon(1, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_FileDialogListView)))
        self.ui.tabWidget_2.setTabIcon(2, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_TrashIcon)))
        self.ui.tabWidget_2.setTabIcon(3, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_MessageBoxWarning)))
        self.ui.tabWidget.setTabIcon(0, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_ComputerIcon)))
        self.ui.tabWidget.setTabIcon(1, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DialogOkButton)))
        self.ui.tabWidget.setTabIcon(2, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_FileDialogInfoView)))
        self.ui.tabWidget.setTabIcon(4, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_DriveHDIcon)))
        self.ui.tabWidget.setTabIcon(5, QtGui.QIcon(
            QtWidgets.QApplication.style().standardIcon(QtWidgets.QStyle.SP_FileDialogContentsView)))


    def get_plan_proj(self):
        self.DICT_ACCESS_PROJ_MONTH = CSQ.zapros(self.db_kplan, f"""SELECT * FROM list_py_month""", rez_dict=True)
        self.DICT_ACCESS_USER_DELTA = F.raskrit_dict(
            CSQ.zapros(self.db_kplan, f"""SELECT * FROM list_py_users_delta_month""", rez_dict=True), 'user')


    @CQT.onerror
    def tab_clcik(self, nom, *args):
        if CMS.kontrol_ver(self.versia, "Создание2") == False:
            sys.exit()
        if not CMS.check_actual_parol(self.glob_ima):
            CQT.msgbox(f'Нужно обновить пароль через меню "Параметры"')
            userm.logout(self)
        name = self.ui.tabWidget.tabText(nom)
        if name == 'Комплектование':
            self.load_table_komplekt()
        if name == 'Оповещение':
            CQT.load_css(self)
        if name == 'Просмотр нарядов':
            self.load_table_prosm_nar()
        if name == 'Распределение нарядов':
            self.get_plan_proj()
            rez = self.check_vnesenie_trudozatrat()
            if rez:
                self.load_table_raspred_nar()
            else:
                self.ui.tabWidget.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget, 'Просмотр нарядов'))
        if name == 'Корректировка':
            self.load_table_korr_naruad()
        if name == 'Контроль проектов':
            compare.load_py(self)


    @CQT.onerror
    def tab2_clcik(self, nom, *args):
        name = self.ui.tabWidget_2.tabText(nom)
        if name == 'МК':
            pass
        if name == 'ДСЕ':
            self.load_brak()
            if self.ui.tbl_brak.rowCount() > 0:
                self.ui.tabWidget_2.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget_2, 'Брак'))
            else:
                self.load_mk()
        if name == 'Наряд':
            if self.raschet_naruada_time_tmp() == False:
                self.ui.tabWidget_2.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget_2, 'ДСЕ'))
                self.ui.cmb_kat_vnepl.setCurrentText('')
                self.ui.cmb_vid_rab_vnepl.setCurrentText('')
                return
            self.raschet_naruada()
        if name == 'Брак':
            self.load_brak()

    def check_vnesenie_trudozatrat(self):
        now = F.now('')
        dict_check_days = dict()
        set_month = set()
        RAB_DAY_LIMIT = 3
        DAYS_CHECK = 5
        counter = 0
        for i in range(-1,-20,-1):
            if counter - RAB_DAY_LIMIT >= DAYS_CHECK:
                break
            day = F.datetostr(F.date_add_days(now,i,'',''),'d_%Y_%m_%d')
            month = F.datetostr(F.date_add_days(now,i,'',''),'jurnaltdz_%Y_%m_01')
            vihodn_val = CSQ.zapros(self.bd_users,f"""SELECT {day} FROM {month} WHERE Пномер = 1""")
            if vihodn_val == False:
                CQT.msgbox(f'ОШибка загрузки календаря')
                return False
            if vihodn_val[-1][0] == 0:
                counter +=1
            if counter > RAB_DAY_LIMIT:
                dict_check_days[day] = month
                set_month.add(month)
        list_month = sorted(list(set_month))
        rez = []
        for month in list_month:
            tbl = CSQ.zapros(self.bd_users,f"""SELECT * FROM {month}""")
            for i in range(3,len(tbl)):
                if self.glob_ima in tbl[i][2]:
                    for day in dict_check_days.keys():
                        if dict_check_days[day] == month:
                            for j in range(3,len(tbl[0])):
                                if day == tbl[0][j]:
                                    if tbl[i][j] == 0:
                                        day_name = F.datetostr(F.strtodate(day,'d_%Y_%m_%d'),'%d.%m.%Y')
                                        rez.append(f'{day_name} для РЦ{tbl[i][1]} не выгружено. Ответственные: {tbl[i][2]}')
                                    break
        if rez == []:
            return True
        CQT.msgbox("\n".join(rez))
        return False


    def check_dost_proj_moth(self,py,fio):
        if fio not in self.DICT_ACCESS_USER_DELTA:
            return True
        delta = self.DICT_ACCESS_USER_DELTA[fio]['delta']
        for item in self.DICT_ACCESS_PROJ_MONTH:
            if item['ПУ'] == py:
                if F.now('') > F.date_add_days(item['Месяц'],delta,'%y-%m-%d',''):
                    return True
                else:
                    return False
        return False

    @CQT.onerror
    def open_zayavk(self, *args):
        if self.glob_login == "":
            CQT.msgbox('Необходимо войти')
            return
        nom_pr = ''
        nom_pu = ''

        if self.ui.tabWidget.currentIndex() == CQT.nom_tab_po_imen(self.ui.tabWidget, 'Создание наряда'):
            if self.ui.tableWidget_vibor_mk.currentRow() != -1:
                nom_pu = self.ui.tableWidget_vibor_mk.item(self.ui.tableWidget_vibor_mk.currentRow(),
                                                           CQT.nom_kol_po_imen(self.ui.tableWidget_vibor_mk,
                                                                              'Номер_заказа')).text()
                nom_pr = self.ui.tableWidget_vibor_mk.item(self.ui.tableWidget_vibor_mk.currentRow(),
                                                           CQT.nom_kol_po_imen(self.ui.tableWidget_vibor_mk,
                                                                               'Номер_проекта')).text()
        if self.ui.tabWidget.currentIndex() == CQT.nom_tab_po_imen(self.ui.tabWidget, 'Распределение нарядов'):
            if self.ui.tbl_vibor_nar_rasp.currentRow() != -1:
                nom_pu = self.ui.tbl_vibor_nar_rasp.item(self.ui.tbl_vibor_nar_rasp.currentRow(),
                                                         CQT.nom_kol_po_imen(self.ui.tbl_vibor_nar_rasp,
                                                                             'Номер_заказа')).text()
                nom_pr = self.ui.tbl_vibor_nar_rasp.item(self.ui.tbl_vibor_nar_rasp.currentRow(),
                                                         CQT.nom_kol_po_imen(self.ui.tbl_vibor_nar_rasp,
                                                                             'Номер_проекта')).text()
        if self.ui.tabWidget.currentIndex() == CQT.nom_tab_po_imen(self.ui.tabWidget, 'Просмотр нарядов'):
            if self.ui.tbl_prosmotr_nar.currentRow() != -1:
                nom_pu = self.ui.tbl_prosmotr_nar.item(self.ui.tbl_prosmotr_nar.currentRow(),
                                                       CQT.nom_kol_po_imen(self.ui.tbl_prosmotr_nar,
                                                                           'Номер_заказа')).text()
                nom_pr = self.ui.tbl_prosmotr_nar.item(self.ui.tbl_prosmotr_nar.currentRow(),
                                                       CQT.nom_kol_po_imen(self.ui.tbl_prosmotr_nar,
                                                                           'Номер_проекта')).text()
        if self.ui.tabWidget.currentIndex() == CQT.nom_tab_po_imen(self.ui.tabWidget, 'Комплектование'):
            if self.ui.tbl_komplektovka.currentRow() != -1:
                nom_pu = self.ui.tbl_komplektovka.item(self.ui.tbl_komplektovka.currentRow(),
                                                       CQT.nom_kol_po_imen(self.ui.tbl_komplektovka,
                                                                           'Номер_заказа')).text()
                nom_pr = self.ui.tbl_komplektovka.item(self.ui.tbl_komplektovka.currentRow(),
                                                       CQT.nom_kol_po_imen(self.ui.tbl_komplektovka,
                                                                           'Номер_проекта')).text()
        if self.ui.tabWidget.currentIndex() == CQT.nom_tab_po_imen(self.ui.tabWidget, 'Корректировка'):
            if self.ui.tbl_red_zhur.currentRow() != -1:
                nom_pu = self.ui.tbl_red_zhur.item(self.ui.tbl_red_zhur.currentRow(),
                                                   CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Номер_заказа')).text()
                nom_pr = self.ui.tbl_red_zhur.item(self.ui.tbl_red_zhur.currentRow(),
                                                   CQT.nom_kol_po_imen(self.ui.tbl_red_zhur,
                                                                       'Номер_проекта')).text()
        if nom_pu == '':
            return
        putf = CMS.Put_k_papke_s_proektom_NPPU(nom_pr, nom_pu)
        modifiers = CQT.get_key_modifiers(self)
        if modifiers == ['shift']:
            F.otkr_papky(putf)
            return
        list_files = F.spis_files(putf)
        if list_files == []:
            return
        for file in list_files[0][2]:
            if 'Заказ на производство №' in file and '.pdf' in file:
                F.zapyst_file(list_files[0][0] + file)
                return
        F.otkr_papky(list_files[0][0])

    @CQT.onerror
    def poz_kol_add(self, *args):
        if self.glob_login == "":
            CQT.msgbox('Необходимо войти')
            return
        try:
            zapros = f'''SELECT Количество FROM mk WHERE Пномер == {self.glob_nom_mk}'''
            rez = CSQ.zapros(self.db_naryd, zapros)
            kol_izd = int(rez[-1][0])
        except:
            CQT.msgbox('Ошибка загрузки количества')
            return
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        nk_kol = CQT.nom_kol_po_imen(tbl, 'Количество,шт.')
        nk_vrab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')

        for i in range(tbl.rowCount()):
            if tbl.cellWidget(i, nk_check).isChecked():
                kol = F.valm(tbl.item(i, nk_kol).text())
                kol_ed = kol / kol_izd
                vrab = int(tbl.item(i, nk_vrab).text())
                if vrab + kol_ed > kol:
                    tbl.item(i, nk_vrab).setText(str(kol))
                else:
                    tbl.item(i, nk_vrab).setText(str(int(vrab + kol_ed)))

    @CQT.onerror
    def poz_kol_minus(self, *args):
        if self.glob_login == "":
            CQT.msgbox('Необходимо войти')
            return
        try:
            zapros = f'''SELECT Количество FROM mk WHERE Пномер == {self.glob_nom_mk}'''
            rez = CSQ.zapros(self.db_naryd, zapros)
            kol_izd = int(rez[-1][0])
        except:
            CQT.msgbox('Ошибка загрузки количества')
            return
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        nk_kol = CQT.nom_kol_po_imen(tbl, 'Количество,шт.')
        nk_vrab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')

        for i in range(tbl.rowCount()):
            if tbl.cellWidget(i, nk_check).isChecked():
                kol = F.valm(tbl.item(i, nk_kol).text())
                kol_ed = kol / kol_izd
                vrab = int(tbl.item(i, nk_vrab).text())
                if vrab - kol_ed < 0:
                    tbl.item(i, nk_vrab).setText("0")
                else:
                    tbl.item(i, nk_vrab).setText(str(int(vrab - kol_ed)))

    @CQT.onerror
    def export_table_txt(self, *args):
        tab = self.ui.tabWidget
        tab2 = self.ui.tabWidget_2
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Создание наряда'):
            if tab2.currentIndex() == CQT.nom_tab_po_imen(tab2, 'ДСЕ'):
                dir_folder = CMS.load_tmp_folder(self, "export_table")
                if dir_folder == None:
                    return
                imaf = f'DSE_mk{str(self.glob_nom_mk)}_{F.now("%d.%m.%Y %H;%M")}.txt'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_dse, shapka=True)
                spis = F.spis_txt_table(spis)
                F.save_file(dir_folder + F.sep() + imaf, spis)

                F.otkr_papky(dir_folder)

    @CQT.onerror
    def export_table(self, *args):
        tab = self.ui.tabWidget
        tab2 = self.ui.tabWidget_2
        if tab.currentIndex() == CQT.nom_tab_po_imen(tab, 'Создание наряда'):
            if tab2.currentIndex() == CQT.nom_tab_po_imen(tab2, 'ДСЕ'):
                dir_folder = CMS.load_tmp_folder(self, "export_table")
                if dir_folder == None:
                    return
                imaf = f'DSE_mk{str(self.glob_nom_mk)}_{F.now("%d.%m.%Y %H;%M")}.xlsx'
                spis = CQT.spisok_iz_wtabl(self.ui.tbl_dse, shapka=True)

                CEX.zap_spis(spis, dir_folder, imaf, '1', 1, 1, True, True, 'g')
                F.otkr_papky(dir_folder)

    @CQT.onerror
    def create_peresilniy(self, *args):
        if self.glob_login == "":
            CQT.msgbox('Необходимо войти')
            return
        if self.ui.tabWidget.currentIndex() != CQT.nom_tab_po_imen(self.ui.tabWidget, 'Комплектование'):
            self.ui.tabWidget.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget, 'Комплектование'))
        tbl = self.ui.tbl_komplektovka
        tblv = self.ui.tbl_komplektovka_view
        CMS.load_peresilniy(self, tbl, tblv)

    @CQT.onerror
    def load_csv(self, *args):
        if self.glob_login == "":
            CQT.msgbox('Необходимо войти')
            return
        CMS.load_csv(self,self.db_nomen)
        self.zapoln_tabl_mk()

    @CQT.onerror
    def tbl_prosmotr_nar_click(self, *args):
        tblp = self.ui.tbl_prosmotr_nar
        tblj = self.ui.tbl_prosmotr_nar_jurnal
        nk_nom_nar = CQT.nom_kol_po_imen(tblp, 'Пномер')
        nom_nar = int(tblp.item(tblp.currentRow(), nk_nom_nar).text())
        zapros = f'''SELECT  Пномер, Номер_наряда, Дата, ФИО, Статус, Подытог, Примечание FROM jurnal WHERE Номер_наряда == {nom_nar}'''
        rez = CSQ.zapros(self.db_naryd, zapros)
        CQT.zapoln_wtabl(self, rez, tblj, isp_shapka=True, separ='')
        CMS.zapolnit_filtr(self, self.ui.tbl_prosmotr_nar_jurnal_filtr, self.ui.tbl_prosmotr_nar_jurnal)
        nk_zad = CQT.nom_kol_po_imen(tblp, 'Задание')
        nk_oper = CQT.nom_kol_po_imen(tblp, 'Операции')
        nk_vrem = CQT.nom_kol_po_imen(tblp, 'Опер_время')
        nk_kol = CQT.nom_kol_po_imen(tblp, 'Опер_колво')

        zad = tblp.item(tblp.currentRow(), nk_zad).text().split('\n')
        zad = [[_] for _ in zad]
        zad.insert(0, ['Задание'])
        oper = tblp.item(tblp.currentRow(), nk_oper).text().split('|')
        vrem = tblp.item(tblp.currentRow(), nk_vrem).text().split('|')
        kol = tblp.item(tblp.currentRow(), nk_kol).text().split('|')
        spis_oper = [['Операция', 'шт.', 'мин.']]
        for i in range(len(oper)):
            spis_oper.append([oper[i].replace('$', ' '), kol[i], vrem[i]])
        CQT.zapoln_wtabl(self, zad, self.ui.tbl_prosm_nar_zadan, separ='', isp_shapka=True)
        CMS.zapolnit_filtr(self, self.ui.tbl_prosm_nar_zadan_filtr, self.ui.tbl_prosm_nar_zadan)
        CQT.zapoln_wtabl(self, spis_oper, self.ui.tbl_prosm_nar_oper, separ='', isp_shapka=True)
        CMS.zapolnit_filtr(self, self.ui.tbl_prosm_nar_oper_filtr, self.ui.tbl_prosm_nar_oper)
        CMS.on_section_resized(self)

    @CQT.onerror
    def tbl_komplektovka_view_click(self, *args):
        tblv = self.ui.tbl_komplektovka_view
        r = tblv.currentRow()
        nk_dse = CQT.nom_kol_po_imen(tblv, 'Операции')
        self.ui.lbl_kompl_info.setText(tblv.item(r, nk_dse).text())

    @CQT.onerror
    def tbl_komplektovka_click(self, *args):
        tblk = self.ui.tbl_komplektovka
        tblv = self.ui.tbl_komplektovka_view
        CMS.specificaciya_naruad(self, tblk, tblv)

    @CQT.onerror
    def otmeka_komplekt(self, *args):
        tbl = self.ui.tbl_komplektovka
        if tbl.currentRow() == -1:
            CQT.msgbox(f'Не вабран наряд')
            return
        if not CMS.user_access(self.db_naryd, 'создание_комплектация',
                               CMS.ima_po_emp(self.glob_login)):
            return
        nk_nom = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nk_nom_tara = CQT.nom_kol_po_imen(tbl, 'Компл_номер_тара')
        nk_adres = CQT.nom_kol_po_imen(tbl, 'Компл_адрес')
        nk_tvrem = CQT.nom_kol_po_imen(tbl, 'Твремя')
        #if float(tbl.item(tbl.currentRow(), nk_tvrem).text()) == 0:
        #    CQT.msgbox(f'Наряд необходимо отнормировать, обратись к нормировщице ТОП')
        #    CQT.migat(self, tbl, tbl.currentRow(), nk_tvrem)
        #    return
        if tbl.item(tbl.currentRow(), nk_nom_tara).text() == '':
            CQT.msgbox(f'Не указана Компл_номер_тара')
            CQT.migat(self, tbl, tbl.currentRow(), nk_nom_tara)
            return
        if F.is_numeric(tbl.item(tbl.currentRow(), nk_nom_tara).text()) == False:
            CQT.msgbox(f'Компл_номер_тара должно быть число')
            CQT.migat(self, tbl, tbl.currentRow(), nk_nom_tara)
            return
        if tbl.item(tbl.currentRow(), nk_adres).text() == '':
            CQT.msgbox(f'Не указан Компл_адрес')
            CQT.migat(self, tbl, tbl.currentRow(), nk_adres)
            return
        nom_nar = int(tbl.item(tbl.currentRow(), nk_nom).text())
        if CQT.msgboxgYN(f'Я, {CMS.ima_po_emp(self.glob_login)}, подтверждаю наличие полного комплекта по'
                         f' наряду №{nom_nar}. Я осознаю и несу полную ответствнность за производственные'
                         f' потери, вызванные недостоверностью предоставленных данных.'):
            zapros = f'UPDATE naryad SET Компл_ФИО = "{CMS.ima_po_emp(self.glob_login)}", Компл_Дата = "{F.now()}",' \
                     f' Компл_номер_тара = "{tbl.item(tbl.currentRow(), nk_nom_tara).text()}",' \
                     f' Компл_адрес = "{tbl.item(tbl.currentRow(), nk_adres).text()}" WHERE Пномер = {nom_nar}'
            CSQ.zapros(self.db_naryd, zapros)
            self.load_table_komplekt()

    @CQT.onerror
    def select_invers_dse(self, *args):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        for i in range(tbl.rowCount()):
            if tbl.isRowHidden(i) == False:
                if tbl.cellWidget(i, nk_check).isChecked():
                    tbl.cellWidget(i, nk_check).setChecked(False)
                    tbl.item(i,nk_check).setText('')
                else:
                    tbl.cellWidget(i, nk_check).setChecked(True)
                    tbl.item(i, nk_check).setText('1')
        self.tbl_dse_select()
        self.raschet_naruada_time_tmp()

    @CQT.onerror
    def select_dse(self, korr=1, row = ''):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        if row == '':
            row = tbl.currentRow()
        if tbl.cellWidget(row - korr, nk_check) == None:
            return
        if tbl.cellWidget(row - korr, nk_check).isChecked():
            tbl.cellWidget(row - korr, nk_check).setChecked(False)
            tbl.item(row - korr, nk_check).setText('')

        else:
            tbl.cellWidget(row - korr, nk_check).setChecked(True)
            tbl.item(row - korr, nk_check).setText('1')
        self.bold_in_marsh_selected_dse()

    @CQT.onerror
    def unselect_all_dse(self, *args):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        for i in range(tbl.rowCount()):
            tbl.cellWidget(i, nk_check).setChecked(False)
            tbl.item(i, nk_check).setText('')
        self.tbl_dse_select()
        self.raschet_naruada_time_tmp()

    @CQT.onerror
    def select_all_dse(self, *args):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        for i in range(tbl.rowCount()):
            if tbl.isRowHidden(i) == False:
                tbl.cellWidget(i, nk_check).setChecked(True)
                tbl.item(i, nk_check).setText('1')
        self.tbl_dse_select()
        self.raschet_naruada_time_tmp()

    @CQT.onerror
    def check_sootv_res_nommk(self):
        lbl = self.ui.lbl_curr_mk
        if "МК " + str(self.glob_nom_mk) != lbl.text().split(' - ')[0]:
            CQT.msgbox('Не выбрана МК')
            return
        self.glob_res = CMS.load_res(self.glob_nom_mk)
        return True

    @CQT.onerror
    def create_naryd(self, *args):
        def delete_nar(date_nar,dse_id):
            CSQ.zapros(self.db_naryd, f"""DELETE FROM naryad WHERE Дата = '{date_nar}' 
                                    AND ДСЕ_ID = '{dse_id}';""")
        if self.glob_login == '':
            return
        try:
            len(self.spis_dse)
        except:
            return
        check = self.ui.checkBox_vneplan_rab.isChecked()

        if check == False:
            if len(self.spis_dse) == 0:
                CQT.msgbox('Не выбраны операции')
                return
            if F.valm(self.ui.lineEdit_cr_nar_norma.text()) == 0:
                CQT.msgbox('Норма времени не может быть 0')
                return
            if self.ui.plainTextEdit_zadanie.toPlainText() == '':
                CQT.msgbox('Задание не может быть пусто')
                return
            if self.check_sootv_res_nommk() != True:
                return

            kat_vnepl = 0
        else:
            if F.valm(self.ui.lineEdit_cr_nar_norma.text()) != 0:
                CQT.msgbox('Норма времени должна быть 0')
                return
            if self.ui.plainTextEdit_zadanie.toPlainText() == '':
                CQT.msgbox('Задание не может быть пусто')
                return
            if self.spis_dse == None:
                CQT.msgbox('Не выбраны ДСЕ')
                return
            if len(self.spis_dse) == 0:
                CQT.msgbox('Не выбраны ДСЕ')
                return
            if self.ui.cmb_kat_vnepl.currentText() == "":
                CQT.msgbox('Не выбрана категория Внеплановых работ')
                return

            if self.ui.cmb_vid_rab_vnepl.currentText() == "":
                CQT.msgbox('Не выбран вид Внеплановых работ')
                return
            if self.ui.lineEdit_cr_nar_kolvo.text() == "":
                CQT.msgbox('Не указано количество')
                return
            if F.is_numeric(self.ui.lineEdit_cr_nar_kolvo.text()) == False:
                CQT.msgbox('Количество должно быть числом')
                return

            kat_vnepl = self.DICT_KATEG_VNEPLAN[self.ui.cmb_kat_vnepl.currentText()]
            if kat_vnepl in (2,3):
                if self.ui.le_nom_zam.text() == '':
                    CQT.msgbox('Не указан номер из журнала замечаний')
                    return

            self.spis_vidrab = [self.ui.cmb_vid_rab_vnepl.currentText()]
            self.spis_dse = self.spis_dse[:1]
            self.spis_id = self.spis_id[:1]
            self.spis_oper = self.spis_oper[:1]
            self.spis_vr = [self.ui.lineEdit_cr_nar_norma.text()]
            self.spis_kolvo = [self.ui.lineEdit_cr_nar_kolvo.text()]
        nom_zam_zhurnal = self.ui.le_nom_zam.text()
        kompl_fio = ''
        kompl_data = ''
        kompl_tara = ''
        kompl_address = ''
        if self.ui.checkBox_bez_kompl.isChecked():
            kompl_fio = CMS.ima_po_emp(self.glob_login)
            kompl_data = F.now()
            kompl_tara = '-'
            kompl_address = '-'

        date_nar = F.now()
        dse_id = '|'.join(self.spis_id)
        stroka = [date_nar,
                  CMS.ima_po_emp(self.glob_login),
                  self.glob_nom_mk,
                  self.ui.checkBox_vneplan_rab.isChecked(),
                  self.ui.plainTextEdit_zadanie.toPlainText(),
                  kompl_fio,
                  kompl_data,
                  kompl_tara,
                  kompl_address,
                  '',
                  '',
                  '',
                  '',
                  F.valm(self.ui.lineEdit_cr_nar_norma.text()),
                  '|'.join(self.spis_dse),
                  dse_id,
                  '|'.join(self.spis_oper),
                  '|'.join(self.spis_vr),
                  '|'.join(self.spis_kolvo),
                  self.ui.plainTextEdit_primechanie.toPlainText(),
                  1, 0, kat_vnepl, '|'.join(self.spis_vidrab),nom_zam_zhurnal,'','']


        zapros = f'''INSERT INTO naryad (Дата,	Автор,Номер_мк,Внеплан,Задание,Компл_ФИО,Компл_Дата,Компл_номер_тара,
        Компл_адрес,ФИО,Фвремя,ФИО2,Фвремя2,Твремя,ДСЕ,ДСЕ_ID,Операции,Опер_время,Опер_колво,Примечание,Коэфф_сложности,
        Подтвержд_вып,Категория_внепл,Виды_работ,Номер_замечания_журнал,Подтвержд_вып_дата,Подтвержд_вып_фио) VALUES 
        ({", ".join(("?" * len(stroka)))});'''
        rez = CSQ.zapros(self.db_naryd, zapros, spisok_spiskov=[stroka])
        if rez == None or rez == False:
            CQT.msgbox(f'Неудачно!, попробуй еще.')
            delete_nar(date_nar, dse_id)
            return
        nom_nar = CSQ.zapros(self.db_naryd, f"""SELECT Пномер FROM naryad WHERE Дата = '{date_nar}' 
        AND ДСЕ_ID = '{dse_id}' ORDER BY Пномер DESC LIMIT 1""")

        try:
            if len(nom_nar) != 2 or F.is_numeric(nom_nar[-1][0]) == False:
                CQT.msgbox(f'Неудачно!, попробуй еще.')
                delete_nar(date_nar,dse_id)
                return
        except:
            CQT.msgbox(f'Неудачно!, попробуй еще.')
            delete_nar(date_nar, dse_id)
            return

        if check == False:
            self.uchet_osvoenih_v_res()

        CQT.msgbox(f'Наряд №{nom_nar[-1][0]} создан')
        self.ui.plainTextEdit_zadanie.setPlainText('')
        self.ui.plainTextEdit_primechanie.setPlainText('')
        self.ui.lineEdit_cr_nar_norma.setText('')
        self.load_mk()

    @CQT.onerror
    def primen_imena(self, *args):
        nk_py = CQT.nom_kol_po_imen(self.ui.tbl_vibor_nar_rasp, 'Номер_заказа')
        if nk_py == None:
            CQT.msgbox(f'Поле Номер_заказа не найдено')
            return

        nom_py = self.ui.tbl_vibor_nar_rasp.item(self.ui.tbl_vibor_nar_rasp.currentRow(), nk_py).text()

        if not self.check_dost_proj_moth(nom_py,self.glob_ima):
            CQT.msgbox(f'{nom_py} отсутствует в плане ПДО, работа ЗАБЛОКИРОВАНА')
            return

        if self.ui.lbl_vibr_nar.text() == '':
            CQT.msgbox('Не выбран наряд')
            return
        if self.ui.lbl_ispoln1.text() == '' and self.ui.lbl_ispoln2.text() == '':
            CQT.msgbox('Не выбран исполнитель')
            return
        fio = self.ui.lbl_ispoln1.text()
        fio2 = self.ui.lbl_ispoln2.text()
        nom_nar = int(self.ui.lbl_vibr_nar.text())

        nk_norma = CQT.nom_kol_po_imen(self.ui.tbl_vibor_nar_rasp, 'Твремя')
        if nk_norma == None:
            CQT.msgbox(f'Поле Твремя не найдено')
            return
        norma = F.valm(self.ui.tbl_vibor_nar_rasp.item(self.ui.tbl_vibor_nar_rasp.currentRow(), nk_norma).text())
        if norma == 0 or norma == 0.0:
            CQT.msgbox(f'Наряд {nom_nar} необходимо отнормировать, обратись к нормировщице ТОП')
            return
        if fio2 != '' and fio != '':
            norma = norma / 2


        zapros = f'''   UPDATE naryad SET ФИО==?, ФИО2==?, Твремя==?  WHERE Пномер == ?'''
        rez = CSQ.zapros(self.db_naryd, zapros, spisok_spiskov=[fio, fio2, norma, nom_nar])
        if not rez:

            CQT.msgbox(f'Ошибка занесения', time_life=3)
            return
        self.ui.lbl_vibr_nar.clear()
        self.ui.lbl_ispoln1.clear()
        self.ui.lbl_ispoln2.clear()
        self.ui.cmb_prof_rasp.clear()
        self.load_table_raspred_nar()
        CQT.clear_tbl(self.ui.tbl_vibor_rabotn_rasp)
        CQT.msgbox(f'Наряд №{nom_nar} успешно распределен')

    @CQT.onerror
    def tek_zagruzka_rabotn(self, fio, conn, spis_nezav_nar):
        summ = 0
        for naryd in spis_nezav_nar:
            if fio == naryd['ФИО'] and naryd['Фвремя'] == '':
                summ += F.valm(naryd['Твремя'])
            if fio == naryd['ФИО2'] and naryd['Фвремя2'] == '':
                summ += F.valm(naryd['Твремя'])
        return summ

    @CQT.onerror
    def zapoln_table_rabont_po_prof(self, prof):
        spis_sotr = [["ФИО", "Минут", 'Прогресс']]

        zapros = f'''SELECT ФИО, ФИО2, Фвремя, Фвремя2, Твремя
                                        FROM naryad WHERE Фвремя == "" OR Фвремя2 == ""'''
        spis_nezav_nar = CSQ.zapros(self.db_naryd, zapros,  rez_dict=True)

        if spis_nezav_nar == False:
            CQT.msgbox('БД занята, пробуй позже')
            return
        for empl in self.SPIS_EMPLOEE:
            if prof == empl[1]:
                zagruzka = self.tek_zagruzka_rabotn(empl[0], '', spis_nezav_nar)
                spis_sotr.append([empl[0], zagruzka, zagruzka])
        CQT.zapoln_wtabl(self, spis_sotr, self.ui.tbl_vibor_rabotn_rasp, separ='', isp_shapka=True)
        CQT.zapolnit_progress(self, self.ui.tbl_vibor_rabotn_rasp, 2, True, False, True)

    @CQT.onerror
    def select_prof_raspr(self, nom, *args):
        if nom == 0:
            return
        prof = self.ui.cmb_prof_rasp.itemText(nom)
        self.zapoln_table_rabont_po_prof(prof)

    @CQT.onerror
    def clear_radio_isp(self, *args):
        if self.ui.radioButton_ispoln1.isChecked():
            self.ui.lbl_ispoln1.clear()
        else:
            self.ui.lbl_ispoln2.clear()

    @CQT.onerror
    def tbl_rabotn_raspr_click(self, *args):
        tbl = self.ui.tbl_vibor_rabotn_rasp
        nk_fio = CQT.nom_kol_po_imen(tbl, 'ФИО')
        if self.ui.radioButton_ispoln1.isChecked():
            if self.ui.lbl_ispoln2.text() != tbl.item(tbl.currentRow(), nk_fio).text():
                self.ui.lbl_ispoln1.setText(tbl.item(tbl.currentRow(), nk_fio).text())
        if self.ui.radioButton_ispoln2.isChecked():
            if self.ui.lbl_ispoln1.text() != tbl.item(tbl.currentRow(), nk_fio).text():
                self.ui.lbl_ispoln2.setText(tbl.item(tbl.currentRow(), nk_fio).text())

    @CQT.onerror
    def tbl_nar_raspr_click(self, *args):
        tbl = self.ui.tbl_vibor_nar_rasp
        self.ui.lbl_ispoln1.clear()
        self.ui.lbl_ispoln2.clear()
        self.ui.cmb_prof_rasp.clear()
        self.ui.cmb_prof_rasp.addItem('')
        CQT.clear_tbl(self.ui.tbl_vibor_rabotn_rasp)
        nk_nom_mar = CQT.nom_kol_po_imen(tbl, 'Номер_мк')
        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nk_vneplan = CQT.nom_kol_po_imen(tbl, 'Внеплан')
        self.ui.lbl_vibr_nar.setText(tbl.item(tbl.currentRow(), nk_nom_nar).text())
        nom_mk = int(tbl.item(tbl.currentRow(), nk_nom_mar).text())
        vneplan = int(tbl.item(tbl.currentRow(), nk_vneplan).text())

        set_prof = set()
        spis_dop_prof = F.load_file(F.scfg('Filtr_rab') + F.sep() + 'spis_dop_prof.txt')
        if spis_dop_prof:
            for prof in spis_dop_prof:
                set_prof.add(prof)

        if vneplan == 1:
            for prof in self.DICT_PROFESSIONS.keys():
                set_prof.add(self.DICT_PROFESSIONS[prof]['имя'])
        else:
            res = CMS.load_res(nom_mk)

            if res == False:
                CQT.msgbox(f'Не удалось загрузить ресурнсую попробуй позже')
                return
            for dse in res:
                for oper in dse['Операции']:
                    if oper['Опер_профессия_код'] in self.DICT_PROFESSIONS:
                        set_prof.add( self.DICT_PROFESSIONS[oper['Опер_профессия_код']]['имя'])
        spis_prof = sorted(list(set_prof))
        for prof in spis_prof:
            self.ui.cmb_prof_rasp.addItem(prof)

        CMS.on_section_resized(self)

    @CQT.onerror
    def edit_check_vneplan(self, *args):

        if not CMS.user_access(self.db_naryd, 'создание_корректировка_подтвердить_внеплан',
                               CMS.ima_po_emp(self.glob_login)):
            return
        tbl = self.ui.tbl_red_zhur
        if tbl.currentRow() == -1:
            return
        nk_vneplan = CQT.nom_kol_po_imen(tbl, 'Внеплан')
        vneplan_status = tbl.item(tbl.currentRow(), nk_vneplan).text()

        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nom_nar = tbl.item(tbl.currentRow(), nk_nom_nar).text()

        if vneplan_status == '0':
            CQT.msgbox(f'Наряд {nom_nar} не является внеплановым')
            return


        vneplan_val = CSQ.zapros(self.db_naryd, f"""SELECT Внеплан FROM naryad WHERE Пномер == {int(nom_nar)}""",
                                 one=True)
        if vneplan_val[-1][0] == 1:
            new_status = 2
        else:
            new_status = 1
        zapros = f'''UPDATE naryad SET Внеплан = {new_status} WHERE Пномер == {int(nom_nar)}'''
        CSQ.zapros(self.db_naryd, zapros)

        tbl.item(tbl.currentRow(), nk_vneplan).setText(str(new_status))

    @CQT.onerror
    def edit_check_naruad(self, *args):
        if not CMS.user_access(self.db_naryd, 'создание_корректировка_подтвердить_наряд',
                               CMS.ima_po_emp(self.glob_login)):
            return
        tbl = self.ui.tbl_red_zhur
        if tbl.currentRow() == -1:
            return
        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nk_nom_pr =  CQT.nom_kol_po_imen(tbl, 'Номер_проекта')
        nk_zadanie = CQT.nom_kol_po_imen(tbl, 'Задание')
        nk_fvrem = CQT.nom_kol_po_imen(tbl, 'Фвремя')
        nk_fvrem2 = CQT.nom_kol_po_imen(tbl, 'Фвремя2')
        nom_nar = tbl.item(tbl.currentRow(), nk_nom_nar).text()
        nom_pr = tbl.item(tbl.currentRow(), nk_nom_pr).text()
        zadanie = tbl.item(tbl.currentRow(), nk_zadanie).text()
        fvrem = F.valm(tbl.item(tbl.currentRow(), nk_fvrem).text())
        fvrem2 = F.valm(tbl.item(tbl.currentRow(), nk_fvrem2).text())
        summ_fvrem = round(fvrem + fvrem2,1)
        nk_primech = CQT.nom_kol_po_imen(tbl, 'Примечание')
        primech = tbl.item(tbl.currentRow(), nk_primech).text()

        if not CQT.msgboxgYN(f'Подтверждаю, что наряд №{nom_nar} выполнен в полном объеме'):
            return

        rez = self.check_podtv_naruad(int(nom_nar))
        if rez:
            CQT.msgbox(f'Наряд №{nom_nar} уже подтвержден')
            self.load_table_korr_naruad()

            return
        rez = self.check_zaversh_naruad(int(nom_nar))
        if rez == False:
            CQT.msgbox(f'Наряд №{nom_nar} еще не завершен всеми работниками, подтверждение не возможно')
            self.load_table_korr_naruad()

            return
        if nom_pr == 'ПРОСТОЙ' and zadanie == 'ПРОСТОЙ':
            if primech.strip().lower() == 'прочее' or primech.strip() == '':
                CQT.msgbox('Не указана причина в примечании')
                return
            zapros = f'''UPDATE naryad SET Подтвержд_вып = 1, Подтвержд_вып_дата = "{F.now()}", 
            Подтвержд_вып_фио = "{self.glob_ima}", Твремя = {summ_fvrem} WHERE Пномер == {int(nom_nar)}'''
        else:
            zapros = f'''UPDATE naryad SET Подтвержд_вып = 1, Подтвержд_вып_дата = "{F.now()}", 
            Подтвержд_вып_фио = "{self.glob_ima}" WHERE Пномер == {int(nom_nar)}'''
        CSQ.zapros(self.db_naryd, zapros)
        CQT.msgbox(f'Наряд №{nom_nar} успешно подтвержден')
        self.load_table_korr_naruad()
        self.load_mk()

    @CQT.onerror
    def edit_delete_naruad(self, *args):
        if not CMS.user_access(self.db_naryd, 'создание_корректировка_удалить_наряд', CMS.ima_po_emp(self.glob_login)):
            return
        tbl = self.ui.tbl_red_zhur
        if tbl.currentRow() == -1:
            return
        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nom_nar = tbl.item(tbl.currentRow(), nk_nom_nar).text()
        if not CQT.msgboxgYN(f'Точно удалить наряд №{nom_nar} ?'):
            return
        rez = self.check_nenachat_naruad(int(nom_nar))
        if rez == False:
            CQT.msgbox(f'Наряд №{nom_nar} уже начат, корректировка невозможна')
            self.load_table_korr_naruad()
            return
        rez = self.vernut_v_mk_dse_iz_naryada(int(nom_nar))
        if rez != None:
            otv = CQT.msgboxgYN("Ошибка, удалить наряд невозможно" + '\n'.join(rez) + 'Удалить принудительно?')
            if otv == False:
                return
        zapros = f'''DELETE FROM naryad WHERE Пномер == {int(nom_nar)}'''
        CSQ.zapros(self.db_naryd, zapros)
        CQT.msgbox(f'Наряд №{nom_nar} успешно удален')
        self.load_table_korr_naruad()
        self.load_mk()

    @CQT.onerror
    def vernut_v_mk_dse_iz_naryada(self, nom_nar: int):
        zapros = f'''SELECT naryad.Номер_мк, naryad.ДСЕ, naryad.ДСЕ_ID, naryad.Операции, naryad.Опер_колво, naryad.Внеплан, naryad.Виды_работ
             FROM naryad 
        INNER JOIN mk ON mk.Пномер = naryad.Номер_мк
        WHERE naryad.Пномер == {nom_nar}'''
        rez = CSQ.zapros(self.db_naryd, zapros)
        res = CSQ.zapros(self.db_resxml, f"""SELECT res.data FROM res WHERE res.Номер_мк == {rez[-1][0]}""", one=True)
        if len(res) == 1:
            return
        self.glob_nom_mk = rez[-1][0]
        self.spis_dse = rez[-1][1].split('|')
        self.spis_id = rez[-1][2].split('|')
        self.spis_oper = rez[-1][3].split('|')
        self.spis_kolvo = rez[-1][4].split('|')
        self.spis_vidrab = rez[-1][6].split('|')
        self.glob_res = F.from_binary_pickle(res[-1][0])
        spis_oshibok = []
        for i in range(len(self.spis_dse)):
            fl_id = False
            fl_oper = False
            fl_kol = False
            for j in range(len(self.glob_res)):
                if self.glob_res[j]['Номерпп'] == int(self.spis_id[i]):
                    fl_id = True
                    for k in range(len(self.glob_res[j]['Операции'])):
                        if self.glob_res[j]['Операции'][k]['Опер_номер'] == self.spis_oper[i].split('$')[0]:
                            fl_oper = True
                            if int(self.spis_kolvo[i]) != 0:
                                fl_kol = True
                            if 'Освоено,шт.' in self.glob_res[j]['Операции'][k]:
                                self.glob_res[j]['Операции'][k]['Освоено,шт.'] -= int(self.spis_kolvo[i])
                            break
                    break
            if fl_id == False:
                spis_oshibok.append(f'Не найден ID на {self.spis_dse[i]} - ID {self.spis_id[i]}')
            else:
                if fl_oper == False:
                    spis_oshibok.append(f'Не найдена операция на {self.spis_dse[i]} - операция {self.spis_oper[i]}')
                else:
                    if fl_kol == False:
                        spis_oshibok.append(
                            f'Количество в наряде на {self.spis_dse[i]} - операция {self.spis_oper[i]} -  {self.spis_kolvo[i]} шт.')
        if len(spis_oshibok) > 0:
            return spis_oshibok

        CSQ.zapros(self.db_naryd, f"""UPDATE mk SET Статус == 'Открыта' WHERE Пномер == {int(self.glob_nom_mk)}""")
        CSQ.zapros(self.db_resxml, f"""UPDATE res SET data = ? WHERE Номер_мк == {int(self.glob_nom_mk)}""",
                   spisok_spiskov=[F.to_binary_pickle(self.glob_res)])

        # CSQ.update_bd_sql(self.db_naryd, 'mk', {'Статус': 'Открыта'},
        #                  {'Пномер': int(self.glob_nom_mk)})
        # CSQ.update_bd_sql(self.db_naryd, 'res', {'data': F.to_binary_pickle(self.glob_res)},
        #                  {'Номер_мк': int(self.glob_nom_mk)})
        return

    @CQT.onerror
    def edit_clear_fio(self, *args):
        # if not CMS.user_access(self.db_naryd,'создание_корректировка_удалить_ФИО',CMS.ima_po_emp(self.glob_login)):
        #    return
        tbl = self.ui.tbl_red_zhur
        if tbl.currentRow() == -1:
            return
        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nom_nar = tbl.item(tbl.currentRow(), nk_nom_nar).text()
        if not CQT.msgboxgYN(f'Точно удалить ФИО исполнителей из наряда №{nom_nar} ?'):
            return
        rez = self.check_nenachat_naruad(int(nom_nar))
        if rez == False:
            CQT.msgbox(f'Наряд №{nom_nar} уже начат, корректировка невозможна')
            self.load_table_korr_naruad()
            return
        nk_fio = CQT.nom_kol_po_imen(tbl, 'ФИО')
        nk_fio2 = CQT.nom_kol_po_imen(tbl, 'ФИО2')
        nk_tvrem = CQT.nom_kol_po_imen(tbl, 'Твремя')
        if tbl.item(tbl.currentRow(), nk_fio).text() != "" and tbl.item(tbl.currentRow(), nk_fio2).text() != "":
            tvrem = F.valm(tbl.item(tbl.currentRow(), nk_tvrem).text()) * 2
        else:
            tvrem = F.valm(tbl.item(tbl.currentRow(), nk_tvrem).text())

        zapros = f'''UPDATE naryad SET ФИО="", ФИО2="", Твремя={tvrem}  WHERE Пномер == {int(nom_nar)}'''

        CSQ.zapros(self.db_naryd, zapros)
        CQT.msgbox(f'Наряд №{nom_nar} успешно очищен')
        self.load_table_korr_naruad()

    @CQT.onerror
    def check_podtv_naruad(self, nom_nar: int, conn='', cur=''):
        zapros = f'''SELECT 
             naryad.Подтвержд_вып
         FROM naryad WHERE naryad.Пномер == {nom_nar}'''
        rez = CSQ.zapros(self.db_naryd, zapros, rez_dict=True, one=True)
        if rez['Подтвержд_вып'] == 1:
            return True
        return False

    @CQT.onerror
    def check_zaversh_naruad(self, nom_nar: int, conn='', cur=''):
        zapros = f'''SELECT 
             naryad.ФИО, naryad.Фвремя, naryad.ФИО2, naryad.Фвремя2, naryad.Твремя
         FROM naryad WHERE naryad.Пномер == {nom_nar}'''
        rez = CSQ.zapros(self.db_naryd, zapros, rez_dict=True, one=True)
        if rez['ФИО'] == "" and rez['ФИО2'] == "":
            return False
        fl_zav = True
        if rez['ФИО'] != "":
            if rez['Фвремя'] == '':
                fl_zav = False
        if rez['ФИО2'] != "":
            if rez['Фвремя2'] == '':
                fl_zav = False
        return fl_zav

    @CQT.onerror
    def check_nenachat_naruad(self, nom_nar: int):
        zapros = f'''SELECT jurnal.Пномер
     FROM jurnal WHERE jurnal.Номер_наряда == {nom_nar}'''
        rez = CSQ.zapros(self.db_naryd, zapros)
        if len(rez) > 1:
            return False
        return True

    @CQT.onerror
    def load_table_korr_naruad(self, close_mk=True):
        if self.glob_login == '':
            return
        if close_mk:
            zapros = f'''SELECT mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата, naryad.Автор, naryad.Номер_мк, naryad.Внеплан, naryad.Коэфф_сложности,
naryad.Компл_ФИО, naryad.Задание, naryad.Примечание, naryad.Опер_колво, naryad.Компл_Дата, naryad.Компл_номер_тара, naryad.Компл_адрес,
 naryad.ФИО, naryad.Фвремя, naryad.ФИО2, naryad.Фвремя2, naryad.Твремя, naryad.Подтвержд_вып
  FROM naryad INNER JOIN mk ON mk.Пномер = naryad.Номер_мк WHERE NOT EXISTS(SELECT jurnal.Номер_наряда FROM jurnal) or naryad.Подтвержд_вып = 0 and (mk.Статус != "Закрыта" or mk.Пномер == 0) ; '''
        else:
            zapros = f'''SELECT mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата, naryad.Автор, naryad.Номер_мк, naryad.Внеплан, naryad.Коэфф_сложности,
            naryad.Компл_ФИО, naryad.Задание, naryad.Примечание, naryad.Операции, naryad.Опер_колво, naryad.Компл_Дата, naryad.Компл_номер_тара, naryad.Компл_адрес,
             naryad.ФИО, naryad.Фвремя, naryad.ФИО2, naryad.Фвремя2, naryad.Твремя, naryad.Подтвержд_вып, jurnal.Дата as Дата_журнал, jurnal.ФИО, jurnal.Статус, jurnal.Примечание
              FROM naryad 
              JOIN mk ON mk.Пномер = naryad.Номер_мк 
              INNER JOIN jurnal ON jurnal.Номер_наряда = naryad.Пномер WHERE jurnal.Статус == 'Завершен' or mk.Пномер == 0 
              ; '''
        rez = CSQ.zapros(self.db_naryd, zapros)
        edit_columns = {F.nom_kol_po_im_v_shap(rez, 'Коэфф_сложности'), F.nom_kol_po_im_v_shap(rez, 'Твремя'), F.nom_kol_po_im_v_shap(rez, 'Примечание')}
        CQT.zapoln_wtabl(self, rez, self.ui.tbl_red_zhur, isp_shapka=True, separ='', select_last_row=False,
                         set_editeble_col_nomera=edit_columns)
        CMS.zapolnit_filtr(self, self.ui.tbl_red_zhur_filtr, self.ui.tbl_red_zhur)
        CQT.cvet_cell_wtabl(self.ui.tbl_red_zhur, 'Внеплан', '', '2', 200, 240, 200)
        CQT.cvet_cell_wtabl(self.ui.tbl_red_zhur, 'Внеплан', '', '1', 240, 200, 200)


    @CQT.onerror
    def edit_red_zhur_koef_sl(self, r, c):
        #if self.ui.tbl_red_zhur.hasFocus() == False:
        #    return
        nk_pnom = CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Пномер')
        nk_zadanie = CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Задание')
        if c == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Коэфф_сложности'):
            if not CMS.user_access(self.db_naryd, 'создание_корректировка_подтвердить_внеплан',
                                   CMS.ima_po_emp(self.glob_login)):
                rez = CSQ.zapros(self.db_naryd,
                                 f"""SELECT Коэфф_сложности FROM naryad WHERE Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""",
                                 rez_dict=True, one=True)
                self.ui.tbl_red_zhur.item(r, c).setText(str(rez['Коэфф_сложности']))
                return
            if F.is_numeric(self.ui.tbl_red_zhur.item(r, c).text()) == False:
                CQT.msgbox(f'Введено не число')
                rez = CSQ.zapros(self.db_naryd,
                                 f"""SELECT Коэфф_сложности FROM naryad WHERE Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""",
                                 rez_dict=True, one=True)
                self.ui.tbl_red_zhur.item(r, c).setText(str(rez['Коэфф_сложности']))
                return
            rez = CSQ.zapros(self.db_naryd, f"""UPDATE naryad SET Коэфф_сложности 
            = {float(self.ui.tbl_red_zhur.item(r, c).text())} WHERE 
            Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""")

        if c == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Твремя'):
            if not CMS.user_access(self.db_naryd, 'создание_корректировка_норма_внеплан',
                                   CMS.ima_po_emp(self.glob_login)) or self.ui.tbl_red_zhur.item(r, nk_zadanie).text() == 'ПРОСТОЙ':
                rez = CSQ.zapros(self.db_naryd,
                                 f"""SELECT Твремя FROM naryad WHERE Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""",
                                 rez_dict=True, one=True)
                self.ui.tbl_red_zhur.item(r, c).setText(str(rez['Твремя']))
                return

            if F.is_numeric(self.ui.tbl_red_zhur.item(r, c).text()) == False:
                rez = CSQ.zapros(self.db_naryd,
                                 f"""SELECT Твремя FROM naryad WHERE Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""",
                                 rez_dict=True, one=True)
                self.ui.tbl_red_zhur.item(r, c).setText(str(rez['Твремя']))
                CQT.msgbox(f'Введено не число')
                return

            rez = CSQ.zapros(self.db_naryd, f"""UPDATE naryad SET Твремя 
            = {float(self.ui.tbl_red_zhur.item(r, c).text())} , Опер_время 
            = {float(self.ui.tbl_red_zhur.item(r, c).text())} WHERE 
            Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""")

        if c == CQT.nom_kol_po_imen(self.ui.tbl_red_zhur, 'Примечание'):
            if not CMS.user_access(self.db_naryd, 'создание_корректировка_подтвердить_наряд',
                                   CMS.ima_po_emp(self.glob_login)) or self.ui.tbl_red_zhur.item(r, nk_zadanie).text() != 'ПРОСТОЙ':
                rez = CSQ.zapros(self.db_naryd,
                                 f"""SELECT Примечание FROM naryad WHERE Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""",
                                 rez_dict=True, one=True)
                self.ui.tbl_red_zhur.item(r, c).setText(str(rez['Примечание']))
                return

            rez = CSQ.zapros(self.db_naryd, f"""UPDATE naryad SET Примечание 
            = {self.ui.tbl_red_zhur.item(r, c).text()} WHERE 
            Пномер == {int(self.ui.tbl_red_zhur.item(r, nk_pnom).text())}""")

    @CQT.onerror
    def load_table_raspred_nar(self, conn='', cur=''):
        if self.glob_login == '':
            return
        self.ui.radioButton_ispoln1.setChecked(True)
        zapros = f'''
                SELECT  mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата, naryad.Автор, naryad.Номер_мк,
naryad.Внеплан, naryad.Компл_ФИО, naryad.Задание, naryad.Примечание, naryad.Компл_Дата, naryad.Компл_номер_тара, naryad.Компл_адрес,
                                                 naryad.Твремя, naryad.Операции
                                                 FROM naryad INNER JOIN mk ON naryad.Номер_мк == mk.Пномер WHERE Компл_ФИО !="" 
                                                 and Компл_Дата !="" and ФИО == "" and ФИО2 == ""  and mk.Статус != "Закрыта"'''
        rez = CSQ.zapros(self.db_naryd, zapros, conn=conn, cur=cur)

        CQT.zapoln_wtabl(self, rez, self.ui.tbl_vibor_nar_rasp, isp_shapka=True, separ='', select_last_row=False)
        CMS.zapolnit_filtr(self, self.ui.tbl_filtr_vibor_nar_rasp, self.ui.tbl_vibor_nar_rasp)
        CMS.load_column_widths(self, self.ui.tbl_vibor_nar_rasp)

    @CQT.onerror
    def load_table_prosm_nar(self, check_mk=True):
        if self.glob_login == '':
            return
        if check_mk == True:
            zapros = f'''
                        SELECT mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата,naryad.Автор,
naryad.Номер_мк,naryad.Внеплан,naryad.Компл_ФИО,naryad.Задание, naryad.Номер_замечания_журнал, naryad.Примечание,naryad.Компл_Дата,
naryad.Компл_номер_тара,naryad.Компл_адрес,
                                        naryad.ФИО,naryad.Фвремя,naryad.ФИО2,naryad.Фвремя2,naryad.Твремя, 
naryad.Операции, naryad.Опер_колво, naryad.Опер_время, naryad.Коэфф_сложности, naryad.Подтвержд_вып
                                         FROM naryad INNER JOIN mk ON naryad.Номер_мк == mk.Пномер WHERE mk.Статус != "Закрыта"'''
        else:
            zapros = f'''
                                    SELECT mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата,naryad.Автор,
            naryad.Номер_мк,naryad.Внеплан,naryad.Компл_ФИО,naryad.Задание, naryad.Номер_замечания_журнал,naryad.Примечание,naryad.Компл_Дата,
            naryad.Компл_номер_тара,naryad.Компл_адрес,
                                                    naryad.ФИО,naryad.Фвремя,naryad.ФИО2,naryad.Фвремя2,naryad.Твремя, 
            naryad.Операции, naryad.Опер_колво, naryad.Опер_время, naryad.Коэфф_сложности, naryad.Подтвержд_вып
                                                     FROM naryad INNER JOIN mk ON naryad.Номер_мк == mk.Пномер'''
        rez = CSQ.zapros(self.db_naryd, zapros)
        if rez == False:
            CQT.msgbox(f'БД занята, пробуй позже')
            return
        set_edit = 0
        if CMS.user_access(self.db_naryd, 'создание_просмотр_корр_внеплан_ксложн_подввып',
                           CMS.ima_po_emp(self.glob_login), False):
            set_edit = {F.nom_kol_po_im_v_shap(rez, 'Внеплан'),
                        F.nom_kol_po_im_v_shap(rez, 'Коэфф_сложности'),
                        F.nom_kol_po_im_v_shap(rez, 'Подтвержд_вып'), }

        CQT.zapoln_wtabl(self, rez, self.ui.tbl_prosmotr_nar, isp_shapka=True, separ='',
                         set_editeble_col_nomera=set_edit, select_last_row=True)
        self.ui.tbl_prosmotr_nar.hideColumn(CQT.nom_kol_po_imen(self.ui.tbl_prosmotr_nar, 'Операции'))
        self.ui.tbl_prosmotr_nar.hideColumn(CQT.nom_kol_po_imen(self.ui.tbl_prosmotr_nar, 'Опер_колво'))
        self.ui.tbl_prosmotr_nar.hideColumn(CQT.nom_kol_po_imen(self.ui.tbl_prosmotr_nar, 'Опер_время'))

        CMS.zapolnit_filtr(self, self.ui.tbl_filtr_prosmotr_nar, self.ui.tbl_prosmotr_nar)
        CMS.load_column_widths(self, self.ui.tbl_prosmotr_nar)
        """CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar,'Внеплан','1',r=222,g=100,b=100)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar,'Внеплан','2',r=100,g=222,b=100)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar,'Подтвержд_вып','0',r=222,g=100,b=100)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar,'Подтвержд_вып','1',r=100,g=222,b=100)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar, 'Коэфф_сложности', '1.3', r=241, g=246, b=210)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar, 'Коэфф_сложности', '1.5', r=219, g=245, b=211)
        CQT.cvet_cell_wtabl(self.ui.tbl_prosmotr_nar, 'Коэфф_сложности', '1.95', r=172, g=247, b=160)"""

    @CQT.onerror
    def edit_koeff_nar_tbl(self, row, column, *args):
        tbl = self.ui.tbl_prosmotr_nar
        if tbl.hasFocus() == True:
            if tbl.currentRow() == -1:
                return
            name = tbl.horizontalHeaderItem(column).text()
            self.edit_koeff_nar(name)

    @CQT.onerror
    def edit_koeff_nar(self, ima=''):
        if ima == '':
            return
        tbl = self.ui.tbl_prosmotr_nar
        row = tbl.currentRow()
        nk_nom_nar = CQT.nom_kol_po_imen(tbl, 'Пномер')
        nk_ima = CQT.nom_kol_po_imen(tbl, ima)
        if nk_nom_nar == None:
            CQT.msgbox('Не найдена колонка Пномер')
            return
        if nk_ima == None:
            CQT.msgbox(f'Не найдена колонка {ima}')
            return
        if CMS.user_access(self.db_naryd, 'создание_просмотр_корр_внеплан_ксложн_подввып',
                           CMS.ima_po_emp(self.glob_login)):
            if F.is_numeric(tbl.item(row, nk_ima).text()) == False:
                CQT.msgbox(f'{tbl.item(row, nk_ima).text()} не число')
                return
            ima_val = F.valm(tbl.item(row, nk_ima).text())
            nom_nar = int(tbl.item(row, nk_nom_nar).text())
            zapros = f'''UPDATE naryad SET {ima} = {ima_val} WHERE Пномер == {nom_nar}'''
            rez = CSQ.zapros(self.db_naryd, zapros)
            self.ui.tbl_prosmotr_nar.item(row, nk_ima).setText(str(ima_val))
        else:
            rez = CSQ.zapros(self.db_naryd,
                             f"""SELECT {ima} FROM naryad WHERE Пномер == {int(self.ui.tbl_prosmotr_nar.item(row, nk_nom_nar).text())}""",
                             rez_dict=True, one=True)
            self.ui.tbl_prosmotr_nar.item(row, nk_ima).setText(str(rez[ima]))
            # self.load_table_prosm_nar()

    @CQT.onerror
    def load_table_komplekt(self):
        if self.glob_login == "":
            return
        zapros = f'''SELECT mk.Номер_проекта, mk.Номер_заказа, naryad.Пномер, naryad.Дата, naryad.Автор, 
        naryad.Номер_мк, naryad.Компл_ФИО, naryad.Компл_Дата, naryad.Компл_номер_тара, naryad.Компл_адрес, naryad.Твремя,
                                 naryad.Примечание,  naryad.ДСЕ, naryad.Операции,
                                 naryad.Опер_колво FROM naryad  INNER JOIN mk ON naryad.Номер_мк == mk.Пномер 
                                WHERE Компл_ФИО =="" and Компл_Дата =="" and mk.Статус != "Закрыта"'''
        rez = CSQ.zapros(self.db_naryd, zapros)
        if rez == False:
            CQT.msgbox(f'Не удалось загрузить данные попробуй еще раз')
            return
        red = {F.nom_kol_po_im_v_shap(rez, 'Компл_Дата') + 1, F.nom_kol_po_im_v_shap(rez, 'Компл_номер_тара') + 1}

        CQT.zapoln_wtabl(self, rez, self.ui.tbl_komplektovka, isp_shapka=True, separ='', set_editeble_col_nomera=red,
                         ogr_maxshir_kol=400, select_last_row=True)

        CMS.zapolnit_filtr(self, self.ui.tbl_filtr_komplektovka, self.ui.tbl_komplektovka)
        CQT.clear_tbl(self.ui.tbl_komplektovka_view)
        self.ui.lbl_kompl_info.clear()

    @CQT.onerror
    def btn_prosm_edit_time_clear_fio(self,field_name, *args):
        tbl = self.ui.tbl_prosmotr_nar
        autor_nar = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Автор')).text()
        if not CMS.user_access(self.db_naryd,f'создание_корректировка_журнал_работ_{autor_nar}',CMS.ima_po_emp(self.glob_login)):
            return
        if tbl.currentRow() == -1:
            CQT.msgbox(f'Не выбрана запись в списке нарядов')
            return
        fio = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, field_name)).text()
        nom_nar = int(tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Пномер')).text())
        if fio == '':
            CQT.msgbox(f'{field_name} - пусто')
            return
        rez = CSQ.zapros(self.db_naryd,f"""SELECT Пномер FROM jurnal WHERE Номер_наряда == {nom_nar} AND ФИО == '{fio}' """)
        if rez == False:
            CQT.msgbox(f'ОШикба загрузки бд, попробуй позже')
            return
        if len(rez) >= 2:
            CQT.msgbox(f'Нелья удалить исполнителя проводившего работы')
            return
        rez = CSQ.zapros(self.db_naryd,f"""SELECT * FROM naryad WHERE Пномер = {nom_nar}""",rez_dict=True)
        if rez == False:
            CQT.msgbox(f'ОШикба загрузки бд, попробуй позже')
            return
        if rez[0]['ФИО'] != '' and rez[0]['ФИО2'] != '':
            double_time = rez[0]['Твремя']*2
            rez = CSQ.zapros(self.db_naryd,f"""UPDATE naryad SET {field_name} = '', Твремя = {double_time} WHERE Пномер = {nom_nar} """)
            tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Твремя')).setText(str(double_time))
        else:
            rez = CSQ.zapros(self.db_naryd, f"""UPDATE naryad SET {field_name} = '' WHERE Пномер = {nom_nar} """)
        tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, field_name)).setText('')
        CQT.msgbox(f'Удачно удален {fio} из {field_name}')

    @CQT.onerror
    def edit_time_jur_btn(self, *args):
        if not CQT.msgboxgYN(f'Точно изменить запись на\n\t"{self.ui.cmb_edit_time_jur.currentText()}"\nи '
                             f'время на:\n\t "{self.ui.dt_edit_time_jur.text()}"'):
            return
        tbl = self.ui.tbl_prosmotr_nar
        autor_nar = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Автор')).text()
        if not CMS.user_access(self.db_naryd,f'создание_корректировка_журнал_работ_{autor_nar}',CMS.ima_po_emp(self.glob_login)):
            if not CMS.user_access(self.db_naryd, f'создание_корректировка_журнал_работ',
                                   CMS.ima_po_emp(self.glob_login)):
                return
        tbl = self.ui.tbl_prosmotr_nar_jurnal
        tbl_nar = self.ui.tbl_prosmotr_nar
        if tbl.currentRow() == -1:
            CQT.msgbox(f'Не выбрана запись в журнале')
            return
        if self.ui.cmb_edit_time_jur.currentText() == '':
            CQT.msgbox(f'Статус не может быть пусто')
            return
        nom_nar = int(tbl.item(tbl.currentRow(),CQT.nom_kol_po_imen(tbl,'Номер_наряда')).text())
        por_nom = int(tbl.item(tbl.currentRow(),CQT.nom_kol_po_imen(tbl,'Пномер')).text())
        fio = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'ФИО')).text()

        list_zap= CSQ.zapros(self.db_naryd,f"""SELECT * FROM jurnal WHERE Номер_наряда = {nom_nar} AND ФИО = '{fio}';""",rez_dict=True)
        if list_zap == False:
            CQT.msgbox(f'Не удалось выгрузить журнал')
            return
        list_zap.insert(0, CPY.deepcopy(list_zap[0]))
        list_zap[0]['Дата'] = '2000-02-03 22:50:32'
        list_zap[0]['Пномер'] = -1
        list_zap[0]['Статус'] = ''
        list_zap.append(CPY.deepcopy(list_zap[-1]))
        list_zap[-1]['Дата'] = '2123-02-03 22:50:32'
        list_zap[-1]['Пномер'] = -1
        list_zap[-1]['Статус'] = ''
        flag = False
        for i, item in enumerate(list_zap):
            if item['Пномер'] == por_nom:
                flag = True
                middle = self.ui.dt_edit_time_jur.text()
                middle_status = self.ui.cmb_edit_time_jur.currentText()
                old_status = list_zap[i]['Статус']
                nach = list_zap[i-1]['Дата']
                nach_status = list_zap[i-1]['Статус']
                nach_pnom = list_zap[i-1]['Пномер']
                kon = list_zap[i+1]['Дата']
                kon_status = list_zap[i + 1]['Статус']
                kon_pnom = list_zap[i + 1]['Пномер']
                break
        if flag == False:
            CQT.msgbox(f'Не найден номер строки')
            return
        nach =F.date_add_time(F.strtodate(nach),'',minutes=1)
        kon = F.date_add_time(F.strtodate(kon),'',minutes=-1)
        middle = F.strtodate(middle)
        if middle <= nach:
            CQT.msgbox(f'Не может быть меньше {nach}')
            return
        if middle >= kon:
            CQT.msgbox(f'Не может быть больше {kon}')
            return

        if middle_status == 'Начат':
            if nach_status == 'Начат':
                CQT.msgbox(f'Нельзя начать два раза')
                return
            if nach_status == 'Завершен':
                CQT.msgbox(f'Нельзя начать после завершения')
                return
            if kon_status == 'Начат':
                CQT.msgbox(f'Нельзя начать два раза')
                return
        if middle_status == 'Приостановлен':
            if nach_status == 'Приостановлен':
                CQT.msgbox(f'Нельзя приостановить два раза')
                return
            if nach_status == 'Завершен':
                CQT.msgbox(f'Нельзя приостановить после завершения')
                return
            if kon_status == 'Приостановлен':
                CQT.msgbox(f'Нельзя приостановить два раза')
                return
            if kon_status == 'Завершен':
                CQT.msgbox(f'Нельзя приостановить до завершения')
                return
        if middle_status == 'Завершен':
            if nach_status == 'Приостановлен':
                CQT.msgbox(f'Нельзя заврешить после приостановки')
                return
            if nach_status == 'Завершен':
                CQT.msgbox(f'Нельзя заврешить после завершения')
                return
            if kon_status == 'Приостановлен':
                CQT.msgbox(f'Нельзя заврешить до приостановки')
                return
            if kon_status == 'Завершен':
                CQT.msgbox(f'Нельзя заврешить до завершения')
                return
            if kon_status == 'Начат':
                CQT.msgbox(f'Нельзя заврешить до начала')
                return

        rez = CSQ.zapros(self.db_naryd,f"""UPDATE jurnal SET Дата = '{F.datetostr(middle)}' , Статус = '{middle_status}' WHERE Пномер = {por_nom};""")
        if rez == False:
            CQT.msgbox(f'ОШибка, не занесено')
            return
        if middle_status == 'Приостановлен' or middle_status == 'Завершен':
            delta = middle - nach
            minutes = round(delta.seconds/60)
            rez = CSQ.zapros(self.db_naryd,
                             f"""UPDATE jurnal SET Подытог = {minutes} WHERE Пномер = {nach_pnom};""")
        if middle_status == 'Начат':
            delta = kon - middle
            minutes = round(delta.seconds / 60)
            rez = CSQ.zapros(self.db_naryd,
                             f"""UPDATE jurnal SET Подытог = {minutes} WHERE Пномер = {por_nom};""")

        rez = CSQ.zapros(self.db_naryd,
                         f"""SELECT Пномер FROM jurnal WHERE Номер_наряда = {nom_nar} AND ФИО = '{fio}' and Статус = 'Завершен';""")
        if rez == False:
            CQT.msgbox(f'Ошибка выгрузки в наряд попробуй еще')
            return
        if len(rez) >= 2:
            zapros = f'''SELECT sum(Подытог) AS "Total Salary"
                                                          FROM jurnal
                                                         WHERE ФИО == "{fio}" AND Статус == "Начат" 
                                                        AND Номер_наряда == {nom_nar}'''
            fact_vr = CSQ.zapros(self.db_naryd, zapros)[-1][0]
            fact_vr = int(fact_vr)
            zapros = f'UPDATE naryad SET Фвремя == {fact_vr} WHERE ФИО == "{fio}" AND Пномер == {nom_nar}'
            CSQ.zapros(self.db_naryd, zapros)
            zapros = f'UPDATE naryad SET Фвремя2 == {fact_vr} WHERE ФИО2 == "{fio}" AND Пномер == {nom_nar}'
            CSQ.zapros(self.db_naryd, zapros)
        else:
            zapros = f'UPDATE naryad SET Фвремя == "" WHERE ФИО == "{fio}" AND Пномер == {nom_nar}'
            CSQ.zapros(self.db_naryd, zapros)
            zapros = f'UPDATE naryad SET Фвремя2 == "" WHERE ФИО2 == "{fio}" AND Пномер == {nom_nar}'
            CSQ.zapros(self.db_naryd, zapros)
        tbl.item(tbl.currentRow(),CQT.nom_kol_po_imen(tbl,'Дата')).setText(F.datetostr(middle))
        tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Статус')).setText(middle_status)
        CQT.msgbox(f'Успешно')
    
    def bold_in_marsh_selected_dse(self):
        tbl_dse = self.ui.tbl_dse
        list_dse = CQT.spisok_iz_wtabl(tbl_dse, shapka=True)
        nk_check = F.nom_kol_po_im_v_shap(list_dse, 'Чек')
        list_marsh = CQT.spisok_iz_wtabl(self.ui.tbl_select_marsh, shapka=True)
        nk_id = F.nom_kol_po_im_v_shap(list_marsh, 'id')
        for i in range(1, len(list_marsh)):
           #i_id = list_marsh[i][nk_id]
            for j in range(3, len(list_marsh[i])):
                if list_marsh[i][j] == '':
                    continue
                nom_strok = self.get_dict_from_tbl_marsh(i, j,list=list_marsh, key='nom_strok')
                if nom_strok == None:
                    continue
                #nom_strok = self.dict_dse_for_marsh[i_id]['nom_strok']
                if list_dse[nom_strok+1][nk_check] == '1':
                    CQT.font_cell_size_format(self.ui.tbl_select_marsh,i-1,j,bold=True)
                else:
                    CQT.font_cell_size_format(self.ui.tbl_select_marsh,i-1,j,bold=False)


    def tbl_select_marsh_dblclk(self):
        tbl = self.ui.tbl_select_marsh
        r = tbl.currentRow()
        c = tbl.currentColumn()
        if c <= 2:
            tbl.setToolTip('')
            nk_id = CQT.nom_kol_po_imen(tbl, 'id')
            id = tbl.item(r, nk_id).text()
            tbl_dse = self.ui.tbl_dse

            nk_nom_id = CQT.nom_kol_po_imen(tbl_dse, 'ID')
            for i in range(tbl_dse.rowCount()):
                if tbl_dse.item(i, nk_nom_id).text() == id:
                    CQT.select_cell(tbl_dse,i,1)
                    break
            return
        if tbl.item(r, c).text() == '':
            tbl.setToolTip('')

            return
        nom_oper = self.get_dict_from_tbl_marsh(r+1, c,key='Номер операции')
        nk_id = CQT.nom_kol_po_imen(tbl, 'id')
        id = tbl.item(r,nk_id).text()
        tbl_dse = self.ui.tbl_dse
        nk_nom_oper = CQT.nom_kol_po_imen(tbl_dse,'Ном_оп')
        nk_nom_id = CQT.nom_kol_po_imen(tbl_dse, 'ID')
        for i in range(tbl_dse.rowCount()):
            if tbl_dse.item(i,nk_nom_oper).text() == nom_oper and tbl_dse.item(i,nk_nom_id).text() == id:
                self.select_dse(0,i)
                self.bold_in_marsh_selected_dse()
                return

        CQT.msgbox(f'Ошибка')



    def tbl_select_marsh_clk(self):
        tbl = self.ui.tbl_select_marsh
        r = tbl.currentRow()
        c = tbl.currentColumn()
        if c <= 2:
            tbl.setToolTip('')
            return
        if tbl.item(r,c).text() == '':
            tbl.setToolTip('')
            return
        txt = self.get_dict_from_tbl_marsh(r+1,c)
        tbl.setToolTip(pprint.pformat(txt))
        
    

    @CQT.onerror
    def tbl_prosmotr_nar_jurnal_clk(self, *args):
        self.TIME_DEAL = 5
        tbl = self.ui.tbl_prosmotr_nar_jurnal
        old_date = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Дата')).text()
        old_status = tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Статус')).text()
        dt_old_date = F.strtodate(old_date)
        cld = self.ui.cal_edit_time_jur
        cld.setSelectedDate(dt_old_date)
        pl = self.ui.hs_edit_time_jur
        pl.setMinimum(0)
        pl.setMaximum(int(24 * 60 / self.TIME_DEAL))
        val_time = dt_old_date.hour * 60 + dt_old_date.minute
        val_time = val_time // self.TIME_DEAL
        pl.setValue(val_time)
        pl.setTickInterval(self.TIME_DEAL)
        self.set_dt_line_jur_edit(self.TIME_DEAL)
        self.ui.cmb_edit_time_jur.setCurrentText(old_status)
    @CQT.onerror
    def edit_time_jur_time_change(self, *args):
        if self.ui.hs_edit_time_jur.hasFocus():
            self.set_dt_line_jur_edit(self.TIME_DEAL)
    @CQT.onerror
    def edit_date_jur_time_change(self, *args):
        if self.ui.cal_edit_time_jur.hasFocus():
            self.set_dt_line_jur_edit(self.TIME_DEAL)

    @CQT.onerror
    def set_dt_line_jur_edit(self, time_deal, *args):
        cld = self.ui.cal_edit_time_jur
        pl = self.ui.hs_edit_time_jur
        dt_line = self.ui.dt_edit_time_jur
        date = cld.selectedDate()
        date = date.toPyDate()
        minutes = pl.value()*time_deal
        hour =  minutes//60
        minute = minutes - 60*hour
        date_and_time = F.date_to_datetime(date,hour=hour,minute=minute)
        dt_line.setDateTime(date_and_time)

    @CQT.onerror
    def dblclick_brak(self, *args):
        # tabl_mk = self.ui.tableWidget_vibor_det
        # tabl_sp_mk = self.ui.tableWidget_vibor_mk
        tabl_vib_brak = self.ui.tbl_brak
        if tabl_vib_brak.currentIndex() == -1:
            return
        row = tabl_vib_brak.currentRow()
        nk_nom_nar = CQT.nom_kol_po_imen(tabl_vib_brak, 'Номер_наряда')
        nk_nom_act = CQT.nom_kol_po_imen(tabl_vib_brak, 'Пномер')
        nk_text = CQT.nom_kol_po_imen(tabl_vib_brak, 'Вид_брака')
        nk_kolvo = CQT.nom_kol_po_imen(tabl_vib_brak, 'Количество')

        nom_nar = tabl_vib_brak.item(row, nk_nom_nar).text()
        nom_nar = tabl_vib_brak.item(row, nk_nom_nar).text()
        N_act = tabl_vib_brak.item(row, nk_nom_act).text()
        brak_t = tabl_vib_brak.item(row, nk_text).text()
        kol_det_brak = tabl_vib_brak.item(row, nk_kolvo).text()

        if F.is_numeric(kol_det_brak) == False:
            kol_det_brak = 1
        n_k = CQT.nom_kol_po_imen(tabl_vib_brak, 'Фото')
        if tabl_vib_brak.currentColumn() == n_k:
            if tabl_vib_brak.item(row, n_k).text() != "":
                sp_foto = tabl_vib_brak.item(row, n_k).text().split(')(')
                sp_pap = F.spis_files(F.scfg('foto_brak'))[0][1]
                for j in range(len(sp_foto)):
                    sp_foto[j] = sp_foto[j].replace(')', '')
                    sp_foto[j] = sp_foto[j].replace('(', '')
                    for i in range(len(sp_pap)):
                        if F.nalich_file(F.scfg('foto_brak') + os.sep + sp_pap[i] + os.sep + sp_foto[j]) == True:
                            F.zapyst_file(F.scfg('foto_brak') + os.sep + sp_pap[i] + os.sep + sp_foto[j])
                return
        n_k = CQT.nom_kol_po_imen(tabl_vib_brak, 'Категория_брака')
        if tabl_vib_brak.item(row, n_k).text() == "Неисправимый":
            CQT.msgbox('Брак неисправимый! Необходимо заказать ДСЕ на новое изготовление через служебную по форме ПДО')
            return

        if self.glob_nom_mk == 0:
            CQT.msgbox('Не выбрана мк')
            self.ui.tabWidget_2.setCurrentIndex(0)
            return
        msg = "Акт №" + N_act + " по наряду №" + nom_nar + "(" + brak_t + ")"
        if self.check_nalich_narad_po_ispravl(msg):
            return
        self.ui.tabWidget_2.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget_2, 'Наряд'))
        self.select_last_dse()
        self.raschet_naruada(prinuditelno=True)
        self.ui.lineEdit_cr_nar_norma.setEnabled(True)
        self.ui.lineEdit_cr_nar_kolvo.setText(str(kol_det_brak))
        self.ui.checkBox_vneplan_rab.setChecked(True)

        self.ui.plainTextEdit_zadanie.setPlainText('Исправление ' + msg + ' Инструкции у цехового технолога')
        self.ui.plainTextEdit_zadanie.setReadOnly(True)
        self.ui.plainTextEdit_primechanie.setPlainText(msg)

    @CQT.onerror
    def check_nalich_narad_po_ispravl(self, msg):
        '''Проверка создан ли ранее наряд на исправление'''
        zapros = f'''SELECT Пномер FROM naryad WHERE Номер_мк == {self.glob_nom_mk} AND Внеплан != 0 AND Задание LIKE "%{msg}%" '''
        rez = CSQ.zapros(self.db_naryd, zapros)
        if len(rez) == 2:
            nomer = rez[-1][0]
            CQT.msgbox(f'Наряд на исправление уже создан ранее: №{nomer} ')
            return True
        return False

    @CQT.onerror
    def select_last_dse(self):
        tbl = self.ui.tbl_dse
        self.load_mk()
        # self.ui.tabWidget_2.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget_2, 'ДСЕ'))
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        tbl.cellWidget(tbl.rowCount() - 1, nk_check).setChecked(True)
        tbl.item(tbl.rowCount() - 1, nk_check).setText('1')

    @CQT.onerror
    def click_vneplan(self, val, *args):
        if val == False:
            self.ui.plainTextEdit_zadanie.clear()
            self.ui.plainTextEdit_zadanie.setReadOnly(True)
            self.ui.lineEdit_cr_nar_norma.clear()
            # self.ui.lineEdit_cr_nar_norma.setEnabled(False)
            self.ui.lineEdit_cr_nar_kolvo.clear()
            self.ui.lineEdit_cr_nar_kolvo.setEnabled(False)
        else:
            self.ui.plainTextEdit_zadanie.clear()
            self.ui.plainTextEdit_zadanie.setReadOnly(False)
            self.ui.lineEdit_cr_nar_norma.clear()
            # self.ui.lineEdit_cr_nar_norma.setEnabled(True)
            self.ui.lineEdit_cr_nar_norma.setText('0')
            self.ui.lineEdit_cr_nar_kolvo.clear()
            self.ui.lineEdit_cr_nar_kolvo.setEnabled(True)

    @CQT.onerror
    def load_brak(self):
        if self.glob_nom_mk == 0:
            return
        zapros = f'''SELECT Пномер,Инициатор,
        Дата,Номер_наряда,Фото,Вид_брака,Категория_брака,
        Примечание,Количество FROM act WHERE Наряд_исправления == "" AND Номер_наряда != ""'''
        rez = CSQ.zapros(self.db_act, zapros)
        nk_nom_nar = F.nom_kol_po_im_v_shap(rez, 'Номер_наряда')
        spis = [rez[0]]
        # zapros = F'''SELECT Номер_мк FROM naryad WHERE Пномер == {int(rez[i][nk_nom_nar])}'''
        # sp_nom_mk = CSQ.zapros(self.db_naryd, zapros, conn)
        zapros = F'''SELECT Номер_мк, Пномер FROM naryad'''
        sp_nom_mk = CSQ.zapros(self.db_naryd, zapros, rez_dict=True)
        if sp_nom_mk == False:
            CQT.msgbox(f'Не найдено')
            return
        dict_mk = F.raskrit_dict(sp_nom_mk, 'Пномер')
        for i in range(1, len(rez)):
            if rez[i][nk_nom_nar] in dict_mk:
                nom_mk = dict_mk[rez[i][nk_nom_nar]]
                if self.glob_nom_mk == nom_mk:
                    spis.append(rez[i])
        CQT.zapoln_wtabl(self, spis, self.ui.tbl_brak, isp_shapka=True, separ='', ogr_maxshir_kol=600)

    @CQT.onerror
    def min_rejim(self, val, *args):
        if self.glob_login == '':
            return
        tbl = self.ui.tbl_dse
        if tbl.rowCount() == 0:
            return
        nk_osv = CQT.nom_kol_po_imen(tbl, 'Освоено,шт.')
        nk_kol = CQT.nom_kol_po_imen(tbl, 'Количество,шт.')
        if val == 2:
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Масса/М1,М2,М3'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Освоено,шт.'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Ссылка'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'ПКИ'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Ном_оп'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Оборудование'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Документы'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Переходы'), True)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Уровень'), True)
            for i in range(tbl.rowCount()):
                if tbl.item(i, nk_osv).text() == tbl.item(i, nk_kol).text():
                    tbl.setRowHidden(i, True)
                else:
                    tbl.setRowHidden(i, False)
        else:
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Масса/М1,М2,М3'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Освоено,шт.'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Ссылка'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'ПКИ'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Ном_оп'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Оборудование'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Документы'), False)
            tbl.setColumnHidden(CQT.nom_kol_po_imen(tbl, 'Переходы'), False)
            for i in range(tbl.rowCount()):
                tbl.setRowHidden(i, False)

    @CQT.onerror
    def select_etap_dse(self, i, *args):
        text = self.ui.cmb_etapi.itemText(i)
        tblf = self.ui.tbl_filtr_dse
        nk_imaop = CQT.nom_kol_po_imen(tblf, 'Операция')
        tblf.item(0, nk_imaop).setText(text)
        CMS.primenit_filtr(self, tblf, self.ui.tbl_dse)

    @CQT.onerror
    def select_etap_mat(self, i, *args):
        text = self.ui.cmb_mat.itemText(i)
        tblf = self.ui.tbl_filtr_dse
        nk_mat = CQT.nom_kol_po_imen(tblf, 'Масса/М1,М2,М3')
        tblf.item(0, nk_mat).setText(text)
        CMS.primenit_filtr(self, tblf, self.ui.tbl_dse)

    @CQT.onerror
    def load_podbor_marsh(self,res,*args):

        def fill_table_marsh(self, res):
            #tbl= self.ui.tbl_dse
            #tbl_m = self.ui.tbl_podb_marsh
            list_mar = [['дсе']]
            for rc in self.DICT_RC.keys():
                if rc[0] == '0' and rc[-2:] != '00':
                    list_mar[0].append(rc)
            res_rev = reversed(res)
            set_mar_neformat = set()
            set_rc = set()
            dict_dse_marh = dict()
            for dse in res_rev:
                dse_name = f"{dse['Номенклатурный_номер']} {dse['Наименование']}"
                tmp_mar = []
                for oper in dse['Операции']:
                    rc = oper['Опер_РЦ_код']
                    if rc[:2] == '01':
                        set_rc.add(rc[:4])
                    tmp_mar.append([
                        oper['Опер_РЦ_код'],{
                            'id': f"{dse['Номерпп']}_{oper['Опер_номер']}",
                            'Количество': dse['Количество'],
                            'Освоено,шт.': oper['Освоено,шт.'],
                            'Закрыто,шт.': oper['Закрыто,шт.']
                        }
                    ])
                marh_str = '->'.join([ _[0] for _ in tmp_mar if _[0][:2] == '01'])
                if marh_str in dict_dse_marh:
                    dict_dse_marh[marh_str].append(dse['Номерпп'])
                else:
                    dict_dse_marh[marh_str] = [dse['Номерпп']]
                set_mar_neformat.add(marh_str)
                list_mar.append([dse_name])
            #    limit = 1
            #    for item in tmp_mar:
            #        rc = item[0]
            #        dict_param = item[1]
            #        dict_param_str = '/'.join([str(_) for _ in dict_param.values()])
            #        fl= False
            #        for i in range(limit,len(list_mar[0])):
            #            if list_mar[0][i] == rc:
            #                fl = True
            #                list_mar[-1].append(dict_param_str)
            #                break
            #            else:
            #                list_mar[-1].append('')
            #            limit = i + 1
            #        if fl == False:
            #            list_mar[0].append(rc)
            #            list_mar[-1].append(dict_param_str)
            #            limit = len(list_mar[0])
            #
            #CQT.fill_wtabl(list_mar,tbl_m,height_row=20,ogr_maxshir_kol=20)
            #tbl_m.setColumnWidth(0,200)
            return set_mar_neformat,  set_rc, dict_dse_marh

        self.set_mar_neformat, set_rc , self.dict_dse_marh = fill_table_marsh(self,res)

        self.ui.cmb_current_rc.clear()
        self.ui.cmb_current_rc.addItem('')
        self.ui.cmb_current_rc.addItems(sorted(list(set_rc)))
        return

    @CQT.onerror
    def select_current_rc(self,*args):
        self.ui.cmb_list_marsh.clear()
        self.ui.cmb_list_marsh.addItem('')
        current_rc = self.ui.cmb_current_rc.currentText()
        if current_rc == '':
            return
        self.ui.cmb_list_marsh.addItems([ _ for _ in self.set_mar_neformat if current_rc in [x[:len(current_rc)] for x in _.split('->')]])

    @CQT.onerror
    def fill_tbl_select_marsh(self,*args):
        if self.ui.cmb_vid_inf_marsh.count() == 0:
            self.ui.cmb_vid_inf_marsh.clear()
            self.ui.cmb_vid_inf_marsh.addItems(['Операция', 'Номер операции', 'Количество','РЦ','Имя РЦ'])
        def create_dict_of_marsh(self):
            spis_dse = CQT.spisok_iz_wtabl(self.ui.tbl_dse,shapka=True,rez_dict=True,only_visible=False)
            dict_dse = dict()

            for i, item in enumerate(spis_dse):
                if self.ui.tbl_dse.isRowHidden(i):
                    continue
                name = item['Обозначение'].strip() + " " + item['Наименование'].strip()
                id = item['ID']
                mat = item['Масса/М1,М2,М3']
                oper = item['Операция']
                nom_oper= item['Ном_оп']
                kol_vo = '/'.join([item['Количество,шт.'],item['Освоено,шт.'],item['Закрыто,шт.']])
                rc = item['РЦ']
                rc_name = item['РЦ_имя']
                if id not in dict_dse:
                    dict_dse[id] = {'name':name, 'id':id, 'mat': mat, 'mar':[]}
                dict_for_rc = {'Операция':oper,'Номер операции':nom_oper,'Количество':kol_vo,'РЦ':rc,'Имя РЦ':rc_name,'nom_strok':i}
                dict_dse[id]['mar'].append(dict_for_rc)
            return dict_dse

        @CQT.onerror
        def oforml_tbl_marsh(self,list_of_lists,*args):
            tbl_marsh = self.ui.tbl_select_marsh
            CQT.fill_wtabl(list_of_lists, tbl_marsh, auto_type=False, height_row=20, set_editeble_col_nomera={})
            CMS.zapolnit_filtr(self,self.ui.tbl_select_marsh_filtr,self.ui.tbl_select_marsh,'',True)
            CMS.update_width_filtr(self.ui.tbl_select_marsh,self.ui.tbl_select_marsh_filtr)
            #list_marsh = CQT.spisok_iz_wtabl(tbl_marsh, shapka=True)
            #if list_marsh == [[]]:
            #    return
            for j in range(3, tbl_marsh.columnCount()):
                rc = tbl_marsh.horizontalHeaderItem(j).text()
                if rc in self.DICT_RC_FULL:
                    r, g, b = self.DICT_RC_FULL[rc]['Цвет'].split(',')
                    r = int(r)
                    g = int(g)
                    b = int(b)
                    for i in range(tbl_marsh.rowCount()):
                        CQT.ust_color_wtab(tbl_marsh, i, j, r, g, b)
                        CQT.ust_color_wtab(tbl_marsh, i, j, r, g, b)
                fl_column_hide = True
                for i in range(tbl_marsh.rowCount()):
                    if tbl_marsh.item(i,j).text() != '':
                        kolvo = self.get_dict_from_tbl_marsh(i+1,j,list_of_lists,'Количество')
                        kol, osv, zak = kolvo.split('/')
                        if F.valm(osv) != F.valm(kol):
                            fl_column_hide = False
                        if F.valm(zak) == F.valm(kol):
                            CQT.ust_font_color_wtab(self.ui.tbl_select_marsh,i,j,84,130,53)
                            continue
                        if F.valm(osv) == F.valm(kol):
                            CQT.ust_font_color_wtab(self.ui.tbl_select_marsh,i,j,198,89,17)
                            continue
                        if F.valm(osv) == 0:
                            CQT.ust_font_color_wtab(self.ui.tbl_select_marsh, i, j, 128, 0, 0)
                            continue
                if fl_column_hide:
                    pass
                    #self.ui.tbl_select_marsh.setColumnHidden(j,True)
                    #CQT.ust_color_wtab(self.ui.tbl_select_marsh,0,j,169,208,142)

            self.bold_in_marsh_selected_dse()


        self.dict_dse_for_marsh = create_dict_of_marsh(self)
        
        list_rc = []
        rez = [['ДСЕ','Материал','id']]
        for dse in  self.dict_dse_for_marsh.keys():
            list_rc.append([])
            rez.append([ self.dict_dse_for_marsh[dse]['name'], self.dict_dse_for_marsh[dse]['mat'], self.dict_dse_for_marsh[dse]['id']])
            for item in  self.dict_dse_for_marsh[dse]['mar']:
                rc = item['РЦ']
                list_rc[-1].append(rc)
        if list_rc == []:
            CQT.msgbox(f'Ошибка генерации списка РЦ')
            return
        list_rc_new = CMS.raspredelenie_marshrutov(copy.deepcopy(list_rc))

        for i in range(len(list_rc_new)):
            for j in range(len(list_rc_new[0])):
                rez[i].append(list_rc_new[i][j])

        body = rez[1:]
        body = sorted(body, key=lambda x: x[1])
        for j in range(len(rez[0])-1,2,-1):
            body = sorted(body, key=lambda x: x[j])
        rez = [rez[0]]
        for item in body:
            rez.append(item)

        for i in range(1,len(rez)):
            for j in range(3,len(rez[i])):
                if rez[i][j] != '':
                    rez[i][j] = self.get_dict_from_tbl_marsh(i,j,rez,self.ui.cmb_vid_inf_marsh.currentText())

        oforml_tbl_marsh(self,rez)

    @CQT.onerror
    def get_dict_from_tbl_marsh(self,r,c,list='',key='',*args):
        if list == '':
            list = CQT.spisok_iz_wtabl(self.ui.tbl_select_marsh,shapka=True)
        nk_id = F.nom_kol_po_im_v_shap(list,'id')
        id = list[r][nk_id]
        num_ceil = 0
        for j in range(3,c+1):
            if list[r][j] != '':
                num_ceil += 1
        if num_ceil == 0:
            return None
        if key == '':
            return self.dict_dse_for_marsh[id]['mar'][num_ceil-1]
        return self.dict_dse_for_marsh[id]['mar'][num_ceil-1][key]

    @CQT.onerror
    def select_dse_po_marsh(self,*args):
        if self.ui.cmb_list_marsh.currentText() == '':
            text = ''
        else:
            text = '|'.join([str(_) for _ in self.dict_dse_marh[self.ui.cmb_list_marsh.currentText()]])
        tblf = self.ui.tbl_filtr_dse
        nk_imaop = CQT.nom_kol_po_imen(tblf, 'ID')
        tblf.item(0, nk_imaop).setText(text)
        CMS.primenit_filtr(self, tblf, self.ui.tbl_dse)
        self.fill_tbl_select_marsh()

    @CQT.onerror
    def select_prof(self, i, *args):
        spis_prof = self.ui.cmb_prof.itemText(i).split('|')
        rez_op = []
        for key in self.DICT_ETAPI.keys():
            fl_add = True
            for prof in spis_prof:
                if prof not in self.DICT_ETAPI[key]:
                    fl_add = False
                    break
            if fl_add:
                rez_op.append(key)
        rez = '|'.join(rez_op)
        tblf = self.ui.tbl_filtr_dse
        nk_imaop = CQT.nom_kol_po_imen(tblf, 'Операция')
        tblf.item(0, nk_imaop).setText(rez)
        CMS.primenit_filtr(self, tblf, self.ui.tbl_dse)

    @CQT.onerror
    def rasch_strukt_dostup(self, res, i, j):
        kol = res[i]['Количество']
        uroven = res[i]['Уровень']
        for i_dse in range(i + 1, len(res)):
            if res[i_dse]['Уровень'] <= uroven:
                break
            if res[i_dse]['Уровень'] == uroven + 1:
                if 'Закрыто,шт.' not in res[i_dse]['Операции'][-1]:
                    dost_vhod_kol = 0
                else:
                    dost_vhod_kol = res[i_dse]['Операции'][-1]['Закрыто,шт.']
                if dost_vhod_kol < kol:
                    kol = dost_vhod_kol
        if kol == 0:
            return False
        return True

    @CQT.onerror
    def rasch_zakritiy_dostup(self, res, i, j):
        if res[i]['Операции'][0]['Освоено,шт.'] == res[i]['Количество']:
            return False
        if j == 0:
            pass
        else:
            if res[i]['Операции'][j - 1]['Закрыто,шт.'] > 0:
                return True
            else:
                return False
        return True

    @CQT.onerror
    def check_box_load_full(self, *args):
        self.load_mk()

    @CQT.onerror
    def load_mk(self, lite=False, nom_mk='', conn='', res=''):
        if nom_mk == '':
            nom_mk = self.glob_nom_mk
        if nom_mk == 0:
            return
        if res == '':

            res = CMS.load_res(nom_mk)

        filtr = self.ui.checkBox_full_dse.isChecked()
        # print(filtr)
        tabl_mk = self.ui.tbl_dse

        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        set_rc = set()
        if res == False:
            self.ui.tabWidget_2.setCurrentIndex(CQT.nom_tab_po_imen(self.ui.tabWidget_2, 'МК'))
            CSQ.close_bd(conn)
            CQT.msgbox('Не найдена структура, необходимо переоткрыть МК')
            return
        spis_shap_mk = [
            ['Чек', "Наименование", "Обозначение", "В работу,шт.", 'Уровень', "Количество,шт.", "Освоено,шт.",
             'Закрыто,шт.',
             'Ном_оп', "Опер_код","Операция",
             "Масса/М1,М2,М3", "Ссылка", "ID",
             "Примечание", "ПКИ", "Тпз", "Тшт", 'РЦ','РЦ_имя', 'Оборудование', "Профессия", "Вид_работ",
             "КР", "КОИД", "Документы", 'Переходы']]
        spis_shab_mk = []

        set_oper = set()
        set_mat = set()
        for i, dse in enumerate(res):
            naim = CMS.uroven_oform(dse['Наименование'], dse['Уровень'])
            nn = CMS.uroven_oform(dse['Номенклатурный_номер'], dse['Уровень'])
            kolich = dse['Количество']
            mat = dse['Мат_кд']
            ssil = dse['Ссылка']
            id = dse['Номерпп']
            prim = dse['Прим']
            pki = dse['ПКИ']
            ur = dse['Уровень']
            if mat.split('/')[1] != '':
                set_mat.add('/'.join(mat.split('/')[1:]))
            for j, oper in enumerate(dse['Операции']):
                if 'Освоено,шт.' not in oper:
                    res[i]['Операции'][j]['Освоено,шт.'] = 0
                if 'Закрыто,шт.' not in oper:
                    res[i]['Операции'][j]['Закрыто,шт.'] = 0
                if filtr or lite:
                    flag_oran_oper = False
                    if self.SPIS_DOST_OPER != []:
                        if oper['Опер_наименовние'] in self.SPIS_DOST_OPER:
                            flag_oran_oper = True
                    else:
                        flag_oran_oper = True
                    flag_zakritiy_dostup = False
                    flag_strukturn_dostup = False
                    if flag_oran_oper:
                        flag_zakritiy_dostup = self.rasch_zakritiy_dostup(res, i, j)
                    if flag_zakritiy_dostup:
                        flag_strukturn_dostup = self.rasch_strukt_dostup(res, i, j)
                else:
                    flag_strukturn_dostup = True
                # print(flag_strukturn_dostup)
                if flag_strukturn_dostup:
                    zakrito = oper['Закрыто,шт.']
                    osvoeno = oper['Освоено,шт.']
                    oper_naim = oper['Опер_наименовние']
                    oper_nom = oper['Опер_номер']
                    oper_rc_kod = oper['Опер_РЦ_код']
                    rc_name = ''
                    if oper_rc_kod in self.DICT_RC:
                        rc_name = self.DICT_RC[oper_rc_kod]
                    set_rc.add(f'{oper_rc_kod}({rc_name})')
                    oper_oborud = oper['Опер_оборудование_наименовние']
                    oper_tpz = oper['Опер_Тпз']
                    oper_tst = round(F.valm(oper['Опер_Тшт']) / kolich, 6)

                    if oper['Опер_профессия_код'] in self.DICT_PROFESSIONS:
                        oper_prof = self.DICT_PROFESSIONS[oper['Опер_профессия_код']]['имя']
                    else:
                        oper_prof = oper['Опер_профессия_код']
                    set_oper.add(oper['Опер_наименовние'])
                    oper_vidrab = oper['Опер_профессия_код']
                    if oper_vidrab in self.DICT_PROFESSIONS:
                        oper_vidrab = self.DICT_PROFESSIONS[oper_vidrab]['вид работ']
                    oper_kr = oper['Опер_КР']
                    oper_koid = oper['Опер_КОИД']
                    docs = '; '.join(dse['Документы']) + "; " + '; '.join(oper['Опер_документы'])
                    perehod = '; '.join(oper['Переходы'])
                    v_raboty = kolich - osvoeno
                    oper_rc_name = ''
                    oper_kod = oper['Опер_код']
                    if oper_rc_kod in self.DICT_RC:
                        oper_rc_name = self.DICT_RC[oper_rc_kod]
                    spis_shab_mk.append(
                        ['', naim, nn, v_raboty, ur, kolich, osvoeno, zakrito, oper_nom, oper_kod, oper_naim, mat, ssil, id,
                         prim, pki, oper_tpz, oper_tst, oper_rc_kod, oper_rc_name, oper_oborud,
                         oper_prof, oper_vidrab, oper_kr, oper_koid, docs, perehod])
        if lite:
            if len(spis_shab_mk) == 0:
                return False
            else:
                return True
        spis_shab_mk = sorted(spis_shab_mk, key=lambda ppor: ppor[F.nom_kol_po_im_v_shap(spis_shap_mk, 'ID')],
                              reverse=True)
        spis_shab_mk.insert(0, spis_shap_mk[0])
        set_red = {F.nom_kol_po_im_v_shap(spis_shab_mk, "В работу,шт.")}
        CQT.zapoln_wtabl(self, spis_shab_mk, tabl_mk, 0, set_red, '', '', 600, True, '', 20)
        tabl_mk.setColumnWidth(CQT.nom_kol_po_imen(tabl_mk, 'Наименование'), 350)
        tabl_mk.setColumnWidth(CQT.nom_kol_po_imen(tabl_mk, 'Обозначение'), 350)
        tabl_mk.setColumnWidth(CQT.nom_kol_po_imen(tabl_mk, 'Масса/М1,М2,М3'), 200)
        tabl_mk.setColumnWidth(CQT.nom_kol_po_imen(tabl_mk, 'Ссылка'), 70)
        tabl_mk.setColumnHidden(CQT.nom_kol_po_imen(tabl_mk, 'ID'), True)
        nk_check = CQT.nom_kol_po_imen(tabl_mk, 'Чек')
        nk_oper_kod = CQT.nom_kol_po_imen(tabl_mk, "Опер_код")
        nk_oper_name = CQT.nom_kol_po_imen(tabl_mk, "Операция")
        nk_osv = CQT.nom_kol_po_imen(tabl_mk, "Освоено,шт.")
        nk_kolvo = CQT.nom_kol_po_imen(tabl_mk, "Количество,шт.")
        nk_zakr = CQT.nom_kol_po_imen(tabl_mk, 'Закрыто,шт.')
        nk_kod_rc = CQT.nom_kol_po_imen(tabl_mk, 'РЦ')
        nk_rc_name = CQT.nom_kol_po_imen(tabl_mk, 'РЦ_имя')
        for i in range(tabl_mk.rowCount()):
            CQT.add_check_box(tabl_mk, i, nk_check, conn_func_checked_row_col=self.clck_check_box_dse)
            if tabl_mk.item(i,nk_oper_kod).text() in self.DICT_OPER:
                if self.DICT_OPER[tabl_mk.item(i,nk_oper_kod).text()]['Вспомогат'] == 1:
                    CQT.ust_font_color_wtab(tabl_mk,i,nk_oper_kod,120,120,120)
                    CQT.ust_font_color_wtab(tabl_mk, i, nk_oper_name, 120, 120, 120)
            if tabl_mk.item(i, nk_osv).text() == tabl_mk.item(i, nk_kolvo).text():
                CQT.font_cell_size_format(tabl_mk, i, nk_osv,bold=True)
            if tabl_mk.item(i, nk_zakr).text() == tabl_mk.item(i, nk_kolvo).text():
                CQT.font_cell_size_format(tabl_mk, i, nk_zakr, bold=True)
                CQT.font_cell_size_format(tabl_mk, i, nk_kolvo, bold=True)


        CMS.zapolnit_filtr(self, self.ui.tbl_filtr_dse, tabl_mk,hidden_scroll=True)
        CMS.load_column_widths(self, self.ui.tbl_dse)
        self.info_label()
        self.oform_dse()
        for i in range(tabl_mk.rowCount()):
            if tabl_mk.item(i, nk_kod_rc).text() in self.DICT_RC_FULL:
                r,g,b = self.DICT_RC_FULL[tabl_mk.item(i, nk_kod_rc).text()]['Цвет'].split(',')
                r = int(r)
                g = int(g)
                b = int(b)
               #min_val =min([r,g,b])
                #r= r - min_val
                #g= g - min_val
                #b = b - min_val
                CQT.ust_color_wtab(tabl_mk, i, nk_kod_rc, r, g, b)
                CQT.ust_color_wtab(tabl_mk, i, nk_rc_name, r, g, b)
        #tabl_mk.setItemDelegate(CQT.Delegate(tabl_mk))

        self.ui.cmb_mat.clear()
        self.ui.cmb_mat.addItem('')
        list_mat = sorted(list(set_mat))
        self.ui.cmb_mat.addItems(list_mat)

        spis_oper = sorted(list(set_oper))
        self.ui.cmb_etapi.clear()
        self.ui.cmb_etapi.addItem('')
        for oper in spis_oper:
            self.ui.cmb_etapi.addItem(oper)


        self.ui.cmb_prof.clear()
        self.ui.cmb_prof.addItem('')
        set_prof = set()
        for prof in self.DICT_ETAPI.keys():
            set_prof.add('|'.join(self.DICT_ETAPI[prof]))
        for prof in set_prof:
            self.ui.cmb_prof.addItem(prof)
        self.glob_res = res

        #======списки для фильра маршрутов=======
        self.load_podbor_marsh(res)
        self.fill_tbl_select_marsh()



    @CQT.onerror
    def uchet_osvoenih_v_res(self):
        if self.glob_res == False:
            CQT.msgbox(f'Не корректно выгружена ресурсная')
            return
        for i in range(len(self.spis_dse)):
            for j in range(len(self.glob_res)):
                if self.glob_res[j]['Номерпп'] == int(self.spis_id[i]):
                    for k in range(len(self.glob_res[j]['Операции'])):
                        if self.glob_res[j]['Операции'][k]['Опер_номер'] == self.spis_oper[i].split('$')[0]:
                            if 'Освоено,шт.' in self.glob_res[j]['Операции'][k]:
                                self.glob_res[j]['Операции'][k]['Освоено,шт.'] += int(self.spis_kolvo[i])
                            else:
                                self.glob_res[j]['Операции'][k]['Освоено,шт.'] = int(self.spis_kolvo[i])
                            break
                    break
        # CSQ.update_bd_sql(self.db_naryd, 'mk', {'Статус': 'Открыта'},
        #                  {'Пномер': int(self.glob_nom_mk)},conn= conn,cur = cur)
        # zapros = f'''UPDATE mk SET 'Статус' = 'Открыта' WHERE Пномер == {int(self.glob_nom_mk)}'''
        # rez = CSQ.zapros(self.db_naryd, zapros,conn= conn,cur = cur)

        # CSQ.update_bd_sql(self.db_resxml, 'res', {'data': F.to_binary_pickle(self.glob_res)},
        #                  {'Номер_мк': int(self.glob_nom_mk)},conn= conn_res,cur = cur_res)
        rez = CSQ.zapros(self.db_resxml,
                   f"""UPDATE res SET data = ?
                   WHERE Номер_мк == {int(self.glob_nom_mk)}""",
                   spisok_spiskov=[F.to_binary_pickle(self.glob_res)])
        if rez == False:
            CQT.msgbox(f'Ошибка учета количества')
        return

    def clck_check_box_dse(self, check='', i='', j='', *args):
        tbl = self.ui.tbl_dse
        if check:
            tbl.item(i,j).setText('1')
        else:
            tbl.item(i, j).setText('')
        self.raschet_naruada_time_tmp(check, i, j, *args)
        self.bold_in_marsh_selected_dse()

    @CQT.onerror
    def raschet_naruada_time_tmp(self, check='', i='', j='', *args):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        nk_tpz = CQT.nom_kol_po_imen(tbl, 'Тпз')
        nk_tst = CQT.nom_kol_po_imen(tbl, 'Тшт')
        nk_v_rab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')
        nk_v_osv = CQT.nom_kol_po_imen(tbl, 'Освоено,шт.')
        nk_v_kol = CQT.nom_kol_po_imen(tbl, 'Количество,шт.')
        nk_koid = CQT.nom_kol_po_imen(tbl, 'КОИД')
        nk_oper = CQT.nom_kol_po_imen(tbl, 'Операция')
        if nk_check == None:
            return
        time = 0
        time_potenc = 0
        self.glob_etap = []

        for i in range(tbl.rowCount()):
            if tbl.cellWidget(i, nk_check).isChecked():
                time_tmp = (F.valm(tbl.item(i, nk_tpz).text()) + F.valm(tbl.item(i, nk_tst).text()) *
                                 F.valm(tbl.item(i, nk_v_rab).text()) / F.valm(tbl.item(i, nk_koid).text()))
                time_potenc += time_tmp

                if self.DICT_ETAPI != dict():
                    if self.glob_etap == []:
                        if tbl.item(i, nk_oper).text() in self.DICT_ETAPI:
                            self.glob_etap = self.DICT_ETAPI[tbl.item(i, nk_oper).text()]
                        else:
                            CQT.msgbox(f'{tbl.item(i, nk_oper).text()} не в списке этапов')
                    else:
                        if tbl.item(i, nk_oper).text() in self.DICT_ETAPI:
                            spis_prof_tek = self.DICT_ETAPI[tbl.item(i, nk_oper).text()]
                        else:
                            CQT.msgbox(f'{tbl.item(i, nk_oper).text()} не в списке этапов')
                            spis_prof_tek = []
                        spis_prof_new = []
                        for prof in spis_prof_tek:
                            if prof in self.glob_etap:
                                spis_prof_new.append(prof)
                        self.glob_etap = spis_prof_new
                        if self.glob_etap == []:
                            CQT.msgbox('Не верное сочетание профессий для наряда')
                            tbl.cellWidget(i, nk_check).setChecked(False)
                            tbl.item(i, nk_check).setText('')
                            return

                if F.valm(tbl.item(i, nk_v_rab).text()) > F.valm(tbl.item(i, nk_v_kol).text()) - \
                        F.valm(tbl.item(i, nk_v_osv).text()):
                    CQT.msgbox('Количество не корректное')
                    tbl.cellWidget(i, nk_check).setChecked(False)
                    tbl.item(i, nk_check).setText('')
                    return False
                else:
                    time += time_tmp

        self.ui.lbl_tmp_time_potenc.setText(f'{str(round(time_potenc,2))} мин.')
        self.ui.lbl_tmp_time.setText(f'{str(round(time,2))} мин.')


    @CQT.onerror
    def raschet_naruada(self, prinuditelno=False):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        zadanie = ''
        nk_dse_naim = CQT.nom_kol_po_imen(tbl, 'Наименование')
        nk_dse_nn = CQT.nom_kol_po_imen(tbl, 'Обозначение')
        nk_dse_kol = CQT.nom_kol_po_imen(tbl, 'Количество,шт.')
        nk_oper_nom = CQT.nom_kol_po_imen(tbl, 'Ном_оп')
        nk_oper = CQT.nom_kol_po_imen(tbl, 'Операция')
        nk_tpz = CQT.nom_kol_po_imen(tbl, 'Тпз')
        nk_tst = CQT.nom_kol_po_imen(tbl, 'Тшт')
        nk_docs = CQT.nom_kol_po_imen(tbl, 'Документы')
        nk_per = CQT.nom_kol_po_imen(tbl, 'Переходы')
        nk_v_rab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')
        nk_kr = CQT.nom_kol_po_imen(tbl, 'КР')
        nk_koid = CQT.nom_kol_po_imen(tbl, 'КОИД')
        nk_id = CQT.nom_kol_po_imen(tbl, 'ID')
        nk_vid_rab = CQT.nom_kol_po_imen(tbl, 'Вид_работ')
        time = 0
        if nk_check == None:
            return
        self.spis_dse = []
        self.spis_id = []
        self.spis_oper = []
        self.spis_vr = []
        self.spis_kolvo = []
        self.spis_vidrab = []
        for i in range(tbl.rowCount()):
            if tbl.cellWidget(i, nk_check).isChecked():
                if F.valm(tbl.item(i, nk_v_rab).text()) != '' and F.valm(
                        tbl.item(i, nk_v_rab).text()) != 0 or prinuditelno:
                    naim = tbl.item(i, nk_dse_naim).text().strip()
                    nn = tbl.item(i, nk_dse_nn).text().strip()
                    time_tmp = (F.valm(tbl.item(i, nk_tpz).text()) + F.valm(tbl.item(i, nk_tst).text()) *
                                     F.valm(tbl.item(i, nk_v_rab).text()) / F.valm(tbl.item(i, nk_koid).text()))
                    time += time_tmp

                    head = f'{naim} {nn} ' \
                           f'({tbl.item(i, nk_v_rab).text()} шт.) - {round(time_tmp,2)} мин.'
                    body = f'    {tbl.item(i, nk_docs).text()}' + '\n' + \
                           f'    {tbl.item(i, nk_oper_nom).text()} {tbl.item(i, nk_oper).text()}' + '\n' + \
                           f'        {tbl.item(i, nk_per).text()}'
                    zadanie += head + body + '\n' + '\n'

                    self.spis_dse.append(naim + '$' + nn)
                    self.spis_id.append(tbl.item(i, nk_id).text())
                    self.spis_oper.append(tbl.item(i, nk_oper_nom).text() + '$' + tbl.item(i, nk_oper).text())
                    self.spis_vr.append(str(round(time_tmp,2)))
                    self.spis_kolvo.append(str(tbl.item(i, nk_v_rab).text()))
                    # vidrab = tbl.item(i,nk_professia).text()
                    # if vidrab in self.DICT_PROFESSIONS:
                    #    vidrab = self.DICT_PROFESSIONS[vidrab]
                    self.spis_vidrab.append(tbl.item(i, nk_vid_rab).text())

        self.ui.lineEdit_cr_nar_norma.setText(str(round(time,2)))
        self.ui.plainTextEdit_zadanie.setPlainText(zadanie)
        tbl_mk = self.ui.tableWidget_vibor_mk
        nk_pnom = CQT.nom_kol_po_imen(tbl_mk, 'Пномер')
        nk_pnom_pr = CQT.nom_kol_po_imen(tbl_mk, 'Номер_проекта')
        nk_pnom_zak = CQT.nom_kol_po_imen(tbl_mk, 'Номер_заказа')
        for i in range(tbl_mk.rowCount()):
            if tbl_mk.item(i, nk_pnom).text() == str(self.glob_nom_mk):
                np = tbl_mk.item(i, nk_pnom_pr).text()
                py = tbl_mk.item(i, nk_pnom_zak).text()
                self.ui.lineEdit_cr_nar_nom_proect.setText(np)
                self.ui.lineEdit_cr_nar_nomerPU.setText(py)
                break
        self.ui.lineEdit_cr_nar_nom_proect.setEnabled(False)
        self.ui.lineEdit_cr_nar_nomerPU.setEnabled(False)

        self.ui.plainTextEdit_zadanie.setReadOnly(True)
        self.ui.lineEdit_cr_nar_kolvo.setEnabled(False)
        self.ui.lineEdit_cr_nar_norma.setEnabled(False)
        self.ui.checkBox_vneplan_rab.setChecked(False)

    @CQT.onerror
    def oform_dse(self):
        tbl = self.ui.tbl_dse
        nk_ur = CQT.nom_kol_po_imen(tbl, 'Уровень')
        nk_v_rab = CQT.nom_kol_po_imen(tbl, 'В работу,шт.')
        max_ur = 0
        for i in range(tbl.rowCount()):
            ur = int(tbl.item(i, nk_ur).text())
            if ur > max_ur:
                max_ur = ur
        if max_ur == 0:
            shag = 55
        else:
            shag = 155 // max_ur
        for i in range(tbl.rowCount()):
            ur = int(tbl.item(i, nk_ur).text())
            ed = 255 - (max_ur - ur) * shag
            CQT.ust_color_row_wtab(tbl, i, 0 + ed, 225, 0 + ed)
            CQT.dob_color_wtab(tbl, i, nk_v_rab, 0, 15, 15)

    @CQT.onerror
    def info_label(self):
        lbl = self.ui.lbl_curr_mk
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        flag = None
        for i in range(tabl_sp_mk.rowCount()):
            if tabl_sp_mk.item(i, 0) == None:
                break
            if tabl_sp_mk.item(i, 0).text() == str(self.glob_nom_mk):
                tabl_sp_mk.setCurrentCell(i, 0)
                flag = i
                break
        if flag == None:
            lbl.setText('')
        else:
            lbl.setText(
                f'МК {tabl_sp_mk.item(flag, 0).text()} - {tabl_sp_mk.item(flag, 3).text()} '
                f'({tabl_sp_mk.item(flag, 6).text()})')

    @CQT.onerror
    def tbl_red_zhur_click(self, *args):
        text = ''
        tbl = self.ui.tbl_red_zhur
        if tbl.currentRow() == -1:
            pass
        else:
            r = tbl.currentRow()
            nk_zad = CQT.nom_kol_po_imen(tbl, 'Задание')
            nk_prim = CQT.nom_kol_po_imen(tbl, 'Примечание')
            nk_kolvo = CQT.nom_kol_po_imen(tbl, 'Опер_колво')
            zad = tbl.item(r, nk_zad).text()
            prim = tbl.item(r, nk_prim).text()
            kolvo = tbl.item(r, nk_kolvo).text()
            text = f'    Количество: {kolvo} \n    Задание: {zad} \n    Примечание: {prim}'
        self.ui.lbl_red_info.setText(text)

    @CQT.onerror
    def tbl_dse_dblclick(self, *args):
        tbl = self.ui.tbl_dse
        r = tbl.currentRow()
        if r == -1:
            return
        if tbl.currentColumn() == CQT.nom_kol_po_imen(tbl, 'Ссылка'):
            os.startfile(f"{tbl.item(r, tbl.currentColumn()).text()}")

    @CQT.onerror
    def tbl_dse_click(self, *args):
        tbl = self.ui.tbl_dse
        nk_check = CQT.nom_kol_po_imen(tbl, 'Чек')
        if tbl.currentColumn() == nk_check:
            self.select_dse(0)
        CMS.on_section_resized(self)
        CMS.update_width_filtr(self.ui.tbl_dse,self.ui.tbl_filtr_dse)


    @CQT.onerror
    def tbl_dse_select(self, *args):
        tbl = self.ui.tbl_dse
        lbl = self.ui.lbl_ima_rc
        lbl_info = self.ui.lbl_info_dse
        nk_rc = CQT.nom_kol_po_imen(tbl, 'РЦ')
        nk_nn = CQT.nom_kol_po_imen(tbl, 'Обозначение')
        nk_naim = CQT.nom_kol_po_imen(tbl, 'Наименование')
        nk_nom_op = CQT.nom_kol_po_imen(tbl, 'Ном_оп')
        if tbl.currentRow() == -1 or nk_nn == None:
            return
        if tbl.item(tbl.currentRow(), nk_nn) == None:
            return
        nn = tbl.item(tbl.currentRow(), nk_nn).text().strip()
        naim = tbl.item(tbl.currentRow(), nk_naim).text().strip()
        nom_oper = tbl.item(tbl.currentRow(), nk_nom_op).text()
        lbl.setText(
            f'РЦ {tbl.item(tbl.currentRow(), nk_rc).text()} - {self.DICT_RC[tbl.item(tbl.currentRow(), nk_rc).text()]}')
        marsh = []
        if self.glob_res == False:
            CQT.msgbox(f'Не загружена ресурсная попробуй позже')
            return
        for dse in self.glob_res:
            if dse['Номенклатурный_номер'] == nn and dse['Наименование'] == naim:
                for oper in dse['Операции']:
                    ima_rc ='Не известен'
                    if oper["Опер_РЦ_код"] in self.DICT_RC:
                        ima_rc = self.DICT_RC[oper["Опер_РЦ_код"]]
                    if nom_oper == oper["Опер_номер"]:
                        marsh.append(f' ___***{ima_rc} ({oper["Опер_РЦ_код"]})***___ ')
                    else:

                        marsh.append(f'{ima_rc} ({oper["Опер_РЦ_код"]})')
                break

        lbl_info.setText('-->'.join(marsh))

    @CQT.onerror
    def tbl_mk_click(self, *args):
        tbl = self.ui.tableWidget_vibor_mk
        self.glob_nom_mk = int(tbl.item(tbl.currentRow(), CQT.nom_kol_po_imen(tbl, 'Пномер')).text())
        self.ui.plainTextEdit_zadanie.setPlainText('')
        self.ui.lineEdit_cr_nar_norma.setText('')
        self.ui.lineEdit_cr_nar_nom_proect.clear()
        self.ui.lineEdit_cr_nar_nomerPU.clear()
        self.ui.plainTextEdit_primechanie.clear()
        self.ui.tbl_dse.clear()
        CMS.on_section_resized(self)
        CMS.update_width_filtr(tbl,self.ui.tbl_filtr_mk)

    @CQT.onerror
    def open_papka_chpy(self, *args):
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        row, column_number = CQT.nomer_vibr_cell_r_c(tabl_sp_mk)
        if column_number == CQT.nom_kol_po_imen(tabl_sp_mk, "Статус_ЧПУ"):
            text = tabl_sp_mk.item(tabl_sp_mk.currentRow(), CQT.nom_kol_po_imen(tabl_sp_mk, "Статус_ЧПУ")).text()
            if text != "":
                try:
                    put = text.split('_')
                    F.otkr_papky(put[2])
                except:
                    CQT.msgbox('Не удалось открыть папку')

    @CQT.onerror
    def zapoln_tabl_mk(self, *args):
        if self.glob_login == '':
            return
        self.get_plan_proj()
        tabl_sp_mk = self.ui.tableWidget_vibor_mk
        row = tabl_sp_mk.currentRow()

        zapros = f'''SELECT mk.Пномер, mk.Дата, mk.Статус, Тип_мк.Имя as Тип, mk.Номенклатура, mk.Номер_заказа, mk.Номер_проекта, 
        mk.Примечание, mk.Основание,
        mk.Прогресс, mk.Приоритет, mk.Направление, mk.Вес, mk.Количество, mk.Статус_ЧПУ, zagot.Прим_резка, zagot.Дата_компл_загот, "Ресурсная"
        FROM mk 
        INNER JOIN zagot ON mk.Пномер = zagot.Ном_МК 
        INNER JOIN Тип_мк ON mk.Тип = Тип_мк.Пномер 
        WHERE mk.Статус == "Открыта" ORDER BY mk.Приоритет ASC;'''
        list_mk= CSQ.zapros(self.db_naryd, zapros)
        spis = [list_mk[0]]
        for i in range(1,len(list_mk)):
            if self.check_dost_proj_moth( list_mk[i][5],self.glob_ima):
                spis.append(list_mk[i])


        nk_res = F.nom_kol_po_im_v_shap(spis, 'Ресурсная')
        spis_wt_res = CPY.deepcopy(spis)

        if spis == False:
            CQT.msgbox(f'Не удалось загрузить данные, попробуй позже')
            return
        nk_nom_mk = F.nom_kol_po_im_v_shap(spis, 'Пномер')

        if self.ui.chk_progress.isChecked():
            conn_res, cur_res = CSQ.connect_bd(self.db_resxml)
            for i in range(1, len(spis)):
                nom_mk = int(spis[i][0])
                data = CSQ.zapros(self.db_resxml, f"""SELECT data FROM res WHERE Номер_мк == {nom_mk}""", conn=conn_res, cur=cur_res)
                if len(data) == 2:
                    spis[i][nk_res] = data[-1][0]
            CSQ.close_bd(conn_res, cur_res)
            spis[0].append('Прогресс_01')
            spis[0].append('Прогресс_0101')
            spis[0].append('Прогресс_0102')
            spis[0].append('Прогресс_0103')
            spis[0].append('Прогресс_0104')
            nk_obsh = F.nom_kol_po_im_v_shap(spis, 'Прогресс_01')
            nk_zag = F.nom_kol_po_im_v_shap(spis, 'Прогресс_0101')
            nk_meh = F.nom_kol_po_im_v_shap(spis, 'Прогресс_0102')
            nk_sb = F.nom_kol_po_im_v_shap(spis, 'Прогресс_0103')
            nk_mal = F.nom_kol_po_im_v_shap(spis, 'Прогресс_0104')
            for i in range(1, len(spis)):
                spis[i].append('Прогресс_01')
                spis[i].append('Прогресс_0101')
                spis[i].append('Прогресс_0102')
                spis[i].append('Прогресс_0103')
                spis[i].append('Прогресс_0104')
                res = F.from_binary_pickle(spis[i][nk_res])
                spis[i][nk_obsh] = CMS.procent_vip(res, '01')
                spis[i][nk_zag] = CMS.procent_vip(res, '0101')
                spis[i][nk_meh] = CMS.procent_vip(res, '0102')
                spis[i][nk_sb] = CMS.procent_vip(res, '0103')
                spis[i][nk_mal] = CMS.procent_vip(res, '0104')
            spis_wt_res = spis
            red_col = {F.nom_kol_po_im_v_shap(spis, 'Прим_резка'),F.nom_kol_po_im_v_shap(spis, 'Дата_компл_загот')}
            set_isp_col = {_ for _ in range(len(spis[0])) if _ != nk_res}
            CQT.zapoln_wtabl(self, spis, tabl_sp_mk, set_isp_col, red_col, (), '', 200, True, '', )
        else:
            red_col = {F.nom_kol_po_im_v_shap(spis, 'Прим_резка'),F.nom_kol_po_im_v_shap(spis, 'Дата_компл_загот')}
            CQT.fill_wtabl(spis_wt_res,tabl_sp_mk,red_col,200,20,30,auto_type=False)

        tmp_spis = spis_wt_res
        for i in range(len(tmp_spis)):
            for j in range(len(tmp_spis[i])):
                tmp_spis[i][j] = str(tmp_spis[i][j]).replace('|', '$')
        F.save_file('mkards.txt', tmp_spis)
        if row != -1 and row != None:
            tabl_sp_mk.setCurrentCell(row, 0)
        if self.ui.chk_progress.isChecked():
            nk_obsh_t = CQT.nom_kol_po_imen(tabl_sp_mk, 'Прогресс_01')
            nk_zag_t = CQT.nom_kol_po_imen(tabl_sp_mk, 'Прогресс_0101')
            nk_meh_t = CQT.nom_kol_po_imen(tabl_sp_mk, 'Прогресс_0102')
            nk_sb_t = CQT.nom_kol_po_imen(tabl_sp_mk, 'Прогресс_0103')
            nk_mal_t = CQT.nom_kol_po_imen(tabl_sp_mk, 'Прогресс_0104')
            CQT.zapolnit_progress(self, tabl_sp_mk, nk_obsh_t)
            CQT.zapolnit_progress(self, tabl_sp_mk, nk_zag_t, isp_poc=False)
            CQT.zapolnit_progress(self, tabl_sp_mk, nk_meh_t, isp_poc=False)
            CQT.zapolnit_progress(self, tabl_sp_mk, nk_sb_t, isp_poc=False)
            CQT.zapolnit_progress(self, tabl_sp_mk, nk_mal_t, isp_poc=False)
        nl_pnom = F.nom_kol_po_im_v_shap(spis, 'Пномер')
        #for i in range(1, len(spis)):
        #    if self.load_mk(True, spis[i][nk_nom_mk], conn='', res=F.from_binary_pickle(spis[i][nk_res])):
        #        CQT.ust_color_wtab(tabl_sp_mk, i - 1, nl_pnom, 102, 153, 102)
        for key in self.DICT_TIP_MK.keys():
            r, g, b = self.DICT_TIP_MK[key]['rgb'].split(',')
            CQT.cvet_cell_wtabl(tabl_sp_mk, 'Тип', '', key, r, g, b, False)
        CMS.load_column_widths(self, tabl_sp_mk)
        CMS.update_width_filtr(tabl_sp_mk, self.ui.tbl_filtr_mk)

    def btn_dse_sh_tree(self):
        if self.ui.fr_dse_tree.isHidden():
            self.ui.fr_dse_tree.setHidden(False)
        else:
            self.ui.fr_dse_tree.setHidden(True)


    def btn_dse_sh_filtr(self):
        if self.ui.fr_dse_filtrs.isHidden():
            self.ui.fr_dse_filtrs.setHidden(False)
        else:
            self.ui.fr_dse_filtrs.setHidden(True)


    def btn_dse_sh_elems(self):
        if self.ui.fr_dse_elems.isHidden():
            self.ui.fr_dse_elems.setHidden(False)
        else:
            self.ui.fr_dse_elems.setHidden(True)

    def btn_dse_info(self):
        msg = []
        for key in self.DICT_RC.keys():
            msg.append(f'{key}:{self.DICT_RC[key]}')
        txt = pprint.pformat(msg)
        CQT.msgbox(txt)

app = QtWidgets.QApplication(sys.argv)

args = sys.argv[1:]
myappid = 'Powerz.BAG.SystCreateWork.1.0.3'  # !!!
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon(os.path.join("icons", "tab.png")))

#S = F.scfg['Stile'].split(",")
app.setStyle('Fusion')
application = mywindow()
# ======================================================
versia = application.versia
if CMS.kontrol_ver(versia, "Создание2") == False:
    sys.exit()
# =========================================================
application.show()
sys.exit(app.exec())



