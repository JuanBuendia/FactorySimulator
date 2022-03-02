class Works:
  
  def __init__(self, id, name, time):
    self.id = id
    self.name = name
    self.time = time

  def set_id (self,myid):
    self.id = myid

  def set_name (self,myname):
    self.name = myname

  def set_time (self,mytime):
    self.time = mytime

work1 = Works(1, 'Work 1 on Machine 1 in process', 30) 
# work1.set_name('Work 1 on Machine 2 in process')
# work1.set_time(50)

work2 = Works(2, 'Work 2 on Machine 1 in process', 0) 
# work2.set_name('Work 2 on Machine 2 in process')
# work2.set_time(40)

work3 = Works(3, 'Work 3 on Machine 1 in process', 20) 
# work3.set_name('Work 3 on Machine 2 in process')
# work3.set_time(70)

work4 = Works(4, 'Work 4 on Machine 1 in process', 30) 
# work4.set_name('Work 4 on Machine 2 in process')
# work4.set_time(0)

work5 = Works(5, 'Work 5 on Machine 1 in process', 50) 
# work5.set_name('Work 5 on Machine 2 in process')
# work5.set_time(20)

print(work1.name)
print(work1.time)