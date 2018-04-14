emosi       = [97,36,63,82,71,79,55,57,40,57,77,68,60,82,40,80,60,50,100,11,58,68,64,57,77,98,91,50,95,27]
provokasi   = [74,85,43,90,25,81,62,45,65,45,70,75,70,90,85,68,72,95,18,99,63,70,66,77,55,64,59,95,55,79]

def up(x, a, b):
    return (x-a)/(b-a)
def down(x, a, b):
    return (-1*(x-b)/(b-a))
def emosiUp(emosi, a, b):
    return up(emosi, a, b)
def emosiDown(emosi, a, b):
    return down(emosi,a ,b)
def provokasiUp(provokasi,a ,b):
    return up(provokasi, a ,b)
def provokasiDown(provokasi, a, b):
    return down(provokasi, a, b)
def inference(tEmosi, tProvokasi):
    if (((tEmosi == "Rendah") and (tProvokasi == "Medium")) or ((tEmosi == "Rendah") and (tProvokasi == "High")) or ((tEmosi == "Sedang") and (tProvokasi == "High")) or ((tEmosi == "Tinggi") and (tProvokasi == "Medium")) or ((tEmosi == "Tinggi") and (tProvokasi == "Normal")) or ((tEmosi == "Tinggi") and (tProvokasi == "High"))):
        tInference = "Ya"
    elif (((tEmosi == "Rendah") and (tProvokasi == "Low")) or ((tEmosi == "Rendah") and (tProvokasi == "Normal")) or ((tEmosi == "Sedang") and (tProvokasi == "Low")) or ((tEmosi == "Sedang") and (tProvokasi == "Normal")) or ((tEmosi == "Sedang") and (tProvokasi == "Medium")) or ((tEmosi == "Tinggi") and (tProvokasi == "Low"))):
        tInference = "Tidak"
    return (tInference)
def ystar(no,ya):
    return (((no*1)+(ya*2))/(no+ya))
def hasil_ystar(ystar):
    if ((ystar(no,ya)>=0) and (ystar(no,ya)<=1)):
        return "Tidak"
    elif ((ystar(no,ya)>1) and (ystar(no,ya)<=2)):
        return "Ya"

"""VARIABLE EMOSI"""

i=0
max=0
ya=0
no=0
print("BERITA   EMOSI   PROVOKASI   HOAX")
while (i<30):
    if (emosi[i]>=0) and (emosi[i]<=36):
        Mrendah = 1
        Msedang = 0
        Mtinggi = 0
        tEmosi = "Rendah"

    elif ((emosi[i]>36) and (emosi[i]<38)):
        a = 30
        b = 40
        Mrendah = emosiDown(emosi[i], a, b)
        Msedang = emosiUp(emosi[i], a, b)
        Mtinggi = 0
        if (Mrendah <= Mtinggi):
            tEmosi = "Rendah"
        else:
            tEmosi = "Sedang"

    elif ((emosi[i]>=38) and (emosi[i]<=66)):
        Msedang = 1
        Mrendah = 0
        Mtinggi = 0
        tEmosi = "Sedang"

    elif ((emosi[i]>66) and (emosi[i]<68)):
        a = 75
        b = 85
        Msedang = emosiDown(emosi[i], a, b)
        Mtinggi = emosiUp(emosi[i], a, b)
        Mrendah = 0
        if (Msedang <= Mtinggi):
            tEmosi = "Sedang"
        else:
            tEmosi = "Tinggi"

    elif ((emosi[i]>=68) and (emosi[i]<=100)):
        Mtinggi = 1
        Mrendah = 0
        Msedang = 0
        tEmosi = "Tinggi"

    """PROVOKASI"""
    if ((provokasi[i]>=0) and (provokasi[i]<=36)):
        Mlow = 1
        Mnormaol = 0
        Mmedium = 0
        Mhigh = 0
        tProvokasi = "Low"

    elif ((provokasi[i]>36) and (provokasi[i]<38)):
        a = 30
        b = 35
        Mlow = provokasiDown(provokasi[i], a, b)
        Mnormal = provokasiUp(provokasi[i], a, b)
        Mmedium = 0
        Mhigh = 0
        if (Mlow<=Mnormal):
            tProvokasi = "Low"
        else:
            tProvokasi = "Normal"

    elif ((provokasi[i]>=38) and (provokasi[i]<=66)):
        Mlow = 0
        Mnormal = 1
        Mmedium = 0
        Mhigh = 0
        tProvokasi = "Normal"

    elif ((provokasi[i]>66) and (provokasi[i]<68)):
        a = 50
        b = 55
        Mlow = 0
        Mnormal = provokasiDown(provokasi[i], a, b)
        Mmedium = provokasiUp(provokasi[i], a, b)
        Mhigh = 0
        if (Mnormal<=Mmedium):
            tProvokasi = "Normal"
        else:
            tProvokasi = "Medium"

    elif ((provokasi[i]>=68) and (provokasi[i]<=85)):
        Mlow = 0
        Mnormal = 0
        Mmedium = 1
        Mhigh = 0
        tProvokasi = "Medium"

    elif ((provokasi[i]>85) and (provokasi[i]<87)):
        a = 80
        b = 85
        Mlow = 0
        Mnormal = 0
        Mmedium = provokasiDown(provokasi[i], a, b)
        Mhigh = provokasiUp(provokasi[i], a, b)
        if (Mmedium<=Mhigh):
            tProvokasi = "Medium"
        else:
            tProvokasi = "High"

    elif ((provokasi[i]>=87) and (provokasi[i]<=100)):
        Mlow = 0
        Mnormal = 0
        Mmedium = 0
        Mhigh = 1
        tProvokasi = "High"

    if (tEmosi == "Rendah"):
        if (tProvokasi == "Low"):
            if (Mrendah<Mlow):
                tCross = Mrendah
            elif (Mrendah>=Mlow):
                tCross = Mlow
        if (tCross>no):
            no = tCross
        elif (tProvokasi == "Normal"):
            if (Mrendah<Mnormal):
                tCross = Mrendah
            elif (Mrendah>=Mnormal):
                tCross = Mnormal
        if (tCross > no):
            no = tCross
            print(no)
        elif (tProvokasi == "Medium"):
            if (Mrendah<Mmedium):
                tCross = Mrendah
            elif (Mrendah>=Mmedium):
                tCross = Mmedium
            if (tCross > ya):
                ya = tCross
        elif (tProvokasi == "High"):
            if (Mrendah<Mhigh):
                tCross = Mrendah
            elif (Mrendah>=Mhigh):
                tCross = Mhigh
            if (tCross > ya):
                ya = tCross
    elif (tEmosi == "Sedang"):
        if (tProvokasi == "Low"):
            if (Msedang<Mlow):
                tCross = Msedang
            elif (Msedang>=Mlow):
                tCross = Mlow
            if (tCross > no):
                no = tCross
        elif (tProvokasi == "Normal"):
            if (Msedang<Mnormal):
                tCross = Msedang
            elif (Msedang>=Mnormal):
                tCross = Mnormal
            if (tCross > no):
                no = tCross
        elif (tProvokasi == "Medium"):
            if (Msedang<Mmedium):
                tCross = Msedang
            elif (Msedang>=Mmedium):
                tCross = Mmedium
            if (tCross > no):
                no = tCross
        elif (tProvokasi == "High"):
            if (Msedang<Mhigh):
                tCross = Msedang
            elif (Msedang>=Mhigh):
                tCross = Mhigh
            if (tCross > ya):
                ya = tCross
    elif (tEmosi == "Tinggi"):
        if (tProvokasi == "Low"):
            if (Mtinggi<Mlow):
                tCross = Mtinggi
            elif (Mtinggi>=Mlow):
                tCross = Mlow
            if (tCross > no):
                no = tCross
        elif (tProvokasi == "Normal"):
            if (Mtinggi<Mnormal):
                tCross = Mtinggi
            elif (Mtinggi>=Mnormal):
                tCross = Mnormal
            if (tCross > ya):
                ya = tCross
        elif (tProvokasi == "Medium"):
            if (Mtinggi<Mmedium):
                tCross = Mtinggi
            elif (Mtinggi>=Mmedium):
                tCross = Mmedium
            if (tCross > ya):
                ya = tCross
        elif (tProvokasi == "High"):
            if (Mtinggi<Mhigh):
                tCross = Mtinggi
            elif (Mtinggi>=Mhigh):
                tCross = Mhigh
            if (tCross > ya):
                ya = tCross

    print("B", i + 1,"   |  ",emosi[i]," |    ",provokasi[i],"   |  ",hasil_ystar(ystar))
    i = i+1
    ya=0
    no=0