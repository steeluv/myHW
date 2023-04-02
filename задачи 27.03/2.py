data = input()
def magic_data(data):
    split_data = data.split('.')
    day = int(split_data[0])
    month = int(split_data[1])
    year = int(split_data[2][2::])
    if day * month == year:
        return True
    else:
        return False

print(magic_data(data))