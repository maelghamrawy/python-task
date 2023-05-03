
#first soultion without function 
string = "abracadabra"     #here we initlize the string we want to change it
my_list = list(string)     #convert the string to list so we can change on it
my_list[5] = "k"           #change chatacter in index 5 
string = ''.join(my_list)  #use join to return it back to list 
print(string)




# function soultion 
def function( string, postion, ch):

    myList = list(string)       #here we initlize the string from the user
    myList[postion] = ch        #convert the string to list so we can change on it
    string = ''.join(myList)    #change chatacter in index the user enter  
    print(string)

function("abracadabra",5,"k") #invoke the function




