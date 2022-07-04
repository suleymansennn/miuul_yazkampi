#########################################################################################################
######################################### Odev 2 ########################################################

# Görev 1: Kendi isminizde bir virtual environment oluşturunuz, oluşturma esnasında python 3 kurulumu yapınız.
# conda create -n pyth3 python=3.9

# Görev 2: Oluşturduğunuz environment'i aktif ediniz.
# conda activate pyth3

# Görev 3: Yüklü paketleri listeleyiniz
# conda list

# Görev 4: Environment içerisine Numpy'ın güncel versiyonu ve Pandas'ın 1.2.1 versiyonunu aynı anda indiriniz.
# conda install pandas=1.2.1 numpy

# Görev 5: İndirilen Numpy'ın veriyonu nedir?
# conda list numpy

# Görev 6: Pandas'ı upgraded ediniz. Yeni versiyonu nedir?
# conda upgrade pandas
# conda list pandas

# Görev 7: Numpy'ı environment'tan siliniz.
# conda remove numpy

# Görev 8: Seaborn ve matplotlib kütüphanesinin güncel versiyonlarını aynı anda indiriniz
# conda install seaborn matplotlib

# Görev 9: Virtual enviroment içindeki kütüphaneleri versiyon bilgisi ile beraber export edinizi ve yaml dosyasını inceleyiniz.
# conda env export > enviroment.yaml

# Görev 10: Oluşturduğunuz environmenti siliniz.
# conda deactivate
# conda env remove -n pyth3

#########################################################################################################
######################################### Odev 3 ########################################################
# Soru 1
# Verilen Değerlerin veri yapılarını inceleyeniz...
################################################################################################
x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}
type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)
################################################################################################
# Soru 2
# Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space
# koyunuz, kelime kelime ayırınız.
################################################################################################
text = "The goal is to turn data into information and information into insight"
text = text.upper()
text.replace(".", " ")
text.replace(",", " ")
text.split(" ")
###############################################################################################
# Soru 3
# Verilen Listeye göre
# Adım1: Verilen listenin eleman sayısına bakınız.
# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız
# Adım3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturunuz
# Adım4: Sekizinci indeksteki elemanı siliniz
# Adım5: Yeni bir eleman ekleyiniz
# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz
################################################################################################
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0], lst[10]
lst[0:4]
del lst[8]
lst.append("S")
lst.insert(8, "N")
#################################################################################################
# Soru 4
# Verilen sözlük yapısına göre;
# Adım1: Key değerlerine erişiniz.
# Adım2: Value değerlerine erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.
################################################################################################
dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}
dict.keys()
dict.values()
dict["Daisy"][1] = 13
dict["Ahmet"] = ["Turkey", 24]
del dict["Antonio"]
dict
################################################################################################
# Soru 5
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan
# ve bu listeleri return eden fonksiyon yazınız.
################################################################################################
l = [2, 13, 18, 93, 22]
even_list = []
odd_list = []


def myFunc(x):
    for i in x:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


odd_list, even_list = myFunc(l)
print(odd_list, even_list)
################################################################################################
# Soru 6
# Tek bir List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
# harfe çeviriniz ve başına NUM ekleyiniz.
################################################################################################
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns
df.columns = ["NUM_" + col.upper() if df[col].dtypes != "object" else col.upper() for col in df.columns]
df.columns
################################################################################################
# Soru 7
# Tek bir list cComprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.
################################################################################################

df = sns.load_dataset("car_crashes")
[col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]

################################################################################################
# Soru 8
# List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden farklı olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
################################################################################################
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
df_new = df[new_cols]
df_new

