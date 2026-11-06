
from datetime import datetime
from zoneinfo import ZoneInfo
import calendar

# ==========================================================
# FP DIGITAL / LOJA DE OFERTAS AFILIADAS
# CALENDÁRIO MENSAL DE MENSAGENS DIÁRIAS
#
# 1 a 31 = dias do mês
# Fevereiro: 28 ou 29 mensagens, conforme o ano.
# Seleção automática pelo calendário de São Paulo.
# ==========================================================

mensagens_mensais = {

    1: {
        "tema": "Começar com Coragem",
        "versiculo": "Seja forte e corajoso. Não tenha medo, pois Deus estará com você.",
        "referencia": "Josué 1:9",
        "mensagem": "Não importa o quão devagar você vá, desde que não pare. Cada passo, por menor que pareça, leva você mais perto dos seus objetivos. Comece este novo mês com fé, coragem e confiança. Deus está com você.",
        "direito": "Todo consumidor tem direito a informações claras sobre preços, características, qualidade e condições dos produtos. Antes de comprar, saiba exatamente o que está adquirindo. (Art. 6º, III, CDC)"
    },

    2: {
        "tema": "Agradecer é Crescer",
        "versiculo": "Deem graças em todas as circunstâncias.",
        "referencia": "1 Tessalonicenses 5:18",
        "mensagem": "Conte suas bênçãos, não apenas seus problemas. Quando reconhecemos aquilo que já recebemos, o coração encontra motivos para seguir em frente. Hoje, comece e termine o dia com gratidão.",
        "direito": "Nas compras realizadas pela internet ou fora do estabelecimento comercial, o consumidor pode exercer o direito de arrependimento em até 7 dias, conforme as condições do artigo 49 do CDC."
    },

    3: {
        "tema": "Sua Persistência Vale",
        "versiculo": "Não nos cansemos de fazer o bem, pois no tempo certo colheremos.",
        "referencia": "Gálatas 6:9",
        "mensagem": "Grandes conquistas exigem paciência, dedicação e perseverança. Nem todos os resultados aparecem imediatamente. Continue fazendo sua parte e confie que cada esforço pode construir um futuro melhor.",
        "direito": "Produtos duráveis, como eletrodomésticos e celulares, possuem prazo legal de 90 dias para reclamação de vícios aparentes ou de fácil constatação. Para produtos não duráveis, o prazo é de 30 dias. (Art. 26, CDC)"
    },

    4: {
        "tema": "Deus Cuida dos Detalhes",
        "versiculo": "Não andem ansiosos por coisa alguma; apresentem seus pedidos a Deus.",
        "referencia": "Filipenses 4:6",
        "mensagem": "Não permita que a ansiedade roube a tranquilidade do seu dia. Faça sua parte, valorize os pequenos passos e entregue a Deus aquilo que está fora do seu controle.",
        "direito": "O preço informado na oferta deve ser respeitado. Se o fornecedor não cumprir a oferta, o consumidor pode exigir seu cumprimento, aceitar produto ou serviço equivalente ou rescindir o contrato, conforme o caso. (Arts. 30 e 35, CDC)"
    },

    5: {
        "tema": "Deus Te Fortalece",
        "versiculo": "O Senhor é a minha força e o meu escudo.",
        "referencia": "Salmos 28:7",
        "mensagem": "Mesmo quando o caminho parece difícil, não perca a esperança. Você não precisa resolver tudo de uma vez. Respire, mantenha a fé e avance um dia de cada vez.",
        "direito": "A publicidade deve ser apresentada de forma que o consumidor consiga identificá-la facilmente. Informações falsas ou capazes de induzir ao erro são proibidas. (Arts. 36 e 37, CDC)"
    },

    6: {
        "tema": "O Poder de Recomeçar",
        "versiculo": "As misericórdias do Senhor se renovam a cada manhã.",
        "referencia": "Lamentações 3:22-23",
        "mensagem": "Não deixe que os erros de ontem determinem seu amanhã. Cada amanhecer traz uma nova oportunidade para aprender, melhorar e construir uma história diferente.",
        "direito": "Antes de concluir uma compra pela internet, verifique a identificação do fornecedor, endereço, características do produto, preço total e condições de entrega. (Decreto nº 7.962/2013)"
    },

    7: {
        "tema": "A Fé Abre Caminhos",
        "versiculo": "Tudo posso naquele que me fortalece.",
        "referencia": "Filipenses 4:13",
        "mensagem": "Acredite na força que nasce da fé. Os desafios podem ser grandes, mas não precisam ser maiores do que sua determinação de continuar. Tenha esperança e siga em frente.",
        "direito": "O consumidor tem direito de receber informações sobre os riscos que produtos e serviços podem oferecer à sua saúde e segurança. (Art. 6º, I, CDC)"
    },

    8: {
        "tema": "Confie no Tempo de Deus",
        "versiculo": "Tudo tem o seu tempo determinado.",
        "referencia": "Eclesiastes 3:1",
        "mensagem": "Nem tudo acontece na hora que desejamos. Algumas conquistas precisam de preparo, paciência e maturidade. Continue caminhando e respeite o tempo de cada etapa.",
        "direito": "Nas compras pela internet, o fornecedor deve apresentar informações claras sobre prazo, forma e condições de entrega. Guarde a confirmação do pedido e os comprovantes da compra. (Decreto nº 7.962/2013)"
    },

    9: {
        "tema": "A Esperança Não Desiste",
        "versiculo": "Alegrem-se na esperança, sejam pacientes na tribulação.",
        "referencia": "Romanos 12:12",
        "mensagem": "Mesmo nos dias difíceis, sempre existe um motivo para continuar. Não permita que um momento complicado apague todos os sonhos que você ainda pode realizar.",
        "direito": "Se o fornecedor não cumprir a oferta, o consumidor pode escolher uma das alternativas previstas no artigo 35 do CDC, conforme a situação."
    },

    10: {
        "tema": "Gratidão Transforma o Dia",
        "versiculo": "Em tudo dai graças.",
        "referencia": "1 Tessalonicenses 5:18",
        "mensagem": "A gratidão nos ensina a perceber a beleza das pequenas coisas. Valorize quem está ao seu lado, reconheça suas conquistas e encontre alegria nas oportunidades de hoje.",
        "direito": "O consumidor tem direito à proteção contra métodos comerciais coercitivos ou desleais e práticas abusivas. (Art. 6º, IV, CDC)"
    },

    11: {
        "tema": "Você Não Está Sozinho",
        "versiculo": "O Senhor é o meu pastor; nada me faltará.",
        "referencia": "Salmos 23:1",
        "mensagem": "Existem momentos em que precisamos de força para continuar. Lembre-se de que a fé pode renovar sua esperança e trazer serenidade para enfrentar cada desafio.",
        "direito": "O fornecedor não pode condicionar a venda de um produto à aquisição de outro, salvo situações permitidas por lei. A venda casada é uma prática abusiva. (Art. 39, I, CDC)"
    },

    12: {
        "tema": "Pequenos Passos, Grandes Conquistas",
        "versiculo": "Quem é fiel no pouco também é fiel no muito.",
        "referencia": "Lucas 16:10",
        "mensagem": "Não despreze os pequenos avanços. Uma atitude positiva, uma decisão consciente e um esforço diário podem transformar sua caminhada.",
        "direito": "O consumidor tem direito à proteção contra cláusulas contratuais abusivas e pode questionar disposições que estabeleçam obrigações desproporcionais. (Art. 51, CDC)"
    },

    13: {
        "tema": "A Paz Começa Dentro de Você",
        "versiculo": "Deixo-lhes a paz; a minha paz lhes dou.",
        "referencia": "João 14:27",
        "mensagem": "Não permita que a correria do mundo tire sua paz. Reserve um momento para respirar, agradecer e colocar seus pensamentos em ordem. A tranquilidade também é uma conquista.",
        "direito": "O consumidor deve receber informação prévia sobre juros, encargos, número de parcelas e valor total de compras a prazo. (Art. 52, CDC)"
    },

    14: {
        "tema": "Acredite na Sua Caminhada",
        "versiculo": "O Senhor firma os passos de quem nele se agrada.",
        "referencia": "Salmos 37:23",
        "mensagem": "Cada pessoa tem sua própria jornada. Não compare seu começo com a conquista de outra pessoa. Continue aprendendo e construindo seu caminho com dedicação.",
        "direito": "Produtos e serviços devem apresentar informações corretas, claras e ostensivas sobre suas características, composição, quantidade e preço. (Art. 31, CDC)"
    },

    15: {
        "tema": "Metade do Caminho, Novas Possibilidades",
        "versiculo": "Entregue o seu caminho ao Senhor; confie nele.",
        "referencia": "Salmos 37:5",
        "mensagem": "Chegar até aqui já representa uma caminhada de experiências e aprendizados. Faça uma pausa, reconheça suas conquistas e renove seus objetivos para os próximos dias.",
        "direito": "O consumidor tem direito de acessar seus dados pessoais e solicitar correção de informações incompletas ou desatualizadas, conforme as regras da LGPD."
    },

    16: {
        "tema": "A Força de Continuar",
        "versiculo": "Aqueles que esperam no Senhor renovam suas forças.",
        "referencia": "Isaías 40:31",
        "mensagem": "Quando o cansaço aparecer, lembre-se do motivo pelo qual você começou. Descanse quando necessário, recupere suas forças e continue acreditando no que deseja construir.",
        "direito": "Se um produto apresentar defeito, o fornecedor deve ter a oportunidade legal de solucionar o problema, em regra no prazo de até 30 dias. Depois disso, podem valer as alternativas do artigo 18 do CDC."
    },

    17: {
        "tema": "Escolhas Conscientes",
        "versiculo": "Tudo o que fizerem, façam de todo o coração.",
        "referencia": "Colossenses 3:23",
        "mensagem": "A qualidade da nossa caminhada também depende das escolhas que fazemos. Pense antes de agir, valorize suas prioridades e escolha aquilo que contribui para seu bem-estar.",
        "direito": "Antes de comprar, compare preços, condições de pagamento e características dos produtos. O consumidor tem direito à liberdade de escolha e à informação adequada. (Art. 6º, II e III, CDC)"
    },

    18: {
        "tema": "Deus Renova Suas Forças",
        "versiculo": "O meu socorro vem do Senhor.",
        "referencia": "Salmos 121:2",
        "mensagem": "Mesmo quando não enxergamos todas as respostas, podemos encontrar força para continuar. Tenha fé, mantenha a esperança e não abandone seus sonhos.",
        "direito": "O consumidor não pode ser obrigado a pagar por um serviço que não solicitou. Serviços não solicitados podem ser considerados práticas abusivas. (Art. 39, III, CDC)"
    },

    19: {
        "tema": "A Bondade Faz a Diferença",
        "versiculo": "Sejam bondosos e compassivos uns para com os outros.",
        "referencia": "Efésios 4:32",
        "mensagem": "Uma palavra de carinho pode transformar um dia. Compartilhe respeito, pratique a gentileza e lembre-se de que pequenas atitudes podem produzir grandes mudanças.",
        "direito": "O consumidor tem direito à prevenção e reparação de danos patrimoniais e morais, individuais, coletivos ou difusos, conforme a legislação. (Art. 6º, VI, CDC)"
    },

    20: {
        "tema": "Não Perca a Esperança",
        "versiculo": "A esperança não nos decepciona.",
        "referencia": "Romanos 5:5",
        "mensagem": "Nem todos os dias serão fáceis, mas todos podem trazer algum aprendizado. Continue com fé, paciência e disposição para fazer o melhor possível.",
        "direito": "Em contratos de consumo, as condições devem ser apresentadas de forma clara. O consumidor deve ter oportunidade de conhecer o conteúdo antes de assumir obrigações. (Art. 46, CDC)"
    },

    21: {
        "tema": "A Sabedoria nas Decisões",
        "versiculo": "Se alguém tem falta de sabedoria, peça-a a Deus.",
        "referencia": "Tiago 1:5",
        "mensagem": "Nem sempre a melhor decisão é a mais rápida. Pense, avalie as possibilidades e escolha com responsabilidade. A sabedoria está também em saber esperar.",
        "direito": "O consumidor pode solicitar informações sobre o preço total, encargos e condições de crédito antes de contratar. Leia as condições com atenção. (Art. 52, CDC)"
    },

    22: {
        "tema": "O Amor Está nas Pequenas Atitudes",
        "versiculo": "Acima de tudo, revistam-se do amor.",
        "referencia": "Colossenses 3:14",
        "mensagem": "A vida ganha mais significado quando colocamos amor em nossas atitudes. Cuide das pessoas, valorize sua família e faça o bem sempre que puder.",
        "direito": "O consumidor tem direito à reparação de danos causados por produtos ou serviços defeituosos, observadas as regras e condições previstas no CDC. (Arts. 12, 14 e 18)"
    },

    23: {
        "tema": "Acredite em Dias Melhores",
        "versiculo": "Este é o dia que o Senhor fez; alegremo-nos nele.",
        "referencia": "Salmos 118:24",
        "mensagem": "Não deixe que as dificuldades de hoje impeçam você de acreditar no amanhã. Existem novas oportunidades esperando por quem continua caminhando com esperança.",
        "direito": "A cobrança de dívidas deve respeitar a dignidade do consumidor. Ele não pode ser exposto ao ridículo nem submetido a constrangimento ou ameaça. (Art. 42, CDC)"
    },

    24: {
        "tema": "A Fé Também é Coragem",
        "versiculo": "Não temas, porque eu sou contigo.",
        "referencia": "Isaías 41:10",
        "mensagem": "Coragem não significa ausência de medo, mas disposição para seguir mesmo diante das incertezas. Confie em Deus e faça sua parte com determinação.",
        "direito": "Nas compras pela internet, o fornecedor deve disponibilizar atendimento adequado para dúvidas, reclamações, suspensão ou cancelamento de contratos. (Decreto nº 7.962/2013)"
    },

    25: {
        "tema": "Valorize Suas Conquistas",
        "versiculo": "Combati o bom combate, terminei a corrida, guardei a fé.",
        "referencia": "2 Timóteo 4:7",
        "mensagem": "Olhe para sua trajetória com carinho. Você enfrentou desafios, aprendeu e chegou até aqui. Reconheça suas conquistas e continue preparando novos sonhos.",
        "direito": "O consumidor tem direito de receber nota fiscal ou documento equivalente nas operações de compra, conforme as obrigações legais do fornecedor."
    },

    26: {
        "tema": "A Generosidade Transforma",
        "versiculo": "Há maior felicidade em dar do que em receber.",
        "referencia": "Atos 20:35",
        "mensagem": "Compartilhar conhecimento, carinho e atenção é uma forma de tornar o mundo melhor. Nunca subestime o poder de uma boa atitude.",
        "direito": "O consumidor pode registrar reclamações junto aos órgãos de defesa do consumidor, como o Procon, quando seus direitos forem desrespeitados."
    },

    27: {
        "tema": "Renove Seus Sonhos",
        "versiculo": "Esqueçam o que se foi; eis que faço uma coisa nova.",
        "referencia": "Isaías 43:18-19",
        "mensagem": "Não tenha medo de recomeçar. Seus sonhos podem ganhar novos caminhos e novas formas. Mantenha a fé e esteja aberto às oportunidades que surgirem.",
        "direito": "O fornecedor deve cumprir as condições anunciadas em sua oferta. Guarde anúncios, mensagens, comprovantes e registros que possam ajudar a demonstrar o que foi prometido. (Arts. 30 e 35, CDC)"
    },

    28: {
        "tema": "Agradeça Pela Jornada",
        "versiculo": "O Senhor tem feito grandes coisas por nós.",
        "referencia": "Salmos 126:3",
        "mensagem": "Cada experiência deixa uma lição. Agradeça pelas conquistas, aprenda com os desafios e mantenha o coração preparado para viver novas oportunidades.",
        "direito": "O consumidor tem direito à informação sobre a origem, características e riscos de produtos e serviços, sempre que essas informações forem exigidas pela legislação. (Arts. 6º e 31, CDC)"
    },

    29: {
        "tema": "Persevere com Fé",
        "versiculo": "Sejam firmes, inabaláveis e sempre abundantes na obra do Senhor.",
        "referencia": "1 Coríntios 15:58",
        "mensagem": "A perseverança transforma planos em conquistas. Continue fazendo o que está ao seu alcance, sem perder a esperança e sem deixar de acreditar em dias melhores.",
        "direito": "Em caso de defeito oculto, que não podia ser identificado no momento da compra, o prazo legal para reclamar começa quando o problema fica evidente, conforme o artigo 26, § 3º, do CDC."
    },

    30: {
        "tema": "O Amanhã Traz Novas Oportunidades",
        "versiculo": "Entregue suas preocupações ao Senhor, e ele o susterá.",
        "referencia": "Salmos 55:22",
        "mensagem": "Quando um ciclo se aproxima do fim, olhe para tudo o que aprendeu. Deixe para trás aquilo que não contribui e prepare o coração para novas possibilidades.",
        "direito": "O consumidor deve receber informações claras sobre as condições de cancelamento, pagamento e eventuais cobranças antes de contratar um serviço. Leia o contrato e guarde uma cópia."
    },

    31: {
        "tema": "Um Novo Ciclo, Uma Nova Esperança",
        "versiculo": "Eis que faço novas todas as coisas.",
        "referencia": "Apocalipse 21:5",
        "mensagem": "Todo encerramento também pode ser o início de algo novo. Agradeça pelo caminho percorrido, renove sua fé e siga com esperança. Que Deus ilumine seus próximos passos.",
        "direito": "Antes de finalizar uma compra, confira o preço total, o prazo de entrega, a identificação do vendedor e as condições de pagamento. Comprar com informação é uma forma de proteger seus direitos."
    }

}


# ==========================================================
# FUNÇÃO PRINCIPAL
# Compatível com a chamada existente no app.py
# ==========================================================

def obter_historia_do_dia():

    hoje = datetime.now(ZoneInfo("America/Sao_Paulo"))

    dia_mes = hoje.day

    dias_semana = [
        "Segunda-feira",
        "Terça-feira",
        "Quarta-feira",
        "Quinta-feira",
        "Sexta-feira",
        "Sábado",
        "Domingo"
    ]

    quantidade_dias = calendar.monthrange(
        hoje.year,
        hoje.month
    )[1]

    historia = mensagens_mensais[dia_mes]

    return {
        "dia": dias_semana[hoje.weekday()],
        "data": hoje.strftime("%d/%m/%Y"),
        "tema": historia["tema"],
        "versiculo": historia["versiculo"],
        "referencia": historia["referencia"],
        "mensagem": historia["mensagem"],
        "direito": historia["direito"],
        "dias_no_mes": quantidade_dias
    }
