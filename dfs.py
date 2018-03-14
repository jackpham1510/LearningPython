from mymap import myMap
from modules import showResult

def DFS(start, goal):
  previous = [] # khởi tạo previous kiểu dictionary
  for city in myMap.keys():
    previous.append((city, None))
  previous = dict(previous)

  def _DFS(_start): # Chạy đệ qui DFS
    for city in myMap[_start].keys(): # Các thành phố có thể đi đến được từ thành phố hiện tại
      if previous[city] == None: # Nếu chưa đi qua thành phố này
        previous[city] = _start # Lưu lại dấu vết
        if city == goal:
          return True  
        elif _DFS(city):
          return True
    return False
  
  if (_DFS(start)):
    print('Success!')
    showResult(previous, start, goal)
    return True # Tìm thấy goal
  else:
    print('Fail!')
    return False