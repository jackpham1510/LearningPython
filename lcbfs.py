import queue
from mymap import myMap
from modules import showResultWithAttr, showStep

def LCBFS(start, goal):
  q = queue.deque() # khởi tạo queue
  q.append(start)  # enqueue
  
  previous = [] # khởi tạo previous kiểu dictionary
  for city in myMap.keys():
    previous.append((city, {'from': None, 'total_cost': 0}))
  previous = dict(previous)
  
  counter = 0
  while 1:
    counter += 1
    showStep(counter, q, previous) # Show các bước thực hiện thuật toán

    curCitys = []
    while len(q) != 0:
      curCitys.append(q.popleft()) # Lấy ra hết tất cả thành phố có thể đi đến được
    
    for curCity in curCitys:
      curCityTotalCost = previous[curCity]['total_cost'] # Chi phí để đi từ start đến curCity
      
      if curCity != goal:
        for city in myMap[curCity].keys(): # Các thành phố có thể đi đến được từ curCity
          cityTotalCost = previous[city]['total_cost'] # Chi phí được tính ở bước trước đó
          totalCost = myMap[curCity][city]['cost'] + curCityTotalCost # Chi phí để đi từ start -> curCity -> city 
          
          # Nếu chưa đi qua thành phố này hoặc chi phi đi từ start -> curCity -> city tốt hơn chi phí trước đó
          if previous[city]['from'] == None or totalCost < cityTotalCost :
            if q.count(city) != 0: # Nếu đã có city này trong hàng đợi thì xóa nó đi
              q.remove(city)
            q.append(city) # Thêm vào hàng đợi
            previous[city]['from'] =  curCity # Lưu lại dấu vết
            previous[city]['total_cost'] = totalCost # Cập nhật lại chi phí mới

    if len(q) == 0: break
  
  if previous[goal]['from'] != None: # Nếu có thể đi tới goal
    showResultWithAttr(previous, start, goal)
    return True
  else: 
    return False