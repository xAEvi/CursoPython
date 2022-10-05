from Vehiculo import Vehiculo
import pickle

def main():
    auto = Vehiculo("Chevrolet", 4, 50)
    f = open('auto.bin', 'wb')
    pickle.dump(auto, f)
    f.close()

    r = open ('auto.bin', 'rb')
    auto2 = pickle.load(r)
    print(auto2)


if __name__ == "__main__":
    main()