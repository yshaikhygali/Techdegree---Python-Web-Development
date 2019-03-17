import sys

def rememberer(thing):
    #open file
    # by default open is just for reading
    # file = open('database.txt', 'a')
    with open('database.txt', 'a') as file:

        #write thing to file
        file.write(thing + "\n")

        #close file
        # file.close() - No need

def show():
    # open file
    with open('database.txt') as file:
        for line in file:
            print(line)
    # print out each line in file
    # close file



# if __name__ == '__main__':
    # rememberer(input("What should I remember? "))

if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer('n'.join(sys.argv[1:]))
