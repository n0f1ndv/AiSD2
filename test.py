#makes test list.txt
tmp=[]
with open("list.txt", "w") as file:
    for i in range(50000):
        file.write(f"{str(i)} ")
    file.write("\n")
    file.write("increasing\nfmm\nprint\nrebalance\nexit")