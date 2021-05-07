def swapFileData():
    file1=input("Enter the name of file1")
    file2=input("Enter the name of file2")
    data_a=0
    data_b=0
    with open(file1,"r") as a:
        data_a=a.read()
    with open(file2,"r") as a:
        data_b=a.read()
    with open(file1,"w") as a:
        a.write(data_b)
    with open(file2,"w") as a:
        a.write(data_a)
swapFileData()
        