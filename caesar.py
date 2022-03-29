#Program implementation of Caesar cipher algorithm 
def caesar_encypt(txt, s):  
        result = ""  
    # transverse the plain txt  
        for i in range(len(txt)):  
            char = txt[i]  
            # encypt_func uppercase characters in plain txt  
      
            if (char.isupper()):  
                result += chr((ord(char) + s - 65) % 26 + 65)  
            # encypt_func lowercase characters in plain txt  
            else:  
                result += chr((ord(char) + s - 97) % 26 + 97)  
        return result  
    # check the above function  
txt = input("Type text : ") 
s = int(input("How many letters go forward? "))  
print("Main txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Caesar: " + caesar_encypt(txt, s))  
#text = input("Type text : ")
#s = int(input("How many letters go forward? "))