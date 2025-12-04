import csv
from pleno import Pleno
from verano import Verano
from disciplina import Disciplina

class Club:
    def __init__(self, archivo_csv):
        self.socios = []
        self.cargar_socios(archivo_csv)
    
    def cargar_socios(self, archivo_csv):
        try:
            with open(archivo_csv, 'r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    # Convertir datos según el tipo
                    tipo = int(fila[0])
                    numero_socio = int(fila[1])
                    nombre_titular = fila[2]
                    integrantes_adicionales = int(fila[3])
                    activo = fila[4].lower() == 'true'
                    
                    if tipo == 1:  # Pleno
                        socio = Pleno(numero_socio, nombre_titular, 
                                    integrantes_adicionales, activo)
                    
                    elif tipo == 2:  # Verano
                        usa_pileta = fila[5].lower() == 'true'
                        socio = Verano(numero_socio, nombre_titular, 
                                     integrantes_adicionales, activo, usa_pileta)
                    
                    elif tipo == 3:  # Disciplina
                        cantidad_disciplinas = int(fila[5])
                        socio = Disciplina(numero_socio, nombre_titular, 
                                         integrantes_adicionales, activo, 
                                         cantidad_disciplinas)
                    
                    self.socios.append(socio)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {archivo_csv}")
    
    def cantidad_socios(self):
        return len(self.socios)
    
    def porcentaje_activos(self):
        if not self.socios:
            return 0
        
        activos = sum(1 for socio in self.socios if socio.activo)
        return (activos / len(self.socios)) * 100
    
    def recaudacion_mes_actual(self):
        total = 0
        for socio in self.socios:
            if socio.activo:
                total += socio.calcular_cuota_mensual()
        return total
    
    def recaudacion_por_tipo_inactivos(self):
        recaudacion = {"Pleno": 0, "Verano": 0, "Disciplina": 0}
        
        for socio in self.socios:
            if not socio.activo:
                recaudacion[socio.nombre_tipo] += socio.calcular_cuota_mensual()
        
        return recaudacion
    
    def socio_activo_que_mas_paga(self):
        socios_activos = [socio for socio in self.socios if socio.activo]
        
        if not socios_activos:
            return None
        
        # Encontrar el socio con mayor cuota
        socio_max = max(socios_activos, key=lambda s: s.calcular_cuota_mensual())
        return socio_max
    
    def cantidad_activos_grupo_familiar_mas_3(self):
        # Contar socios activos con más de 3 integrantes adicionales
        # (titular + adicionales > 4, o sea, adicionales > 3)
        cantidad = 0
        for socio in self.socios:
            if socio.activo and socio.integrantes_adicionales > 3:
                cantidad += 1
        return cantidad