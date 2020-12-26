



files = ["1.txt", "2.txt", "3.txt"]
dictionary = {}

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        dictionary[file] = lines


with open("output.txt", "w", encoding="utf-8") as f:
    def write_output(index):
        f.write(files[index])
        f.write("\n")
        f.write(str(len(dictionary[files[index]])))
        f.write("\n")
        f.writelines(dictionary[files[index]])

    if len(dictionary[files[0]]) < len(dictionary[files[1]]) and len(dictionary[files[0]]) < len(dictionary[files[2]]):
        write_output(0)
        if len(dictionary[files[1]]) < len(dictionary[files[2]]):
            write_output(1)
            write_output(2)
        else:
            write_output(2)
            write_output(1)
    elif len(dictionary[files[1]]) < len(dictionary[files[0]]) and len(dictionary[files[1]]) < len(dictionary[files[2]]):
        write_output(1)
        if len(dictionary[files[0]]) < len(dictionary[files[2]]):
            write_output(0)
            write_output(2)
        else:
            write_output(2)
            write_output(0)
    elif len(dictionary[files[2]]) < len(dictionary[files[0]]) and len(dictionary[files[2]]) < len(dictionary[files[1]]):
        write_output(2)
        if len(dictionary[files[1]]) < len(dictionary[files[0]]):
            write_output(1)
            write_output(0)
        else:
            write_output(0)
            write_output(1)

