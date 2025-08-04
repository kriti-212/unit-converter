import csv
def km_mi():
    km=float(input('Enter kilometer value:'))
    mi=km*0.6215
    ans=str(km)+'kilometer='+str(mi)+'miles'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def mi_km():
    mi=float(input('Enter miles value:'))
    km=mi*1.609
    ans=str(mi)+'miles='+str(km)+'kilometer'
    f=open('Calculation record.csv','a')
    print(ans)
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
    
def m_yd():
    m=float(input('Enter meter value:'))
    yd=m*1.0936
    ans=str(m)+'meters='+str(yd)+'yards'
    print(ans)
    f=open ('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def m_ft():
    m=float(input('Enter meter value:'))
    ft=m*3.281
    ans=str(m)+'meters='+str(ft)+'feet'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def m_inc():
    m=float(input('Enter meter value:'))
    inc=m*39.37
    ans=str(m)+'meters='+str(inc)+'inches'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
    
def kg_g():
    kg=float(input('Enter kilogram value:'))
    g=kg*1000
    ans=str(kg)+'kilograms='+str(g)+'grams'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
    
def t_kg():
    t=float(input('Enter tones value:'))
    kg=t*1000
    ans=str(t)+'tones='+str(kg)+'kilograms'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def u_kg():
    u=float(input('Enter atomic mass unit value:'))
    kg=u*1.6606
    ans=str(u)+'atomic mass unit='+str(kg)+'kilograms'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def kg_u():
    kg=float(input('Enter kilogram value:'))
    u=kg*6.022
    ans=str(kg)+'kilograms='+str(u)+'atomic mass unit'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def kmh_ms():
    kmh=float(input('Enter kilometer/hour value:'))
    ms=kmh*0.2778
    ans=str(kmh)+'kilometer/hour='+str(ms)+'meter/second'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
 
def mih_ms():
    mih=float(input('Enter miles/hour value:'))
    ms=mih*0.4470
    ans=str(mih)+'miles/hour='+str(ms)+'meter/second'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def kmh_mih():
    kmh=float(input('Enter kilometer/hour value:'))
    mih=kmh*0.6215
    ans=str(kmh)+'kilometer/hour='+str(mih)+'miles/hour'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def mih_kmh():
    mih=float(input('Enter miles/hour value:'))
    kmh=mih*1.609
    ans=str(mih)+'miles/hour='+str(kmh)+'kilometer/hour'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def mih_fts():
    mih=float(input('Enter miles/hour value:'))
    fts=mih*1.467
    ans=str(mih)+'miles/hour='+str(fts)+'feet/second'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def b_kpa():
    b=float(input('Enter bar value:'))
    kpa=b*100
    ans=str(b)+'bar='+str(kpa)+'kilopascal'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def atm_kpa():
    atm=float(input('Enter atmosphere value:'))
    kpa=atm*101.325
    ans=str(atm)+'atmosphere='+str(kpa)+'kilopascal'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def atm_bar():
    atm=float(input('Enter atmosphere value:'))
    b=atm*1.01325
    ans=str(atm)+'atmosphere='+str(b)+'bar'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def gal_l():
    gal=float(input('Enter gallon value:'))
    l=3.786*gal
    ans=str(gal)+'gallon='+str(l)+'liters'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()

def gal_oz():
    gal=float(input('Enter gallon value:'))
    oz=128*gal
    ans=str(gal)+'gallon='+str(oz)+'ounce'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
   
def gal_qz():
    gal=float(input('Enter gallon value:'))
    qz=4*gal
    ans=str(gal)+'gallon='+str(qz)+'quart'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
   
def hp_w():
    hp=float(input('Enter horsepower value:'))
    w=745.7*hp
    ans=str(hp)+'horsepower='+str(w)+'watt'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
    
def w_hp():
    w=float(input('Enter watt value:'))
    hp=1.341*(10**-3)*w
    ans=str(w)+'watt='+str(hp)+'horsepower'
    print(ans)
    f=open('Calculation record.csv','a')
    mywriter=csv.writer(f,delimiter=',')
    mywriter.writerow([ans])
    f.close()
    
def main_menu():
    print('Enter serial number to choose physical quantity')
    print(' Serial number                    physical quantity')
    print('          1                                    length')
    print('          2                                    mass')
    print('          3                                   speed')
    print('          4                                  pressure')
    print('          5                                   volume')
    print('          6                                    power')
    print('          7                      to see previous calculations')
    PQ_choice=int(input('Enter choice:'))
    return PQ_choice
def len_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1                       kilometer->miles')
    print('          2                      miles->kilometer')
    print('          3                        meter->yards')
    print('          4                        meter->feet')
    print('          5                        meter->inches')
    U_choice=int(input('Enter choice:'))
    return U_choice
def mass_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1                       kilograms->grams')
    print('          2                      tones->kilogram')
    print('          3              atomic mass unit->kilograms')
    print('          4              kilograms->atomic mass unit')
    U_choice=int(input('Enter choice:'))
    return U_choice
def speed_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1            kilometer/hour->meter/second')
    print('          2              miles/hour->meter/second')
    print('          3             kilometer/hour->miles/hour ')
    print('          4             miles/hour->kilometer/hour')
    print('          5             miles/hour->feet/second')
    U_choice=int(input('Enter choice:'))
    return U_choice
def pressure_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1                       bar->kilopascal')
    print('          2                 atmosphere->kilopascal')
    print('          3                     atmosphere->bar')
    U_choice=int(input('Enter choice:'))
    return U_choice
def volume_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1                        gallon->liters')
    print('          2                       gallon->ounce')
    print('          3                       gallon->quart ')
    U_choice=int(input('Enter choice:'))
    return U_choice
def power_menu():
    print('Enter serial number to choose unit to convert')
    print(' Serial number                    Unit')
    print('          1                     horsepower->watt')
    print('          2                       watt->horsepower')
    U_choice=int(input('Enter choice:'))
    return U_choice
def previous_cal():
    with open('Calculation record.csv','r') as f1:
        myreader=csv.reader(f1,delimiter=',')
        for r in myreader:
            if r!=[]:
                print(r)
