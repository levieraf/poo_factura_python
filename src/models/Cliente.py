class Cliente:
    def __init__(self, **atributos):
        self.__nombre = atributos['nombre']
        self.__email = atributos['email']

    def get_nombre(self):
        return self.__nombre + ".."
    
    def get_email(self):
        return self.__email

