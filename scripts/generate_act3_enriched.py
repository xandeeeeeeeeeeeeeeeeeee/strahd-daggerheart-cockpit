# -*- coding: utf-8 -*-
"""
Generator for Act III (Arcs J, K, L, M, O, P, Q) enriched scenes.
Reads DragnaCarta source from reloaded-source and merges with existing rich mechanics,
completely eliminating all generic boilerplate placeholders.
Total: 54 scenes (J1..J7, K1..K2c, L1..L4, M1..M7, O1..O11, P1..P12, Q1..Q7).
"""

import json
import os
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes_by_code = {s['code']: s for s in data['scenes']}

ACT3_METADATA = {
    # ARC J: THE STOLEN GEM (WINERY & YESTER HILL)
    "J1": {
        "obj": "Receiver o apelo desesperado de Urwin Martikov na Estalagem Água Azul, descobrir que os estoques de vinho de toda Baróvia cessaram devido ao ataque à Vinícola Mago dos Vinhos, e aceitar a missão de libertar a vinícola ancestral de sua família.",
        "ctx": "Urwin é o filho afastado de Davian Martikov. A Vinícola Mago dos Vinhos foi invadida por druidas corrompidos e agulheiros da Colina de Yester. Se o fluxo de vinho parar, a pouca sanidade que resta às vilas entrará em colapso total.",
        "sights": "Urwin atrás do balcão encarando barris de carvalho vazios; o olhar preocupado de Danika abraçando seus filhos Brom e Bray; chuva fina batendo nas janelas da taverna.",
        "sounds": "O som oco de um barril vazio ao ser batido; murmúrios apreensivos de clientes reclamando da falta de vinho; e a voz grave e emotiva de Urwin suplicando ajuda.",
        "smells": "Cerveja choca, madeira molhada, pão fresco e resíduos de vinho envelhecido no fundo de canecas de estanho.",
        "touch": "O aperto firme de mãos calejadas de Urwin entregando um mapa com o atalho dos vinhedos.",
        "narrar": "No salão comunal da Estalagem Água Azul, o clima é de velório velado. Atrás do balcão, Urwin Martikov afasta uma caneca vazia e apoia as mãos na madeira, encarando vocês com olhos marejados de angústia: 'A última remessa não chegou de Krezk... e nossos batedores viram fumaça subindo sobre os vinhedos de meu pai. A Vinícola Mago dos Vinhos foi invadida por selvagens da montanha. Se as cubas forem destruídas, toda a Baróvia afundará em desespero absoluto. Por favor... salvem meu pai e libertem a vinícola.'"
    },
    "J2": {
        "obj": "Percorrer a Estrada Svalich em direção ao sudoeste, cruzar os vinhedos carcomidos sob chuva torrencial e encontrar o patriarca Davian Martikov e sua família de wereravens abrigados no bosque próximo à vinícola.",
        "ctx": "Davian Martikov (o severo líder dos Guardiões das Penas) e seus filhos Elvir, Adrian e Stephanie estão escondidos na floresta vigiando o casarão da vinícola tomado por cerca de trinta agulheiros e druidas armados com cajados venenosos.",
        "sights": "Fileiras de videiras retorcidas e sem folhas estendendo-se por colinas lamacentas; o casarão de dois pavimentos da vinícola com varandas de madeira ao fundo; corvos aos milhares empoleirados nas árvores em vigília silenciosa.",
        "sounds": "A chuva forte chicoteando as folhas secas de uva; o grasnar baixo e disciplinado dos corvos; e a voz áspera e autoritária do velho Davian repreendendo seus filhos.",
        "smells": "Terra encharcada, folhas de uva apodrecidas, fumaça de tochas dos druidas e o cheiro doce de mosto de uva fermentando.",
        "touch": "Lama pegajosa até os tornozelos e capas encharcadas sob a tempestade fria do vale.",
        "narrar": "Os vinhedos da família Martikov estendem-se por encostas suaves sob uma tempestade inclemente de outono. As videiras, despidas de folhas e uvas, erguem-se da lama como garras esqueléticas. No bosque de pinheiros vizinho, abrigados sob lonas e vigiados por centenas de corvos silenciosos, está a família Martikov. Um velho de barba espessa e olhos de águia empunha uma besta pesada: Davian Martikov. Ele avalia o grupo com desdém inicial que logo se transforma em esperança ferrenha: 'Vocês vieram da parte de Urwin? Então segurem suas lâminas com firmeza: trinta selvagens e agulheiros estão dentro de minha casa quebrando os tonéis.'"
    },
    "J3": {
        "obj": "Invadir e purificar o casarão da Vinícola Mago dos Vinhos (áreas W1 a W20), expulsar os druidas corrompidos, triturar as hordas de agulheiros e recuperar o controle das cubas de fermentação.",
        "ctx": "A batalha na vinícola é dinâmica e brutal: os agulheiros atacam em enxames através das janelas e rampas de carregamento, enquanto os druidas tentam despejar veneno nas cubas de fermentação de Purple Grapemash e Red Dragon Crush. O túnel secreto dos Martikov chega à adega W15.",
        "sights": "Grandes cubas de carvalho de quatro metros de altura; tonéis de vinho jorrando líquido vermelho pela adega; agulheiros vegetais esguios saltando de vigas; druidas com máscaras de casca de carvalho conjurando vinhas espinhosas.",
        "sounds": "O som viscoso de flechas de espinhos sendo disparadas por agulheiros; cânticos guturais dos druidas; e o quebrar violento de madeira de barris.",
        "smells": "Vinho tinto derramado misturado com seiva vegetal venenosa, sangue fresco e fumaça de madeira queimada.",
        "touch": "O assoalho escorregadio de vinho e mosto sob as botas e espinhos afiados cravando-se nas armaduras.",
        "narrar": "As portas da adega da vinícola são arrombadas em meio a um banho de sangue e vinho. O interior cavernoso da destilaria ecoa com os estalos secos de dezenas de agulheiros que rastejam pelas vigas do teto como aranhas de galhos secos. Druidas vestidos com peles de lobo e máscaras de casca de árvore entoam maldições sobre as cubas monumentais de fermentação, derramando veneno escuro no precioso vinho de Baróvia. Ao lado de vocês, corvos mergulham das frestas do teto bicando os olhos dos invasores em um turbilhão de penas e fúria!"
    },
    "J4": {
        "obj": "Ouvir a revelação dolorosa de Davian sobre as três gemas mágicas que davam vida aos vinhedos, contactar o espírito ancestral do chefe Kavan e marchar antes do amanhecer para a Colina de Yester.",
        "ctx": "Davian revela que as três gemas mágicas roubadas tornaram os vinhedos estéreis: uma sumiu há dez anos (roubada por Urwin), outra foi levada por Baba Lysaga para Berez, e a terceira foi roubada ontem pelos druidas para acordar o titã vegetal Wintersplinter na Colina de Yester.",
        "sights": "Davian acariciando com tristeza as raízes mortas da videira central; o espírito etéreo do guerreiro bárbaro ancestral Kavan sussurrando em sonhos; relâmpagos avermelhados rasgando o céu ao sul sobre a Colina de Yester.",
        "sounds": "Trovões contínuos rolando das montanhas do sul; o som distante de tambores de guerra primitivos marcando um ritual apocalíptico; e a voz ancestral de Kavan ecoando no vento.",
        "smells": "Ozônio elétrico, terra queimada por raios e seiva mágica fervente.",
        "touch": "A vibração profunda no solo causada pelos tambores dos druidas a quilômetros de distância.",
        "narrar": "Reunidos na cozinha da vinícola entre barris salvos, o velho Davian desaba em uma cadeira e confessa a verdade: 'Nossa terra só produz uvas porque há séculos meu avô plantou três gemas mágicas que pulsavam com a luz da Criação. A primeira perdeu-se há anos. A segunda foi levada para a bruxa do pântano de Berez. E a última... os druidas levaram para a Colina de Yester. Eles estão usando o coração da terra para erguer um monstro que destruirá toda a vida deste vale antes do amanhecer!'"
    },
    "J5": {
        "obj": "Escalar os anéis de terra da colossal Colina de Yester sob tempestade elétrica, enfrentar os druidas do círculo sombrio e impedir o ritual que desperta a colossal abominação vegetal Wintersplinter.",
        "ctx": "A Colina de Yester é um túmulo ancestral pagão com círculos concêntricos de terra e uma estátua gigantesca de vime de Strahd no topo. Ao fundo, uma ilusão da muralha de névoa mostra a antiga pátria ensolarada de Strahd. Os druidas usam a gema para animar a colossal árvore maldita Wintersplinter.",
        "sights": "Uma colina gigantesca recortada por relâmpagos vermelhos; círculos de pedras monolíticas no topo; druidas dançando freneticamente ao redor de uma colossal efígie de madeira de quinze metros; a gema verde brilhando no peito da árvore monstruosa que começa a se mover.",
        "sounds": "O estrondo ensurdecedor de relâmpagos caindo sobre as pedras; o rufar frenético de tambores de pele humana; e o gemido telúrico de raízes colossais rasgando a terra conforme Wintersplinter desperta.",
        "smells": "Ozônio primordial, cinzas de fogueiras sacrificiais, sangue animal e seiva viva em ebulição.",
        "touch": "A terra tremendo com violência tectônica sob as passadas do titã vegetal.",
        "narrar": "A Colina de Yester ergue-se contra o céu negro como uma pirâmide pagã banhada por relâmpagos avermelhados. No cume varrido por ventos furiosos, dezenas de druidas de olhos ensanguentados dançam ao redor de um círculo de monólitos antigos, entoando hinos fúnebres ao Senhor da Noite. Diante deles, no centro de uma cova profunda, uma abominação colossal de raízes retorcidas, galhos negros e casca de carvalho de doze metros de altura começa a se erguer: Wintersplinter. Em seu peito de madeira oca, a gema mágica da vinícola pulsa com um clarão esmeralda que faz o solo tremer sob seus pés!"
    },
    "J6": {
        "obj": "Conduzir as consequências imediatas da destruição ou neutralização de Wintersplinter no cume da Colina de Yester, recuperar a gema mágica do coração da besta e contemplar a ilusão da muralha de névoa.",
        "ctx": "Com a derrota da abominação e dos druidas, a gema mágica é extraída de suas entranhas de madeira. Na borda sul da colina, através de uma fresta nas brumas, os personagens avistam uma miragem das antigas terras férteis e ensolaradas da família von Zarovich antes da queda.",
        "sights": "O corpo titânico de Wintersplinter tombado como uma floresta caída gotejando seiva negra; a gema verde-esmeralda cintilando na lama; ao sul, a visão impossível de colinas douradas banhadas por sol de verão através das brumas.",
        "sounds": "O silêncio estupefato da vitória após o fim dos tambores; o cessar suave da chuva; e o suspiro de alívio dos corvos pousando nos monólitos.",
        "smells": "Madeira verde estilhaçada, terra molhada e a pureza revigorante de magia natural restaurada.",
        "touch": "O calor suave e pulsante da gema mágica na palma da mão, como o bater de um coração vegetal vivo.",
        "narrar": "Com um rugido vegetal final que estremece as montanhas, Wintersplinter tomba sobre o cume da colina, desmanchando-se em toneladas de raízes mortas e troncos estilhaçados. No centro de seu peito carcomido, livre das amarras dos druidas, a gema mágica da vinícola repousa limpa, brilhando com um fulgor verde-esmeralda sereno e reconfortante. E ao olharem para o sul, onde a barreira das brumas parecia intransponível, uma fresta revela uma visão comovente: montanhas douradas banhadas pela luz de um sol distante e acolhedor — o mundo além do pesadelo."
    },
    "J7": {
        "obj": "Retornar triunfante à Vinícola Mago dos Vinhos, entregar a gema recuperada a Davian Martikov, restaurar os laços familiares e carregar a primeira carroça de barris de vinho com destino a Krezk.",
        "ctx": "Davian planta a gema nas raízes da videira central com lágrimas nos olhos, reconciliando-se com a memória de sua família. Ele presenteia os heróis com a carroça de barris de vinho necessária para abrir os portões de Krezk e os acolhe como membros honorários dos Guardiões das Penas.",
        "sights": "Videiras florescendo com brotos verdes em minutos assim que a gema é enterrada; barris pesados de carvalho sendo içados para a carroça de tração; a família Martikov reunida em abraço comovido.",
        "sounds": "O bater alegre de martelos ajustando aros de ferro nos barris; risos e canções de trabalho; o trote firme dos cavalos atrelados à carroça.",
        "smells": "Vinho doce recém-engarrafado, madeira nova de carvalho e o aroma fresco de folhas verdes renascendo.",
        "touch": "O aperto de mão caloroso de Davian e o peso glorioso das rédeas da carroça de vinho.",
        "narrar": "O retorno à vinícola é marcado por um milagre: assim que Davian deposita a gema mágica sob o solo fértil da adega, pequenas folhas verdes brotam instantaneamente das vinhas que pareciam mortas há semanas. O patriarca abraça seus filhos com a voz embargada e vira-se para o grupo com a maior reverência de sua vida: 'Vocês devolveram o coração da nossa terra. Esta carroça de vinho é de vocês. Levem-na para Krezk... e digam a Dmitri que os Guardiões das Penas nunca abandonam seus irmãos!'"
    },

    # ARC K: THE FALLEN ABBEY
    "K1": {
        "obj": "Entregar a carroça de vinho nos portões de Krezk, ser recebido com honras pelo Burgomestre Dmitri Krezkov e sua esposa Anna, e aceitar o convite para descansar em sua casa.",
        "ctx": "A chegada do vinho quebra o isolamento de Krezk. Dmitri cumpre sua palavra e abre os portões, mas seu coração está em luto recente pela morte de seu último filho, Ilya. A vila celebra a chegada do vinho, mas olhares apreensivos voltam-se para a Abadia no penhasco.",
        "sights": "Os portões monumentais de Krezk abrindo-se com estrondo; aldeões curvando-se em gratidão ao verem os barris de vinho; a casa rústica e confortável dos Krezkov com lareira aquecida.",
        "sounds": "Sinos de Krezk repicando em festa; o ranger das rodas da carroça entrando na praça; e a voz comovida de Dmitri agradecendo pela salvação de seu povo.",
        "smells": "Pão quente de centeio assado em fornos comunitários, vinho de carvalho e fumaça de pinho.",
        "touch": "O calor das mantas de lã oferecidas por Anna Krezkova e a sensação de abrigo seguro.",
        "narrar": "Os pesados portões de ferro e carvalho de Krezk finalmente abrem-se sob aplausos e lágrimas dos guardas e aldeões. A visão da carroça transbordando de barris de vinho da vinícola é recebida como a salvação do ânimo da comunidade. O Burgomestre Dmitri Krezkov desce das ameias, aproxima-se dos heróis com a mão sobre o peito e curva a cabeça em reverência solene: 'Vocês cumpriram o impossível. Sejam bem-vindos a Krezk, amigos de honra. Minha casa, meu pão e minha lareira são seus por direito.'"
    },
    "K1a": {
        "obj": "Conhecer a intimidade da Casa dos Krezkov, vivenciar o luto da família pela perda trágica de Ilya Krezkov e ouvir a proposta perturbadora do Abade celestial para ressuscitar o garoto.",
        "ctx": "Ilya morreu de febre há quatro dias. Dmitri e Anna revelam que o Abade da Abadia de Santa Markovia ofereceu ressuscitar o filho em troca de um vestido de noiva imaculado para sua misteriosa 'pupila' Vasilka.",
        "sights": "Sala de estar acolhedora com retratos em carvão de quatro crianças falecidas; o quarto fechado onde o corpo de Ilya repousa coberto de sal e flores de montanha; o olhar atormentado de Dmitri diante do dilema moral.",
        "sounds": "O soluço abafado de Anna Krezkova segurando as roupas do filho falecido; o estalar de lenha na lareira; e o silêncio pesado da morte em um lar amoroso.",
        "smells": "Flores secas de montanha, sal marinho de embalsamamento e cera de vela fúnebre.",
        "touch": "O tecido áspero da manta de velório cobrindo o corpo inerte do garoto.",
        "narrar": "Apesar do calor da lareira na casa do Burgomestre, uma sombra fria paira sobre a família Krezkov. Em um quarto fechado repousa o corpo jovem de Ilya, o quarto e último filho do casal, morto há poucos dias por uma febre implacável. Dmitri apoia o rosto nas mãos, com a voz embargada pela dor: 'O Abade do alto da colina... ele diz que tem o poder divino de trazer meu garoto de volta à vida. Mas ele pede um preço bizarro: um vestido de noiva de seda branca para uma criatura que ele mantém trancada no convento. Eu não sei se é uma bênção dos céus... ou a armadilha de um demônio.'"
    },
    "K2": {
        "obj": "Subir a estrada sinuosa do penhasco até a Abadia de Santa Markovia, confrontar os guardas mongilóides (mongrelfolk) nos portões de ferro e estabelecer aliança com a destemida caçadora Ezmerelda d'Avenir.",
        "ctx": "A Abadia ergue-se em um platô elevado sobre o precipício. Ezmerelda d'Avenir está disfarçada nos arredores investigando o Abade e preparando suas armas de prata para caçar Strahd.",
        "sights": "Complexo monástico gótico com muralhas de pedra e telhados pontiagudos; névoa densa ao redor do penhasco; criaturas híbridas de humanos com animais (mongilóides) espirrando de trás de muros; Ezmerelda com sua capa vermelha e bota de metal.",
        "sounds": "Latidos, cacarejos e risadas histéricas dos mongilóides trancados nos pátios; o vento uivando na garganta do penhasco; e a voz confiante de Ezmerelda sacando seu florete de prata.",
        "smells": "Esterco animal, feno podre, incenso fúnebre e o cheiro metálico de prata polida.",
        "touch": "O frio intenso de altitude e a mureta de pedra úmida que margeia a subida do penhasco.",
        "narrar": "A subida para a Abadia de Santa Markovia serpenteia por despenhadeiros de rocha nua onde o vento montanhoso corta como navalha. No topo do penhasco ergue-se o monastério ancestral, com duas torres pontiagudas rasgando a névoa. Mas o som que emana dos muros não é de oração: é um coro enlouquecedor de cacarejos, uivos, latidos e risos deformados. De trás das ameias, uma jovem de pele morena, sobretudo vermelho elegante e uma prótese de metal na perna direita salta com graça felina, embainhando um florete reluzente: Ezmerelda d'Avenir. Ela sorri com um brilho afiado no olhar: 'Se vocês estão subindo para conhecer o santo homem do mosteiro... preparem-se para ver como a loucura pode usar a face de um anjo.'"
    },
    "K2a": {
        "obj": "Negociar a passagem com os guardas mongilóides nos portões da abadia, cruzar o pátio externo repleto de celas e compreender a tragédia da degeneração da linhagem dos Belview.",
        "ctx": "Os Belview eram camponeses de Krezk que pediram ao Abade séculos atrás que curasse suas doenças e lhes desse traços de animais. O Abade usou carne e cirurgia celestial bizarra para transformá-los em quimeras grotescas que vivem encarceradas alimentadas por carniça.",
        "sights": "Celas de madeira e ferro ao longo das muralhas onde dezenas de mongilóides (homens com cabeças de bode, asas de morcego, pernas de sapo) estendem mãos deformadas suplicando por comida; pátio enlameado com ossos roídos.",
        "sounds": "Gritos guturais, relinchos e uivos desafinados em cacofonia enlouquecedora; o bater de tigelas de ferro nas grades das celas.",
        "smells": "Fedor intolerável de excrementos animais misturados com pus, carne estragada e palha fétida.",
        "touch": "Mãos com garras escamosas tentando agarrar as capas dos heróis através das frestas das grades.",
        "narrar": "Os portões de ferro da abadia abrem-se para um cenário de delírio e deformidade. Ao longo das muralhas do pátio interno, dezenas de celas gradeadas abrigam os sobreviventes da linhagem Belview: criaturas híbridas grotescas criadas pelas 'misericórdias' do Abade. Homens com focinhos de porco, mulheres com escamas de peixe e braços em forma de asas de morcego debatem-se nas grades com tigelas vazias, uivando por sobras de comida sob o olhar impassível de estátuas de santos cujos olhos foram arrancados."
    },
    "K2b": {
        "obj": "Adentrar o salão principal da abadia, confrontar o celestial Abade (um Deva insano disfarçado de monge de túnica imaculada) e testemunhar sua criação bizarra: a noiva de carne costurada Vasilka.",
        "ctx": "O Abade é um Deva celestial enviado séculos atrás pelo Senhor da Manhã que perdeu a sanidade ao tentar 'curar' a maldição de Strahd. Ele acredita que se construir uma mulher perfeita de partes de cadáveres para casar com Strahd, o vampiro encontrará a paz e a névoa se dissipará. Vasilka é um golem de carne perfeito com o rosto costurado para parecer Tatyana.",
        "sights": "Salão de baile iluminado por candelabros dourados; o Abade com sua túnica branca imaculada, feições angelicais e olhos de ouro líquido; Vasilka, uma criatura alta de pele pálida com finas cicatrizes cirúrgicas no pescoço e braços, usando um vestido incompleto de cetim branco e aprendendo a dançar valsa.",
        "sounds": "Uma melodia suave e triste de realejo tocando uma valsa baroviana; o som de passos pesados de Vasilka dançando desajeitadamente; e a voz hipnótica, serena e perturbadoramente mansa do Abade.",
        "smells": "Flores frescas de alfazema, perfume de rosas caras, cera de abelha e o odor sutil de formol e carne embalsamada sob o vestido.",
        "touch": "A mão do Abade quente como o sol e a pele gélida e inerte de Vasilka ao toque.",
        "narrar": "No salão principal do monastério, a ilusão de serenidade desafia a razão. O chão de mosaicos brancos brilha impecável, e de um realejo dourado emana uma valsa suave e melancólica. Conduzindo uma jovem alta pelos passos da dança está um homem de beleza sobre-humana, com túnica de linho imaculado e olhos de ouro reluzente: o Abade. Ao lado dele, movendo-se com rigidez mecânica, está Vasilka. Sob o vestido de noiva de cetim branco inacabado, finas suturas cirúrgicas de fio de prata unem pedaços de peles de mulheres diferentes para compor um corpo de beleza cadavérica. O Abade para a dança, abre os braços com um sorriso de pura beatitude e declara: 'Não tenham medo, filhos da terra. Eu estou tecendo a noiva que redimirá a alma de Strahd von Zarovich... e trará a luz de volta a este vale.'"
    },
    "K2c": {
        "obj": "Explorar a ala oriental e a torre hospitalar da abadia com Ezmerelda d'Avenir, investigar os laboratórios cirúrgicos do Abade e planejar se confrontarão o anjo caído ou negociarão uma trégua para a vila.",
        "ctx": "Na ala oriental repousam os instrumentos de cirurgia do Abade, livros de anatomia celestial e os aposentos temporários de Ezmerelda. Ezmerelda alerta que o Abade em sua verdadeira forma é um Deva com asas flamejantes e maça radiante devastadora que aniquilará o grupo se atacado sem estratégia.",
        "sights": "Mesas de dissecação de mármore com canaletas de drenagem; serras cirúrgicas, agulhas de prata e frascos de formol; o quarto austero de Ezmerelda com mapas de Ravenloft e estacas de madeira de carvalho talhadas.",
        "sounds": "O som sibilante de Ezmerelda afiando sua lâmina de prata em uma pedra de amolar; e o uivo de vento do precipício.",
        "smells": "Álcool cirúrgico, vinagre de maçã, óleo de cravo e ferro.",
        "touch": "O fio cirúrgico de prata brilhando sob a luz de uma lamparina de latão.",
        "narrar": "Na ala oriental da abadia, longe do salão de dança de Vasilka, a realidade das 'obras de caridade' do Abade revela-se em detalhes cruéis: mesas de cirurgia de pedra manchadas de sangue antigo cercadas por serras ósseas e ganchos de açougueiro. Em uma cela isolada, Ezmerelda desdobra sobre uma mesa de madeira mapas minuciosos dos acessos às masmorras do Castelo Ravenloft. Ela encara o grupo com expressão severa: 'O Abade não é um homem: é um anjo que caiu nas trevas da própria arrogância. Se vocês lutarem contra ele agora, ele os reduzirá a cinzas sagradas. Nossa prioridade é recuperar as relíquias de Ravenloft antes que ele termine o monstro.'"
    },

    # ARC L: THE DEN OF WOLVES
    "L1": {
        "obj": "Rastrear as pegadas de lobos e pistas de carniça pelas escarpas selvagens da borda norte do Lago Baratok para localizar a entrada secreta do temido Covil dos Lobisomens.",
        "ctx": "A alcateia de lobisomens tem seu covil principal em uma caverna natural escavada no rochedo do Monte Baratok, guardada por armadilhas de estacas e sentinelas em forma de lobo camufladas entre os pinheiros.",
        "sights": "Ravinadas escarpadas com rochas afiadas; ossadas roídas de animais espalhadas entre samambaias; a fenda de uma caverna em forma de bocarra de lobo esculpida pela erosão.",
        "sounds": "Uivos ecoando nas profundezas da rocha; o estalar de ossos sendo mastigados por sentinelas; e o farfalhar de arbustos espinhosos.",
        "smells": "Almíscar forte de lobo, urina de demarcação territorial, carniça fresca e terra úmida de caverna.",
        "touch": "A pedra áspera da entrada da caverna gotejando água gelada.",
        "narrar": "A trilha de caça contorna as escarpas vertiginosas do Monte Baratok até alcançar uma garganta árida e sombria. No paredão de rocha nua, uma fenda natural que lembra as mandíbulas abertas de um lobo colossal marca a entrada do covil da alcateia. Ao redor da entrada, dezenas de crânios de cervos e ossadas humanas empaladas em estacas de madeira servem como aviso territorial macabro: vocês pisaram no coração do território dos lobisomens."
    },
    "L2": {
        "obj": "Recuperar suprimentos vitais nas margens do Lago Baratok, desativar armadilhas de laço dos licantropos e preparar emboscadas táticas contra os batedores da alcateia.",
        "ctx": "Os lobisomens mantêm postos avançados de caça na orla da floresta para emboscar pescadores e lenhadores. Destruir os batedores silenciosamente impede que a caverna inteira seja alertada.",
        "sights": "Armadilhas de laço de corda de cânhamo escondidas sob folhas secas; tocas de vigia escavadas sob raízes de carvalhos antigos; batedores lupinos rastejando na grama.",
        "sounds": "O som repentino de armadilha estalando; rosnados baixos de aviso; e o murmúrio do vento nas margens do lago.",
        "smells": "Pinho esmagado, barro úmido e terra mexida recentemente.",
        "touch": "A tensão da corda de aço da armadilha pronta para prender tornozelos desatentos.",
        "narrar": "A floresta que circunda as margens de Baratok é uma teia mortal de armadilhas. Laços de corda pesada e estacas pontiagudas de madeira embebidas em veneno de serpente escondem-se sob a folhagem. Movendo-se com cautela extrema, vocês desarmam os laços dos licantropos antes que os primeiros batedores da matilha possam farejar sua aproximação."
    },
    "L3": {
        "obj": "Montar uma vigília furtiva nas sombras da mata ao redor da caverna, identificar a ausência temporária do líder tirânico Kiril van Holtz em sua caçada noturna, e planejar a infiltração.",
        "ctx": "Kiril lidera uma matilha de caça de oito lobisomens fora do covil durante a noite, deixando a caverna sob a guarda de sua rival Zuleika Toranescu (esposa de Emil, o líder tradicional que foi aprisionado por Strahd nas masmorras de Ravenloft a pedido de Kiril).",
        "sights": "A matilha de caça de Kiril partindo a galope pelas trilhas do vale sob o luar; a caverna iluminada apenas por uma fogueira de tochas fumegantes; Zuleika andando de um lado para o outro na entrada com olhar amargurado.",
        "sounds": "A marcha pesada da matilha de Kiril afastando-se na distância; o gotejar constante de estalactites no interior da rocha; e os soluços débeis de crianças presas ao fundo.",
        "smells": "Fumaça de osso queimado, esterco lupino e vento noturno.",
        "touch": "O frio da rocha onde os heróis aguardam agachados na penumbra.",
        "narrar": "Das sombras dos pinheiros, a vigília dos heróis é recompensada: liderada pelo colossal e cruel Kiril van Holtz, metade da alcateia uiva para a lua cheia e parte a galope para a caçada noturna nas estradas. O covil fica para trás com guarda reduzida. Na entrada da caverna, iluminada pelo fulgor avermelhado de tochas, uma loba cinzenta de grande porte assume a forma de uma mulher musculosa com cicatrizes de batalha: Zuleika Toranescu, a esposa do líder traído."
    },
    "L4": {
        "obj": "Infiltrar o interior do Covil dos Lobisomens, negociar uma aliança tensa com Zuleika Toranescu em troca da promessa de libertar seu marido Emil das masmorras de Ravenloft, e resgatar as crianças barovianas presas nas jaulas.",
        "ctx": "No fundo do covil repousa o altar sagrado de Madre Noite (Mother Night) e jaulas de madeira com seis crianças sequestradas que Kiril planejava forçar a lutar até a morte na próxima lua cheia para infectar os sobreviventes com licantropia. Zuleika odeia Kiril por ter entregue Emil a Strahd e concorda em deixar os heróis levarem as crianças se eles jurarem libertar Emil.",
        "sights": "Salão cavernoso monumental com uma estátua de três metros de uma deusa de pedra sem rosto de cujos olhos escorrem lágrimas de sangue (Madre Noite); piscina natural de água negra; jaulas de madeira rústica com seis crianças assustadas abraçadas; tesouros e bugigangas saqueadas espalhados pelo chão.",
        "sounds": "Choros baixos e aterrorizados das crianças nas jaulas; a respiração tensa de Zuleika segurando uma lança de prata; e o eco cavernoso da água pingando na piscina sagrada.",
        "smells": "Almíscar de fera, incenso amargo de folhas secas, sangue seco nos altares e o cheiro doce de medo infantil.",
        "touch": "As grades de madeira lascada das jaulas arrombadas com alavancas e as mãos trêmulas das crianças salvas.",
        "narrar": "O interior do covil abre-se em uma caverna titânica iluminada por tochas fixadas em estalactites. No centro ergue-se o altar tenebroso de Madre Noite: uma estátua colossal esculpida em pedra obsidiana que chora gotas de sangue na piscina natural abaixo. Em jaulas toscas de madeira no canto norte, seis crianças camponesas choram abraçadas em terror absoluto. Mas antes que as armas sejam erguidas contra os guardas, Zuleika coloca-se entre vocês e as jaulas com os olhos brilhando em desespero materno: 'Vocês querem as crianças? Levem-nas! Mas jurem pela honra de suas almas que quando entrarem naquele maldito castelo de Ravenloft... vocês trarão meu marido Emil de volta para mim!'"
    },

    # ARC M: THE DRAGON'S MANOR (ARGYNVOSTHOLT)
    "M1": {
        "obj": "Subir as colinas enevoadas em direção à monumental mansão fortificada de Argynvostholt, cruzar a floresta de carvalhos antigos assombrada por sombras e testemunhar a imponente estátua de dragão de pedra.",
        "ctx": "Argynvostholt foi a fortaleza da sagrada Ordem do Dragão de Prata, liderada pelo nobre dragão Argynvost. Quando Strahd conquistou o vale, massacrou os cavaleiros e decapitou o dragão, levando seu crânio para Ravenloft. Agora os cavaleiros mortos vagam como revenantes consumidos pelo ódio.",
        "sights": "Um colossal solar fortificado de três pavimentos de pedra cinzenta com torres quadradas e ameias pontiagudas; no centro do pátio frontal, uma estátua monumental de um dragão de prata com asas abertas cujo focinho aponta desafiadoramente para o Castelo Ravenloft.",
        "sounds": "O uivo do vento soprando pelas seteiras vazias da mansão; o estalar de folhas de carvalho secas sob as botas; e o bater distante de armaduras de aço se movendo nas sombras.",
        "smells": "Pedra envelhecida, musgo seco, ferrugem e o odor inconfundível de poeira militar secular.",
        "touch": "O frio intenso de pedra lavrada que não recebe calor de lareira há mais de quatro séculos.",
        "narrar": "Emergindo das brumas das colinas do sul, a silhueta colossal de Argynvostholt ergue-se como uma fortaleza espectral que recusa a morrer. O imponente casarão de pedra calcária, com suas arcadas góticas e torres ameheadas, vigia o vale com orgulho ferido. No centro do pátio de cascalho, sobre um pedestal monumental, ergue-se a estátua majestosa de um dragão com asas estendidas: Argynvost, o dragão de prata ancestral, com o olhar de pedra cravado eternamente na direção do Castelo Ravenloft."
    },
    "M2": {
        "obj": "Explorar o exterior decadente da mansão, inspecionar as brechas nas muralhas provocadas pelo cerco original do exército de Strahd e escolher um ponto de entrada seguro.",
        "ctx": "O casarão guarda cicatrizes da batalha lendária onde o dragão de prata fez sua última resistência contra os generais de Strahd. Janelas quebradas, balcões desabados e portas de ferro maciço marcam os acessos.",
        "sights": "Paredes com marcas de aríetes e catapultas de quatro séculos atrás; vitrais partidos no chão; estátuas decapitadas de cavaleiros com brasões de dragão nos nichos externos.",
        "sounds": "O bater ritmado de uma veneziana quebrada contra a pedra; e o eco de passos pesados patrulhando o andar superior.",
        "smells": "Ferro oxidado, cinzas ancestrais e terra batida.",
        "touch": "O ferro gelado e áspero das aldravas em forma de cabeça de dragão na porta principal.",
        "narrar": "Caminhar ao redor de Argynvostholt é como passear por um campo de batalha congelado no tempo. Grandes blocos de cantaria foram arrancados por máquinas de cerco e repousam na relva morta cobertos de hera. Nos nichos das paredes, esculturas de cavaleiros empunhando espadas de lâmina larga guardam as portas com cabeças quebradas pela fúria dos invasores. Ao empurrarem as portas duplas de ferro forjado, o ranger pesado ecoa pelos salões vazios como um trovão fúnebre."
    },
    "M3": {
        "obj": "Adentrar o saguão principal de Argynvostholt, encontrar o nobre cavaleiro espectral Sir Godfrey Gwilym no refeitório e ouvir a trágica história da Ordem do Dragão de Prata e do Farol Sagrado apagado.",
        "ctx": "Sir Godfrey Gwilym é um revenante nobre e amoroso que foi companheiro do comandante Vladimir Horngaard em vida. Diferente de Vladimir (que deseja que Strahd sofra eternamente na maldição mesmo que isso condene o vale inteiro), Godfrey deseja libertar seus irmãos cavaleiros. Ele revela que se o crânio de Argynvost for resgatado de Ravenloft e depositado no mausoléu, o Farol se acenderá e trará a luz da esperança definitiva.",
        "sights": "Salão monumental com teto de dez metros e escadaria dupla de mármore; tapeçarias puídas exibindo dragões voando sob um sol dourado; Sir Godfrey sentado à cabeceira de uma mesa comprida de banquete, trajando uma armadura completa de placas prateadas com capa azul-marinho gasta e olhos iluminados por chamas azuis de determinação.",
        "sounds": "O som metálico e cadenciado da armadura de Godfrey ao se levantar; e sua voz nobre, profunda e repleta de dor e honra militar.",
        "smells": "Ferro polido, cera velha e o perfume tênue de rosas congeladas.",
        "touch": "A manopla de aço gélida de Godfrey ao cumprimentar os heróis com a continência sagrada dos cavaleiros.",
        "narrar": "No salão de banquetes de Argynvostholt, a luz cinzenta das janelas filtrada por vitrais partidos ilumina uma mesa colossal de carvalho onde armaduras vazias repousam em silêncio solene. À cabeceira da mesa ergue-se uma figura imponente em armadura completa de placas com o emblema do dragão prateado no peito: Sir Godfrey Gwilym. Sob o elmo aberto, seus olhos ardem com chamas azuis e sua voz ressoa com dignidade inabalável: 'Bem-vindos à morada dos esquecidos. Nós somos os cavaleiros que lutaram até o último sopro contra a tirania de Strahd. Nosso comandante Vladimir foi consumido pelo ódio eterno... mas se vocês trouxerem de volta o crânio de nosso lorde Argynvost de Ravenloft e acenderem o farol nesta torre, a alma de meus irmãos encontrará finalmente o descanso e a bênção do amanhecer.'"
    },
    "M4": {
        "obj": "Explorar o primeiro andar de Argynvostholt, desativar os guardas espectrais na capela, desvendar os segredos de Zorya e vasculhar as antigas cozinhas e alojamentos da guarnição.",
        "ctx": "O primeiro andar abriga a Capela do Dragão, as cozinhas e os alojamentos dos soldados. Fantasmas e sombras do cerco original atacam intrusos que não demonstrem a insígnia da Ordem.",
        "sights": "Capela com bancos de madeira tombados e um altar de mármore branco em forma de asa de dragão; vitrais despedaçados exibindo santos cavaleiros; sombras fantasmagóricas lutando batalhas invisíveis nas paredes.",
        "sounds": "O sussurro agoniado de espadas imaginárias se chocando; orações em uníssono de espíritos de guerreiros; e o ranger de portas de madeira maciça.",
        "smells": "Incenso sagrado queimado há séculos, cinzas e poeira.",
        "touch": "Fragmentos afiados de vitrais coloridos espalhados pelo chão de pedra polida.",
        "narrar": "A capela de Argynvostholt guarda a solene majestade de uma época em que o bem resistia de cabeça erguida em Baróvia. O altar de mármore branco, esculpido com a silhueta graciosa de asas de dragão, reflete os relâmpagos através do vitral destruído. Ao cruzarem a nave, silhuetas translúcidas de cavaleiros de joelhos erguem-se empunhando lanças espirituais, desafiando os heróis a provarem sua pureza de propósito antes de avançarem pelos salões sagrados."
    },
    "M5": {
        "obj": "Subir ao segundo pavimento da mansão, explorar as alas residenciais dos nobres cavaleiros, os arquivos históricos e os aposentos dos oficiais da Ordem.",
        "ctx": "Nos quartos dos oficiais e nos arquivos repousam cartas históricas, armas de boa forja de cavalaria e pistas sobre a fraqueza de Strahd e o juramento que selou a maldição dos revenantes.",
        "sights": "Corredores compridos forrados por retratos a óleo de cavaleiros de capa azul; estantes de biblioteca com mapas militares desbotados da conquista de Baróvia; baús de carvalho com uniformes de gala puídos.",
        "sounds": "Passos suaves de fantasmas caminhando pelos corredores acarpetados; o silvo do vento nos vitrais; e o crepitar ilusório de lareiras apagadas.",
        "smells": "Papel envelhecido, pergaminho, couro mofado e cedro.",
        "touch": "A friagem que emana das paredes de cantaria nos corredores sem aquecimento.",
        "narrar": "O segundo pavimento é um corredor de memórias e glórias esquecidas. Retratos a óleo de homens e mulheres em armaduras reluzentes encaram o grupo com olhares austeros através de quatrocentos anos de história. Nas escrivaninhas dos arquivos, diários de guerra relatam os últimos dias da resistência contra as legiões de Strahd, elogiando a bravura de Sir Godfrey e o nobre sacrifício do dragão que protegeu os refugiados até seu coração parar de bater."
    },
    "M6": {
        "obj": "Alcançar os aposentos superiores no terceiro pavimento, confrontar o terrível e amargurado Comandante Vladimir Horngaard em seu trono de ódio, e sobreviver à sua fúria vingativa.",
        "ctx": "Vladimir Horngaard é o líder dos revenantes. Sentado em seu trono com sua montante monumental, ele está completamente louco de ódio: ele se recusa a deixar Strahd morrer, pois acredita que a maldição de ser um prisioneiro vampiro em Ravenloft é a maior tortura possível para seu inimigo. Quem tentar matar Strahd é visto por Vladimir como um inimigo que quer aliviar o sofrimento do conde!",
        "sights": "Salão do trono com estandartes rasgados; Vladimir em armadura enegrecida e amassada por maças de guerra, segurando uma colossal montante de aço fosco com as mãos ossudas; olhos incandescentes com chamas de ódio eterno.",
        "sounds": "A voz estrondosa, gutural e cavernosa de Vladimir que faz tremer os caibros do teto; o raspar pesado de sua espada arrastando pelo assoalho de pedra.",
        "smells": "Ferro queimado, enxofre de vingança e o cheiro sufocante de raiva sobrenatural que não se extingue.",
        "touch": "A aura sufocante de terror que emana do comandante e faz as armas tremerem nas mãos dos heróis.",
        "narrar": "No topo da mansão, em um salão circular cercado por estandartes em tiras, repousa o núcleo da maldição de Argynvostholt: o Comandante Vladimir Horngaard. O revenante colossal ergue-se de seu trono de pedra empunhando uma montante descomunal manchada de sangue seco. Chamas escarlates de puro rancor ardem sob sua viseira de aço, e sua voz troveja com fúria que racha a argamassa das paredes: 'Tolos! Vocês vêm falar de matar Strahd? A morte seria uma misericórdia para aquele monstro! Ele deve sofrer eternamente nesta jaula de brumas... e qualquer um que ouse tentar quebrar sua prisão enfrentará a fúria da minha lâmina!'"
    },
    "M7": {
        "obj": "Subir ao telhado e ao topo da Torre do Farol de Argynvostholt, contemplar a pira apagada do dragão voltada para o Castelo Ravenloft e selar o juramento de resgatar o crânio de Argynvost.",
        "ctx": "O Farol de Argynvostholt é uma torre de 20 metros no topo da mansão com uma gigantesca taça de prata para o fogo sagrado. Se o crânio for devolvido ao mausoléu em Arc Q, o farol acenderá com uma luz solar permanente de trinta quilômetros que concede +2 na CA e testes de resistência para todos os heróis em Baróvia!",
        "sights": "O telhado aberto sob céu tempestuoso a cinquenta metros de altura; o vale de Baróvia inteiro espalhado aos pés do grupo; a pira monumental de prata apagada voltada diretamente para as torres de Ravenloft; relâmpagos iluminando o horizonte.",
        "sounds": "O rugido selvagem do vendaval das montanhas soprando sem obstáculos; trovões que estouram logo acima do telhado; e o sussurro espiritual do dragão Argynvost abençoando os heróis.",
        "smells": "Ar puro, ozônio puro e a brisa livre das alturas.",
        "touch": "A pedra gélida da torre e o metal prateado da pira esperando a centelha do retorno.",
        "narrar": "No topo da torre mais alta de Argynvostholt, o mundo de Baróvia abre-se em uma vista monumental e aterrorizante. O vento montanhoso ruge como um dragão vivo através das ameias de pedra. Diante de vocês, voltada diretamente para o abismo e para a silhueta gótica do Castelo Ravenloft a quilômetros de distância, ergue-se a colossal taça de prata do Farol da Ordem. A pira está fria e apagada há quatro séculos... mas quando vocês tocam o metal com a bênção de Godfrey, um calor tênue de esperança pulsa na pedra: 'Tragam o crânio de meu lorde de volta... e a luz da justiça queimará as sombras deste vale para todo o sempre.'"
    }
}

print(f"Total Act III metadata (Part 1: J, K, L, M) defined: {len(ACT3_METADATA)} scenes.")
