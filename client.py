# test 1,2,3,4,5,6 = A(1)
# test 2.5,3.75,5,6.25,7.5,8.75 = A(1.25)
# test 1,2,4,8,16,32 = G(2)
# test 1,3,9,27,81 = G(3)
# test 1.111,11.11,111.1,1111,11110,111100 = G(10)

# Importarea bibliotecii socket pentru a crea si conecta socket-ul la server

import socket


def main():
    # cream un socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # conectam socket-ul la adresa IP si portul serverului
    client_socket.connect(("127.0.0.1", 6969))
    # Introducem setul de numere separate prin ','
    setNr = list(map(float, input("Introduceti setul de numere separate prin ',': ").split(',')))
    # Verificam daca lungimea setului de numere este intre 5 si 10
    if len(setNr) < 5 or len(setNr) > 10:
        print("Eroare", "Setul de numere trebuie sa fie intre 5 si 10!")
    else:
        # convertim setul de numere in string pentru a se putea trimite catre server
        setNr_str = ",".join(map(str, setNr))
        # trimitem setul de numere catre server
        client_socket.send(setNr_str.encode())
        # primim raspunsul de la server
        data = client_socket.recv(1024)
        # afisam raspunsul
        print(data.decode())
        # inchidem conexiunea cu serverul
        client_socket.close()

    # Verificam daca acest fisier este cel principal


if __name__ == "__main__":
    main()
