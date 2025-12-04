from socio import Socio

class Pleno(Socio):
    def __init__(self, numero_socio, nombre_titular, integrantes_adicionales, activo):
        super().__init__(1, numero_socio, nombre_titular, integrantes_adicionales, activo)
    
    def calcular_cuota_mensual(self):
        # 40000 fijos + 30000 por cada integrante adicional
        return 40000 + (self.integrantes_adicionales * 30000)
    
    @property
    def nombre_tipo(self):
        return "Pleno"