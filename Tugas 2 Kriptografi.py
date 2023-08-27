from string import ascii_lowercase as letter
import string
import random

# fungsi yang mengubah string menjadi angka
def letter_to_number(l):
    l_new = []
    for i in l:
        l_new.append((ord(i) - 97))
    return l_new

# fungsi yang mengubah angka menjadi string
def number_to_letter(a):
    letter = []
    for i in a:
        letter.append(chr(int(i) + 97))
    return "".join(letter)

# fungsi yang mengekripsi kata asal x dengan enkripsi vigenere dengan kunci k
def e_vigenere(x, k):
    n = len(k)
    key_list = letter_to_number(k)
    plain_list = letter_to_number(x)
    for i in range(len(plain_list)):
        plain_list[i] = (plain_list[i] + key_list[i % n]) % 26
    return number_to_letter(plain_list)

# fungsi yang mendekripsi kata cypher y dengan kunci k
def d_vigenere(y, k):
    n = len(k)
    key_list = letter_to_number(k)
    cypher_list = letter_to_number(y)
    for i in range(len(cypher_list)):
        cypher_list[i] = (cypher_list[i] - key_list[i % n]) % 26
    return number_to_letter(cypher_list)


# fungsi yang inputnya string a dengan output string a tanpa spasi dan huruf kecil
def clean(a):
    return a.replace(" ", "").lower()


# fungsi yang menerima input string y dengan output array yang berisi frekuensi huruf di string y
def count(y):
    fi = []
    for i in letter:
        n = 0
        for j in y:
            if i == j:
                n += 1
        fi.append([i, n])
    return fi


# fungsi yang menerima input array y dan integer m dengan output
def block(y, m):
    temp_y = []
    for j in range(m):
        temp_y.append([])
    for i in range(len(y)):
        temp_y[i % m].append(str(y[i]))
    return temp_y


# fungsi dengan input matriks y dengan output matriks y yang terurut berdasarkan kolom pertama
def Sort(y):
    return sorted(y, key=lambda tup: tup[0])


# fungsi dengan input array y, integer m dengan output float indeks koinsidensi
def indeks_koinsidensi(y, m):  # input frekuensi tiap huruf di block ciperteks dan output rata2 index koinsidensi tiap block
    out = 0
    Hasil = block(y, m)
    for j in range(m):
        n = 0
        sum = 0
        con_arr = count(Hasil[j])
        for i in range(len(con_arr)):
            sum += (int(con_arr[i][1]) * (int(con_arr[i][1]) - 1))
            n += int(con_arr[i][1])
        out += sum / (n * (n - 1))
    return out / m

# fungsi yang menerima string y dengan output tebakan panjang kunci k yang digunakan
def len_k(y):
    a = True
    m = 1
    while a:  # mecari panjang k dengan indeks koinsidensi
        ic = indeks_koinsidensi(y, m)
        if ic >= Ic * 0.85:
            a = False
        else:
            m += 1
    return m


# fungsi dengan input string y, integer g, dan array pi (peluang tiap huruf pada bahasa Indonesia)
# dengan output nilai mutual koinsidensi string y yang digeser sejauh g terhadap pi
def mutual_koinsiden(y, g, pi):
    sum = 0
    n = 0
    for i in range(26):
        sum += float(pi[i][1]) * int(y[(i + g) % 26][1]) / 100
        n += int(y[i][1])
    return sum / n


# tabel distribusi bahasa indonesia
pi = [['a', '19.61109506'], ['b', '2.849915220'], ['c', '0.647422008'], ['d', '3.425222193'], ['e', '7.953626966'],
      ['f', '0.191500105'], ['g', '4.324966160'], ['h', '2.552904525'], ['i', '7.571110749'], ['j', '0.889096109'],
      ['k', '5.231002044'], ['l', '3.420866251'], ['m', '4.682476046'], ['n', '10.06964666'], ['o', '1.558136495'],
      ['p', '2.916544996'], ['q', '0.004678604'], ['r', '4.976582779'], ['s', '4.087486670'], ['t', '5.063701614'],
      ['u', '5.589479916'], ['v', '0.056949905'], ['w', '0.432367551'], ['x', '0.014197143'], ['y', '1.844015339'],
      ['z', '0.035008865']]
Ic = 0.08267724949016449  # indeks koinsiden Bahasa Indonesia

# kata asal x
x = """Surainya yang indah menggelombang perlahan bagai tarian Kuda itu menderap melebihi ke-
        cepatan angin Lihat Ada kuda Kuda Kuda Dari atas bukit anak anak itu bisa melihat bahwa
        cahaya putih yang meluncur di padang rumput membentang itu adalah seekor kuda Itu kuda
        putih Mereka memerhatikan bagaimana kuda itu berlari dengan indah Di mata anak anak yang
        setiap hari pergi menggembalakan kambing bercakap dengan daun daun dan sengaja menden-
        garkan sungai bernyanyi laju kuda itu bisa dicermati begitu rupa seolah kuda itu bergerak
        begitu lamban bagaikan tarian yang terjaga Mereka memerhatikan kuda itu dengan bertanya
        tanya Kuda bukanlah binatang yang asing bagi mereka begitu pula kuda yang berlari lepas di
        padang padang terbuka Namun laju kuda ini bukanlah laju kuda biasa bukan hanya karena
        lebih cepat namun mengapakah seekor kuda harus berlari secepat itu Kitab Omong Kosong
        Kuda itu berlari ke arah desa mereka Apakah orang orang akan me nangkapnya Satya melihat
        kesibukan yang luar biasa di gerbang desa Orang orang berlarian membawa tombak bambu
        runcing pentungan kayu bahkan juga alu Apakah yang akan mereka lakukan Apakah mereka
        akan membunuh kuda gagah perkasa yang melaju dengan kecepatan angin itu Tapi untuk apa
        membunuh kuda indah yang tidak bersalah Apa yang mereka lakukan Satya bertanya Tak ada
        satu anak pun bisa menjawabnya Seingat Satya tidak ada sesuatu yang istimewa belakangan
        ini yang harus mereka perhatikan se perti misalnya jika orang orang desa harus melakukan
        upacara Kalau ada sesuatu yang harus diketahuinya anak anak akan mendapat penjelasan dari
        orangtuanya
        """
print(x)
#membersihkan kata asal x
x = clean(x)

#generate kata kunci random sepanjang N
N = 7
k = "".join(random.choices(string.ascii_lowercase, k=N))
k = "inikatakunci"
# mengenkripsi x dengan kunci k
y = e_vigenere(x,k)
b = list(y)
print(b)
c = []
for i in range(len(b)):
    c.append(b[i])
    if (i+1) % 5 == 0:
        c.append(" ")
print("".join(c))
#menebak panjang kunci k
m = len_k(y)

# menghitung frekuensi tiap huruf di y1,y2,...,ym
Y = []
temp = block(y, m)
for i in temp:
    Y.append(i)
fi = []
for i in Y:
    fi.append(count(i))

Hasil = []
hasil = []

# menghitung mutual koinsidensi untuk setiap y1,y2,...ym
for g in range(26):
    for i in range(m):
        Hasil.append([i, g, mutual_koinsiden(fi[i], g, pi)])

# mencari
for i in range(len(Hasil)):
    if Hasil[i][2] >= 0.85 * Ic:
        hasil.append(Hasil[i])
    print(Hasil[i])
hasil = Sort(hasil)
for i in range(len(hasil)):
    hasil[i] = hasil[i][1]
key = number_to_letter(hasil)
print("kunci yang digunakan:", k)
print("kunci yang ditebak:", key)
print("kata asal:", d_vigenere(y, key))
