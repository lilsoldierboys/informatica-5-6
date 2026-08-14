

def main():
    unput = input(" ")
    unput = unput.replace(":)" , "🙂", count=-1)
    unput = unput.replace(":(" , "🙁", count=-1)
    print(unput)


main()
