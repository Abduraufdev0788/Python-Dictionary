
config = {
    
}
for i in range(3):
    key = input(f"{i} key va qiymatini kiriting (,): ")
    text = key.split(",")
    config[text[0]] = text[1]
    
print(config)
    