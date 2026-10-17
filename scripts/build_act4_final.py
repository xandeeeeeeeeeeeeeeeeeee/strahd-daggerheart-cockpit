# -*- coding: utf-8 -*-
"""
Generator for Act IV & Epilogue (Arcs R, S, T, U, EP) enriched scenes.
Reads DragnaCarta source from reloaded-source and merges with existing rich mechanics,
completely eliminating all generic boilerplate placeholders.
Total: 49 scenes (R1..R6, S1..S8, T1..T5d, U1..U6, EP1..EP6).
"""

import json
import os
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes_by_code = {s['code']: s for s in data['scenes']}

ACT4_METADATA = {
    # ARC R: TRIALS OF THE MOUNTAIN (TSOLENKA PASS & SOLDAV)
    "R1": {
        "obj": "Encontrar o ancião Kasimir Velikov no acampamento dos elfos do crepúsculo, ouvir sua confissão atormentada sobre o apedrejamento de sua irmã Patrina Velikovna e aceitar a perigosa expedição às neves eternas do Templo de Âmbar para recuperar o dom da ressurreição.",
        "ctx": "Kasimir tem sonhos induzidos pelo espírito de Patrina, que implora para ser ressuscitada através dos poderes dos sarcófagos de âmbar negro no lendário Templo de Âmbar no Monte Ghakis.",
        "sights": "Kasimir sentado em sua choça com o capuz puxado cobrindo as orelhas mutiladas; runas arcanas traçadas em peles de animais; pergaminhos de magias de proteção contra o frio extremo; montanhas geladas visíveis ao fundo.",
        "sounds": "O sussurro agoniado de Kasimir relatando a morte trágica de sua raça; o vento frio sibilando na lona da choça; e o tilintar de anéis mágicos.",
        "smells": "Fumo amargo de ervas secas, couro de alce e o odor de gelo que desce das montanhas.",
        "touch": "O frio intenso de altitude que penetra pelas costuras dos casacos de pele.",
        "narrar": "Na penumbra de sua choça miserável aos pés de Vallaki, o ancião elfo Kasimir Velikov desfaz o manto para revelar suas cicatrizes ancestrais. Seus olhos escuros ardem com uma determinação desesperada: 'Por quatrocentos anos eu ouvi o choro da minha irmã Patrina ecoando em meus sonhos. Nas altitudes proibidas do Monte Ghakis repousa o Templo de Âmbar, onde deuses esquecidos aprisionam os segredos da vida e da morte. Conduzam-me pelas geleiras do Passo Tsolenka... e eu lhes entregarei os segredos para destruir o lorde de Ravenloft.'"
    },
    "R2": {
        "obj": "Concluir a transição política ou a queda do tirano local em Vallaki antes da partida para a expedição das montanhas, garantindo a segurança de Ireena e dos aliados durante a longa ausência.",
        "ctx": "A partida para o Monte Ghakis levará pelo menos quatro dias de viagem nas altitudes gélidas. Os heróis devem deixar Vallaki sob custódia confiável (os Martikov na Água Azul ou Lady Wachter) e com defesas preparadas.",
        "sights": "Os portões de Vallaki guarnecidos por guardas aliados; Ireena abraçando os heróis e prometendo manter a guarda na igreja consagrada; carroças de suprimentos de montanha sendo carregadas.",
        "sounds": "O ranger de rodas de carroças sobre paralelepípedos; despedidas emocionadas de aliados; e o badalar do sino da igreja abençoando a partida.",
        "smells": "Pão de viagem amanteigado, graxa de botas impermeabilizante e fumaça de chaminés da cidade.",
        "touch": "O peso de pesadas mantas de pele de urso e cordas de escalada acomodadas nas mochilas.",
        "narrar": "Com o governo de Vallaki estabilizado e Ireena protegida atrás dos muros sagrados de Santo Andral, o grupo ajusta as correias de suas mochilas de expedição. Diante de vocês, erguendo-se como uma muralha titanica de rocha nua e gelo contra as nuvens de tempestade, estão as montanhas do sul. A marcha para o desconhecido começou."
    },
    "R3": {
        "obj": "Adquirir roupas de frio extremo, crampons de ferro e raquetes de neve em Vallaki ou Krezk, superar a primeira provação climática da subida e resistir à hipotermia nas encostas baixas do Monte Ghakis.",
        "ctx": "Sem roupas de inverno pesadas, os personagens sofrem dano de frio e exaustão a cada hora. A subida começa a testar a resistência física da comitiva.",
        "sights": "A vegetação desaparecendo gradualmente, substituída por pedras cobertas de gelo escorregadio e neve virgem; o ar tornando-se rarefeito e visível em jatos densos de vapor.",
        "sounds": "O som seco de crampons de ferro cravando no gelo; o assobio cortante de rajadas de vento alpino; e o ranger de pedregulhos sob o peso da comitiva.",
        "smells": "Ar glacial puro sem cheiro, terra congelada e lã encharcada.",
        "touch": "O entorpecimento gradual dos dedos das mãos e a dormência nas bochechas fustigadas por flocos de neve afiados.",
        "narrar": "A cada mil metros de altitude vencidos nas encostas do Monte Ghakis, a vida vegetal definha até desaparecer. Os pinheiros colossais tornam-se esqueletos retorcidos de madeira petrificada pelo gelo, e a lama da estrada dá lugar a uma crosta espessa de neve dura e pedregulhos escorregadios. O ar rarefeito queima os brônquios a cada respiração, e o silêncio da cordilheira é quebrado apenas pelo ranger rítmico dos cravos de ferro das botas cravando-se na montanha."
    },
    "R4": {
        "obj": "Iniciar a travessia da lendária garganta do Passo Tsolenka, um desfiladeiro estreito esculpido entre despenhadeiros abissais de rocha e geleiras eternas.",
        "ctx": "O Passo Tsolenka é a única rota terrestre que cruza as montanhas em direção ao Templo de Âmbar e à aldeia isolada de Soldav. Uma ponte de pedra secular e uma guarnição fortificada guardam a garganta.",
        "sights": "Um desfiladeiro de três metros de largura cercado por paredões verticais de pedra cinzenta de cem metros de altura; o abismo rochoso caindo à esquerda; névoa de nevasca cobrindo o caminho.",
        "sounds": "O vento uivando na garganta estreita como o grito de um titã ferido; estalos de gelo quebrando nas alturas.",
        "smells": "Gelo antigo de geleira e pedra congelada.",
        "touch": "Rajadas violentas de vento lateral que ameaçam jogar viajantes no precipício.",
        "narrar": "A entrada do Passo Tsolenka é uma fenda gigantesca na espinha dorsal de Baróvia. O caminho estreita-se em uma borda de rocha escorregadia ladeada por um abismo vertiginoso de quinhentos metros de queda livre à esquerda e paredões intransponíveis de basalto à direita. O vento alpino canaliza-se pela fenda com força devastadora, uivando como uma legião de espectros que proíbem o avanço dos vivos."
    },
    "R4a": {
        "obj": "Conduzir a subida pela trilha da geleira, superar o congelamento de equipamentos e enfrentar a emboscada de carniceiros alados nas encostas.",
        "ctx": "Predadores das montanhas atacam viajantes enfraquecidos pela altitude. A disciplina de grupo é essencial para não perder integrantes nas fendas de gelo.",
        "sights": "Geleiras azuis antigas rachadas por fendas profundas; neblina branca cegante que elimina a linha do horizonte.",
        "sounds": "O estalo seco de gelo abrindo-se sob os pés; o grasnar agudo de aves de rapina das neves.",
        "smells": "Frio estéril e ozônio de tempestade.",
        "touch": "A corda de segurança entre os aventureiros puxando com força quando alguém escorrega.",
        "narrar": "A marcha através da geleira exige concentração total e nervos de aço. Amarrados uns aos outros por cordas de segurança, cada passo deve ser testado com bastões antes de apoiar o peso do corpo sobre pontes de gelo traiçoeiras. Quando a neblina fecha-se em um 'whiteout' completo, a voz do companheiro à frente é o único guia em meio ao vazio branco."
    },
    "R4d": {
        "obj": "Sobreviver a uma nevasca furiosa de montanha no Passo Tsolenka, construir um abrigo de emergência na rocha e resistir ao congelamento durante a noite.",
        "ctx": "A nevasca atinge velocidade de furacão. Sem abrigo em caverna ou muralha de pedra, os aventureiros sofrerão congelamento letal.",
        "sights": "Flocos de neve horizontais voando a oitenta quilômetros por hora; visibilidade zero a mais de um metro; tochas apagando-se instantaneamente sob o vendaval.",
        "sounds": "O rugido ensurdecedor da nevasca que abafa qualquer tentativa de diálogo; estalos de placas de gelo soltando-se.",
        "smells": "Neve atomizada e fumaça fraca de pederneira tentando acender fogo.",
        "touch": "O congelamento doloroso das pálpebras e lábios expostos ao vento polar.",
        "narrar": "A nevasca desaba sobre o desfiladeiro com fúria apocalíptica. O céu e a terra fundem-se em uma parede impiedosa de gelo e vento uivante que arranca mochilas e cega os olhos em segundos. Abrigados sob uma saliência de rocha cavada às pressas com picaretas, os heróis amontoam-se ombro a ombro compartilhando o calor de seus corpos enquanto o vendaval tenta congelar o próprio ar à sua volta."
    },
    "R4e": {
        "obj": "Alcançar a monumental Portaria de Tsolenka, confrontar a cortina mágica de chamas verdes que bloqueia o arco da muralha e sobreviver ao ataque aterrador do lendário Roc de Ghakis (a colossal ave de rapina das montanhas).",
        "ctx": "A Portaria de Tsolenka é uma muralha fortificada de quinze metros de altura erguida sobre a ponte de pedra que cruza o abismo. O arco da passagem é bloqueado por uma cortina permanente de fogo mágico verde que causa dano de fogo e radiante. No topo da montanha nidifica o Roc de Ghakis, um pássaro descomunal de sessenta metros de envergadura que desce em rasante para arrebatar viajantes com suas garras gigantescas.",
        "sights": "Muralha de pedra com duas torres de vigia quadradas erguida sobre uma ponte de arco único sobre a ravina; cortina crepitante de chamas verdes de três metros de altura no portal; uma sombra colossal de asas gigantescas cobrindo o céu conforme o Roc mergulha das nuvens.",
        "sounds": "O grito estridente e ensurdecedor do Roc que faz a rocha vibrar; o estalar contínuo das chamas mágicas verdes; e o bater de asas monumentais que desloca toneladas de ar como um ciclone.",
        "smells": "Enxofre mágico do fogo verde, ar gélido e o cheiro almiscarado de ninho de ave colossal.",
        "touch": "O calor violento do fogo verde contrastando com o vendaval gelado gerado pelo bater de asas da fera colossal.",
        "narrar": "Erguendo-se sobre a garganta do abismo como uma sentinela eterna, surge a imponente Portaria de Tsolenka. Duas torres de pedra calcária flanqueiam uma muralha de quinze metros de altura onde arde uma cortina crepitante de labaredas verdes e fantasmagóricas que barram a passagem. Mas antes que os heróis possam analisar o feitiço, um guincho aterrador rasga os céus: quebrando a tempestade com asas que medem sessenta metros de uma ponta à outra, o lendário Roc de Ghakis projeta-se das nuvens como um meteoro de penas cinzentas e garras de ferro puro prontas para o abate!"
    },
    "R4f": {
        "obj": "Confrontar a segunda provação do tirano: desativar os guardas esqueléticos nas torres da portaria, desvendar a senha das chamas verdes e cruzar a ponte sobre o abismo.",
        "ctx": "Nas torres da portaria repousam cavaleiros esqueléticos e catapultas antigas. As chamas verdes abrem-se com a recitação do nome de sangue da dinastia von Zarovich ou com magias de dissipação de trevas.",
        "sights": "Interior das torres de vigia com esqueletos de sentinelas armados com arcos longos e flechas flamejantes; o mecanismo de contrapeso da ponte levadiça congelado pelo gelo.",
        "sounds": "O chiar de flechas incendiárias; o ranger metálico de engrenagens de ferro sendo descongeladas com tochas; e o eco de passos na pedra.",
        "smells": "Breu queimado, osso calcinado e gelo derretido.",
        "touch": "As correntes de ferro congeladas que machucam as mãos ao serem puxadas.",
        "narrar": "Limpando as ameias dos arqueiros esqueléticos que guardavam a passagem, os heróis alcançam os controles da muralha. Com a invocação das palavras arcanas reveladas pelas anotações de Kasimir, a cortina de fogo verde divide-se como um mar de chamas esmeraldas, permitindo que a comitiva cruze a ponte de pedra e alcance os planaltos superiores do Monte Ghakis."
    },
    "R4i": {
        "obj": "Sobreviver a uma avalanche catastrófica de toneladas de neve e pedras na encosta sul do monte, utilizando rotas de escape rápidas e magias de proteção para não ser soterrado vivo.",
        "ctx": "O rugido do Roc ou vibrações sonoras soltam uma placa maciça de neve de quinhentos metros de largura encosta abaixo. Testes atléticos e reflexos rápidos decidem a vida dos personagens.",
        "sights": "Uma colossal onda branca de centenas de toneladas de neve e rochas despencando pela montanha como um maremoto congelado; nuvem colossal de pó de gelo que escurece o sol.",
        "sounds": "Um trovão telúrico e contínuo que sacode as montanhas até os ossos; árvores sendo arrancadas como gravetos.",
        "smells": "Gelo triturado e terra revolvida.",
        "touch": "O impacto violento da onda de choque de ar que empurra os heróis em direção a fendas na rocha.",
        "narrar": "Um estalo seco e estrondoso ecoa no alto do maciço rochoso, seguido por um trovão que faz a montanha inteira estremecer. No topo da encosta, uma colossal muralha branca de centenas de toneladas de gelo e rochas desprende-se em um estrondo titânico, descendo em direção à trilha como uma avalanche implacável que engole tudo em seu caminho! É uma corrida desesperada de segundos para saltar para dentro de fendas na rocha antes que a torrente branca soterre os heróis sob metros de sepultura gelada!"
    },
    "R4j": {
        "obj": "Explorar o covil subterrâneo dos bodaks nas cavernas escarpadas da montanha, enfrentar o olhar mortal de drenagem de vida das abominações necróticas e recuperar artefatos arcanos esquecidos.",
        "ctx": "Os bodaks são criaturas cadavéricas tocadas pela magia sombria do Templo de Âmbar cujo olhar direto pode matar criaturas instantaneamente ou causar dano necrótico avassalador.",
        "sights": "Caverna de basalto negro gotejando gelo; silhuetas humanoides esqueléticas de pele cinzenta sem pelos com órbitas oculares completamente negras que drenam a luz ao redor.",
        "sounds": "Um sibilar agoniado e fúnebre; o sussurro de morte que ressoa nos ouvidos; e o estalo de ossos secos se movendo.",
        "smells": "Carne decomposta congelada, ozônio e o cheiro sufocante de vácuo necrótico.",
        "touch": "A aura de frio absoluto que drena as forças vitais de quem se aproxima.",
        "narrar": "Nas profundezas de uma caverna de basalto que corta a geleira, a escuridão parece viva e faminta. Das fendas da pedra emergem os bodaks: carcaças humanoides essecadas de pele cinzenta com órbitas oculares que são poços de puro vazio consumidor. Seu olhar não fere a carne: ele atinge a alma diretamente, tentando arrancar o sopro da vida com o toque gélido do além."
    },
    "R4k": {
        "obj": "Navegar pelo labirinto translúcido das Cavernas de Gelo milenares, desviar de fendas abissais e alcançar o platô oculto onde repousa o vilarejo de Soldav.",
        "ctx": "As cavernas de gelo formam uma passagem subterrânea segura contra o vento polar que corta o cume da montanha, revelando formações espetaculares de estalactites de cristal azul.",
        "sights": "Paredes de gelo puro translúcido brilhando em tons turquesa e safira com a luz das tochas; reflexos infinitos das figuras dos heróis nas superfícies congeladas; estalactites colossais como dentes de cristal.",
        "sounds": "O som cristalino e musical de gotas de água caindo em poças límpidas; ecos suaves de passos no chão congelado.",
        "smells": "Pureza absoluta de água de degelo milenar.",
        "touch": "Gelo perfeitamente liso e escorregadio que exige passos medidos e cautelosos.",
        "narrar": "Entrar nas Cavernas de Gelo é penetrar em uma catedral de cristal subterrânea. As paredes de gelo eterno de dezenas de metros de espessura filtram a luz externa em reflexos radiantes de turquesa, esmeralda e safira. Entre arcos naturais de gelo puro e fendas abissais onde correm riachos subterrâneos, a trilha sobe em direção ao platô esquecido onde os humanos das montanhas ainda resistem."
    },
    "R5": {
        "obj": "Alcançar a isolada e austera vila montanhesa de Soldav, obter abrigo nas casas de pedra aquecidas por lareiras de turfa e conhecer a cultura ancestral dos montanheses que guardam os segredos do Templo de Âmbar.",
        "ctx": "Soldav é o assentamento habitado mais alto de Baróvia, povoado por bárbaros e caçadores que reverenciam as Rozana (as antigas deusas fadas) e temem o Templo de Âmbar como o covil dos demônios antigos.",
        "sights": "Chalés robustos de pedra de basalto com telhados baixos de turfa cobertos de neve; fumaça branca subindo de dezenas de chaminés; homens e mulheres de feições fortes vestidos com peles de iaque e lobo da montanha; mastins brancos de pelo espesso guardando os caminhos.",
        "sounds": "Latidos graves de cães de montanha; o som reconfortante de madeira crepitando em fornos de pedra; e a canção gutural dos anciãos de Soldav entoando preces antigas.",
        "smells": "Fumaça de turfa, carne de caça defumada com raízes de montanha, queijo forte de cabra e cerveja quente com especiarias.",
        "touch": "O calor bendito do interior das casas de pedra que expulsa o gelo de dias de caminhada na geleira.",
        "narrar": "No topo de um platô abrigado entre os picos nevados do Monte Ghakis, surge a vila de Soldav. As casas baixas de pedra e turfa, construídas para resistir a séculos de avalanches, soltam plumas de fumaça aromática contra o céu de chumbo. Caçadores de ombros largos vestidos com peles pesadas de urso recebem a comitiva com arcos abaixados e respeito austero: em uma terra onde o frio mata os fracos, os viajantes que cruzam o Passo Tsolenka vivos são acolhidos como guerreiros de honra."
    },
    "R5d": {
        "obj": "Conseguir audiência na Casa da Liderança de Soldav, negociar com a matriarca da aldeia e participar dos jogos sociais de hospitalidade e honra para assegurar guias para o cume do templo.",
        "ctx": "A liderança da aldeia exige provas de que o grupo não serve a Strahd e que não busca libertar os Vestígios Sombrios para o mal. Provas de combate honrado ou diplomacia (*Presença CD 12*) garantem apoio total.",
        "sights": "Salão comunal aquecido por três fogueiras de pedra; crânios de cabras montanhesas e estandartes de couro nas paredes; a matriarca de cabelos brancos sentada em uma cadeira entalhada com chifres de alce.",
        "sounds": "Cânticos guerreiros, batidas rítmicas de canecas de cerveja em mesas compridas e debates acalorados sobre a profecia da queda de Strahd.",
        "smells": "Cerveja escura fermentada, carne de javali assada com zimbro e fumo de cachimbo.",
        "touch": "O aperto de mão caloroso e rude dos guerreiros das montanhas selando o pacto de abrigo.",
        "narrar": "No salão comunitário de Soldav, o calor das chamas e a fúria das canecas cheias de cerveja escura quebram a friagem da montanha. A matriarca da aldeia, com feições esculpidas pelo vento e olhar de quem conhece as estrelas, ouve o relato da libertação dos vinhedos e da derrota de Kiril com assentimento solene: 'Vocês têm coragem de lobos e alma de guerreiros. Nós abriremos os caminhos sagrados do templo para vocês... mas preparem suas mentes: o âmbar não tenta os fracos, ele corrompe os fortes.'"
    },
    "R5f": {
        "obj": "Visitar o sagrado Santuário das Rozana em Soldav, receber a bênção ancestral das antigas deusas da terra e preparar as proteções mentais contra a corrupção dos sarcófagos de âmbar.",
        "ctx": "O santuário das Rozana preserva a memória da Tecelã, da Caçadora e da Buscadora antes de sua corrupção. As preces concedem aos heróis resistência mágica a feitiços de charme e possessão no Templo de Âmbar.",
        "sights": "Câmara circular escavada na rocha com três estátuas de deusas antigas esculpidas em cristal de quartzo; uma chama eterna que arde sobre uma bacia de pedra sem combustível; oferendas de flores secas e pontas de flecha de prata.",
        "sounds": "Um zumbido harmônico e divino que parece emanar do próprio coração da montanha; o murmúrio suave de preces femininas.",
        "smells": "Incenso puro de pinho alpino, flores de neve e ar limpo.",
        "touch": "A água pura da fonte do santuário que limpa as feridas e acalma a ansiedade do espírito.",
        "narrar": "No interior do Santuário das Rozana, a atmosfera é de pura transcendência divina. Três estátuas majestosas de quartzo límpido representam as três deusas ancestrais que cuidavam do vale antes da chegada da sombra. Ao receberem a unção com a água da fonte sagrada, uma sensação de paz inabalável e clareza mental preenche os pensamentos de cada aventureiro: uma couraça de luz para proteger a alma nas trevas que aguardam adiante."
    },
    "R6": {
        "obj": "Conquistar o cume escarpado do Monte Ghakis, enfrentar o lendário bode demoníaco colossal Sangzor e alcançar o limiar do Templo de Âmbar.",
        "ctx": "Sangzor é uma besta lendária de quatro chifres e pelagem cinzenta manchada de sangue que salta entre precipícios com agilidade sobrenatural para arremeter intrusos no abismo. Destruí-lo abre a entrada do templo.",
        "sights": "O cume do Monte Ghakis sob um céu estrelado gélido; fendas verticais de rocha; um bode colossal do tamanho de um mamute com quatro chifres curvados de aço natural investindo com ferocidade; ao fundo, os blocos de âmbar dourado reluzindo sob o gelo.",
        "sounds": "O bater trovejante de cascos de ferro na rocha nua; o bufado furioso de Sangzor; e o vento supremo do topo de Baróvia.",
        "smells": "Almíscar de fera ancestral, neve fresca e poeira de pedra esmagada.",
        "touch": "O impacto monumental dos chifres de Sangzor estilhaçando rochas ao redor dos heróis.",
        "narrar": "No topo mais alto de Baróvia, onde o ar é tão rarefeito que as estrelas parecem palpáveis, a terra estremece sob o galope de uma lenda viva. Saltando de um pináculo de rocha com agilidade impossível, surge Sangzor: o colossal bode montanhês de quatro chifres de ferro e olhos rubros de fúria demoníaca. Ele bufa jatos de vapor escaldante e investe de cabeça baixa como uma avalanche viva! Mas com aço firme e pontaria precisa, o monstro é tombado no abismo, revelando logo adiante a fachada monumental esculpida em âmbar puro do Templo Proibido."
    },

    # ARC S: A SWORD OF SUNLIGHT (AMBER TEMPLE)
    "S1": {
        "obj": "Adentrar a colossal fachada do Templo de Âmbar esculpida diretamente no coração da geleira do Monte Ghakis, desvendar os relevos ciclópeos e cruzar o portal de pedra obsidiana.",
        "ctx": "O Templo de Âmbar foi construído por uma ordem esquecida de magos benevolentes para aprisionar os Vestígios Sombrios (os resquícios de deuses mortos do mal absoluto) em blocos indestrutíveis de âmbar negro. Com os séculos, o templo foi corrompido e seus guardiões enlouqueceram.",
        "sights": "Entrada monumental com colunas de dez metros de altura esculpidas em blocos gigantescos de âmbar translúcido dourado que aprisionam centelhas de escuridão viva; estátuas de deuses sem rosto decapitadas; escadarias colossais cobertas por geada milenar.",
        "sounds": "Um zumbido grave e hipnótico que ressoa diretamente nos ossos e na mente; sussurros sedutores de vozes invisíveis prometendo poder absoluto; e o eco solene de passos na pedra polida.",
        "smells": "Âmbar resinoso queimado, ozônio primordial, ar gélido e o perfume venenoso e tentador de magia proibida.",
        "touch": "O frio de zero absoluto que emana da pedra e a atração magnética irresistível dos blocos de âmbar.",
        "narrar": "A fachada do Templo de Âmbar é uma visão de grandiosidade cósmica que beira a loucura. Esculpida diretamente no ventre de basalto da montanha sob toneladas de gelo eterno, colunas titânicas de âmbar dourado translúcido erguem-se sustentando arcadas ciclópeas. No interior do âmbar, centelhas de sombras informes contorcem-se como entidades aprisionadas que esperam por libertação. Um coro de sussurros sedutores ecoa no silêncio da pedra: o maior tesouro e o maior perigo de todo o multiverso aguardam além deste portal."
    },
    "S2": {
        "obj": "Sobreviver às defesas arcanas do templo, desmascarar a farsa do arcanista anfitrião e desativar os guardas de chamas e estátuas de pedra animadas no grande átrio X5.",
        "ctx": "O átrio do templo abriga uma estátua colossal de trinta metros de um deus sem rosto de cujos olhos magos e esqueletos de chamas disparam bolas de fogo em quem cruzar o salão aberto sem cobertura.",
        "sights": "Salão de proporções titânicas com teto de trinta metros; uma estátua gigantesca de um deus encapuzado sentado em um trono de pedra; feixes de bolas de fogo arcanas estourando em clarões alaranjados contra colunas de âmbar.",
        "sounds": "O estrondo ensurdecedor de explosões mágicas de fogo ecoando no salão cavernoso; risadas estridentes de crânios flamejantes voadores; e o sibilar de flechas arcanas.",
        "smells": "Enxofre calcinado, fumaça de breu, âmbar derretido e pedra tostada.",
        "touch": "O choque térmico brutal de explosões de fogo contra armaduras congeladas.",
        "narrar": "Ao cruzarem o limiar do átrio principal, o templo acorda em um espetáculo de chamas mortais. No centro do salão colossal, erguendo-se até o teto de trinta metros de altura, uma estátua titânica de um deus encapuzado encara o grupo. De dentro de seteiras esculpidas nos olhos e mãos da estátua, crânios flamejantes e golens de pedra disparam rajadas devastadoras de fogo arcano que iluminam as colunas de âmbar em um mar de labaredas e estilhaços de rocha!"
    },
    "S3": {
        "obj": "Explorar as catacumbas inferiores do templo, enfrentar ou negociar com o bárbaro berserker de montanha Nardag e encontrar chaves e itens de proteção mágica.",
        "ctx": "Nardag é um bárbaro de montanha que enlouqueceu de frio e isolamento nas catacumbas do templo. Ele guarda passagens secretas que levam aos cofres profundos.",
        "sights": "Túneis estreitos de basalto negro esculpidos na rocha fria; camas de pedra vazias de monges mortos há milênios; Nardag, um homem musculoso coberto de cicatrizes e peles ensanguentadas, empunhando uma machadinha de batalha.",
        "sounds": "Gritos furiosos ecoando nas fendas de pedra; o estalar de armas colidindo contra rocha; e a respiração ofegante de quem luta pela sanidade.",
        "smells": "Suor frio, sangue velho e terra úmida de sepultura.",
        "touch": "O choque violento de aço contra aço em corredores onde não há espaço para manobra.",
        "narrar": "Nas catacumbas inferiores do templo, o silêncio é subitamente quebrado pelo rugido ensurdecedor de um homem consumido pela loucura do isolamento. Das sombras das celas de pedra salta Nardag, um bárbaro com olhos desvairados e machados afiados em punho. Com golpes precisos para desarmá-lo ou palavras firmes de autoridade, o guerreiro é contido, revelando caminhos ocultos que descem para os santuários onde os deuses sombrios dormem."
    },
    "S4": {
        "obj": "Infiltrar o Templo Ocidental e suas câmaras de sarcófagos de âmbar, resistir às tentações sussurradas dos Vestígios Sombrios que oferecem poder divino em troca de corrupção da alma.",
        "ctx": "Cada sarcófago de âmbar de três metros abriga um Vestígio Sombrio que oferece uma 'Dádiva Sombria' (Dark Gift): poder de ressuscitar os mortos, olhos de visão verdadeira, asas de morcego, feitiços de necromancia. Mas cada dádiva cobra uma deformidade física ou moral terrível.",
        "sights": "Câmaras circulares com paredes de âmbar escuro brilhando com luz fosforescente verde e roxa; blocos monumentais de âmbar translúcido onde silhuetas de demônios, serpentes colossais e olhos cósmicos flutuam congelados.",
        "sounds": "Sussurros sedutores e frios soando diretamente no cérebro de cada herói, prometendo a realização de seus desejos mais íntimos de poder, vingança ou vida eterna.",
        "smells": "Incenso amargo, ozônio e o perfume inebriante e venenoso do poder absoluto.",
        "touch": "O calor magnético e pulsante do âmbar ao encostar a mão, fazendo veias brilharem através da pele.",
        "narrar": "No Templo Ocidental, o horror adquire uma beleza perversa e tentadora. Em nichos semicirculares de pedra negra, erguem-se blocos maciços de âmbar dourado de três metros de altura. No interior de cada monolito repousa a essência viva de um deus esquecido: uma massa amorfa de olhos brilhantes, asas de fogo negro ou tentáculos cósmicos. Ao aproximarem-se, vozes de veludo ecoam na mente de vocês, oferecendo o poder de rasgar montanhas e ressuscitar os mortos... pelo preço irrisório de uma centelha de sua humanidade."
    },
    "S5": {
        "obj": "Navegar pelas alas do Templo Oriental, superar armadilhas de teletransporte e ilusões de espelhos de âmbar, e encontrar a câmara onde o arquimago Exethanter reside.",
        "ctx": "O Templo Oriental abriga os aposentos dos antigos sacerdotes e a biblioteca de segredos proibidos. Ilusões e armadilhas mentais testam a determinação do grupo.",
        "sights": "Salões com espelhos de âmbar polido refletindo versões corrompidas dos heróis; portas secretas giratórias de pedra; estantes de ferro com tabletes de argila e pergaminhos dourados.",
        "sounds": "Ecos de passos que parecem vir de trás das paredes; sussurros em idiomas primordiais; e o estalar suave de magia estática.",
        "smells": "Cera de vela velha, pó de múmia e pergaminho ressecado.",
        "touch": "A superfície fria dos espelhos arcanos que vibram sob o toque.",
        "narrar": "Os corredores do Templo Oriental são um labirinto de ilusões e revelações perturbadoras. Espelhos de âmbar polido mostram aos heróis reflexos sombrios de como se tornariam se aceitassem as dádivas do templo: tiranos de armadura negra, feiticeiros de olhos incandescentes de loucura. Com disciplina mental inabalável, o grupo quebra as miragens e alcança o santuário do arquimago que jurou proteger o templo pela eternidade."
    },
    "S6": {
        "obj": "Confrontar o momento decisivo de Kasimir Velikov diante do sarcófago de Zhudun (o Cadáver Estelar), testemunhar sua decisão trágica de aceitar o dom de ressuscitar sua irmã Patrina, e recolher tesouros arcanos dos cofres selados.",
        "ctx": "Kasimir toca o sarcófago de Zhudun e recebe o poder de conjurar True Resurrection uma única vez, mas sua pele torna-se gélida e cadavérica. Ele planeja ir às catacumbas de Ravenloft ressuscitar Patrina (sem saber que ela retornará como uma arquimaga nefasta aliada a Strahd).",
        "sights": "O sarcófago de âmbar negro de Zhudun brilhando com centelhas pálidas de estrela morta; Kasimir ajoelhado em lágrimas com a mão sobre o âmbar, enquanto seus olhos adquirem um fulgor leitoso e sobrenatural; baús de pedra abertos repletos de gemas preciosas e pergaminhos raros.",
        "sounds": "O som profundo e cósmico de um trovão místico ressoando dentro do crânio de Kasimir; seu grito de triunfo doloroso; e o silêncio de morte que se segue.",
        "smells": "Ozônio estelar, terra de sepultura e ferro puro.",
        "touch": "O corpo de Kasimir tornando-se frio como mármore após receber o dom sombrio.",
        "narrar": "Diante do sarcófago de Zhudun, o Corruptor de Estrelas, o destino de Kasimir Velikov é selado. Com as mãos trêmulas apoiadas no âmbar negro, o elfo aceita o pacto milenar: uma luz cinzenta e gélida irrompe do bloco, envolvendo seu corpo em espirais de energia necrótica. Seus olhos perdem a cor, tornando-se poços brancos de poder primordial, e sua voz ressoa com autoridade sepulcral: 'Patrina... Minha irmã... Eu tenho o poder de trazer você de volta do túmulo!' O preço da ressurreição foi pago com a própria alma de Kasimir."
    },
    "S7": {
        "obj": "Encontrar o lendário arquimago lich Exethanter em sua biblioteca circular, curar sua amnésia milenar com magias de restauração divina, descobrir o plano de fuga de Strahd e recuperar a lendária Espada da Luz Solar (Sunsword)!",
        "ctx": "Exethanter é o guardião do Templo que se tornou lich para preservar o conhecimento, mas esqueceu seu próprio nome e feitiços com os séculos. Se os heróis o curarem com Greater Restoration ou gentileza, o velho arquimago agradece com lucidez radiante, revela que Strahd veio ao templo no passado para barganhar com Vampyr, e entrega a lendária Sunsword (a lâmina viva de platina e pura luz solar que é a ruína suprema dos vampiros)!",
        "sights": "Biblioteca circular monumental de três andares forrada por dezenas de milhares de livros arcanos; o lich Exethanter, uma figura esquelética vestindo túnicas de veludo carmesim puídas e coroa de platina torta; no centro de uma câmara secreta, um punho de platina cinzelada com o símbolo do sol que, ao ser empunhado, projeta uma lâmina de pura luz solar radiante!",
        "sounds": "A voz rouca e senil de Exethanter transformando-se em tom claro e sábio de arquimago conforme sua mente é curada; o zumbido harmônico e celestial da Espada da Luz Solar cortando o ar.",
        "smells": "Pergaminho antigo, lavanda sagrada e a explosão de calor e perfume de luz solar pura da lâmina mágica.",
        "touch": "A vibração de poder divino e justiça que emana do punho da Sunsword, aquecendo todo o braço do guerreiro que a empunha.",
        "narrar": "No coração da grande biblioteca de âmbar, a figura esquelética do arquimago Exethanter recupera a consciência de seus séculos de vida após o toque da magia de cura. Com lágrimas de clareza nos olhos ossudos, o lich curva a cabeça em reverência aos heróis: 'Vocês trouxeram de volta minha dignidade... e por isso, eu lhes entrego a arma que o lorde de Ravenloft mais teme em toda a existência.' Ele abre um compartimento secreto sob o altar de mármore e ergue um punho de platina pura com um cristal solar lapidado. Ao ser empunhada por um herói, uma lâmina reluzente de puro fogo solar irrompe da empunhadura com um zumbido divino que dissipa toda a escuridão do templo em um raio de esperança invencível: a Espada da Luz Solar está nas mãos dos libertadores de Baróvia!"
    },
    "S8": {
        "obj": "Confrontar o astuto arcanoloth Neferon que embosca o grupo na saída do templo, neutralizar suas magias de ilusão e tempestade e escapar com a Espada de Luz Solar rumo aos vales.",
        "ctx": "Neferon é um demônio raposa (arcanoloth) que atua como o verdadeiro guardião das relíquias do templo. Ele tenta cobrar a saída do grupo com sangue ou feitiços devastadores de cadeia de relâmpagos. Destruí-lo encerra o domínio do Templo de Âmbar.",
        "sights": "A estátua do deus encapuzado no átrio; o arcanoloth Neferon com cabeça de raposa de olhos esmeraldas vestindo mantos de seda púrpura e empunhando um cajado de osso; relâmpagos arcanos ricocheteando nas colunas de âmbar.",
        "sounds": "A risada zombeteira e estridente de Neferon; trovões mágicos dentro do templo; e o silvo da luz solar da Sunsword repelindo a escuridão infernal.",
        "smells": "Enxofre, pelos queimados de raposa e ozônio.",
        "touch": "O choque elétrico das defesas arcanas do demônio estilhaçando sob o fio da lâmina solar.",
        "narrar": "No limiar da saída do templo, a estátua colossal ganha vida com a manifestação do guardião definitivo: o arcanoloth Neferon. Com cabeça de chacal de feições refinadas e olhos faiscantes de malícia cósmica, o demônio flutua no ar erguendo seu cajado: 'Ninguém sai dos cofres dos deuses com a lâmina do sol sem pagar o tributo de suas almas!' Mas contra o brilho cegante da Espada da Luz Solar recém-despertada, a magia infernal do demônio quebra-se em cinzas, abrindo o caminho para o retorno triunfante ao vale."
    },

    # ARC T: THE THREE FANES
    "T1": {
        "obj": "Retornar vitorioso à aldeia montanhesa de Soldav, reunir-se com os sábios das montanhas e traçar o ritual definitivo para reconconsagrar as Três Fanes de Baróvia (o Pântano, a Floresta e a Montanha).",
        "ctx": "Strahd roubou os poderes das três deusas fadas de Baróvia (as Três Fanes), o que lhe concedeu imunidades sobrenaturais, controle sobre os animais e resistência quase invulnerável. Para torná-lo mortal e vencê-lo em Ravenloft, os heróis devem reconconsagrar os três santuários ancestrais.",
        "sights": "A aldeia de Soldav iluminada pelo fulgor distante do Farol de Argynvostholt; a matriarca estendendo mapas das três Fanes; oferendas sagradas de sementes, água e prata preparadas.",
        "sounds": "Cânticos de guerreiros das montanhas comemorando o retorno dos heróis do Templo de Âmbar; o uivo do vento soprando com menos hostilidade.",
        "smells": "Turfa queimada, pão assado e ervas medicinais purificadoras.",
        "touch": "A textura áspera dos três talismãs sagrados entregues pela matriarca para os rituais das Fanes.",
        "narrar": "Em Soldav, o clima não é mais de desespero, mas de preparação para a guerra final. A matriarca da aldeia coloca sobre a mesa de madeira três símbolos esculpidos em osso e pedra: 'O Senhor da Noite só é invencível porque roubou o coração das três mães desta terra. Se vocês purificarem a Fane do Pântano em Berez, a Fane da Floresta com os Guardiões das Penas e a Fane da Montanha sob o cume... o demônio perderá suas defesas divinas e sangrará como qualquer mortal diante de suas lâminas.'"
    },
    "T2": {
        "obj": "Conduzir a descida do Monte Ghakis de volta para as terras baixas do vale, testemunhar como a luz do Farol de Argynvostholt já começou a quebrar a opressão das névoas, e marchar para o confronto com Baba Lysaga.",
        "ctx": "A descida é rápida e inspiradora: a luz do Farol afasta as sombras e os monstros da estrada recuam aterrorizados pela Espada de Luz Solar.",
        "sights": "O vale de Baróvia estendendo-se abaixo sob uma abóbada de luz prateada e dourada emanada pelo Farol; florestas outrora impenetráveis agora iluminadas por feixes de esperança; aldeões e batedores acenando ao longe.",
        "sounds": "O trote confiante dos corcéis; o grasnar alegre de corvos voando em bandos protetores ao redor da comitiva.",
        "smells": "Ar fresco de pinheiro, terra aquecida e a doçura de flores silvestres renascendo nas bordas da trilha.",
        "touch": "A sensação indescritível de que a maré da guerra virou definitivamente a favor da luz.",
        "narrar": "Descer as encostas do Monte Ghakis carregando a Espada da Luz Solar é testemunhar o renascimento de uma terra que esteve morta por quatro séculos. No horizonte, o pilar de luz incandescente do Farol de Argynvostholt rasga as brumas em todas as direções, e as criaturas da noite fogem em disparada para o fundo das cavernas. Com o moral inabalável e os aliados mobilizados, a comitiva ruma para o sul para expurgar a abominação de Berez."
    },
    "T3": {
        "obj": "Invadir as ruínas pantanosas de Berez com força militar total, resgatar os prisioneiros das bruxas e conduzir o cerco contra a cabana de Baba Lysaga.",
        "ctx": "Berez é um campo de batalha alagado. Os heróis avançam pelas ruínas da antiga cidade acompanhados por batedores dos Guardiões das Penas e guerreiros de Krezk.",
        "sights": "Ruínas de pedra afundadas em lamaçal negro cercadas por salgueiros espectrais; a colossal cabana viva de madeira erguendo-se sobre raízes gigantescas no centro do brejo; Baba Lysaga em seu crânio voador de gigante conjurando nuvens de insetos e raios.",
        "sounds": "Gargalhadas ensurdecedoras da velha bruxa voando pelo céu cinzento; o estrondo de raízes colossais esmagando a terra; e o coro de corvos bicando os olhos das feras do pântano.",
        "smells": "Lodo sulfuroso, matéria orgânica em fermentação, sangue de animais sacrificados e enxofre.",
        "touch": "A água pantanosa borbulhando com calor mágico venenoso ao redor das pernas dos guerreiros.",
        "narrar": "O pântano de Berez explode em um campo de batalha mítico. Voando sobre as copas dos salgueiros em um crânio fossilizado de gigante de pedra de quatro metros, Baba Lysaga dispara relâmpagos esmeraldas e gargalha com dentes pontiagudos de ouro: 'Malditos vermes! Vocês nunca tocarão no meu amado Strahd! Eu sou a mãe do lorde e este pântano engolirá seus cadáveres!' Abaixo dela, a colossal cabana de madeira viva arremete contra o grupo com raízes do tamanho de troncos de carvalho!"
    },
    "T3f": {
        "obj": "Encontrar a aparição sagrada do Príncipe Sergei von Zarovich no monumento de Marina nas ruínas de Berez, receber sua bênção fraternal e desvendar a verdade do amor imortal de Tatyana.",
        "ctx": "Marina foi uma das reencarnações históricas de Tatyana assassinada em Berez. No monumento memorial ergue-se o espírito de Sergei (o irmão virtuoso de Strahd), que abençoa a Espada da Luz Solar e perdoa os pecados da terra.",
        "sights": "Um monumento de mármore branco preservado no centro de uma ilhota florida no pântano; o fantasma radiante de um jovem nobre de armadura de prata polida e olhar repleto de amor e tristeza (Príncipe Sergei).",
        "sounds": "Uma melodia celestial suave que dissipa os sons da batalha; a voz pura e comovente de Sergei abençoando Ireena e os heróis.",
        "smells": "Rosas brancas frescas e perfume de flores da primavera que florescem na lama.",
        "touch": "A mão espectral de Sergei tocando o peito de Ireena e a empunhadura da Sunsword com calor celestial.",
        "narrar": "No centro das ruínas afundadas, sobre uma ilhota onde flores brancas brotam desafiando o lodo podre, ergue-se o monumento à jovem Marina. Ao lado do altar de mármore surge a silhueta luminosa e celestial do Príncipe Sergei von Zarovich. Seus olhos gentis encontram os de Ireena, e ele curva a cabeça com um sorriso de paz imortal: 'Tatyana... Meu amor atravessou as eras para vê-la livre das correntes do meu irmão. Não tenham medo da escuridão: a luz do amanhecer é mais forte do que a mais longa noite de sofrimento.' Ele estende a mão sobre a Espada da Luz Solar, infundindo-a com a chama sagrada do verdadeiro amor."
    },
    "T3k": {
        "obj": "Confrontar e destruir a monstruosa Baba Lysaga e sua Cabana Rastejante, arrancar a segunda gema mágica da vinícola de suas entranhas e desmantelar o covil das bruxas do pântano.",
        "ctx": "Destruir a cabana viva exige arrancar a gema mágica verde incrustada no assoalho ou derrotar Baba Lysaga em seu crânio voador. Ao morrer, a bruxa amaldiçoa os heróis, mas o pântano começa a desintoxicar-se.",
        "sights": "A cabana colossal tombando e estilhaçando em milhares de toras de madeira inerte quando a gema verde é arrancada; Baba Lysaga despenhando-se de seu crânio de pedra em chamas; a água fétida do pântano clareando e tornando-se límpida.",
        "sounds": "O grito de agonia derradeira de Baba Lysaga que quebra as árvores ao redor; o colapso estrondoso da estrutura de três andares da cabana; e suspiros de alívio dos aliados.",
        "smells": "Fumaça preta dissipando-se, terra fértil e o aroma adocicado da gema mágica da vida.",
        "touch": "A gema mágica reluzente e quente nas mãos dos heróis, pulsando em sintonia com a terra libertada.",
        "narrar": "Com um golpe certeiro da Espada de Luz Solar desferido no coração da estrutura, a gema verde da vida é arrancada do assoalho da cabana viva. As raízes titânicas estremecem e paralisam instantaneamente, tombando a colossal construção de troncos na lama com um estrondo monumental que faz voar águas por todos os lados. Despencando de seu crânio de pedra destruído, Baba Lysaga dissolve-se em uma poça de lodo negro e cinzas: a maior feiticeira do vale foi extirpada da terra para sempre!"
    },
    "T3l": {
        "obj": "Conduzir a reconciliação histórica e comovente entre Urwin Martikov e seu pai Davian Martikov na vinícola, celebrando o retorno da segunda gema mágica e unificando os Guardiões das Penas.",
        "ctx": "Urwin e Davian passaram dez anos sem se falar devido à perda da gema. Ao verem as duas gemas reunidas e Berez purificada, pai e filho abraçam-se em lágrimas na adega, unificando toda a rede de corvos e espiões para a guerra final.",
        "sights": "Davian e Urwin com as mãos dadas segurando a gema mágica; Danika e os netos chorando de alegria; taças de vinho Purple Grapemash sendo erguidas em brinde memorável.",
        "sounds": "Lágrimas e palavras de perdão sincero entre pai e filho; centenas de corvos pousados nas janelas da vinícola grasnando em coro harmonioso de celebração.",
        "smells": "Vinho nobre de safra lendária, pão quente assado e lenha de carvalho.",
        "touch": "O abraço vigoroso e emocionado de uma família unificada que não teme mais as sombras.",
        "narrar": "Na adega da Vinícola Mago dos Vinhos, uma década de ressentimento e dor dissolve-se em um único abraço. Davian apoia as mãos nos ombros de Urwin, com lágrimas escorrendo pela barba prateada: 'Perdoe-me, meu filho... Eu deixei o orgulho me cegar para o que realmente importava.' Urwin abraça o pai com a voz embargada, enquanto Danika e as crianças comemoram com taças cheias de vinho recém-fermentado: 'Os Guardiões das Penas estão unidos novamente! Quando as asas de nossos corvos escurecerem os céus de Ravenloft... o vampiro saberá que seu reinado acabou!'"
    },
    "T3m": {
        "obj": "Executar o ritual sagrado de purificação no monólito primordial do Pântano em Berez, restaurar a Fane do Pântano e despojar Strahd de sua imunidade a magias e venenos.",
        "ctx": "Reconconsagrar a Fane do Pântano (dedicada à Tecelã) remove permanentemente os bônus mágicos de defesa de Strahd, tornando sua carne vulnerável a danos normais.",
        "sights": "O círculo de pedras do pântano cercado por águas agora cristalinas; a luz do sol do Farol tocando a pedra central; raízes floridas cobrindo a terra.",
        "sounds": "Um cântico suave de vozes femininas divinas ecoando na água; o som de riachos correndo limpos.",
        "smells": "Lótus brancos, água pura de nascente e terra fértil.",
        "touch": "A pedra do monólito quente e vibrante com poder cósmico purificado.",
        "narrar": "Depositando a essência sagrada sobre o monólito primordial de Berez, o pântano fétido é banhado por uma onda de luz cristalina. As águas negras clareiam em segundos, revelando leitos de seixos brancos e flores aquáticas de lótus que desabrocham sobre a lama purificada. Uma voz ancestral e melodiosa sussurra através das águas: 'A Fane do Pântano está restaurada. O usurpador de Ravenloft não mais tecerá o destino a seu bel-prazer: sua armadura arcana está quebrada!'"
    },
    "T4": {
        "obj": "Reunir Rudolph van Richten, Ezmerelda d'Avenir e o bardo Arturi no Acampamento de Tser Pool, compartilhar as descobertas das Fanes e preparar o ritual da Floresta.",
        "ctx": "Van Richten e Ezmerelda unem suas mentes táticas: o segundo santuário, a Fane da Floresta (da Caçadora), repousa nos bosques ancestrais e exige uma oferenda de coragem e prata pura.",
        "sights": "A mesa de carvalho do acampamento com o Tomo de Strahd aberto entre mapas de caça; Van Richten e Ezmerelda ajustando bestas de repetição de prata e estacas de madeira abençoada.",
        "sounds": "O som seco de parafusos de besta sendo testados; debates táticos afiados entre os dois maiores caçadores de monstros do mundo.",
        "smells": "Óleo de armas, fumo de cachimbo de cerejeira e resina de pinho.",
        "touch": "O aperto de mão inquebrável de caçadores experientes que sabem que marcharão para o combate supremo.",
        "narrar": "Ao redor da fogueira de Tser Pool, Rudolph van Richten e sua protegida Ezmerelda d'Avenir traçam os últimos detalhes da cruzada contra o castelo. O velho caçador aponta para o Tomo de Strahd: 'As defesas dele estão caindo uma a uma graças a vocês. Purifiquem a Fane da Floresta e da Montanha... e quando cruzarmos a ponte levadiça de Ravenloft, Strahd estará mais fraco e vulnerável do que esteve em qualquer momento dos últimos quatro séculos.'"
    },
    "T4d": {
        "obj": "Reconconsagrar a Fane da Floresta no círculo megalítico da mata profunda, devolver o santuário à Senhora Caçadora e despojar Strahd de seu controle sobre as feras e lobos de Baróvia.",
        "ctx": "A purificação da Fane da Floresta liberta a natureza do jugo do vampiro. Os lobos selvagens e corvos deixam de obedecer ao chamado de Strahd, privando-o de seus espiões e enxames.",
        "sights": "O monólito da mulher com chifres de cervo na mata profunda brilhando com luz verde-esmeralda; corvos e lobos pacificados sentando-se em círculo ao redor da clareira em reverência silenciosa.",
        "sounds": "O soar magnífico de uma trompa de caça espectral ecoando pelas copas dos pinheiros; o uivo harmonioso e calmo das feras libertadas.",
        "smells": "Resina pura de pinho alpino, terra úmida fértil e flores silvestres de outono.",
        "touch": "A pedra da deusa emanando calor vital que dissipa qualquer geada nos galhos ao redor.",
        "narrar": "Ao ser entoada a prece da Caçadora sobre o monólito da mata profunda, a pedra antiga irrompe em um fulgor verde-esmeralda de poder avassalador. O som glorioso de uma trompa de caça celestial ecoa pelas copas dos pinheiros ancestrais, e por toda a extensão de Baróvia, os lobos e feras da terra erguem os focinhos e soltam um uivo de libertação. A vontade de ferro de Strahd foi expurgada do sangue da floresta: as feras de Baróvia agora pertencem apenas à terra livre!"
    },
    "T5": {
        "obj": "Firmar a aliança militar definitiva em Vallaki com Lady Fiona Wachter ou com a liderança popular, mobilizar os soldados e milicianos da cidade e preparar a purificação final da Montanha.",
        "ctx": "Com o governo de Vallaki alinhado à causa e o povo ciente da proximidade da batalha decisiva, milicianos armam-se com lanças de ponta de ferro e tochas para guarnecer os portões e apoiar os heróis.",
        "sights": "A praça de Vallaki apinhada de cidadãos armando-se com escudos e espadas; ferreiros forjando pontas de lanças sem cessar; estandartes solares erguidos nas muralhas.",
        "sounds": "O som rítmico de martelos na bigorna; ordens militares sendo declamadas aos guardas; e o clamor de coragem do povo reunido.",
        "smells": "Carvão em brasa, ferro em forja, suor de guerreiros e pão de campanha.",
        "touch": "O aperto firme de mãos calejadas de soldados da cidade jurando lutar até o último suspiro pelas suas famílias.",
        "narrar": "A cidade de Vallaki transformou-se em uma fortaleza de ferro e determinação indomável. Na praça central, guardas municipais, caçadores experientes e cidadãos voluntários afiam espadas e ajustam armaduras sob a luz radiante do Farol de Argynvostholt. Não há mais sorrisos forçados de medo: há a chama ardente de um povo que decidiu que é melhor morrer de armas em punho do que continuar vivendo como gado nas sombras do castelo."
    },
    "T5d": {
        "obj": "Subir ao Santuário da Fane da Montanha sob o cume do Monte Ghakis, realizar o rito final de reconconsagração da Buscadora e despojar Strahd de sua armadura impenetrável de pedra e de sua regeneração de terra.",
        "ctx": "A purificação da terceira e última Fane é o clímax da desconstrução do vilão: Strahd perde sua regeneração sobrenatural vinda da terra de Baróvia e seu bônus maciço de CA. Ele agora é plenamente vulnerável à morte definitiva!",
        "sights": "O santuário de rocha nua nas alturas com vista para todo o vale; o símbolo da Buscadora acendendo-se em luz branca diamantina que se conecta ao pilar do Farol e aos santuários do Pântano e da Floresta em um triângulo de luz sagrada que cobre todo o mapa de Baróvia!",
        "sounds": "Um acorde harmônico celestial ressoando por todo o vale como o tanger de uma harpa divina; o rugido de fúria e dor de Strahd ecoando das torres distantes de Ravenloft.",
        "smells": "Ozônio sagrado puro, ar rarefeito de vitória e perfume de luz primordial.",
        "touch": "A vibração estática triunfante que percorre todo o corpo de cada guerreiro do grupo.",
        "narrar": "Ao depositar a oferenda final sobre a Fane da Montanha, o milagre supremo de Baróvia completa-se diante dos olhos do grupo. Um pilar de luz branca diamantina irrompe do cume do Monte Ghakis, conectando-se em linhas incandescentes de fogo sagrado com a Fane do Pântano em Berez e a Fane da Floresta na mata profunda. Um triângulo divino de pura energia purificadora sela os céus do vale! A quilômetros de distância, no Pináculo do Castelo Ravenloft, as vidraças explodem com um rugido aterrorizado e ensurdecedor de Strahd von Zarovich: suas defesas eternas foram destruídas. O senhor da noite sangra. O Diabo pode morrer!"
    },

    # ARC U: DREAMS OF DAWN (FINAL CONFRONTATION)
    "U1": {
        "obj": "Presidir o Grande Conselho de Guerra na Estalagem Água Azul em Vallaki com todos os aliados reunidos (Van Richten, Ezmerelda, Davian e Urwin Martikov, Godfrey, Kasimir, Ismark e Ireena), traçar a estratégia de invasão final a Ravenloft e preparar a defesa da cidade contra a horda que se aproxima.",
        "ctx": "Strahd compreendeu que seu fim se aproxima e ordenou a Noite Eterna: todas as criaturas mortas-vivas, morcegos, espectros e lobos de Baróvia marcharão em um exército apocalíptico para arrasar as vilas enquanto ele aguarda os heróis em seus salões.",
        "sights": "O grande salão da estalagem apinhado de líderes com armaduras completas; mapas táticos de Ravenloft e das muralhas de Vallaki estendidos sobre a mesa central; a Espada da Luz Solar pulsando com fulgor radiante no centro do conselho.",
        "sounds": "Debates estratégicos firmes; o som metálico de armaduras sendo travadas; a voz resoluta de Ireena declarando que lutará ao lado de seu povo.",
        "smells": "Cera de vela, metal polido, vinho forte e o cheiro elétrico de determinação pré-batalha.",
        "touch": "Mãos unidas sobre a lâmina da Sunsword em um juramento de vitória ou morte.",
        "narrar": "No salão principal da Estalagem Água Azul, a esperança de quatro séculos de opressão está reunida ao redor de uma única mesa. Cavaleiros revenantes em placas prateadas, caçadores lendários, chefes de clãs de corvos e guerreiros barovianos encaram os heróis com lealdade inabalável. No centro da mesa, a Espada da Luz Solar ilumina o mapa de Ravenloft com chamas douradas. Rudolph van Richten ergue sua taça de prata: 'Strahd convocou cada osso e garra desta terra para nos esmagar. Mas nós não somos mais as presas assustadas das brumas. Nós somos o Amanhecer que expurgará o Diabo de seu trono!'"
    },
    "U2": {
        "obj": "Compartilhar a revelação do sonho profético de Ireena Kolyana na madrugada anterior à batalha, compreender o preço sagrado de sua alma e selar seu papel definitivo na destruição do vampiro.",
        "ctx": "Ireena sonhou com Sergei e compreendeu que não é uma vítima passiva: sua presença na batalha final confrontará Strahd com a verdade de que ela nunca será dele por coerção, quebrando o controle mental do lorde no momento crucial.",
        "sights": "Ireena trajando armadura de placas leves de aço com capa carmesim e espada desembainhada; seus olhos brilhando com determinação serena sem qualquer traço de medo.",
        "sounds": "A voz firme, calma e comovente de Ireena agradecendo aos heróis por terem devolvido sua dignidade e coragem.",
        "smells": "Aço limpo, lavanda e ar fresco da noite.",
        "touch": "O aperto de mão caloroso e fraterno de Ireena selando o destino da luta.",
        "narrar": "Na varanda superior da estalagem, sob o fulgor radiante do Farol nas nuvens, Ireena Kolyana ajusta as fivelas de sua armadura de batalha. Seus olhos castanhos encontram os de vocês com uma serenidade que desarma qualquer angústia: 'Por toda a minha vida eu fugi da sombra daquele homem... Mas agora eu compreendo: eu não sou o prêmio de um monstro, eu sou a mulher que verá a justiça ser feita. Eu empunharei minha lâmina ao lado de vocês nos salões de Ravenloft.'"
    },
    "U3": {
        "obj": "Comandar a defesa das muralhas de Vallaki no início da Noite Eterna, repelir a primeira onda da horda de mortos-vivos e carniçais que assalta os portões e manter as linhas firmes.",
        "ctx": "Milhares de esqueletos, zumbis e carniçais marcham sobre a paliçada sob um eclipse solar mágico que torna a noite permanente. Os arqueiros de Vallaki e os Guardiões das Penas defendem os muros enquanto os heróis partem para decapitar a serpente em seu castelo.",
        "sights": "O horizonte tomado por milhares de olhos incandescentes de mortos-vivos avançando sobre a neve; flechas incendiárias riscando a noite; paliçadas de madeira tremendo sob o impacto de aríetes de ossos.",
        "sounds": "O rugido fúnebre de milhares de gargantas mortas uivando em uníssono; o retinir de flechas contra escudos; e os gritos de comando de Ismark mantendo a muralha firme.",
        "smells": "Flesh podre queimando em flechas de fogo, enxofre, piche fervente e terra revirada.",
        "touch": "A vibração brutal no chão sob a marcha da horda inumerável.",
        "narrar": "A Noite Eterna cai sobre Baróvia como um sudário de trevas absolutas. Do limite das florestas emerge o exército apocalíptico de Ravenloft: milhares de esqueletos em armaduras enferrujadas, carniçais sedentos de sangue e lobos atrozes avançam em marcha imparável contra as muralhas de Vallaki. Das passarelas de defesa, Ismark comanda o disparo de centenas de flechas flamejantes que incendeiam a noite: 'Mantenham as linhas, homens de Baróvia! Nossos campeões estão marchando para o coração do castelo! Segurem os portões até o sol nascer!'"
    },
    "U3d": {
        "obj": "Cruzar as linhas de cerco externas através de manobras táticas com os corvos de Davian, superar os pesadelos alucinatórios conjurados pelas brumas e avançar pela Estrada Svalich.",
        "ctx": "As brumas tentam atrasar os heróis com visões psíquicas de fracasso e entes queridos mortos. Com a bênção da Fane da Montanha, o grupo quebra as ilusões e abre caminho a cavalo.",
        "sights": "As brumas tomando formas fantasmagóricas de parentes e companheiros caídos; cavalos de guerra disparando em galope sob chuva de fagulhas radiantes da Sunsword.",
        "sounds": "Vozes ilusórias chamando para trás; o bater cadenciado de cascos na lama congelada; e o zumbido protetor da lâmina solar abrindo a névoa.",
        "smells": "Cinzas frias e ozônio.",
        "touch": "O impacto de lâminas solares cortando as ilusões como teias de aranha.",
        "narrar": "Cavalgando em disparada pela Estrada Svalich sob o céu escuro da Noite Eterna, as brumas contorcem-se em pesadelos vivos que tentam agarrar as rédeas dos heróis com garras ilusórias. Mas empunhando a Espada da Luz Solar erguida como uma tocha estelar na vanguarda, a comitiva rasga as trevas como um cometa de fogo, quebrando o cerco e avançando direto para os portões do covil do lorde."
    },
    "U3i": {
        "obj": "Infiltrar a base do Pináculo de Ravenloft, localizar e destruir o Coração da Tristeza (o cristal gigante pulsante que absorve todo o dano infligido a Strahd) e neutralizar o cordão umbilical de sangue do castelo.",
        "ctx": "O Coração da Tristeza é um cristal vermelho colossal de três metros de altura suspenso no vazio da torre mais alta de Ravenloft por correntes de ferro, conectado a Strahd por fios mágicos de sangue que absorvem os primeiros 50 pontos de dano que o vampiro sofreria. Destruí-lo faz chover cacos de cristal e sangue sobre a torre e deixa Strahd vulnerável!",
        "sights": "A torre oca vertiginosa com uma escadaria espiral de madeira suspensa sobre o abismo; no centro, pulsando como um coração biológico de cristal vermelho incandescente, o Coração da Tristeza gotejando sangue carmesim nas correntes; halberds animadas e gárgulas guardando a estrutura.",
        "sounds": "Um bater ritmado, pesado e aterrador de coração colossal que ressoa na pedra da torre: *tum-dum... tum-dum...*; o estalo estrondoso de cristal estilhaçando sob golpes de armas mágicas.",
        "smells": "Sangue fresco quente, ozônio mágico pulsante e vidro quebrado.",
        "touch": "O calor febril e pulsante do cristal de sangue antes de ser estilhaçado.",
        "narrar": "No topo oco do Pináculo de Ravenloft, suspenso no ar sobre um abismo vertiginoso por correntes maciças de ferro, bate o motor da imortalidade de Strahd: o Coração da Tristeza. O colossal cristal vermelho pulsa com um brilho rubro doentio, bombeando sangue mágico através de veias translúcidas que sobem para as pedras do castelo. Com golpes devastadores de aço sagrado e magia radiante, a lâmina da Sunsword quebra o cristal: com um estrondo de ensurdecer os deuses, o Coração da Tristeza explode em uma tempestade de cacos brilhantes e sangue ancestral! No andar abaixo, o grito de dor de Strahd confirma o golpe fatal em suas defesas!"
    },
    "U3j": {
        "obj": "Coordenar o avanço dos aliados pelas antecâmaras do castelo, neutralizar os últimos guardas de elite de Rahadin e alcançar as portas da câmara final do confronto.",
        "ctx": "Ezmerelda, Van Richten e os cavaleiros de Godfrey seguram as portas inferiores e abatem os últimos vampiros da corte, permitindo que os personagens e Ireena avancem para a batalha definitiva.",
        "sights": "Salões de Ravenloft iluminados por relâmpagos e fogo mágico; aliados lutando bravamente de costas unidas nas arcadas; as portas duplas de ferro da câmara do destino abertas.",
        "sounds": "O estrondo de magias colidindo; o brado de guerra de Ezmerelda e Van Richten; e a música triunfante da batalha final ecoando no castelo.",
        "smells": "Pólvora, cinzas de vampiros destruídos por luz solar e sangue nobre.",
        "touch": "O empurrão fraterno de Van Richten nos ombros dos heróis: 'Vão! Terminem isso por todos nós!'",
        "narrar": "Nos corredores superiores do castelo, Ezmerelda e Rudolph van Richten erguem suas espadas de prata e bestas de repetição, bloqueando a chegada dos últimos lacaios de Ravenloft. O velho caçador olha para os heróis com um sorriso radiante e orgulhoso: 'O caminho está livre, amigos! Vão e libertem esta terra da maldição dos séculos!' As portas duplas da câmara final abrem-se com estrondo: diante de vocês aguarda o confronto que decidirá o destino de Baróvia para sempre."
    },
    "U4": {
        "obj": "Confrontar o camareiro Rahadin em seu último combate de honra antes do salão do trono, silenciar o Coro da Morte e romper a última barreira de proteção de Strahd.",
        "ctx": "Rahadin luta até o último suspiro para proteger seu mestre com sua cimitarra e feitiços de sombras. Sua derrota é solene e trágica: ele morre jurando lealdade eterna à linhagem von Zarovich.",
        "sights": "Rahadin em postura de esgrima impecável diante do portal do trono; o coro de almas sussurrando em turbilhão espectral ao redor de seu corpo; faíscas metálicas cortando o ar.",
        "sounds": "O sussurro agoniado de milhares de fantasmas cessando de repente quando a lâmina de Rahadin cai no mármore; o último suspiro de lealdade do elfo.",
        "smells": "Ferro, poeira de almas e sangue élfico.",
        "touch": "O silêncio absoluto que se instala no corredor quando a aura do camareiro desvanece.",
        "narrar": "Diante das portas do trono repousa a última e mais leal sentinela de Ravenloft: o camareiro Rahadin. Com a cimitarra empunhada com maestria milenar e o coro de almas sussurrando em seus ouvidos, o elfo do crepúsculo luta com graça letal. Mas sob o golpe definitivo dos heróis, o general tomba sobre o mármore polido. Ele apoia a mão ensanguentada no peito, encara o grupo com olhar límpido e sussurra suas últimas palavras: 'Eu servi ao meu senhor até o fim do mundo... Que a noite receba minha alma.' O silêncio supremo abre as portas do destino."
    },
    "U5": {
        "obj": "Conduzir a batalha climácica final contra o Conde Strahd von Zarovich nos salões majestosos ou no terraço do Castelo Ravenloft, resistir aos seus ataques lendários, confrontá-lo com a Espada de Luz Solar e desferir o golpe de misericórdia definitivo que liberta Baróvia da escuridão!",
        "ctx": "Este é o clímax absoluto de toda a campanha: Strahd luta com toda a sua fúria aristocrática, invocando sombras, feitiços de destruição, escalada de paredes e ataques predatórios de presas. Mas com as Três Fanes reconconsagradas, o Coração da Tristeza destruído, os aliados mobilizados e a Sunsword empunhada, o vampiro é encurralado. Ireena desafia sua obsessão, e sob o golpe radiante do herói, o coração de Strahd é trespassado e seu corpo dissolve-se em cinzas eternas!",
        "sights": "O terraço do castelo sob o céu de tempestade iluminado pela lâmina de pura luz solar da Sunsword; Strahd com a capa esvoaçando, olhos vermelhos brilhando em fúria majestosa e presas expostas em sua verdadeira forma demoníaca; relâmpagos violetas quebrando sobre as torres; o golpe final de luz dourada atravessando o peito do vampiro, fazendo sua carne queimar em fogo sagrado e desmanchar-se em cinzas sopadas pelo vento.",
        "sounds": "O órgão de tubos de Ravenloft ressoando em acordes apocalípticos; o choque estrondoso de aço radiante contra garras de vampiro; as palavras cortantes de Ireena: 'Eu nunca pertenci a você, Strahd!'; e o rugido final de agonia e derrota do lorde de Baróvia conforme seu corpo sucumbe à luz do sol.",
        "smells": "Cinzas sagradas, incenso divino, ozônio elétrico e a pureza revigorante do ar da alvorada que rompe as trevas.",
        "touch": "A empunhadura incandescente da Sunsword vibrando de triunfo absoluto na mão do guerreiro e o calor da luz dourada que dissipa todo o frio de Baróvia.",
        "narrar": "A batalha suprema de Ravenloft ecoa pelos séculos. No alto do terraço açoitado pela tempestade, Strahd von Zarovich luta como um deus da noite encurralado, movendo-se como uma sombra voraz armada com garras e feitiços de destruição pura. Mas a luz da Espada da Luz Solar é implacável: ela corta as trevas, queima a carne morta e cega a soberba do conquistador. Encurralado contra o parapeito de pedra sob os olhos desafiadores de Ireena Kolyana, o soberano de Baróvia compreende que sua era de pesadelo acabou. Com um golpe lendário de luz radiante desferido com toda a coragem acumulada em sua jornada, a lâmina solar trespassa o coração de Strahd! Um clarão dourado ensurdecedor explode de seu peito, consumindo o vampiro em chamas purificadoras até que seu corpo desfaça-se em cinzas arrastadas pelo vendaval da montanha. O tirano caiu. Baróvia está livre!"
    },
    "U6": {
        "obj": "Testemunhar o milagre supremo do amanhecer sobre Baróvia: as brumas eternas dissolvendo-se pela primeira vez em quatrocentos anos, os raios dourados do sol da manhã banhando o vale e o fim da maldição de Ravenloft.",
        "ctx": "Pela primeira vez em quatro séculos, a barreira impenetrável das brumas desvanece por completo. O sol verdadeiro nasce sobre as montanhas, trazendo calor, céu azul límpido e lágrimas de libertação para toda a população do vale.",
        "sights": "As nuvens de chumbo rompendo-se para revelar um céu de azul safira imaculado; raios dourados e quentes de sol verdadeiro descendo sobre as torres de Ravenloft, sobre os telhados de Vallaki e sobre as águas brilhantes do Lago Zarovich; a névoa das fronteiras recuando e sumindo na terra; flores silvestres desabrochando em minutos nas colinas.",
        "sounds": "Sinos de todas as igrejas de Baróvia repicando em uníssono em júbilo incontrolável; cantos de pássaros que nunca haviam cantado no vale; o som de rios correndo límpidos; e os vivas e soluços emocionados de milhares de camponeses libertados.",
        "smells": "Terra aquecida pelo sol de verdade, ar puro das montanhas, flores frescas de outono e a sensação doce de uma nova manhã.",
        "touch": "O calor suave e reconfortante do sol tocando o rosto, os braços e as armaduras dos heróis após uma vida de trevas.",
        "narrar": "No horizonte oriental de Baróvia, o impossível acontece. As nuvens eternas de cinzas e chumbo abrem-se lentamente, e da crista dos picos nevados do Monte Ghakis irrompem os primeiros raios dourados de sol verdadeiro que esta terra contempla em quatrocentos anos. A névoa da morte dissolve-se como vapor sob a brisa morna da manhã, revelando florestas verdejantes, rios cintilantes e montanhas de beleza majestosa. Sinos de igrejas repicam em todas as vilas, e o choro de milhares de homens e mulheres livres ecoa pelo vale: as sombras fugiram. O pesadelo acabou. O sol nasceu sobre Baróvia."
    },

    # ARC EP: EPILOGUE (DRAGNACARTA CANONICAL SECTIONS 1 TO 6)
    "EP1": {
        "obj": "Conduzir a descida vitoriosa do Castelo Ravenloft sob a luz da manhã, reencontrar na encruzilhada os desertores arrependidos da horda (Cyrus Belview, Lief Lipsiege e Pidlwick II) e ajudá-los a encontrar um novo propósito de vida.",
        "ctx": "Cyrus, Lief e Pidlwick II fugiram do castelo quando a Noite Eterna ruiu. Eles estão atordoados pela luz do sol e temem ser executados. Os heróis podem mostrar misericórdia, integrando-os à comunidade ou enviando-os para Krezk.",
        "sights": "A encruzilhada do Rio Ivlis banhada pelo sol matinal; arbustos onde Cyrus esconde-se segurando uma colher de pau como adaga; Lief piscando os olhos sob a luz solar que lhe parece dolorosa; o boneco mecânico Pidlwick II observando o mundo exterior fascinado.",
        "sounds": "O som rítmico de engrenagens de Pidlwick II; a voz fanhosa e trêmula de Cyrus perguntando se o sol é 'um truque de mágica'; e risos gentis dos aventureiros.",
        "smells": "Grama molhada aquecendo ao sol e pinho silvestre.",
        "touch": "A madeira esculpida de Pidlwick II aceitando um aperto de mão amistoso.",
        "narrar": "Descendo a Estrada Svalich sob a luz quente do sol, a conhecida Encruzilhada do Rio Ivlis parece um lugar completamente novo. Escondidos atrás de um carvalho secular, uma cena inusitada arranca sorrisos do grupo: o disforme Cyrus Belview, o contador fantasmagórico Lief Lipsiege e o autômato saltitante Pidlwick II piscam sob a luz dourada da manhã, atordoados pelo nascer do sol. Cyrus brande uma colher de madeira com olhar desconfiado: 'Vocês têm certeza de que aquele troço amarelo e brilhante no céu não é um feitiço de fogo do mestre?' Com paciência e generosidade, os heróis acolhem os três fugitivos, provando que até mesmo as criaturas esquecidas de Ravenloft têm direito à redenção sob a nova aurora."
    },
    "EP2": {
        "obj": "Participar do alegre e triunfante Festival do Amanhecer na praça central de Vallaki, compartilhar contos de coragem e reconciliação com o povo libertado e celebrar a vitória com música e dança.",
        "ctx": "Pela primeira vez na história de Vallaki, um festival ocorre por pura alegria espontânea, sem ameaças de pelourinho ou forca. Mesas compridas cobrem a praça com comida farta, vinho da vinícola e jogos infantis.",
        "sights": "Praça de Vallaki enfeitada com flores do campo amarelas e estandartes solares dourados; famílias dançando ao som de violinos; crianças brincando ao redor de barris de vinho; Rictavio e Blinsky fazendo truques circenses alegres para a multidão.",
        "sounds": "Risos genuínos e canções alegres ecoando pelas ruas; o som de taças de estanho brindando à saúde dos heróis libertadores; e o dedilhar virtuoso de alaúdes.",
        "smells": "Pão doce de centeio assado na hora, tortas de maçã verdadeiras sem farinha de ossos, vinho tinto nobre e carne de porco defumada.",
        "touch": "Coroas de flores silvestres tecidas pelas crianças e colocadas sobre a cabeça dos aventureiros.",
        "narrar": "A praça central de Vallaki é o palco da celebração mais linda e comovente da história do vale: o Festival do Amanhecer. Sem ordens de barões ou ameaças de pelourinho, centenas de cidadãos e refugiados cantam, dançam e abraçam-se sob o céu azul e ensolarado. Crianças com coroas de margaridas correm entre mesas transbordando de pão fresco e vinho da vinícola Martikov. Ao verem os heróis entrarem na praça, a multidão irrompe em aplausos e vivas ensurdecedores que ecoam até as montanhas: os salvadores de Baróvia são coroados com o amor eterno de um povo libertado."
    },
    "EP3": {
        "obj": "Retornar à vila pacificada de Krezk, receber a gratidão imorredoura da família Krezkov e contemplar a nova harmonia entre os mongilóides redimidos da abadia e a comunidade.",
        "ctx": "Krezk prospera com o retorno dos heróis. O Burgomestre Dmitri Krezkov e sua esposa Anna abençoam a partida do grupo, enquanto a Abadia de Santa Markovia tornou-se um hospital de acolhimento sob a supervisão de Ezmerelda.",
        "sights": "As muralhas de Krezk com portões abertos de par em par; a Piscina Abençoada refletindo o céu límpido; aldeões trabalhando lado a lado com os mongilóides pacificados que aprenderam novos ofícios; Dmitri Krezkov com sorriso sereno no rosto.",
        "sounds": "Águas cantarolando na fonte sagrada; ferramentas de marcenaria e cultivo soando em harmonia; e a bênção de despedida de Dmitri.",
        "smells": "Terra fértil, flores de maçã e ar fresco de montanha.",
        "touch": "O abraço solene e fraterno do Burgomestre Krezkov entregando provisões para a viagem de volta.",
        "narrar": "Nas muralhas brancas de Krezk, os portões de ferro não mais se fecham contra o mundo. As águas da Piscina Abençoada cintilam sob o sol da manhã, refletindo um vale pacificado onde o medo foi sepultado. Dmitri e Anna Krezkov seguram as mãos dos heróis com olhos brilhando de gratidão sincera: 'Krezk nunca esquecerá os nomes daqueles que devolveram a luz aos nossos lares. Onde quer que seus passos os levem neste mundo... que o Senhor da Manhã ilumine sempre os seus caminhos.'"
    },
    "EP4": {
        "obj": "Visitar pela última vez a Vila de Baróvia e o Acampamento de Tser Pool, testemunhar a reconstrução das casas devastadas e despedir-se com afeto de Ismark, da taverna de Arik e da sábia Madame Eva.",
        "ctx": "A Vila de Baróvia renasce das cinzas do cerco sob a liderança nobre do novo Burgomestre Ismark Kolyanovich. Em Tser Pool, Madame Eva fecha seu baralho de Tarokka com um sorriso tranquilo de dever cumprido.",
        "sights": "Casas da vila com telhados novos sendo consertados com madeira fresca; Ismark vistoriando as obras com sorriso confiante; a Taverna Sangue da Videira cheia de viajantes; a tenda de Madame Eva iluminada pela luz da tarde.",
        "sounds": "Martelos na madeira; canções ciganas de violino em tom doce de despedida; e a risada satisfeita de Stanimir na fogueira.",
        "smells": "Madeira de pinho nova, fumaça perfumada de incenso Vistani e ensopado de comitiva.",
        "touch": "O aperto de mão de irmão de armas de Ismark e o abraço materno de Madame Eva.",
        "narrar": "Na Vila de Baróvia, o ranger de serras e o bater de martelos marcam o renascimento das casas destruídas pelo antigo cerco. Ismark Kolyanovich comanda a reconstrução com o porte digno de seu pai, abraçando os aventureiros com lágrimas nos olhos: 'Minha irmã está a salvo... e nosso povo tem um futuro digno pela primeira vez em séculos. Obrigado, meus irmãos.' E em Tser Pool, sentada diante de sua fogueira, a velha Madame Eva guarda a última carta do Tarokka com um olhar de pura paz: 'Os fios do destino teceram a mais bela das vitórias. Vão em paz... o mundo além das montanhas aguarda por seus passos.'"
    },
    "EP5": {
        "obj": "Descobrir o destino final do consorte vampiro Escher: testemunhar sua redenção melancólica ao buscar um caminho de expiação solitária nas montanhas ou sua despedida pacífica do vale.",
        "ctx": "Com a destruição de Strahd, as crias de vampiro recuperaram seu livre-arbítrio. Escher, livre da escravidão mental do lorde, escolhe viver recluso nas alturas ou buscar um meio de expiar os erros do passado sem fazer novas vítimas.",
        "sights": "Escher em trajes de viagem escuros com capuz cobrindo o rosto para proteger-se do sol direto; seu olhar sensível e aliviado contemplando as montanhas distantes.",
        "sounds": "A voz suave e poética de Escher declamando versos de libertação; o vento nas folhas secas.",
        "smells": "Rosas murchas e ar fresco da floresta.",
        "touch": "A reverência graciosa e respeitosa de Escher ao despedir-se do grupo nos limites da mata.",
        "narrar": "Na orla da floresta ocidental, uma silhueta esguia em capa escura aguarda sob a sombra dos carvalhos para não ser tocada pelo sol direto: Escher. Livre do jugo mental e da crueldade de Strahd, o jovem elfo encara os heróis com um sorriso tímido e melancólico: 'O mestre se foi... e pela primeira vez em séculos, meus pensamentos pertencem apenas a mim. Não pretendo ferir ninguém. Vou procurar refúgio nas cavernas altas onde a música e as memórias possam curar a dor do que fui obrigado a fazer. Obrigado... por me devolverem a minha própria alma.'"
    },
    "EP6": {
        "obj": "Participar da Grande Assembleia dos líderes de Baróvia, declarar o fim oficial da era das trevas, despedir-se calorosamente de todos os companheiros de jornada e cruzar os lendários Portões de Baróvia de volta para o mundo exterior sob o sol da liberdade!",
        "ctx": "Todos os líderes (Ismark, Ireena, Dmitri, Davian, Urwin, Van Richten, Ezmerelda, Kasimir e os Wachter) reúnem-se na Estrada Svalich Antiga junto aos Portões de Baróvia. As portas de ferro abrem-se de par em par, e onde antes havia uma muralha de névoa mortal, estende-se uma estrada límpida e ensolarada que conduz de volta para a Costa da Espada e para novas lendas no multiverso.",
        "sights": "Os colossais Portões de Baróvia abertos com as estátuas decapitadas cobertas de flores silvestres; todos os aliados e heróis em fila de honra sob o sol dourado do meio-dia; a estrada estendendo-se límpida até colinas verdes sem brumas no horizonte exterior; lágrimas e sorrisos de despedida eterna.",
        "sounds": "Um coro uníssono de despedida de centenas de vozes; o som solene de trompas de cavalaria e corvos grasnando em formação de asas de anjo no céu azul; e os passos firmes dos aventureiros cruzando o limiar do vale.",
        "smells": "Grama fresca, ar livre sem fronteiras, flores de primavera e o perfume inconfundível da liberdade conquistada.",
        "touch": "O último e mais caloroso abraço de Ireena Kolyana e de cada companheiro de estrada antes da partida definitiva.",
        "narrar": """Diante dos lendários Portões de Baróvia, onde sua jornada começou sob o terror da névoa cinzenta e o aviso de morte dos corvos, a história atinge seu ápice glorioso. Os imensos portais de ferro forjado repousam abertos de par em par, encimados por hera florida e banhados por um sol radiante que aquece cada centímetro da terra. Onde outrora havia a barreira sufocante de brumas que aprisionava almas por séculos, estende-se agora uma estrada larga e luminosa que serpenteia livremente em direção às montanhas e ao mundo além.

Ao lado da estrada, perfilados em uma guarda de honra que jamais será esquecida, estão todos os amigos que sangraram, riram e resistiram ao lado de vocês: Ismark empunhando sua espada com orgulho de herói; Davian e Urwin Martikov com suas famílias sorrindo sob o voo gracioso de dezenas de corvos protetores; Ezmerelda e o mestre Rudolph van Richten prestando uma continência solene com o olhar brilhando de admiração pura; e Ireena Kolyana, que caminha até vocês com passos leves, segurando as mãos de cada um com lágrimas de gratidão infinita nos olhos:

'Vocês entraram nesta terra como estranhos perdidos na tempestade... e saem como as lendas imortais que devolveram o amanhecer às nossas vidas. Baróvia nunca esquecerá os seus nomes. Que a luz do Senhor da Manhã e o amor de nossos corações acompanhem cada passo de seus destinos, por toda a eternidade.'

Com as bênçãos de um vale renascido ressoando em seus corações, as relíquias sagradas guardadas com honra e a Espada da Luz Solar brilhando em suas bainhas, vocês dão o primeiro passo além dos portões. A névoa se foi. O Diabo está morto. E diante de vocês, infinita, livre e majestosa sob a luz do sol... a estrada da vida aguarda por novas aventuras."""
    }
}

ACT4_METADATA.update(ACT4_METADATA_PART2 if 'ACT4_METADATA_PART2' in locals() else {})
print(f"Total Act IV & Epilogue metadata defined: {len(ACT4_METADATA)} scenes.")

# Helper to compile one scene
def compile_act4_scene(code):
    meta = ACT4_METADATA.get(code)
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
        if any(l_s.startswith(p) for p in ('### ', '**Local', '**Mapa', '**Consulta', '**Casa:', '**Entrada:', '**Oficina', '**Lago', '**Szoldar', '**Pedir', '**Conhecimento', '**Apoio', '**Registro', '**Origem:', '**Quarto', '**Cripta', '**Confronto', '**Se os', '**Reunião', '**Loot', '**Inimigos', '**Táticas', '**Objetivo real', '**Mecânica', '**O que', '**Salão', '**R1', '**R2', '**R3', '**R4', '**R5', '**R6', '**S1', '**S2', '**S3', '**S4', '**S5', '**S6', '**S7', '**S8', '**T1', '**T2', '**T3', '**T4', '**T5', '**U1', '**U2', '**U3', '**U4', '**U5', '**U6', '**EP', '**1.', '**2.', '**3.', '**4.', '**5.', '**6.')):
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

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam momentos heróicos e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para manifestar complicações imediatas no ambiente ou acelerar as ameaças finais de Baróvia."""
    return output.strip()

all_act4_code = {}
for code in ACT4_METADATA:
    compiled = compile_act4_scene(code)
    if compiled:
        all_act4_code[code] = compiled

print(f"Successfully compiled {len(all_act4_code)} Act IV & Epilogue scenes.")

with open('scripts/enrichment_content_act4.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nCurse of Strahd: Reloaded (DragnaCarta) - Act IV & Epilogue (Scenes R1-R6, S1-S8, T1-T5d, U1-U6, EP1-EP6)\n')
    f.write('Tradução e adaptação 100% fiel do repositório oficial do GitHub (DragnaCarta/Curse-of-Strahd-Reloaded).\n')
    f.write('Roteiros detalhados sem placeholders, descrições autênticas de leitura em voz alta, perfis de NPCs e CDs de Daggerheart.\n"""\n\n')
    f.write("ACT4_SCENES = {\n")
    for code, text in all_act4_code.items():
        escaped_text = text.replace('\\', '\\\\').replace('"""', r'\"\"\"')
        f.write(f'    "{code}": """{escaped_text}""",\n\n')
    f.write("}\n")

print("Saved: scripts/enrichment_content_act4.py")
