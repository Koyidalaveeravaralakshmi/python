#                                              DAY1  7-05-25
#  print(“Hello world!”) 
# print(“Hello Harika”) 
# name = “Virat” 
# print(“hello “+name ) 
# name = input(“enter name:”) 
# print(“Hello”+name) 
# print(“Hello”) 
# # name = input(“enter name “) 
# # print(“hello “ + name) 
# “Good morning mr name! How are you?” 
# name = input(“Enter your name: “) 
# print(“Good morning Mr. “ + name + “! How are you?”) 
#print(“good morning mr. “ + name + “! How are you? “ + name ) 
# name = input() 
#print(f”hello {name}”) 
#print(“hello {} , how are you {}”.format(name,name)) 


# #a = 10
# #b= 5 
# #print(a+b) 
# #a = int(input()) 
# #b= int(input()) 
# #print(a//b) 
# ‘’’ 
# is they are eligible for vote??? 
# inputType: integer 
# output type: if age is greater or equal to 18 
# they are eligible for vote  
# so print “You are Eligible” 
# or else  “sorry you are not eligible” 
# 1tc -  input: 12 
# 2tc – input: 19 

# #if (): 
# #print() 
# #else: 
# #print() 
# #age = int(input()) 
# #if (age >= 18): 
# #print(“You are Eligible”)
# #b= 5 
# #print(a+b) 
# #a = int(input()) 
# #b= int(input()) 
# #print(a//b) 
# '''
# output:
# '''
# is they are eligible for vote??? 
# inputType: integer 
# output type: if age is greater or equal to 18 
# they are eligible for vote  
# so print “You are Eligible” 
# or else  “sorry you are not eligible” 
# 1tc -  input: 12 
# 2tc – input: 19 
# '''
# #if (): 
# #print() 
# #else: 
# #print() 

#age = int(input()) 
#if (age >= 18): 
#print(“You are Eligible”)
# else: 
# print(“sorry you are not eligible”) 
 ''' 
# output:
'''
# wolves 
# grey wolves + black wolves + sheeps  
# input:- gw = 3 ,bw = 5 , sheeps =?   
# Outpu1 : sheeps are four times of wolves . 
# gwe = 5/sheeps  , bwe = 3/sheeps  
# output2 : the no of sheeps remained after haunting?   
# Is wolves doubled??? 
# Output3 : not doubled // yes they are doubled  
# input: gw = 3 
# bw = 5  
# output:  
# total sheeps = 32  
# the no of sheeps remained = 2  
# is they are doubled = not doubled 
# '''
 gw = int(input()) 
bw = int(input()) 
sheeps = (4 * (gw+bw))   
rem_sheeps = sheeps (gw * 5 + bw * 3 ) 
if (rem_sheeps >= 10): 
doubled = “ yes they are doubled “ 
else: 
doubled=”not doubled “ 
print(“total sheeps = “,sheeps) 
print(“the no of sheeps remained = “,rem_sheeps)
print("is they are doubled=doubled")

 # output:



                           DAY2(8-05-25) & 3(9-05-25)
# '''Q1 )  
# input: 100  
# output :- 1h 40m 
# input: 123 
# output:- 2h 3m 
# input:- 12300 
# output :- 205h 0m 
# input :- 12478  
# output:- 
# 5 ,"56" 
# ''  
#minutes = int(input())
 hr = minutes // 60  
#min = minutes % 60 
#print(hr,"h",min,"m") 
#print(str(hr)+"h "+str(min)+"m") 
# ''' 
# Q2.) Sum of n natural numbers  
# input: 10 
# output :- 1+2+3+4+5+6+7+8+9+10 = 55 
# input :- 50  
# output:-  
# ''' 
# # n = int(input()) 
# # sum_n = 0 
# # for i in range(n+1):    
# #sum_n = sum_n + i 
# # print(sum_n) 
# '''sum of even numbers in n natural numbers''' 
# '''input:- 10 
# output:-30 
# input:- 100 
# output:  ''' 
# # n = int(input()) 
# # sum_e = 0  
# # for i in range(n+1):   
# #if ( i % 2 == 0):        
# #sum_e = sum_e + i  
# # print(sum_e) 
# ''' 
# input:- arr = [5,7,8,3,6] 
# output:-  
# s_even = 14 
# s_odd =  15  
# s_all = 29  
# ''' 
# # arr = [9,25,14,6,15,22] 
# # s_e = 0 
# # s_o = 0 
# # s_a = 0 
# # arr = [9,25,14,6,15,22] 
# # for i in arr:       
# #s_a += i 
# #if (i % 2 == 0): 
# #s_e +=  i  
# #else: 
# #s_o += i  
# # print(s_e,s_o,s_a) 
#                            '''09-05-2025''' DAY3

 
# '''STRING SLICING 
# Computer  => Comp''' 
# # word = "computer" 
 
# # print(word[0:4])  
 
# 'Q1.)print first and last values' 
 
# '''input : Room 
#   output : R 
#            m 
#    input : Vizag 
#    output : v  
#            g        
# ''' 
 
# word = "computer" 
# print(word[5]) 
 # print(word[:5]) 
#print(word[5:]) 
 
# word = input() 
# print(word[0]) 
# print(word[-1]) 
# print(word[:-2]) 
#print(word[::2]) 
 
# '''output: 
# Developer 
# D 
# r 
# Develop 
# Dvlpr''' 
 
# '''Q2) first n characters of a word''' 
# '''input: Superman 
#     input: 5 
#     output: super 
     
#     input: impossible 
#     input: 2  
#     output: im 
#     ''' 
# word = input() 
 # n = int(input()) 
 # print(word[:n]) 
 
# '''even index string slicing ''' 
# '''input: Developer 
# output: Dvlpr''' 
# word = input() 
# length = len(word) 
 # even = "" 
# odd ="" 
# for i in range(length): 
#  if i % 2 == 0: 
 #even += word[i] 
 #else: 
 #odd += word[i]    
#print(even , odd) 
# '''AIML and DS''' 
# '''string slicing  
# word = "department 
# 0123456789 
# department 
# ''' 
# # word = input() 
# # print(word[5:]) 
# # print(word[0:8:3]) 
#print(word[::-1]) 
 
# '''q1) input:- India 
# output:-I  
#         a 
#   input:- pakisthan 
#    output: p 
#            n  ''' 
 
# # word = input() 
# # print(word[0]) 
# # print(word[-1]) 
 
# '''input: SuperWomen 
#  input: 5 
#  output: Super 
  
#  input : Impossible 
#  input: 4 
#  output: impo''' 
 
# # word = input() 
# # n = int(input()) 
# # print(word[:n]) 
 
# '''even index and odd index''' 
# '''input : RangeRover 
# output:      
# '''' 
# ''' 
# 0123456789 
# RangeRover 
# even : 
# Rneoe 
# odd: 
# agrvr 
# ''' 
# # word = input() 
# # length = len(word) 
# # even = "" 
# # odd = "" 
# # for i in range(length): 
# #   f ( i % 2 == 0): 
# #even += word[i] 
# #else: 
# #odd += word[i]            
# #if ( i % 2 == 0): 
# #even += word[i] 
# #else: 
# #odd += word[i] 
# # print(even,odd) 
# # print(word[::2]) 
# # print(word[1::2]) 
                     


#                                    DAY4 10-05-25

# ''Q1).Special Eleven  
# Write a program that reads a number N and checks  
# if the remainder is O or 1 when N is divided by 11. 
# Print Special Eleven if the remainder is 0 or 1  
# when N is divided by 11. Otherwise, print Normal Number. 
# input:  n = 22  
# output:  Special Eleven  
# input: n = 23  
# output:  Special Eleven  
# input:15 
# output: Normal number 
# '
# # n = int(input()) 
# # r = n % 11  
# # if r == 0 or r== 1 : 
# #print("Special Eleven") 
# # else: 
# #     print("Normal number") 
 
 
# '''Q2). Write a program that reads two numbers A and B and 
#  prints the Quoitient and remainder when A is divisible  
#  by B 
 
# input: 5  
#        2 
 
# output: 2 
#         1 
 
# input: 30 
#        10 
 
# output: 3 
#         0 
# '' 
 
# # a = int(input()) 
# # b = int(input()) 
# # print(a//b) 
# # print(a%b) 
 
# '''Q3).Write a program that reads a number N  
# and finds the, 
# Remainder when N is divided by 4 
# remainder When N is divided by 5 
# print the greatest remainder among the two remainders  
# when n is divisible by 4 and 5  
# input : 12 
# output : 2  
# input: 147 
# output: 3  
# ''
# # N = int(input()) 
# # remainder_4 = N % 4 
# # remainder_5 = N % 5 
# # greatest_remainder = max(remainder_4, remainder_5) 
# # print(greatest_remainder) 
# '''Q4) Lucky number  
# a two digit number will be given  ,the number is  
# lucky number  
# if it is divided by 9 or it contains a number 9 in it  
# print Lucky  other wise print unlucky  
# input: 18 
# output :Lucky number  
# input : 23 
# output : Unlucky number 
# input: 39 
# output: lucky number
# ''
# #n=int(input("enter 2 digit number")) 
# #if(n%9==0) or ("9" in str(n)): 
# #print("lucky number") 
# #else: 
# #print("unlucky number")        


#                                     DAY5 (11-05-25)
#  '''Q1). Write a program that reads a number N and prints  
# the cube of N numbers from 1 
 
# input: 4  
# output: 1 =>  1 * 1*1 = 1 
#         8 => 2*2*2 
#         27 =>3 *3*3 
#         64 =>4*4*4 
         
# input: 5  
# output:- 1    
#         8 
#         27 
#         64 
#         125                            ''' 
 
# # n =int(input())  
# # for i in range(1,n+1): 
# #     print(i**3) 
# '''using while loop''' 
# # i = 1 
# # while (i< 5): 
# # print(i**3) 
# # i += 1 
# '''Q2). Remove character''' 
# '''given two strings A and B  remove all characters   
# in A that are present in B print the resulting string 
# a = tiger 
# b = ti 
# output: ger 
# '''
# # a = input() 
# # b= input() 
# # r ="" 
# # for i in a: 
# #if i not in b: 
# # r += i  
# # print(r)  
# ''' Q12) 412 in leetcode 
# Given an integer n, return a string array answer (1-indexed) where: 
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5. 
# answer[i] == "Fizz" if i is divisible by 3. 
# answer[i] == "Buzz" if i is divisible by 5. 
# answer[i] == i (as a string) if none of the above conditions are true. 
# Example 1: 
# Input: n = 3 
# Output: ["1","2","Fizz"] 
# Example 2: 
# Input: n = 5 
# Output: ["1","2","Fizz","4","Buzz"] 
# Example 3: 
# Input: n = 15 
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz", 
# "Buzz","11","Fizz","13","14","FizzBuzz"] 
# '' 
# # n=int(input('enter a number: ')) 
# # l = [] 
# # for i in range(1,n+1):             
# # if i%3==0 and i % 5 == 0: 
# #l.append('FizzBuzz') 
# #elif i%3==0:
# #l.append('Fizz') 
# #elif i%5==0: 
# #l.append('Buzz')      
# #else: 
# #l.append(str(i))
# #print(l)


#                                         DAY 6(13-05-25)
#    split() method is used to separate a string into substrings 
# map(function,iterable) => The map() function is used to apply a given 
# function to every item of an iterable 
# ord("") => this method is used to get ascii number for a character 
# chr() => this chr() method is used get the character for that ascii 
# number 
# ''' 
# ''' 
# s = code 
# output :-  
# 99 
# 111 
# 100 
# 101 
# ''' 
# # s = input() 
# # for i in s: 
# #     
# '''
# #print(ord(i)) 
# #get the word by using the given  ascii values  
# #l = 109 111 98 105 108 101 
# output: mobile 
# '' 
# # l = list(map(int,input().split())) 
# # r = "" 
# # for i in l: 
# # r += chr(i)
# #print(r)

#                                DAY 7 (14-05-25)

# '''Q1) given a string s and a number n, write a program  
# to print the count of characters in s whose unicode value 
# is equal to the given number N 
# input: Google    
# 111 
# output: 2  
# 2tc: code-editor 
# : 101 
# output: 2 
# '''  
# # s = input() 
# # n = int(input()) 
# # c = 0 
# # for each in s: 
# #if ord(each) == n:                
# # print(c) 
# #c += 1  
# '''Q2)given string s,write a program to print the  
# character with the smallest unicode value in the  
# string s. 
# input: edit => 101 100 105 116  
# output:  d 
# input: baking => 
# output:  a    =>5 6 8 9 4 2    
# ''' 
# # s = input() 
# # smallest = ord(s[0])   
# # for each in s:   
# # if (ord(each) < smallest): 
# #smallest  = ord(each) 
# # print(chr(smallest)) 
# '''using list ''' 
# # s= input()  
# # l = [] 
# # for each in s: 
# #l.append(ord(each))  
# # print(l)    
# # m = min(l)    
# # print(chr(m))     


#                                    DAY 8 (15-05-25)
# '''Q1) Given  two unicode values M and N , write a program 
#  to print characters with  unicode values from m to n  
#  each on a new line 
  
#  input: m = 65  
#         n = 70  
 
# output: A 
#         B 
#         C 
#         D 
#         E 
#         F 
 
# input:  m = 98  
#         n = 115 
 
# output:  b c d e f g h i j k l m n o p  q r s 
#  ''' 
 
# # m = int(input()) 
# # n = int(input()) 
# # for i in range(m,n+1): 
# # print(chr(i)) 
# '''input reading types 
# s = input()                          
# x = int(input())                       
# => "a"  / "word"  
# => 50 
# l = list(map(int,input().split()))   => [50,10,25,36,85] 
# c = list(map(str,input().split()))=> ["a", "85","ball","5"] 
# ''' 
# # s = input().split() 
# # print(s) 
# # l = list(map(str,input().split())) 
# # print(l) 
# ''' 
# 3 
# 10 
# 20 
# 30 
# ''' 
# # a = int(input()) 
# # for i in range(a): 
# #     b = int(input()) 
 
# '''Q2) given a number N write a program that reads n unicode  
# values and print a string by joining the characters  
# of given n unicode values 
# input: 3  
#         67 
#         97 
#         114 
#   output: Car 
 
# input:5  
#  73 
#  110 
#  100 
#  105 
#  97 
# output:  India 
# '''
# #a = int(input())                                
# #r = ""   
# #for i in range(a): 
# # b = int(input()) 
# # r  +=  chr(b) 
# #print(r) 

#                                      DAY 8(16-05-25)
# Q1) Given a number n, write a program that reads n numbers as input and prints the product of the given n numbers  
# Tc-1 :  input: - 3                                          
#                 2 
#                 3 
#                 7  
# Output:- 42                                       
#    [explanation  2 *3*7  = 42] 
 
# Tc-2:- 4  
# 11  
# 2  
# 4 
# 9 
 
# Output: - 792 
 
# ''' 
# # n = int(input()) 
# # product = 1 
# # for x in range(n):   
# # i = int(input()) 
# #product *= i 
# # print(product) 
#                                      16-05-2025  DAY8
# '''Q1) NEXT Character 
# Given a string , write a program to print the  
# next characters of all characters in s based on the  
# unicode value, each on a new line 
# input: coding 
# d 
# p 
# e 
# j 
# o 
# h 
# input 2:- Unique 
# '''
# # s = input() 
# # for i in s:     
# #u = ord(i) 
# #print(chr(u+1)) 
# '''Unicode value of first Uppercase Letter 
# given a string s, write a program to print the  
# unicode value of the first uppercase character in  
# the string s 
# input:- proGrammeR 
# output: 71 
# input:coDing  
# output: 68''
# # s= input() 
# # for i in s:        
# #print(ord(i)) 
# #if 65<= ord(i)<=90 : 
# #print(ord(i)) 
# #break 
# # s = input() 
# # for i in s:       
# #if i.isupper(): 
# #print(ord(i)) 
# #break 


#                                    DAY 9(17-05-25)

#                                    ''Practice-question :-   
# Q1) .Write a program that reads a distance d in km and 
# calculates  
# the score   
#  If D is less than 10, the score is D.  
#  If D is greater than 10, the score is the sum of 10 and (D-10) 
# * 3   
# Input:- d = 3  
# Output: 3    [bcoz 3 is less than 10]  
# Input : 25   
# Output : 55   
# [ d is greater than 10   
# Value = 10 + (d-10) * 3   
# = 10 + (25-10) * 3  
# = 10 + 15 * 3  
# = 10 + 45      
# = 55   ] ''' 
# # d = int(input()) 
# # if (d < 10):    
# #print(d) 
# # else:     
# #v = 10 + (d-10) * 3 
# # print(v) 
# ''
# Q2).write a program that reads a number X and checks ,  
#  If x is greater than 30   
# Print  
# X is greater than 30  
#  If x is greater than 30, check if x is greater than 50  
# Print   
# X is greater than 30   
# X is greater than 50  
# Input:-  x= 45   
# X is greater than 30   
# Input:- X= 99   
# X is greater than 30   
# X is greater than 50 ''' 
# # x = int(input()) 
# # if (x>30 and x> 50):     
# #print("x is greater than 30 ") 
# #print("X is greater than 50") 
# # elif(x > 30): 
# #print("X is greater than 30")  
#                                                 '''17-05-2025''' 
# '''Q1)Given a strring s, we have uppercase letters and  
# lower case letters 
# print the all lowercase letters as a word  
# input: CowORKER  
# Ouput:-  ow 
# ''
# # s = input() 
# # for i in s:   
# # if i.islower(): 
# #print(i,end ="") 
# '''Q2) Compare First N and Last N characters 
# write a program that reads a string and a number N, 
# checks if the first  
# N characters of the string and the last n characters of  
# the string  are same, or not same  
# input1 : bulb 
# 1  
# output:  True      
# input2: toronto 
# 2  
# output: True  
# input3 : educated 
# 3  
# output: False 
# ''' 
# # s = input() 
# # n = int(input()) 
# # f = s[:n] 
# # l = s[-n:] 
# # if f == l : 
# #print("True") 
# # else: 
# # print("False") 
# '''Q3)'Square root of a number  
# write a program that reads two numbers A and B and  
# checks if the sqrt of A is equal to B  
# input: 64 
# 8  
# output:  "Square root of A is equal to B"  
# input :55 
# 5   
# out put : "Square root of A is not equal to B" 
# ''' 
# # s = int(input()) 
# # t = int(input()) 
# # x = (s ** 0.5 )  
# # if x == t :    
# #print("Square root of A is equal to B") 
# # else:    
# #print("Square root of A is Not equal to B") 
# '''by using sqrt function''' 
# # if v == t:      
# #print("Square root of A is equal to B") 
# # else:  
# #print("Square root of A is Not equal to B") 
# '''
# working 
# 012345679''' 
# s = "working" 
# # print(s[::-1]) 
# '''s[start:end:difference]''' 
         

#                                     DAY 10(21-05-25)


# Q1) write a program that reads the rank  
# R of a student and checks , 
# if R is less than or equal to 3   
# => print one of top 3  
# if R is not less than or equal to 3,check if R is less  
# than or equal to 10 
# => print  Not top 3 but one of top 10  
# input1 :  7  
# output: Not top 3 but one of top 10  
# input2:3 
# output :one of top 3  
# ''' 
# # r = int(input()) 
# # if (r<=3): 
# #print("one of top 3 ") 
# # elif ( r <= 10): 
# # print("not top 3 but one of top 10") 


# Q2)write a program that reads a number N and  
# prints the average of N numbers from 1  
# average of N numbers from 1 can be calculated as, 
# Average = sum of N numbers from 1 / count of nunmbers(n) 
# Input : 4 
# output : 2.5   => (1+2+3+4) /4  = 10/4 = 2.5  
# ''' 
# # n = int(input()) 
# # sum = 0 
# # for i in range(1,n+1): 
# # sum += i 
# # avg = sum / n 
# # print(avg) 
# '''21-05-2025''' 
# '''Q1) Shuffel String 
# Given a string and N indices, where N is the length of the  
# string. write a program to print the string after  
# shuffling the characters in the order of the given  
# N indices. 
# input: goindc 
# 6 
# 5     
# 1     
# 4     
# 2     
# 3     
# 0     
# =>C 
# =>o 
# =>D 
# =>I 
# =>N 
# => G 
# output: coding 
# input2 : eimag 
# 5 
# 1    
# 2     
# 3     
# 4     
# 0      
# => I 
# =>M 
# => A 
# => G 
# => E 
# output: image 
# ''' 
# # s = input() 
# # n = int(input()) 
# # r = "" 
# # for i in range(n):    
# #v = int(input()) 
# #r += s[v] 
# # print(r) 
# '''Q2) sum of even numbers from m to n  
# m = 5 
# n = 13  
# output: 36 
# input2: m = 10  
# n = 20  
# output: 90   
# ''' 
# # m = int(input()) 
# # n = int(input()) 
# # sum = 0 
# # for i in range(m,n+1):        
# #if i %2 ==0: 
# #sum += i 
# # print(sum) 
# '''Q3)Given a string s, write a program to find the  
# vowels in the given string s 
# DAY – 10   21-05-2025 
# print the resultant string by joining all the vowels 
# in the string 
# input:- container 
# output:- oaie 
# input:- queue  
# output:  ueue 
# input:- online 
# output: oie''' 
# # s = input() 
# # r = "" 
# # for i in s:         
# #if i in "aeiouAEIOU":
#     #r+=i
# #print(r)  


#                                        DAY11(26-05-25)
                                       
# '''Q1) count 1's in the binary number 
# input: 0111010101  
# output: 6 
# input: 11101 
# output: 4 
# ''' 
# # 1st method 
# # n = int(input()) 
# # count = 0 
# # for i in str(n): 
# # if i =="1": 
# #count +=1        
# # print(count) 
# # 2nd method 
# # s = input() 
# # v = s.count("1") 
# # print(v) 
# # 3rd method 
# # s = input().split("0") 
# # r = "".join(s) 
# # print(s) 
# # print(r) 
# # print(len(r)) 
 
# '''practice qs ''' 
# '''print "ok!" if n is divided by 4 or  
# else print "AAAA" 
 
# input: 25 
# output:AAAA 
 
# input: 16 
# output:OK!''' 
 
# '''''' 
 
# '''q2)reverse method have to find the qsn logic  
#    input:10 
#    output: 15 
    
#    input:25 
#    otput:37 
    
#    input:50 
#    output:75 ''' 
 
# # n=int(input("enter a no:")) 
# # print(n+(n//2)) 
 
# # '''Q3) input : [72, 101, 108, 108, 111] 
# #        output:  Hello ''' 
 
# # l = list(map(int,input().split())) 
 
# # for each in l: 
# #     print(chr(each),end="") 
 
 
 
#                                              DAY12(29-05-25)
# '''Q1) Given N number of days as input, write a program to  
# convert N number of days to years Y, weeks W and days D 
#  1 year = 365days 
#  week = 7days  
  
  
#  input :- 1329 
#  output :- 3 years    =>3 * 365 = 1095 
#            33 weeks   => 33 * 7 = 231 
#             3 days  =>   3 *1  => 3  
             
# input: 2561 
# output:- '''  
             
# # n = int(input())      
# # y = n//365       
# # w = ((n%365)//7)      
# # d = (n%365)%7      
# # print(y,"years") 
# # print(w,"weeks") 
# # print(d,"days") 
 
# '''Q2) sum of the given digits 
 
# input: 23654889    => 2+3+6+5+4+8+8+9 
# output: 45 
# input: 12345  =>1+2+3+4+5 
# output:15''' 
# # n = int(input()) 
# # m = str(n) 
# # sum = 0 
# # for each in m:   
# #sum += int(each) 
# # print(sum) 
# # n=int(input()) 
# # l=[] 
# # for i in str(n):    
# #l.append(int(i)) 
# # print(l) 
# # print(sum(l)) 
# '''Remove characters''' 
# '''input 1:- "Program" 
# input 2 :- "ogr" 
# output:-"pam" ''' 
# # w = input() 
# # r = input() 
# # result ="" 
# # for each in w:         
# #if each not in r: 
# #result += each 
# # print(result)             

#                               DAY13(30-05-25)  

# '''Q1)input format in multi line 
# f
#  ind the maximum number in the given numbers 
# input: 58 
# input: 6547 
# input: 896 
# output:6547''' 
# # x = int(input()) 
# # y = int(input()) 
# # z = int(input()) 
# # print(max(x,y,z)) 
# ''' 
# Practice qsn 
# greatest of two numbers 
# input : 4 5 
# output: 5' 
# input: 56 999999 
# output:999999''' 
# '''Q2)''check wheather the number  
# is perfect number or not''' 
# '''The sum of factors of the number 
# (excluding itself) is equals to the given  
# number then it is considered as 
# perfect number''' 
# '''testcase-1:- 
# input:-6 
# output:- Perfect number 
# explanation :- 1,2,3 => 1+2+3 = 6 
# testcase-2 
# input2 :- 28 
# output=perfect number  
# explaination:-1+2+4+7+14=28 
# testcase-3 
# input2 :- 36 
# output= not perfect number  
# explaination:-1+2+3+4+6+9+12=37''' 
# # n = int(input()) 
# # fact_sum = 0 
# # for i in range(1,n):        
# #if n % i == 0: 
# #fact_sum += i 
# # if fact_sum == n:  
# #print("perfect number")  
# # else:     
# #print("Not perfect number") 
# '''Q3)check a number is prime or not''' 
# '''prime number :- A number which one and 
# itself as factors''' 
# ''' 
# input:35 
# output:not prime 
# input:11 
# output:prime''' 
# # n = int(input()) 
# # factors_count = 0 
# # for i in range(1,n+1):        
# #if n % i == 0: 
# #factors_count += 1 
# # if factors_count == 2:    
# #print("Prime number") 
# # else:     
# #print("Not a Prime number") 
# '''Q4)return all the digits in the given string''' 
# '''input: a1b234cd56 
# output: 123456 
# input: 5star3roses 
# output :- 53''' 
# ''' 
# =>.isalpha() => only alphabets =>true 
# =>.isdigit()=>only numbers => true 
# =>.isalnum() =>numbers,alphabets,both =>true  
# # s = "a1b234cd56" 
# # v = "abc 1" 
# # print(s.isalnum()) 
# # print(v.isalnum())'''

# # s = input() 
# # result = "" 
# # for i in s:         
# #if i.isdigit(): 
# #result += i 
# # print(result)               


#                                     DAY 14(31-05-25)

#  '''Q1) leetcode -3110 -Score of a string- 
# you are given a string s. 
# The score of a string is defined as the  
# sum of the absolute differece between  
# the ascii values of adjacent characters''' 
# '''input:  hello   => 104  101 108 108 111 
# => |104-101|+|101-108|+|108-108|+|108-111| 
# =>3+7+0+3 => 13 
# output : 13''' 
# ''' 
# 0123456 
# hello 
# ''' 
# # n = input() 
# # s = len(n) 
# # sum = 0 
# # for i in range(s-1):    
# #sum += abs(ord(n[i])-ord(n[i+1])) 
# # print(sum) 
 
#         #      rough   
#         # c1 = n[i]       h  
#         # c2 = n[i+1]      e 
#         # v1 = ord(c1)     104 
#         # v2 = ord(c2)     101 
#         # abs(ord(n[i])-ord(n[i+1])) 
#         # abs(104-101) 
 
# '''Q) Extract only symbols 
# input : abs@123$ 
# output: @$ 
 
# input: h@el#/o 
# output: @#/ 
# ''' 
# # s=input('enter string:') 
# # r = "" 
# # for i in s: 
# #     if not i.isalnum(): 
# #         r += i 
# # print(r) 
 
# '''Q3)you are given N elements your task to  
# determine the number elements divisible by k 
# input format :- first line :- n [no of elements] 
#                 second line : k  => elements would be divide by k 
#                 next n lines: elements  
                 
                 
# input: n= 5 
#        k = 7  
#        1 
#        7 
#        9 
#        14 
#        21 
 
# otput:  3 
#       ''' 
# # n = int(input("enter n:")) 
# # k = int(input("enterk: ")) 
# # c = 0 
# # for i in range(n): 
# #     x = int(input()) 
# #     if x % k == 0: 
# #         c += 1 
# # print(c) 
 

#                                      DAY 15(03-06-25)    
# '''Q1) given a number  
# replace "1" with "0"s and "'0"s with "1"s 
# return the number 
# ''' 
# '''input : 1010 
# output : 0101 
# input: 94123064 
# output: 94023164 
# ''' 
# # n = int(input()) 
# # s = str(n) 
# # result = "" 
# # for i in s:       
# #if i == "1": 
# #result += "0" 
# #elif(i == "0"): 
# #result += "1" 
# #else: 
# #result += i 
# # print(result) 
# '''Q2)chocolate factory and return the  
# empty packets to last''' 
# '''inputs:-  n = arrsize 
# arr = [] 
# output = [x,x,x,x,x,0,0,0] 
# #input ; n = 7              
# arr = [4,5,0,1,0,5,0]      
# out put = [4,5,1,5,0,0,0] 
# input: 5  
# arr = [ 3,0,9,1,7]  
# output:[3,9,1,7,0]      
# ''' 
# # n = int(input()) 
# # arr = list(map(int, input().split())) [:n] 
# # n_li =[] 
# # z_li = [] 
# # for i in arr:         
# #if i == 0: 
# #z_li.append(i) 
# #else: 
# #n_li.append(i) 
# # n_li.extend(z_li) 
# # print(n_li) 
# '''Q3) ATM PIN CODE VALIDATION 
# => exactly 4 or 6 characters 
# => all characters should be digits 
# input:va1b2c 
# output:Invalid Pin code 
# input:234569 
# output: Valid Pin code 
# input: 12456 
# output:Invalid 
# ''' 
# #n = input() 
# #if (len(n) == 4 or len(n) == 6) and n.isdigit():   
#  #    print("Valid PIN")    
#  #else:
#  #    print("Invalid PIN")    
                          
#                                     DAY 16(04-06-25)
#    '''find the sum of prime numbers in the given  
# range''' 
# '''tcs-2025-mar-20 shift-1 -easy  
# asked question 
# input:10 
# output:-17 
# explanation:-2+3+5+7= 17''' 
# ''' 
# 1st method''' 
# # x = int(input()) 
# # sum = 0 
# # for n in range(1,x+1):         
# #factors = 0 
# #for i in range(1,n+1): 
# #if n% i == 0: 
# #factors += 1 
# #if factors == 2: 
# #sum += n 
# # print(sum) 
# '''2nd method''' 
# # def prime_or_not(n):      
# #factors = 0 
# #for i in range(1,n+1): 
# #if  n%i == 0: 
# #factors += 1 
# #if factors == 2 : 
# #return n 
# #return 0 
# # x = int(input()) 
# # sum = 0 
# # for n in range(1,x+1):    
# #s = prime_or_not(n) 
# # sum+=s
# #print(sum)                  

#                                                DAY17(12-06-25)  -PYTHON COMPETITIVE CODING   

# '''CSE''' 
# '''armstrong number''' 
# '''armstrong number means a number  
# which is sum of its own digits  
# length of power equal to given number 
# example = 153 => 1^3 + 3^3+5^3 = 1+27+125= 153 
# example = 1634 => 1^4+ 6^4+3^4+4^4 = 1+1296+81+256 = 1634 
# input format : given a number''' 
# '''input:- 153  
# output: armstrong number 
# input: 1653 
# output: ''' 
# # n = int(input())   
# # s = str(n)          
# # l = len(s) 
# # sum = 0 
# # for i in s:        
# #sum += int(i) ** l 
# # if n == sum:     
# #print("armstromg number") 
# # else:     
# #print("Not a armstrong number") 
# '''TCS NQT Most Repeated Questions For Easy''' 
# '''check a number is palindrome or not''' 
# '''example 
# palindrome:- ex ;-121 ,224422,11211''' 
# '''input: 112111 
# output: Not a palindrome 
# input:123454321 
# output : Palindrome''' 
# # n =int(input()) 
# # s = str(n) 
# # x = s[::-1] 
# # if s == x:     
# #print("palindrome") 
# # else:    
# #print("not a palindrome") 
# # 156  0 
# # s = 156 %10 => 6  x => 156//10 = 15 
# # 15%10 = 5   => 15 // 10 = 1 
# # 1 %10 => 1 => 1//10  => 0 
# # r = r * 10 + s 
# #   = 0 *10 + 6 = > 6 
# #   = 6 * 10 + 5 => 65 
# #   => 65 * 10 + 1  => 651 
# # n = int(input()) #=> 12345 
# # x = n           
# # r = 0           
# # => 12345 
# # => 0 , 5 , 54 , 
# # while ( x != 0): 
# #   s = x % 10     # => 5  => 4  => 3 => 2 => 1 
# #   r = r *10 + s  # => 5   => 54  => 543 => 5432 => 54321
# #   x = x// 10      # => 1234  =>123 => 12=> 1 => 0 
# # if r == n: 
# #   print("Palindrome") 
# # else: 
# #   print("Not a Palindrome") 
# '''find all palindrome number in a given range''' 
# '''input :-1,20 
# output:-10  
# =>"1,2,3,4,5,6,7,8,9,11" 
# input:20,50 
# output:-3 
# =>"22,33,44"''' 
# # a,b = map(int,input().split()) 
# # count = 0 
# # for i in range(a,b+1):                 
# #x = i 
# #r = 0 
# #while(x!= 0): 
# #s = x % 10 
# #r = r* 10+ s 
# #x = x//10 
# #if r == i: 
# #count += 1 
# #print(count)         
                            
#                                           DAY18 (11-06-25)
# # Q1 
# '''find the elements that are even number of 
# t
#  imes repeated''' 
# '''input:-1  1 1 2 2  2 2 2  2 3 3 4 4  4 4 4 ''' 
# '''output:-2 3''' 
# # n = list(map(int, input ().split())) 
# # l = [] 
# # for each in n:             
# #cnt = n.count(each) 
# #if cnt % 2 == 0: 
# #if each not in l: 
# #l.append(each) 
# # print(*l) 
# # n = list(map(int, input ().split())) 
# # s = list(set(n)) 
# # l = [] 
# # for each in s:            
# #cnt = n.count(each) 
# #if cnt % 2 == 0: 
# #if each not in l: 
# #l.append(each) 
# # print(*l) 
# # Q2) 
# ''' first unique element in the list ''' 
# ''' input : 4 7 9 7 2 5 8 4 7 2 8 4 ''' 
# '''output: 9 ''' 
# # n = list(map(int, input ().split())) 
# # for each in n:            
# #cnt = n.count(each) 
# #if cnt ==1: 
# #print(each) 
# #break 
# # Q3) 
# '''first non-repeated char and 
# f
#  irst most repeated char in a string ''' 
# '''input:"abcdededdeegg 
# output:a d 
# explanation :- "a" because a was not repeated 
# and it is the first non-repeated char  
# d because "d" was repeated most no of times 
# ''' 
# # s = input() 
# # l = [] 
# # max = 1 
# # for i in s:         
# #if s.count(i) == 1: 
# #l.append(i) 
# #break 
# # for j in s:  
# #cnt = s.count(j)        
# #if cnt  > max : 
# #max = cnt 
# #val = j 
# # l.append(val) 
# # print(*l)     
# #s.count(a) => 1 > max  => max = 1  
# #s.count(c)=> 1  > max => max = 1  
# #s.count(d) => 4 > max => max = 4 
# #s.count(e)=> 4 > max = > max = 4 
# #s.count(g)=> 2 > max => max = 4                                        