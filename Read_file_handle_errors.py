try:
    with open("sample.txt", "r") as f:
        reading_data = f.read()
        print(reading_data)

except:
    print("Error : File sample.txt does not found")