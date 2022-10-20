

from collections import deque
import threading 
import time
class queue:
    def __init__(self):
        self.box=deque()
    def enque(self,data):
        self.box.appendleft(data)
    def deque(self):
        print(self.box.pop())
        
od=queue()
items=["Beef","salad","rice","mutton"]
ln=len(items)
for data in range (0,ln):
   
   thrd1=threading.Thread(target=od.enque,args=(items[data],))
   thrd2=threading.Thread(target=od.deque ,args=())
  
   time.sleep(0.5)

   thrd1.start()
    
   time.sleep(2)

   thrd2.start()
    
   time.sleep(1)