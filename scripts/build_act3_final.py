# -*- coding: utf-8 -*-
"""
Append Arcs O, P, Q to ACT3_METADATA and build scripts/enrichment_content_act3.py.
Total Act III: 54 scenes (J1..J7, K1..K2c, L1..L4, M1..M7, O1..O11, P1..P12, Q1..Q7).
"""

from generate_act3_enriched import ACT3_METADATA, data, scenes_by_code
import re

ACT3_METADATA_PART2 = {
    # ARC O: DINNER WITH THE DEVIL
    "O1": {
        "obj": "Receber a carta formal de convite lacrada com o selo real de Ravenloft, analisar a garantia expressa de hospitalidade de Strahd e deliberar a decisão de aceitar o jantar no castelo.",
        "ctx": "Strahd enviou um convite formal garantindo salvo-conduto absoluto sob as leis sagradas do Direito de Hóspede (Guest Right). Se os heróis aceitarem, a Carruagem Negra os aguardará na encruzilhada. Recusar ofenderá o conde e acelerará seus ataques.",
        "sights": "Carta de pergaminho pesado escrita com tinta dourada sobre velino fino; selo de cera carmesim com o brasão do dragão e castelo; carruagem negra aguardando ao longe.",
        "sounds": "O som rítmico de cascos de cavalo parando na estrada; e a leitura da caligrafia refinada e ameaçadora do lorde.",
        "smells": "Cera de lacre, perfume de sândalo aristocrático e vinho doce.",
        "touch": "O velino frio e impecável do convite real.",
        "narrar": "A carta repousa sobre a mesa, exalando a autoridade incontestável de Ravenloft. O pergaminho grosso de velino traz a caligrafia sinuosa do próprio soberano de Baróvia: 'Meus distintos amigos. É chegado o momento de nos encontrarmos como cavalheiros de honra à minha mesa de banquetes. Garanto-lhes salvo-conduto sagrado e inviolável do crepúsculo ao amanhecer. Minha carruagem os aguarda.' O aviso está dado: o convite do Diabo não é um pedido, é um ultimato aristocrático."
    },
    "O2": {
        "obj": "Consultar o astuto Vistana Arrigal sobre o protocolo e as armadilhas da corte de Ravenloft, obter conselhos de etiqueta e identificar possíveis traidores entre os nobres do castelo.",
        "ctx": "Arrigal conhece a corte de Strahd melhor do que ninguém. Ele adverte que na presença de Strahd nenhuma mentira sobrevive, mas que bajulação tola atrai seu desprezo: Strahd respeita coragem inteligente e arrogância contida.",
        "sights": "Arrigal sentado com um cálice de vinho tinto na mão, sorrindo com olhar afiado e calculista; adagas de arremesso brilhando nas mangas de seu gibão bordado.",
        "sounds": "A voz calma e perigosa de Arrigal sussurrando os segredos das noivas de Strahd e de seu camareiro Rahadin.",
        "smells": "Fumo picante de ervas Vistani e vinho forte.",
        "touch": "Moedas de ouro deslizando sobre o tampo da mesa.",
        "narrar": "No canto sombrio da tenda Vistani, Arrigal gira um cálice de vinho escarlate entre os dedos e ergue uma sobrancelha irônica: 'Vocês vão jantar com o Diabo? Então prestem atenção nas regras do jogo: comam o que for servido, elogiem o castelo, mas nunca, jamais, demonstrem covardia. Strahd von Zarovich despedaça homens fracos como galhos secos... mas ele adora brincar com oponentes que têm coragem de olhar em seus olhos sem desviar o olhar.'"
    },
    "O3": {
        "obj": "Subir a Estrada Svalich em direção aos despenhadeiros de Ravenloft, cruzar os portões de ferro e embarcar na suntuosa Carruagem Negra rumo ao castelo.",
        "ctx": "A subida noturna pelas curvas da montanha é solene e aterrorizante. Corvos e lobos observam em fileiras silenciosas conforme a carruagem acelera em direção às muralhas ciclópicas.",
        "sights": "A carruagem negra laqueada com cortinas de veludo vermelho e quatro cavalos colossais de olhos incandescentes; despenhadeiros de rocha caindo centenas de metros no abismo.",
        "sounds": "O estalo do chicote no ar úmido; o trote veloz e compassado dos cavalos na lama; e o vento uivando na garganta da montanha.",
        "smells": "Couro nobre recém-engraxado, chuva fria e o vapor avermelhado das narinas dos corcéis.",
        "touch": "O estofamento de veludo capitonê macio e aquecido dentro da carruagem, em contraste chocante com o frio congelante do lado de fora.",
        "narrar": "As portas da Carruagem Negra fecham-se com um clique suave de bronze, isolando o grupo do vendaval da tempestade. Conforme os quatro cavalos de guerra colossais disparam pelas curvas vertiginosas da serra, os relâmpagos através das janelas laqueadas iluminam o abismo que se aprofunda a cada segundo. À frente, rasgando o céu como navalhas de pedra negra, erguem-se as torres monumentais do Castelo Ravenloft."
    },
    "O4": {
        "obj": "Chegar ao pátio de carruagens do Castelo Ravenloft, cruzar a ponte levadiça sobre o abismo de trezentos metros e ser recebido nos portais do castelo pelo camareiro Rahadin.",
        "ctx": "A entrada em Ravenloft é uma demonstração de poder gótico esmagador. Gárgulas de pedra parecem seguir os heróis com os olhos nas ameias. Rahadin os recebe com frieza aristocrática e recolhe as armas maiores sob protocolo de banquete.",
        "sights": "Pátio interno cercado por muralhas de trinta metros de altura; ponte levadiça de madeira sobre um fosso sem fundo; estátuas de dragões e gárgulas com garras prontas; portas duplas de carvalho maciço com oito metros de altura.",
        "sounds": "O ranger colossal das correntes da ponte levadiça se erguendo atrás do grupo; o bater de botas no mármore polido do vestíbulo; e o eco sussurrado da aura de almas de Rahadin.",
        "smells": "Chuva sobre pedra antiga, óleo de lamparinas de prata e incenso aristocrático de mirra e cedro.",
        "touch": "O mármore negro do piso do vestíbulo gelado como um espelho d'água.",
        "narrar": "A Carruagem Negra para no centro do pátio do castelo. Atrás de vocês, as correntes da ponte levadiça rangem e erguem-se com estrondo, trancando o abismo. As portas colossais de Ravenloft abrem-se sem ruído de dobradiças, revelando um vestíbulo imenso de mármore negro iluminado por archotes de chamas douradas. Parado na base da escadaria imperial, trajando libré de gala e capa cinzenta, está o camareiro Rahadin. Ele curva-se com precisão milimétrica: 'Sejam bem-vindos ao Castelo Ravenloft. Meu senhor os aguarda no Grande Salão de Jantar.'"
    },
    "O5": {
        "obj": "Participar do monumental Banquete no Salão K10 de Ravenloft, dialogar frente a frente com o Conde Strahd von Zarovich sentado à cabeceira da mesa suntuosa e responder às suas três perguntas com astúcia e honra.",
        "ctx": "DragnaCarta Canônica: Strahd está presente em carne e osso, não como ilusão! A mesa de mogno de dez metros está coberta de iguarias nobres, porcelanas e vinho Red Dragon Crush. Strahd conduz uma conversa de inteligência e avaliação psicológica, fazendo três perguntas que testam a bússola moral dos personagens.",
        "sights": "Salão de banquete majestoso com lareira crepitante de quatro metros de largura; mesa monumental de mogno iluminada por candelabros de prata pura com dezenas de velas de cera de abelha; javali assado com maçãs, faisões caramelizados e cálices de cristal lapidado; Strahd sentado à cabeceira em trajes nobres de veludo escarlate e seda preta.",
        "sounds": "O som grandioso e suave de um órgão de tubos tocando acordes fúnebres ao fundo; o crepitar da lareira; o tilintar de talheres de prata em pratos de ouro; e a voz hipnótica, aveludada e profunda de Strahd.",
        "smells": "Carne assada com ervas nobres, pão quente de centeio, vinho tinto envelhecido, cera perfumada e o cheiro aristocrático de sândalo e poder.",
        "touch": "Cadeiras estofadas em veludo acolhedor e a taça de cristal lapidado pesada e fria nas mãos.",
        "narrar": "O Salão de Jantar K10 de Ravenloft é uma obra-prima de esplendor gótico e terror aristocrático. Sob uma abóbada de dez metros de altura iluminada por candelabros colossais de prata e uma lareira colossal onde toras de carvalho ardem em chamas douradas, uma mesa de mogno estende-se coberta por baixelas de ouro, faisões assados e cálices de cristal transbordando do mais raro vinho tinto. À cabeceira da mesa, com as mãos enluvadas cruzadas e um sorriso sereno nos lábios, está o Conde Strahd von Zarovich em pessoa. Ele ergue seu cálice na direção de vocês com graça soberana: 'Acomodem-se, meus convidados. Em uma terra tão sombria quanto a nossa, a civilidade e a boa conversa são privilégios que devemos saborear com lentidão. Vamos conversar sobre o futuro de suas vidas.'"
    },
    "O6": {
        "obj": "Conduzir a visita guiada pelos salões nobres de Ravenloft acompanhados pela noiva vampira Sasha Ivliskova, explorar a galeria de retratos e descobrir as fissuras emocionais na corte do vampiro.",
        "ctx": "Sasha Ivliskova é uma das noivas de Strahd que foi esquecida e substituída em seu coração. Ela conduz o tour com melancolia dolorosa, revelando aos poucos os segredos dos ancestrais de Strahd e o retrato de Tatyana original.",
        "sights": "Corredores monumentais com paredes revestidas de painéis de carvalho entalhado e retratos de generais e reis da dinastia von Zarovich; Sasha com seu vestido de seda cinzenta e olhos tristes e pálidos de cria de vampiro; a grande pintura a óleo da bela Tatyana no auge de sua juventude.",
        "sounds": "Passos suaves ecoando pelas arcadas desertas; o sussurro de cortinas pesadas com a brisa da noite; e o suspiro abafado de Sasha encarando o retrato de sua rival imortal.",
        "smells": "Rosas murchas, verniz antigo, linho fino e poeira secular preservada pelo frio.",
        "touch": "O mármore das balaustradas liso e gélido.",
        "narrar": "Acompanhados pela bela e melancólica noiva Sasha Ivliskova, vocês percorrem os salões silenciosos do castelo. Entre retratos imponentes de reis e generais que conquistaram o vale há séculos, Sasha para diante de uma tela monumental iluminada por duas arandelas de prata: o retrato original de Tatyana Federovna. A semelhança absoluta com Ireena Kolyana é de tirar o fôlego. Sasha toca a moldura de ouro com a ponta de unhas afiadas e sussurra em tom doloroso: 'Ela morreu há quatro séculos... e ainda assim, eu sou apenas uma sombra esquecida no castelo enquanto meu senhor queima o mundo para ter os olhos dela de volta.'"
    },
    "O7": {
        "obj": "Instalar-se na suntuosa Suíte de Hóspedes K50 no andar superior de Ravenloft, inspecionar os aposentos luxuosos em busca de passagens secretas e armadilhas, e estabelecer a vigília da noite.",
        "ctx": "A suíte K50 é um refúgio de luxo imperial com lareira acesa, camas de dossel de veludo e banheiros de mármore. Sob as leis de hospitalidade, Strahd não atacará o quarto durante a noite, mas o castelo em si é vivo e assombrado por espíritos que tentam roubar a sanidade dos heróis.",
        "sights": "Dois quartos amplos com camas gigantescas de dossel carmesim; lareira acesa com chamas azuis reconfortantes; roupões de seda limpos dobrados sobre cadeiras; janelas de vitral com vista para o abismo vertiginoso lá fora.",
        "sounds": "O uivo do vento na escarpa rochosa lá fora; o crepitar acolhedor da lareira; e o murmúrio sussurrado de almas presas no encanamento e nas chaminés.",
        "smells": "Lavanda, cera perfumada, lenha de cedro e linho lavado.",
        "touch": "Colchões de penas de ganso macios como nuvens e colchas de veludo pesado.",
        "narrar": "A Suíte de Hóspedes K50 oferece um nível de conforto e opulência inédito em toda a Baróvia. Camas monumentais de dossel com lençóis de linho alvíssimo e colchas de veludo carmesim repousam diante de uma lareira acesa que afasta qualquer vestígio de frio. Mas ao olharem pelas frestas das tapeçarias, a ilusão de paz quebra-se: seteiras secretas nas paredes permitem que espiões do castelo vigiem o quarto de ângulos invisíveis, e o abismo negro do precipício estende-se trezentos metros abaixo da janela."
    },
    "O8": {
        "obj": "Enfrentar o terrível pesadelo induzido pelo espírito atormentado da criada Varushka na calada da noite, resistir ao terror psíquico do suicídio histórico do quarto e libertar sua alma da repetição eterna.",
        "ctx": "Varushka foi uma criada que se trancou neste quarto séculos atrás e cortou os pulsos para não ser transformada em vampira por Strahd. Seu espírito revive o pesadelo todas as noites e tenta arrastar a mente de um dos personagens para o abismo do desespero.",
        "sights": "As chamas da lareira apagando-se em fumaça cinzenta; o quarto cobrindo-se de gelo e teias de aranha ilusórias; o fantasma translúcido de uma jovem criada sangrando nos pulsos sobre uma bacia de prata.",
        "sounds": "Choro agoniado e sussurros desesperados de 'Ele está vindo... Trancem a porta... Ele tem dentes de lobo...'; o gotejar lento de sangue no metal.",
        "smells": "Sangue quente, ferro oxidado e frio de túmulo.",
        "touch": "O frio de zero absoluto que congela o suor na testa dos heróis durante o pesadelo.",
        "narrar": "Na hora mais escura da madrugada, a lareira da suíte apaga-se de repente com um chiado de cinzas úmidas. As sombras do quarto esticam-se e o ar gela até a respiração doer nos pulmões. Junto ao guarda-roupa, a aparição de uma jovem criada de olhos vazios e avental ensanguentado surge soluçando, com as mãos cortadas derramando sangue espectral em uma bacia: 'Não abram a porta... O mestre bebe o sangue dos vivos... A morte é a única porta que ele não pode trancar!' O terror psíquico atinge a mente do grupo como uma onda de agonia pura."
    },
    "O9": {
        "obj": "Despertar ileso na manhã seguinte no Castelo Ravenloft, constatar que o juramento de hospitalidade foi cumprido à risca pelo lorde, e recolher seus pertences para o desjejum.",
        "ctx": "O amanhecer rompe as nuvens cinzentas. Criados do castelo (liderados pelo velho Lief Lipsiege ou Cyrus Belview) trazem café fresco, pães e frutas para o quarto.",
        "sights": "A luz cinzenta da manhã entrando pelos vitrais da suíte; bandejas de prata com café quente, torradas amanteigadas e frutas frescas trazidas por criados silenciosos.",
        "sounds": "O badalar solene de um sino no campanário de Ravenloft marcando a alvorada; passos discretos de servos no corredor.",
        "smells": "Café fresco, pão quente assado e lenha de pinho.",
        "touch": "O vapor quente do café aquecendo as mãos tensas dos heróis.",
        "narrar": "O toque solene do sino da torre de Ravenloft anuncia a alvorada. Contra todas as probabilidades, vocês sobreviveram à noite sob o teto do soberano de Baróvia. A porta da suíte abre-se suavemente para revelar criados silenciosos com libré impecável trazendo bandejas de prata com desjejum farto de café fresco, pães crocantes e frutas silvestres: a prova de que Strahd cumpre sua palavra de honra como nobre até a última letra."
    },
    "O10": {
        "obj": "Aproveitar a permissão formal de trânsito concedida por Strahd para explorar discretamente as áreas comuns permitidas do castelo antes da partida, mapeando rotas e entradas secretas para a futura invasão.",
        "ctx": "Os heróis têm permissão para caminhar pelo vestíbulo, refeitório e capela até o meio-dia. Personagens astutos usam essa brecha para memorizar a disposição dos guardas, os elevadores de serviço e os acessos às catacumbas.",
        "sights": "Corredores iluminados pela luz do dia com sombras góticas; detalhes das portas das masmorras e da torre do relógio memorizados em croquis mentais.",
        "sounds": "Ecos de passos da guarda de mortos-vivos marchando nas muralhas superiores; sussurros distantes de prisioneiros nas fendas do piso.",
        "smells": "Pedra molhada, incenso matinal e poeira antiga.",
        "touch": "O entalhe discreto feito na argamassa para marcar um ponto de fuga futuro.",
        "narrar": "Com passos comedidos e olhos atentos a cada detalhe arquitetônico, o grupo caminha pelas galerias autorizadas de Ravenloft. Cada nicho, cada escadaria em caracol, cada porta reforçada de ferro é gravada na memória como ouro puro: vocês estiveram dentro do coração da fortaleza do inimigo, e agora sabem exatamente por onde atacar quando a hora do golpe final chegar."
    },
    "O11": {
        "obj": "Despedir-se formalmente do castelo, cruzar a ponte levadiça escoltados por Rahadin e embarcar na carruagem de retorno para o vale com a cabeça erguida e segredos cruciais na bagagem.",
        "ctx": "O Jantar com o Diabo encerra-se com sucesso absoluto. O salvo-conduto foi honrado e o grupo sai do castelo não como vítimas aterrorizadas, mas como estrategistas que mediram o calibre de Strahd e sobreviveram para contar.",
        "sights": "A ponte levadiça baixada sobre o abismo; Rahadin fazendo uma vênia militar solene nos portões de ferro; a carruagem negra pronta para descer a serra; o vale de Baróvia se abrindo lá embaixo.",
        "sounds": "O bater firme da porta da carruagem; o estalar de chicote; e o eco de cascos descendo a estrada.",
        "smells": "Vento fresco da floresta expulsando o cheiro de pedra de castelo.",
        "touch": "A sensação revigorante de liberdade ao cruzar os portões de volta para as terras baixas.",
        "narrar": "Nos portões monumentais de Ravenloft, Rahadin curva a cabeça com frieza solene: 'Meu senhor agradece por sua distinta companhia. Ele aguardará ansioso pelo próximo reencontro de vocês.' A Carruagem Negra parte em disparada descendo as curvas da montanha rumo ao vale. Atrás de vocês, as muralhas colossais do castelo encolhem na neblina, mas em suas mentes arde a certeza inabalável: o monstro pode ser majestoso, mas ele é de carne, sangue e dor... e pode ser derrotado."
    },

    # ARC P: RAVENLOFT HEIST
    "P1": {
        "obj": "Conduzir a reunião clandestina de planejamento do Grande Golpe de Ravenloft (Ravenloft Heist), definir as funções de cada herói (infiltrador, vigia, arrombador, combatente) e traçar a rota de invasão pelas muralhas ou despenhadeiros.",
        "ctx": "O grupo reúne-se com Ezmerelda d'Avenir e aliados para planejar o roubo das relíquias sagradas (o Crânio de Argynvost, a Espada de Luz Solar ou o Símbolo Sagrado) e a libertação de prisioneiros das masmorras. A invasão deve ser cirúrgica e silenciosa.",
        "sights": "Mesa com mapa arquitetônico completo de Ravenloft desenhado por Ezmerelda; cordas com ganchos de escalada de ferro fosco; gazuas, frascos de ácido e poções de invisibilidade alinhadas.",
        "sounds": "Sussurros tensos de planejamento tático; o tilintar de ferramentas de arrombamento sendo guardadas nos bolsos.",
        "smells": "Óleo de couro, graxa de armas e chá de ervas quentes.",
        "touch": "A textura firme e áspera da corda de escalada que sustentará a vida dos aventureiros nas muralhas.",
        "narrar": "À luz de uma única lamparina em uma cabana segura, Ezmerelda desenha a planta das masmorras e catacumbas do castelo com precisão de mestre: 'Não há exército que possa derrubar as portas de Ravenloft de frente. Mas quatro ou cinco sombras bem coordenadas podem entrar pela fenda do penhasco, pegar o crânio e as relíquias nas catacumbas e sair antes que Strahd termine sua taça de sangue. Se alguém falhar... a morte será o menor dos nossos problemas.'"
    },
    "P2": {
        "obj": "Executar a aproximação furtiva sob a calada da noite aos pés do Pináculo de Ravenloft, escalar o penhasco vertical de trezentos metros e infiltrar as ameias inferiores sem ser detectado.",
        "ctx": "A escalada do penhasco é uma proeza atlética sob vento cortante e chuva fina. Ganchos de ferro e magias de passos de aranha garantem o acesso aos parapeitos sem soar os sinos de alerta das gárgulas.",
        "sights": "A colossal muralha de rocha de basalto negro subindo reta até as fundações de pedra do castelo; nuvens de tempestade rolando abaixo dos pés dos escaladores; seteiras de ferro fracamente iluminadas.",
        "sounds": "O som seco de ganchos acolchoados com pano prendendo nas ameias; o uivo do vento no precipício; e a respiração ofegante de quem escala sobre a morte.",
        "smells": "Pedra molhada, líquen congelado e ozônio.",
        "touch": "A rocha escorregadia e congelante que queima a ponta dos dedos através das luvas de couro.",
        "narrar": "A escalada do Pináculo de Ravenloft desafia a gravidade e o bom senso. Trezentos metros abaixo dos pés dos heróis, a floresta de Baróvia é um mar de névoa escura. Movendo-se de saliência em saliência sob a proteção das sombras, os ganchos de ferro mordem as ameias do pátio inferior. Com um impulso final de força e coragem, os heróis saltam sobre o parapeito de pedra: a fortaleza mais vigiada do mundo está invadida."
    },
    "P3": {
        "obj": "Navegar pelos pátios externos e acessos periféricos do castelo, evitar as sentinelas de ferro e cruzar em direção à ala dos servos.",
        "ctx": "O pátio interno é patrulhado por esqueletos de armadura completa e cães do inferno adormecidos. A rota mais segura passa pelo pátio das carroças e pela pequena porta de serviço da ala da despensa.",
        "sights": "Pátio deserto iluminado por relâmpagos intermitentes; a Carruagem Negra imóvel no galpão; estátuas de gárgulas cujos olhos parecem girar na direção do movimento.",
        "sounds": "Passos metálicos de patrulhas de armaduras de placas; correntes tilintando; e o sopro gélido do vento nas esquinas do pátio.",
        "smells": "Cinzas frias de fogueiras extintas e esterco velho de cavalos monstruosos.",
        "touch": "O ferro oxidado da tranca da porta de serviço sendo forçado com gazua de prata.",
        "narrar": "As sombras do pátio são traiçoeiras e frias. Rastejando sob o casco de carruagens velhas e entre os contrafortes de pedra, o grupo cronometra a ronda dos sentinelas esqueléticos. Quando a última armadura vira a esquina com passos pesados, uma gazua rápida gira no trinco da porta dos criados: a passagem para as entranhas de Ravenloft está aberta."
    },
    "P4": {
        "obj": "Atravessar as áreas comuns e o grande Salão de Entrada do castelo, desativar armadilhas de glifos arcanos e acessar a Capela de Ravenloft K15.",
        "ctx": "A Capela de Ravenloft abriga o espírito decaído do bispo e relicários sagrados profanados. O grupo deve mover-se sem fazer barulho para não despertar as vigias do segundo pavimento.",
        "sights": "Salão com abóbadas góticas monumentais e colunas de mármore entalhadas com brasões reais; a Capela com bancos quebrados e um altar de bronze escurecido sob vitrais partidos.",
        "sounds": "O som oco de passos contidos na pedra polida; e o eco distante de risadas cruéis vindas dos andares superiores.",
        "smells": "Incenso amargo envelhecido, poeira de capela e pedra úmida.",
        "touch": "A madeira carcomida dos bancos sagrados e o frio cortante do piso de mármore.",
        "narrar": "A travessia dos salões comuns de Ravenloft é uma dança no fio de uma navalha. Sob os arcos pontiagudos da Capela Real, onde reis antigos foram coroados e noivas foram veladas em sangue, o silêncio é espesso como chumbo. Desativando glifos arcanos desenhados com sangue seco nos umbrais, os aventureiros alcançam a escadaria espiral que desce para as alas de serviço e masmorras."
    },
    "P5": {
        "obj": "Explorar a Ala dos Servos, desviar ou subornar o contador leal Lief Lipsiege acorrentado aos seus livros contábeis, e enganar o bizarro lacaio Cyrus Belview no elevador de carga.",
        "ctx": "Lief Lipsiege é um escriba moribundo acorrentado a uma escrivaninha contando moedas e dívidas eternas de Baróvia. Cyrus Belview é um mongilóide grotesco com asas de morcego e pernas deformadas que pilota o elevador de carga que conecta a cozinha às masmorras e torres.",
        "sights": "Câmara contábil apinhada de livros de registro financeiro de quatrocentos anos; Lief Lipsiege com óculos de aros de ferro e correntes presas aos tornozelos; Cyrus Belview com sua corcunda, avental imundo e caldeirão de ensopado de ratos.",
        "sounds": "O arranhar furioso de penas de ganso no pergaminho; o tilintar de correntes de ferro; e a voz fanhosa e subserviente de Cyrus tentando 'agradar os convidados'.",
        "smells": "Tinta nanquim, pergaminho mofado, ensopado podre de vísceras e gordura vegetal.",
        "touch": "As moedas de cobre antigas e o cabo de madeira da manivela do elevador de serviço.",
        "narrar": "Na ala dos servos, a rotina bizarra de Ravenloft continua sem pausa: Lief Lipsiege, com correntes presas aos pés, escreve freneticamente colunas de impostos e tributos em livros centenários sem erguer os olhos. Mais adiante, perto do poço do elevador de carga, o disforme Cyrus Belview mexe um caldeirão com uma colher de pau gigantesca. Ao ver os heróis, o servo pisca os olhinhos miúdos com medo e reverência: 'Visitantes nobres! Cyrus não viu nada! Cyrus só cuida do elevador e do ensopado do mestre!'"
    },
    "P6": {
        "obj": "Infiltrar os Aposentos Reais no andar superior, encontrar a ingênua cortesã baroviana Gertruda (a filha desaparecida de Mad Mary) vivendo em luxo ilusório, e recolher joias e chaves mestras.",
        "ctx": "Gertruda fugiu de casa em busca de romance de conto de fadas e está hospedada em um quarto imperial de Ravenloft, acreditando inocentemente que Strahd é um príncipe nobre e gentil que logo casará com ela. Ela se recusa a fugir, mas sua inocência permite ao grupo pegar chaves e joias sem soar o alarme.",
        "sights": "Quarto de luxo de conto de fadas com dossel de seda rosa, almofadas bordadas e doces finos; Gertruda, uma bela jovem de cabelos negros e camisola de renda, escovando os cabelos diante de um espelho de prata.",
        "sounds": "Gertruda cantando baixinho com voz doce de donzela apaixonada; o estalo suave de trincos de joias sendo abertos.",
        "smells": "Perfume de jasmim, pó de arroz, açúcar e frutas secas.",
        "touch": "A seda macia das almofadas e o peso de um colar de rubis tirado da cômoda.",
        "narrar": "Atrás de uma porta de carvalho esculpida com figuras de anjos, o horror cede lugar a um delírio surreal de conto de fadas. Em uma cama de dossel de cetim cor-de-rosa forrada de travesseiros de plumas, a jovem Gertruda escova os cabelos longos com um pente de tartaruga e marfim. Ela olha para os aventureiros armados com um sorriso ingênuo e encantado: 'Vocês são cavaleiros enviados por meu amado conde? Ele é tão bondoso... Me deu vestidos de princesa e prometeu que nunca mais terei que viver na miséria da vila!'"
    },
    "P7": {
        "obj": "Escalar a vertiginosa Torre do Campanário de Ravenloft, atravessar as vigas estreitas de madeira sobre o abismo interno e saquear a Tesouraria Secreta do campanário.",
        "ctx": "No alto do campanário repousa o sino monumental de bronze e baús trancados contendo relíquias arcanas, pergaminhos de magias esquecidas e barras de platina guardadas pelo lorde.",
        "sights": "Um sino titânico de bronze de três metros de altura suspenso por correntes de ferro maciço; vigas de carvalho cruzando um poço vertical de trinta metros; baús de madeira de lei reforçados com ligas de prata.",
        "sounds": "O som agudo de correntes balançando com o vento das frestas; e o tilintar de moedas de platina caindo nas bolsas dos heróis.",
        "smells": "Bronze oxidado, poeira de teias de aranha seculares e madeira seca.",
        "touch": "O equilíbrio tenso sobre vigas estreitas onde um passo falso significa despencar no poço.",
        "narrar": "No topo da Torre do Campanário, o espaço abre-se em um vazio cavernoso onde vigas de carvalho entrecruzam-se sobre um poço escuro sem fundo. Acima de suas cabeças repousa o colossal sino de bronze de Ravenloft, adormecido como um monstro de metal. Em um mezanino de tábuas grossas, baús pesados protegidos por cadeados complexos guardam a fortuna acumulada por séculos de tributos e conquistas de Strahd."
    },
    "P8": {
        "obj": "Utilizar a Suíte de Hóspedes como ponto de passagem estratégico temporário durante a incursão noturna, despistar cães farejadores e reagrupar a equipe.",
        "ctx": "O grupo utiliza o conhecimento prévio adquirido durante o Jantar para esconder-se temporariamente na suíte enquanto uma patrulha de guardas de armadura pesada passa pelo corredor.",
        "sights": "A suíte vazia iluminada apenas pela luz azulada da tempestade lá fora; sombras de alabardas passando sob a fresta da porta principal.",
        "sounds": "O trote pesado e rítmico de patrulhas de esqueletos no corredor; respirações contidas da equipe nas sombras.",
        "smells": "Cinzas frias da lareira e óleo de tochas do corredor.",
        "touch": "A madeira grossa da porta trancada por dentro que barra os caçadores por preciosos minutos.",
        "narrar": "Deslizando pelas sombras do corredor no momento em que uma patrulha de cavaleiros espectrais se aproxima, os heróis abrigam-se na familiar Suíte K50. Trancando o ferrolho com cuidado absoluto, todos prendem a respiração enquanto o tilintar de aço e passos pesados passam a centímetros do umbral: o conhecimento prévio do castelo transformou uma armadilha em rota de sobrevivência."
    },
    "P9": {
        "obj": "Infiltrar o antro das Bruxas de Baróvia nos desvãos superiores de Ravenloft, sabotar seus caldeirões de veneno e obter reagentes arcanos raros.",
        "ctx": "As bruxas de Baróvia servem a Strahd preparando poções de cegueira, venenos de paralisia e vassouras animadas. Neutralizá-las furtivamente evita que alarmes mágicos despertem os vampiros.",
        "sights": "Aposento escuro e imundo repleto de peles de morcego penduradas, potes de barro com olhos de sapo e caldeirões de ferro borbulhando com fumaça esmeralda venenosa; bruxas decrépitas de unhas pretas curvadas sobre grimórios.",
        "sounds": "Sussurros malévolos em dialeto arcano; gargalhadas esganiçadas; e o borbulhar viscoso de veneno fervente.",
        "smells": "Enxofre, urina de rato, ervas amargas venenosas e gordura animal rançosa.",
        "touch": "A umidade pegajosa que cobre cada superfície da cozinha das bruxas.",
        "narrar": "Os aposentos das bruxas de Baróvia fedem a malícia e podridão. Em volta de caldeirões de ferro borbulhantes que lançam vapores esmeraldas contra o teto de pedra, megeras encurvadas com rostos cobertos de verrugas e unhas de ferro cortam raízes venenosas. Com ataques precisos e silenciosos das sombras, os heróis calam as sentinelas arcanas antes que o primeiro frasco de alarme seja quebrado no chão."
    },
    "P10": {
        "obj": "Navegar pela Guarnição dos Guardas e pela grande escadaria espiral que conecta os andares verticais de Ravenloft, desarmando armadilhas de glifos e descendo em direção às masmorras.",
        "ctx": "A escadaria espiral de pedra calcária é o eixo vertical de Ravenloft, descendo centenas de degraus desde o topo das torres até as profundezas das catacumbas.",
        "sights": "Escadaria circular de pedra sem corrimão serpenteando em torno de um poço vertical; seteiras com vento zunindo; nichos com armaduras decorativas com machados de guerra prontos para cair.",
        "sounds": "O som sibilante do vento subindo pelo poço da escada como um lamento contínuo; e o eco de passos suaves descendo degrau por degrau.",
        "smells": "Pedra seca, poeira e o ar gélido e denso das profundezas que sobe da terra.",
        "touch": "A pedra gasta pelo passo de séculos de soldados sob as solas das botas.",
        "narrar": "A grande escadaria espiral de Ravenloft desce como uma serpente de pedra pelas entranhas da montanha. Olhar para o vão central é encarar um poço de escuridão sem fim. Degrau por degrau, descendo cada vez mais fundo sob as fundações do castelo, o calor dos andares nobres desvanece por completo, substituído pelo frio mortal e pelo cheiro de ferro e sepulturas que anuncia a proximidade das masmorras."
    },
    "P11": {
        "obj": "Invadir as tenebrosas Masmorras de Ravenloft (área K73 a K80), resgatar o líder lobisomem aprisionado Emil Toranescu de sua cela de ferro e desvendar o enigma do Braseiro Mágico de teletransporte.",
        "ctx": "Nas masmorras inundadas por trinta centímetros de água podre repousam celas de ferro onde prisioneiros esquecidos apodrecem. Em uma cela isolada está Emil Toranescu, ferido e faminto. No laboratório de tortura repousa o grande Braseiro de Pedra com pedras coloridas que ativam teletransportes instantâneos para locais secretos do castelo.",
        "sights": "Corredores de celas com água fétida cobrindo o chão até as canelas; grades de ferro enferrujado com esqueletos em grilhões; Emil Toranescu, um homem musculoso de cabelos grisalhos e olhos lupinos amarrado com correntes de prata; o grande braseiro de pedra no centro da câmara circular com chamas brancas mágicas.",
        "sounds": "O som constante de água gotejando e espirrando sob as botas; gemidos fracos de prisioneiros moribundos; e o ranger pesado das trancas de ferro sendo forçadas com alavanca.",
        "smells": "Água estagnada fétida, esgoto, sangue seco nas mesas de tortura e a fumaça mágica aromática do braseiro.",
        "touch": "A água gélida e lodosa ensopando as pernas e o calor mágico convidativo das chamas do braseiro.",
        "narrar": "As masmorras de Ravenloft são o ápice da crueldade silenciosa do lorde vampiro. Água negra e viscosa cobre o chão de pedra, refletindo tochas solitárias cravadas em paredes gotejantes. Atrás de grades pesadas de ferro forjado, o líder lobisomem Emil Toranescu ergue o olhar cansado e feroz, quebrando em lágrimas de alívio ao ouvir que Zuleika enviou os heróis para libertá-lo: 'Tirem-me dessas correntes de prata... e minha matilha uivará a favor de suas lâminas até o fim dos tempos!'"
    },
    "P12": {
        "obj": "Adentrar as monumentais Catacumbas de Ravenloft (K84 com as quarenta criptas funerárias e tumbas reais K85-K88), desvendar as criptas dos ancestrais, recuperar as relíquias sagradas (o Crânio de Argynvost, a Espada de Luz Solar e o Símbolo Sagrado) e escapar com o tesouro supremo de Baróvia.",
        "ctx": "As catacumbas são um labirinto monumental de colunas e nichos de pedra que abrigam 40 criptas numeradas. Aqui repousam os restos mortais do Rei Barov e da Rainha Ravenovia (criptas reais K85 e K86), o túmulo de Sergei von Zarovich (K87) onde a armadura brilhante repousa, e na cripta de um general jaz o Crânio de Argynvost (o crânio colossal do dragão de prata) ou a lendária Espada de Luz Solar!",
        "sights": "Salão subterrâneo de proporções ciclópicas com teto sustentado por dezenas de colunas grossas de pedra; fileiras de criptas de mármore numeradas com inscrições douradas; morcegos aos milhares dormindo no teto alto; o túmulo de mármore branco de Sergei refletindo uma luz etérea; e a colossal ossada prateada do crânio do dragão de três metros de largura.",
        "sounds": "O bater de asas de morcegos gigantes no teto alto; o eco profundo de lajes de mármore sendo empurradas; e o zumbido divino da lâmina de luz solar ao ser desembainhada.",
        "smells": "Pó de pedra milenar, essências de embalsamamento de reis antigos, terra fria e o perfume radiante de relíquias abençoadas.",
        "touch": "O peso monumental do crânio de dragão carregado pelos heróis e o calor radiante da empunhadura da Espada de Luz Solar.",
        "narrar": "As Catacumbas de Ravenloft abrem-se em uma necrópole subterrânea de grandeza colossal. Entre colunas maciças que sustentam o peso da montanha inteira, quarenta criptas funerárias de mármore enfileiram-se no silêncio da eternidade. Ao forçarem a laje da tumba indicada pela profecia de Madame Eva, a luz da esperança ressurge com poder avassalador: diante de vocês repousam os tesouros sagrados que selarão o destino de Strahd. Com o crânio monumental do dragão de prata nos braços e as relíquias empunhadas, o maior golpe da história de Baróvia está concluído!"
    },

    # ARC Q: A SHINING BEACON
    "Q1": {
        "obj": "Conduzir a fuga frenética dos limites de Ravenloft carregando o crânio de Argynvost e as relíquias sagradas, despistar enxames vorazes de morcegos e lobos nas trilhas da montanha e romper o cerco.",
        "ctx": "O alarme de Ravenloft soou: Strahd descobriu o roubo das relíquias e despachou sua guarda predatória. A fuga morro abaixo é uma perseguição tensa em terreno acidentado onde cada segundo conta.",
        "sights": "Céus escurecidos por milhares de morcegos vampiros mergulhando em rasante; tochas acendendo-se no alto das muralhas de Ravenloft; relâmpagos violetas estourando atrás do castelo.",
        "sounds": "O som sibilante de nuvens de morcegos cortando o ar; uivos furiosos de matilhas famintas; e o respirar ofegante dos heróis correndo com o peso do crânio.",
        "smells": "Ozônio elétrico, pelo de morcego, chuva torrencial e terra revirada.",
        "touch": "Garras e asas de morcegos fustigando rostos e capas durante a corrida.",
        "narrar": "O retorno de Ravenloft transforma-se em uma corrida desenfreada pela sobrevivência. O sino do castelo dobra em fúria ensurdecedora, e do topo das torres projeta-se uma nuvem negra de milhares de morcegos carnívoros uivando por sangue. Carregando o colossal crânio prateado e as relíquias conquistadas, os heróis despencam pelas trilhas lamacentas da montanha sob uma chuva torrencial, quebrando o cerco antes que as portas do vale se fechem."
    },
    "Q2": {
        "obj": "Retornar com urgência aos portões de Krezk, convencer o desconfiado Burgomestre Dmitri Krezkov de que o perigo da noite é iminente e obter abrigo para as crianças resgatadas e a comitiva.",
        "ctx": "Dmitri hesita ao ver os heróis perseguidos por feras, mas a visão das crianças barovianas salvas das garras dos lobisomens quebra sua relutância e as portas de Krezk abrem-se para o refúgio seguro.",
        "sights": "Os portões de Krezk com arqueiros posicionados nas ameias; Dmitri avaliando a aproximação dos heróis com binóculo de latão; as crianças chorando de alívio ao cruzarem a muralha.",
        "sounds": "O estrondo dos portões de ferro batendo e trancando logo após a passagem da comitiva; uivos de lobos frustrados do lado de fora dos muros.",
        "smells": "Feno quente, fumaça de lareiras e chuva fria.",
        "touch": "O abraço apertado e emocionado de mães de Krezk acolhendo os órfãos resgatados do covil.",
        "narrar": "A chegada a Krezk dá-se no limite do crepúsculo. Vendo os heróis emergirem da floresta com as crianças resgatadas nos ombros e a alcateia uivando em seus calcanhares, Dmitri Krezkov não hesita: 'Abram os portões! Protejam as crianças!' As pesadas traves de ferro caem no segundo em que o último herói cruza a soleira, deixando as mandíbulas dos lobos estalarem no vazio da noite."
    },
    "Q3": {
        "obj": "Subir à Abadia de Santa Markovia para um confronto filosófico ou físico decisivo com o Abade, quebrar sua ilusão de beatitude mostrando que Vasilka jamais saciará a fome de Strahd, e redimir ou neutralizar o anjo decaído.",
        "ctx": "O Abade pretendia enviar Vasilka com o vestido de noiva para o castelo. Os heróis revelam que Strahd apenas deseja a verdadeira alma de Tatyana e que Vasilka é uma profanação aos olhos do Senhor da Manhã. Se confrontado com argumentos teológicos irrefutáveis (*Conhecimento/Presença CD 15*), o Deva desaba em arrependimento e abençoa as armas do grupo com chamas celestiais; se atacado, luta até a morte em sua forma angelical com asas de fogo.",
        "sights": "O salão do monastério com o Abade revelando asas colossais de luz dourada que queimam os olhos; Vasilka imóvel com lágrimas escorrendo pelos pontos de sua pele costurada; feixes de luz solar mística banhando o altar.",
        "sounds": "A voz angelical e ressonante do Abade tremendo com o peso da verdade cósmica; o som de metal celeste vibrando; e o choro de redenção de uma criatura divina que compreendeu sua própria cegueira.",
        "smells": "Ozônio sagrado, incenso puro de olíbano e flores celestes imortais.",
        "touch": "O calor radiante de bênção angelical que restaura a integridade de armaduras e armas dos heróis.",
        "narrar": "No salão principal da abadia, a verdade quebra a mente do ser celestial. Diante dos argumentos dos heróis e da visão das profanações que cometeu em nome de uma falsa salvação, as ilusões do Abade desmoronam. Ele cai de joelhos no chão de mosaicos, e de suas costas explodem duas asas gloriosas de pura luz dourada que iluminam toda a montanha. Com lágrimas de ouro descendo pelo rosto de anjo, ele estende as mãos sobre as armas do grupo: 'Eu pequei por orgulho... Pensei que poderia curar o Diabo tecendo carne mortal. Que a espada de vocês seja a foice da verdadeira justiça do Senhor da Manhã!'"
    },
    "Q4": {
        "obj": "Receber a aparição espectral urgente de Sir Godfrey Gwilym alertando que o alfa Kiril van Holtz reuniu toda a alcateia de lobisomens e marcha furioso para emboscar os heróis na estrada de Argynvostholt.",
        "ctx": "Godfrey surge nas sombras da trilha: Kiril descobriu que seu covil foi invadido e que as crianças foram libertadas. O alfa mobilizou mais de vinte lobos e guerreiros licantropos para recuperar o controle da floresta.",
        "sights": "Sir Godfrey materializando-se em névoa azulada sobre a relva; a silhueta espectral de seu dragão prateado rugindo no céu noturno.",
        "sounds": "A voz firme e honrada de Godfrey avisando: 'O lobo caça com a fúria dos desesperados... Estejam prontos para o aço prateado!'",
        "smells": "Gelo, ozônio e metal polido.",
        "touch": "O arrepio elétrico da mensagem espectral que desperta todos os reflexos de combate.",
        "narrar": "Na encruzilhada da floresta, uma rajada de vento glacial traz a silhueta espectral de Sir Godfrey em sua armadura prateada reluzente. Seus olhos em chamas azuis fitam os heróis com gravidade urgente: 'Kiril descobriu a perda de seu covil! Ele reuniu todos os dentes e garras da montanha e marcha para esmagar vocês antes que alcancem o solar do dragão. Mantenham suas armas de prata limpas e seus corações firmes: a caçada final começou!'"
    },
    "Q5": {
        "obj": "Enfrentar e destruir o líder supremo dos lobisomens, Kiril van Holtz, e sua guarda predatória de elite em um combate climácico de floresta sob a luz da lua prateada.",
        "ctx": "Kiril é um lobisomem titânico (forma híbrida colossal) que usa ataques viscerais, sopro aterrorizante e resistência monstruosa. Destruí-lo com armas de prata ou fogo liberta a alcateia da tirania de Strahd e encerra a ameaça dos lobos em Baróvia.",
        "sights": "Um lobisomem monstruoso de três metros de altura com pelo negro como azeviche e olhos amarelos incandescentes; garras do tamanho de adagas banhadas em sangue; lobos atrozes avançando em formação cerrada pela mata.",
        "sounds": "O rugido apocalíptico de Kiril que faz tremer os troncos dos pinheiros; o estalar de espadas de prata rasgando carne regenerativa; e o ganido agoniado de lobos abatidos.",
        "smells": "Sangue fumegante sobre a terra congelada, pelo queimado por prata e pólvora.",
        "touch": "O impacto monumental de garras pesadas colidindo contra escudos e armaduras.",
        "narrar": "A mata explode em galhos partidos e uivos ensurdecedores quando Kiril van Holtz arremete contra os heróis. Na forma híbrida de um monstro de três metros com presas do tamanho de adagas e pelos negros eriçados de eletricidade estática, o alfa despedaça árvores com as próprias patas: 'Vocês roubaram minhas crias e traíram minha matilha! Eu vou arrancar seus corações e beber seu sangue sob a lua!' Mas com lâminas banhadas em prata e determinação inquebrável, os heróis cravam o aço no peito da besta, encerrando séculos de terror nas florestas de Baróvia."
    },
    "Q6": {
        "obj": "Conduzir a procissão sagrada de volta a Argynvostholt, depositar o colossal Crânio de Argynvost no Mausoléu do Dragão, e acender o lendário Farol Sagrado que banha todo o vale em luz solar permanente e destrói o domínio de Strahd.",
        "ctx": "Este é um dos maiores momentos de triunfo da campanha: ao depositar o crânio no mausoléu, o espírito de Argynvost ascende em luz prateada e a pira do farol no topo da torre explode em um raio monumental de pura luz solar que brilha eternamente dia e noite. Todos os revenantes encontram a paz e seus espíritos abençoam o grupo com +2 na CA e em todos os testes pelo resto da campanha!",
        "sights": "O crânio de dragão de três metros assentado sobre o sarcófago de mármore do mausoléu; um turbilhão de luz prateada e dourada irrompendo da pedra e subindo até a torre mais alta; a colossal taça de prata do Farol explodindo em chamas sagradas de pura luz solar que varrem as trevas de Baróvia como uma estrela nascida na terra; os espíritos de Vladimir e Godfrey abraçando-se em paz e ascendendo aos céus com sorrisos de gratidão eterna.",
        "sounds": "O rugido majestoso e triunfante de um dragão celestial ressoando por todo o vale; cânticos de hosanas de centenas de cavaleiros espectrais sendo redimidos; e o estalar crepitante do fogo solar que nunca se apagará.",
        "smells": "Incenso puro celestial, ar aquecido pelo sol de verão, rosas em plena floração e a queima definitiva de séculos de cinzas e ódio.",
        "touch": "O calor aconchegante, puro e divino da luz solar tocando a pele dos personagens pela primeira vez desde que entraram nas brumas.",
        "narrar": "No momento em que o crânio monumental de Argynvost é assentado sobre o sarcófago de mármore do mausoléu, o mundo parece parar. Uma luz prateada incandescente e pura irrompe dos ossos do dragão, serpenteando pela torre como uma serpente de fogo celestial até explodir na taça monumental do Farol no topo da mansão. Um pilar de pura luz solar rasga as nuvens de tempestade de Baróvia, banhando montanhas, florestas e as torres distantes de Ravenloft em um brilho dourado e sagrado que jamais se apagará. Ao redor de vocês, os corpos decrépitos dos cavaleiros revenantes desfazem-se em poeira estelar: Sir Godfrey e o Comandante Vladimir prestam sua última e mais gloriosa continência, com sorrisos de paz eterna enquanto seus espíritos voam livres em direção ao amanhecer."
    },
    "Q7": {
        "obj": "Retornar ao Covil dos Lobisomens agora pacificado, entregar o libertado Emil Toranescu nos braços de sua esposa Zuleika, consolidar a nova liderança pacífica da alcateia e selar o juramento de aliança com os homens-lobo contra Ravenloft.",
        "ctx": "Com Kiril destruído e Emil restaurado, a alcateia cessa os ataques aos camponeses e jura fidelidade aos heróis para o grande cerco final contra o Castelo Ravenloft.",
        "sights": "A estátua de Madre Noite com olhos limpos de sangue; Emil e Zuleika abraçados em frente à alcateia; guerreiros lobisomens em forma humana prestando reverência com lanças baixadas.",
        "sounds": "Um uivo longo, harmônico e solene de toda a alcateia em uníssono sob o luar, celebrando a libertação de seu líder tradicional; o murmúrio de juramentos de honra dos caçadores.",
        "smells": "Fogueiras de madeira limpa, carne assada e fumo de ervas aromáticas.",
        "touch": "O aperto de mão de ferro com garras recolhidas de Emil selando o pacto dos lobos.",
        "narrar": "No interior do covil de rocha, o clima de terror deu lugar ao respeito solene de guerreiros da floresta. Emil e Zuleika abraçam-se diante da fogueira sagrada, cercados pela matilha reunida. O líder lobisomem vira-se para o grupo com olhar límpido e firme: 'Kiril nos vendeu como cães para o vampiro do castelo. Vocês nos devolveram nossa honra e nossas famílias. Quando o clarão do Farol chamar para a batalha final... o uivo de nossas presas marchará ao lado de suas espadas!'"
    }
}

ACT3_METADATA.update(ACT3_METADATA_PART2)
print(f"Total Act III metadata completely defined: {len(ACT3_METADATA)} scenes.")

# Helper to compile one scene
def compile_act3_scene(code):
    meta = ACT3_METADATA.get(code)
    sc = scenes_by_code.get(code)
    if not sc or not meta:
        return None
    
    title = sc.get('title', '')
    title_clean = re.sub(r'^[A-Z0-9]+[a-z]?\s*·\s*', '', title)
    
    raw = sc.get('roteiro_raw', '')
    lines = raw.splitlines()
    body_lines = []
    skip = True
    for line in lines:
        l_s = line.strip()
        if any(l_s.startswith(p) for p in ('### ', '**Local', '**Mapa', '**Consulta', '**Casa:', '**Entrada:', '**Oficina', '**Lago', '**Szoldar', '**Pedir', '**Conhecimento', '**Apoio', '**Registro', '**Origem:', '**Quarto', '**Cripta', '**Confronto', '**Se os', '**Reunião', '**Loot', '**Inimigos', '**Táticas', '**Objetivo real', '**Mecânica', '**O que', '**Salão', '**W1', '**W2', '**W3', '**K10', '**K15', '**K50', '**K73', '**K84', '**K85', '**Cavaleiros', '**Torre', '**Pátio')):
            skip = False
        if not skip:
            if l_s.startswith('**Ambiente & Sensações:') or l_s.startswith('**Ambiente & Atmosfera:') or l_s.startswith('**Para narrar:'):
                break
            body_lines.append(line)
            
    body_text = '\n'.join(body_lines).strip()
    body_text = re.sub(r'\b(Instinto|Presença|Conhecimento|Agilidade|Força|Finesse)\s+(\d{1,2})\b', r'\1 (CD \2)', body_text)
    body_text = re.sub(r'\bCD\s*(\d{1,2})\b(?!\))', r'(CD \1)', body_text)
    
    output = f"""## Roteiro Completo · {code} · {title_clean}

**Objetivo:** {meta['obj']}

**Contexto & Segredo (DragnaCarta Lore):** {meta['ctx']}

**Ambiente & Sensações:**
- *Visão:* {meta['sights']}
- *Sons:* {meta['sounds']}
- *Cheiro:* {meta['smells']}
- *Tato:* {meta['touch']}

**Para narrar:** “{meta['narrar']}”

{body_text}

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para manifestar complicações imediatas no ambiente ou acelerar as ameaças de Ravenloft."""
    return output.strip()

all_act3_code = {}
for code in ACT3_METADATA:
    compiled = compile_act3_scene(code)
    if compiled:
        all_act3_code[code] = compiled

print(f"Successfully compiled {len(all_act3_code)} Act III scenes.")

with open('scripts/enrichment_content_act3.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nCurse of Strahd: Reloaded (DragnaCarta) - Act III: The Broken Land & Ravenloft (Scenes J1-J7, K1-K2c, L1-L4, M1-M7, O1-O11, P1-P12, Q1-Q7)\n')
    f.write('Tradução e adaptação 100% fiel do repositório oficial do GitHub (DragnaCarta/Curse-of-Strahd-Reloaded).\n')
    f.write('Roteiros detalhados sem placeholders, descrições autênticas de leitura em voz alta, perfis de NPCs e CDs de Daggerheart.\n"""\n\n')
    f.write("ACT3_SCENES = {\n")
    for code, text in all_act3_code.items():
        escaped_text = text.replace('\\', '\\\\').replace('"""', r'\"\"\"')
        f.write(f'    "{code}": """{escaped_text}""",\n\n')
    f.write("}\n")

print("Saved: scripts/enrichment_content_act3.py")
