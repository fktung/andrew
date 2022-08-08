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

def totalPesanan():
  total = 0
  print('Memu yang kamu pesan:')
  print('------------------------------------')
  for nomer,pesan in enumerate(pesanan):
    print(f"No.{nomer+1}\t {pesan[0]}\t {pesan[1]}")
    total += pesan[1]
  print('------------------------------------')
  print(f"Total Pesanan = {total}", '\n')

while True:
  menuTampil()
  prosesPesan()

  ulang = input('Apakah Mau pesan yang lain? Y/T : ')
  print('\n')
  if(ulang == 'y' or ulang == 'Y'):
    continue
  else:
    break

totalPesanan()
print(pesanan)
