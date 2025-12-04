from socio import Socio

class Disciplina(Socio):
    def __init__(self, numero_socio, nombre_titular, integrantes_adicionales, activo, cantidad_disciplinas):
        super().__init__(3, numero_socio, nombre_titular, integrantes_adicionales, activo)
        self.cantidad_disciplinas = cantidad_disciplinas
    
    def calcular_cuota_mensual(self):
        # 10000 por el titular y cada integrante adicional
        total_integrantes = 1 + self.integrantes_adicionales
        cuota_integrantes = total_integrantes * 10000
        
        # 6000 por cada disciplina
        cuota_disciplinas = self.cantidad_disciplinas * 6000
        
        return cuota_integrantes + cuota_disciplinas
    
    @property
    def nombre_tipo(self):
        return "Disciplina"