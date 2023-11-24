import random
import time
premiacion_por_pregunta = {
    1: 100000,
    2: 200000,
    3: 300000,
    4: 500000,
    5: 1000000,  # Seguro 1
    6: 2000000,
    7: 3000000,
    8: 5000000,
    9: 7000000,
    10: 10000000,  # Seguro 2
    11: 12000000,
    12: 20000000,
    13: 50000000,
    14: 100000000,
    15: 300000000
}
preguntas_y_respuestas = {
    1: {"pregunta": "¿Cuál es la capital de Francia?", "respuestas": {"A": "Berlín", "B": "Madrid", "C": "París", "D": "Londres"}, "respuesta_correcta": "C"},
    2: {"pregunta": "¿Cuál es el río más largo del mundo?", "respuestas": {"A": "Amazonas", "B": "Nilo", "C": "Misisipi", "D": "Yangtsé"}, "respuesta_correcta": "A"},
    3: {"pregunta": "¿En qué año se llevó a cabo la Revolución Rusa?", "respuestas": {"A": "1917", "B": "1789", "C": "1945", "D": "1600"}, "respuesta_correcta": "A"},
    4: {"pregunta": "¿Cuál es el componente principal del aire?", "respuestas": {"A": "Nitrógeno", "B": "Oxígeno", "C": "Dióxido de carbono", "D": "Argón"}, "respuesta_correcta": "A"},
    5: {"pregunta": "¿Cuál es el cuarto planeta del sistema solar?", "respuestas": {"A": "Tierra", "B": "Marte", "C": "Júpiter", "D": "Saturno"}, "respuesta_correcta": "B"},
    6: {"pregunta": "¿Quién escribió la obra 'Romeo y Julieta'?", "respuestas": {"A": "William Shakespeare", "B": "Fiodor Dostoievski", "C": "Gabriel García Márquez", "D": "Homer Simpson"}, "respuesta_correcta": "A"},
    7: {"pregunta": "¿Cuál es el planeta más grande del sistema solar?", "respuestas": {"A": "Júpiter", "B": "Marte", "C": "Venus", "D": "Saturno"}, "respuesta_correcta": "A"},
    8: {"pregunta": "¿En qué año se fundó la Organización de las Naciones Unidas (ONU)?", "respuestas": {"A": "1945", "B": "1919", "C": "1960", "D": "1980"}, "respuesta_correcta": "A"},
    9: {"pregunta": "¿Quién fue el primer presidente de Estados Unidos?", "respuestas": {"A": "George Washington", "B": "Thomas Jefferson", "C": "Abraham Lincoln", "D": "John F. Kennedy"}, "respuesta_correcta": "A"},
    10: {"pregunta": "¿Cuál es la capital de Brasil?", "respuestas": {"A": "Bogotá", "B": "Santiago", "C": "Buenos Aires", "D": "Brasilia"}, "respuesta_correcta": "D"},
    11: {"pregunta": "¿Cuál es la capital de Japón?", "respuestas": {"A": "Pekín", "B": "Bangkok", "C": "Seúl", "D": "Tokio"}, "respuesta_correcta": "D"},
    12: {"pregunta": "¿En qué año se inauguró la Torre Eiffel?", "respuestas": {"A": "1889", "B": "1900", "C": "1925", "D": "1850"}, "respuesta_correcta": "A"},
    13: {"pregunta": "¿Cuál es la montaña más alta del mundo?", "respuestas": {"A": "Monte Everest", "B": "K2", "C": "Monte Kilimanjaro", "D": "Aconcagua"}, "respuesta_correcta": "A"},
    14: {"pregunta": "¿Cuál es el océano más grande?", "respuestas": {"A": "Océano Atlántico", "B": "Océano Pacífico", "C": "Océano Índico", "D": "Océano Ártico"}, "respuesta_correcta": "B"},
    15: {"pregunta": "¿Quién pintó la Mona Lisa?", "respuestas": {"A": "Leonardo da Vinci", "B": "Pablo Picasso", "C": "Vincent van Gogh", "D": "Claude Monet"}, "respuesta_correcta": "A"},
}

def seleccionar_participantes():
    participantes = ["Participante 1", "Participante 2"]
    random.shuffle(participantes)
    return participantes

def preguntar_con_comodin(pregunta, opciones, comodines_utilizados):
    if len(comodines_utilizados) >= 3:
        print("Ya has utilizado el máximo de comodines permitidos (3).")
        return False

    comodin = input("Selecciona un comodín: '50/50', 'ayuda_del_publico' o 'llamada_a_amigo' o si no desea seleccione 'no': ").lower()

    if comodin == "50/50":
        opciones_restantes = random.sample(opciones, 2)
        respuesta_correcta = preguntas_y_respuestas[pregunta]["respuesta_correcta"]
        if respuesta_correcta not in opciones_restantes:
            opciones_restantes.pop()
            opciones_restantes.append(respuesta_correcta)

        print(f"Opciones restantes: {opciones_restantes}")
        comodines_utilizados.append("50/50")
    elif comodin == "ayuda_del_publico":
        estadisticas = {"Opción A": 20, "Opción B": 30, "Opción C": 25, "Opción D": 25}
        print("Estadísticas del público:")
        for opcion, porcentaje in estadisticas.items():
            print(f"{opcion}: {porcentaje}%")
        respuesta_publico = input("Selecciona la respuesta según las estadísticas: ").upper()
        print(f"Respuesta seleccionada por el público: {respuesta_publico}")
        comodines_utilizados.append("ayuda_del_publico")
    elif comodin == "llamada_a_amigo":
        print("Llamando a un amigo...")
        time.sleep(5)
        amigo_respuesta = random.choice(opciones)
        print(f"Respuesta de tu amigo: {amigo_respuesta}")
        comodines_utilizados.append("llamada_a_amigo")
    elif comodin == "no":
        return False
    else:
        print("Comodín no válido. Ignorando comodín.")
        return False

def hacer_pregunta(numero_pregunta, premio_actual, seguro_actual):
    pregunta_info = preguntas_y_respuestas.get(numero_pregunta)
    if pregunta_info:
        print(f"\nPregunta {numero_pregunta}: {pregunta_info['pregunta']}")
        opciones = list(pregunta_info['respuestas'].keys())
        random.shuffle(opciones)
        for opcion in opciones:
            print(f"{opcion}: {pregunta_info['respuestas'][opcion]}")

        comodines_utilizados = []
        comodin_utilizado = preguntar_con_comodin(numero_pregunta, opciones, comodines_utilizados)
        respuesta_correcta = pregunta_info['respuesta_correcta']

        return respuesta_correcta, comodin_utilizado
    else:
        print(f"Pregunta {numero_pregunta} no encontrada en la base de datos.")
        return None, False

def jugar_quien_quiere_ser_millonario():
    participantes = seleccionar_participantes()
    try:
        with open("ultimo_dia.txt", "r") as file:
            ultimo_dia = file.read().strip()
            if ultimo_dia not in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
                raise ValueError("Día aleatorio no válido")
    except (FileNotFoundError, ValueError):
        ultimo_dia = random.choice(["lunes", "martes", "miércoles", "jueves", "viernes"])
        with open("ultimo_dia.txt", "w") as file:
            file.write(ultimo_dia)
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    indice_ultimo_dia = dias_semana.index(ultimo_dia)
    siguiente_dia_indice = (indice_ultimo_dia + 1) % len(dias_semana)
    dia_semana_actual = dias_semana[siguiente_dia_indice]
    with open("ultimo_dia.txt", "w") as file:
        file.write(dia_semana_actual)
    for participante in participantes:
        print(f"\n¡Bienvenido, {participante}! Hoy es {dia_semana_actual}.")
        nombre = input("Ingresa tu nombre: ")
        edad = input("Ingresa tu edad: ")
        correo = input("Ingresa tu correo electrónico: ")

        premio_actual = 0
        seguro_actual = None

        for numero_pregunta in range(1, 16):
            respuesta_correcta, comodin_utilizado = hacer_pregunta(numero_pregunta, premio_actual, seguro_actual)
            respuesta_participante = input("Ingresa la letra de tu respuesta: ").upper()

            if respuesta_participante == respuesta_correcta:
                premio_actual += premiacion_por_pregunta[numero_pregunta]
                print(f"¡Correcto! Has ganado {premiacion_por_pregunta[numero_pregunta]:,} pesos.")
                if numero_pregunta == 5 or numero_pregunta == 10:
                    seguro_actual = premio_actual
            else:
                print("Respuesta incorrecta. Fin del juego.")
                if seguro_actual:
                    premio_actual = seguro_actual
                break

            retirarse = input("¿Quieres retirarte con el premio acumulado hasta ahora? (si/no): ").lower()
            if retirarse == "si":
                print(f"\n--- Resultado para {participante} ---")
                print(f"Nombre: {nombre}")
                print(f"Edad: {edad}")
                print(f"Correo electrónico: {correo}")
                print(f"Premio obtenido: {premio_actual:,} pesos")
                return

        print(f"\n--- Resultado para {participante} ---")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Correo electrónico: {correo}")
        print(f"Premio obtenido: {premio_actual:,} pesos")

jugar_quien_quiere_ser_millonario()
