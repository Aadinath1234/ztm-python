"""print("hello world")
print(input("what is your name?"))
name = input("what is your name?: ")
print(name)
print("helloooo  " + name)
"""
# fundamental data types:
    #int
    #float
    #boot
    #str
    #list
    #tuple
    #set
    #dict

# classes -> custom types
     #  supercar (not exits  but we can create it)
# specialized data types:
 
# None
# integers:
'''
print(2+5)
print(2-5)
print(2*5)
print(2/4)
print(type(0.000)) # float
print(type(2+5))
print(type(2-4))

print(type(0))  # int
print(type(20+1.1)) #  float
print(20+1.1)
print(2 ** 3)
print(2 // 4) # 0
print(4 // 4) # 1
print(5% 4) # remainder=1
'''


"""
# math functions:
print(round(3.1)) # ans: 3
print(round(3.9)) # ans: 4 it rounds off
   # abs = absolute value with signs.
print(abs(-20))   # ans: 20

"""

'''
# operator precedence:
print(20 - 3 * 4) # ans: 8
 # order: first is ( ) brackets
 #        second is ** power of
 #       third is * and /
 #       fourth is + and - 

print((20-3) + 2 ** 2)# here first brackets will be solved then ** power of .

# exercise:
print((5+4)*10/2) # 45.0
print(((5+4) * 10)/2)# 45.0
print((5+4)* (10/2))# 45.0
print(5+(4*10)/2)# 25.0
print(5+4*10//2)# 25
'''



"""
# complex numbers : real+ imaginary(i))
print(bin(5)) # ans: 0b101
print(int("0b101", 2)) # ans:base 2 of this no. is :5
"""



'''
# variables are used to store values :
iq = 190
print(iq) # output : 190

# variable should start with lowercase or underscore(letters,underscores)
 # variable is case sensitive
 # don't overwrite keywords.
user_iq = 190 # this variable form is sneak case.
print(user_iq)# output: 190
 #or
_user_iq = 180
print(_user_iq)# output: 180
# user_IQ is differ from user_iq because it is a casesensitive
# repeatation should not happen
# y9u can use reassigning:
iq = 190
user_age= iq/4
print(user_age) # output: 47.5
a = user_age
print(a) # output: 47.5

# constants : value should not change.user_age
PI = 3.14
# a variable should not be with double underscore
a,b,c = 1,2,3
print(a,b,c) # output: 1,2,3



iq = 100
user_age = iq/5 # this iq/5 is a statement or a expression.


# augmented assignment operator:
some_value=5
some_value= 5+2
some_value=some_value + 2
print(some_value) # output: 9
some_value += 2
print(some_value) # 11
some_value -= 2
print(some_value) # 9
some_value *= 2
print(some_value) # 18


# strings:
print(type("hello bro is also a string")) # str.
username = "super coder"
password = 'supersecret'
long_string = """
what yar kya baat boli tune
WOW
0 0
---

             """
print(long_string) # output: what yar kya baat boli tune
print(password)# supersecret
print(username)# supercoder
first_name = "Andrei"
last_name = "Neagonie"
full_name = first_name + "  " + last_name
print(full_name) # Andrei Neagonie.

# string concatenation:
print("hello" + " andrei") # hello andrei
 # string cannot be concatenate with numbers.
print(type(str(100)))  # str , here we have converted 100 to a string.
print(type(int(str(100)))) # int
a = str(100)
b= int(a)
c = type(b)
print(c) # int

# escape sequences:
weather= "it\\'s \"kind of \"  sunny"  # whatever comes after \ is string.
print(weather) # it\'s "kind of " sunny
# \t is used to add a tab:
#\n is used to next line:
dj = "\t It's \"kind of \" sunny \n hope you have a good day!"
print(dj) # output:     It's "kind of" sunny
                # hope you have a good day!
                
'''


'''
# formatted strings:
name = "John"
age = '55'
print("hi" + " " + name +".you are" + " " + age + " year old")# output : hi John. you are 55 year old
print(str(age)) # 55
print(f'hi {name}. You are {age} years old')# output is same as before this is the example of formatted string.hi john. you are 55 years old
print('hi {}. You are {} years old'.format('Jonny', '55')) # output: hi Jonny. You are 55 years old.
print('hi {}. You are {} years old'.format(name, age)) # hi John . You are 55 years old
   # to change the sequence of formatting.
print("hi {1}. You are {0} years old".format(name,age))   # output: hi 55 , you are John years old.
print('hi {new_name}. You are {age} years old'. format(new_name="sally", age=100))# output: hi sally. you are 100 years old.

# string Indexes:
selfish = 'me me me'
        #  01234567
print(selfish[0]) # output: m
print(selfish[7])  # output: e
print(selfish)     # me me me
    # in indexing [start:stop] starting point=start, stop=ending point but it is not counted.
print(selfish[0:4]) # me m  , here ending point 4 is not counted.
print(selfish[0:7])   # me me m
print(selfish[0:8]) # me me me
   #  string indexes has: [start:stop:stepover]
print(selfish[0:8:1])  # me me me
print(selfish[0:8:2])  # m em
print(selfish[1: ]) # e me me
print(selfish[:5]) # me me
print(selfish[::1]) # me me me
print(selfish[-1]) # e from last me
print(selfish[-2])# m from me , second last
print(selfish[-3])#   space ,
print(selfish[::-1]) # em em em , reverse of the string.
print(selfish[::-2]) # e me , in reverse we are skipping by 2

'''
 
#Immutability : string value cannot be changed.
'''
selfish = '01234567'
selfish[0] = 8 # here after assigning the value we cannot change it.
print(selfish)


  # in string value can only changed by completely reassigning value to the variable.
selfish = '8'
print(selfish) # 8
selfish=selfish + '7654321'
print(selfish) # output: 87654321 and selfish='8' does not exits now.

'''

"""
# built-in functions:
print(len("helllooooo")) # 10
  # len calculates the length of string.
greet = 'helllooo'
print(greet[0:])  # helllooo
print(greet[0:len(greet)]) # helllooo
print(greet[0:9]) # helllooo
quote = 'to be or not to be'
print(quote.upper()) # TO BE OR NOT TO BE
print(quote.capitalize()) # To be or not to be
print(quote.lower()) # to be or not to be
print(quote.find('be')) # 3, be starts with index 3.
print(quote.replace("be", 'me')) # to me or not to me.
print(quote )# to be or not to be , strings cannot be it can be done only be reassign the value to then otherwise they unchangeable.


quotee = " to be or not to you"
quotee3 = quotee.replace("be", "ye")
print(quotee3) # to ye or not to ye.
print(quotee) # to be or not to you

"""





  # booleans:
    # it can be true or false.
name= 'Andrei'
is_cool = False
print(bool(1)) # true
print(bool(0)) # false

# type conversion:

name = "aadi"
age = 50
variable= "single"
variable="double"
print(variable)# this will print double

birth_year = input("what year were you born? :  ")
# print(birth_year) # output = what you will give input to it.
age= 2019 - int(birth_year)
print('your age is : {age} ',age) # age = 19

# developer , comments:
   #1. by using # you can comment
   #2. ''' '''
   #3. """"""
   # can place at anywhere.
   # code should be more understandable.


# password checker;
input('jayjay')
input('secret')
#print("password {password} is {passwordlength} long")
print(" {username}, your password {******} is {6} long")

username=input("what is your username?")
password=input("what is your password?")
print(f'{username}, your password,{password},is {len(password)} letters long') # output: yash, your password,6743798,is 7 letters long



username=input("what is your username?")
password=input("what is your password?")

password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password,{hidden_password},is {password_length} letters long')# y, your password,*****,is 5 letters long




#list :
  # inside the list you can have different objects like 1,2,3,4 or letters like a, b, c etc.
  #you can mix this numbers with letters and
   #li is list1
     li =[1,2,3,4,5]
     li2 = ['a', 'b','c']
     li3 = [1,2,'a', True]

     amazon_cart = ['notebooks', 'sunglasses']
     print(amazon_cart[0]) # this will print notebooks
     print(amazon_cart[1]) # this will print sunglasses
     print(amazon_cart[2]) # this will show an error that items are not present in the list.



#list slicing:
    amazon_cart = ['notebooks','sunglasses','toys','grapes']
    print(amazon_cart) # this will print the whole list from notebooks to grapes.
    print(amazon_cart[0:2]) # this will print notebooks and sunglasses
    print(amazon_cart[0::2]) #  this will print notebooks and toys only.
    #list are immutable you cannot assign item to a list
    greet= "hello"
    greet[0] = 'z'
    print(amazon_cart[0::2]) # this will show an error str object does not  support item assignment.
    #
      amazon_cart= ['notebooks','sunglasses','toys','grapes']
      amazon_cart[0] = "laptop"
      print(amazon_cart) # this is showing output laptop,sunglasses, toys,grapes.
      print(amazon_cart[0:3]) # the output will be laptop, sunglasses, toys.
      new_cart = amazon_cart[0:3]
      new_cart[0] = 'gum'
      print(new_cart)# gum , sunglasses, toys
      print(amazon_cart) # laptop , sunglasses, toys, grapes.
      # if
      amazon_cart[0] = 'laptop'
      new_cart = amazon_cart
      new_cart[0] = 'gum'
      print(new_cart) # gum , sunglasses, toys, grapes
      print(amazon_cart) # gum, sunglasses, toys, grapes.
      #
      amazon_cart[0] = 'laptop'
      new_cart = amazon_cart[:]
      new_cart[0] = 'gum'
      print(new_cart) # gum, sunglasses, toys, grapes
      print(amazon_cart) # laptop, sunglasses, toys, grapes.



      # matrix:
       # it is a 2d list or multidimensional list.
        matrix = [[1,5,1],[0,1,0],[1,0,1]]
        print(matrix[0][1])# this will access the element 5 from the first list which is 1,5,1.


        basket = [1,2,3,4,5]
        print(len(basket)) # length of the list is 5.

        #list methods :
           # adding:
               basket = [1,2,3,4,5]
               new_list = basket.append(100)
               print(basket)# [1,2,3,4,5,100]
               print(new_list) # None

               ##
               basket = [1, 2, 3, 4, 5]
               basket.append(100)
               new_list = basket
               print(basket)  # [1,2,3,4,5,100]
               print(new_list)  # [1,2,3,4,5,100]


               # insert method:
                  #insert method have insert(index, object) so
                    basket = [1, 2, 3, 4, 5]
                    basket.insert(4,100) # here you are adding 100 at 4 index no. in the list.
                    new_list = basket
                    print(basket) # the output will be [1,2,3,4,100,5]
                    print(new_list) # the output will be [1,2,3,4,100,5]

                    basket.insert(5,100)
                    new_list = basket
                    print(basket) # the output will be [1,2,3,4,5,100]
                    print(new_list) # the output will be [1,2,3,4,5,100]


                    basket = [1, 2, 3, 4, 5]
                    new_list = basket.insert(4,100) #
                    print(basket) # the output will be [1,2,3,4,100,5]
                    print(new_list) #None




            # extend method :
              # extend method modify the list
                basket = [1, 2, 3, 4, 5]
                new_list = basket.extend([100,101])
                print(basket)# [1, 2, 3, 4, 5,100,101]
                print(new_list) # none


           # removing method:
             #pop():
            basket = [1, 2, 3, 4, 5]
            basket.pop()
            print(basket) # [1, 2, 3, 4]
            basket.pop(0)
            print(basket)# [2, 3, 4]


             #remove:
             basket = [1, 2, 3, 4, 5]
             basket.remove(4)
             print(basket) # [1, 2, 3, 5]


            basket = [1, 2, 3, 4, 5]
            new_list= basket.remove(4)
            print(new_list)  # None

            #but
            new_list = basket.pop(4)
            print(new_list) # this will print 4


            # clear method:
             new_list = basket.clear()
             print(new_list) # NOne

             new_list = basket.clear()
             print(basket)  # [] this show empty list.


             # index method:
             basket = [1,2,3,4,5]
             print(basket.index(2)) # output is 1

             basket = ['a','b','c','d','e']
             print(basket.index('d')) # the output is 3

            basket = ['a', 'b', 'c', 'd', 'e']
            print(basket.index('d', 0,4)) # here 0 is start and 4 is stop point. and the output is 3.
            # here ('d',0,3 is showing error and 'd',0,2 is also showing an error.

            basket = ['a', 'b', 'c', 'd', 'e']
            print('d' in basket) # this will show : True.

            print('x' in basket) # this will show : False.
            print('i' in 'hi my name is Ian') # the output: True.


            basket = ['a', 'b', 'c', 'd', 'e']
            print(basket.count('d')) # here the count show how many times the 'd' is present in the list.

            # Sort method:
              basket = ['a', 'b', 'c', 'd', 'e']
              print(basket.sort()) #none

              basket = ['a', 'b', 'c', 'd', 'e','d']
              basket.sort()
              print(basket) # this will sort the list ['a','b','c','d','d','e']

              basket = ['a', 'b', 'c', 'd', 'e', 'd']
              basket.sort()
              sorted(basket) # ['a','b','c','d','d','e']
              print(basket)# sorted is not a method it is a function.
              print(sorted(basket)) # ['a','b','c','d','d','e']
              #if we comment out the basket.sort the results will be the same .
              print(sorted(basket))
              print(basket) # ['a', 'b', 'c', 'd', 'e', 'd']

              basket =['a','x','b','c','d','e','d']
              new_basket =basket.copy()
              new_basket.sort()
              print(new_basket)# ['a','b','c','d','d','e','x']
              print(basket) #['a','x','b','c','d','e','d']

              # reverse method:
             basket =['a','x','b','c','d','e','d']
             basket.reverse()
             print(basket) # ['d','e','d','c','b','x','a'] here nothing is sorted

             basket =['a','x','b','c','d','e','d']
             basket.sort()
             basket.reverse()
             print(basket) # ['x','e','d','d','c','b','a']
             print(basket[::-1]) # ['a','b','c','d','d','e','x']
             print(basket) #['x','e','d','d','c','b','a']
             print(range(1,100))  # output : range(1,100)
             print(list(range(1,100))) #output: [1,2,3,4,5,.....,99] here 1 is start and 100 is stop.
             print(list(range(100))) # output: [0,1,2,3,4,.....,99]
             print(list(range(101))) # output: [0,1,2,3,4,.....,99,100]
             #join is a string method
              sentence = ' ' # this empty space is a string
              sentence.join(['hi','my','name','is','JOJO'])
              print(sentence)
               ## but if you:
                  sentence = '!'
                  sentence.join(['hi','my','name','is','JOJO'])
                  print(sentence) # output is : !

                  ### and by doing this:
                  sentence = '!'
                  new_sentence= sentence.join(['hi','my','name','is','JOJO'])
                  print(new_sentence) # hi!my!name!is!JOJO

                   sentence = ''
                  new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
                  print(new_sentence)#himynameisJOJO

                      sentence = ' '
                      new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'JOJO'])
                      print(new_sentence)  # hi my name is JOJO

                 new_sentence = " ".join(['hi','my','name','is','JOJO'])
                 print(new_sentence) # hi my name is JOJO


            # list unpacking:
                 #list:
                    basket=[1,2,3]
                     # to print the list items one by one you can do this by taking variables like this.
                     a,b,c = [1,2,3]
                     print(a)
                     print(b)
                     print(c)
                     # the output will be 1
                                          2
                                          3
                                or

                                a,b,c = 1,2,3
                                print(a)
                                print(b)
                                print(c) # this will generate the same output: 1
                                                                               2
                                                                               3

                        #to unpack  the list
                        a,b,c, *other = [1,2,3,4,5,6,7,8,9]
                        print(a)
                        print(b)
                        print(c)
                        print(other) # this will generate the output:
                                       1
                                       2
                                       3
                                       [4,5,6,7,8,9]

                                a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
                                    print(a)
                                    print(b)
                                    print(c)
                                    print(other)
                                    print(d) #  this will generate the output:
                                       1
                                       2
                                       3
                                       [4,5,6,7,8]
                                       9 # here  the d is the last element in the list.



                #NONE:
                  # datatype having no value
                  weapons = None
                  print(weapons)
                  # the output will be None.



                   #Dictionary:
                       # it is a datatype in python and also a datastructure.
                       # dictionary uses the keyword dict.
                       # dictionary having a key and a value.
                       dictionary = {'a':1,'b':2}
                       print(dictionary['b']) # the output will be : 2
                       print(dictionary['c']) # the output will be an error.
                       # dictionary is an unordered key value pair.
                       # the output in dictionary is may be b:2, a:1 because it is unordered.
                       dictionary = {'a':[1,2,3],'b':'hello','x':True}
                       print(dictionary['a'][1]) # this will take the value of a and 1 indexed no. which is 2

                       my_list = [{'a':[1,2,3],'b':'hello','x':True},{'a':[4,5,6],'b':'hello','x':True}]
                       print(my_list[0]['a'][2]) #the output is 3


                        dictionary = {123:[1,2,3], 'greeting':'hello','is_Magic':True,True:'hello',[100]:True}
                        print(dictionary[123]) # output: [1,2,3]
                        print(dictionary[True]) # output: hello
                        print(dictionary[100]) # output is : unhashable type list.list keyvalue can be changed.
                        # key should be immutable means the value of key should not change.

                        dictionary = {'123':[1,2,3],'123':'hello'}
                        print(dictionary['123']) # output is : hello

                         dictionary = {'basket':[1,2,3],'greet':'hello'}
                         print(dictionary['basket']) # output: [1,2,3]

                     user = {'basket': [1, 2, 3], 'greet': 'hello'}
                     print(user['age']) # this is showing an keyerror
                     #get is a python method.
                     user = {'basket': [1, 2, 3], 'greet': 'hello'}
                     print(user.get('age')) # the output is none.
                     print(user.get('age', 55)) # the output is 55



                     user = {'basket': [1, 2, 3], 'greet': 'hello', 'age':20}
                     print(user.get('age', 55)) # the output is 20 but if no value of age is present then we get the age as 55

                     user2 = dict(name='JohnJohn')
                     print(user2) # output: {'name':'JohnJohn'}

                    user = {'basket': [1, 2, 3], 'greet': 'hello', 'age':20}
                    print('basket' in user) #  output: True.
                    print('size' in user) # False

                       # keys method is used to find the key is present inside the dictionary or not.

                      user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                      print('age' in user.keys()) # output: True.
                      print('hello' in user.values()) # output: True.
                      print(user.items()) # this will grab the whole dictionary like: dict_items([ ('basket': [1, 2, 3]), ('greet': 'hello'), ('age': 20)])
                      print(user.clear()) # this will clears the whole dictionary.


                     user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                     user.clear()
                     print(user) # this will also empty the dictionary  but it is showing: {}


                    user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                    user2 = user.copy()
                    print(user) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                    print(user2) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}


                    user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                    user2 = user.copy()
                    print(user.clear()) # output is : None
                    print(user2) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}



                   user = {'basket': [1, 2, 3], 'greet': 'hello', 'age': 20}
                   print(user.pop('age')) # output: 20 # pop returns the value whatever got removed.
                   print(user) # {'basket': [1, 2, 3], 'greet': 'hello'}

                   print(user.popitem()) # this will remove the item  randomly from the dictionary.here the output is ('age', 20)
                   print(user) #  {'basket': [1, 2, 3], 'greet': 'hello'}

                   print(user.update({'age':55})) # None
                   print(user) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55}
                   print(user.update({'ages':55})) # None
                   print(user) # {'basket': [1, 2, 3], 'greet': 'hello', 'age': 55,'ages':55}



                 # Tuples:
                   # we cannot modify tuples it is immutable. they are immutable list.
                    my_tuple = (1,2,3,4,5)
                    my_tuple[1] = 'z'
                     # the output is  : tuple object does not support item assignment.
                     # but you can access it by printing it.
                    print(my_tuple[1]) # output: 2
                    print(5 in my_tuple) # output: True.

                    user = {(1,2):[1,2,3],'greet':'hello', 'age':20}
                    print(user[(1,2)]) # output: [1,2,3]

                       # keys in a dictionary is behave like tuple.
                         my_tuple = (1,2,3,4,5)
                         new_tuple = my_tuple[1:2]
                         print(new_tuple) # output: (2,)
                         new_tuple = my_tuple[1:4]
                         print(new_tuple) # output: (2,3,4)
                           # you can assign like list  to the tuple
                            my_tuple = (1,2,3,4,5)
                            x = my_tuple[0]
                            y = my_tuple[1]
                            print(x) # output: 1
                            print(y) # output: 2




                            x,y,z, *other = (1,2,3,4,5)
                            print(x) # output: 1
                            print(z) # output: 3
                            print(other) # output: [4,5]


                          my_tuple = (1,2,3,4,5,)
                          print(my_tuple.count(5)) # output: 1
                          my_tuple = (1,2,3,4,5,5)
                          print(my_tuple.count(5)) # output: 2

                          print(my_tuple.index(5)) # 4
                          print(len(my_tuple)) # 6



             # Set:
             my_set = {1,2,3,4,5,5}
             print(my_set) # output: {1,2,3,4,5} # in the sets there is no duplicacy only uniqueness.


             my_set = {1,2,3,4,5,5}
             my_set.add(100)
             my_set.add(2) # the output is {1,2,3,4,5,100} here the add(2) is not added to the set because there 2 is already present.
             print(my_set)

             # when you have to take only unique items from the list you can convert it to the set the you will get unique items.
             my_list = [1,2,3,4,5,5]
             print(set(my_list)) # output: {1,2,3,4,5}

             # set objects does not support indexing
             my_set = {1,2,3,4,5,5}
             print(my_set[0]) # showing an error.
             print(1 in my_set) # output: True.
             print(len(my_set)) # output: 5
             print(list(my_set)) # output: [1,2,3,4,5]
             new_set = my_set.copy()
             my_set.clear()
             print(new_set) # output: {1,2,3,4,5}
             print(my_set) # output: set() , means empty.


            my_set = {1,2,3,4,5}
            your_set = {4,5,6,7,8,9,10}
            print(my_set.difference(your_set)) # output: {1,2,3}
            print(my_set) # output: {1,2,3,4,5}
            print(my_set.discard(5)) # output: None
            print(my_set) # output: {1,2,3,4}
            print(my_set.difference_update(your_set)) # output: None
            print(my_set) # output: {1,2,3}
            print(my_set.intersection(your_set)) # output: {4,5}
            print(my_set & your_set) # output: {4,5}
            print(my_set.isdisjoint(your_set)) # output: False

            my_set = {1, 2, 3}
            your_set = {4,5,6,7,8,9,10}
            print(my_set.isdisjoint(your_set)) # output: True. # isdisjoint is means nothing is common between the two sets.
            print(my_set.union(your_set)) # output: {1,2,3,4,5,6,7,8,9,10} #joins two sets but remove duplicacy.
            print(my_set | your_set) #  output: {1,2,3,4,5,6,7,8,9,10}


            my_set = {4,5}
            your_set = {4,5,6,7,8,9,10}
            print(my_set.issubset(your_set)) # output: True.
            print(my_set.issuperset(your_set)) # output: False.
            print(your_set.issuperset(my_set)) # output: True.




            # conditional logic:
              is_old = True
              is_licenced = True

              if is_old:
                  print('you are old enough to drive!') #output: you are old enough to drive!
              print('checheck') # checheck




              is_old = false
              is_licenced = True
              if is_old:
                  print('you are old enough to drive!') # output: nothig , here it only print checheck.
              print('checheck') # output : checheck




            is_old = false
            is_licenced = True
            if is_old:
                  print('you are old enough to drive!') # this will not get printed because is_old is a false condition.
            else:
                print('checheck') # output: checheck



            is_old = True
            is_licenced = True
            if is_old:
                  print('you are old enough to drive!') # output: you are old enough to drive!
            else:
                   print('checheck')  # output: this will not get executed because is_old is true so if get executed and else will not.



            is_old = True
            is_licenced = True
            if is_old:
                  print('you are old enough to drive!') # output: you are old enough to drive!
            elif is_licenced:
                print('you can  drive now!') # this will not get executed
            else:
                print('you are not of age!') # this will also not get executed.
            print('okoko') # output: okoko





           is_old = False
           is_licenced = True
           if is_old:
               print('you are old enough to drive!')  # output: this will not execute
           elif is_licenced:
               print('you can  drive now!')  # you can drive now!
           else:
                print('you are not of age!')  # this will also not get executed.
           print('okoko') # output: okoko





          is_old = False
          is_licenced = False
          if is_old:
              print('you are old enough to drive!')  # output: this will not execute
          elif is_licenced:
             print('you can  drive now!')  # this will not execute
          else:
             print('you are not of age!')  # you are not of age!
          print('okoko')  # output: okoko


          is_old = False
          is_licenced = False
          if is_old and is_licenced:
              print('you are old enough to drive! and you have a licence!')  # output: this will not execute

          else:
             print('you are not of age!')  # you are not of age!
          print('okoko')  # output: okoko




            is_old = True
            is_licenced = False
            if is_old and is_licenced:
                print('you are old enough to drive! and you have a licence!')  # output: this will not execute

           else:
             print('you are not of age!')  # you are not of age!
           print('okoko')  # output: okoko




            is_old = True
            is_licenced = True
            if is_old and is_licenced:
                print('you are old enough to drive! and you have a licence!')  # output: you are old enough to drive, and you have a licence!

           else:
             print('you are not of age!')  # this will not get executed.
           print('okoko')  # output: okoko
           # in python we can have multiple elif with if and else conditional statement.





            is_old = True
            is_licenced = True
            if is_old and is_licenced:
                print('you are old enough to drive! and you have a licence!')  # output: you are old enough to drive, and you have a licence!

           else:
             print('you are not of age!')  # this will not get executed.
             print('okoko')  # this will not get executed.
           # in python indentation matters so indentation may change the output of the code.






         is_old = True
         is_licenced = False
         if is_old and is_licenced:
                 print(' you are old enough to drive! and you have a licence!')  # output: this will not get executed.

         else:
             print('you are not of age!')  # you are not of age!
             print('okoko')  # okoko




        # Truthy and Falsey:

is_old = 'hello'
is_licenced = 5
if is_old and is_licenced:
    print(' you are old enough to drive! and you have a licence!')  # output: you are old enough to drive! and you have a licence!

else:
    print('you are not of age!')  #not executed
    print('okoko')  # not executed







is_old = bool('hello')
is_licenced = bool(5)
     ##truthy value
print(bool('hello')) #output: True
print(bool(5)) #output: True

if is_old and is_licenced:
    print(' you are old enough to drive! and you have a licence!')  # output: you are old enough to drive! and you have a licence!

else:
    print('you are not of age!')  # not executed
    print('okoko')  # not executed









is_old = bool('')
is_licenced = bool(0)
    ## Falsey value.
print(bool('')) #output: False
print(bool(0)) #output: False

if is_old and is_licenced:
    print(' you are old enough to drive! and you have a licence!')  # output: you are old enough to drive! and you have a licence!

else:
    print('you are not of age!')  # not executed
    print('okoko')  # not executed








password = '123'
username = 'johnny' # this will evaluate automatically in the boolean form it is truthy or falsey.
if password and username:
    print('you are old enough to drive, and you have a licence!')
else:
    print('you are not of age!')
    print('okoko')





# Ternary operator:

  # condition_if_true if condition else condition_if_false
  is_friend = True
  can_message = "message allowed" if is_friend else "not allowed to message"
  print(can_message)  # output: message allowed

is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)  # output: not allowed to  message



# short circuiting:

is_Friend = True
is_User = True
print(is_Friend and is_User) #output: True



is_Friend = True
is_User = True
if is_Friend and is_User:
    print('best friends forever') # output: best friends forever

is_Friend = True
is_User = True
if is_Friend or is_User:
    print('best friends forever')  # output: best friends forever

    # in the short circuiting in if condition you are using and , or , interpreter checks first condition is true then it doesn't care next condition and execute the program this is the concept of short circuiting.














#Logical operators:
     #logical operators: > , < , == , and ,or, not, >= ,<= , !=
     print(4<5) #output: True.
     print(4 == 5) # output: False
     print(4 = 5) # output: error because = we use to assign value to variable for comparison we use == inplace of = .
     print('hello' == 'hello') # True
     print('a' > 'b') # output: False, try this on google
     print('a' > 'A') # output: True .try this on google
     print(1 < 2 < 3 < 4) # output: True
     print(1 < 2 > 3 < 4) # output: False
     print(1 <= 0) # output: False
    print(1 >= 0) # output: True
    print(0 <= 0) # output: True
    print(0 != 0) # output: False
    print(0 != 1) # output: True
    print(not(True)) # output: False
    print(not(False)) # output: True
    print(not(1 == 1 )) # output: False
     # exercising logical operators:
         is_magician = False
         is_expert = True

         #Q.1 : check if magician AND expert :"you are a master magician"
         if is_expert and is_magician:
             print("you are a master magician") # not executed
         #Q.2 : check if magician but not expert: "at least you're getting there"
         elif is_magician and not is_expert:
             print("at least you're getting there") # not executed
         #Q.3 : if you're not a magician : "YOu need magic powers"
         elif not is_magician:
             print("YOu need magic powers") # output: YOu need magic powers.








is_magician = True
is_expert = True
# Q.1 : check if magician AND expert :"you are a master magician"
if is_expert and is_magician:
    print("you are a master magician")  #you are a master magician
# Q.2 : check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")  # not executed
# Q.3 : if you're not a magician : "YOu need magic powers"
elif not is_magician:
    print("YOu need magic powers")  # output:  not executed






is_magician = True
is_expert = False
# Q.1 : check if magician AND expert :"you are a master magician"
if is_expert and is_magician:
    print("you are a master magician")  # not executed
# Q.2 : check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")  # at least you're getting there
# Q.3 : if you're not a magician : "YOu need magic powers"
elif not is_magician:
    print("YOu need magic powers")  # output:  not executed



# is vs == :
   print(True == 1) # output: True
   print('' == 1) # output: False, empty string evaluates to the falsey so falsey cannot be equal to 1
   print([] == 1) # output: False, empty array evaluates to falsey so this falsey is not equal to 1.
   print(10 == 10.0) # output: True
   print([] == []) # output: True
   print([1,2,3] == [1,2,3]) #output: True.
   print('1' == 1) # output: false



print(True is 1)  # output: False
print('1' is 1)  # output: False
print([] is  1)  # output: False
print(10 is 10.0)  # output:False
print([1,2,3] is  [1,2,3]) # output: False



print(True is True)  # output:True
print('1' is '1')  # output: True
print([] is  [])  # output: False, list are whenever get created is stored at another locations not at the same places
print(10 is 10)  # output:True , because this items are stored at the same memory locations.
print([1,2,3] is  [1,2,3]) # output: False, but with the list the list are stored at the different memory locations.
a =[1,2,3]
b =[1,2,3]
print(a == b) # True
print(a is b) # False.




# LOOPS:
  # for loop:
     for item in 'zero to mastery':
         print(item)
# output:

z
e
r
o

t
o

m
a
s
t
e
r
y



for item in [1,2,3,4,5]:
    print(item) #
#output:
1
2
3
4
5



for item in {1,2,3,4,5}:
    print(item) #
#output:
1
2
3
4
5




for item in (1,2,3,4,5):
    print(item) #
#output:
1
2
3
4
5

# for loop is used to iterate over a collection of items.

for item in [1,2,3,4,5]:
    print(item)
    print(item)
    print(item)
#output:
1
1
1
2
2
2
3
3
3
4
4
4
5
5
5


for item in [1,2,3,4,5]:
    print(item)
    print(item)
    print(item)
print('hi!')
#output:
1
1
1
2
2
2
3
3
3
4
4
4
5
5
5
'hi!'



for item in [1,2,3,4,5]:
    print(item)
    print(item)
    print(item)
print(item)
#output:
1
1
1
2
2
2
3
3
3
4
4
4
5
5
5
5




for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item, x)

#output:
1 a
1 b
1 c
2 a
2 b
2 c
3 a
3 b
3 c
4 a
4 b
4 c
5 a
5 b
5 c

# ITERABLE: iterable is the object that can be iterated.
   # list, dictionary, tuple, set , string can iterable.
      # iterate -> one by one check each item in the  collection.
       user = {
           'name': 'Golem',
           'age':5006,
           'can_swim': False

       }
       for item in user:
           print(item)
#output:
name
age
can_swim # by this way you can print the keys of the Dictionary.







user = {
           'name': 'Golem',
           'age':5006,
           'can_swim': False

       }
       for item in user.items():
           print(item) #output: #('name', 'Golem')
                                #('age', 5006)
                                #('can_swim', False)
       for item in user.values():
           print(item)#output: #Golem
                               #5006
                               #False
       for item in user.keys():
           print(item) # name
                        #age
                        #can_swim
       for item in user.items():
           key, value = item;
           print(key, value) #name Golem
                             #age 5006
                             #can_swim False
       for key, value in user.items():
           print(key, value) # output:#name Golem
                                      #age 5006
                                      #can_swim False
       for k,v in user.items():
           print(k,v )# output:#name Golem
                               #age 5006
                               #can_swim False
       for a,b in user.items():
           print(a,b) ## output:#name Golem
                               #age 5006
                               #can_swim False
       for item in 50:
           print(item) # error , int object is not iterable , because int object is not a collection of items.






       # exercise : Tricky Counter.
         # counter:
         my_list = [1,2,3,4,5,6,7,8,9,10]
         counter = 0
         for item in my_list:
             counter = counter + item
         print(counter) # output: 55




my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for item in my_list:
    counter = counter + item
    print(counter)
#output:1
3
6
10
15
21
28
36
45
55



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in my_list:
    counter = 0
    counter = counter + item
    print(counter) #output: 10




# range():
   # range is the object that produces a sequence of integers from start to stop .
      # range object is looks like tuple but it is not tuple it is a special type of object.
      print(range(100)) #output: range(0,100)
      print(range(0,100)) # output: range(0,100)


      for number in range(0,100):
          print(number)
#output:0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99


for number in range(0, 10):
    print('email email list')
#output:email email list
email email list
email email list
email email list
email email list
email email list
email email list
email email list
email email list
email email list



for _ in range(0, 10)
    print(_)
#output:0
1
2
3
4
5
6
7
8
9


for _ in range(0,10,2 ) # here 2 is steps
    print(_)
#output:0
2
4
6
8


for _ in range(0,10,-1 ) # here 2 is steps
    print(_) #output: nothing.

for _ in range(10,0,-1 ) # here 2 is steps
    print(_)
#output:10
9
8
7
6
5
4
3
2
1

for _ in range(10,0)
    print(_) # output: nothing.

for _ in range(10,0,-2)
    print(_)
# output: 10
# 8
# 6
# 4
# 2.

for _ in range(10,0,-2)
    print(list(range(10)))
#output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for _ in range(2):
    print(list(range(10)))
#output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]






# enumerate() object:
     for i, char in enumerate('Helllooo'):
         print(i, char) # in the enumerate we are getting index of every item which is printing.
#output:
0 H
1 e
2 l
3 l
4 l
5 o
6 o
7 o

for i, char in enumerate([1,2,3]):
    print(i, char) # this is list.
#output:
0 1
1 2
2 3
# here 0,1,2 is the index no. of 1,2,3



for i, char in enumerate((1,2,3)):
    print(i, char) # this is tuple
#output:
0 1
1 2
2 3


for i, char in enumerate(list(range(100))):
   if char == 50:
       print(f'index of 50 is: {i}')
       # output: index of 50 is : 50


for i, char in enumerate(list(range(100))):
   print(i,char)
   if char == 50:
       print(f'index of 50 is: {i}')
#output:
0 1
1 2
2 3
0 0
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
11 11
12 12
13 13
14 14
15 15
16 16
17 17
18 18
19 19
20 20
21 21
22 22
23 23
24 24
25 25
26 26
27 27
28 28
29 29
30 30
31 31
32 32
33 33
34 34
35 35
36 36
37 37
38 38
39 39
40 40
41 41
42 42
43 43
44 44
45 45
46 46
47 47
48 48
49 49
50 50
index of 50 is: 50
51 51
52 52
53 53
54 54
55 55
56 56
57 57
58 58
59 59
60 60
61 61
62 62
63 63
64 64
65 65
66 66
67 67
68 68
69 69
70 70
71 71
72 72
73 73
74 74
75 75
76 76
77 77
78 78
79 79
80 80
81 81
82 82
83 83
84 84
85 85
86 86
87 87
88 88
89 89
90 90
91 91
92 92
93 93
94 94
95 95
96 96
97 97
98 98
99 99


# while loops:
  # while condition:
  i = 0
  while i < 50:
      print(i) #here the value 0 prints infinite times.this is creating a infinite loop

i = 0
while i < 50:
    print(i)
    break # output: 0



i = 0
while i < 50:
    print(i)
    i += 1 # i = i + 1
# output:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49


i = 0
while i < 50:
    print(i)
    i += 1
print('done with all the work')
# output:
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
done with all the work.




i = 0
while i < 50:
    print(i)
    i += 1
    break # output: 0
else:
  print('done with all the work') # the else statement is not get executed.



my_list = [1,2,3]
for item in my_list:
    print(item) # output: 1
                          2
                          3


i = 0
while i < len(my_list)
    print(my_list[i])
    i += 1
    #output:
     1
     2
     3

while True:
    input('say something: ')
    break #  output: say something: hi!

while True:
    input('say something:  ') #output: say something : hi
                                       say something: hi
                                       say something : hi
                                     #this output comes again and again.infinite loop


while True:
    response = input('say something:  ')
    if(response == 'bye'):
        break # output: say something: hi
                        say something: hi
                        say something: hi
                        say something: bye # here execution stops.

# break
  # break works in for loop also.
  my_list = [1,2,3]
  for item in my_list:
      print(item)
      break # when we use break statement we are coming out of the  current loop

my_list = [1, 2, 3]
for item in my_list:
    print(item)
    continue # continue break the loop and send back again to the its initial point to execute again.




my_list = [1, 2, 3]
for item in my_list:
    continue
    print(item) # output: nothing




i = 0
while i < len(my_list):
    i += 1
    continue
    print(my_list[i]) # output: nothing

    # pass doesn't do anything in the code.

    my_list = [1, 2, 3]
    for item in my_list:
        pass
        print(item) #output:
        1
        2
        3

    i = 0
    while i < len(my_list):
        print(my_list[i])
        i +=1
        pass # output:
        1
        2
        3





my_list = [1, 2, 3]
    for item in my_list:
        #still thinking what to do next in the code.
    pass # here the error is just not printed because of the pass statement.
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass # output:
    1
    2
    3


# out first gui:
picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
for row in picture:
     for pixel in row:
         if(pixel == 1):
             print('*' , end = '')
         else:
             print(' ', end='')
     print('')
#output:
   *
  ***
 *****
*******
   *
   *


   # developer fundamentals:
       # clean : code should be neat and clean
       #Readability : code should be read by other persons also
       # predictability:
       #DRY: Do not repeat your code.code should be short and easy to read.

fill = '$'
empty = ''
for row in picture:
    for pixel in row:
        if(pixel):
            print(fill, end='')
            print(fill , end='')
            print(fill, end='')
        else:
            print(empty, end='')
            print(empty, end='')
    print('')
#output:
$$$
$$$$$$$$$
$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$
$$$
$$$


# exercise : find duplicates in list.
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates) # output: ['b', 'n']


#Functions:
 def say_hello():
     print('hellllooooo') # output: nothing will be in the output.
 say_hello()  # this will print the hellllooooo in the output.
 # if you say_hello without the brackets then nothing will be in the output.


picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
def show_tree():
 for row in picture:
     for pixel in row:
         if(pixel):
             print('*' , end = '')
         else:
             print(' ', end='')
     print('')
show_tree()
show_tree()
show_tree()
#output:
*
  ***
 *****
*******
   *
   *
   *
  ***
 *****
*******
   *
   *
   *
  ***
 *****
*******
   *
   *

# if you put show_tree() function before defining it then error shown that name show_tree is not  defined.
# if you just print show_tree without the brackets then it will show you the memory location where the function is stored.
  # like print(show_tree) # output:<function show_tree at 0x000001BA46F7C1E0 >

# Arguments v/s parameters:
   # parameters : when we define the function
   def say_hello(name, emoji):
       print(f'hellllooooo {name} {emoji}') # here the name and emoji is parameters.
   # arguments:  when we call the function
     say_hello('Andrei','symbol of emoji') # here the andrei and symbol of emoji is arguments where we are calling it.
      # here the output: hellllloooo Andrei symbol of emoji.
     say_hello('Dan', 'symbol of emoji')# output: helllooo Dan symbol of emoji
     say_hello('Emily', 'symbol of emoji')#output: hellllooo Emily symbol of emoji.
     # you should take name first in the arguments if it is defined in the parameters in the first place , we should follow the sequence of parameters in the arguments.
       ## this following of the sequence is in the #positional arguments.
    # keyword arguments:
       # in the keyword arguments you do not need to follow the sequence  ,you can pass arguments in any place.
        say_hello(emoji = 'smily symbol', name ='Bibi') # output: hellloooo Bibi smily symbol

    # default parameters:
def say_hello(name='Darth Vader', emoji='devil symbol '):
    print(f'hellllooooo {name} {emoji}')


say_hello('Andrei', 'symbol of emoji') #output: hellllloooo Andrei symbol of emoji.
say_hello('Dan', 'symbol of emoji')  #output: helllooo Dan symbol of emoji
say_hello('Emily', 'symbol of emoji')#output: hellllooo Emily symbol of emoji.
say_hello()#output: helllooo Darth Vader devil symbol.
# here in the function you haven't pass the arguments so it is taking the default parameters as an argument.
# if you pass arguments then it take that arguments in the output of the function.
say_hello('Timmy')#output: hellllo Timmy devil symbol, here the devil symbol is take as default and the timmy we have passed so it is taken in the output.



#Return:
def sum(num1, num2):
    num1 + num2

sum(4,5)# in the output: nothing is printed.




def sum(num1, num2):
    num1 + num2

print(sum(4, 5)) #output: None




def sum(num1, num2):
   return num1 + num2

print(sum(4, 5)) #output: 9
print(sum(10,5))#output: 15





def sum(num1, num2):
    print('hiiii') #output: hiiii
    num1 + num2
print(sum(10, 5))# output: None





def sum(num1, num2):
   return num1 + num2

total = sum(10, 5)
print(sum(10,total)) # output: 25





def sum(num1, num2):
   return num1 + num2

print(sum(10,sum(10,5)))# output: 25






def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2

total = sum(10, 20)
print(total) # output: None







def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func

total = sum(10, 20)
print(total) # output : <function sum.<locals>.another_func at 0x7fd9c8dfa0d0>




def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func

total = sum(10, 20)
print(total(10,20)) # output: 30



def sum(num1, num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)

total = sum(10, 20)
print(total) #output: 30






def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10, 20)
print(total) #output: 30







def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
    return 5
    print('hello') # here in the output: return 5 is not executed not the print statement get executed
                      # only return another_func(num1, num2) get executed and exit the function
                         # while in the return n1 + n2 function not exit because here only we are defining values.
                               # but in the return another_func(num1, num2) we are executing the code so here the function got exited.


total = sum(10, 20)
print(total)







# Methods  v/s  Functions:
  #methods are used after . like 'elephant'.capitalize() here the capitalize() is the method of the string , if you only writes capitalize() like function it will give you an error.
  # in the function you will first define it  then you just call the function.
    def some_random_stuff():
        pass

    some_random_stuff()
     # this happens in the function.

     # methods are  built in objects.



#Docstrings:
   # Docstrings tells us about the function which we have commented inside the function  like:
     def test(a):
         '''

         Info: this function tests and prints param a
         '''
         print(a)

     test('!!!!!')
     test() # here when we are calling the function then , which we have commented inside the function that will be automatically shown to us.
            # when you come to test() then you can see the Info: this function tests and prints param a.
     help(test) # output: test(a)
                         #Info: this function tests and prints param a .
     print(test.__doc__) # output: Info: this function tests and prints param a.



# clean code: it stands for , to how we can short the code with same output.
  def is_even(num):
      if num % 2 == 0:
          return True
      elif num % 2 != 0:
          return False
  print(is_even(50)) # output: True
  print(is_even(51)) # output: False




def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(50))  # output: True
print(is_even(51)) # output: False






def is_even(num):
    if num % 2 == 0:
        return True
    return False # code execute this line only when the if statement is not satisfied .


print(is_even(50))  # output: True
print(is_even(51)) # output: False






def is_even(num):
    return num % 2 == 0

print(is_even(50))# output: True
print(is_even(51))# output: False





# *args  **kwargs :
  def super_func(*args):
      return sum(args) # *args is a parameter here not the argument, inside the function.

  super_func(1,2,3,4,5) # output: error , because here in sum(args) we are printing only one value but in super_func we have given 5 values.



def super_func(*args):
    print(*args)
    return sum(args)  # *args is a parameter here not the argument, inside the function.


super_func(1, 2, 3, 4, 5)  # output: 1,2,3,4,5






def super_func(*args):
    print(args)
    return sum(args)  # *args is a parameter here not the argument, inside the function.


super_func(1, 2, 3, 4, 5)  # output:( 1,2,3,4,5) we getting a tuple
print(super_func(1,2,3,4,5))#output: 15






def super_func(*args, **kwargs):
    print(kwargs)# **kwargs: keyword argument, # output: {'num1':5, 'num2':10} # this is a dictionary which  have key and value.
    return sum(args)

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10)) # output: 15








def super_func(*args, **kwargs):
   total = 0
   for items in kwargs.values():
       total += items
    return sum(args) + total

print(super_func(1,2,3,4,5, num1 = 5, num2 = 10)) # output: 30
# rules: which would should  come first.
 1.params, 2.*args,3.default parameters, 4. **kwargs # this is the sequence.
 # so in the function it would be like this:
     def super_func(name, *args, i='hi', **kwargs):
         print(super_func('Andy',1,2,3,4,5, num1=5, num2=10)) # here we do not need to pass the default parameter at the place of arguments.





# exercise functions:
   def highest_even(li):
       evens = []
       for item in li:
           if item % 2 == 0:
               evens.append(item)
       return max(evens)# indentation should be taken care, right way of writing return.
   print(highest_even([10,2,3,4,8,11])) # output: 10



def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
        return max(evens)  # indentation should be taken care


print(highest_even([2,10, 2, 3, 4, 8, 11])) # here the output is 2





# Scope:
  #Scope stands for what variables do i have access to
    # global scope.
      # function scope:
        if True:
            x = 10

        def some_func():
            total = 100

        print(x) # output: 10 because it is in the global scope.
        print(total) # output: if you are trying to print total you will get an error because it is in the local scope not in global scope so you cannot access it.


# Scope rules:
   a = 1

   def confusion():
       a = 5
       return a

   print(a) # output: 1
   print(confusion())#output: 5






a = 1

def confusion():
    a = 5
    return a


print(confusion())  # output: 5
print(a)  # output: 1



#1- rules of the scopes :first it  start with local scope
#2- if local scope is not present then go to parent local scope to be get executed.

a = 1


def parent():
    a = 10
    def confusion():
        return a
    return confusion()



print(parent())  # output: 10
print(a)  # output: 1
# 3 : when the local and parent local scope is not present then the global scope will get executed.

a = 1


def parent():
    def confusion():
        return a

    return confusion()


print(parent())  # output: 1
print(a) # output: 1


#4:  at last built in  python functions will get executed:


a = 1


def parent():
    def confusion():
        return sum

    return confusion()


print(parent())  # output: <built-in function sum> first it check sum in local then in parent local then in global but when it not found in that scopes then it will print the sum is built-in function.
print(a) # output: 1






# global keyword:
  a = 10
  def confusion(b):
      print(b)
      a = 90

  confusion(300) #output: 300




  #
  total = 0

  def count():
      total = 0
      total += 1
      return total

  count()
  count()
  print(count()) # 1



  #
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())# output: 3




 total = 0

 def count(total):
     total += 1
     return total

 print(count(count(count(total)))) #output: 3




# Non local keyword:
  # parent local = non local keyword.
  def outer():
      x = "local"
      def inner():
          nonlocal x # here we are calling parent local x which is x = "local".
          x = "nonlocal" #here we have declared nonlocal to the x variable ,so by this way we have changed the value of x to local to nonlocal.
          print("inner:", x)

      inner()#output: inner: nonlocal
      print("outer:", x)
  outer()# output: outer: nonlocal






def outer():
    x = "local"

    def inner():
        #nonlocal x  # here we are calling parent local x which is x = "local".
        x = "nonlocal"  # here we have declared nonlocal to the x variable ,so by this way we have changed the value of x to local to nonlocal.
        print("inner:", x)
    inner()# output: inner: nonlocal

    print("outer:", x)


outer() # output: outer: local






# why do we need scope:
  # cpu of computer has limited memory and allocation of resources to process need to be done.
    # so after executing the function  python interpreter removes its space and allocate to other needed program.
       # scopes makes this easy and that is why scope is need in programming.





# modules in python:
  # modules is composed of many python files.
    # here you have created 2 files
       one is main.py and utility.py
        in the utility.py you have defined the
 functions:

   # inside the utility.py:
     def multiply(num1,num2):
         return num1 * num2
     def divide(num1, num2):
         return num1/num2



     # in the second file which is main.py you are importing utility.py
      import utility
      print(utility.multiply(2,3)) #output: 6
      print(utility.divide(2,3)) # output: 0.66666


# pycharm in python:

# packages in python:
    # here we are creating another file whose name is shopping_cart.py which is inside the shopping package.
        # package: package is simply a folder.package cantains files inside it, modules inside it.
      # shopping_cart.py:
         def buy(item):
             cart = []
             cart.append(item)
             return cart
         # now in main.py:
           import utility
           import shopping_cart

           print(shopping_cart) # error , no module found error , no module named shopping_cart.

             # so as correction in main.py:
               import utility
               import shopping.shopping_cart # here shopping is package while the shopping_cart  is a module.

               print(shopping.shopping_cart) # output: <module 'shopping.shopping_cart' from 'path of the package...'.>





             import utility
             import shopping.shopping_cart  # here shopping is package while the shopping_cart  is a module.

             print(shopping.shopping_cart.buy('apple')) # output: ['apple']





             # Different ways to import:
                import utility
                from shopping.more_shopping.shopping_cart import buy
                print(buy('apple')) # output: ['apple']
                  # by this way you can also  import modules .
                    # here shopping is a package
                       # more_shopping is a package inside the shopping package.
                         # shopping_cart is a python file or a module
                            # buy is function inside the python file.


                from utility import multiply, divide
                from shopping.more_shopping.shopping_cart import buy

                print(buy('apple'))#output: ['apple']
                print(divide(5, 2))# output: 2.5
                print(multiply(5,2)) #output: 10






              from utility import multiply, divide
              from shopping.more_shopping import shopping_cart

              print(shopping_cart.buy('apple'))  # output: ['apple']
              print(divide(5, 2))  # output: 2.5
              print(multiply(5, 2))  # output: 10

#






              from utility import multiply, divide
              from shopping.more_shopping import shopping_cart

              print(shopping_cart.buy('apple'))  # output: ['apple']
              print(divide(5, 2))  # output: 2.5
              print(multiply(5, 2))  # output: 10
              print(max([1,2,3])) # output: 3




              # in the function you have taken:
               def max():
                return 'oops'
#             # when you are calling the max function :
              from utility import multiply, divide, max
              from shopping.more_shopping import shopping_cart

              print(shopping_cart.buy('apple'))  # output: ['apple']
              print(divide(5, 2))  # output: 2.5
              print(multiply(5, 2))  # output: 10
              print(max([1,2,3])) #output: error , parameter are zero but the 1 argument is given.


              # you can also import by using * where we are taking all the conditions .

             from utility import *
             from shopping.more_shopping import shopping_cart

             print(shopping_cart.buy('apple'))  # output: ['apple']
             print(divide(5, 2))  # output: 2.5
             print(multiply(5, 2))  # output: 10
             print(max([1, 2, 3]))  # output: error , parameter are zero but the 1 argument is given.


            # the good way to import is by passing the function name at the import.


# Error handling in python:
   def hooohooooo()
       pass # here in the output: you will get an syntax error.

   def hoohojoo():
       1 + name  # output: syntaxError.


def hoohojoo():
    1 + name

hoohojoo() # output: NameError.


def hoooohooo():
    li = [1,2,3]
    li[5]

hoooohooo()# indexError.

  # error handling allows us to let the program execute if error comes , there will be no stopping of execution.
  age = int(input('what is your age?'))
  print(age) # output: error shown , invalid literal for int() with base10:'jhdkasF'
     # to prevent this error  we can use this blocks:
      try:
          age = int(input('what is your age? '))
          print(age)
      except:
          print('please enter a number') # output: what is your age: 5
                                          # 5
          # output: what is your age? jkojk
             # please enter a  number
                # after this to program ended.

        # but we want that the program should not be ended so we will use here while loop:
        while True:
            try:
                age = int(input('what is your age? '))
                print(age)
            except:
                print('please enter a number')
                #output:
                # what is your age? jkojoj
                # please enter a number
                # what is your age?  # this will happen again and again till you put the right value here.
                   # when you put the right value like:
                        what is your age? 10
                          10
                        what is your age? # is showing again.

              # so to stop this execution after putting the right value to it we will use else:
                 while True:
                     try:
                         age = int(input('what is your age?'))
                         print(age)
                     except:
                         print('please enter a number')
                     else:
                         print('thank you !')
                         break
                         # output: what is your age? : 10
                                   # 10
                                   # thank you!.

while True:
    try:
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you !')
        break
                # output: what is your age? : 0
                 # please enter age higher than 0
                # output: what is your age? : kjfkl
                 # please enter a number.
                 # what is your age?
                # output: what is your age? : 77
                # thank you!




        while True:
            try:
                age = int(input('what is your age?'))
                10 / age
            except ValueError:
                print('please enter a number')
            except ValueError:
                print('!!!')
            except ZeroDivisionError:
                print('please enter age higher than 0')
            else:
                print('thank you !')
                break
          # output: what is your age?: fjfj
             # please enter a number.
        # here which error is found that  except error will be get executed and comes out of the program.
          # and remaining errors will not get executed.




#Error handling 2:

def sum(num1, num2):
    try:
        return num1 + num2
    except:
        print('something is wrong')


print(sum('1',2)) # this is error , here string 1 and int 2 is given which is not correct
#output: something is wrong.
   # None


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('please enter numbers') # to be more specific so we are giving the name of the error which is typeerror.
        # output: please enter numbers


print(sum('1', 2)) #output: None





def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('please enter numbers') # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, 2)) #output:3






def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers' + err)  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2'))  # output: during the handling of the above exception , another exception occurred.
  # typeerror : unsupported operand type(s) for +: 'int' and 'str'.









def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('please enter numbers')  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2')) # output: please enter numbers
                   # None







def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2')) # output: please enter numbers unsupported operand type(s) for + : 'int' and 'str'
                   # None






def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(err)  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2')) # output: unsupported operand type(s) for + : 'int' and 'str'
                   # None






def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):
        print('ooops')  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2')) # output: ooops
                   # None




def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError):
        print('ooops')  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, 0))  # output: ooops
# None





def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, 0))  # output: division by zero
                  # None





def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err:
        print(err)  # to be more specific so we are giving the name of the error which is typeerror.


print(sum(1, '2'))  # output:unsupported operand type(s) for /: 'int' and 'str'
                    # None





# exercise error handling:

while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you !')
        break
    finally:
        print('ok, i am finally done') # output:
         # what is your age? 40
         # thank you!
         # ok, i am finally done






while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you !')
        break
    finally:
        print('ok, i am finally done') # output:
          # what is your age?: 0
          # please enter age higher than 0
          # ok, i am finally done
          # what is your age?




while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
    except ValueError:
        print('!!!')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thank you !')
        break
    finally:
        print('ok, i am finally done')  # output:
        # what is your age?: fljflkjf
        #please enter a number
        # ok, i am finally done
        # what is your age?

   # finally will get executed at the end of the program whether it is wrong or correct.




while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
    #output: what is your age? 0
    #please enter age higher than 0
    #ok, i am finally done # here the finally gets executed but print is not after executing finally we came out of the loop.






while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
        break
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
    # output: what is your age? jkkjfk
    # please enter  a number
    # ok, i am finally done
    # what is your age?




    while True:
        try:
            age = int(input('what is your age?'))
            10 / age
        except ValueError:
            print('please enter a number')
            continue
        except ZeroDivisionError:
            print('please enter age higher than 0')
            break
        else:
            print('thank you !')
            break
        finally:
            print('ok, i am finally done')
        print('can you hear me?')
        #output:  what is your age? 18
        # thank you!
        # ok, i am finally done




while True:
    try:
        age = int(input('what is your age?'))
        10 / age
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
    # output: what is your age? 18
    #thank you!
    # ok, i am finally done
    # can you hear me?
    # what is your age?







# Error handling 3:


while True:
    try:
        age = int(input('what is your age?'))
        10 / age
        raise ValueError('hey cut it out') # this throws execution to except valueerror block.
    except ValueError:
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
     # output: what is your age? 5
     # please enter a number
     # ok, i am finally done
    # what is your age?




while True:
    try:
        age = int(input('what is your age?'))
        10 / age
        raise ValueError('hey cut it out')  # this throws execution to except valueerror block.
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
    # output: error is shown , showing ValueError: hey cut it out , here that is shown which we want to be displayed.





while True:
    try:
        age = int(input('what is your age?'))
        10 / age
        raise Exception('hey cut it out')  # this throws execution to except valueerror block.
    except ZeroDivisionError:
        print('please enter age higher than 0')
        break
    else:
        print('thank you !')
    finally:
        print('ok, i am finally done')
    print('can you hear me?')
  # output: Exception: hey cut it out








# Working with files in python:

   # in the python file named script.py:
      # script.py:
         my_file = open('test.txt')

         print(my_file.read())

    # in the mac ,first we have created a file named test.txt by using touch command
         # in the terminal we are running the script.py
            # inside the test.txt , we have written: hi my name is andrei neagoie
              # so while running the script.py you will get  the output : hi my name is andrei neagoie.


    #
          my_file = open('test.txt')

          print(my_file.read())
          print(my_file.read())
          print(my_file.read())
         #output:
          you will get : hi my name is Andrei Neagoie


           this two print is showing blank spaces

       # to resolve this :

            my_file = open('test.txt')

            print(my_file.read())
            my_file.seek(0)
            print(my_file.read())
            my_file.seek(0)
            print(my_file.read())
           # output:
hi my name is Andrei Neagoie
hi my name is Andrei Neagoie
hi my name is Andrei Neagoie


          #script.py:
           my_file = open('test.txt')
           print(my_file.readline())

          # test.txt:
            hi my name is Andrei Neagoie
            :)
            how are you?

           # on executing the script.py:
             we will get in the output:  hi my name is Andrei Neagoie
             next lines are not get  printed







           my_file = open('test.txt')
           print(my_file.readline())
           print(my_file.readline())
           print(my_file.readline())

           # output :
          hi my name is Andrei Neagoie
          :)
          how are you?





           my_file = open('test.txt')
           print(my_file.readlines())
           #output:
          ['hi my name is Andrei Neagoie\n', ':)\n', '
          how are you?']

        # when you are done then you should close your file with:
           .close()  function

         my_file = open('test.txt')
         print(my_file.readlines())

         my_file.close()
         # this is stop further execution of the program in the file.






# file path:
         # script.py:
         with open('app\sad.txt', mode='r') as my_file:
             print(my_file.read())
             # output: :(
             # on providing the absolute path(whole path name ) , results are the same.
          with open('\user\windows\downloads\app\sad.txt', mode='r') as my_file:
                print(my_file.read())

            with open('./app/sad.txt', mode='r') as my_file: # in the mac os
                print(my_file.read())
                # by using ./ in front of app, we are working in current folder.
               with open('../app/sad.txt', mode='r') as my_file:  # in the mac os
                     print(my_file.read()) # it is going to user account to find app/sad.txt by using ../

                # pathlib - object - oriented filesystem paths for both windows and mac.






# file i/o errors:
                # script.py:
                     try:
                          with open('sad.txt', mode ='r') as my_file:
                              print(my_file.read())
                     except FileNotFoundError as err:
                         print('file does not exist') # while running script.py output:file does not exist
                                                      # FileNotFoundError: no such file or directory:'sad.txt'

                         raise err




try:
    with open('sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')  # while running script.py output:file does not exist
    # FileNotFoundError: no such file or directory:'sad.txt'

    raise err
except IOError as err:
    print('IO error')
    raise err
# output:
   #file does not exist
  # file not found error # FileNotFoundError







try:
    with open('sad.txt', mode='x') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')  # while running script.py output:file does not exist
    # FileNotFoundError: no such file or directory:'sad.txt'

    raise err
except IOError as err:
    print('IO error')
    raise err
#output:
 # IO error
 # io UnsupportedOperation not readable.


 # Read, write and append:
    with open('test.txt') as my_file:
        print(my_file.readlines()) # output:  ['hi my name is Andrei Neagoie\n', ':)\n', '
          how are you?']

        # open has a default parameter mode where read is as r mode = 'r'

with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())
    #output: ['hi my name is Andrei Neagoie\n', ':)\n', '
          how are you?']


with open('test.txt', mode='w') as my_file:
    print(my_file.readlines())
    #output: while executing script.py
       # io.UnsupportedOperation: not readable

with open('test.txt', mode='rw') as my_file:
    print(my_file.readlines())
    # output: ValueError: must have exactly one of create/read/write/append mode

with open('test.txt', mode='r+') as my_file:
    print(my_file.readlines()) # in order to read and write we will take r+
     # output: [], here we are getting empty list because test.txt is empty.

with open('test.txt', mode='r+') as my_file:
   text = my_file.write('hey it\' me!')
   print(text)
    #output: 11

with open('test.txt', mode='r+') as my_file:
    text = my_file.write(':)')
    print(text)
        #output: 2
    #in the test.txt the front letters he has been replaced by :) .
    #by using append mode you can add text at the end of the line .

with open('test.txt', mode='a') as my_file:
    text = my_file.write('hey it\' me!') # here the a is for append mode.
    print(text) #output: hey it' me!:)

with open('test.txt', mode='w') as my_file:
        text = my_file.write('hey it\' me!')
        print(text) #output: in the test.txt only :) smily  face is shown.

with open('test.txt', mode='r+') as my_file:
    text = my_file.write(':)') # here the r+ is for read and write
    print(text)
    # output: he is overwrite and write :) , recursor set to 0 and overwrite it.
      # text is showing in the file is :)y it' me!:)
      # while executing script.py we are getting output 2


    # if we are taking that file which doesn't exist at the desktop
    with open('sad.txt', mode='r+') as my_file:
        text = my_file.write(':(')
        print(text)
        #output:
           # while executing script.py
         # FileNotFoundError: No such file or  directory: 'sad.txt'

        with open('sad.txt', mode='w') as my_file:
            text = my_file.write(':(')
            print(text)
            # output:
             # while executing script.py output is 2.
                # while doing ls you will get sad.txt and inside it you will get :(
                   # so the write also creates a file if it is not exist in desktop and also overwrite files.







# Exercise : Translator:
   # here in the script.py :
      try:
          with open('./test.txt', mode='r') as my_file:
              print(my_file.read())

      except FileNotFoundError as e:
          print('check your file path silly!')

          # in mac running script.py:
            # output: My name is Andrei Neagoie


    # inside the test.txt we had written :
        # My name is Andrei Neagoie.


    # first install the translator .
    # then use as a python module  file has given the next steps.
    # in the script.py:
     from translate import Translator

     translator = Translator(to_lang="ja")
     try:
         with open('./test.txt', mode='r') as my_file:
             text = my_file.read()
             translation = translator.translate(text)
             print(translation)
     except FileNotFoundError as e:
         print('check your file path silly!')

         # while running python3 script.py:
            #  output: text in japanese Andrei Neagoie text in japanese.

from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('./test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./test-ja.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path silly!')
    # while executing script.py now a output file of translation of english to japenese is being saved to desktop as a test-ja.txt.
