import os, sys
while True:
    if sys.argv[1]=='up':
        t='0'
    else:
        t='1'
        
    if t == '1':
        os.system("pip install requests")
        os.system("pip install colorama")
        os.system("pkg install php")
        os.system("rm i.tl")
        save_file = open("s.sh", "w+")
        save_file.write("python3 sherl.py")
        save_file.close()
        os.system("cat s.sh > /data/data/com.termux/files/usr/bin/s")
        os.system("chmod 700 /data/data/com.termux/files/usr/bin/s")
        break
    elif t == '0':
        os.system("pkg install wget")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/sherl.py")
        os.system("wget https://raw.githubusercontent.com/termux-lab/sherlock/master/index.php")
        os.system("s")
        break
    else:
        print("0/1 ???")
