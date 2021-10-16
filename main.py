from os import close


CreationO = open(file="Creation.txt",mode="r")
Creation = CreationO.readline(1)
nameO = open("name.txt","a+")
ageO = open("age.txt","a+")
countryO = open("country.txt","a+")
#^^^Importing files^^^
#\/Short creation\/
if Creation == "0":
    CreationO.close
    print("Welcome plese add informations to use this system")
    name = input("Name: ")
    age = input("age in words: ")
    country = input("Country: ")
    print("Thanks!")
    nameO.write(name)
    ageO.write(age)
    countryO.write(country)
    CreationO = open(file="Creation.txt",mode="w+")
    CreationO.write("True")
#\/First code(pick action)\/
print("Hello",nameO.readline(1))
print("I'm Si your bot asistent")
print("what you want to do?")
print("1.show me the apps \n2.wants to do the setup again")

    

