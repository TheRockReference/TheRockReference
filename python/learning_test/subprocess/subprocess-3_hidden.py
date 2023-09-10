
#************** IN PROGESS ***************

# windows only

import subprocess

info = subprocess.STARTUPINFO()
info.dwFlags = 1
info.wShowWindow = 0  # hidden

openProcess = subprocess.Popen('notepad', startupinfo=info)

print(f"returncode = {openProcess.returncode}")
print(f"PID = {openProcess.pid}")




# import subprocess

# IS_WIN32 = 'win32' in str(sys.platform).lower()


# def subprocess_call(*args, **kwargs):
#     #also works for Popen. It creates a new *hidden* window, so it will work in frozen apps (.exe).
#     if IS_WIN32:
#         startupinfo = subprocess.STARTUPINFO()
#         startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
#         startupinfo.wShowWindow = subprocess.SW_HIDE
#         kwargs['startupinfo'] = startupinfo
#     retcode = subprocess.call(*args, **kwargs)
#     return retcode


