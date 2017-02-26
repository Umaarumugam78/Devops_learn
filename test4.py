for letter in'positive':
    if letter == 't':
        pass
        print('this is a block')
    print ('current letter:', letter)
print ("Good bye!")

count = 10
while count>0:
    count=count-1
    if count==3:
        break
    print ('current value:', count)
print("its closed")


for letter in 'Python': 
   if letter == 'h':
      pass
      print ('This is pass block')
   print ('Current Letter :', letter)

print ("Good bye!")

try:
    work=40*2
    print(work)
except:
    print("not valid answer")



try:
    user1=int(input("enter a number 1"))
    user2=int(input("enter a number 2"))
    answer=user1*user2
    print("final answer is:", answer)
    myfile=open("not valid num",'a')

except valueerror:
    print("Error: enter a number")

except zerovalueerror:
    print("Error: cannot multiply by 0")

except Exception as e:
    print("unknow error", e)


def models(acura, BMW, Benz, Honda):
    print(modles)
    return

