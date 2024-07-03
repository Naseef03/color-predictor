def save_row(row, file_path="data.csv"):
    # Check the length of row
    if len(row) != 10:
        print("Length of data should be 11")
        return
    
    with open(file_path, 'a') as file:
        file.write(", ".join([str(i) for i in row]) + "\n")
    print("Row:", row, "saved to", file_path)


def load_data(file_path="data.csv"):
    data = []
    with open(file_path, "r") as file:
        for row in file.readlines():
            data.append([int(i) for i in row.strip("\n").split(", ")])
    return data

def save_continues_data(file_path="data.csv"):
    print("Enter the label line by line:")
    row = []
    while True:
        label = input(str(len(row) + 1) + ": ")
        if label == "q":
            return
        
        row.append(int(label))
        if len(row) == 10:
            save_row(row)
            row.pop(0)