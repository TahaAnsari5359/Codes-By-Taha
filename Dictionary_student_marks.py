
names = input('Enter Students Name: ')
try:
    my_dict = {"Alice": 80, "Max": 90, "Michel": 50, "Alex":100 }

    print(names, "Marks: ", my_dict[names])
except:
    print("Name Doesent Found")