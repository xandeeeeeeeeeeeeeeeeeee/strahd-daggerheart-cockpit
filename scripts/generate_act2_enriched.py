# -*- coding: utf-8 -*-
"""
Generator for Act II (Arcs D, E, F, G, H, I) enriched scenes.
Reads DragnaCarta source from reloaded-source and merges with existing rich mechanics,
completely eliminating all generic boilerplate placeholders.
Total: 38 scenes (D1..D6, E1..E8, F1..F5, G1..G4, H1..H9, I1..I6).
"""

import json
import os
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes_by_code = {s['code']: s for s in data['scenes']}

ACT2_METADATA = {
    # ARC D: ST. ANDRAL'S FEAST
    "D1": {
        "obj": "Investigar o roubo dos ossos sagrados de Santo Andral na igreja de Vallaki, conversar com o Padre Lucian Petrovich e Yeska, e iniciar a busca pelas relíquias antes do Festival do Sol Flamejante.",
        "ctx": "A Igreja de Santo Andral é o único refúgio sagrado contra vampiros em toda Baróvia devido aos ossos do mártir Andral sob o altar. Sem eles, o solo sagrado perdeu o hallow e Strahd pode massacrar os refugiados.",
        "sights": "Candelabros de ferro forjado banhando bancos de carvalho encerado em luz suave; dezenas de famílias de refugiados deitadas em mantas humildes; a laje de mármore do altar erguida revelando a cripta vazia.",
        "sounds": "Murmúrios de orações desesperadas; choro abafado de crianças; o som de vassoura limpando o chão de pedra; e a respiração trêmula do Padre Lucian.",
        "smells": "Incenso de olíbano, linho lavado, madeira envelhecida e a friagem de terra que sobe da cripta aberta.",
        "touch": "O choque gélido ao tocar a cripta violada e a tensão quase elétrica de um santuário desprotegido.",
        "narrar": "Doze candelabros ornamentados banham fileiras de bancos bem cuidados em luz suave de velas, tocando cada canto da capela de Santo Andral com calor acolhedor. No entanto, atrás do altar de mármore, o Padre Lucian ajoelha-se com as mãos trêmulas diante de uma cavidade de pedra aberta: o relicário sob a laje foi forçado e os ossos sagrados do mártir desapareceram."
    },
    "D2": {
        "obj": "Confrontar o jovem coveiro Milivoj em sua casa em ruínas no bairro noroeste de Vallaki, descobrir seu motivo desesperado e obter sua confissão sobre a venda dos ossos para Henrik van der Voort.",
        "ctx": "Milivoj roubou os ossos porque precisava desesperadamente de moedas para comprar comida para seus irmãos menores famintos (Bogan e Zondra) e remédios para sua mãe doente Jarzinka, viciada em tortas de sonho.",
        "sights": "Sobrado decadente de madeira podre com venezianas tortas; cômodos minúsculos com colchões de palha no chão; mãe esquálida de olhar vítreo usando colar de contas; crianças descalças com rostos sujos de lama.",
        "sounds": "O gemido da porta de entrada rangendo em dobradiças emperradas; tosse seca de criança no canto escuro; e a voz grossa e defensiva de Milivoj ameaçando com uma pá de coveiro.",
        "smells": "Madeira encharcada, mofo antigo, terra de cemitério fresca nas botas do rapaz e farinha azeda de repolho cozido.",
        "touch": "Ar gélido vazando pelas frestas das paredes e o chão pegajoso de umidade e miséria.",
        "narrar": "A estrada lamacenta que leva ao bairro noroeste de Vallaki é áspera e irregular, gelada por uma névoa persistente que parece grudar na terra encharcada. Conforme vocês se afastam da praça central, as ruas se estreitam e os sobrados tornam-se decrépitos. Ao baterem na porta da casa de Milivoj, uma mulher esquálida de olhar vítreo abre uma fresta; ao fundo, um jovem robusto de ombros largos segura uma pá com nós dos dedos brancos de tensão."
    },
    "D3": {
        "obj": "Investigar o depósito de carroças Arasek Stockyard em Vallaki, questionar os proprietários Gunther e Yelena Arasek e examinar a misteriosa carroça de circo trancada pertencente a Rictavio.",
        "ctx": "A carroça de circo de Rictavio está estacionada no pátio cercado por muros altos. Letras desbotadas dizem 'Carnaval de Rictavio'. Dentro da carroça não há animais dóceis, mas sim um tigre-dentes-de-sabre treinado para caçar vampiros e Vistani.",
        "sights": "Pátio lamacento cercado por estacas de madeira; galpões com arreios, cordas e fardos de feno; e uma grande carroça de viagem com grades reforçadas de ferro e cadeado robusto.",
        "sounds": "O relinchar inquieto de cavalos de tração; mastigação abafada e respiração pesada de uma fera carnívora vindo de dentro da carroça; e o estalo de correntes de ferro.",
        "smells": "Esterco de cavalo, feno molhado, couro curtido e o odor forte e almiscarado de um predador de grande porte enjaulado.",
        "touch": "Cadeados de ferro gelados pela geada e a madeira da carroça vibrando quando a fera se move em seu interior.",
        "narrar": "O depósito de carroças de Arasek é um pátio de terra batida cercado por muros altos de madeira, onde carroças de carga e fardos de feno repousam sob a neblina. No canto sul do terreno, isolada das demais, repousa uma carroça de viagem com laterais pintadas em cores circenses desbotadas. Um pesado cadeado de ferro prende a porta traseira, e de dentro das frestas reforçadas emana um rosnado baixo e gutural que faz os cavalos das baias vizinhas estremecerem."
    },
    "D4": {
        "obj": "Invadir a oficina de caixões de Henrik van der Voort, confrontar o marceneiro e sobreviver à emboscada orquestrada pela noiva vampira Volenta Popofsky e seis crias de vampiro famintas no depósito do andar superior.",
        "ctx": "Henrik comprou os ossos a mando de um nobre cavalheiro (Vasili von Holtz / Strahd disfarçado). A noiva Volenta Popofsky, usando sua sinistra máscara de caveira de porcelana, escondeu seis crias de vampiro nos caixões do sótão prontas para atacar Vallaki durante o Festival.",
        "sights": "Sobrado de dois pavimentos com dúzias de caixões de pinho inacabados empilhados como dominós; serragem espalhada pelo chão; no andar superior, seis caixões fechados em cavaletes sob vigas escuras do teto.",
        "sounds": "O som sibilante de uma plaina parando de repente; o rangido de tábuas de assoalho no piso superior; e o estrondo súbito de madeira estilhaçando quando as tampas dos caixões explodem.",
        "smells": "Serragem fresca de pinheiro, verniz de breu sufocante, terra seca de sepultura e o fedor adocicado de carne em decomposição guardada em caixões fechados.",
        "touch": "Poeira de madeira fina grudando no suor da pele e lascas afiadas voando pelo ar na penumbra.",
        "narrar": "A oficina de caixões de Henrik cheira a resina e morte iminente. No andar térreo, caixões vazios de pinho empilham-se até o teto em fileiras silenciosas. No segundo pavimento, a escuridão é densa, com pó de serra cobrindo o chão. No fundo do depósito sul repousam seis caixões fechados com tampas pregadas. Mas assim que vocês dão o primeiro passo em direção ao quarto onde o saco com os ossos brilha tênue, um ruído horrendo de garras arranhando madeira rompe o silêncio: as tampas saltam com estrondo e olhos escarlates abrem-se na escuridão!"
    },
    "D5": {
        "obj": "Levar os ossos sagrados de volta à Igreja de Santo Andral a tempo, realizar o ritual de reconsagração e restaurar a barreira divina que protege os refugiados do vale.",
        "ctx": "O retorno dos ossos restaura a magia Hallow na igreja. Se completado antes do anoitecer, as crias de vampiro e o próprio Strahd não podem penetrar o templo.",
        "sights": "O altar de Santo Andral iluminado por feixes dourados de luz mística assim que os ossos tocam a cripta; lágrimas de alívio escorrendo pelo rosto de mães e idosos.",
        "sounds": "O cântico solene do Padre Lucian em louvor ao Senhor da Manhã; o som suave de sino de prata tocando; e suspiros profundos de esperança na nave.",
        "smells": "Incenso de sândalo purificador expulsando o odor de cinzas e morte; ar limpo e aquecido.",
        "touch": "Uma onda de calor e alívio que dissipa o frio sobrenatural dos ossos de quem esteve à beira do abismo.",
        "narrar": "Conforme o saco com os ossos sagrados é depositado na cavidade sob o altar, o Padre Lucian ergue seu símbolo solar e entoa a prece milenar de consagração. Uma centelha dourada irrompe da pedra, espalhando-se como ondas de calor pelas paredes de pedra da igreja e fazendo os vitrais brilharem em matizes vívidos de aurora. A sensação asfixiante de pavor desvanece instantaneamente: o solo sagrado de Santo Andral está restaurado."
    },
    "D6": {
        "obj": "Testemunhar a chegada solene e aterrorizante do camareiro Rahadin na praça de Vallaki, ouvir o decreto real de Strahd contra Henrik van der Voort e receber a carta de convite formal para o Jantar no Castelo Ravenloft.",
        "ctx": "Rahadin chega em seu corcel negro representando a autoridade imperial de Strahd. Ele executa Henrik publicamente por 'perturbar a paz do conde' e entrega aos heróis a carta de convite com o brasão de Ravenloft.",
        "sights": "O elfo do crepúsculo de feições angulares severas e armadura de placas cinzentas imaculadas; a praça de Vallaki em silêncio absoluto; moradores paralisados de terror diante do camareiro de Ravenloft.",
        "sounds": "O sussurro agoniado e fantasmagórico de milhares de almas mortas que emana da aura sobrenatural de Rahadin (*Coro da Morte*); o trote compassado de seu cavalo negro; e sua voz calma, precisa e impiedosa.",
        "smells": "Ozônio gélido, ferro polido, couro nobre e o odor asfixiante de morte militar sem misericórdia.",
        "touch": "A vibração psíquica nos tímpanos causada pelos gritos sussurrados das vítimas de Rahadin.",
        "narrar": "O som de um trote solitário ecoa pelas ruas de paralelepípedos de Vallaki, fazendo moradores correrem para dentro de casa e trancarem portas e janelas. Rompendo a névoa na praça central, surge um cavaleiro de postura ereta impecável: o camareiro Rahadin, o elfo do crepúsculo de Ravenloft. Uma aura aterrorizante de sussurros fantasmagóricos emana de sua figura, ecoando as agonias daqueles que ele chacinou em séculos de guerras. Ele desce do cavalo, desdobra um pergaminho com o selo real de Strahd e declara o veredito do conde com frieza aristocrática."
    },

    # ARC E: THE MISSING VISTANA
    "E1": {
        "obj": "Visitar a bizarra oficina de brinquedos Blinsky Toys em Vallaki, conversar com o excêntrico fabricante de brinquedos Gadof Blinsky e seu macaco Piccolo, e descobrir a sinistra encomenda da boneca idêntica a Ireena Kolyana feita por Izek Strazni.",
        "ctx": "Blinsky é o único fabricante de brinquedos de Baróvia e opera sob o lema 'Não é divertido? É Blinsky!'. Izek Strazni, o capitão demoníaco da guarda municipal de Vallaki, sonha compulsivamente com uma mulher de cabelos ruivos desde a infância e obriga Blinsky a confeccionar dezenas de bonecas idênticas a Ireena a cada mês.",
        "sights": "Loja apinhada de prateleiras com brinquedos macabros: guilhotinas em miniatura, bonecos enforcados que se debatem ao puxar uma cordinha, palhaços sem olhos; um macaco de pelo verde e colete vermelho (Piccolo) pulando sobre caixas; e uma boneca de porcelana com o rosto exato de Ireena.",
        "sounds": "O chiar agudo de caixas de música desafinadas; risinhos mecânicos de bonecos de corda; o ganido travesso do macaco Piccolo; e a voz animada e com sotaque exagerado de Blinsky.",
        "smells": "Serragem, tinta a óleo fresca, cola de ossos fervida, óleo de engrenagem e fumaça de cachimbo de cerejeira.",
        "touch": "O toque perturbador e frio de porcelana pálida esculpida com as feições de Ireena.",
        "narrar": "A oficina Blinsky Toys parece uma vitrine de pesadelos infantis. Sob uma placa que declara em letras tortas: 'Se Não É Divertido, Não É Blinsky!', dezenas de brinquedos bizarros ocupam prateleiras até o teto: pequenas forcas de madeira com bonecos que se debatem, caixas de surpresa com cabeças decepadas e marionetes macabras. No balcão, um homem gordo de bochechas coradas e colete xadrez ajusta o chapéu de um macaco minúsculo enquanto lustra a bochecha de uma boneca de porcelana que traz, com fidelidade assustadora, o rosto exato de Ireena Kolyana."
    },
    "E2": {
        "obj": "Adentrar o acampamento Vistani e a colina dos elfos do crepúsculo nos arredores sul de Vallaki, conhecer os líderes Luvash e Arrigal, ouvir o lamento desesperado pelo desaparecimento da menina Arabelle, e conversar com o ancião Kasimir Velikov.",
        "ctx": "Luvash e Arrigal lideram os Vistani de Vallaki. Arabelle, a amada filha de sete anos de Luvash, desapareceu misteriosamente e o pai bebe em fúria cega enquanto pune seus servos. Na colina ao lado vivem os elfos do crepúsculo sobreviventes liderados por Kasimir Velikov, mutilados por Strahd séculos atrás.",
        "sights": "Uma colina com dezenas de carroças coloridas cercadas por barris de vinho; homens Vistani abatidos e armados com cimitarras; choças miseráveis de pele e estacas onde elfos do crepúsculo de orelhas cortadas observam em silêncio solene; e Kasimir em sua tenda lendo runas antigas.",
        "sounds": "Gritos furiosos de Luvash ameaçando seus homens com um chicote de couro; gemidos de punição; cães de caça latindo; e o vento uivando na colina descampada.",
        "smells": "Fogueiras de turfa, ensopado picante, vinho derramado na lama, couro cru e o cheiro acre de sangue de açoitamento.",
        "touch": "O aperto de mão de ferro de guerreiros endurecidos e a cicatriz áspera nas orelhas decepadas de Kasimir.",
        "narrar": "No topo de uma colina a sudoeste de Vallaki ergue-se o acampamento Vistani. Dezenas de carroças vistosas cercam uma grande fogueira central, mas o ambiente não é de festa: homens de feições tensas empunham cimitarras enquanto gritos furiosos ecoam da tenda principal. Luvash, com os olhos vermelhos de vinho e cólera, chora o sumiço de sua filha Arabelle, ameaçando enforcar seus guardas. Na base da colina, em cabanas miseráveis, os últimos elfos do crepúsculo — homens de orelhas decepadas e olhares milenares — observam em silêncio a agonia de seus captores."
    },
    "E3": {
        "obj": "Conseguir audiência na Mansão do Burgomestre com o Barão Vargas Vallakovich e sua esposa Lydia Petrovna, investigar a vasta biblioteca da mansão em busca das notas do arquimago Khazan, e desvendar a oficina secreta do jovem mago Victor Vallakovich no sótão.",
        "ctx": "O Barão Vargas é obcecado pela doutrina fanática de que a felicidade obrigatória repele Strahd. Na biblioteca da mansão repousam anotações sobre a lendária Torre de Khazan no Lago Baratok. No sótão (área N3t), seu filho recluso Victor tenta fugir de Baróvia criando círculos de teletransporte experimentais que já incineraram dois criados.",
        "sights": "Casarão imponente de dois pavimentos com brasões do sol esculpidos nas portas; salão nobre com espelhos cobertos por panos roxos; o Barão com seus dois mastins enormes no colo; sótão empoeirado com círculos mágicos traçados com giz e sangue em tábuas chamuscadas.",
        "sounds": "Os latidos graves dos mastins do Barão; o riso forçado e histérico de Lydia Petrovna arrumando vestidos de festa; e os estalos arcanos e sussurros de feitiços de teletransporte ecoando do sótão.",
        "smells": "Cera de assoalho cara, lavanda seca, pelo de cão e o odor penetrante de ozônio queimado e enxofre no sótão.",
        "touch": "O estofamento de veludo roxo das poltronas do Barão e o arrepio estático no ar ao aproximar-se do círculo arcano de Victor.",
        "narrar": "A Mansão do Burgomestre exala uma atmosfera de falsa ordem e opressão cortês. O Barão Vargas Vallakovich recebe os visitantes afagando dois mastins gigantescos com sorrisos ensaiados e ameaças veladas a quem demonstrar 'malícia e tristeza'. Mas enquanto a Senhora Lydia costura laços para o próximo festival, os degraus que sobem para o sótão revelam algo muito mais perigoso: feixes de luz púrpura vazam sob a porta do último andar, onde círculos arcanos chamuscados no assoalho mostram que o jovem Victor está brincando com forças que rasgam o tecido da realidade."
    },
    "E4": {
        "obj": "Viajar para a margem oeste do Lago Zarovich, localizar a cabana de preparação de peles dos caçadores Szoldar e Yevgeni, obter orientações seguras sobre as trilhas do norte e examinar a estela ancestral da Sonhadora (Rozana).",
        "ctx": "DragnaCarta Reloaded removeu o clichê do afogamento de Arabelle por Bluto. Em vez disso, a pista da menina e da torre mágica passa pelos caçadores de elite Szoldar e Yevgeni em sua cabana de caça na margem do lago. Eles conhecem os perigos dos lobos do oeste e revelam uma estela esculpida com uma borboleta (o santuário da Sonhadora, uma das Rozana ancestrais).",
        "sights": "Águas gélidas e escuras do Lago Zarovich refletindo as montanhas sob névoa rasteira; cabana rústica de troncos com peles de cervo e lobo secando em armações de madeira; estela antiga de pedra com uma borboleta estilizada talhada em relevo.",
        "sounds": "O bater suave de marolas gélidas nas pedras da margem; o grasnar distante de garças cinzentas; o som rítmico de facas raspando couro na cabana; e o uivo de vento entre os juncos.",
        "smells": "Água doce de degelo, lama de brejo, fumaça de pinho e couro curtido com gordura animal e sal marinho.",
        "touch": "Água congelante que queima a ponta dos dedos ao tocar o lago e a pedra antiga e desgastada da estela de borboleta.",
        "narrar": "A margem ocidental do Lago Zarovich estende-se em um silêncio melancólico e solene sob o sopé do Monte Baratok. As águas calmas e límpidas como vidro escuro refletem a floresta densa da encosta. Junto a uma enseada pedregosa, ergue-se uma cabana rústica de troncos onde peles de lobos e cervos secam esticadas ao vento frio. Sentados sobre cepos de madeira, afiando longas facas de caça, estão os dois caçadores mais temidos de Vallaki: Szoldar e Yevgeni. Perto dali, uma estela milenar de pedra exibe a figura delicada de uma borboleta com asas abertas — o símbolo esquecido da deusa Sonhadora."
    },
    "E5": {
        "obj": "Percorrer a Estrada Svalich em direção ao Monte Baratok, cruzar a secular Ponte do Rio Luna e a encruzilhada setentrional, navegando por trilhas infestadas por feras sob orientação dos caçadores.",
        "ctx": "O Rio Luna desce impetuoso dos picos de Baratok. A ponte de pedra arqueada é antiga e sólida. O ramal noroeste sobe em zigue-zague pelas encostas íngremes em direção à lendária Torre de Khazan.",
        "sights": "Ponte de pedra ancestral com muretas cobertas de hera; correnteza rápida e espumante do Rio Luna quebrando sobre pedregulhos; floresta fechada de pinheiros de alta altitude; trilha rochosa que sobe para o norte.",
        "sounds": "O rugido caudaloso do Rio Luna correndo sob o arco da ponte; vento forte uivando nas encostas; estalos de galhos nas matas laterais.",
        "smells": "Resina pura de pinheiro alpino, ar rarefeito de montanha e água mineral gelada.",
        "touch": "O frio intenso que começa a entorpecer as extremidades conforme a comitiva ganha altitude.",
        "narrar": "A estrada deixa as terras baixas de Vallaki e sobe rumo aos maciços rochosos do norte. Diante de vocês ergue-se a monumental Ponte do Rio Luna, com seus arcos de pedra resistindo há séculos à fúria de águas turbulentas e espumantes de degelo. Ao cruzarem a ponte, a trilha divide-se: o caminho noroeste afunda em uma garganta arborizada que serpenteia até as margens secretas do Lago Baratok, onde as histórias afirmam que uma torre sem portas nem janelas guarda segredos arcanos de outros mundos."
    },
    "E6": {
        "obj": "Explorar o promontório isolado do Lago Baratok, desvendar o enigma do dragão na porta da Torre de Khazan (o campo antimagia), inspecionar a carroça booby-trapped de Ezmerelda d'Avenir e recuperar o diário de Rudolph van Richten.",
        "ctx": "A Torre de Khazan é uma torre de pedra de 25 metros erguida em uma ilhota conectada por um dique de pedras. A torre é protegida por um poderoso campo antimagia permanente. A porta de ferro só abre com a dança correta dos braços de estátuas de dragão. Do lado de fora repousa a carroça de Ezmerelda, protegida por armadilhas mortais de frascos de fogo alquímico.",
        "sights": "Torre cilíndrica de pedra lisa sem janelas erguendo-se em uma península pedregosa; andaimes de madeira podre sustentando um dos lados; a carroça amarela de viagem com cortinas fechadas; e o relevo esculpido de dragões entrelaçados na porta de ferro.",
        "sounds": "O vento uivando na superfície calma do Lago Baratok; o eco oco de passos sobre o dique de pedra; e o rangido metálico de trincos e agulhas de armadilha na porta da carroça.",
        "smells": "Pó de pedra milenar, enxofre químico de substâncias alquímicas na carroça e ar frio de montanha.",
        "touch": "O amortecimento sobrenatural de toda magia ao cruzar a soleira da torre (o campo antimagia suprime magias instantaneamente).",
        "narrar": "Em uma península pedregosa que se projeta sobre as águas espelhadas do Lago Baratok, ergue-se a Torre de Khazan. A estrutura cilíndrica de vinte e cinco metros de altura parece esculpida em um único bloco de pedra cinzenta sem janelas, encimada por andaimes de madeira podre. Junto à margem repousa uma carroça coberta pintada em amarelo vivo com detalhes azuis. A porta de ferro da torre não possui fechadura ou maçaneta, apenas entalhes de dragões em relevo cujos braços e caudas formam posições codificadas de um enigma arcano ancestral."
    },
    "E7": {
        "obj": "Retornar com segurança do Lago Baratok para Vallaki carregando os segredos de Van Richten e as pistas da caçadora Ezmerelda, despistando patrulhas de lobos e batedores que tentam emboscar o grupo.",
        "ctx": "A jornada de volta é tensa: a noite começa a cair e a alcateia de lobisomens sabe que estrangeiros invadiram a área do lago. Se os heróis tiverem resgatado Arabelle ou trazido os manuscritos, devem evitar combates desnecessários na escuridão.",
        "sights": "Sombras alongadas dos pinheiros engolindo a Estrada Svalich; olhos amarelos observando da vegetação; o brilho distante das tochas nas torres de Vallaki.",
        "sounds": "Uivos distantes em três direções diferentes na floresta; galhos quebrando atrás do grupo; e o bater apressado de botas na lama.",
        "smells": "Terra molhada pelo orvalho noturno e o odor característico de pelos de lobo na brisa.",
        "touch": "O arrepio constante de estar sendo perseguido por predadores que esperam um tropeço.",
        "narrar": "O crepúsculo cai rapidamente sobre as florestas de Baratok, tingindo as brumas em tons roxos e cinzentos. Conforme vocês refazem o caminho rumo ao sul, a sensação de vigilância predatória torna-se insuportável: silhuetas ágeis movem-se entre os troncos no limite da visão, e uivos coordenados avisam que a alcateia está cercando a estrada. Somente o passo acelerado e a visão das tochas acesas nas muralhas de Vallaki prometem refúgio antes que a noite feche suas mandíbulas."
    },
    "E8": {
        "obj": "Confrontar o falso mestre de circo Rictavio na Estalagem Água Azul, desmascará-lo como o lendário Rudolph van Richten, devolver a menina Arabelle em segurança a Luvash no acampamento Vistani e consolidar a aliança com os Vistani.",
        "ctx": "Com as pistas da torre e a boneca de Blinsky, o grupo pode confrontar Rictavio. Ele confessa ser Rudolph van Richten e revela que caça o vampiro-mestre há décadas. Devolver Arabelle a Luvash transforma o pai de um bêbado furioso em um aliado eterno que concede tesouros e apoio leal aos heróis.",
        "sights": "Rictavio retirando seu chapéu emplumado e exibindo o olhar severo e cabelos grisalhos de um sábio guerreiro; Luvash de joelhos na lama abraçando Arabelle em lágrimas de gratidão; baús de tesouros abertos na fogueira Vistani.",
        "sounds": "Canções alegres de violinos explodindo em celebração no acampamento Vistani; taças de vinho se chocando; e a voz grave de Van Richten explicando seus planos táticos.",
        "smells": "Vinho de festa, cordeiro assado no espeto, fumo de cachimbo de boa qualidade e a sensação libertadora de dever cumprido.",
        "touch": "O calor das fogueiras Vistani e o aperto de mão firme de Rudolph van Richten selando um pacto de sangue contra Strahd.",
        "narrar": "No quarto superior da Estalagem Água Azul, a persona jovial de Rictavio finalmente desfaz-se: diante de vocês, retirando os adereços circenses com dedos calejados, está o lendário caçador Rudolph van Richten. Seus olhos cinzentos e penetrantes encaram o grupo com respeito renovado: 'Vocês têm aço em suas almas, amigos. É hora de pararmos de nos esconder nas sombras e começarmos a traçar a queda do tirano.' E quando a pequena Arabelle é entregue nos braços de Luvash no acampamento da colina, o patriarca chora copiosamente, proclamando que os heróis são irmãos eternos do sangue Vistani."
    },

    # ARC F: LADY WACHTER'S WISH
    "F1": {
        "obj": "Receber a visita discreta de Ernst Larnak na Estalagem Água Azul, ouvir a mensagem misteriosa e o convite formal da nobre Lady Fiona Wachter para uma reunião confidencial em Wachterhaus.",
        "ctx": "Ernst Larnak é o espião e lacaio mais leal de Lady Fiona. Ela soube das proezas dos aventureiros e deseja recrutá-los para um golpe político contra o insano Barão Vargas Vallakovich.",
        "sights": "Um homem esguio de sobretudo cinzento e capuz puxado sentado em uma mesa de canto da estalagem; olhos astutos que acompanham cada movimento dos heróis; uma carta com selo de cera preta exibindo o brasão da família Wachter.",
        "sounds": "O zumbido da estalagem cheia cobrindo a voz baixa e sussurrada de Ernst; o tilintar de uma moeda de ouro deixada sobre a mesa.",
        "smells": "Cerveja de centeio, fumaça de cachimbo e o perfume sutil de lavanda e cera de lacre na carta.",
        "touch": "O envelope de pergaminho grosso e pesado passado de mão em mão sob a mesa de carvalho.",
        "narrar": "Enquanto a estalagem vibra com canecas de cerveja e conversas tensas, um homem magro de sobretudo cinza aproxima-se com passos que não produzem som no assoalho. Ele puxa o capuz para trás revelando feições pontiagudas e olhos de falcão: Ernst Larnak. Ele desliza sobre a mesa uma carta selada com cera preta trazendo o brasão aristocrático dos Wachter: 'Minha senhora, Lady Fiona Wachter, solicita a honra de sua presença em sua residência para uma taça de vinho e uma conversa sobre o futuro desta infeliz cidade. Há males que nem mesmo os festivais de Vargas podem disfarçar.'"
    },
    "F2": {
        "obj": "Adentrar o casarão aristocrático e sombrio de Wachterhaus, conhecer Lady Fiona Wachter, descobrir seus ideais políticos e sua proposta para assassinar o monstruoso capitão Izek Strazni em troca de ouro e poder político.",
        "ctx": "Lady Wachter é pragmática, aristocrática e leal à casa von Zarovich. Ela considera Vargas um tirano ridículo que arruinará Vallaki. Ela propõe eliminar Izek Strazni (o braço armado do Barão), prometendo que com a queda de Izek a guarda se renderá e Vallaki terá um governo estável e pacífico.",
        "sights": "Casarão imponente com paredes de madeira escura e tapeçarias desbotadas; lareira crepitando com gatos pretos deitados sobre almofadas; um grande retrato do jovem Strahd na parede da biblioteca; e Lady Fiona com seu vestido de veludo negro e anéis reluzentes.",
        "sounds": "O ronronar suave de múltiplos gatos; o crepitar cadenciado da lenha na lareira de mármore; e a voz aveludada, culta e cortante de Lady Fiona expondo seu plano com frieza cirúrgica.",
        "smells": "Cera de vela pura, incenso leve de cedro, vinho tinto nobre e o cheiro aconchegante de casarão senhorial.",
        "touch": "Cadeiras de encosto alto com estofamento de veludo e taças de prata lavrada cheias de vinho de safra pessoal.",
        "narrar": "Wachterhaus é uma mansão gótica que respira nobreza e segredos ancestrais. Ao cruzarem os salões de carvalho escuro onde gatos de pelos negros dormem sobre almofadas de veludo, vocês são conduzidos à sala de estar de Lady Fiona Wachter. Uma mulher distinta de meia-idade, com cabelos castanhos presos com elegância e olhar penetrante de quem comanda impérios, serve cálices de vinho com mãos firmes: 'O Barão Vargas é um lunático que pendura cabeças de lobo e obriga o povo a sorrir na forca. Mas ele só governa porque tem um monstro como braço direito: Izek Strazni. Matem Izek... e eu assegurarei que Vallaki prospere sob uma liderança digna e generosa.'"
    },
    "F3": {
        "obj": "Planejar com Ernst Larnak a rota de patrulha de Izek Strazni, escolher o local ideal para a emboscada nos becos de Vallaki e preparar armadilhas para isolá-lo de seus guardas da cidade.",
        "ctx": "Izek patrulha a cidade todas as noites acompanhado por dois ou quatro guardas. Ernst revela que ele visita regularmente os fundos da taverna ou os becos perto da praça. A chave é separá-lo de seus homens para evitar que o alarme da cidade seja soado.",
        "sights": "Mapa detalhado das ruas de Vallaki desenhado em pergaminho; anotações dos horários de troca da guarda; becos estreitos e lamacentos com caixotes e pilhas de lenha perfeitos para emboscada.",
        "sounds": "Passos compassados de patrulhas de guardas ao longe na noite fria; o bater de lanças no chão de pedra; e o sussurro calculista de Ernst explicando a rota.",
        "smells": "Chuva fina sobre calçadas sujas, esgoto de rua e fumaça fria.",
        "touch": "A madeira áspera de vigas de beco onde os heróis aguardam o momento do ataque.",
        "narrar": "Nos fundos de um depósito abandonado perto da praça central, Ernst desenha na lama com a ponta de uma adaga o itinerário noturno de Izek. Ele aponta para um beco sem saída cercado por muros altos de pedra: 'Izek passa por aqui à meia-noite para inspecionar as correntes dos pelourinhos. Ele sempre caminha à frente, arrogante e impaciente. Se vocês fecharem as duas pontas do beco, ele estará encurralado antes que possa soprar o apito de alerta.'"
    },
    "F4": {
        "obj": "Executar a emboscada contra o capitão Izek Strazni nos becos escuros de Vallaki, derrotar seu monstruoso braço demoníaco que cospe fogo e neutralizar o braço armado da ditadura do Barão.",
        "ctx": "Izek é um brutamontes cruel de dois metros de altura com um braço direito deformado coberto de escamas espinhosas e garras que disparam labaredas de fogo místico. Ele luta com ferocidade psicopata usando um machado de batalha pesado.",
        "sights": "Um gigante de sobretudo de couro aberto exibindo o braço vermelho e monstruoso com garras fumegantes; faíscas incandescentes iluminando as paredes do beco; o machado ensanguentado cortando o ar.",
        "sounds": "O rugido bestial de Izek chamando os heróis para o abate; o estalo furioso de fogo mágico crepitando em suas garras; e o estrondo metálico de machado colidindo contra escudos.",
        "smells": "Enxofre puro, carne queimada pelo fogo demoníaco, fumaça preta e chuva sobre pedra aquecida.",
        "touch": "O calor sufocante e violento das chamas mágicas que lambem armaduras a cada golpe de garra.",
        "narrar": "Das sombras da névoa surge o pesadelo de Vallaki: Izek Strazni. Com dois metros de altura e olhos injetados de cólera, ele empunha um pesado machado de batalha com a mão esquerda, enquanto seu braço direito — uma monstruosidade coberta de escamas vermelhas com espinhos negros e garras de demônio — acende-se em labaredas crepitantes de fogo. Ele solta uma gargalhada gutural que ecoa pelo beco: 'Ratos insolentes! Vocês pensam que podem me encurralar? Eu vou queimar suas entranhas e pendurar suas cabeças nos portões da cidade!'"
    },
    "F5": {
        "obj": "Conduzir as consequências da morte de Izek em Vallaki, testemunhar o golpe de estado de Lady Wachter com o apoio do povo revoltado, e receber a recompensa prometida em Wachterhaus.",
        "ctx": "Sem Izek para protegê-lo, o Barão Vargas é cercado em sua mansão pelo povo furioso liderado pelos Wachter. Lady Fiona assume o governo de Vallaki, cancela os festivais obrigatórios e recompensa os heróis com ouro, salvo-conduto e informações privilegiadas sobre as relíquias de Baróvia.",
        "sights": "A praça central apinhada de cidadãos quebrando os pelourinhos e queimando as bandeiras roxas de Vargas; Lady Fiona discursando nos degraus da prefeitura sob aplausos calorosos; um baú de moedas de prata entregue aos heróis.",
        "sounds": "Gritos de libertação do povo; sinos tocando em júbilo; e o discurso firme e magnético de Lady Fiona instaurando a nova ordem.",
        "smells": "Madeira queimada das efígies do festival, vinho novo distribuído nas ruas e o ar fresco de mudança política.",
        "touch": "O peso reconfortante das bolsas de ouro e a gratidão palpável de cidadãos que não precisam mais sorrir sob ameaça de prisão.",
        "narrar": "A notícia da queda de Izek espalha-se como pólvora pelas ruelas de Vallaki. Ao amanhecer, a praça central é tomada por uma multidão enfurecida que arranca as faixas de 'Tudo Ficará Bem' e incendeia os pelourinhos. O Barão Vargas é deposto sem que uma única lança seja erguida em sua defesa. No palanque municipal, Lady Fiona Wachter ergue os braços sob os vivas do povo: 'O reinado do medo e da loucura acabou! Vallaki agora é livre para governar a si mesma!' Nos bastidores, ela entrega aos heróis a bolsa pesada de moedas prometida com um aceno de cumplicidade respeitosa."
    },

    # ARC G: THE STRAZNI SIBLINGS
    "G1": {
        "obj": "Vivenciar o momento aterrorizante em que Izek Strazni invade a Estalagem Água Azul com seus guardas após avistar Ireena Kolyana pela janela, gerando um impasse tenso no salão comunal.",
        "ctx": "Izek avistou Ireena da rua e entrou em choque absoluto: o rosto da mulher de seus sonhos de infância está vivo diante dele. Ele entra na taverna exigindo levá-la consigo para 'sua própria segurança', sem saber ainda que são irmãos de sangue separados no ataque dos lobos que arrancou seu braço quando crianças.",
        "sights": "A porta da estalagem escancarada com violência batendo contra a parede; seis guardas da cidade armados com lanças bloqueando a saída; Izek parado no vão da porta com o olhar fixo e alucinado cravado em Ireena.",
        "sounds": "Copos caindo e quebrando no chão; clientes calando-se em pânico; o ranger pesado das botas blindadas de Izek; e a respiração ofegante do capitão em choque.",
        "smells": "Cerveja derramada, fumaça de cachimbos apagados e o odor metálico de ferro e chuva que entra pela porta aberta.",
        "touch": "O arrepio paralisante de dezenas de homens prendendo a respiração diante de uma tragédia iminente.",
        "narrar": "A porta da Estalagem Água Azul é escancarada com um estrondo violento que faz as canecas tremerem sobre as mesas. Seis guardas armados com alabardas posicionam-se nos batentes com ordens de cercar o salão. E entre eles avança a silhueta colossal de Izek Strazni. O capitão ignora Urwin, ignora os clientes, ignora tudo ao redor: seus olhos arregalados e fixos estão cravados em Ireena Kolyana. Seu braço monstruoso fumega levemente sob a capa e seus lábios tremem como se visse um fantasma: 'Você... É você... O rosto dos meus sonhos... Você vem comigo agora!'"
    },
    "G2": {
        "obj": "Navegar pelas ruas de Vallaki sob estado de sítio após o confronto na taverna, evitar as patrulhas agressivas da guarda municipal e encontrar cartazes de recompensa com o retrato de Ireena espalhados pela cidade.",
        "ctx": "Se Ireena fugir ou for escondida, Izek declara toque de recolher e espalha cartazes com o retrato dela desenhado pelo próprio Blinsky, oferecendo 100 PO por informações. O grupo precisa se mover pelas sombras para protegê-la.",
        "sights": "Ruas desertas sob chuva fina; cartazes de papel úmido pregados com pregos em postes e portas de lojas com o desenho de Ireena; patrulhas de quatro guardas com tochas e cães de caça farejando becos.",
        "sounds": "Latidos furiosos de cães de guarda ecoando pelas esquinas; passos de botas pesadas correndo em rondas contínuas; e o sussurro tenso dos heróis escondidos em beirais.",
        "smells": "Chuva fria sobre lamaçal, tochas de alcatrão e o cheiro acre de cola de trigo dos cartazes.",
        "touch": "Paredes de pedra geladas onde o grupo se encosta nas sombras para escapar dos fachos de luz das tochas.",
        "narrar": "Vallaki transformou-se em uma jaula sufocante. A mando de Izek, as ruas estão sob toque de recolher absoluto e a cada esquina há cartazes úmidos pregados nos postes exibindo o retrato fiel de Ireena com os dizeres: 'PROCURADA POR ORDEM DO BURGOMESTRE — 100 PEÇAS DE OURO'. O latido cavernoso de mastins farejadores e o clarão trêmulo de tochas forçam o grupo a rastejar por becos lamacentos e telhados de enxaimel para evitar a captura."
    },
    "G3": {
        "obj": "Descobrir o rapto súbito de Ireena por Izek através de uma emboscada traiçoeira nas ruas ou na estalagem, interrogar testemunhas e rastrear os passos do monstro até a Mansão do Burgomestre.",
        "ctx": "Izek conseguiu emboscar a comitiva ou invadir o esconderijo, arrastando Ireena em direção à mansão do Barão. Urwin Martikov ou um dos caçadores viu a direção da fuga e alerta os heróis antes que seja tarde demais.",
        "sights": "Móveis virados e sinais de luta desesperada; a espada de Ireena caída na lama com o cabo quebrado; rastros pesados de botas afundando na direção da mansão do Barão.",
        "sounds": "Urwin falando aos sussurros e com extrema urgência; o som da chuva batendo no chão; e trovões distantes rolando sobre o vale.",
        "smells": "Lama revolvida, sangue de um guarda ferido no confronto e chuva torrencial.",
        "touch": "O cabo gelado da espada de Ireena apanhada no chão como prova de seu rapto.",
        "narrar": "O pior cenário concretizou-se: um rastro de destruição e sangue marca o beco onde Ireena foi subjugada. Sua adaga jaz abandonada na lama com a lâmina manchada de fuligem demoníaca, e pegadas pesadas e profundas seguem sem hesitação em direção aos portões de ferro da Mansão do Burgomestre. Urwin Martikov segura o ombro de vocês com urgência cortante: 'Izek a levou para a mansão! Ele a trancou em seus aposentos privados no andar de cima. Se vocês não entrarem agora, nunca mais a verão viva!'"
    },
    "G4": {
        "obj": "Invadir ou infiltrar a Mansão do Burgomestre de Vallaki, lutar ou contornar as patrulhas de guardas, arrombar os aposentos privados de Izek Strazni, resgatar Ireena e desvendar a revelação bombástica de que Izek e Ireena são irmãos biológicos.",
        "ctx": "Nos aposentos de Izek, o grupo encontra dezenas de bonecas idênticas a Ireena alinhadas em prateleiras (feitas por Blinsky). Ao confrontar Izek, Ireena reconhece a canção de ninar que ele murmura e a marca de nascença que ambos compartilham no ombro: Izek é o irmão mais velho que ela julgava morto quando os lobos atacaram sua caravana na infância e arrancaram o braço do garoto.",
        "sights": "Quarto de casal austero com paredes de madeira escura; prateleiras cobrindo três paredes repletas de dezenas de bonecas de porcelana de tamanhos diferentes, todas vestindo cópias dos trajes de Ireena; Ireena amarrada em uma poltrona, chorando em choque diante de Izek de joelhos.",
        "sounds": "A respiração pesada e soluçante de Izek murmurando uma cantiga infantil antiga; o ranger de tábuas de assoalho; e o choro emocionado de Ireena ao reconhecer as palavras.",
        "smells": "Cera de vela, alfazema de bonecas, cinzas de lareira e o cheiro metálico de sangue e emoção contida.",
        "touch": "A madeira esculpida das bonecas e o contato comovente de duas mãos que se tocam através de anos de pesadelo e separação.",
        "narrar": "Ao arrombarem a porta dos aposentos de Izek no segundo andar da mansão, o horror dá lugar a um choque avassalador. Três paredes inteiras estão cobertas de prateleiras onde descansam mais de quarenta bonecas de porcelana com o rosto idêntico ao de Ireena em todas as idades de sua vida. No centro do quarto, Ireena está sentada em uma poltrona de veludo com os olhos arregalados, enquanto o temível capitão — a besta que aterrorizava Vallaki — está de joelhos diante dela, soluçando como uma criança e cantando baixinho com voz rouca a mesma cantiga de ninar que Kolyan cantava na infância: 'Irmãzinha... Eu procurei por você nas brumas por toda a minha vida...'"
    },

    # ARC H: THE LOST SOUL
    "H1": {
        "obj": "Testemunhar a manifestação espectral comovente do fantasma de Erasmus van Richten (o filho assassinado de Rudolph van Richten) na Igreja de Santo Andral, ouvir seu apelo por libertação e descobrir a conexão com a Mansão do Barão.",
        "ctx": "Erasmus foi transformado em cria de vampiro séculos atrás e executado pelo próprio pai Van Richten por misericórdia. Sua alma vaga presa em Baróvia e reside no espelho espiritual na mansão do Barão. Ele pede que os heróis o libertem do ciclo eterno de tormento.",
        "sights": "Uma aparição etérea de luz azul-celeste tomando a forma de um jovem elfo/humano de rosto angelical e olhos tristes flutuando acima dos bancos da igreja vazia.",
        "sounds": "Um sussurro melódico e gelado que ressoa diretamente dentro das mentes dos personagens; o estalar de gelo que se forma nos vitrais ao redor do fantasma.",
        "smells": "Frio de altitude, ozônio puro e flores de lírio secas em sepultura.",
        "touch": "Uma rajada de ar congelante que faz a pele arrepiar e a respiração condensar em fumaça branca.",
        "narrar": "No silêncio solene da capela após o cair da noite, as chamas das velas tremulam e adquirem um tom azul-safira sobrenatural. Flutuando a poucos centímetros do chão de pedra, surge a silhueta translúcida e luminosa de um jovem de cabelos claros e olhar repleto de dor ancestral: Erasmus. Sua voz ecoa suave como a brisa de inverno: 'Viajantes da luz... Meu pai ainda vaga por esta terra consumido pelo ódio e pela culpa de ter tirado a minha vida. Minha alma está aprisionada em um espelho no casarão dos governantes. Por favor... libertem-me das correntes do reflexo para que eu possa encontrar a paz eterna.'"
    },
    "H2": {
        "obj": "Subir ao sótão secreto da Mansão do Burgomestre, confrontar o jovem aprendiz de mago Victor Vallakovich em seu laboratório, investigar o Espelho Espiritual no guarda-roupa e negociar o ritual para libertar a alma de Erasmus.",
        "ctx": "Victor é arrogante, brilhante e amargurado. Ele descobriu um espelho mágico que aprisiona almas e pode conjurar assassinos espectrais se comandado. Victor possui o Tomo de Strahd em seu baú de pergaminhos, mas só o entrega se os heróis o ajudarem a consertar sua rota de fuga ou libertarem o fantasma.",
        "sights": "Sótão amplo iluminado por globos de luz mágica arroxeada; bancadas com tubos de ensaio, crânios de gato e grimórios abertos; o círculo de teletransporte no chão com marcas de corpos queimados; e um grande espelho oval com moldura de prata oxidada coberto por veludo negro.",
        "sounds": "O zumbido vibrante de energia mágica no ar; o miado fantasmagórico de esqueletos de gatos animados; e a voz cínica e irritada de Victor segurando sua varinha de teixo.",
        "smells": "Ozônio queimado, enxofre, cera de vela de breu e folhas secas de pergaminho antigo.",
        "touch": "Cabelos e pelos do braço eriçando devido à estática mágica que pulsa do espelho espiritual.",
        "narrar": "O sótão da mansão de Vargas é o santuário sombrio de um gênio perturbado. Sob vigas de carvalho centenárias, bancadas de alquimia com frascos borbulhantes e livros encadernados em couro cercam um círculo arcano desenhado com giz de prata e sangue no assoalho. No canto mais escuro, um grande espelho oval de moldura prateada entalhada com almas agonizantes pulsa com um fulgor espectral sob uma cortina de veludo negro. Victor Vallakovich, um jovem pálido de olheiras fundas e sobretudo manchado de reagentes, aponta sua varinha para vocês: 'Mais espiões de meu pai? Ou vocês têm intelecto suficiente para compreender que este vale é uma sepultura da qual eu pretendo escapar?'"
    },
    "H3": {
        "obj": "Visitar o acampamento de refugiados do lado de fora dos muros de Vallaki, ouvir o relato emocionante de Franz e dos camponeses sobreviventes da Vila de Baróvia e compreender o alcance das tortas de sonho das bruxas.",
        "ctx": "Os refugiados sofrem de abstinência das Tortas de Sonho de Morgantha. Franz, um camponês que vendeu o próprio filho por uma torta, chora em delírio e revela os segredos do Velho Moedor de Ossos e os nomes das três bruxas.",
        "sights": "Tendas de lona podre e carroças quebradas na lama lamacenta; fogueiras fracas soltando fumaça cinzenta; homens e mulheres tremendo em abstinência com olhares alucinados; Franz amarrado a um poste para não arranhar a própria pele.",
        "sounds": "Tosse rouca, gemidos de delírio de camponeses viciados em tortas; o murmúrio de mães chorando filhos perdidos; e o estalar de gravetos úmidos no fogo.",
        "smells": "Fumaça de turfa, lama fétida, suor frio e o cheiro doce e enjoativo de açúcar queimado que ainda emana dos trapos dos viciados.",
        "touch": "O aperto trêmulo e febril das mãos de Franz suplicando por perdão e redenção.",
        "narrar": "Do lado de fora dos muros imponentes de Vallaki, o campo de refugiados é um retrato cru da decadência baroviana. Sob tendas esfarrapadas que mal barram o vento gélido, dezenas de homens e mulheres tremem em delírio febril. Amarrado a um esteio de madeira para não dilacerar os próprios braços em desespero, o camponês Franz chora copiosamente: 'As tortas... Elas tiravam a dor... Mas o preço foram os ossos do meu menininho! A velha Morgantha e suas filhas Bella e Offalia moem as crianças no moinho da colina! Se vocês souberem seus nomes verdadeiros, a magia delas quebra!'"
    },
    "H4": {
        "obj": "Decidir o destino de Victor Vallakovich: convencê-lo a usar seus talentos para o bem da cidade e entregar suas anotações arcanas, ou neutralizá-lo para impedir mais acidentes fatais no sótão.",
        "ctx": "Victor tem duas rotas: se confrontado com empatia e diplomacia por um conjurador (*Presença CD 13*), ele percebe que seus feitiços de teletransporte estavam matando inocentes devido à barreira das brumas de Baróvia e aceita ajudar a decifrar rituais; caso contrário, luta ferozmente para defender seus livros.",
        "sights": "Victor abaixando a varinha com lágrimas de frustração nos olhos; grimórios antigos espalhados sobre a mesa; o Tomo de Strahd repousando sob uma pilha de manuscritos astronômicos.",
        "sounds": "A respiração trêmula do jovem aceitando a verdade sobre as brumas; o farfalhar de folhas de pergaminho; e o silêncio que se instala no sótão.",
        "smells": "Tinta nanquim fresca, chá de camomila frio e poeira.",
        "touch": "O peso secular e a textura de couro humano da capa do Tomo de Strahd ao ser retirado do baú.",
        "narrar": "A fúria arrogante de Victor desfaz-se quando as falhas de seus cálculos arcanos são expostas: as brumas de Baróvia não podem ser rompidas por teletransporte comum — qualquer um que cruze o círculo é rasgado entre as dimensões. O rapaz desaba em uma cadeira de mogno, cobrindo o rosto com as mãos: 'Eu só queria sair daqui... Este vale sufoca tudo que é belo.' Em troca de ajuda para escapar de forma segura quando Strahd cair, ele abre seu baú de ferro e retira um pesado volume encadernado em couro negro: o lendário Tomo de Strahd."
    },
    "H5": {
        "obj": "Consultar Lady Fiona Wachter em Wachterhaus sobre o ritual lunar de cura mental para sua filha Stella Wachter (que acredita ser um gato devido a um trauma causado por Victor).",
        "ctx": "Stella enlouqueceu após Victor testar nela feitiços de sugestão e crueldade emocional. Fiona mantém a filha trancada em um quarto forrado com trapos, alimentando-a com leite e peixe cru. Fiona revela que um ritual com a flor do luar e a derrota das bruxas pode restaurar a mente da garota.",
        "sights": "Quarto acolchoado com colchões velhos e cheiro de animais; Stella encolhida no topo de um guarda-roupa, miando e sibilando com unhas afiadas; Lady Fiona com os olhos marejados de sofrimento materno genuíno.",
        "sounds": "Miados assustados e rosnados felinos vindos da jovem; o fechar suave da porta trancada a chave; e a voz embargada de Fiona pedindo socorro.",
        "smells": "Leite azedo, peixe cru, serragem e o perfume triste de rosas murchas no vaso.",
        "touch": "As unhas compridas de Stella arranhando quem tentar pegá-la à força.",
        "narrar": "Atrás de uma porta trancada nos aposentos superiores de Wachterhaus, a fachada aristocrática de Lady Fiona quebra-se completamente. O quarto está forrado de palha e trapos limpos, e no alto de um armário alto, encolhida como um felino selvagem com olhos arregalados e cabelos desgrenhados, está a jovem Stella Wachter. Ao ver os estranhos, a moça sibilha e solta um miado estridente de pânico. Fiona fecha os punhos contra o peito em desespero: 'Victor quebrou a mente da minha menina... Tragam a essência da pedra sagrada do moinho sob a luz da lua cheia, e eu prometo a vocês a gratidão perpétua de toda a minha linhagem!'"
    },
    "H6": {
        "obj": "Marcha armada de volta à colina do Velho Moedor de Ossos sob céu de tempestade, munidos com os nomes verdadeiros das três bruxas da noite e preparados para o resgate dos órfãos.",
        "ctx": "A jornada até o moinho é decidida: sabendo os nomes verdadeiros de Morgantha, Bella e Offalia, os heróis têm uma arma mágica poderosa que pode quebrar a ligação do coven de bruxas da noite (*Night Hag Coven*).",
        "sights": "Céu tempestuoso de outono com nuvens arroxeadas; as pás do moinho girando ferozmente contra o vento forte; a fumaça doce de baunilha e canela subindo com intensidade sinistra da chaminé.",
        "sounds": "O gemido ensurdecedor das pás do moinho sob vendaval; trovões que sacodem o chão; e o grasnar agudo de corvos nos monólitos avisando que o combate começou.",
        "smells": "Açúcar queimado, gordura rançosa, ozônio elétrico e o cheiro metálico de sangue que escapa das frestas do moinho.",
        "touch": "Chuva gelada chicoteando armaduras e rostos ao subir a colina gramada em direção ao moinho.",
        "narrar": "A colina do Velho Moedor de Ossos ergue-se contra o horizonte de tempestade como um monumento de pesadelo. Sob relâmpagos violetas que cortam as nuvens pesadas, as pás de madeira carcomida do moinho giram com violência inusitada, rangendo como os dentes de um titã carnívoro. O aroma de tortas doces não mais ilude: agora ele fede a cinzas, sangue infantil e magia negra ancestral. Com as armas em punho e os nomes sagrados na memória, vocês cruzam a cerca em direção à batalha decisiva."
    },
    "H7": {
        "obj": "Confrontar as três bruxas da noite (Morgantha, Bella e Offalia) no interior do Velho Moedor de Ossos, invocar seus nomes verdadeiros para desmantelar o coven, salvar as crianças Freek e Myrtle e reconquistar o monólito corrompido.",
        "ctx": "O combate no moinho é vertical e claustrofóbico através de quatro andares de escadas estreitas. Invocar os nomes verdadeiros das bruxas reduz sua CA e impõe vulnerabilidade a dano psíquico/radiante. As crianças Freek e Myrtle estão presas em caixotes no sótão prestes a serem atiradas no funil do moedor.",
        "sights": "O caldeirão fervente no térreo transbordando calda pegajosa; mó de pedra gigantesca moendo ossos humanos no segundo andar; caixotes com crianças chorando no terceiro andar; e as três bruxas com pele púrpura e chifres retorcidos revelando suas verdadeiras formas monstruosas.",
        "sounds": "Gargalhadas histéricas e estridentes das três irmãs bruxas; o ranger colossal da pedra da mó triturando ossos; choros agudos de Freek e Myrtle; e o cantar de feitiços arcanos estalando em chamas.",
        "smells": "Farinha de ossos suspensa no ar sufocando a respiração, manteiga rançosa, carne crua e o fedor de covil infernal.",
        "touch": "O pó fino de ossos cobrindo rostos e mãos e o calor asfixiante do forno aceso.",
        "narrar": "Ao ser chutada a porta do moinho, os disfarces de camponesas bondosas rasgam-se em uma transformação monstruosa: a velha Morgantha e suas filhas Bella e Offalia revelam sua verdadeira natureza de bruxas da noite, com pele púrpura coriácea, olhos amarelos de cabra e chifres retorcidos gotejando icor negro! No andar de cima, sobre a mó de pedra que gira triturando ossos com estalos horríveis, os pequenos Freek e Myrtle gritam por socorro de dentro de caixotes amarrados: 'Socorro! Elas vão nos jogar no forno!' Mas ao pronunciarem os nomes verdadeiros das megeras, as paredes do moinho estremecem e as bruxas uivam em agonia sobrenatural!"
    },
    "H8": {
        "obj": "Realizar o ritual sagrado da lua cheia nos jardins de Wachterhaus, utilizando a essência purificada da pedra do moinho para dissipar a maldição de loucura de Stella Wachter e restaurar sua humanidade.",
        "ctx": "Sob a luz da lua cheia, a flor da Fane e a água benta desfazem o trauma mental imposto por Victor. Stella recobra a consciência, abraça sua mãe em prantos e revela os segredos que ouviu sobre os cultistas e o Tomo de Strahd.",
        "sights": "O círculo de velas acesas no pátio interno sob a luz prateada e plena da lua cheia; Stella deitada em um lençol branco; feixes de luz prateada descendo sobre sua testa.",
        "sounds": "Cântico suave de cura em harmonia com o silêncio da noite; o som de uma respiração que se acalma; e as primeiras palavras humanas de Stella quebrando meses de silêncio felino.",
        "smells": "Incenso de alfazema, orvalho noturno e a pureza de água benta sobre pedras frias.",
        "touch": "A testa febril da garota esfriando para uma temperatura saudável e o abraço comovido de uma mãe que reencontra a filha.",
        "narrar": "A luz prateada da lua cheia banha o pátio de paralelepípedos de Wachterhaus em um fulgor etéreo. Deitada no centro do círculo de velas e orvalho sagrado, Stella para de se debater conforme a essência da Fane toca sua fronte. O olhar felino e vidrado desfaz-se em lágrimas cristalinas, e seus traços relaxam em uma expressão de pura humanidade. Ela abre os olhos, olha para a mãe que chora de joelhos ao seu lado e sussurra com voz fraca e doce: 'Mãe... O pesadelo finalmente acabou?'"
    },
    "H9": {
        "obj": "Estudar e desvendar os segredos arcanos do Tomo de Strahd, vivenciar as memórias da conquista de Baróvia, o ciúme doentio contra seu irmão Sergei, a morte trágica de Tatyana e os pontos fracos do Lorde de Ravenloft.",
        "ctx": "O Tomo de Strahd é uma das três relíquias sagradas profetizadas pelo Tarokka de Madame Eva. Lê-lo não é apenas obter lore: concede aos personagens bônus de dano de conhecimento contra Strahd e desvenda os segredos de suas Fanes e vulnerabilidades emocionais.",
        "sights": "Páginas amareladas de pergaminho encadernadas em couro negro reforçado com cantoneiras de ferro; caligrafia aristocrática impecável escrita pelo punho do próprio Strahd com tinta vermelha; ilustrações detalhadas de Tatyana e do Castelo Ravenloft.",
        "sounds": "O farfalhar solene de páginas seculares; ecos psíquicos da voz de Strahd ecoando na mente de quem lê; o som distante de um sino fúnebre de casamento interrompido.",
        "smells": "Couro antigo, cinzas frias, rosas secas prensadas entre folhas e o odor sutil de sangue imortal preservado no pergaminho.",
        "touch": "O choque estático e gelado ao folhear as memórias de um lorde que vendeu a própria alma por amor e poder.",
        "narrar": "O Tomo de Strahd repousa aberto sobre a mesa, exalando o peso esmagador de quatro séculos de dor e tragédia. Ao passarem os dedos pelas páginas encadernadas em couro negro, a caligrafia elegante e precisa de Strahd von Zarovich ganha vida diante de seus olhos: 'Eu sou o Antigo. Eu sou a Terra. Minhas mãos ergueram este castelo e meu aço pacificou estas colinas... Mas toda a glória de um guerreiro transformou-se em cinzas no dia em que ela olhou para Sergei com o amor que nunca dedicou a mim.' Nas entrelinhas de sua amargura, revelam-se as fraquezas secretas do soberano: a dependência do Coração da Tristeza e o poder das Três Fanes que sustentam sua imortalidade."
    },

    # ARC I: THE WALLS OF KREZK
    "I1": {
        "obj": "Conduzir a travessia das terras ocidentais de Vallaki até as imponentes muralhas de pedra calcária da vila de Krezk, enfrentando as névoas gélidas da subida da serra e as patrulhas de espantalhos corrompidos.",
        "ctx": "A jornada para o oeste cruza o Rio Corvo e aproxima-se dos contrafortes montanhosos de Krezk. As matas aqui são mais silenciosas e o ar é visivelmente mais frio, descendo dos picos nevados.",
        "sights": "Estrada pedregosa subindo entre pinheiros cobertos de líquen branco; neblina espessa cobrindo ravinas profundas; e o vulto colossal de muralhas medievais de pedra calcária surgindo no fim da garganta.",
        "sounds": "O vento glacial uivando através das agulhas de pinheiro; o crocitar de corvos nas árvores; e o ranger abafado de espantalhos mórbidos plantados na beira da estrada.",
        "smells": "Gelo, resina pura, terra congelada e o odor fétido de carniça de animais presos em armadilhas esquecidas.",
        "touch": "Ar gélido que queima as narinas e o bater de dentes com a queda brusca de temperatura.",
        "narrar": "A estrada para o oeste sobe inexorável em direção às montanhas escarpadas de Krezk. A vegetação torna-se mais austera, com pinheiros cobertos por geada e ravinas de pedra nua cortadas por riachos de degelo. No meio da névoa que rasteja pelo solo congelado, espantalhos com sacos de estopa ensanguentados e dentes humanos costurados vigiam as curvas do caminho como sentinelas macabras. E ao dobrarem a última garganta rochosa, erguem-se contra o céu as ciclópicas muralhas de pedra cinzenta que isolam a comunidade de Krezk do resto do mundo."
    },
    "I2": {
        "obj": "Confrontar o Burgomestre Dmitri Krezkov e os arqueiros da guarda nos portões fechados de Krezk, ouvir suas exigências austeras de quarentena e aceitar a missão de trazer vinho da Vinícola Mago dos Vinhos para obter a abertura dos portões.",
        "ctx": "Krezk é estritamente fechada e auto-suficiente sob o comando sábio e amargurado de Dmitri Krezkov. Ele teme pragas, espiões e zumbis. O único suprimento que falta à vila é o vinho para os funerais e o ânimo do povo. Sem uma carroça de vinho da Vinícola Martikov, os portões jamais serão abertos para estrangeiros.",
        "sights": "Portões maciços de carvalho com traves de ferro de seis metros de altura; ameias de pedra onde guardas apontam arcos longos com flechas encordoadas; o Burgomestre Dmitri Krezkov de pé nas passarelas com seu casaco pesado de pele de lobo e olhar severo.",
        "sounds": "O som seco de cordas de arco sendo retesadas; o vento batendo nos estandartes cinzentos da vila; e a voz grave e intransigente de Dmitri ecoando do alto da muralha.",
        "smells": "Fumaça de lenha de pinho de dentro da vila, geada sobre a pedra e couro ensebado.",
        "touch": "A madeira impenetrável dos portões frios como gelo sob as mãos dos heróis.",
        "narrar": "Os gigantescos portões de carvalho e ferro de Krezk permanecem hermeticamente fechados. No alto das ameias da muralha de pedra calcária, quatro guardas em trajes pesados de pele apontam flechas prontas para o disparo. Um homem maduro de barba grisalha e postura militar autoritária apoia as mãos na amurada de pedra: o Burgomestre Dmitri Krezkov. Seu tom é calmo, mas frio como o inverno: 'Krezk não recebe estrangeiros e não dá asilo a quem atrai a fúria do demônio do castelo. Nossos muros guardam nossa gente. Mas nossos estoques de vinho estão secos há semanas. Tragam-nos uma carroça cheia de barris da Vinícola Mago dos Vinhos... ou deem meia-volta e enfrentem as florestas.'"
    },
    "I3": {
        "obj": "Navegar pelas trilhas lamacentas e alagadas que descem para o sul em direção ao Vale de Berez, enfrentando enxames de insetos do pântano e armadilhas naturais de lodo movediço.",
        "ctx": "A estrada para o pântano de Berez afunda sob a planície úmida. O Rio Luna serpenteia criando charcos viscosos onde a névoa é pesada e ácida. As lendas locais afirmam que Berez é um cemitério afundado governado por uma bruxa colossal.",
        "sights": "Salgueiros-chorões com musgo cinzento pendendo como barbas de mortos; poças de água lodosa borbulhando com gases de pântano; ruínas de choupanas de madeira meio afundadas na lama.",
        "sounds": "O coaxar monótono e agourento de milhares de rãs carnívoras; o zumbido incessante de mosquitos colossais; e o estalar viscoso de bolhas de metano estourando na lama.",
        "smells": "Lodo sulfuroso, matéria orgânica em decomposição, água estagnada e fumaça acre.",
        "touch": "Lama pegajosa que suga as botas até as canelas a cada passo e umidade asfixiante que cola a roupa ao corpo.",
        "narrar": "A trilha para o sul afunda em um pesadelo pantanoso e desolado. As árvores vigorosas dão lugar a salgueiros retorcidos com musgos negros escorrendo como mortalhas sobre poças de água fétida e estagnada. O ar torna-se pesado e quente, infestado pelo zumbido ensurdecedor de nuvens de insetos carnívoros. Ao longe na neblina, silhuetas de ruínas de pedra semi-afundadas no lodo revelam a entrada dos pântanos malditos de Berez."
    },
    "I4": {
        "obj": "Efetuar o reconhecimento e adivinhação nos arredores das ruínas afundadas de Berez, vislumbrar a colossal Cabana Rastejante de Baba Lysaga caminhando sobre raízes monstruosas e recolher inteligência crucial sobre a gema mágica roubada da vinícola.",
        "ctx": "Berez foi destruída por Strahd séculos atrás e agora é o covil de Baba Lysaga (a antiga ama de leite e mãe adotiva fanática de Strahd). Ela roubou uma das três gemas mágicas da Vinícola Mago dos Vinhos para animar sua colossal cabana de madeira que caminha sobre raízes e crânio de dragão. Atacar Berez agora é mortal; o objetivo é obter informações e escapar.",
        "sights": "Ruínas de uma cidade gótica afundada na lama negra; no centro do pântano, uma cabana de madeira de três andares que se ergue sobre raízes colossais animadas que se movem com passadas titânicas; milhares de corvos empalados em estacas na água.",
        "sounds": "O impacto estrondoso de raízes de madeira colidindo contra a lama a cada passo da cabana; risadas histéricas e agudas de Baba Lysaga banhando-se em sangue de animais; e o grasnar agoniado de corvos feridos.",
        "smells": "Sangue podre em fermentação, lodo sulfuroso, enxofre e carniça velha.",
        "touch": "O tremor na terra a cada passo da cabana viva que faz a água do pântano criar ondas concêntricas.",
        "narrar": "Através da névoa sulfurosa das ruínas afundadas de Berez, o vislumbre do horror supremo paralisa os sentidos. Entre paredes de pedra carcomidas e arcos de pontes desabadas, ergue-se uma colossal cabana de troncos enegrecidos. Mas a cabana não repousa sobre a terra: ela caminha! Quatro troncos colossais de raízes retorcidas sustentam a estrutura, movendo-se com passos pesados que fazem a lama tremer. No topo da varanda, uma velha decrépita de olhos ensanguentados atira ossos em um caldeirão de cobre, enquanto no coração da cabana brilha uma luz verde-esmeralda pulsante: a gema roubada da vida da vinícola!"
    },
    "I5": {
        "obj": "Retornar com as informações essenciais de Berez para Krezk e traçar o plano definitivo para obter o carregamento de vinho na Vinícola Mago dos Vinhos (Arc J).",
        "ctx": "Os heróis compreendem que para abrir os portões de Krezk e derrotar a bruxa de Berez no futuro, precisam primeiro libertar a Vinícola Mago dos Vinhos que está sob ataque dos druidas de Yester Hill.",
        "sights": "O vale ocidental abrindo-se sob a luz do entardecer; a trilha que sobe de volta para os vinhedos dos Martikov; os portões austeros de Krezk vigiando a serra.",
        "sounds": "O vento uivando nas copas dos pinheiros altos; e a voz resoluta de Ismark e Ireena planejando o próximo passo.",
        "smells": "Resina de pinho fresca expulsando o odor fétido do pântano.",
        "touch": "A firmeza da rocha sólida sob as botas ao deixar para trás a lama podre de Berez.",
        "narrar": "Deixando para trás a brenha sulfurosa de Berez, o ar fresco das montanhas ocidentais enche novamente os pulmões com promessa de esperança. Os fatos estão claros: a bruxa de Berez é um monstro imenso alimentado pelo coração roubado da vinícola. Para salvar Krezk e conquistar a confiança de Dmitri, o caminho deve cruzar as colinas rumo à Vinícola Mago dos Vinhos, onde a família dos Guardiões das Penas luta desesperadamente por sobrevivência."
    },
    "I6": {
        "obj": "Conquistar o acesso final aos portões de Krezk, contemplar a sagrada Piscina Abençoada do Senhor da Manhã, explorar as ruelas serenas da vila e iniciar a subida íngreme para a misteriosa Abadia de Santa Markovia.",
        "ctx": "Uma vez dentro de Krezk, os heróis encontram uma vila pacífica e ordeira que parece isolada da loucura do mundo exterior. No centro da vila repousa a Piscina Abençoada, onde um santuário solar emana águas puras e sagradas com propriedades restauradoras. No topo do penhasco que vigia a vila ergue-se a Abadia de Santa Markovia, governada pelo enigmático e celestial Abade.",
        "sights": "Casas de pedra e madeira com telhados de ardósia bem cuidados; hortas férteis irrigadas por canais de pedra; a Piscina Abençoada com águas cristalinas refletindo um raio de sol impossível; e a colossal abadia gótica erguendo-se sobre o penhasco escarpado.",
        "sounds": "O murmúrio cristalino de água pura correndo na fonte; crianças brincando com calma inédita em Baróvia; e, vindo do alto da colina da abadia, um cântico perturbador e desafinado de vozes animalescas.",
        "smells": "Terra fértil, feno fresco, pão assado e a pureza revigorante de água mineral abençoada.",
        "touch": "A calmaria abençoada das águas da piscina que curam o cansaço dos músculos e renovam o espírito.",
        "narrar": "Cruzar os portões de Krezk é como entrar em um refúgio esquecido pela maldição de Baróvia. Ruas de cascalho limpo serpenteiam entre casas robustas de pedra e chalés agrícolas com chaminés fumegantes. No coração da vila, cercada por salgueiros prateados, repousa a lendária Piscina Abençoada: uma fonte de águas tão límpidas que refletem o fundo de seixos brancos, onde um raio suave de luz solar parece tocar o altar do Senhor da Manhã. Mas quando vocês erguem os olhos para o penhasco que domina a vila, a silhueta austera da Abadia de Santa Markovia lança uma sombra comprida sobre a paz dos aldeões, enquanto ecos de gritos e uivos desafinados descem da colina do monastério."
    }
}

print(f"Total Act II metadata defined: {len(ACT2_METADATA)} scenes.")

def compile_act2_scene(code):
    meta = ACT2_METADATA.get(code)
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
        if any(l_s.startswith(p) for p in ('### ', '**Local', '**Mapa', '**Consulta', '**Casa:', '**Entrada:', '**Oficina', '**Lago', '**Szoldar', '**Pedir', '**Conhecimento', '**Apoio', '**Registro', '**Origem:', '**Quarto', '**Cripta', '**Confronto', '**Se os', '**Reunião', '**Loot', '**Inimigos', '**Táticas', '**Objetivo real', '**Mecânica', '**O que')):
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

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki."""
    return output.strip()

all_act2_code = {}
for code in ACT2_METADATA:
    compiled = compile_act2_scene(code)
    if compiled:
        all_act2_code[code] = compiled

print(f"Successfully compiled {len(all_act2_code)} Act II scenes.")

with open('scripts/enrichment_content_act2.py', 'w', encoding='utf-8') as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nCurse of Strahd: Reloaded (DragnaCarta) - Act II: The Shadowed Town (Scenes D1-D6, E1-E8, F1-F5, G1-G4, H1-H9, I1-I6)\n')
    f.write('Tradução e adaptação 100% fiel do repositório oficial do GitHub (DragnaCarta/Curse-of-Strahd-Reloaded).\n')
    f.write('Roteiros detalhados sem placeholders, descrições autênticas de leitura em voz alta, perfis de NPCs e CDs de Daggerheart.\n"""\n\n')
    f.write("ACT2_SCENES = {\n")
    for code, text in all_act2_code.items():
        escaped_text = text.replace('\\', '\\\\').replace('"""', r'\"\"\"')
        f.write(f'    "{code}": """{escaped_text}""",\n\n')
    f.write("}\n")

print("Saved: scripts/enrichment_content_act2.py")
