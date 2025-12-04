import pytest
from club import Club
from socio import Socio
from pleno import Pleno
from verano import Verano
from disciplina import Disciplina
from datetime import datetime

def test_constructor_club():
    club = Club("socios.csv")
    assert club is not None
    assert len(club.socios) == 9

def test_constructor_archivo_inexistente():
    with pytest.raises(FileNotFoundError):
        Club("archivo_inexistente.csv")

def test_cantidad_socios():
    club = Club("socios.csv")
    assert club.cantidad_socios() == 9

def test_pleno_sin_adicionales():
    pleno = Pleno(1001, "Juan Pérez", 0, True)
    assert pleno.calcular_cuota_mensual() == 40000

def test_pleno_con_2_adicionales():
    pleno = Pleno(1001, "Juan Pérez", 2, True)
    assert pleno.calcular_cuota_mensual() == 100000

def test_pleno_con_4_adicionales():
    pleno = Pleno(1002, "María González", 4, True)
    assert pleno.calcular_cuota_mensual() == 160000

def test_verano_sin_pileta():
    verano = Verano(2002, "Luis Fernández", 2, True, False)
    # 25000 * (1 + 2) = 75000
    assert verano.calcular_cuota_mensual() == 75000

def test_verano_con_pileta_en_verano():
    # Este test depende del mes actual
    verano = Verano(2001, "Ana Martínez", 3, True, True)
    mes_actual = datetime.now().month
    es_verano = mes_actual in [12, 1, 2, 3]
    # 25000 * (1 + 3) = 100000
    if es_verano:
        assert verano.calcular_cuota_mensual() == 140000  # 100000 * 1.40
    else:
        assert verano.calcular_cuota_mensual() == 100000

def test_disciplina_2_integrantes_3_disciplinas():
    disciplina = Disciplina(3001, "Pedro Ramírez", 2, True, 3)
    # 10000 * (1 + 2) + 6000 * 3 = 30000 + 18000 = 48000
    assert disciplina.calcular_cuota_mensual() == 48000

def test_disciplina_5_integrantes_2_disciplinas():
    disciplina = Disciplina(3002, "Sofía Torres", 5, True, 2)
    # 10000 * (1 + 5) + 6000 * 2 = 60000 + 12000 = 72000
    assert disciplina.calcular_cuota_mensual() == 72000

def test_disciplina_0_integrantes_4_disciplinas():
    disciplina = Disciplina(3003, "Diego López", 0, False, 4)
    # 10000 * (1 + 0) + 6000 * 4 = 10000 + 24000 = 34000
    assert disciplina.calcular_cuota_mensual() == 34000

def test_porcentaje_activos():
    club = Club("socios.csv")
    porcentaje = club.porcentaje_activos()
    # 6 activos de 9 total = 66.666...
    assert abs(porcentaje - 66.66666666666666) < 0.01

def test_recaudacion_mes_actual():
    club = Club("socios.csv")
    recaudacion = club.recaudacion_mes_actual()
    # Socios activos:
    # 1001: Pleno 2 adic = 100000
    # 1002: Pleno 4 adic = 160000
    # 2001: Verano 3 adic, pileta = 100000 (sin verano) o 140000 (con verano)
    # 2002: Verano 2 adic, sin pileta = 75000
    # 3001: Disciplina 2 adic, 3 disc = 48000
    # 3002: Disciplina 5 adic, 2 disc = 72000
    mes_actual = datetime.now().month
    es_verano = mes_actual in [12, 1, 2, 3]
    if es_verano:
        assert recaudacion == 595000  # 100000 + 160000 + 140000 + 75000 + 48000 + 72000
    else:
        assert recaudacion == 555000  # 100000 + 160000 + 100000 + 75000 + 48000 + 72000

def test_recaudacion_por_tipo_inactivos():
    club = Club("socios.csv")
    recaudacion = club.recaudacion_por_tipo_inactivos()
    # Socios inactivos:
    # 1003: Pleno 1 adic = 70000
    # 2003: Verano 1 adic, pileta = 50000 (sin verano) o 70000 (con verano)
    # 3003: Disciplina 0 adic, 4 disc = 34000
    mes_actual = datetime.now().month
    es_verano = mes_actual in [12, 1, 2, 3]
    if es_verano:
        assert recaudacion == {"Pleno": 70000, "Verano": 70000, "Disciplina": 34000}
    else:
        assert recaudacion == {"Pleno": 70000, "Verano": 50000, "Disciplina": 34000}

def test_socio_activo_que_mas_paga():
    club = Club("socios.csv")
    socio_max = club.socio_activo_que_mas_paga()
    assert socio_max.numero_socio == 1002
    assert socio_max.nombre_titular == "María González"
    assert socio_max.calcular_cuota_mensual() == 160000

def test_cantidad_activos_grupo_familiar_mas_3():
    club = Club("socios.csv")
    cantidad = club.cantidad_activos_grupo_familiar_mas_3()
    # Activos con más de 3 integrantes adicionales: 1002 (4 adic), 3002 (5 adic)
    assert cantidad == 2

def test_herencia_socios():
    assert issubclass(Pleno, Socio)
    assert issubclass(Verano, Socio)
    assert issubclass(Disciplina, Socio)

def test_composicion_club_socios():
    club = Club("socios.csv")
    assert hasattr(club, 'socios')
    for socio in club.socios:
        assert isinstance(socio, Socio)

def test_atributos_pleno():
    pleno = Pleno(1001, "Juan Pérez", 2, True)
    assert pleno.tipo == 1
    assert pleno.numero_socio == 1001
    assert pleno.nombre_titular == "Juan Pérez"
    assert pleno.integrantes_adicionales == 2
    assert pleno.activo == True

def test_atributos_verano():
    verano = Verano(2001, "Ana Martínez", 3, True, True)
    assert verano.tipo == 2
    assert verano.usa_pileta == True

def test_atributos_disciplina():
    disciplina = Disciplina(3001, "Pedro Ramírez", 2, True, 3)
    assert disciplina.tipo == 3
    assert disciplina.cantidad_disciplinas == 3

def test_nombre_tipo_socios():
    pleno = Pleno(1001, "Juan Pérez", 2, True)
    verano = Verano(2001, "Ana Martínez", 3, True, True)
    disciplina = Disciplina(3001, "Pedro Ramírez", 2, True, 3)
    assert pleno.nombre_tipo == "Pleno"
    assert verano.nombre_tipo == "Verano"
    assert disciplina.nombre_tipo == "Disciplina"
