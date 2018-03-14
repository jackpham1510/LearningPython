import queue
from mymap import myMap, heuristic
from modules import showResultWithAttr, showStep, aweSomeSort

def GBFS(start, goal):
  q = queue.deque()
  q.append(start)

  previous = [] # khởi tạo previous kiểu dictionary
  for city in myMap.keys():
    previous.append((city, {'from': None, 'heuristic': heuristic[city]}))
  previous = dict(previous)

  counter = 0
  while 1:
    counter += 1
    showStep(counter, q, previous, 'heuristic') # Show các bước thực hiện thuật toán

    curCity = q.popleft() # dequeue
    
    if curCity == goal:
      print('Success!')
      showResultWithAttr(previous, start, goal, 'heuristic')
      return True # Tìm thấy goal
    
    for city in myMap[curCity].keys(): # Các thành phố có thể đi đến được từ thành phố hiện tại
      if previous[city]['from'] == None: # Nếu chưa đi qua thành phố này
        q.append(city) # Thêm vào hàng đợi
        previous[city]['from'] = curCity # Lưu lại dấu vết
        

    if len(q) == 0:
      print('Fail!')
      return False # Không thể đi đến goal từ start
    q = queue.deque(aweSomeSort(q, previous, 'heuristic'))
