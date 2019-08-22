#!/opt/rh/rh-python36/root/usr/bin/python
import subprocess
cmd = 'iostat'
args = '-x'
p1 = subprocess.Popen([cmd, args], stdout=subprocess.PIPE)
out1 = str(p1.communicate())
out2 = out1.split("\n")
out2 = out2[0].split('\\')
res = []
for line in out2:
	res.append(line)

for i in range(1, len(res) - 1):
	print(res[i])
  
