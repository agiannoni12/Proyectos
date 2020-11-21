import datetime
import os
class Billetera():

    local_path = os.getcwd()

    def __init__(self, nombre, apellido, dineroInicial):
        self.nombre = nombre
        self.apellido = apellido
        self.dineroInicial = dineroInicial
        self.nuevoDinero = dineroInicial
        self.registro = open("/Users/agus/Desktop/Proyectos/Billetera/repo/registroBilletera_{}.txt".format(self.nombre+"_"+ self.apellido), "a")


    def depositarDinero(self, monto):

        self.nuevoDinero += monto
        print("deposito {}, su nuevo dinero disponible es {} ".format(monto, self.nuevoDinero))
        self.registro.write('{}|deposito|{}|pesos\n'.format(datetime.date.today(),monto))

    def retirarDinero(self, monto):

        if monto > self.nuevoDinero:
            print("no cuenta con ese monto en su billetera")
            monto = int(input('ingrese un nuevo monto a retirar'))
            return self.retirarDinero(monto)


        else:
            self.nuevoDinero -= monto
            print("retiro {}, su nuevo dinero disponible es {} ".format(monto, self.nuevoDinero))
            self.registro.write('{}|retiro|{}|pesos\n'.format(datetime.date.today(), monto))
