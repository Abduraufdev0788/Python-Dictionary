key = input("matnni kiriting : ")

dict = {
    "a" : "salom",
    "b" : "olma",
    "c" : "behi"
}
value = dict.get(key, "topilmadi")

print(value)