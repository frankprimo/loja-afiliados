
from datetime import datetime
from zoneinfo import ZoneInfo

# HISTÓRIAS DA SEMANA
# 0 = Domingo | 6 = Sábado

historias_semana = {
    0: """Descansar também faz parte do caminho. Nem todos os dias são de corrida — alguns dias são simplesmente para respirar, recarregar e agradecer. Isso não é parar. É se preparar para ir mais longe. 🌙""",

    1: """Comece devagar, mas não pare. Um pequeno passo já é suficiente para hoje. O importante é não perder de vista para onde você quer ir. O resto vem com o tempo. 🌅""",

    2: """Se hoje não saiu como planejou, respire. Amanhã traz uma nova chance. O ontem já ensinou, o hoje está acontecendo e o amanhã ainda é seu para construir. ✨""",

    3: """Você é mais forte do que os desafios que enfrenta. Cada dificuldade superada é uma lição que te torna melhor do que era ontem. Confie no seu processo. 💪""",

    4: """Não se compare com ninguém. Seu tempo não precisa ser igual ao de outra pessoa. Floresça no seu ritmo. O importante é que você esteja progredindo, mesmo que devagar. 🌸""",

    5: """Olhe para trás com gratidão, para frente com esperança. Você já chegou até aqui — isso prova que é capaz. Confie no que ainda está por vir. O melhor está a caminho. 🌟""",

    6: """O descanso de hoje é a força de amanhã. Permita-se parar um instante. Cuide de sua mente e de seu coração. Você merece paz e tranquilidade. Amanhã recomeça com mais clareza. 💛"""
}


def obter_historia_do_dia():

    hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))

    dia_semana = (hoje.weekday() + 1) % 7

    dias_semana = [
        "Domingo",
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado"
    ]

    return {
        "dia": dias_semana[dia_semana],
        "data": hoje.strftime("%d/%m/%Y"),
        "mensagem": historias_semana[dia_semana].strip()
    }
