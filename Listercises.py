'''Question 1'''


def ones_digits(l):
  li = []
  for i in range(0, len(l)):
    li.append(abs(l[i]) % 10)
  return li


print(ones_digits([321, 49120, 9112])) # [1, 0, 2] 321/(10) = (32) remainder 1
print(ones_digits([-123456]))

# Another Example
n = 321
l = 49120
e = 9112
last_digit = [n, l, e]
print(ones_digits(last_digit))

"""#Question 2"""

def lengths_of(l):
  l1 = []
  for i in range(0,len(l)):
    l1.append(len(l[i]))
  return l1
  
print(lengths_of(["hello", "world", ""])) #[5,5,0]

"""#Question 3"""

def filter_odd_lengths(l):
  new_list = [elem for elem in l if len(elem) % 2 != 0]
  return new_list

"""#Question 4"""

def filter_upper(l):
  list_of_upper = [elem for elem in l if elem.isupper()]
  return list_of_upper

"""#Question 5"""

def list_all(l):
  if l == []:
    return False
    l.sort()
    return1[0]

"""#Question 6"""

def list_any(l):
  l.sort()
  return l[-1]

"""#Question 7"""

def immutable_replicate(l, n):
  new_list = []
  for x in range (n):
    new_list.extend(l)
    return new_list

"""#Question 8"""

def mutable_replicate(l, n):
  temp = l [:]
  for i in range(1, n):
    l += temp
  return l 
#enter in your array. the second input is how many times you want your array to be copied. 
mutable_replicate([1, 2, 3, 4, 5], 5)

"""#Question 9"""

def at_least(l, a, n):  
  temp = []
  for elem in l:
    if elem != a:
      temp.append(elem)
# the first list - the temporary list will define whether or not the boolean is true or false. The numbers have to be the same. 
  return len(l) - len(temp) >= n

at_least([1, 2, 3, 4, 5, 1], 1, 3 )
