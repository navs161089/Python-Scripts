#!/opt/rh/rh-python36/root/usr/bin/python
import subprocess
cmd1 = 'df'
args1 = '-h'
cmd2 = 'grep'
args2 = 'xvda1' 
p1 = subprocess.Popen([cmd1, args1], stdout=subprocess.PIPE)
p2 = subprocess.Popen([cmd2, args2], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
out1 = str(p2.communicate())
out2 = out1.split("\n")
print(out2)
result = []
for line in out2:
	result.append(line)

for i in range(1, len(result) - 1):
	print(result[i])
