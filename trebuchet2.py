def number():
    lmao = open("poopycumcum.txt")
        
    y = ""
    
    #numl = ['o', 't', "f", "s", "e", "n"]

    poop = []

    #splits file into lines and makes range of the length of the string to access characters
    for line in lmao:
        for x in range(len(line)):

            #checks if character is not the newline character
            if line[x] != "\n":

                #checks if it is numeric and then adds it to a string y 
                if line[x].isnumeric():

                    y = y + line[x]
                    continue
                
                #checks for any starting letters of single digit numbers and then checks string for the full word and adds it y
                if line[x] == 'o' or line[x] == 't' or line[x] == 'f' or line[x] == 's' or line[x] == 'e' or line[x] == 'n':
                    if line.startswith('one', x):
                        y = y + '1'
                        continue
                    if line.startswith('two', x):
                        y = y + '2'
                        continue
                    if line.startswith('three', x):
                        y = y + '3'
                        continue
                    if line.startswith('four', x):
                        y = y + '4'
                        continue
                    if line.startswith('five', x):
                        y = y + '5'
                        continue
                    if line.startswith('six', x):
                        y = y + '6'
                        continue
                    if line.startswith('seven', x):
                        y = y + '7'
                        continue
                    if line.startswith('eight', x):
                        y = y + '8'
                        continue
                    if line.startswith('nine', x):
                        y = y + '9'
                        continue
                        
                        

            else:
                y = int(y[0] + y[-1])
                poop.append(y)
                y = ""

    return poop


def adder(stinky):
    y = 0
    for x in stinky:
        y = y + x
    return y


a = number()

print(adder(a))
