
import socket
import threading
import geocoder
import json


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)

m = {"lp": "3", "in_danger": True,"helmet_in": False,"latitude":0,"longitude":0} # a real dict.



def send_stat_on_req(helmet_in):
    global m,dataj
    while True:
        try:
            conn, addr = serv.accept()
            data = conn.recv(4096)

            g = geocoder.ip('me')
            m['latitude'],m['longitude'] = g.latlng[0],g.latlng[1]
            m['helmet_in'] = m['helmet_in']
            m['in_danger'] = m['in_danger']
            if bytes("100",'utf-8')==data:
                dataj = json.dumps(m)
                conn.send(bytes(dataj,'utf-8'))






            if(m['in_danger']):
                conn.send(bytes(dataj,'utf-8'))



        except KeyboardInterrupt:   
            conn.close()


helmet_in = True
t1 = threading.Thread(target=send_stat_on_req, args=(helmet_in,))
t1.start()
####################################################



i = 0
while 1:
    print(f"\rClient doing client shit {i}",end='')
    i+=1