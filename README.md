[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AZ2G2kav)
# Sistema de Gestión de Club Deportivo

Un club deportivo necesita un sistema para gestionar sus socios y calcular la recaudación mensual.

• **Socio Pleno**: paga un importe fijo mensual de $40000 más $30000 por cada integrante adicional del grupo familiar.
• **Socio Verano**: paga $25000 por el titular y por cada integrante adicional. Si va a usar la pileta paga 40% extra en los meses de verano (diciembre a marzo, se sabe si es verano desde la hora del sistema operativo).
• **Socio Disciplina**: paga $10000 por el titular y cada integrante adicional más $6000 por cada disciplina, registrando únicamente el total de disciplinas contratadas.

## Archivo socios.csv:

    • Tipo de socio (1 = pleno, 2 = verano, 3 = disciplina)
    • Número de socio
    • Nombre del titular
    • Cantidad de integrantes adicionales del grupo familiar
    • Activo (True/False)
    • Característica extra (no aplica para pleno, usa_pileta para verano, cantidad_disciplinas para disciplina)

## Funcionalidades:

    1. Cargar socios desde el archivo.
    2. Contar la cantidad de socios existentes.
    3. Calcular el porcentaje de activos sobre el total.
    4. Calcular la sumatoria de recaudación del mes actual, considerando únicamente activos.
    5. Calcular la sumatoria de recaudación por tipo de socio en un diccionario con claves "Pleno", "Verano", "Disciplina", pero sólo incluyendo no activos.
    6. Obtener todos los datos del socio activo que más paga.
    7. Contar la cantidad de socios activos con grupo familiar de más de 3 integrantes.
