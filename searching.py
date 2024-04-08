import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):

    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path=os.path.join(cwd_path,file_name)
    with open("sequential.json",mode="r") as file_obj:
        data=json.load(file_obj)
    for key in data.keys():
        if field ==key:
            sequential_data = data[field]
            return sequential_data
    return None


def linear_search(search_sequence, search_number):
    positions=[]
    count=0
    for i in range(len(search_sequence)):
        if search_sequence[i]==search_number:
            count+=1
            positions.append(i)
    slovnik = {"positions":positions,"count":count}
    return slovnik

def pattern_search(data, vzor):
    velikost_vzoru= len(vzor)
    delka_data= len(data)
    positions = []
    count = 0
    for i in range(delka_data-velikost_vzoru+1):
        if data[i:i+velikost_vzoru] == vzor:
            count += 1
            positions.append(i)
    slovnik = {"positions": positions, "count": count}
    return slovnik

def binary_search(numbers,cislo):
    left = 0
    right = len(numbers)-1
    while left <= right:
        mid=(left+right) // 2
        if numbers[mid] == cislo:
            return mid
        elif numbers[mid] < cislo:
            left=mid+1
        else:
            right = mid-1
    return None

def main():
    data=read_data(file_name="sequential.json", field="ordered_numbers")
    print(data)
    search=linear_search(data, search_number=0)
    print(search)
    vysledek=pattern_search(data,vzor="ATA")
    print(vysledek)
    binary=binary_search(data,cislo=8)
    print(binary)


if __name__ == '__main__':
    main()