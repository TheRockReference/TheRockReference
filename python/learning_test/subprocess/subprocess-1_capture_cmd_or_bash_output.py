
import platform

if platform.system() == "Windows":
    
    # windows
    import subprocess
    resultCmdDir = subprocess.run(["cmd", "/c", "dir", "/b"], capture_output=True, text=True)
    
    print(f"\nOn {platform.system()} the list of files and folders in the current directory is : {resultCmdDir}\n")
    print(f"The data type of the output is {type(resultCmdDir.stdout.splitlines())}\n")
    print(f"Complete Process Result = {resultCmdDir}\n")
    print(f"Result type string = {resultCmdDir.stdout}\n")
    print(f"Result type list string = {resultCmdDir.stdout.splitlines()}\n")
    print(f"Returncode = {resultCmdDir.returncode}\n")
    print(f"Error (if any) = {resultCmdDir.stderr}\n")



if platform.system() == "Linux":
    
    # linux
    import subprocess
    resultBashLs = subprocess.run(["ls"], capture_output=True, text=True)
    
    print(f"\nOn {platform.system()} the list of files and folders in the current directory is : {resultBashLs.stdout}\n")
    print(f"The data type of the output is {type(resultBashLs.stdout.splitlines())}\n")
    print(f"Complete Process Result = {resultBashLs}\n")
    print(f"Result type string = {resultBashLs.stdout}\n")
    print(f"Result type list string = {resultBashLs.stdout.splitlines()}\n")
    print(f"Returncode = {resultBashLs.returncode}\n")
    print(f"Error (if any) = {resultBashLs.stderr}\n")
    

