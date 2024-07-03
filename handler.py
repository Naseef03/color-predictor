def save_row(row, file_path="data.csv"):
    # Check the length of row
    if len(row) != 11:
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
