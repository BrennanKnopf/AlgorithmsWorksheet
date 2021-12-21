word = input('Put any word here.') 
print(word[::-1])  #this slices a word. You can also use slice to print between position of indexes i.e. [2:5] would print ste from master

sentence = input('Input any sentence you want here. ')
print(sentence)
print(sentence.title()) #for capitalizing every word in a sentence. Words a seperated by one space.



uncompressed_string = 'QQQRRRRHH'



def compress_string2(uncompressed_string):
    count = 1 #counter for index
    index = 0 #starting position
    total_length_string = len(uncompressed_string)
    new_string = ''
    while index != total_length_string: #while starting position is not equal to the total length of string keep looping
        if index == total_length_string - 1: #if index is equal to total length of string - 1 because counting starts at 0
            new_string += uncompressed_string[index] + str(count) #add last set of letters plus the number of said letters to finish the loop
        elif uncompressed_string[index] == uncompressed_string[index + 1]: #if the index is the same as the next index
            count += 1 #add one to the count of letter within index
        else:
            new_string += uncompressed_string[index] + str(count) #if the character in the index is not the same add the letter you have been counting plus the number of times it occured 
            count = 1 #reset the count
        index += 1 # move to the next index
    print(new_string) #print the new string

compress_string2(uncompressed_string)

word = input('Type any word. Lets see if its a palindrome.')

if word == word[::-1]:
    print('Yes this is a palindrome.')
else:
    print('Sorry thats not a palindrome.')


