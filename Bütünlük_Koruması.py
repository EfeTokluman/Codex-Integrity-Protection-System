import time

krl = 0
krl2 = 0

print("system start")

def codex_butunluk_koruması():
    
    print("Codex Integrity Protection System Activeting.")
    time.sleep(1)

    if(krl == 1):
        print("1 Code Correct")
        time.sleep(1)

        if(krl2 == 2): #check "krl2" is value 2
            print("All Code Correct")
            time.sleep(1)

        else:
            print("Error Codex  Integrity Not Verifide")






krl = 1 #set "krl" to 1 
print("System active.")
time.sleep(1)

if (krl == 2):#You see "krl" is not 2 if is failed
    krl2 = 2

time.sleep(1)

codex_butunluk_koruması()


