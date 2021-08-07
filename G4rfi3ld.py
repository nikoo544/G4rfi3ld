import codecs

# "I hate Mondays."

print("G4RFI3LD D3C0D3R - LASAGNA TEAM")
print()
print("Hi John.")
print()

def menu():
    print("[1] ENCODE A MESSAGE")
    print("[2] D-CODE A MESSAGE")
    print("[0] Exit")

menu()

print(" ")
option = int(input("Enter your choose: "))
print()

while option!= 0:

    #Encode the message
    if option == 1:

        text = input('Enter the text to encode: ')

        #Diccionario
        base = 'abcdef0123456789'
        garfield = 'GARFIELDg4rfi3ld'

        #Encode text to hex to G4rfi3ld
        encode = text.encode("utf-8").hex()
        magic = str.maketrans(base,garfield)

        print()
        print("Encoded message:")
        print()
        print(encode.translate(magic))
        print()
        break

    #Decode the message
    elif option == 2:

        text = input('Enter the text to d-code: ')

        #Diccionario para ungarfieldlización
        garfield = 'GARFIELDg4rfi3ld'
        base = 'abcdef0123456789'
        
        #Encode G4rfi3ld to hex to ASCII
        magic = str.maketrans(garfield,base)
        hextext = text.translate(magic)
        decode = bytes.fromhex(hextext).decode('utf-8')

        print()  
        print('Decoded message:')  
        print()  
        print(decode)
        break

    else:
        print("John, " + str(option) + " is a invalid option")
        print()
        menu()
        print()
        option = int(input("Enter your choose: "))

print()    
print("Bye John")

        

                #              _.++. .+.                                 
                #            .'///|\Y/|\;                               
                #           : :   _ | _ |                                
                #          /  `-.' `:' `:                                 
                #         /|i, :     ;   ;.                             
                #        ,     |     |   |`\                            
                #        ||Ii  :     |   |  ;                          
                #        ;      \--gg;-gg; i:                           
                #        ||Ii    `._,gg.'   |                               
                #        '       .' `**'`. i;                               
                #         `.\`   `. .'`..' /                            
                #          |`-._      __.-'                              
                #          :           `.                                
                #         /i,\  ,        \                               
                #        /    ; :         \                              
                #       :Ii  _:  \         ;                            
                #       ;   (     ;        :                              
                #       :i'( _,  /         ;                           
                #        ;. `"--'         /                             
                #        :i\Ii'         .'                               
                #        |  ;  :__.--:*"                                     
                #        |Ii|  :  ;  :                                   
                #        ;  |  |  |  |                                  
                #       /Y  |  |  |  | [bug]                            
                #   .=-'Y  /|  ;  |  |                                  
                #  :E    .' ;  L__:-***-.-***-.                             
                #   `=--' .'       _   , ;   , ;                         
                #        '----.__.__J--'"`*--'"    
