import subprocess
def executeCommand():
    '''
    Read a command from user input, validate it, and execute it.
    '''
    command = input("Enter the command to execute: ")
    # Perform necessary validation on the command
    # ...

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Command executed successfully.")
        print("Output:", result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print("Error in command execution:", e.stderr.decode())

executeCommand()

