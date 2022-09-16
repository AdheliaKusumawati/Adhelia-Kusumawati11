indeks = {
    "celcius   " : "c",
    "reamur    " : "r",
    "fahrenheit" : "f",
    "kelvin    " : "k",
}
print ("==========indeks satuan skala suhu==========")
for i in indeks :
    print("satuan suhu :", i, "\t Indeks : ",indeks[i])

suhu = float(input("Masukkan suhu : "))
satuan = input ("Masukkan indeks satuan skala suhu : ") 

if (satuan == "c"):
    print (suhu, "derajat celsius : ")
    print ("Reamur = ", (suhu*4/5), "derajat")
    print ("Fahrenheit = ", ((suhu*9/5)+32), "derajat")
    print ("kelvin = ", (suhu + 273), "derajat")

elif (satuan == "r"):
    print (suhu, "derajat reamur : ")
    print ("celsius = ", (suhu*5/4), "derajat")
    print ("Fahrenheit = ", (suhu*9/4)+32, "derajat")
    print ("kelvin = ", (suhu*5/4 + 273), "derajat")

elif (satuan == "f"):
    print (suhu, "derajat reamur : ")
    print ("celsius = ", (5/9)*(suhu-32), "derajat")
    print ("reamur = ", (4/9)*(suhu-32), "derajat")
    print ("kelvin = ", (5/9)*(suhu-32) + 273, "derajat")

elif (satuan == "k"):
    print (suhu, "derajat kelvin : ")
    print ("celsius = ", suhu-273, "derajat")
    print ("reamur = ", (4/5)*(suhu-273), "derajat")
    print ("fahrenheit = ", (9/5)*(suhu-273 + 32), "derajat")









