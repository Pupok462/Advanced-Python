import json
import csv

########
# Task 1
########


names = ['A', 'B6', 'C', 'D', 'K']
header = ["vitamin", "vitamers", "solubility", "daily_requirement", "deficiency_diseases"]
json_dict=[]

def create_json():
    with open(file='vitamins.json', mode='w', encoding='utf-8') as vitamins_json:

        for i in range(len(names)):
            file = open("vitamins/%s.txt" % (names[i]), 'r')
            arr = [i.rstrip() for i in file]
            dictionary = {
                header[0] : arr[0],
                header[1] : arr[1].split(','),
                header[2] : arr[2],
                header[3] : float(arr[3]),
                header[4] : arr[4].split(',')
            }
            json_dict.append(dictionary)

        json.dump(json_dict, vitamins_json, indent=4)
        vitamins_json.close()

def create_csv():
    with open('vitamins.csv', 'w', newline='') as vitamin_csv:

        file_writer = csv.DictWriter(vitamin_csv, fieldnames=header)
        file_writer.writeheader()

        for i in range(len(names)):
            file = open("vitamins/%s.txt" % (names[i]), 'r')
            arr = [i.rstrip() for i in file]
            file_writer.writerow({header[0]:arr[0] ,header[1]:arr[1].split(','), header[2]:arr[2],
                                  header[3]:float(arr[3]), header[4]:arr[4].split(',')})
        vitamin_csv.close()



def main():
    create_json()
    create_csv()

if __name__ == "__main__" :
    main()
    print("-- Successfully Compiled")
else:
    print("-- Error")














