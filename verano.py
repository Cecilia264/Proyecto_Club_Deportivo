from socio import Socio
from datetime import datetime

class Verano(Socio):
    def __init__(self, numero_socio, nombre_titular, integrantes_adicionales, activo, usa_pileta):
        super().__init__(2, numero_socio, nombre_titular, integrantes_adicionales, activo)
        self.usa_pileta = usa_pileta
    
    def calcular_cuota_mensual(self):
        # Base: 25000 por el titular y cada integrante adicional
        total_integrantes = 1 + self.integrantes_adicionales
        cuota_base = total_integrantes * 25000
        
        # Verificar si es verano (diciembre a marzo)
        mes_actual = datetime.now().month
        es_verano = mes_actual in [12, 1, 2, 3]
        
        if self.usa_pileta and es_verano:
            return cuota_base * 1.40
        else:
            return cuota_base
    
    @property
    def nombre_tipo(self):
        return "Verano"