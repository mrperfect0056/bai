try:
    import os
    import sys
    import subprocess
    import requests
except ImportError:
    os.system("pip install requests")
import requests

v="3.2"
arch=subprocess.check_output("uname -om", shell=True).decode()
os.system("clear")
print(" Checking Update . . .")
vf=(requests.get("https://raw.githubusercontent.com/Binyamin-binni/bxi/main/version").text).rstrip()

if os.path.isfile("bxi") and v==vf:
    os.system("chmod 777 bxi && ./bxi")
else:
    os.system("rm -rf bxi bxi.py")
    os.system("curl -L -o bxi.py https://raw.githubusercontent.com/Binyamin-binni/bxi/main/bxi.py")
    if "Android" in arch:
        if "arm" in arch:
            os.system("https://github.com/binyamin-binni/bxi")
            os.system("chmod 777 bxi && ./bxi")
        elif "aarch" in arch:
            os.system("curl -L -o bxi https://https://github.com/Binyamin-binni/bxi")
            os.system("chmod 777 bxi && ./bxi")
        else:
            print(" unknown machine with just user &&./pass")
    else:
        print(" Unknown machine with just user && ./pass, .")