import os 
os.system("clear")
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"

banner=f"""{r} ▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄▓██   ██▓     
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██  ██▒     
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌ ▒██ ██░     
▒██░█▀  ▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌ ░ ▐██▓░     
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓  ░ ██▒▓░     
░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒      
▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░      
 ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░       
 ░          ░  ░    ░ ░      ░ ░     ░    ░ ░          
      ░                            ░      ░ ░          
▓█████▄  ██▀███   ▄▄▄        ▄████  ▒█████   ███▄    █ 
▒██▀ ██▌▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░   ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░   ░░   ░   ░   ▒   ░ ░   ░ ░ ░ ░ ▒     ░   ░ ░ 
   ░       ░           ░  ░      ░     ░ ░           ░ 
 ░"""
logo=f"""{r}                 ___====-_  _-====___
           _--^^^#####//      \\\\#####^^^--_
        _-^##########// (    ) \\\\##########^-_
       -############//  |\^^/|  \\\\############-
     _/############//   (@::@)   \\\\############\\_
    /#############((     \\\\//     ))#############\\
   -###############\\\\    (oo)    //###############-
  -#################\\\\  / VV \\  //#################-
 -###################\\\\/      \\//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv){y}
                  
                   by BLINKING-IDIOT
                 {p}insta: @a.r.n_beatzzzz{g}
                  """
print(banner)
print(logo)
def wireless():
    print("make sure android debugging is on in your mobile\nmake sure your pc and mobile are connected on same network!")
    print("now connect your mobile with pc using usb!...")
    input("press enter to continue.....")
    os.system("adb tcpip 5555")
    print("now disconnect your phone")
    input("press enter to continue.....")
    x=input("enter the ip address:")
    os.system("adb connect "+x+":5555")
def wired():
    print("make sure android debugging is on in your mobile")
    print("just connect your mobile with pc using usb!")
    input("press enter to continue.....")
def connect():
    os.system("clear")
    print(banner)
    print(logo)
    x=input("[1]:wired connection:\n[2]:wireless connection:\n")
    if x=="1":
        wired()
    else: 
        wireless() 
def lis():
    os.system("clear")
    print(banner)
    print(logo)
    print("screen - to control screen from desktop -(you need to install scrcpy in linux by executing \"sudo apt install scrcpy\" in terminal)")
    print("activity - to see activity of mobile")
    print("battery - to see battrey information of mobile")
    print("system info - to see system information of mobile")
    print("type - to type in mobile")
    print("net state - to see net state of mobile")
    print("restart - to restart mobile")
    print("openurl -to open a url in mobile")
    print("wifi on - to switch on wifi in mobile (sometimes root required!)")
    print("wifi off - to switch off wifi in mobile(sometimes root required!)")
    print("adv prop -for getting advanced properties")
    print("shell - for opening mobile shell")
    print("new tools adding soon!")
def tools():
    print(banner)
    print(logo)
    while True:
        print("enter \"tools\" for listing tools")
        x=input("enter the tool:")
        if x=="tools":
            lis()
        elif x=="screen":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("scrcpy")
            os.system("clear")
            print(banner)
            print(logo)   
        elif x=="battery":
            os.system("clear")
            print(banner)
            print(logo)            
            os.system("adb shell dumpsys battery")
        elif x=="activity":
            os.system("clear")
            print(banner)
            print(logo)            
            os.system("adb shell dumpsys activity")
        elif x=="system info":
            os.system("clear")
            print(banner)
            print(logo)
            print("Operating System:android\nComputer Hostname:")
            os.system("adb shell getprop net.hostname")
            print("Computer Username:")
            os.system("adb shell getprop ro.product.name")
            print("Release Version:")
            os.system("adb shell getprop ro.build.version.release")
            print("Processor Architecture:")
            os.system("adb shell getprop getprop ro.product.cpu.abi")
        elif x=="type":
            os.system("clear")
            print(banner)
            print(logo)
            k=input("enter the word to type:")
            os.system("adb shell input text "+k)
        elif x=="net state":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell netstat")
        elif x=="restart":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell reboot")
        elif x=="wifi on":
            os.system("clear")
            print(banner)
            print(logo)
            print("done!")
            os.system("adb shell svc wifi enable")
        elif x=="wifi off":
            os.system("clear")
            print(banner)
            print(logo)
            print("done!")
            os.system("adb shell svc wifi disable")
        elif x=="openurl":
            os.system("clear")
            print(banner)
            print(logo)
            k=input("enter the url to open:")
            os.system("adb shell am start -a android.intent.action.VIEW -d "+k)
            os.system("clear")
            print(banner)
            print(logo)
        elif x=="adv prop":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell getprop | grep -e 'model' -e 'version.sdk' -e 'manufacturer' -e 'hardware' -e 'platform' -e 'revision' -e 'serialno' -e 'product.name' -e 'brand'")
        elif x=="shell":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell")
            os.system("clear")
            print(banner)
            print(logo)          
        else:
            os.system("clear")
            print(banner)
            print(logo)
            print("not a tool...retry")
def main():
    x=input("is your mobile connected with ADB?[y/n]")
    if x=="n":
        connect()
    os.system("clear")
    tools()
main()
