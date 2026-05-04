from time import time
from socket import socket, AF_INET, SOCK_DGRAM
from rdflib import Graph, URIRef, Namespace
from subprocess import Popen, PIPE, run as subrun, call as subcall



# Nodefinē vārdnīcu, kura uzglabā informāciju par pakešu ierašanās biežumu no noteiktām ip adresēm
ipDict = {}

# Ievāc informāciju par mapju saturu, lai novērotu izmaiņas
start_files_tmp = subrun("ls /tmp", shell=True, capture_output=True, text=True)
start_files_tmp = (start_files_tmp.stdout).split("\n")
        


# Veic novēršanas šablona atrašanu un taja esošo komandu izpildi
def defense_execute(variable, defenseDetect):
    g = Graph()
    try:
        # Iegūs ontoloģiju no .ttl faila un nodefinē sākuma mainīgos
        g.parse('patternOntology.ttl')
        security = Namespace('http://example.org/security#')
        detection_pattern = URIRef(('http://example.org/security#' + defenseDetect))

        # No ontoloģijas ievāc nepieciešamo informāciju
        defensePtr = next(g[detection_pattern: security.PreventedBy])
        defenseCommands = next(g[defensePtr: security.commands])
        defenseSteps = next(g[defensePtr: security.steps])
        defenseName = next(g[defensePtr: security.name])
        
        # Veic izgūto komandu apstradi
        defenseCommands = str(defenseCommands)
        if '<var>' in defenseCommands:
            defenseCommands = defenseCommands.replace('<var>', variable)

        # Izvada informāciju par veiktajām darbibām
        print(f'Tiks veikta {defenseName}, izpildot sekojošos soļus:\n{defenseSteps} \n{defenseCommands}')

        # Paņem no manuāli izveidotā secret.py faila sudo paroli
        from secret import pwd

        # Veic komandas izpildi, kas nodrošina aizsardzību no kiberuzbrukuma
        p = Popen(['sudo', '-S'] + defenseCommands.split(), stdin=PIPE, stderr=PIPE, universal_newlines=True)
        p.communicate(pwd + '\n')[1]
        del pwd

    except:
        print('Kļūda defense_execute funkcijā')
    return



# Veic darbības, kas ir nepiciešamas, lai noteiktu, kad tiek veikts pakalpojumatteices uzbrukums
def DOS_detect(ipaddr):
    
    # Iegūst pēdējos 3 ip adreses ciparus
    ip_lastByte = (ipaddr[0])[10:13]

    # Pārbauda, vai ip adrese ir jau ievietota vārdnīcā vai arī ir pagājušas 2 sekundes kopš ip adreses pievienošanas vai atjaunošanas
    if ip_lastByte not in ipDict or time() - (ipDict[ip_lastByte])[0] > 2:

        # Pa jaunu iestata veco vai pievieno jaunu ip adresi
        ipDict[ip_lastByte] = [time(), 1]
    else:

        # Palielina reižu skaitu, cik daudz no konkrētās ip adreses ir ienākušas paketes 2 sekunžu laikā
        (ipDict[ip_lastByte])[1] += 1

        # Pārbauda, vai ir ienākušas 4 paketes no konkrētas ip adreses 2 sekunžu laikā
        if (ipDict[ip_lastByte])[1] >= 4:
            defense_execute(ipaddr[0], 'endPointDenialOfService')
    return



# Veic nepiciešamās darbības, lai noteiktu, kad tiek veikts datu manipulācijas uzbrukums
def manipulation_detect():
    try:

        # Ievāc informāciju par pašreizējo /tmp un koda faila mapes stāvokli
        current_files_tmp = subrun('ls /tmp', shell=True, capture_output=True, text=True)
        current_files_tmp = (current_files_tmp.stdout).split('\n')

        # Pārbauda vai /tmp mape ir mainījusies
        if start_files_tmp != current_files_tmp:
            print('Izmaiņas /tmp mapē')
            defense_execute('/tmp', 'dataManipulation')
    except:
        print('Kļūda manipulation_detect funkcijā')
    return



# Veic darbības, kas novēro, vai tiek veikts injekcijas uzbrukums
def injection_detect(command):
    if 'wget ' in command:
        defense_execute('','contentInjection')



# Izpilda saņemtās komandas
def execute_bash(addr, command):
    try:
        response = subcall(command, shell=True, )
    except:
        print(f'Komandas izpildes kļūda no {addr}:25565 adreses, lai veiktu {command}')



def main():
    # Nodefinē pakešu saņēmēja ip adresi un pieslēgvietu
    host_ip = '192.168.0.134'
    host_port = 25565

    # Izveido ligzdas objektu un tai iestata norādītās adreses
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((host_ip, host_port))

    # Palaiž ciklu, kas mēģina nepārtraukti atklāt kiberuzbrukumu
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            print(f'Saņēma paketi no {addr}: {data.decode('utf-8')}')
            DOS_detect(addr)
            injection_detect(data.decode('utf-8'))
            execute_bash(addr, data.decode('utf-8'))
            manipulation_detect()
        return
    except:
        print("Kļūda main funkcijā")
        return



if __name__ == '__main__':
    main()