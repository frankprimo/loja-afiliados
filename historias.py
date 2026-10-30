
from datetime import datetime
from zoneinfo import ZoneInfo

# ==================================================
# HISTÓRIAS DA SEMANA
# Objetivo: motivar, criar relacionamento com visitantes
# e incentivar a descoberta de ofertas da loja.
# 0 = Domingo | 6 = Sábado
# ==================================================

historias_semana = {

    0: """Domingo é dia de respirar, agradecer e renovar as energias. Aproveite este momento para cuidar de você e planejar uma nova semana. E, se estiver procurando algo para facilitar sua rotina ou realizar um desejo, conheça as ofertas selecionadas em nossa Loja de Ofertas Afiliadas. Cada nova semana traz novas possibilidades! 🌙🛍️""",

    1: """Uma nova semana começa com novas oportunidades! Dê um passo de cada vez, mantenha seus objetivos e não desista dos seus planos. Aproveite também para conhecer nossas seleções de produtos na Shopee, Mercado Livre, Amazon, Temu e Hotmart. Talvez aquela solução ou oportunidade que você procura esteja entre nossas ofertas! 🌅🛒""",

    2: """Nem tudo precisa acontecer de uma vez. Pequenas escolhas podem fazer diferença no seu dia. Pesquise, compare e escolha com consciência aquilo que realmente precisa. Nossa loja reúne ofertas e produtos de diferentes plataformas para ajudar você a descobrir novas possibilidades. ✨🛍️""",

    3: """Você é mais forte do que os desafios que enfrenta. Continue construindo seus objetivos com dedicação e confiança. E lembre-se: boas escolhas também fazem parte de uma vida mais organizada. Visite nossas vitrines e descubra produtos que podem ajudar no seu dia a dia. 💪🛒""",

    4: """Cada pessoa tem seu próprio ritmo, seus sonhos e suas prioridades. Não se compare: valorize suas conquistas e faça escolhas que combinem com sua realidade. Na Loja de Ofertas Afiliadas, você encontra seleções de produtos de diferentes lojas para pesquisar e escolher com tranquilidade. 🌸🛍️""",

    5: """Sexta-feira chegou! Olhe para trás com gratidão e para frente com esperança. Que seu dia seja cheio de boas notícias e boas oportunidades. Antes de comprar, aproveite para conhecer nossas ofertas, comparar opções e encontrar produtos que façam sentido para você. 🌟🛒""",

    6: """O sábado é uma oportunidade para aproveitar a vida, cuidar da casa, da família e de você. Se estiver procurando algo especial ou útil para sua rotina, visite nossas vitrines e descubra as seleções de produtos disponíveis. Que seu dia seja leve, feliz e cheio de boas escolhas! 💛🛍️"""
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
