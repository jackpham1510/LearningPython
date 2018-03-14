def showResult(previous, start, goal):
  curCity = goal # Truy vết từ điểm đích về điểm bắt đầu
  print('Result:', curCity, end=' ')
  while curCity != start:
    curCity = previous[curCity]
    print('->', curCity, end=' ')

def showResultWithAttr(previous, start, goal, attr='total_cost'):
  curCity = goal # Truy vết từ điểm đích về điểm bắt đầu
  print('Result:', (curCity, previous[curCity][attr]), end=' ')
  while curCity != start:
    curCity = previous[curCity]['from']
    print('->', (curCity, previous[curCity][attr]), end=' ')

def showStep(counter, q, previous, attr='total_cost'):
  print('%d. {' % counter, end=' ')
  i = 0
  lenQ = len(q)
  for v in q:
    i += 1
    if (i < lenQ):
      print((v, previous[v][attr], previous[v]['from']), end=', ')
    else:
      print((v, previous[v][attr], previous[v]['from']), end=' ') 
  print('}')

def aweSomeSort(array, previous, sortBy='total_cost'): # QuickSort (python version)
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = previous[array[0]][sortBy]
        for city in array:
            cost = previous[city][sortBy]
            if cost < pivot:
                less.append(city)
            if cost == pivot:
                equal.append(city)
            if cost > pivot:
                greater.append(city)
        return aweSomeSort(less, previous, sortBy) + equal + aweSomeSort(greater, previous, sortBy) # toán tử nối mảng
    else:  
        return array