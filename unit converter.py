#Program to convert units of different physical quantities
import unitconvertermodule as a
print('                                WELCOME TO MY PROGRAM')
print('You can use this program to convert units of different physical quantities')
choice='yes'
while choice.lower()=='yes':
    PQ_choice=a.main_menu()
    if PQ_choice==1:
        U_choice=a.len_menu()
        if U_choice==1:
            a.km_mi()
        elif U_choice==2:
            a.mi_km()
        elif U_choice==3:
            a.m_yd()
        elif U_choice==4:
            a.m_ft()
        elif U_choice==5:
            a.m_inc()
    elif PQ_choice==2:
        U_choice=a.mass_menu()
        if U_choice==1:
            a.kg_g()
        elif U_choice==2:
            a.t_kg()
        elif U_choice==3:
            a.u_kg()
        elif U_choice==4:
            a.kg_u()
    elif PQ_choice==3:
        U_choice=a.speed_menu()
        if U_choice==1:
            a.kmh_ms()
        elif U_choice==2:
            a.mih_ms()
        elif U_choice==3:
            a.kmh_mih()
        elif U_choice==4:
            a.mih_kmh()
        elif U_choice==5:
            a.mih_fts()
    elif PQ_choice==4:
        U_choice=a.pressure_menu()
        if U_choice==1:
            a.b_kpa()
        elif U_choice==2:
            a.atm_kpa()
        elif U_choice==3:
            a.atm_bar()
    elif PQ_choice==5:
        U_choice=a.volume_menu()
        if U_choice==1:
            a.gal_l()
        elif U_choice==2:
            a.gal_oz()
        elif U_choice==3:
            a.gal_qz()
    elif PQ_choice==6:
        U_choice=a.power_menu()
        if U_choice==1:
            a.hp_w()
        elif U_choice==2:
            a.w_hp()
    elif PQ_choice==7:
        a.previous_cal()
    choice=input('do u want to continue? yes/no:')
print('Thank you for using this program:)')
print('*******************************************************************************************************')
