import os
import subprocess

username = os.getlogin() #get username windows


Value = 'C:\\Users\\{0}\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe -list-avds'.format(username)
listDevice = subprocess.check_output(Value).decode('UTF-8')

list = ['']
index = 0
for find in listDevice :
	if find == '\n' :
		index+=1
		list.append('')
	if find != '\n' and find != '\r' :
		list[index] = list[index] + find



del(list[-1]) #delete the last list

print(list)

index = 0
for Device in list:
	print(
		str(index)+'. '+ Device
	)
	index += 1
	

while True :
	choice = int(input('\n\ninput your number Device = '))
	if choice < 0 or choice > index :
		continue
	else:
		break


os.system(
		'C:\\Users\\{0}\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe -avd {1}'
		.format(username,list[choice])
	)



input() #breakLine