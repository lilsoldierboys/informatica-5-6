def largest(a):
    list = []
    with open(a) as num_list:
        for number in num_list:
            number = number.replace("\n","")
            list.append(int(number))
    print(max(list))
def main():
    #with open("sample.txt") as new_file:
        #content = new_file.read()


    #count = 0
    #with open("sample.txt") as list:
        #for line in list:
            #line = line.replace("\n","")
            #count += 1
            #print(f"{count}: {line}")

    largest("sample.txt")


main()




