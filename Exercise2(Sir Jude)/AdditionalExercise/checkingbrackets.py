# declare function takes 1 parameter
def isPairedParenthesis(stringValue):
    #declare a list to store the closing brackets in sequence
    queue = []

    #loop each element in stringValue
    for char in stringValue:
        #if current element is opening bracket
        if char == "[":
            #then add closing pair to the queue list
            queue.append("]")
        #if current element is closing bracket
        elif char == "]":
            #if there is not found in the queue
            if len(queue) == 0 :
                return False
            #if founded then remove the closing bracket from queue list
            else:
                #remove closing bracket
                 queue.pop()

    #if queue list is empty then true else false
    return len(queue) == 0



#calling function
print(isPairedParenthesis("[[]]]]["))

