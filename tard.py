import time

print('\a')
print("started")
count = 0
while count < 10:
	count = count + 1
	time.sleep(60)
	print(str(count) + " minutes passed")
	print('\a')
while True:
	time.sleep(5)
	print('\a')
print("done")