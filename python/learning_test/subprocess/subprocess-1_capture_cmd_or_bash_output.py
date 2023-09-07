
import platform

if platform.system() == "Windows":
    
    # windows
    import subprocess
    resultCmdDir = subprocess.run(["cmd", "/c", "dir", "/b"], capture_output=True).stdout.splitlines()
    
    print(f"\nOn {platform.system()} the list of files and folders in the current directory is : {resultCmdDir}")
    print(f"The data type of the output is {type(resultCmdDir)}\n")




if platform.system() == "Linux":
    
    # linux
    import subprocess
    resultBashLs = subprocess.run(["ls"], capture_output=True).stdout.splitlines()
    
    print(f"\nOn {platform.system()} the list of files and folders in the current directory is : {resultBashLs}\n")
    print(f"The data type of the output is {type(resultBashLs)}\n")
    
    newStrResult = []
    for result in resultBashLs:
        strResult = result.decode('utf-8')
        newStrResult.append(strResult)
        
    print(f"Each result in the list are Encoded bytes : {resultBashLs}\n")
    print(f"To get string, I need to decode('utf-8) : {newStrResult}")
        
        
    


