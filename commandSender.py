from socket import socket, AF_INET, SOCK_DGRAM
from time import sleep



# Veic paketes sagatavošanu un izsūtīšanu, izmantojot UDP protokolu
def udp_send(comm):

    # Nodefinē virtuālās mašīnas ip adresi un pieslegvietas numuru
    udp_ip = '192.168.0.134'
    udp_port = 25565

    # Izveido socket objektu, kas varēs izsūtīt paketes, kur AF_INET norāda, ka adrese ir ip adreses un pieslēgvietas formātā, bet SOCK_DGRAM 
    sock = socket(AF_INET, SOCK_DGRAM)

    # Veic lietotāja ievadītās informācijas izsūtīšanu
    try:
        # for i in range(0,6): #(ATKOMENTĒT DOS UZBRUKUMA SIMULĒŠANAI)
        sock.sendto(comm.encode(), (udp_ip, udp_port))
        print(f'Sūta udp paketi uz {udp_ip}:{udp_port}: {comm}')
            # sleep(0.25) #(ATKOMENTĒT DOS UZBRUKUMA SIMULĒŠANAI)
    finally:
        sock.close()



def main():
    comm = ''

    # Veic bezgalīgu ciklu, lai saņemtu ievadi no lietotāja un padotu to funkcijai, kas izsūta to saņēmejam 
    while True:
        comm = input()

        # Pārbauda, vai nav dota stop komanda, ka sapturētu ciklu un partrauktu programmas darbību
        if comm != 'stop':

            # Padod komandu izsūtīšanas funkcijai
            udp_send(comm)
        else:
            print('Darbs pabeigts')
            break



if __name__ == '__main__':
    main()