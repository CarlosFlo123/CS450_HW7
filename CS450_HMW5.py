'''--------------------------------------------------------------------------
Author: Carlos Flores Valero
Northwestern Polytechnic University, Fremont, CA
Date: 10/28/2019
---------------------------------------------------------------------------'''

#1______________________________________________
def rpl_all(d, m, n):
  for i in d:
    if d[i] == m:
      d[i] = n

d = {'f':2, 'b':3, 'g':3, 'xy':99}
rpl_all(d,3,'poof')
d == {'f':2, 'b':'poof', 'g':'poof', 'xy':99}



#2______________________________________________
def freq(L):
  con = {}
  for i in L:
    if i not in con:
      con[i] = 1
    else:
      con[i] += 1
  return con

freq(['the', 'name', 'of', 'the', 'name', 'of', 'the', 'song'])



#3______________________________________________
def mst_freq(lst):
  con = freq(lst)
  values = list(con.values())
  most_freq=(max(values))
  for i in con:
    if con[i] == most_freq:
      return i
  return {}

lst = [1, 4, 2, 4]
mst_freq(lst)


#4______________________________________________
def is_dplc(L):
  con = freq(L)
  for i in con:
    if con[i] > 1:
      return True
  return False

lst = [1, 4, 2, 1]
is_dplc(lst)



#5______________________________________________
#Didnt know what to put as value in the dict, so returned
#list of the common keys instead.
def cmn_keys(d0, d1):
  res = []
  for i in d0:
    for j in d1:
      if j == i:
        res.append(j)
  return list(set(res))

#This is returning a dict I hope this is the expected output.
def cmn_keys1(d0, d1):
  res = {}
  for i in d0:
    for j in d1:
      if j == i:
        tmp = {d0[i]:d1[j]}
        res[j] = tmp
  return dict(res)

a = {'f':2, 'b':5, 'g':3, 'xy':99}
b = {'e':2, 'b':3, 'c':3, 'xy':100}
cmn_keys(a, b)
cmn_keys1(a, b)


#6______________________________________________
# class Dictionary:
#   key = ''
#   value = []
#   def __init__(self):
#     key = ''
#     value = []
#   def addValue(a):
#     self.value += a

# def bld_successors_tab(tokens):
#   con = Dictionary()
#   con.key = tokens[0]
#   con.addValue(1)
#   con.__dict__
#   #   for i in range(len(tokens)):
# #     if i+1 == len(tokens):
# #       con[i] = tokens[0]
# #     else:
# #       con[i] = tokens[i+1]
# #   return con.values()

# text = ['We', 'are', 'learning', 'python', ',', 'it', 'is', 'very', 'powerful', 'and', 'very', 'important', '.']
# table = bld_successors_tab(text)
# # sorted(table)
# table


#7______________________________________________
def rm_first(lst, elm):
  if lst == []:
    return lst
  elif lst[0] == elm:
    lst.remove(lst[0])
    return lst
  else:
    return [lst[0]] + rm_first(lst[1:], elm)

rm_first([3, 4], 3)
rm_first([3, 4, 3], 3)
rm_first([2, 4], 3)
rm_first([], 0)



#8______________________________________________
def sort(lst):
  if lst == [] or len(lst) == 1:
    return lst
  else:
    tmp = min(lst)
    return [tmp] + sort(rm_first(lst, tmp))

#sort([5, 2, 1, 7, 8, 3])
#sort([6, 2, 5])
#sort([2,3])
#sort([3])
#sort([])
    
