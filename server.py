import socket


# Functia care determina daca setul de nr este o progresie aritmetica sau geometrica

def progresie(setNr):
    R = setNr[1] - setNr[0]  # R = ratia pt progresia aritmetica
    Q = setNr[1] / setNr[0]  # Q = ratia pt progresia geometrica
    aritmetica = True
    geometrica = True

    # parcurgem lista, verificand daca este progresie aritmetica sau geometrica
    for i in range(len(setNr) - 1):
        if setNr[i + 1] - setNr[i] != R:
            aritmetica = False
        if setNr[i + 1] / setNr[i] != Q:
            geometrica = False

    # returnam rezultatul
    if aritmetica:
        return "A(" + str((R)) + ")"
    elif geometrica:
        return "G(" + str((Q)) + ")"
    else:
        return "N"


def main():
    # cream un socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # asociem socket-ul cu o adresa IP si un port
    server_socket.bind(("127.0.0.1", 6969))
    # setam server-ul sa asculte conexiuni
    server_socket.listen()
    print("Serverul a pornit!")

    while True:
        # acceptam conexiunea de la client
        client_socket, client_address = server_socket.accept()
        print("S-a conectat clientul:", client_address)
        # primim setul de numere de la client
        data = client_socket.recv(1024)
        # convertim string-ul primit in setul de numere
        setNr = list(map(float, data.decode().split(',')))
        # determinam tipul progresiei
        tipProgresie = progresie(setNr)
        # trimitem rezultatul catre client
        client_socket.send(tipProgresie.encode())
        # inchidem conexiunea cu clientul si a serverului
        client_socket.close()
        server_socket.close()


# Verificam daca acest fisier este rulat direct si daca da, apelam functia main().
if __name__ == "__main__":
    main()
