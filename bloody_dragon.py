import os,time
import choose,option
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
    os.system("adb kill-server")
    os.system("adb start-server")
    print(f"{g}[{r}!{g}]{y}make sure android debugging is on in your mobile\n{g}[{r}!{g}]{y}make sure your pc and mobile are connected on same network!")
    print(f"{g}[{r}!{g}]{y}now connect your mobile with pc using usb!...")
    input("press enter to continue.....")
    print(f"{g}[{r}!{g}]{r}check your phone! sometimes there will be a permisson to allow!")
    print(f"{g}[{r}!{g}]{r}enter always allow this computer and give permission")
    print("wait for 3 seconds!")
    time.sleep(3)
    input("press enter to continue...")
    os.system("adb shell ip route > addrs.txt")
    f=open("addrs.txt","r")
    ip=f.read()
    ip=ip[56:68]
    f.close()
    print(f"{g}[{r}!{g}]{r}Trying automatic connection....!")
    if ip=="":
        print(f"{g}[{r}!{g}]{r}Automatic connection failed")
        print(f"{g}[{r}!{g}]{r}try manual connection")
        ip=input(f"{y}enter the ip address of mobile:")
    else:
        if ip[11]==" ":
            ip=ip[:11]
        print(f"{g}[{r}!{g}]{r}Automatic connection success!")
    print(f"{g}ip adress={y}{ip}")
    os.system("adb tcpip 5555")
    print(f"{y}now disconnect your phone")
    input("press enter to continue...")
    os.system("adb connect "+str(ip)+":5555")
def wired():
    os.system("adb kill-server")
    os.system("adb start-server")
    print(f"{g}[{r}!{g}]{y}make sure android debugging is on in your mobile")
    print(f"{g}[{r}!{g}]{y}just connect your mobile with pc using usb!")
    print(f"{r}check your phone! sometimes there will be a permisson to allow!")
    print(f"{r}enter always allow this computer and give permission")
    input("press enter to continue.....")
def connect():
    os.system("clear")
    print(banner)
    print(logo)
    x=input(f"{g}[{r}1{g}]{r}:{y}wired connection:\n{g}[{r}2{g}]{r}:{y}wireless connection:\n")
    if x=="1":
        wired()
    else: 
        wireless() 
def tools():
    print(banner)
    print(logo)
    while True:
        option.opt()
        x=input(f"enter the tool:{r}")
        if x=="99":
            os.system("adb kill-server")
            print("thanks for using our tool!\n don't forget to star this tool!")
            exit()
        choose.chos(x)
def main():
    while True:
        print(f"\n{g}[{r}!{g}]{r} this tools is for educational purpose only\n")
        print(f"{g}[{r}!{g}]{r} i am not responsible for any damage caused by using this tool!{g}\n")
        x=input(f"{y}Is your mobile connected with ADB?{g}[{r}y{g}/{r}n{g}]")
        if x=="n":
            connect()
            os.system("clear")
            tools()
        elif x=="y":
            os.system("clear")
            tools()
        else:
            os.system("clear")
            print(banner)
            print(logo)
            print(f"{g}[{r}!{g}]{r}wrong input!,try agian")
main()
