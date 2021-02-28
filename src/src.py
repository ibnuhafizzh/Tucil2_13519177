# Decrease and Conquer (tugas kecil 2)
# M. Ibnu Syah Hafizh
# 13519177


def inputfile(): # Fungsi untuk input file dan mengembalikan nilai berupa array yang elemennya adalah baris dari isi file
    namafile = str(input("Masukkan nama file (tanpa .txt): "))
    file = open('./test/'+namafile+'.txt', 'r')
    Lines = file.readlines()
    wordlist = [] 
    for line in Lines:
        clear = line.rstrip('\n').rstrip('.').replace(",","").split(' ')
        wordlist.append(clear)
    return wordlist

matkul = [] #list untuk menampung hasil mata kuliah tiap semester

# Fungsi decrease dengan parameter X bertipe list adalah fungsi untuk mengeleminasi
# simpul GAD yang berderajat masuk 0 dan memasukkan simpul tersebut ke dalam list matkul
# Fungsi deacrease mengembalikan nlai berupa list baru tanpa simpul yang tereleminasi
def decrease(X):
    Xbaru = [] #list untuk menampung elemen yang bukan berderajat masuk 0
    derajat_masuk = [] #list untuk menampung derajat masuk tiap simpul
    for i in X: 
        derajat_masuk.append(len(i)-1)
    group = [] #list untuk menampung simpul yang berderajat masuk 0
    for i in range (len(derajat_masuk)):
        if (derajat_masuk[i] == 0):
            group.append(X[i][0]) #Menambahkan simpul yang berderajat masuk 0 ke dalam list group
        else:
            continue
    for i in range (len(derajat_masuk)):
        if (derajat_masuk[i] == 0):
            awal = X[i][0] #menyimpan simpul yang berderajat masuk 0
            break
        else:
            continue
    X.remove([awal]) #menghapus simpul yang berderajat masuk 0 dari list X
    matkul.append(group) #memasukkan list group ke dalam list matkul, nantinya elemen yang berada dalam satu group akan menjadi satu kesatuan (matkul pada 1 semester)
    for i in range (len(X)):
        if(awal in X[i]):
            (X[i]).remove(awal) #menghapus matkul yang dieleminasi dari prerequisite tiap mata kuuliah
            Xbaru.append(X[i])
        else:
            Xbaru.append(X[i])
    return (Xbaru) #mengembalikan list baru tanpa simpul berderajat masuk 0
    
# Prosedur conquer dengan parameter X bertipe list adalah prosedur yang digunakan untuk menyelesaikan persoalan
# topological sort dengan mereduksi sebuah persoalan menjadi 2 buah upa-persoalan dan menyelesaikan salah satu upa-persoalan tersebut
# hingga mendapat solusi untuk persoalan awal. Pada hal ini sebuah persoalan direduksi dengan konstanta konstan 1.
def conquer(X):
    if (len(X) == 1): #jika hanya terdapat satu simpul maka akan memasukkan simpul tersebut (kode mata kuliah) ke dalam list matkul
        matkul.append([X[0][0]])
    else: #jika terdapat lebih dari 1 simpul maka akan dieleminiasi satu persatu simpul yang berderajat masuk 0 sampai bersisa satu simpul
        conquer(decrease(X))

# MAIN PROGRAN
listmatkul = inputfile() #membaca input file
conquer(listmatkul) #menyelesaikan persoalan dari file masukkan

# Menghapus duplikat matkul pada tiap semester.
# Tanpa prosedur di bawah ini maka akan terjadi duplikasi kode mata kuliah di beberapa semester.
# Misalnya pada semester pertama terdapat matkul C1 dan di semester kedua terdpaat pula matkul C1
for i in range(1, len(matkul)):
    dual = []
    duplikat = matkul[i][0]
    if (duplikat in matkul[i-1]):
        (matkul[i]).remove(duplikat) #
    j = len(matkul[i])
    for k in range (i):
        for l in range (len(matkul[k])):
            dual.append(matkul[k][l])
    while j > 0:
        if (matkul[i][j-1] in dual): 
            (matkul[i]).remove(matkul[i][j-1])
        j = j- 1
while ([] in matkul):
    matkul.remove([])

# Menampilkan hasil program pada layar dengan format "Semester <angka> : <kode mata kuliah>, <kode mata kuliah>." (banyaknya 
# kode mata kuliah  tergantung elemen dalam list matkul)
for i in range(len(matkul)):
    print("Semester", i+1, ": ", end='')
    for j in range(len(matkul[i])):
        if (j == len(matkul[i])-1):
            print(matkul[i][j] + '.')
        else:
            print(matkul[i][j], end=', ')