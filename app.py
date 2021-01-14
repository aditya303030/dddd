# num = input('enter a number: ')
# list2=[]
# list1 = list(num)
# n = len(list1)
# k = 0
# for i in range(k,n):
#     a = int(list1[k])
#     d = a**3
#     list2.append(d)
#     k+=1
# b = sum(list2)
# print(b)
# c = int(num)

# if b==c:
#     print('it is an Armstron number.')
# else:
#     print('It is not an Armstrong number.')

# x = int(input('enter number of seconds: '))
# mins = x//60
# seconds = x%60
# print('{} seconds is equal to {} minutes and {} seconds.'.format(x,mins,seconds))
 
# string = input('enter a string: \n')
# char = input('enter a character: ')

# num = 0
# list1 = list(string)
# list2 = list(char)
# n = len(list1)
# for i in range(0,n):
#     if list2 in list1:
#         num+=1
# print('the character {} occures in the string {} {} times.'.format(char,string,num))
# s = input('enter a string: \n')
# c = input('enter a character: \n')
# num = 0

# for i in range(len(s)):
#     if s[i]==c:
#         num+=1
# print(num)

# string = input('enter a string: ')
# vowels = ['a','e','i','o','u']
# list1 = []
# for x in string:
#     if x in vowels:
#         list1.append(x)

# print(list1)
# print('There are {} vowels in string {}.'.format(len(list1),string))

# n = int(input('enter number of nums: '))
# list1 = []
# k = 0

# for i in range(1,(2*n+1),2):
#     list1.append(i)
#     list1.reverse()
     

# print(list1)   


# Python program to print odd Numbers in given range 
# start = int(input('enter starting num of range: '))
# end = int(input('enter end num of range: '))
# iterating each number in list 
# for num in range(start, end*2): 
      
    # checking condition 
    # if num % 2 != 0: 
        # print(num, end = " ") 

# string = input('enter a sentence: ')
# words = char = dig = spc_char = spaces = 0

# for i in range(0,len(string)):
#     if string[i] == ' ':
#         spaces+=1
#     char = len(string)-spaces 
#     words = spaces+1
#     elif string[i]   







# s = input('Enter a sentence : ')
# spaces = 0
# digs = 0
# number_of_words = 1
# number_of_characters = len(s)
# al_num = 0
# for i in s:
#     if i.isalnum():
#         al_num += 1
#     elif i == ' ': # there is a space means there is another word
#         number_of_words += 1
#         spaces+=1        
# print('Number of words are', number_of_words)
# print('Number_of_characters are', number_of_characters)
# print('the number of spaces are', spaces)
# import string
# s = input("String:\n")
# d = sc = l = w = spaces = 0
# for x in s:
#     if x in string.ascii_letters: 
#         l += 1
#     elif x in string.digits: 
#         d += 1
#     elif x in string.punctuation: 
#         sc += 1
#     elif x==" ":
#         spaces+=1
#     w = spaces +1
# print("digits:",d,"letters:",l,"special characters:",sc, 'Words:',w)

# series = ('1+2+3+4...+n')
# n = int(input('enter last number os series: '))
# sum_n = (n/2)*(2+(n-1))
# print(sum_n)

# series1 = ('1^2+2^2+3^2+...+n^2')
# n = int(input('enter last number os series: '))
# sum1 = (n*(n+1)*(2*n+1))/6
# print(sum1)
# from math import factorial
# print("Series: x – x2 /2! + x3 /3! – x4 /4! + x5 /5! – x6 /6! (Input x) ")
# sum = 0
# x = int(input("x:\n"))
# for n in range(1,7): 
#     sum += ( (x ** n) / (factorial(n)) ) * ((-1) ** (n-1) )
# print("Answer:",sum)


# x = []
# while True:
#     print("int",str(len(x)+1)+ ':')
#     i = input()
#     if i != 'n' and i.strip().replace(' ','') != '' and i.isdigit():
#         x.append(int(i))
#     else: break

# y = []
# for e in x: y.insert(0, e)
# print("New list:",y)
# list1=[]
# k = 0
# n = int(input('enter number of inputs: '))
# while k<n:
#     input1 = int(input('enter a number: '))
#     list1.append(input1)
#     k+=1

# list1.reverse()
# print('New list:', list1)
# list1 = ['a','e','i','o','u']
# list2 = []
# k = 0
# n = int(input('enter number of strings: '))
# while k<n:
#     input1 = input('enter a string: ')
#     for i in input1:
#         if input1[0] in list1:
#             list2.append(input1)
#             break
#     k+=1
# print(list2)
# vowel = 'AEIOUaeiou'
# s = input('enter a string: ')

# for x in s:
#     for y in vowel:
#         if x==y:
#             s.replace(x,'*')
# s = input("String:\n")
# for vowel in "aeiou": 
#     s = s.replace(vowel, "*")
# print("New string:",s)
# for i in range(5):
#     for j in range(5,i,-1):
#         print(j, end=" ")
#     else:
#         print()
# stud1=[]
# stud2=[]
# stud3=[]
# stud4=[]
# stud5=[]

# for subject in range(3):
#     a = int(input('enter marks for subject'))
#     stud1.append(a)
#     a1=tuple(stud1)
# for subject in range(3):
#     b = int(input('enter marks for subject'))
#     stud2.append(b)
#     a2=tuple(stud2)

# for subject in range(3):
#     c = int(input('enter marks for subject'))
#     stud3.append(c)
#     a3=tuple(stud3)

# for subject in range(3):
#     d = int(input('enter marks for subject'))
#     stud4.append(d)
#     a4=tuple(stud4)

# for subject in range(3):
#     e = int(input('enter marks for subject'))
#     stud5.append(e)
#     a5=tuple(stud5)


# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# for stud in range(5):
#     for sub in range(3):
#         mark1 = int(input('enter sub 1 marks: '))
#         mark2 = int(input('enter sub 2 marks: '))
#         mark3 = int(input('enter sub 3 marks: '))
#         mark = (mark1,mark2,mark3)
#         print(mark)
#         total = sum(mark)
#         average = total/3
#         print('the total score of the student {} is {} and the average is {}.'.format(stud+1,total,average))
#         break









