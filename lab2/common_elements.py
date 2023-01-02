def common(list1, list2):
  set1 = set(list1)
  set2 = set(list2)

  if len(set1.intersection(set2)) > 0:
      return list(set1.intersection(set2)) 
  else:
      return []

l1 = ['a', 'b', 'c']
l2 = ['d', 'c', 'a']

print(common(l1, l2))

print(l1, l2)
