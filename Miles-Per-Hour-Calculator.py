#This Program will calculate the distances at incremented times until it reaches the final hour
#Pedro Ayala

#input speed and time
speed = int(input('Input speed in miles per hours: '))
time = int(input('Input time in hours: '))

#loop to calculate and print distance for each hour that passes
for i in range( 1, time + 1):
   distance = speed * i
   print ('Hour:', i, 'Distance Traveled:', distance)
   i = i + 1   #increments loop counter
