import subprocess

# Change how much time the goggle form to be submit 
input = 5

for x in range(input):
    burst_command = 'python autogform.py'
    running_program = subprocess.Popen(burst_command)
    stdoutdata, stderrdata = running_program.communicate()
    print(x)