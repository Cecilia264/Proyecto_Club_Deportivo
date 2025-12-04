from club import Club

def main():
    try:
        # Crear el club y cargar socios
        club = Club("socios.csv")
        
        print("=== Sistema de Gestión de Club Deportivo ===\n")
        
        # 1. Cantidad de socios
        print(f"1. Cantidad total de socios: {club.cantidad_socios()}")
        
        # 2. Porcentaje de socios activos
        porcentaje = club.porcentaje_activos()
        print(f"2. Porcentaje de socios activos: {porcentaje:.2f}%")
        
        # 3. Recaudación mensual actual
        recaudacion = club.recaudacion_mes_actual()
        print(f"3. Recaudación del mes actual: ${recaudacion:,.2f}")
        
        # 4. Recaudación por tipo (inactivos)
        recaudacion_inactivos = club.recaudacion_por_tipo_inactivos()
        print("\n4. Recaudación de socios inactivos por tipo:")
        for tipo, monto in recaudacion_inactivos.items():
            print(f"   {tipo}: ${monto:,.2f}")
        
        # 5. Socio activo que más paga
        socio_max = club.socio_activo_que_mas_paga()
        if socio_max:
            print(f"\n5. Socio activo que más paga:")
            print(f"   Número: {socio_max.numero_socio}")
            print(f"   Nombre: {socio_max.nombre_titular}")
            print(f"   Tipo: {socio_max.nombre_tipo}")
            print(f"   Cuota mensual: ${socio_max.calcular_cuota_mensual():,.2f}")
        
        # 6. Cantidad de activos con grupo familiar grande
        cantidad_grandes = club.cantidad_activos_grupo_familiar_mas_3()
        print(f"\n6. Socios activos con más de 3 integrantes adicionales: {cantidad_grandes}")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()