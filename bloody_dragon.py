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
                 {p}insta: @arn_beatz{g}
                  """
print(banner)
print(logo)
def wireless():
    print("make sure android debugging is on in your mobile\nmake sure your pc and mobile are connected on same network!")
    print("now connect your mobile with pc using usb!...")
    input("press enter to continue.....")
    print(f"{r}check your phone! sometimes there will be a permisson to allow!")
    print(f"{r}enter always allow this computer and give permission")
    os.system("adb tcpip 5555")
    print("now disconnect your phone")
    input("press enter to continue.....")
    x=input("enter the ip address:")
    os.system("adb connect "+x+":5555")
def wired():
    print("make sure android debugging is on in your mobile")
    print("just connect your mobile with pc using usb!")
    print(f"{r}check your phone! sometimes there will be a permisson to allow!")
    print(f"{r}enter always allow this computer and give permission")
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
    print(f"{r}-"*120+f"{g}")
    print("screen - to control screen from desktop")
    print(f"{r}-"*120+f"{g}")
    print("activity - to see activity of mobile")
    print(f"{r}-"*120+f"{g}")
    print("battery - to see battrey information of mobile")
    print(f"{r}-"*120+f"{g}")
    print("system info - to see system information of mobile")
    print(f"{r}-"*120+f"{g}")
    print("type - to type in mobile")
    print(f"{r}-"*120+f"{g}")
    print("net state - to see net state of mobile")
    print(f"{r}-"*120+f"{g}")
    print("restart - to restart mobile")
    print(f"{r}-"*120+f"{g}")
    print("openurl -to open a url in mobile")
    print(f"{r}-"*120+f"{g}")
    print("wifi on - to switch on wifi in mobile (sometimes root required!)")
    print(f"{r}-"*120+f"{g}")
    print("wifi off - to switch off wifi in mobile(sometimes root required!)")
    print(f"{r}-"*120+f"{g}")
    print("adv prop -for getting advanced properties")
    print(f"{r}-"*120+f"{g}")
    print("shell - for opening mobile shell")
    print(f"{r}-"*120+f"{g}")
    print("keycode - for sending key")
    print(f"{r}-"*120+f"{g}")
    print("download - to download a file from phone")
    print(f"{r}-"*120+f"{g}")
    print("upload - to uplode a file from phone")
    print(f"{r}-"*120+f"{g}")
    print("new tools adding soon!")
    print(f"{r}-"*120+f"{g}")
def tools():
    print(banner)
    print(logo)
    while True:
        print(f"{g}[{r}0{g}]{y}list tools properties")
        print(f"{g}[{r}1{g}]{y}screen")
        print(f"{g}[{r}2{g}]{y}battery")
        print(f"{g}[{r}3{g}]{y}activity")
        print(f"{g}[{r}4{g}]{y}system info")
        print(f"{g}[{r}5{g}]{y}type")
        print(f"{g}[{r}6{g}]{y}net state")
        print(f"{g}[{r}7{g}]{y}restart")
        print(f"{g}[{r}8{g}]{y}wifi on")
        print(f"{g}[{r}9{g}]{y}wifi off")
        print(f"{g}[{r}10{g}]{y}openurl")
        print(f"{g}[{r}11{g}]{y}adv prop")
        print(f"{g}[{r}12{g}]{y}shell")
        print(f"{g}[{r}13{g}]{y}download")
        print(f"{g}[{r}14{g}]{y}upload")
        print(f"{g}[{r}15{g}]{y}keycode")
        print(f"{g}[{r}16{g}]{y}about Developers")
        print(f"{g}[{r}17{g}]{y}tool not working?")
        print(f"{g}[{r}99{g}]{y}exit")
        x=input(f"enter the tool:{r}")
        if x=="0":
            lis()
        elif x=="1":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("scrcpy")
            os.system("clear")
            print(banner)
            print(logo)   
        elif x=="2":
            os.system("clear")
            print(banner)
            print(logo)            
            os.system("adb shell dumpsys battery")
        elif x=="3":
            os.system("clear")
            print(banner)
            print(logo)            
            os.system("adb shell dumpsys activity")
        elif x=="4":
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
        elif x=="5":
            os.system("clear")
            print(banner)
            print(logo)
            k=input("enter the word to type:")
            os.system("adb shell input text "+k)
        elif x=="6":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell netstat")
        elif x=="7":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell reboot")
        elif x=="8":
            os.system("clear")
            print(banner)
            print(logo)
            print("done!")
            os.system("adb shell svc wifi enable")
        elif x=="9":
            os.system("clear")
            print(banner)
            print(logo)
            print("done!")
            os.system("adb shell svc wifi disable")
        elif x=="10":
            os.system("clear")
            print(banner)
            print(logo)
            k=input("enter the url to open:")
            os.system("adb shell am start -a android.intent.action.VIEW -d "+k)
            os.system("clear")
            print(banner)
            print(logo)
        elif x=="11":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell getprop | grep -e 'model' -e 'version.sdk' -e 'manufacturer' -e 'hardware' -e 'platform' -e 'revision' -e 'serialno' -e 'product.name' -e 'brand'")
        elif x=="12":
            os.system("clear")
            print(banner)
            print(logo)
            os.system("adb shell")
            os.system("clear")
            print(banner)
            print(logo)    
        elif x=="13":
            os.system("clear")
            print(banner)
            print(logo)
            pu=input("Enter the file to download:")
            os.system(f"adb pull {pu}")
            os.system("clear")
            print(banner)
            print(logo)      
        elif x=="14":
            os.system("clear")
            print(banner)
            print(logo)
            pu=input("Enter the file to upload:")
            lo=input("Enter the folder in phone to upload:")
            os.system(f"adb push {pu} {lo}")
            os.system("clear")
            print(banner)
            print(logo)
        elif x=="15":
            codes=""""
0 -->  "KEYCODE_0" 
1 -->  "KEYCODE_SOFT_LEFT" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "KEYCODE_MEDIA_PLAY_PAUSE"
86 -->  "KEYCODE_MEDIA_STOP"
87 -->  "KEYCODE_MEDIA_NEXT"
88 -->  "KEYCODE_MEDIA_PREVIOUS"
89 -->  "KEYCODE_MEDIA_REWIND"
90 -->  "KEYCODE_MEDIA_FAST_FORWARD"
91 -->  "KEYCODE_MUTE"
92 -->  "KEYCODE_PAGE_UP"
93 -->  "KEYCODE_PAGE_DOWN"
94 -->  "KEYCODE_PICTSYMBOLS"
122 -->  "KEYCODE_MOVE_HOME"
123 -->  "KEYCODE_MOVE_END"
"""
            os.system("clear")
            print(banner)
            print(logo)
            print(codes)
            pu=input("Enter keycode:")
            os.system(f"adb shell input keyevent {pu}")
            os.system("clear")
            print(banner)
            print(logo)
        elif x=="16":
            os.system("clear")
            print(banner)
            print(logo)
            print("script by BLINKING-IDIOT")
            print("Insta : @a.r.n_beatzzzz")
            print("thanks for using this tool!")
            print("please give a star to this tool!")
        elif x=="99":
            exit()
        elif x=="17":
            os.system("clear")
            print(banner)
            print(logo)
            print("make sure android debugging is on in your mobile")
            xy = os.popen("adb shell getprop ro.build.version.release").read()
            print(f"{r}check your phone! sometimes there will be a permisson to allow!")
            print(f"{r}enter always allow this computer and give permission")
            print(f"{g}now try agian")
            input("press enter to continue")
            del xy
            os.system("clear")
            print(banner)
            print(logo)
        else:
            os.system("clear")
            print(banner)
            print(logo)
            print("not a tool...retry")
def main():
    while True:
        print(f"\n{g}[{r}!{g}]{r} this tools is for educational purpose only\n")
        print(f"{g}[{r}!{g}]{r} i am not responsible for any damage caused by using this tool!{g}\n")
        x=input("Is your mobile connected with ADB?[y/n]")
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
            print("wrong input!,try agian")
    
    
main()
