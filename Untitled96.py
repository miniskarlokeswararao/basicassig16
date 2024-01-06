#!/usr/bin/env python
# coding: utf-8

# In[22]:


n = int(input("Enter the range = "))

class generator_divisible7:
    def __init__(self, n):
        self.a = n
        print("Given range is (__init__)", self.a)

    def division7(self):
        for i in range(0, self.a + 1):
            if i % 7 == 0:
                print("We are inside the method block", i)

# Create an instance of the class
obj = generator_divisible7(n)

# Call the division7 method
obj.division7()


# In[12]:





# In[ ]:





# In[2]:


#Question 3:
#Define a class Person and its two child classes: Male and Female. 
#All classes have a method "getGender" which can print "Male" 
#for Male class and "Female" for Female class.
class Person:
    def getGender(self):
        pass  # This method will be overridden in the child classes

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

# Example usage:
male_person = Male()
female_person = Female()

male_person.getGender()  # Output: Male
female_person.getGender()  # Output: Female

    


# In[3]:



subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

# Generate all possible sentences
sentences = [f"{subject} {verb} {obj}" for subject in subjects for verb in verbs for obj in objects]

# Print the generated sentences
for sentence in sentences:
    print(sentence)


# #question
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# 
# Suppose the following input is supplied to the program:
# 
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 
# Then, the output should be:
# 
# 2:2
# 
# 3.:1
# 
# 3?:1
# 
# New:1
# 
# Python:5
# 
# Read:1
# 
# and:1
# 
# between:1
# 
# choosing:1
# 
# or:2
# 
# to:1
# 
# 
# 

# In[62]:


#ans)
def word_frequency(input_text):
    words = input_text.split()
    print("in sentance words are splitted =",words)
    count={}
    c=1
    for i in range(0,len(words)-1,):
        #print(i,words[i])
        if(words[i]==words[i+1]):
            #print(words[i],"==",words[i+1])
            #print(words[i],"number of its repeated is = ",c+1)
            print(words[i],"-------------------------------------> ",c+1)
            c=c+1
        
        else:
            c=c-c+1
            #print(words[i+1],"is reapted for  =  ",c)
            print(words[i+1],"----------------------------> ",c)
        
        
        
        
word_frequency("hello hello hello hello hello how  how are you dear")


# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# 
# Suppose the following input is supplied to the program:
# 
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# 
# Then, the output should be:
# 
# 2:2
# 
# 3.:1
# 
# 3?:1
# 
# New:1
# 
# Python:5
# 
# Read:1
# 
# and:1
# 
# between:1
# 
# choosing:1
# 
# or:2
# 
# to:1
# 
# 

# In[63]:


def word_frequency(input_text):
    word_count = {}

    # Split the input text into words
    words = input_text.split()

    # Count the frequency of each word
    for word in words:
        # Remove punctuation marks
        word = word.strip('.,?!:;()[]{}"\'')
        # Convert to lowercase for case-insensitive counting
        word = word.lower()

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Sort the word frequencies alphanumerically
    sorted_word_count = sorted(word_count.items())

    # Print the results
    for word, count in sorted_word_count:
        print(f"{word}:{count}")

# Example usage
input_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
word_frequency(input_text)


# In[ ]:


def word_frequency(input_text):
    words = input_text.split()
    word_count = {}

    for word in words:
        word = word.strip('.,?:;!"()[]{}')  # Remove punctuation
        word_count[word] = word_count.get(word, 0) + 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: (x[0].lower(), x[0].isdigit(), x[1]))

    for word, count in sorted_word_count:
        print(f'{word}:{count}')


if __name__ == "__main__":
    input_text = input("Enter the text: ")
    word_frequency(input_text)


# In[ ]:





# In[65]:


def compress_string(s):
    compressed = ''
    count = 1

    for i in range(1, len(s)):
        
        
        if s[i] == s[i - 1]:
            
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            print(compressed)
            count = 1

    compressed += s[-1] + str(count)
    return compressed

def decompress_string(s):
    decompressed = ''
    i = 0

    while i < len(s):
        char = s[i]
        count_str = ''
        i += 1

        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1

        count = int(count_str) if count_str else 1
        decompressed += char * count

    return decompressed

# Example usage
original_string = "hello world!hello world!hello world!hello world!"
compressed_string = compress_string(original_string)
decompressed_string = decompress_string(compressed_string)

print("Original String:", original_string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)


# In[66]:


#binary sorting
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]

        if mid_element == target:
            return mid  # Element found, return its index
        elif mid_element < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found

# Example usage
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 7

result = binary_search(sorted_list, search_element)

if result != -1:
    print(f"Element {search_element} found at index {result}.")
else:
    print(f"Element {search_element} not found in the list.")


# In[74]:



def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = arr[mid]
        

        if mid_element == target:
            return mid  # Element found, return its index
        elif mid_element < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return 0  # Element not found


# In[ ]:




