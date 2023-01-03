# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atliks nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

def getUserAverageAge(users):
    all_users_age = []
    for q in range (len(users)): # sukuriamas ciklas reiksmems gauti
      users_age = users[q].get("age") # gaunamos users metu reiksmes
      all_users_age.append(users_age) # reiksmes idedu i sarasa all_users_age
      # print(users_age)
    print(all_users_age)
    users_average_age = round((sum(all_users_age) / len(all_users_age)), 2) # suskaiciuoju visu users metu vidurki (metu suma padalinti is saraso ilgio)
    print(f"Users average age: ", users_average_age)
getUserAverageAge(users)

def getUsersNames(users):
    names = []
    for y in range (len(users)): # sukuriamas ciklas visoms reiksmems gauti
      names.append(users[y].get("name")) # gauta sarasa su vardais pridedu i names masyva
    print(sorted(names)) # vardu masyvas ispausdinamas pagal abecele

getUsersNames(users)