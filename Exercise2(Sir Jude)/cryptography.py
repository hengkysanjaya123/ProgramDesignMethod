while True:
    while True:
        # validate input rotation
        try:
            rotation = int(input("Number of rotation : "))
            break
        except ValueError:
            print("Please input integer ")

    #declare new dictionary to store encode / decode data
    key = {}

    #define a function to generate encode / decode data
    def generateDictionary():
        #declare list alphabet
        dataUpper = list("abcdefghijklmnopqrstuvwxyz")
        dataLower = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        #add to dictionary the values of the pair for the upper case
        for i in dataUpper:
            key[i] = dataUpper[(dataUpper.index(i) + rotation )% 26]

        #add to dictionary the values of the pair for the lower case
        for i in dataLower:
            key[i] = dataLower[(dataLower.index(i) + rotation )% 26]

        print(key)

    #define encode function passing stringValue to be encoded
    def encode(stringValue):
        data = ""
        #loop each element in stringValue and get the value of specific key from dictionary then store into variable data
        for i in stringValue:
            data += key[i]
        return data

    #define decode function passing stringValue to be decoded
    def decode(stringValue):
        data = ""
        #loop each element in stringValue and get the key from specific value from dictionary then store into variable data
        for i in stringValue:
            data += key.get(i)
        return data


    #calling statement
    generateDictionary()
    inputed = input("Please input text you want to decode : ")

    print("Encoded : " + encode(inputed))
    print("Decoded : " + decode(encode(inputed)))

    #ask confirmation to repeat
    operation = input("Do you want to repeat ? (Yes/No) : ")
    if(operation.lower()[0] == 'n'):
        break
