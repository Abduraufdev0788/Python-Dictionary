fruicts = {
    "apple" : 3,
    "pear" : 5
}
search = input("qidirilayotgan mevani kiriting: ")
if search not in fruicts:
    fruicts[search] = 0
    
if fruicts[search]==0:
    print("quantity =0")
else:
    print("mahsulot bor")
    
