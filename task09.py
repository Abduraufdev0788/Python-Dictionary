users = [
  {"id": 1, "active": True},
  {"id": 2, "active": True},
]
for i in users:
    i["active"] = False
print(users)