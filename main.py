def logger(msg):

  def log_message():
    print('Log:', msg)
  return log_message

log_hi = logger('Hi!')
log_hi()

def sum(a, b):

  def addnum():
    print(a+b)
  return addnum
summation = sum(20,20)
summation()