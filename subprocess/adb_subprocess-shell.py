import subprocess
command = 'adb devices '
p = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)

stdout, stderr = p.communicate('ls')
print (stdout)

