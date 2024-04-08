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
        allowed_keys=json.load(file_obj)

    if field not in allowed_keys:
        return None

    return allowed_keys.get(field,None)


def main():
    data=read_data(file_name="sequential.json", field="unordered_numbers")
    print(data)


if __name__ == '__main__':
    main()