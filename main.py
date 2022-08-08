dataMinuman = [
  ['kopi', 5000],
  ['susu', 8000],
  ['teh', 4000]
]

pesanan = []
total = 0

def menuTampil():
  print('========== Daftar Minunam ==========')
  print("Nomor \t Nama \t Harga")
  print('------------------------------------')
  for nomor,menu in enumerate(dataMinuman):
    print(f"{nomor}. \t {menu[0]} \t {menu[1]}")
  print('------------------------------------')
  
def pesananDiproses(menu, banyak):
  catatPesan = dataMinuman[int(menu)]
  catatPesan[1] = catatPesan[1] * int(banyak)
  pesanan.append(catatPesan)

def prosesPesan():
  pesan = input('Mau pesan apa nomer berapa? ')
  porsi = input('Berapa Porsi? ')
  pesananDiproses(pesan, porsi)
  return porsi

def totalPesanan(porsi):
  total = 0
  print('Memu yang kamu pesan:')
  print('------------------------------------')
  for nomer,pesan in enumerate(pesanan):
    print(f"No.{nomer+1}\t {pesan[0]}\t {porsi}\t total:{pesan[1]}")
    total += pesan[1]
  print('------------------------------------')
  print(f"Total Pesanan = {total}", '\n')
  return total

def pembayaran(sembarang):
    while True:
      bayar=input('bayar')
      bayaran=int(bayar)
      kembalian = bayaran - sembarang
      if kembalian >=0 :
        print(f'kembalian anda {kembalian}')
        break
      else:
        print(f'uang anda kurang')
        continue
  


while True:
  menuTampil()
  porsi=prosesPesan()

  ulang = input('Apakah Mau pesan yang lain? Y/T : ')
  print('\n')
  if(ulang == 'y' or ulang == 'Y'):
    continue
  else:
    break

total = totalPesanan(porsi)
pembayaran(total)
print(pesanan)
print(total)
