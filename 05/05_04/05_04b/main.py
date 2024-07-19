from collections import deque
def binary_number(number):
  if number <= 0:
    return
  
  queue = deque()
  queue.append(1)
    
  for i in range(number):
      binary = queue.popleft()
      print(binary)
      queue.append(binary * 10)
      queue.append(binary * 10 + 1)

number = int(input())
binary_number(number)
