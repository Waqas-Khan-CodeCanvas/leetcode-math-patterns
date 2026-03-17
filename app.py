""" 
    1 :- count string charcters
    2 :- length of the last word in a string 
    3 :- reverse string in memory replacement
    4 :- reverse vowels in a string 
    5 :- count  digits of a number
    6 :- sum of digits of a number
    7 :- reverse even digits of a number

"""

# 1 :- count string charcters
def count_string_characters(s:str) -> int:
    character_list = list(s.strip())
    count_characters = 0
    for i in character_list:
        count_characters +=1
    return count_characters
    
    # return len(list(s.strip()))

s = "hello world"
count = count_string_characters(s)
print(f"total characters in {s} is : {count}")    





# 2 :- length of the last word in a string 
def length_of_last_word(s:str) -> int:
    list_of_words = s.strip().split(" ")
    last_word_lenght = len(list_of_words[-1])
    return last_word_lenght
    
    # return len(s.strip().split()[-1])

s = "hello world"
lenght = length_of_last_word(s) 
print(f"lenght of the last word of : {s} is : {lenght}")   



# 3 :- reverse string in memory replacement
def reverse_string(s:int)->str:
    char_list = list (s.strip())
    left_side = 0
    right_side = len(char_list) - 1
    
    while( left_side < right_side):
        char_list[left_side] , char_list[right_side] =char_list[right_side] , char_list[left_side]
        left_side += 1
        right_side -=1
    
    return "".join(char_list)    

s= "hello world"
reverse = reverse_string(s)
print(f"reverse sting of {s} is : {reverse}")    


# 4 :- reverse vowels in a string 
def reverse_vowels(s:str ) -> str :
    char_list = list(s.strip())
    vowels = []
    index_pointer = []
    
    for i in range(len(char_list)):
        if char_list[i].lower() in "aeiou":
            vowels.append(char_list[i])
            index_pointer.append(i)
            
    vowels.reverse()
    for i in range(len(vowels)):
        char_list[index_pointer[i]] = vowels[i]
    
    print("".join(char_list))    
        


reverse_vowels("hello world")    
reverse_vowels("IceCreAm")    
reverse_vowels("Leetcode")    




# 5 :-  count digits of a number
def count_digits_of_number(n:int) ->int:
    count = 0 
    while n > 0 :
        n = n // 10
        count += 1
        
    print(count)    


count_digits_of_number(12345)  



# 6 :-  sum  of digits of a number
def count_digits_of_number(n:int) ->int:
    sum = 0 
    while n > 0 :
        sum += n % 10
        n = n // 10
        
    print(sum)    


count_digits_of_number(12345)  