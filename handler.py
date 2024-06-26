def save_row(row, file_path="data.csv"):
    with open(file_path, 'a') as file:
        file.write(", ".join([str(i) for i in row]) + "\n")
    print("Row:", row, "saved to", file_path)
    