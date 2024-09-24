import os 

def crear_archivos():
    for i in range(10):
        with open(f"archivo_{i}.txt", "w") as f:
            f.write("Este archivo ha sido creado por un script")

def abrir_ventanas():
    while True:
        os.system("start notepad")

if __name__ == "__main__":
    crear_archivos()
    abrir_ventanas()