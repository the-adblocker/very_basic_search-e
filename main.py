# print("howdy world")
f = open("tekstfil1.txt", "r")
g = open("tekstfil2.txt", "r")
h = open("tekstfil3.txt", "r")
file1 = f.read()
file2 = g.read()
file3 = h.read()
file1_list = []
file2_list = []
file3_list = []


searchgo = 0

def getWord():
    print("____________________________________________")
    print("")
    sw = input("search for a word:  ")
    print("")
    print("____________________________________________")
    print("")
    return sw

def searchtype():
    s_type = 0
    print("")
    print("Hva ønsker du å finne?")
    print("1: vis ord | 2: vis antall ord | 3: vis linje med ordet | 4: vis alt")
    while s_type == 0:
        s_type = int(input(""))
        if s_type == 1 or s_type == 2 or s_type == 3 or s_type == 4:
            print("")
        else:
            print("vennligst velg et tall 1-4")
            s_type = 0
    print("")
    return s_type

def chooseFile():
    c_file = 0
    print("")
    print("Hvilken tekstfil ønsker du å se i?")
    print("1: tekstfil1 | 2: tekstfil2 | 3: tekstfil3 | 4: vis alle filer")
    while c_file == 0:
        c_file = int(input(""))
        if c_file == 1 or c_file == 2 or c_file == 3 or c_file == 4:
            print("")
        else:
            print("vennligst velg et tall 1-4")
            c_file = 0
    print("____________________________________________")
    print("")
    return c_file


searchword = getWord()
stype = searchtype()
cfile = chooseFile()

def lesInnTekst():
    print("")




def finnOrd(ord):

    a = 0
    while a != -1:
        if a == 0:
            a = file1.find(ord, a)
            if a == -1:
                break
            b = file1.find(" ", a)
            c = file1.find("\n", a)
            if b < c:
                file1_list.append(file1[a:b])
            else:
                file1_list.append(file1[a:c])
            # print(file1[a:b])

            
            a+=1
        else:
            a = file1.find(ord, a + 1)
            b = file1.find(" ", a+1)
            # print(file1[a:b])
            c = file1.find("\n", a + 1)
            if b < c:
                file1_list.append(file1[a:b])
            else:
                file1_list.append(file1[a:c])
            

    a2 = 0
    while a2 != -1:
        if a2 == 0:
            a2 = file2.find(ord, a2)
            if a2 == -1:
                break
            b2 = file2.find(" ", a2)
            c2 = file2.find("\n", a2)
            if b2 < c2:
                file2_list.append(file2[a2:b2])
            else:
                file2_list.append(file2[a2:c2])
            # print(file1[a:b])

            
            a2+=1
        else:
            a2 = file2.find(ord, a2 + 1)
            b2 = file2.find(" ", a2+1)
            # print(file1[a:b])
            c2 = file2.find("\n", a2 + 1)
            if b2 < c2:
                file2_list.append(file2[a2:b2])
            else:
                file2_list.append(file2[a2:c2])
            


    a3 = 0
    while a3 != -1:
        if a3 == 0:
            a3 = file3.find(ord, a3)
            if a3 == -1:
                break
            b3 = file3.find(" ", a3)
            #print(file3[a3:b3])
            c3 = file3.find("\n", a3+1)
            if b3 < c3:
                file3_list.append(file3[a3:b3])
            else:
                file3_list.append(file3[a3:c3])
            
            a3+=1
        else:
            a3 = file3.find(ord, a3 + 1)
            b3 = file3.find(" " or ",", a3+1)
            #print(file3[a3:b3])
            c3 = file3.find("\n", a3+1)
            if b3 < c3:
                file3_list.append(file3[a3:b3])
            else:
                file3_list.append(file3[a3:c3])
    if len(file1_list) > 0:

        file1_list.remove("")
    if len(file2_list) > 0:

        file2_list.remove("")
    if len(file3_list) > 0:

        file3_list.remove("")

            







def printOrd():

    count1 = len(file1_list)
    count2 = len(file2_list)
    count3 = len(file3_list)


    if cfile == 1 or cfile == 4:

        if stype == 1 or stype == 4:
            print(file1_list)

        if stype == 2 or stype == 4:
            print("I fil 1 finner vi", searchword, count1, "ganger")
            print("")

        if stype == 3 or stype == 4:
            filename1 = r"tekstfil1.txt"

            with open(filename1) as filer1:
                lines1 = filer1.readlines()
            

            for number1, line1 in enumerate(lines1, 1):  

                if searchword in line1:  
                    print(searchword, 'er på linje', number1, "i tekstfil 1")
            
        print("")
        print("____________________________________________")
        print("")


    if cfile == 2 or cfile == 4:
        if stype == 1 or stype == 4:
            print(file2_list)
        if stype == 2 or stype == 4:
            print("I fil 2 finner vi", searchword, count2, "ganger")
            print("")

        if stype == 3 or stype == 4:
            filename2 = r"tekstfil2.txt"

            with open(filename2) as filer2:
                lines2 = filer2.readlines()

            for number2, line2 in enumerate(lines2, 1):  

                if searchword in line2:  
                    print(searchword, 'er på linje', number2, "i tekstfil 2")
            
        print("")
        print("____________________________________________")
        print("")


    if cfile == 3 or cfile == 4:
        if stype == 1 or stype == 4:
            print(file3_list)

        if stype == 2 or stype == 4:
            print("I fil 3 finner vi", searchword, count3, "ganger")
            print("")


        if stype == 3 or stype == 4:
            filename3 = r"tekstfil3.txt"
            

            with open(filename3) as filer3:
                lines3 = filer3.readlines()

            for number3, line3 in enumerate(lines3, 1):  

                if searchword in line3:  
                    print(searchword, 'er på linje', number3, "i tekstfil 3")
        
        print("")
        print("____________________________________________")
        print("")


finnOrd(searchword)
printOrd()




    
    


# print(f.read())

# with open(r'tekstfil1.txt', 'r') as file1:
#         # read all content from a file using read()
#         content1 = file1.read()
#         # check if string present or not
#         if searchword in content1:
#             print('string exist in file 1')
#         else:
#             print('string does not exist')
# file1.close()
		
			

# # if searchgo == 1:
# with open(r'tekstfil2.txt', 'r') as file2:
#         # read all content from a file using read()
#         content2 = file2.read()
#         # check if string present or not
#         if searchword in content2:
#             print('string exist in file 2')
#         else:
#             print('string does not exist')
# file2.close()



# # if searchgo  == 2:
# with open(r'tekstfil3.txt', 'r') as file3:
#         # read all content from a file using read()
#         content3 = file3.read()
#         # check if string present or not
#         if searchword in content3:
#             print('string exist in file 3')
#         else:
#             print('string does not exist')
# file3.close()
