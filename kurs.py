import requests

print('Selamat datang')
print ('Silakan pilih konversi yang Anda lakukan: ')
print('(1) IDR Indonesia => USD United States \n(2) USD United States => IDR Indonesia \n(3) IDR Indonesia => Bitcoin \n(4) Bitcoin => IDR Indonesia ') 
pilih = int(input('Pilihan Anda (1/2/3): '))
bank = input('Silakan ketik bank pilihan Anda: ')

url = 'https://kurs.web.id/api/v1/'+bank
data = (requests.get(url))
jual = float(data.json()['jual'])
beli = float(data.json()['beli'])
urlbit = 'https://blockchain.info/ticker'
bit = requests.get(urlbit)
buybit = float(bit.json()['USD']['buy'])
print(buybit)

if pilih == 1:
    uang = int(input('Silakan input nominal yang akan dikonversi: Rp.'))
    print ('Hasil konversi Rp '+str(uang)+' adalah USD'+str(uang / jual))
elif pilih == 2:
    uang = int(input('Silakan input nominal yang akan dikonversi: USD.'))
    print ('Hasil konversi USD '+str(uang)+' adalah Rp '+str(uang * beli))
elif pilih == 3:
    uang = int(input('Silakan input nominal yang akan dikonversi: Rp.'))
    print ('Hasil konversi Rp '+str(uang)+' adalah bitcoin '+str(uang / jual*buybit))
elif pilih == 4:
    uang = int(input('Silakan input nominal yang akan dikonversi: Bitcoin. '))
    print ('Hasil konversi Bitcoin '+str(uang)+' adalah Rp'+str(uang*buybit*beli))


print('Dengan kurs jual = '+str(jual)+ ' & kurs beli'+str(beli))

