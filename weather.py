import re
import urllib.request
city = input("Bir şehir giriniz.(Türkçe karakter kullanmayınız.)").lower() #Türkçe karakter ile çalışmamaktadır örneğin ağrı yerine agri yazmalısınız.
url = f"https://www.havadurumu15gunluk.net/havadurumu/{city}-hava-durumu-15-gunluk.html"
site = urllib.request.urlopen(url).read().decode('utf-8')

r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
r_aciklama = f'<img src="/havadurumu/images/trans.gif" alt="{city.capitalize()} Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'

comp_gunduz = re.compile(r_gunduz)
comp_gece = re.compile(r_gece)
comp_gun = re.compile(r_gun)
comp_tarih = re.compile(r_tarih)
comp_aciklama = re.compile(r_aciklama)

gunduz = []
gece = []
gun = []
tarih = []

for i in re.findall(r_gunduz, site):
    gunduz.append(i)

for i in re.findall(r_gece, site):
    gece.append(i)

for i in re.findall(r_gun, site):
    gun.append(i)

for i in re.findall(r_tarih, site):
    tarih.append(i)


print("-" * 75)
print(f"                         {city.upper()} HAVA DURUMU")
print("-" * 75)
for i in range(0, len(gun)):
    print("{} {},\t\tgündüz: {} °C\tgece: {} °C".format(tarih[i], gun[i], gunduz[i], gece[i],))
    print("-" * 75)
    
#https://github.com/aydinnyunus kişisinden yardım aldım.
