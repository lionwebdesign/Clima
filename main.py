from clima.clima import CLIMA

if __name__ == "__main__":
    clima = CLIMA()
    city = input("Ingrese el nombre de la ciudad: ")
    clima.get_clima(city)
