"""app registor de productos"""
class Diccionario:
    def __init__(self) -> None:
        self.dic={}
        self.menu()
        

    def menu(self):
        print("1-Carga de Productos")
        print("2-Impresion de Productos")
        print("3-Consulta de Productos")
        print("4-Finalizar")
        op=int(input("Elija una opcion: "))

        match op:
            case 1:
                self.ingresar()
            case 2:
                self.imprimir()
            case 3:
                self.consulta()
            case 4:
                self.fin()


    def fin(self):
        print("****Hasta pronto****")


    def ingresar(self):
        self.cont="s"
        while self.cont=="s":
            self.nombre=input("Ingresa nombre producto: ")
            self.precio=int(input("Ingresa Valor: "))
            self.dic[self.nombre]=self.precio
            self.cont=input("Deseas seguir s/n: ")
        self.menu()

    def imprimir(self):
        print(self.dic)
        for nombre in self.dic:
            print(f"{nombre} ${self.dic[nombre]}")

        op=input("Volver al menu s/n: ")
        if op =="s":
            self.menu()
        else:
            self.fin()
        

    def consulta(self):
        cont="s"
        while cont =="s":        
            self.buscar=input("Ingrese producto a buscar: ")
            if self.buscar in self.dic:
                print("encontrado")
                print(f"{self.buscar} {self.dic[self.buscar]}")
            else:
                print("No tiene stock")

            cont=input("Desa seguir s/n: ")
        self.menu()


op=Diccionario()
