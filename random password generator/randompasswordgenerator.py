from base64 import b64encode
from pyfiglet import figlet_format as style

print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")
print("\n\tWelcome here")

#__main__
quit = ""
while(len(quit)==0 or quit[0]=='y' or quit[0]=='Y'):
    pasd = input('\nEnter hint word to generate random password = ')
    
    pasd = pasd.encode()
    #converting string format -> byte format

    pasd = b64encode(pasd)
    #converting byte format -> ascii format

    pasd = pasd.decode()
    #converting ascii format -> string format

    print("Your random password is successfully generated... ", "\U0001F973")
    print("\nGenerated password :- ", pasd)

    quit = input("\nWant to continue ? [Y/n] = ")

    print("\n_.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._.~\"~._")

print()
print( style(" HAVE A NICE DAY CHIEF", font="digital") )
