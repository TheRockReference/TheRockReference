
# powershell subprocess

import subprocess

resultPwsh = subprocess.run(["pwsh", "-Command", "Get-Childitem", "-Name"], capture_output=True, text=True)
print("\n")
print(f"Complete Process Result = {resultPwsh}\n")
print(f"Result type string = {resultPwsh.stdout}\n")
print(f"Result type list string = {resultPwsh.stdout.splitlines()}\n")
print(f"Returncode = {resultPwsh.returncode}\n")
print(f"Error (if any) = {resultPwsh.stderr}\n")
