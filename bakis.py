import time, socket, pprint, os
from rdflib import Graph, Namespace, RDF, RDFS, OWL

class attack_detector:
    def __init__(self):
        self.identify

class attack_detection_pt:
    def __init__(self, name, attack_type, charecteristics, affected_area):
        self.name = name
        self.attack_type = attack_type
        self.charecteristics = charecteristics
        self.affected_area = affected_area
        pass

class attack_prevention_pt:
    def __init__(self, name, problem, goal, affected_area, limitations, steps, executable_commands):
        self.name = name
        self.problem = problem
        self.goal = goal
        self.affected_area = affected_area
        self.limitations = limitations
        self.steps = steps
        self.executable_commands = executable_commands
        pass



def test_con():
    aaaa = attack_detection_pt("DOS", "Impact", "", "")
    print(aaaa.name)
    spoon = socket.socket()
    port = 80
    spoon.bind(('', port))
    spoon.listen(5)
    curr = time.time()
    print(curr)

    while True:
        connection, address = spoon.accept()
        print(time.time()-curr)
        curr = time.time()
        print ('Got connection from', address)
        connection.send('Thank you for connecting'.encode())
        print(time.time()-curr)
        curr = time.time()
        connection.close()
        print(time.time()-curr)



def test_rdflib():
    g = Graph()
    # g.parse("http://www.w3.org/People/Berners-Lee/card")
    g.parse("patternOntology.ttl")
    # print(g.serialize(format="turtle"))
    print(len(g))
    # print(len(g))
    # OWL.Class()

    # EX = Namespace("http://example.org/security#")
    # Get all OWL classes
    # for s in g.subjects(RDF.type, OWL.Class):
    #     print(s)


    # for cls in g.subjects(RDF.type, OWL.Class):
    #     label = g.value(cls, RDFS.label)
    #     print(cls, label)


    # from owlready2 import *   
    # onto = get_ontology("ontology.ttl").load()
    # for cls in onto.classes():
    #     print(cls)
    # # Use as Python class
    # Person = onto.Person
    # p = Person()

    for row in g:
        pprint.pprint(row)
    return



def test_random():
    apple = """for i in range(0,5):
        print(i)"""
    exec(apple)
    return



def test_socket():
    host = '192.168.0.175'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, 5005))
    while True:
        # Receive data from the socket
        data, addr = sock.recvfrom(1024)
        print(f'Received packet from {addr}: {data.decode('utf-8')}')

    # sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    # print(sniffer.recvfrom(65565))
    # sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    # socket


def udp_send():
    udp_ip = '192.168.0.134'
    udp_port = 5005

    message = 'Hello UDP!!!!!!!!'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        for i in range(0,3):
            sock.sendto(message.encode(), (udp_ip, udp_port))
            print(f'Sent UDP packet to {udp_ip}:{udp_port}:{message}')
            time.sleep(1)
    finally:
        sock.close()



def main():
    # while True:
        # test_con()
        # test_rdflib()
        # test_random()
        # test_socket()
    udp_send()



if __name__ == '__main__':
    main()