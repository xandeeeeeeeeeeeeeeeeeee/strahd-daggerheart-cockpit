# -*- coding: utf-8 -*-
"""
Curse of Strahd: Reloaded (DragnaCarta) - Act II: The Shadowed Town (Scenes D1-D6, E1-E8, F1-F5, G1-G4, H1-H9, I1-I6)
Tradução e adaptação 100% fiel do repositório oficial do GitHub (DragnaCarta/Curse-of-Strahd-Reloaded).
Roteiros detalhados sem placeholders, descrições autênticas de leitura em voz alta, perfis de NPCs e CDs de Daggerheart.
"""

ACT2_SCENES = {
    "D1": """## Roteiro Completo · D1 · Igreja: abrir a investigação

**Objetivo:** Investigar o roubo dos ossos sagrados de Santo Andral na igreja de Vallaki, conversar com o Padre Lucian Petrovich e Yeska, e iniciar a busca pelas relíquias antes do Festival do Sol Flamejante.

**Contexto & Segredo (DragnaCarta Lore):** A Igreja de Santo Andral é o único refúgio sagrado contra vampiros em toda Baróvia devido aos ossos do mártir Andral sob o altar. Sem eles, o solo sagrado perdeu o hallow e Strahd pode massacrar os refugiados.

**Ambiente & Sensações:**
- *Visão:* Candelabros de ferro forjado banhando bancos de carvalho encerado em luz suave; dezenas de famílias de refugiados deitadas em mantas humildes; a laje de mármore do altar erguida revelando a cripta vazia.
- *Sons:* Murmúrios de orações desesperadas; choro abafado de crianças; o som de vassoura limpando o chão de pedra; e a respiração trêmula do Padre Lucian.
- *Cheiro:* Incenso de olíbano, linho lavado, madeira envelhecida e a friagem de terra que sobe da cripta aberta.
- *Tato:* O choque gélido ao tocar a cripta violada e a tensão quase elétrica de um santuário desprotegido.

**Para narrar:** “Doze candelabros ornamentados banham fileiras de bancos bem cuidados em luz suave de velas, tocando cada canto da capela de Santo Andral com calor acolhedor. No entanto, atrás do altar de mármore, o Padre Lucian ajoelha-se com as mãos trêmulas diante de uma cavidade de pedra aberta: o relicário sob a laje foi forçado e os ossos sagrados do mártir desapareceram.”

### NPCs & Diálogos · Padre Lucian Petrovich
- **Aparência e Postura:** Homem de cerca de 50 anos, feições suaves, voz pausada e acolhedora, mas consumido por angústia secreta. Irmão de Lady Vargas Vallakovich (a esposa do Barão), mas odeia a tirania das festas obrigatórias da cidade.
- **Falas do Mestre:**
  - *“Por favor... falem baixo. Se as pessoas souberem que os ossos se foram, o pânico destruirá o pouco de sanidade que resta a esta congregação.”*
  - *“Santo Andral foi um mártir da luz que morreu resistindo às trevas séculos atrás. Seus ossos mantinham este solo consagrado; nenhum vampiro ou sombra do castelo jamais pôde cruzar estas portas. Mas ontem pela manhã, a cripta foi arrombada. As relíquias desapareceram.”*
  - *“Apenas duas outras pessoas sabiam da existência da cripta secreta sob o altar: a velha beata Yeska e o rapaz que ajuda nos serviços pesados da paróquia, o jovem Milivoj. Encontrem os ossos, meus amigos! Sem eles, o demônio entrará nesta igreja como uma foice no trigo.”*

### Investigação do Relicário
- *A Cripta Vazia (Área sob o Altar):* Uma cavidade forrada de chumbo com 60 cm de profundidade. A laje de mármore foi erguida com uma alavanca de ferro (marcas no rejunte).
  - *Instinto (CD 11):* As marcas na pedra foram feitas por alguém com força física descomunal e pressa, mas sem ferramentas arcanas.
  - *Conhecimento (CD 12):* Quem roubou os ossos não o fez por ganância de ouro (o relicário de prata dourada foi deixado para trás; levaram apenas os fragmentos esqueléticos). O roubo foi encomendado por alguém que serve às trevas de Ravenloft.
  - *Interrogatório de Yeska:* A velha beata chora e confessa (*Presença (CD 10)*) que comentou inocentemente sobre os ossos protetores com o coveiro e servente da igreja, o jovem **Milivoj**, enquanto ele cavava sepulturas no pátio.

**Daggerheart & Mecânicas:** A investigação do roubo dos ossos inicia a contagem regressiva para o temido **Banquete de Santo Andral**. O Mestre abre o Relógio de Tensão de Vallaki (6 unidades). Cada dia sem os ossos avança 2 unidades. Conceda **1 Esperança** ao grupo por assumir a proteção dos inocentes.

**Transição:** Os personagens podem ir aos fundos da igreja para confrontar o jovem coveiro Milivoj (Cena D2 · Milivoj: Culpa e Necessidade).

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "D2": """## Roteiro Completo · D2 · Milivoj: culpa e necessidade

**Objetivo:** Confrontar o jovem coveiro Milivoj em sua casa em ruínas no bairro noroeste de Vallaki, descobrir seu motivo desesperado e obter sua confissão sobre a venda dos ossos para Henrik van der Voort.

**Contexto & Segredo (DragnaCarta Lore):** Milivoj roubou os ossos porque precisava desesperadamente de moedas para comprar comida para seus irmãos menores famintos (Bogan e Zondra) e remédios para sua mãe doente Jarzinka, viciada em tortas de sonho.

**Ambiente & Sensações:**
- *Visão:* Sobrado decadente de madeira podre com venezianas tortas; cômodos minúsculos com colchões de palha no chão; mãe esquálida de olhar vítreo usando colar de contas; crianças descalças com rostos sujos de lama.
- *Sons:* O gemido da porta de entrada rangendo em dobradiças emperradas; tosse seca de criança no canto escuro; e a voz grossa e defensiva de Milivoj ameaçando com uma pá de coveiro.
- *Cheiro:* Madeira encharcada, mofo antigo, terra de cemitério fresca nas botas do rapaz e farinha azeda de repolho cozido.
- *Tato:* Ar gélido vazando pelas frestas das paredes e o chão pegajoso de umidade e miséria.

**Para narrar:** “A estrada lamacenta que leva ao bairro noroeste de Vallaki é áspera e irregular, gelada por uma névoa persistente que parece grudar na terra encharcada. Conforme vocês se afastam da praça central, as ruas se estreitam e os sobrados tornam-se decrépitos. Ao baterem na porta da casa de Milivoj, uma mulher esquálida de olhar vítreo abre uma fresta; ao fundo, um jovem robusto de ombros largos segura uma pá com nós dos dedos brancos de tensão.”

**Casa:** madeira podre, janelas rachadas e sala apertada. Jarzinka, irritada após terminar os doces, atende. Bogan (12), Zondra (10), Lazlo (8), Grilsha (7), Dargos (5), Victoria/Vasha (gêmeas de 4) e Jirko (3) dependem do irmão Milivoj. O pai Oleg, ex-guarda, foi ferido por lobos; ambos os pais ficaram dependentes dos doces.

**Entrada:** Bogan diz que Milo está doente. Urgência explícita ou Presença (CD 10) faz Zondra chamá-lo. Ele aparece carregando os menores, deixa-os com Bogan e enfrenta visitantes. Sinais de tensão são visíveis a quem observa; Instinto (CD 10) pode distinguir evasão de simples hostilidade.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "D3": """## Roteiro Completo · D3 · Arasek: a carroça que parece perigosa

**Objetivo:** Investigar o depósito de carroças Arasek Stockyard em Vallaki, questionar os proprietários Gunther e Yelena Arasek e examinar a misteriosa carroça de circo trancada pertencente a Rictavio.

**Contexto & Segredo (DragnaCarta Lore):** A carroça de circo de Rictavio está estacionada no pátio cercado por muros altos. Letras desbotadas dizem 'Carnaval de Rictavio'. Dentro da carroça não há animais dóceis, mas sim um tigre-dentes-de-sabre treinado para caçar vampiros e Vistani.

**Ambiente & Sensações:**
- *Visão:* Pátio lamacento cercado por estacas de madeira; galpões com arreios, cordas e fardos de feno; e uma grande carroça de viagem com grades reforçadas de ferro e cadeado robusto.
- *Sons:* O relinchar inquieto de cavalos de tração; mastigação abafada e respiração pesada de uma fera carnívora vindo de dentro da carroça; e o estalo de correntes de ferro.
- *Cheiro:* Esterco de cavalo, feno molhado, couro curtido e o odor forte e almiscarado de um predador de grande porte enjaulado.
- *Tato:* Cadeados de ferro gelados pela geada e a madeira da carroça vibrando quando a fera se move em seu interior.

**Para narrar:** “O depósito de carroças de Arasek é um pátio de terra batida cercado por muros altos de madeira, onde carroças de carga e fardos de feno repousam sob a neblina. No canto sul do terreno, isolada das demais, repousa uma carroça de viagem com laterais pintadas em cores circenses desbotadas. Um pesado cadeado de ferro prende a porta traseira, e de dentro das frestas reforçadas emana um rosnado baixo e gutural que faz os cavalos das baias vizinhas estremecerem.”

**Local N5:** pátio de estoque, loja/galpão dos Arasek, carroça de Rictavio. A pintura velha contrasta com a placa “Carnaval das Maravilhas”, recém-pintada: indício de uma identidade preparada recentemente.

**Se tentam entrar:** Lucian desencoraja arrombamento. A carroça sacode, ouvem garras pesadas. Na verdade, Erasmus, poltergeist filho de Van Richten, protege Arabelle, escondida ali; não há tigre vivo nesta revisão.

**Tranca em DH autoral:** Finesse (CD 15) com ferramentas apropriadas; Força (CD 18) para romper sob risco de chamar atenção. Falha chama observadores/Erasmus assusta e faz objetos se moverem; não transforma a menina em alvo automático. Uma chave ou autorização de Rictavio elimina o teste.

**Interior se aberto:** palha macia, manta de lã, alguns livros, menina vistana abraçando tigre-dentes-de-sabre de pelúcia, colar com amuleto de cobre. Ela é Arabelle; adiante E8 conforme o que realmente descobrirem.

**Escolha:** ouvir a criança e confrontar Rictavio, chamar família ou deixá-la protegida. A descoberta não obriga reiniciar toda a investigação E nem autoriza um NPC a apagar a memória do grupo.

**Registro:** carroça aberta/danificada, Arabelle encontrada, proteção de Erasmus, notícia enviada a Luvash/Arrigal/Rictavio. O prazo dos ossos segue correndo; não interrompa o calendário para a nova trama.

**Origem:** Reloaded, Arco D, e áreas N1/N5/N6 do livro fornecido. Valores DH autorais ainda sem teste de mesa; substituem as orientações mecânicas resumidas abaixo.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "D4": """## Roteiro Completo · D4 · Loja de caixões: entrada, ossos e armadilha

**Objetivo:** Invadir a oficina de caixões de Henrik van der Voort, confrontar o marceneiro e sobreviver à emboscada orquestrada pela noiva vampira Volenta Popofsky e seis crias de vampiro famintas no depósito do andar superior.

**Contexto & Segredo (DragnaCarta Lore):** Henrik comprou os ossos a mando de um nobre cavalheiro (Vasili von Holtz / Strahd disfarçado). A noiva Volenta Popofsky, usando sua sinistra máscara de caveira de porcelana, escondeu seis crias de vampiro nos caixões do sótão prontas para atacar Vallaki durante o Festival.

**Ambiente & Sensações:**
- *Visão:* Sobrado de dois pavimentos com dúzias de caixões de pinho inacabados empilhados como dominós; serragem espalhada pelo chão; no andar superior, seis caixões fechados em cavaletes sob vigas escuras do teto.
- *Sons:* O som sibilante de uma plaina parando de repente; o rangido de tábuas de assoalho no piso superior; e o estrondo súbito de madeira estilhaçando quando as tampas dos caixões explodem.
- *Cheiro:* Serragem fresca de pinheiro, verniz de breu sufocante, terra seca de sepultura e o fedor adocicado de carne em decomposição guardada em caixões fechados.
- *Tato:* Poeira de madeira fina grudando no suor da pele e lascas afiadas voando pelo ar na penumbra.

**Para narrar:** “A oficina de caixões de Henrik cheira a resina e morte iminente. No andar térreo, caixões vazios de pinho empilham-se até o teto em fileiras silenciosas. No segundo pavimento, a escuridão é densa, com pó de serra cobrindo o chão. No fundo do depósito sul repousam seis caixões fechados com tampas pregadas. Mas assim que vocês dão o primeiro passo em direção ao quarto onde o saco com os ossos brilha tênue, um ruído horrendo de garras arranhando madeira rompe o silêncio: as tampas saltam com estrondo e olhos escarlates abrem-se na escuridão!”

### NPCs & Diálogos · Henrik van der Voort
- **Aparência:** Homem magro, curvado, de rosto encovado e olhos saltados de terror. Tenta mentir (*Intuição vs Blefe*), mas quebra em desespero quando pressionado (*Presença (CD 11)*):
  - *“Ele me prometeu ouro e proteção! Um cavalheiro de capa preta chamado Vasili... Ele disse que se eu guardasse os caixões e comprasse o saco do garoto, os monstros nunca tocariam na minha loja! Eu não sabia que havia demônios dormindo lá em cima!”*

### Combate & Fuga Tática (As Seis Crias de Vampiro)
- **Classificação:** Seis Crias de Vampiro (Tier 2 Elite). Luta mortal se enfrentada em campo aberto.
- **Objetivo Tático dos Heróis:** O objetivo primordial não é exterminar os seis vampiros de uma só vez, mas agarrar o saco de ossos no quarto de Henrik e **fugir pelas ruas de Vallaki até a Igreja de Santo Andral** antes que as criaturas espalhem o caos pela cidade.
- **Mecânicas da Perseguição:**
  - *Resgatar os Ossos:* *Agilidade (CD 12)* ou *Força (CD 11)* para arrombar o baú do quarto de Henrik e recolher o saco de linho com os ossos sagrados.
  - *Corrida pelos Telhados e Ruelas:* Uma corrida tensa com testes de *Agilidade (CD 13)* para saltar janelas e disparar pela praça de Vallaki enquanto as crias saltam pelos telhados caçando o portador dos ossos.

### Restauração da Barreira Sagrada (Cena D5)
- Ao alcançarem a Igreja de Santo Andral, depositar os ossos na cavidade do altar ativa uma explosão de luz dourada divina que preenche todo o templo.
- Qualquer vampiro que toque o piso da igreja começa a queimar em chamas solares purificadoras (Dano 2d10 radiante contínuo) e é forçado a fugir uivando nas trevas.

**Daggerheart & Mecânicas:** A recuperação dos ossos salva a Igreja de Santo Andral da aniquilação e encerra a maior ameaça de Vallaki. Cada jogador ganha **2 Pontos de Esperança** e a bênção permanente do Padre Lucian (+1 em testes de proteção sagrada).

**Transição:** A vitória ecoa pela cidade e chama a atenção das duas grandes facções políticas de Vallaki: o Barão Vargas Vallakovich e Lady Fiona Wachter (Arcos E e F).

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "D5": """## Roteiro Completo · D5 · Restaurar a proteção da igreja

**Objetivo:** Levar os ossos sagrados de volta à Igreja de Santo Andral a tempo, realizar o ritual de reconsagração e restaurar a barreira divina que protege os refugiados do vale.

**Contexto & Segredo (DragnaCarta Lore):** O retorno dos ossos restaura a magia Hallow na igreja. Se completado antes do anoitecer, as crias de vampiro e o próprio Strahd não podem penetrar o templo.

**Ambiente & Sensações:**
- *Visão:* O altar de Santo Andral iluminado por feixes dourados de luz mística assim que os ossos tocam a cripta; lágrimas de alívio escorrendo pelo rosto de mães e idosos.
- *Sons:* O cântico solene do Padre Lucian em louvor ao Senhor da Manhã; o som suave de sino de prata tocando; e suspiros profundos de esperança na nave.
- *Cheiro:* Incenso de sândalo purificador expulsando o odor de cinzas e morte; ar limpo e aquecido.
- *Tato:* Uma onda de calor e alívio que dissipa o frio sobrenatural dos ossos de quem esteve à beira do abismo.

**Para narrar:** “Conforme o saco com os ossos sagrados é depositado na cavidade sob o altar, o Padre Lucian ergue seu símbolo solar e entoa a prece milenar de consagração. Uma centelha dourada irrompe da pedra, espalhando-se como ondas de calor pelas paredes de pedra da igreja e fazendo os vitrais brilharem em matizes vívidos de aurora. A sensação asfixiante de pavor desvanece instantaneamente: o solo sagrado de Santo Andral está restaurado.”

### Se perderam o prazo

A proteção termina no amanhecer e a ameaça ao anoitecer fica concreta. Avise Lucian/Ireena e dê oportunidade de evacuar, fortificar, interceptar Volenta ou recuperar relíquias. Rito pode ser feito num amanhecer posterior; perder a data não destrói ossos para sempre nem força a morte de todos.

**Ataque, se Volenta ainda puder executar:** use o quadro local de D4, com alvos/terreno da igreja. Evacuação e proteção dos congregantes são objetivos próprios; não aumente fichas porque há vários NPCs. Se Volenta morreu, foi contida ou abandonou a trama, use as consequências desse estado, sem repetir o ataque intacto.

**Avanço:** registrar marco coletivo, sem conceder 1.250 XP individuais ou subir imediatamente por cada tarefa paralela. O guia DH reúne os marcos de Vallaki para o nível seguinte.

**Gatilho posterior:** só quando ossos restaurados **e** Fiona no poder, D6 acontece ao entardecer da primeira noite seguinte. Se um requisito não ocorreu, a cena não é acionada automaticamente.

**Origem:** Reloaded, Arco D, e áreas N1/N5/N6 do livro fornecido. Valores DH autorais ainda sem teste de mesa; substituem as orientações mecânicas resumidas abaixo.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "D6": """## Roteiro Completo · D6 · Rahadin: convite e julgamento

**Objetivo:** Testemunhar a chegada solene e aterrorizante do camareiro Rahadin na praça de Vallaki, ouvir o decreto real de Strahd contra Henrik van der Voort e receber a carta de convite formal para o Jantar no Castelo Ravenloft.

**Contexto & Segredo (DragnaCarta Lore):** Rahadin chega em seu corcel negro representando a autoridade imperial de Strahd. Ele executa Henrik publicamente por 'perturbar a paz do conde' e entrega aos heróis a carta de convite com o brasão de Ravenloft.

**Ambiente & Sensações:**
- *Visão:* O elfo do crepúsculo de feições angulares severas e armadura de placas cinzentas imaculadas; a praça de Vallaki em silêncio absoluto; moradores paralisados de terror diante do camareiro de Ravenloft.
- *Sons:* O sussurro agoniado e fantasmagórico de milhares de almas mortas que emana da aura sobrenatural de Rahadin (*Coro da Morte*); o trote compassado de seu cavalo negro; e sua voz calma, precisa e impiedosa.
- *Cheiro:* Ozônio gélido, ferro polido, couro nobre e o odor asfixiante de morte militar sem misericórdia.
- *Tato:* A vibração psíquica nos tímpanos causada pelos gritos sussurrados das vítimas de Rahadin.

**Para narrar:** “O som de um trote solitário ecoa pelas ruas de paralelepípedos de Vallaki, fazendo moradores correrem para dentro de casa e trancarem portas e janelas. Rompendo a névoa na praça central, surge um cavaleiro de postura ereta impecável: o camareiro Rahadin, o elfo do crepúsculo de Ravenloft. Uma aura aterrorizante de sussurros fantasmagóricos emana de sua figura, ecoando as agonias daqueles que ele chacinou em séculos de guerras. Ele desce do cavalo, desdobra um pergaminho com o selo real de Strahd e declara o veredito do conde com frieza aristocrática.”

### Defesa · uma conclusão por réu

**Henrik:** coação de Volenta, agente de Strahd; sem antecedentes; sem violência pessoal; colaboração na recuperação; remorso. **Milivoj:** pobreza e irmãos; ignorância do perigo; manipulação por Henrik; sem antecedentes/violência; remorso. Permita reunir provas e testemunho, não exija que o jogador fale como advogado.

**Conversão DH autoral:** um personagem lidera Presença, outros ajudam conforme DH. Evidência relevante concede vantagem, sem empilhar vários dados de vantagem ilimitados. Para Henrik: resultado 10 = marca cruel; 15 = açoite; 18 = multa/trabalho reparador; 20 = liberdade. Para Milivoj: 10 = prisão perpétua; 15 = mutilação; 18 = marca cruel; 20 = açoite. Resultado abaixo de 10 mantém ameaça de execução, mas a cena pausa para última escolha, não encerra o personagem jogador. Esperança/Medo aplicam suas consequências normais ao teste; não altere uma sentença bem-sucedida para satisfazer a crueldade do NPC.

**As punições são atos do tirano, não validação moral:** se a mesa prefere não narrar mutilação graficamente, corte para o resultado e registre. Jogadores podem propor reparação; Rahadin aceita ou contrapõe dentro da severidade obtida. Uma consequência corporal de PJ só nasce de ação/resultado real e acordo de tom, nunca automática por perguntar.

**Estagnação:** pede nova prova, não infinitos testes repetidos com o mesmo argumento. Milivoj pede que não arrisquem vidas e protejam os irmãos. Fiona reconhece vidas salvas e teme represália ao povo; não torna resistência mecanicamente impossível.

### Intervenção física

Rahadin adverte e usa fichas DH do catálogo, com focos, custos e objetivo de incapacitar. Sem vitória gratuita, execução inevitável do grupo ou marca automática enquanto a ficha do PJ marca último PV. Retirada, distração, negociação e resgate clandestino continuam possíveis; use testes conforme posições/guardas. Antes de conflito, descreva claramente poder e consequências políticas.

**Saída:** registre cada sentença, sobreviventes, ajuda à família, atitude de Fiona/Rahadin, conflito aberto e data do convite. Depois de concluir, Rahadin retorna ao castelo. O segue com essas relações reais.

**Origem:** Reloaded, Arco D, e áreas N1/N5/N6 do livro fornecido. Valores DH autorais ainda sem teste de mesa; substituem as orientações mecânicas resumidas abaixo.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E1": """## Roteiro Completo · E1 · Blinsky: brinquedo e conexões

**Objetivo:** Visitar a bizarra oficina de brinquedos Blinsky Toys em Vallaki, conversar com o excêntrico fabricante de brinquedos Gadof Blinsky e seu macaco Piccolo, e descobrir a sinistra encomenda da boneca idêntica a Ireena Kolyana feita por Izek Strazni.

**Contexto & Segredo (DragnaCarta Lore):** Blinsky é o único fabricante de brinquedos de Baróvia e opera sob o lema 'Não é divertido? É Blinsky!'. Izek Strazni, o capitão demoníaco da guarda municipal de Vallaki, sonha compulsivamente com uma mulher de cabelos ruivos desde a infância e obriga Blinsky a confeccionar dezenas de bonecas idênticas a Ireena a cada mês.

**Ambiente & Sensações:**
- *Visão:* Loja apinhada de prateleiras com brinquedos macabros: guilhotinas em miniatura, bonecos enforcados que se debatem ao puxar uma cordinha, palhaços sem olhos; um macaco de pelo verde e colete vermelho (Piccolo) pulando sobre caixas; e uma boneca de porcelana com o rosto exato de Ireena.
- *Sons:* O chiar agudo de caixas de música desafinadas; risinhos mecânicos de bonecos de corda; o ganido travesso do macaco Piccolo; e a voz animada e com sotaque exagerado de Blinsky.
- *Cheiro:* Serragem, tinta a óleo fresca, cola de ossos fervida, óleo de engrenagem e fumaça de cachimbo de cerejeira.
- *Tato:* O toque perturbador e frio de porcelana pálida esculpida com as feições de Ireena.

**Para narrar:** “A oficina Blinsky Toys parece uma vitrine de pesadelos infantis. Sob uma placa que declara em letras tortas: 'Se Não É Divertido, Não É Blinsky!', dezenas de brinquedos bizarros ocupam prateleiras até o teto: pequenas forcas de madeira com bonecos que se debatem, caixas de surpresa com cabeças decepadas e marionetes macabras. No balcão, um homem gordo de bochechas coradas e colete xadrez ajusta o chapéu de um macaco minúsculo enquanto lustra a bochecha de uma boneca de porcelana que traz, com fidelidade assustadora, o rosto exato de Ireena Kolyana.”

### Loja de brinquedos N8

Nesta revisão fica **ao norte da praça**, mesmo que uma planta antiga a coloque em outra rua. Gadóf Blinsky é afável, excêntrico e orgulhoso de seus brinquedos macabros; o letreiro brinca com a falta de diversão. Piccolo, seu macaco, foi presente de Alanik Ray há três meses: esse nome é uma identidade antiga de Van Richten, informação que Blinsky não conhece. Não revele o disfarce por uma narração onisciente aos jogadores.

**Brinquedos visíveis:** bonecas de expressão triste, fantoche de enforcado, pequenos mecanismos grotescos e uma série de bonecas ruivas com rosto de Ireena. O presente de Eva já está pago; permita escolher algo apropriado, sem exigir converter moedas D&D em dezenas de transações DH.

**Bonecas de Ireena:** não estão à venda. Izek exige uma versão nova periodicamente e ameaça o artesão. Presença (CD 10) com argumento/pressão plausível ou demonstração direta da semelhança pode fazê-lo explicar a encomenda. A retirada de uma boneca à força também provoca a explicação, mas prejudica a confiança. Blinsky teme represálias e não sabe a causa da obsessão de Izek.

**Outros assuntos:** o barão paga por peças para festivais; ele fez a prótese de uma viajante chamada Ezmerelda. Admira Fritz von Weerg e sonha recuperar seu homem mecânico, perdido em Ravenloft: Pidlwick II, gancho futuro, não um tesouro gratuito presente na loja.

**Ao sair:** Izek e dois guardas pregam proclamações do festival. Descreva a mão monstruosa e a autoridade abusiva, mas não force combate. Registre se Izek viu Ireena, se reconheceram as bonecas e se o grupo comprou/recebeu o presente.

**Seguir:** E2 para a família de Arabelle; G para consequências da atenção de Izek. Os relógios dos ossos e do festival continuam.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E2": """## Roteiro Completo · E2 · Acampamento vistani e Kasimir

**Objetivo:** Adentrar o acampamento Vistani e a colina dos elfos do crepúsculo nos arredores sul de Vallaki, conhecer os líderes Luvash e Arrigal, ouvir o lamento desesperado pelo desaparecimento da menina Arabelle, e conversar com o ancião Kasimir Velikov.

**Contexto & Segredo (DragnaCarta Lore):** Luvash e Arrigal lideram os Vistani de Vallaki. Arabelle, a amada filha de sete anos de Luvash, desapareceu misteriosamente e o pai bebe em fúria cega enquanto pune seus servos. Na colina ao lado vivem os elfos do crepúsculo sobreviventes liderados por Kasimir Velikov, mutilados por Strahd séculos atrás.

**Ambiente & Sensações:**
- *Visão:* Uma colina com dezenas de carroças coloridas cercadas por barris de vinho; homens Vistani abatidos e armados com cimitarras; choças miseráveis de pele e estacas onde elfos do crepúsculo de orelhas cortadas observam em silêncio solene; e Kasimir em sua tenda lendo runas antigas.
- *Sons:* Gritos furiosos de Luvash ameaçando seus homens com um chicote de couro; gemidos de punição; cães de caça latindo; e o vento uivando na colina descampada.
- *Cheiro:* Fogueiras de turfa, ensopado picante, vinho derramado na lama, couro cru e o cheiro acre de sangue de açoitamento.
- *Tato:* O aperto de mão de ferro de guerreiros endurecidos e a cicatriz áspera nas orelhas decepadas de Kasimir.

**Para narrar:** “No topo de uma colina a sudoeste de Vallaki ergue-se o acampamento Vistani. Dezenas de carroças vistosas cercam uma grande fogueira central, mas o ambiente não é de festa: homens de feições tensas empunham cimitarras enquanto gritos furiosos ecoam da tenda principal. Luvash, com os olhos vermelhos de vinho e cólera, chora o sumiço de sua filha Arabelle, ameaçando enforcar seus guardas. Na base da colina, em cabanas miseráveis, os últimos elfos do crepúsculo — homens de orelhas decepadas e olhares milenares — observam em silêncio a agonia de seus captores.”

**Local N9:** acampamento de carroças no alto de uma colina, cerca de meia milha/dez minutos de Vallaki; casebres dos elfos sombrios na base. Vistanis e elfos são proibidos de entrar na cidade, razão concreta para precisarem da ajuda dos personagens.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E3": """## Roteiro Completo · E3 · Mansão e biblioteca do barão

**Objetivo:** Conseguir audiência na Mansão do Burgomestre com o Barão Vargas Vallakovich e sua esposa Lydia Petrovna, investigar a vasta biblioteca da mansão em busca das notas do arquimago Khazan, e desvendar a oficina secreta do jovem mago Victor Vallakovich no sótão.

**Contexto & Segredo (DragnaCarta Lore):** O Barão Vargas é obcecado pela doutrina fanática de que a felicidade obrigatória repele Strahd. Na biblioteca da mansão repousam anotações sobre a lendária Torre de Khazan no Lago Baratok. No sótão (área N3t), seu filho recluso Victor tenta fugir de Baróvia criando círculos de teletransporte experimentais que já incineraram dois criados.

**Ambiente & Sensações:**
- *Visão:* Casarão imponente de dois pavimentos com brasões do sol esculpidos nas portas; salão nobre com espelhos cobertos por panos roxos; o Barão com seus dois mastins enormes no colo; sótão empoeirado com círculos mágicos traçados com giz e sangue em tábuas chamuscadas.
- *Sons:* Os latidos graves dos mastins do Barão; o riso forçado e histérico de Lydia Petrovna arrumando vestidos de festa; e os estalos arcanos e sussurros de feitiços de teletransporte ecoando do sótão.
- *Cheiro:* Cera de assoalho cara, lavanda seca, pelo de cão e o odor penetrante de ozônio queimado e enxofre no sótão.
- *Tato:* O estofamento de veludo roxo das poltronas do Barão e o arrepio estático no ar ao aproximar-se do círculo arcano de Victor.

**Para narrar:** “A Mansão do Burgomestre exala uma atmosfera de falsa ordem e opressão cortês. O Barão Vargas Vallakovich recebe os visitantes afagando dois mastins gigantescos com sorrisos ensaiados e ameaças veladas a quem demonstrar 'malícia e tristeza'. Mas enquanto a Senhora Lydia costura laços para o próximo festival, os degraus que sobem para o sótão revelam algo muito mais perigoso: feixes de luz púrpura vazam sob a porta do último andar, onde círculos arcanos chamuscados no assoalho mostram que o jovem Victor está brincando com forças que rasgam o tecido da realidade.”

### Conseguir acesso à mansão

Clavdia recebe visitantes e conduz ao escritório de Vargas, com os cães Fang e Claw. Se Ireena já obteve audiência como refugiada, o uso da biblioteca está autorizado. Caso contrário, Vargas troca acesso por investigação da assombração que incomoda empregados há dois meses; não se comove automaticamente com o sumiço de uma criança vistana. Aceitar investigar permite pesquisar antes de terminar o serviço.

**Tereska, cozinheira:** viu reflexo de jovem triste no segundo andar, ouviu respiração fria no sótão, percebeu que Victor come perto da porta da oficina. Valentina, antiga criada, e o mordomo abandonaram o trabalho. A cozinheira oferece pão/queijo para levar a Victor e indica a escada N3o. Lydia mantém seus encontros e roupas do festival, ignorando parte da situação.

**Entrada clandestina:** Vargas fica de dia na biblioteca e à noite no quarto com os cães; Lydia na sala de jantar/quarto; Victor na oficina; Tereska na cozinha/quarto dos empregados; Clavdia no segundo andar pela manhã e primeiro à tarde. Tereska adverte antes de alarmar, Victor pode ouvir uma explicação, Clavdia chama ajuda imediatamente. Alarme traz doze guardas em cerca de dois minutos e Izek um minuto depois. Só aplique confisco/expulsão se forem realmente capturados ou derrotados; bens ficam no armário N3m, junto de Udo preso. Isso permite recuperação, não apaga equipamento de PJ por decreto.

### Biblioteca N3l

Uma hora de pesquisa não identifica o anel, mas revela **Ireena Strazni**, irmã mais nova de Izek; desapareceu aos quatro anos, dezoito anos atrás, em ataque de lobos. Pais Grygori e Fatima foram enforcados pouco depois. Dê esse dado a quem examinar registros genealógicos; um teste pode reduzir tempo, nunca bloquear a revelação principal.

Victor procura *Entidades Etéreas*, de Mordenkainen. Seu grimório tem o sigilo do anel na capa. Mostrar o problema da criança ou Presença (CD 15) convence-o a conversar na oficina.

### Oficina N3t

Victor é inteligente, defensivo e compassivo, amigo de Stella; não um adolescente cruel que matou aprendizes deliberadamente. Murka é seu gato esqueleto, morto por Izek dois anos atrás. Pode começar invisível, mas ruído de papéis/espirro denuncia presença. Um vislumbre de jovem no espelho é Stella, cuja identidade ele ainda tenta esconder. Se confrontado, pede que não a exorcizem e promete conter o incômodo; H aprofunda a verdade.

**Armadilha da porta:** glifo de medo, sem o raio do texto antigo. Examinar runas identifica risco; Conhecimento (CD 15) decifra, Finesse/Conhecimento (CD 15) com meios apropriados neutraliza. Se acionado, reação Instinto (CD 15); falha marca 1 Estresse e desvantagem no próximo teste de aproximação da oficina, removida ao enfrentar a origem do medo com apoio/ação. Não controla decisões do jogador nem obriga cair da escada.

**Conhecimento de Victor:** o anel é de Khazan, construtor de Ravenloft e antigo mago da torre de Lake Baratok. A torre neutraliza magia dos visitantes. Seu grimório foi encontrado há três anos; o círculo de teleporte está geometricamente correto, e o problema vem de Baróvia, não de erro infantil. Pergunta se podem trazer relíquias de Khazan, sobretudo um cajado que acreditava ser convocado por seu nome. **Segredo:** o cajado está na Cripta 15 de Ravenloft, não na torre. Anote o pedido, sem prometer que a torre conterá o objeto.

**Outros ganchos:** templo de âmbar protegido outrora pela ordem de um dragão; Szoldar conhece a trilha para Baratok. O grimório contém versões narrativas de comunicação/medo; isso não concede cartas de domínio, slots ou Remover Maldição aos personagens.

### Entidades Etéreas · consulta para o mestre

O Etéreo Profundo difere da borda etérea junto ao mundo. Fantasmas atravessam como espíritos; bruxas noturnas, pesadelos e aranhas de fase são viajantes físicos. Um espírito incorpóreo na matéria exige capacidade adequada, componente de presa de fase, veneno de aranha de fase ou água benta aplicada à arma para ser atingido. Uma dose serve a uma arma durante um conflito ou três projéteis; não dobra o dano.

Um coração de bruxa noturna, linha ley e lua cheia podem levar até dez pessoas ao Etéreo por uma hora. Pactos de coven dependem de nomes verdadeiros/vínculos de feridas; detalhes operacionais virão em H. Essas são regras especiais da campanha, não magias gratuitas da ficha DH.

**Registro:** parentesco descoberto, acordo com Vargas, pista de Stella, pedido do cajado, sigilo identificado. E4/E5 levam à torre; H permanece aberto.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E4": """## Roteiro Completo · E4 · Lago Zarovich: caçadores e orientação

**Objetivo:** Viajar para a margem oeste do Lago Zarovich, localizar a cabana de preparação de peles dos caçadores Szoldar e Yevgeni, obter orientações seguras sobre as trilhas do norte e examinar a estela ancestral da Sonhadora (Rozana).

**Contexto & Segredo (DragnaCarta Lore):** DragnaCarta Reloaded removeu o clichê do afogamento de Arabelle por Bluto. Em vez disso, a pista da menina e da torre mágica passa pelos caçadores de elite Szoldar e Yevgeni em sua cabana de caça na margem do lago. Eles conhecem os perigos dos lobos do oeste e revelam uma estela esculpida com uma borboleta (o santuário da Sonhadora, uma das Rozana ancestrais).

**Ambiente & Sensações:**
- *Visão:* Águas gélidas e escuras do Lago Zarovich refletindo as montanhas sob névoa rasteira; cabana rústica de troncos com peles de cervo e lobo secando em armações de madeira; estela antiga de pedra com uma borboleta estilizada talhada em relevo.
- *Sons:* O bater suave de marolas gélidas nas pedras da margem; o grasnar distante de garças cinzentas; o som rítmico de facas raspando couro na cabana; e o uivo de vento entre os juncos.
- *Cheiro:* Água doce de degelo, lama de brejo, fumaça de pinho e couro curtido com gordura animal e sal marinho.
- *Tato:* Água congelante que queima a ponta dos dedos ao tocar o lago e a pedra antiga e desgastada da estela de borboleta.

**Para narrar:** “A margem ocidental do Lago Zarovich estende-se em um silêncio melancólico e solene sob o sopé do Monte Baratok. As águas calmas e límpidas como vidro escuro refletem a floresta densa da encosta. Junto a uma enseada pedregosa, ergue-se uma cabana rústica de troncos onde peles de lobos e cervos secam esticadas ao vento frio. Sentados sobre cepos de madeira, afiando longas facas de caça, estão os dois caçadores mais temidos de Vallaki: Szoldar e Yevgeni. Perto dali, uma estela milenar de pedra exibe a figura delicada de uma borboleta com asas abertas — o símbolo esquecido da deusa Sonhadora.”

**Lago Zarovich, margem oeste:** saia pelo portão norte de Vallaki, acompanhe a margem até a cabana de preparação de peles perto da saída do Luna. Árvores, lama, água fria e silêncio compõem o cenário. **Bluto não aparece e não há afogamento roteirizado de Arabelle nesta versão.**

**Szoldar e Yevgeni:** cuidam das armadilhas pela manhã, trabalham na cabana do meio-dia ao entardecer; fora desse período ela fica vazia e trancada, ambos com chave. Interior contém facas, correntes, peles e ferramentas, não um arsenal mágico. Cada caçador tem três flechas prateadas.

**Pedir orientação:** pagamento razoável de serviço, bebidas ou vínculo estabelecido permite guia. Também podem dar direções sem integrar o grupo: portão oeste/Pôr do Sol, ponte do Luna, encruzilhada, ramal noroeste indicado para Lake Baratok. Não troque descobrir rota por combate obrigatório com os caçadores.

**Conhecimento:** lobos do oeste tornaram-se agressivos; suspeitam de mudança de liderança, mas não sabem o covil. A estela próxima com borboleta representa a Sonhadora, uma Rozana; eles não conhecem essa origem. Mostre o símbolo como pista, sem narrar toda a teologia secreta.

**Apoio DH:** guia dá vantagem em um teste de navegação quando seu conhecimento realmente se aplica. Em conflito, uma vez por cena pode usar flecha prateada para suprimir a recuperação de 1 PV de um licantropo até o próximo foco dele ou ajudar a retirada; não recebe ficha de PJ, múltiplas ações ofensivas e cura gratuita.

**Registro:** guia contratado, pagamento, flechas disponíveis e símbolos vistos. Seguir E5; não pare os prazos de Vallaki durante a excursão.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E5": """## Roteiro Completo · E5 · Estrada até Baratok

**Objetivo:** Percorrer a Estrada Svalich em direção ao Monte Baratok, cruzar a secular Ponte do Rio Luna e a encruzilhada setentrional, navegando por trilhas infestadas por feras sob orientação dos caçadores.

**Contexto & Segredo (DragnaCarta Lore):** O Rio Luna desce impetuoso dos picos de Baratok. A ponte de pedra arqueada é antiga e sólida. O ramal noroeste sobe em zigue-zague pelas encostas íngremes em direção à lendária Torre de Khazan.

**Ambiente & Sensações:**
- *Visão:* Ponte de pedra ancestral com muretas cobertas de hera; correnteza rápida e espumante do Rio Luna quebrando sobre pedregulhos; floresta fechada de pinheiros de alta altitude; trilha rochosa que sobe para o norte.
- *Sons:* O rugido caudaloso do Rio Luna correndo sob o arco da ponte; vento forte uivando nas encostas; estalos de galhos nas matas laterais.
- *Cheiro:* Resina pura de pinheiro alpino, ar rarefeito de montanha e água mineral gelada.
- *Tato:* O frio intenso que começa a entorpecer as extremidades conforme a comitiva ganha altitude.

**Para narrar:** “A estrada deixa as terras baixas de Vallaki e sobe rumo aos maciços rochosos do norte. Diante de vocês ergue-se a monumental Ponte do Rio Luna, com seus arcos de pedra resistindo há séculos à fúria de águas turbulentas e espumantes de degelo. Ao cruzarem a ponte, a trilha divide-se: o caminho noroeste afunda em uma garganta arborizada que serpenteia até as margens secretas do Lago Baratok, onde as histórias afirmam que uma torre sem portas nem janelas guarda segredos arcanos de outros mundos.”

### Ponte e pista

Um lenço branco está preso numa raiz doze jardas abaixo da ponte, do lado do rio. As iniciais **R.V.R.** são legíveis. Arabelle o deixou de propósito, assim como o anel, a pulseira e a carta. Examinar a margem encontra o lenço; risco só se houver correnteza ao recuperá-lo. Reação Finesse (CD 10) evita escorregar; falha gera atraso/roupa molhada, não perda automática da pista.

### Encruzilhada

Placa quebrada, quatro árvores mortas e dois espantalhos com penas de corvo. O ramal noroeste leva ao lago; as demais direções continuam conforme o mapa do mestre. Os caçadores percebem que os espantalhos são novos.

**Emboscada, primeira passagem:** ao examinar a placa ou deixar o lugar, os espantalhos e criaturas de gravetos atacam. Dê um sinal anterior de movimento/penas; um teste Instinto (CD 15) pode impedir a posição desfavorável, sem inventar uma rodada de surpresa com ataques grátis.

### Fichas DH autorais · patamar 2

**Espantalho, Padrão:** Dificuldade 14; limiares 9/18; PV 4; Estresse 3; ataque +2; garras 2d6+2 físico corpo a corpo. **Olhar aterrador:** em vez de atacar, foco e 1 Estresse, reação Instinto (CD 14) de um alvo Próximo; falha Vulnerável até agir ou receber apoio de aliado. **Palha inflamável:** dano por fogo impede sua reação defensiva/ocultação até o próximo foco; não duplica todo dano. **Fingir objeto:** imóvel, pode estar Oculto se não for examinado; examinar fornece a pista de artificialidade sem ataque automático.

**Gravetos animados, grupo de Lacaios:** Dificuldade 12; PV 1 cada; ataque +1, farpas 4 físico. Grupo de até quatro pode concentrar um ataque, somando 2 físico por participante adicional; um ataque acertado com dano de pelo menos 5 derruba o alvo e um graveto adjacente por cada 5 de dano adicionais. Não marque limiares/PV de criatura Padrão nos lacaios.

**Composição:** três PJ, um espantalho e dois gravetos; quatro, dois e dois; cinco, dois e quatro; seis, três e quatro. Espantalhos custam 2 PB cada, grupo de lacaios 1; encontro curto antes da ameaça da torre. Se chegarem muito desgastados, os gravetos podem fugir ao primeiro espantalho cair; não aumente PV secretamente.

**Saída:** fugir pela estrada/para árvores é possível; peças podem revelar magia corrompida ligada à floresta. Não contém a solução completa da vinícola. Registrar desgaste, lenço, tempo e perseguidor. E6.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E6": """## Roteiro Completo · E6 · Torre de Khazan e carroça de Ezmerelda

**Objetivo:** Explorar o promontório isolado do Lago Baratok, desvendar o enigma do dragão na porta da Torre de Khazan (o campo antimagia), inspecionar a carroça booby-trapped de Ezmerelda d'Avenir e recuperar o diário de Rudolph van Richten.

**Contexto & Segredo (DragnaCarta Lore):** A Torre de Khazan é uma torre de pedra de 25 metros erguida em uma ilhota conectada por um dique de pedras. A torre é protegida por um poderoso campo antimagia permanente. A porta de ferro só abre com a dança correta dos braços de estátuas de dragão. Do lado de fora repousa a carroça de Ezmerelda, protegida por armadilhas mortais de frascos de fogo alquímico.

**Ambiente & Sensações:**
- *Visão:* Torre cilíndrica de pedra lisa sem janelas erguendo-se em uma península pedregosa; andaimes de madeira podre sustentando um dos lados; a carroça amarela de viagem com cortinas fechadas; e o relevo esculpido de dragões entrelaçados na porta de ferro.
- *Sons:* O vento uivando na superfície calma do Lago Baratok; o eco oco de passos sobre o dique de pedra; e o rangido metálico de trincos e agulhas de armadilha na porta da carroça.
- *Cheiro:* Pó de pedra milenar, enxofre químico de substâncias alquímicas na carroça e ar frio de montanha.
- *Tato:* O amortecimento sobrenatural de toda magia ao cruzar a soleira da torre (o campo antimagia suprime magias instantaneamente).

**Para narrar:** “Em uma península pedregosa que se projeta sobre as águas espelhadas do Lago Baratok, ergue-se a Torre de Khazan. A estrutura cilíndrica de vinte e cinco metros de altura parece esculpida em um único bloco de pedra cinzenta sem janelas, encimada por andaimes de madeira podre. Junto à margem repousa uma carroça coberta pintada em amarelo vivo com detalhes azuis. A porta de ferro da torre não possui fechadura ou maçaneta, apenas entalhes de dragões em relevo cujos braços e caudas formam posições codificadas de um enigma arcano ancestral.”

### V1 · carroça de Ezmerelda

Placas mandam ficar fora e ameaçam incineração. Pegadas de lobos indicam visita na noite anterior, e a carroça está ali há no máximo dois dias. Cheiro de enxofre adverte do perigo. Abrir cadeado por ferramentas ou força exige 20 e pode acionar dispositivos; não significa que todo o interior explodirá como no livro original.

**Entrada segura:** rastejar sob a carroça e examinar encontra alçapão; Instinto (CD 15) se a busca for apressada. Ez usa esse acesso. Entrar por baixo permite observar/desativar os mecanismos por dentro sem enfrentar o disparo da porta.

**Armadilhas da porta, independentes:** rede de prata com farpas e garrafa de fogo alquímico, ambas disparadas por bestas. Conhecimento/Instinto (CD 15) identifica a montagem; Finesse (CD 15) com ferramentas desarma cada uma, risco anunciado antes do teste.

- Rede: reação Finesse (CD 15); falha sofre 1d6 físico e fica Restrito. Soltar cuidadosamente exige ação Força/Finesse (CD 15); falha marca 1 Estresse pelas farpas, sem novo ataque grátis. Aliado corta a rede com ação e ferramenta adequada, sem rolar dano contra CA de objeto.
- Fogo: reação Finesse (CD 15); falha sofre 2d8 mágico, sucesso 1d8. Incêndio progride em **três etapas de ação dedicada a apagar**, por personagens ou ajuda; se ignorado até o próximo foco do mestre, um ocupante exposto sofre 1d8 mágico e o fogo avança para bagagem. Uma ação de retirada evita ficar preso. Não aplique 6d6 D&D a cada turno de todos.

**Interior:** roupa, máscara, perucas, instrumentos, panelas e pequena gaiola com galinha chamada Eggsmerelda, alimentada e com água. Comunicação com animais produz indignação por invasão, não uma chave mágica para a trama. Fundo falso de baú: equipamentos de escalada/disfarce/cura/veneno, Tarokka, algemas, símbolo do Senhor da Manhã, três águas bentas, perfume/antitoxina, corda, espelho, estaca, luneta e pergaminhos. O mapa mostra **estradas e povoações**, sem todos os locais secretos. O diário de Van Richten não está aqui.

**Magia adaptada:** carroça invoca cavalos espectrais com “Drovash” e os dispensa com “Arvesh”; puxam apenas esta carroça e não lutam. Pergaminho de ilusão cria imagem/som estático plausível em alcance Próximo por uma cena, sem dano ou controle de pessoas; usar requer ação e Conhecimento (CD 15). Pergaminho de quebrar maldição neutraliza um vínculo menor identificado mediante ritual de uma hora/Conhecimento (CD 18); não cura a licantropia desta campanha, não restaura Stella sozinho e não rompe a Névoa. Cada pergaminho é consumido ao uso; não concede carta permanente.

**Rastros de outra carroça:** vêm do leste, passam pela torre e seguem sul para a Svalich e depois Vallaki. Numa clareira o solo mostra pintura amarela/branca recente: preparação da placa de Rictavio.

### V2 · enigma das oito escolas

Porta de ferro sem maçaneta, selo vermelho e “KHAZAN” na verga. A cerca de um metro e meio surgem oito botões rúnicos; mudam de posição a cada aproximação, mas sua ordem circular permanece: **Ilusão → Abjuração → Necromancia → Conjuração → Adivinhação → Encantamento → Transmutação → Evocação**, sentido anti-horário. Conhecimento (CD 10) ou formação arcana reconhece os nomes; apresente-os por escrito, sem depender de cores ou conhecimento real de D&D.

**Solução:** sobreponha mentalmente o desenho do anel. Comece numa de suas pontas e siga as linhas, apertando as oito escolas uma vez:

1. Evocação → Adivinhação → Ilusão → Transmutação → Conjuração → Abjuração → Encantamento → Necromancia;
2. ou exatamente o inverso, de Necromancia a Evocação.

Acertar abre a porta. Não há dança de bonecos, dragão azul ou solução por dizer apenas Khazan. Ofereça pistas graduais: as duas pontas são começo/fim; linhas definem caminho; rotação do anel importa. Bons planos resolvem sem teste.

**Erros:** tocar a chapa indevidamente dá choque doloroso, sem dano relevante. Forçar a porta é Força (CD 25); falha libera raio em linha de cerca de trinta metros: reação Finesse (CD 15), 3d8 mágico na falha/metade no sucesso. Repetições **não derrubam a torre**. O primeiro conjunto completo de oito botões em ordem errada desperta gárgulas; podem continuar tentando a solução durante o conflito. Uma falha parcial não cria gárgulas infinitas.

### V3 · andaime e gárgulas

Andaime leva ao buraco do **terceiro andar**, mas alcançar a altura do segundo já desperta as sentinelas. Suporta aproximadamente noventa quilos, incluindo equipamento; avise madeiras cedendo antes de impor queda. Escalada cuidadosa com corda, Finesse/Força (CD 10); sobrecarga ou falha sob risco rompe apoio. Reação Finesse (CD 15) pode agarrar corda/suporte; queda curta 2d6 físico, queda do terceiro 3d6. Pessoas sob os escombros fazem reação Finesse (CD 15), sofrendo 2d6 na falha. Não use dano D&D por metro nem morte automática.

**Gárgula, patamar 2, Brutamontes:** Dificuldade 15; limiares 13/23; PV 5; Estresse 3; ataque +2; garras 2d8+3 físico. Voa; aterrissar/mover não concede ataque adicional. **Capturar:** substitui dano de ataque acertado por Restrito; vítima se liberta com Força/Finesse (CD 15) ou ação de aliado. **Levar ao alto:** em outro foco dedicado, sobe um nível/até Próximo levando a vítima; anuncie a ameaça antes do foco. Mordida exige novo foco/ataque. Se soltar vítima, reação Finesse (CD 15) para agarrar apoio/corda; dano da queda como acima. **Corpo de pedra:** ignore dano meramente cosmético de objetos improvisados, sem resistência geral à metade contra armas comuns.

**Composição:** três PJ, duas; quatro, três; cinco, quatro; seis, cinco. Custam 4 PB cada: perto do teto 3×PJ+2, especialmente após estrada. No DH nível 3 esta é ameaça alta, não o “85% de PV” garantido do texto D&D. Abertura correta e retirada permitem evitar combate. Não reative as mortas nem some todas as variantes simultaneamente.

### Interior V4–V7 · antimagia e pistas

O campo abrange interior e **um metro e meio além das paredes**, excetuando mecanismos/armadilhas de Khazan. Suspende conjuração e efeitos mágicos ativos de visitantes nessa área; volta ao normal ao sair. Não apaga cartas, classes, recursos ou próteses físicas; armadura comum continua protegendo. Avise a sensação de magia apagando. Personagens precisam de luz/equipamento mundanos.

**V4, térreo:** entulho, caixas vazias, quatro golems de argila e elevador de correntes. Os golems apenas atendem comandos de subir/descer para o piso indicado; “Khazan” não concede controle de exército. Elevador lento e trêmulo, sem teste se uso normal. Não atacam salvo atacados; destruir um impede funcionamento do conjunto.

**V5, segundo:** vazio, teias e piso frágil junto ao poço; trechos suportam cerca de sessenta e oito quilos. **V6, terceiro:** mofo, buraco noroeste, piso que suporta só cerca de vinte e três quilos em trechos junto do poço; berço apodrecido, lembrança da criança e companheira de Khazan mortas no parto dois anos após a Névoa. Use elevador ou apoios seguros. Aviso de fragilidade é claro; reação/queda conforme V3, evitando punir cegamente pesos que jogador não teve como estimar.

**V7, quarto:** cama, mesa, cadeira, tapeçarias, fogão e correntes no teto. Armadura de placas **mundana**, não animada. A caixa com a cabeça de Yan foi retirada. Examinar por dez minutos encontra pistas sem teste; Conhecimento/Instinto (CD 15) agiliza:

- adaga de prata embrulhada numa pulseira de contas de criança e carta **Encapuzado**, no travesseiro: recém-chegado de identidade oculta;
- página queimada do diário, lamento do caçador que perdeu o filho para um vampiro e não encontrou descanso; letra corresponde ao guia de vampiros de B e ao manuscrito de lobisomens de C;
- esboço recente da placa “Carnaval das Maravilhas de Rictavio”;
- da janela, manchas amarelas entre plantas aquáticas; a aproximadamente quatro metros e meio da margem, três potes de cerâmica afundados a três metros, dois amarelos e um branco, usados para pintar a carroça.

**Golems, se provocados:** a escolha normal é recuar; não obrigatório combate de quatro monstros. Para resolver, patamar 2, Brutamontes: Dificuldade 16, limiares 15/25, PV 6, Estresse 3, ataque +3, golpe 2d10+3 físico; imunes a efeitos de veneno/doença, sem imunidade geral a armas. Um foco pode empurrar alvo Próximo substituindo dano. Ativam um por vez se agressão localizada; quatro ativos excedem encontro desejado. Avise o risco, permita parar de atacar e retirar-se.

**Registro:** solução, gárgulas/estrutura, equipamentos usados, pistas, carroças, tempo. E7/E8; a torre não contém o cajado.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E7": """## Roteiro Completo · E7 · Regresso com a descoberta

**Objetivo:** Retornar com segurança do Lago Baratok para Vallaki carregando os segredos de Van Richten e as pistas da caçadora Ezmerelda, despistando patrulhas de lobos e batedores que tentam emboscar o grupo.

**Contexto & Segredo (DragnaCarta Lore):** A jornada de volta é tensa: a noite começa a cair e a alcateia de lobisomens sabe que estrangeiros invadiram a área do lago. Se os heróis tiverem resgatado Arabelle ou trazido os manuscritos, devem evitar combates desnecessários na escuridão.

**Ambiente & Sensações:**
- *Visão:* Sombras alongadas dos pinheiros engolindo a Estrada Svalich; olhos amarelos observando da vegetação; o brilho distante das tochas nas torres de Vallaki.
- *Sons:* Uivos distantes em três direções diferentes na floresta; galhos quebrando atrás do grupo; e o bater apressado de botas na lama.
- *Cheiro:* Terra molhada pelo orvalho noturno e o odor característico de pelos de lobo na brisa.
- *Tato:* O arrepio constante de estar sendo perseguido por predadores que esperam um tropeço.

**Para narrar:** “O crepúsculo cai rapidamente sobre as florestas de Baratok, tingindo as brumas em tons roxos e cinzentos. Conforme vocês refazem o caminho rumo ao sul, a sensação de vigilância predatória torna-se insuportável: silhuetas ágeis movem-se entre os troncos no limite da visão, e uivos coordenados avisam que a alcateia está cercando a estrada. Somente o passo acelerado e a visão das tochas acesas nas muralhas de Vallaki prometem refúgio antes que a noite feche suas mandíbulas.”

### Lobisomem DH · patamar 2, Brutamontes

Dificuldade 15; limiares 12/22; PV 4; Estresse 3; ataque +2; garras/lança 2d8+2 físico. **Transformar:** descrição durante seu foco, sem ataque adicional. **Recuperação:** foco e 1 Estresse para recuperar 1 PV, bloqueado por prata/água benta até seu próximo foco; armas comuns podem ferir normalmente. **Mordida:** um ataque normal em vez das garras, 2d6+2 físico; se marcar PV, aplicar exposição à licantropia conforme guia C11, com reação Força (CD 15) e relógio da próxima lua cheia. Não somar automaticamente dano de garra, mordida e lança no mesmo foco.

**Tática:** priorizam quem usa prata; fogem se um cair ou ambos chegarem a metade dos PV. Dois ativos custam 8 PB; três jogadores podem enfrentar só um ativamente enquanto outro mantém rota/ameaça, se desgaste já tornar combate excessivo. Uma rendição/pedido de passagem pode alterar a decisão; a fonte não exige que sejam suicidas.

**Retorno:** não há novo encontro aleatório obrigatório nessa viagem. O prazo de D/G/H avançou pelo tempo real consumido. Registre exposição, estado de Ezmerelda divulgado, prisioneiros/fugitivos, horários. Chegando a Vallaki, E8.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "E8": """## Roteiro Completo · E8 · Rictavio, Arabelle e Arrigal

**Objetivo:** Confrontar o falso mestre de circo Rictavio na Estalagem Água Azul, desmascará-lo como o lendário Rudolph van Richten, devolver a menina Arabelle em segurança a Luvash no acampamento Vistani e consolidar a aliança com os Vistani.

**Contexto & Segredo (DragnaCarta Lore):** Com as pistas da torre e a boneca de Blinsky, o grupo pode confrontar Rictavio. Ele confessa ser Rudolph van Richten e revela que caça o vampiro-mestre há décadas. Devolver Arabelle a Luvash transforma o pai de um bêbado furioso em um aliado eterno que concede tesouros e apoio leal aos heróis.

**Ambiente & Sensações:**
- *Visão:* Rictavio retirando seu chapéu emplumado e exibindo o olhar severo e cabelos grisalhos de um sábio guerreiro; Luvash de joelhos na lama abraçando Arabelle em lágrimas de gratidão; baús de tesouros abertos na fogueira Vistani.
- *Sons:* Canções alegres de violinos explodindo em celebração no acampamento Vistani; taças de vinho se chocando; e a voz grave de Van Richten explicando seus planos táticos.
- *Cheiro:* Vinho de festa, cordeiro assado no espeto, fumo de cachimbo de boa qualidade e a sensação libertadora de dever cumprido.
- *Tato:* O calor das fogueiras Vistani e o aperto de mão firme de Rudolph van Richten selando um pacto de sangue contra Strahd.

**Para narrar:** “No quarto superior da Estalagem Água Azul, a persona jovial de Rictavio finalmente desfaz-se: diante de vocês, retirando os adereços circenses com dedos calejados, está o lendário caçador Rudolph van Richten. Seus olhos cinzentos e penetrantes encaram o grupo com respeito renovado: 'Vocês têm aço em suas almas, amigos. É hora de pararmos de nos esconder nas sombras e começarmos a traçar a queda do tirano.' E quando a pequena Arabelle é entregue nos braços de Luvash no acampamento da colina, o patriarca chora copiosamente, proclamando que os heróis são irmãos eternos do sangue Vistani.”

### Encontrar Rictavio

Arrigal volta a seguir discretamente; Instinto (CD 20) durante vigilância pode descobri-lo. Na estalagem, Danika diz que Rictavio está reparando a carroça em Arasek. Se o aguardam, finge ignorância até ouvir intenção de ajudar/provas ou ameaça à cobertura; então convida ao quarto. Se seguem ao pátio, ajusta repetidamente o mesmo raio da roda traseira esquerda por cinco minutos, movendo os lábios: fala com Arabelle. Observar com atenção descobre a repetição; Instinto (CD 18) percebe de longe.

**Confronto em particular:** ergue espada-bengala, exige prova de que não servem Strahd. Provas de boa-fé bastam; Presença (CD 15) ajuda quando há dúvida. Confere janela/corredor, fecha venezianas, retira chapéu de disfarce e admite ser **Dr. Rudolph van Richten**. Se fracassam diante da carroça, a voz de Arabelle pede que abra: não feche a investigação por um único dado.

### Verdade e cronologia

Yan levou Arabelle num saco ao Luna, para Escher. Van Richten, coletando ervas, viu o saco mover e atacou, lembrando-se de Erasmus: matou Yan, feriu Escher, que fugiu. Interrogou a cabeça por talismã; soube da recompensa por menina de pele oliva, cabelos escuros e olhos lilases. Voltou à torre com Arabelle, mas temeu que Strahd procurasse primeiro a conhecida zona antimagia. Disfarçado de Yan roubou tinta do acampamento, pintou a carroça e entrou em Vallaki como Rictavio na manhã da chegada dos personagens. Deu a Arabelle amuleto antidetecção que antes pertencia à sua aprendiz Ezmerelda; usa outro em si.

**Revolta de Baróvia, se perguntarem:** Doru reconheceu o caçador após sua luta com lobo terrível morto-vivo e ameaçou liderar multidão inexperiente caso ele não assumisse comando. Van Richten aceitou para tentar controlar o desastre. Escher desapareceu nas catacumbas; o caixão de Strahd estava vazio e o ataque destruiu a revolta. Ao fugir, Eva avisou que outra pessoa levaria a notícia e voltar à vila à luz do dia traria sua morte; ele seguiu para Baratok, lamentando o povo. É culpa e medo, não prova de que desejou matar os rebeldes.

### Menina e tio

Interior da carroça: palha limpa, manta, livros, Arabelle abraçando tigre de pelúcia e usando amuleto de cobre. Erasmus, espírito filho de Van Richten, a protege; **não existe tigre vivo**. Ela esperava o grupo por premonição e deixou carta, pulseira, lenço e anel. Não transforme a criança em oráculo que conhece todas as salas e decisões futuras.

Arrigal sai de um beco, agradece a ajuda e ordena que volte com ele. Van Richten o acusa de espionagem: viu-o cochichar com um morcego enquanto roubava tintas. Ambos alcançam armas; Arabelle pede que conversem. Arrigal não sabia da recompensa e **jamais entregaria a sobrinha**, mas teme que Van Richten a tenha manipulado. Acalmar e apresentar provas é o objetivo, sem iniciativa D&D automática.

### Cabeça de Yan · evidência verificável

Van Richten guarda-a numa caixa em compartimento oculto da carroça. O talismã permite perguntar. Cinco respostas essenciais: “Yan”; “servia Strahd”; “Escher transmitiu a ordem”; “levar a menina ao Luna para ser conduzida ao castelo”; “uma lâmina me atingiu por trás”. Outras: prometeram riqueza/poder, ordem recebida ao entardecer anterior à chegada em Vallaki, não conhecia a finalidade última. Arabelle confirma saco, conversa e entrega. O conjunto convence Arrigal; não peça teste extra para invalidar prova clara.

**Talismã dos Ecos, DH autoral:** quatro cargas; ação/1 carga conserva restos sem decomposição por dez dias; ação/2 cargas permite até cinco perguntas a um cadáver com boca, respostas limitadas ao que sabia em vida, sem convocar alma, forçar lealdade ou obter futuro. Pode repetir sessão sem limite arbitrário de dez dias, mas cada sessão consome cargas. Recupera 1d4 ao amanhecer. Ao gastar a última, role d20: 1 desfaz o talismã, demais mantém-no vazio. Esse d20 é efeito específico do objeto, não teste de Esperança/Medo. Van Richten oferece-o ao grupo após resolução; registre cargas.

### Acordo que todos aceitam

Três interesses: Van Richten quer impedir localização por espiões; Arrigal quer menina perto do pai/família; Arabelle quer segurança e conforto. Uma solução plausível que atende aos três é aceita **sem teste obrigatório**: carroça discreta nos bosques perto do acampamento, visitas diárias de Luvash, amuleto mantido e Arrigal desviando informações. Outras soluções válidas são bem-vindas. Não entregue automaticamente local a Strahd porque a preparação presume perseguição futura.

### Premonição e recompensas

Arabelle agradece e diz que o filho de Van Richten concorda que ele é bom. O caçador percebe que Erasmus a acompanha; ela transmite o amor do filho. Em seguida, visão: noite sem amanhecer, mortos marchando, coração vermelho faminto no alto do castelo, céu rompido pelo grito de milhares de almas. Desmaia, dorme e desperta sem lembrar, não sofre dano. **Segredo:** o Coração de Strahd reúne almas para romper seu cárcere, tratado em U.

Arrigal conserva vínculo de espionagem, mas omite o paradeiro da sobrinha/caçador e evita entregar movimentos dos personagens quando possível. Pode prestar **um favor de desinformação plausível**, não controlar Strahd infalivelmente. A recompensa prometida por Luvash vale após confirmação segura.

### Consultas úteis ao caçador

**Licantropia:** não promete cura instantânea. Elixir com flor de acônito da piscina de Krezk, seis horas de preparo e demais ingredientes fornecidos pelo caçador torna a transformação da próxima noite de lua cheia dócil; ainda vira lobo, não se cura. Próxima lua cheia: **Neyavr 8**. Lucian não consegue remover por uma bênção comum.

**Marca de Ireena:** não é mordida ordinária; vampiros reconhecem que devem preservá-la. Ele não conhece toda a razão.

**Entrar no grupo:** recusa por proteção de Arabelle e um motivo íntimo. Instinto (CD 15) percebe que omite algo; não o força a confessar maldição, resolvida em T. Seus itens/disfarces não se tornam estoque ilimitado de magias dos jogadores.

**Saída:** registre Arabelle/local/amuletos, pai informado, acordo, identidade de Van Richten conhecida por quem, favor de Arrigal, talismã/cargas, profecia e prazo da lua. Avanço por marco coletivo, sem 1.250 XP D&D. D/F/G/H permanecem conforme calendário real.

**Origem:** Reloaded, Arco E, e áreas N3/N5/N8/N9/L/V1–V7 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "F1": """## Roteiro Completo · F1 · Convite na Estalagem Água Azul

**Objetivo:** Receber a visita discreta de Ernst Larnak na Estalagem Água Azul, ouvir a mensagem misteriosa e o convite formal da nobre Lady Fiona Wachter para uma reunião confidencial em Wachterhaus.

**Contexto & Segredo (DragnaCarta Lore):** Ernst Larnak é o espião e lacaio mais leal de Lady Fiona. Ela soube das proezas dos aventureiros e deseja recrutá-los para um golpe político contra o insano Barão Vargas Vallakovich.

**Ambiente & Sensações:**
- *Visão:* Um homem esguio de sobretudo cinzento e capuz puxado sentado em uma mesa de canto da estalagem; olhos astutos que acompanham cada movimento dos heróis; uma carta com selo de cera preta exibindo o brasão da família Wachter.
- *Sons:* O zumbido da estalagem cheia cobrindo a voz baixa e sussurrada de Ernst; o tilintar de uma moeda de ouro deixada sobre a mesa.
- *Cheiro:* Cerveja de centeio, fumaça de cachimbo e o perfume sutil de lavanda e cera de lacre na carta.
- *Tato:* O envelope de pergaminho grosso e pesado passado de mão em mão sob a mesa de carvalho.

**Para narrar:** “Enquanto a estalagem vibra com canecas de cerveja e conversas tensas, um homem magro de sobretudo cinza aproxima-se com passos que não produzem som no assoalho. Ele puxa o capuz para trás revelando feições pontiagudas e olhos de falcão: Ernst Larnak. Ele desliza sobre a mesa uma carta selada com cera preta trazendo o brasão aristocrático dos Wachter: 'Minha senhora, Lady Fiona Wachter, solicita a honra de sua presença em sua residência para uma taça de vinho e uma conversa sobre o futuro desta infeliz cidade. Há males que nem mesmo os festivais de Vargas podem disfarçar.'”

**Registro:** convite/data, gatilho, ações públicas observadas, posição de Ireena. D/E/G continuam no mesmo calendário. F2.

**Origem:** Reloaded, Arco F, e áreas N2/N4/L do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "F2": """## Roteiro Completo · F2 · Wachterhaus: proposta política

**Objetivo:** Adentrar o casarão aristocrático e sombrio de Wachterhaus, conhecer Lady Fiona Wachter, descobrir seus ideais políticos e sua proposta para assassinar o monstruoso capitão Izek Strazni em troca de ouro e poder político.

**Contexto & Segredo (DragnaCarta Lore):** Lady Wachter é pragmática, aristocrática e leal à casa von Zarovich. Ela considera Vargas um tirano ridículo que arruinará Vallaki. Ela propõe eliminar Izek Strazni (o braço armado do Barão), prometendo que com a queda de Izek a guarda se renderá e Vallaki terá um governo estável e pacífico.

**Ambiente & Sensações:**
- *Visão:* Casarão imponente com paredes de madeira escura e tapeçarias desbotadas; lareira crepitando com gatos pretos deitados sobre almofadas; um grande retrato do jovem Strahd na parede da biblioteca; e Lady Fiona com seu vestido de veludo negro e anéis reluzentes.
- *Sons:* O ronronar suave de múltiplos gatos; o crepitar cadenciado da lenha na lareira de mármore; e a voz aveludada, culta e cortante de Lady Fiona expondo seu plano com frieza cirúrgica.
- *Cheiro:* Cera de vela pura, incenso leve de cedro, vinho tinto nobre e o cheiro aconchegante de casarão senhorial.
- *Tato:* Cadeiras de encosto alto com estofamento de veludo e taças de prata lavrada cheias de vinho de safra pessoal.

**Para narrar:** “Wachterhaus é uma mansão gótica que respira nobreza e segredos ancestrais. Ao cruzarem os salões de carvalho escuro onde gatos de pelos negros dormem sobre almofadas de veludo, vocês são conduzidos à sala de estar de Lady Fiona Wachter. Uma mulher distinta de meia-idade, com cabelos castanhos presos com elegância e olhar penetrante de quem comanda impérios, serve cálices de vinho com mãos firmes: 'O Barão Vargas é um lunático que pendura cabeças de lobo e obriga o povo a sorrir na forca. Mas ele só governa porque tem um monstro como braço direito: Izek Strazni. Matem Izek... e eu assegurarei que Vallaki prospere sob uma liderança digna e generosa.'”

### NPCs & Diálogos · Lady Fiona Wachter
- **Aparência e Postura:** Mulher de 55 anos, olhar penetrante de estrategista política. Desprovida de medo vulgar de Strahd: para ela, Strahd é o senhor legítimo e eterno da terra, uma força da natureza com a qual se governa através de respeito mútuo, não de histeria.
- **Falas do Mestre:**
  - *“Vargas Vallakovich transformou esta cidade em um hospício a céu aberto. Ele acredita que fingir felicidade afasta o Lorde de Ravenloft! Enquanto isso, crianças morrem de fome e homens livres são jogados no pelourinho por não rirem das piadas sem graça de seus festivais.”*
  - *“Strahd von Zarovich não é um demônio irracional. Ele é o governante incontestado deste vale. Tratem-no com a deferência devida a um soberano, e ele deixará Vallaki em paz. Mas para que a ordem retorne, o tirano Vargas e seu cão de guarda demônio, Izek Strazni, precisam cair.”*
  - *“A proposta é simples e vantajosa para vocês: eliminem Izek Strazni. Sem aquele braço armado e monstruoso, a guarda da cidade se renderá aos meus homens em uma hora. Em troca, darei a vocês o ouro de nossa família, salvo-conduto absoluto em toda a região e a chave da biblioteca onde repousa o tomo ancestral que vocês procuram.”*

### Segredos de Wachterhaus (Investigação)
- *O Tomo de Strahd:* Se as cartas de Tarokka indicaram Wachterhaus, o livro histórico de memórias de Strahd está trancado em uma arca de ferro no sótão de Fiona, guardado por cinco esqueletos servis.
- *O Cadáver de Nikolai Wachter:* No quarto principal do 2º andar, repousa sobre a cama o corpo perfeitamente embalsamado de seu marido Nikolai, coberto de flores preservadas. Fiona dorme ao lado dele todas as noites.
  - *Instinto (CD 13):* Notar o cheiro de sais de embalsamamento que desce pela escada.
- *O Culto do Sol Negro:* Na adega subterrânea, oito cultistas encapuzados realizam reuniões semanais lendo tratados filosóficos sobre as sombras e a nobreza de Ravenloft.

**Daggerheart & Mecânicas:** A negociação com Lady Fiona é um dos grandes dilemas políticos da campanha. Aliar-se a ela liberta a cidade da tirania histérica de Vargas, mas instala um governo leal e complacente com Strahd. A decisão dos jogadores altera permanentemente o destino de Vallaki.

**Transição:** Os personagens decidem se aceitam a missão de emboscar Izek (Cena F4) ou se recusam e buscam aliados na Estalagem Água Azul.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "F3": """## Roteiro Completo · F3 · Ernst e a preparação

**Objetivo:** Planejar com Ernst Larnak a rota de patrulha de Izek Strazni, escolher o local ideal para a emboscada nos becos de Vallaki e preparar armadilhas para isolá-lo de seus guardas da cidade.

**Contexto & Segredo (DragnaCarta Lore):** Izek patrulha a cidade todas as noites acompanhado por dois ou quatro guardas. Ernst revela que ele visita regularmente os fundos da taverna ou os becos perto da praça. A chave é separá-lo de seus homens para evitar que o alarme da cidade seja soado.

**Ambiente & Sensações:**
- *Visão:* Mapa detalhado das ruas de Vallaki desenhado em pergaminho; anotações dos horários de troca da guarda; becos estreitos e lamacentos com caixotes e pilhas de lenha perfeitos para emboscada.
- *Sons:* Passos compassados de patrulhas de guardas ao longe na noite fria; o bater de lanças no chão de pedra; e o sussurro calculista de Ernst explicando a rota.
- *Cheiro:* Chuva fina sobre calçadas sujas, esgoto de rua e fumaça fria.
- *Tato:* A madeira áspera de vigas de beco onde os heróis aguardam o momento do ataque.

**Para narrar:** “Nos fundos de um depósito abandonado perto da praça central, Ernst desenha na lama com a ponta de uma adaga o itinerário noturno de Izek. Ele aponta para um beco sem saída cercado por muros altos de pedra: 'Izek passa por aqui à meia-noite para inspecionar as correntes dos pelourinhos. Ele sempre caminha à frente, arrogante e impaciente. Se vocês fecharem as duas pontas do beco, ele estará encurralado antes que possa soprar o apito de alerta.'”

**Registro:** posse/rotulagem, plano, alvo da segunda garrafa e dia concreto. F4; o sequestro G pode ocorrer antes se deixarem passar Neyavr 6.

**Origem:** Reloaded, Arco F, e áreas N2/N4/L do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "F4": """## Roteiro Completo · F4 · Acompanhar e emboscar Izek

**Objetivo:** Executar a emboscada contra o capitão Izek Strazni nos becos escuros de Vallaki, derrotar seu monstruoso braço demoníaco que cospe fogo e neutralizar o braço armado da ditadura do Barão.

**Contexto & Segredo (DragnaCarta Lore):** Izek é um brutamontes cruel de dois metros de altura com um braço direito deformado coberto de escamas espinhosas e garras que disparam labaredas de fogo místico. Ele luta com ferocidade psicopata usando um machado de batalha pesado.

**Ambiente & Sensações:**
- *Visão:* Um gigante de sobretudo de couro aberto exibindo o braço vermelho e monstruoso com garras fumegantes; faíscas incandescentes iluminando as paredes do beco; o machado ensanguentado cortando o ar.
- *Sons:* O rugido bestial de Izek chamando os heróis para o abate; o estalo furioso de fogo mágico crepitando em suas garras; e o estrondo metálico de machado colidindo contra escudos.
- *Cheiro:* Enxofre puro, carne queimada pelo fogo demoníaco, fumaça preta e chuva sobre pedra aquecida.
- *Tato:* O calor sufocante e violento das chamas mágicas que lambem armaduras a cada golpe de garra.

**Para narrar:** “Das sombras da névoa surge o pesadelo de Vallaki: Izek Strazni. Com dois metros de altura e olhos injetados de cólera, ele empunha um pesado machado de batalha com a mão esquerda, enquanto seu braço direito — uma monstruosidade coberta de escamas vermelhas com espinhos negros e garras de demônio — acende-se em labaredas crepitantes de fogo. Ele solta uma gargalhada gutural que ecoa pelo beco: 'Ratos insolentes! Vocês pensam que podem me encurralar? Eu vou queimar suas entranhas e pendurar suas cabeças nos portões da cidade!'”

### Agenda do dia, se não interrompida

11h acorda/come na mansão com dois guardas; 11h30 inspeciona portões oeste, norte, leste; 13h recebe almoço e duas garrafas na praça; 14h visita três/quatro informantes; 16h nova inspeção dos portões; 17h30 dispensa guardas, passa por Blinsky, segue ao lago; 22h volta ao quarto para refeição e terceira garrafa. Perseguição pública/alarme altera a rotina; não o teleporte para o lago enquanto busca criminosos.

### Trocar a garrafa

**Cozinha:** ao meio-dia Tereska põe duas Purple Grapemash Nº3 no balcão; 12h15 coloca na caixa, começando pela mais próxima; 12h45 leva almoço. Troca física pode usar Finesse (CD 15) conforme acesso/distração. Rotulagem diferente desperta breve surpresa: uma história convincente, Presença (CD 15), pode explicar encomenda especial. Ela não aceita suborno/ameaça simples porque teme Izek. Quem inspeciona ordem das garrafas sabe qual será segunda.

**Praça:** distração plausível separa atenção de Izek/guardas; um líder faz Finesse (CD 15), aliados ajudam conforme DH. Falha parcial pode levantar suspeita antes de perseguição, abrindo chance de recuar. Flagrante de crime traz doze guardas fora de serviço e busca até a noite; missão pode recomeçar no dia seguinte com o calendário avançado.

### Seguir Izek, cenas de tensão

- Bluto oferece peixes malcheirosos na praça e grita ofensas se rejeitado; compra pequena ou Presença (CD 15) acalma. Ele aparece aqui, não afogando Arabelle.
- Informante denuncia doces de Morgantha que fazem sonhar acordado. Mastim sarnento rosna aos observadores; comida ou Instinto (CD 15) evita alarme.
- No portão leste, três refugiados pedem comida/abrigo: lobos cercam acampamento, um quarto depende dos doces. Izek ameaça fogo, pede uma dúzia de virotes de prata de caixa perto do esconderijo e manda comprar doce no dia seguinte. Finesse (CD 15) ou mudança coerente de posição evita o guarda; ou intervir revela identidade e muda o plano.
- Em Blinsky, recolhe boneca de Ireena. Se ausente, agride artesão, queima brinquedos e exige outra até o próximo entardecer. A mesa pode intervir e impedir; não narre ferimento inevitável enquanto PJ agem. Izek esquece a caixa de vinho no balcão. Ajudar o artesão ou Presença (CD 15) conquista colaboração para recolocar o vinho depois.

**Descobertos:** ainda podem esconder-se com Finesse (CD 15), ganhando vantagem por telhado/cobertura preparada com Força/Finesse (CD 10). Confrontados, mentira plausível Presença (CD 10) pode encerrar; falha ameaça prisão. Se Izek já viu Ireena com o grupo, exige seu paradeiro, também Presença (CD 10), com desvantagem para negação contradita por observação. Resistir inicia conflito real, não prisão automática.

### Lago Zarovich · duas formas DH

Sozinho junto à água, bebe segunda garrafa e encara boneca obsessivamente. Ireena presente ou perguntas não o tornam aliado: manda-a afastar-se e tenta dominar o grupo. Ele quer controlar a irmã, não protegê-la segundo suas escolhas.

**Izek I, Enforcer — patamar 2, Solo:** Dificuldade 15; limiares 12/22; PV 6; Estresse 4; ataque +3; machado prateado 2d8+3 físico Corpo a Corpo, podendo empurrar Muito Próximo em vez de +3 dano. **Arremessar chama:** ataque normal Próximo, 2d6+3 mágico; mesmo em corpo a corpo não penalize só por ser projeção. **Giro cortante:** foco/1 Estresse, reação Finesse (CD 15) de quem está Muito Próximo, falha 2d6 físico e Vulnerável até agir para recuperar equilíbrio, sucesso metade sem estado. **Salva de fogo:** foco/1 Estresse, área Muito Próxima em alcance Próximo, reação Finesse (CD 15), falha 2d6 mágico/sucesso metade.

**Indomável:** foco e 1 Estresse remove um estado de origem resistível; não apaga veneno preparado, ferimento ou consequência narrativa definitiva. **Recuo vigoroso:** após dano corpo a corpo, pode gastar 1 Medo para empurrar atacante Muito Próximo e recuar igual; sem ataque gratuito. **Retaliação:** foco normal para avançar e atacar; custos de spotlight adicionais continuam normais DH, não três reações por rodada D&D.

**Transição:** em 0 PV, braço e machado inflamam, pele avermelha. Forma II tem novos PV/Estresse; posição/veneno/estados plausíveis permanecem, excesso de dano não atravessa. Dê foco ao grupo antes da primeira nova ofensiva.

**Izek II, Infernal — Solo:** mesma Dificuldade/limiares, PV 5, Estresse 4, ataque +3; machado 2d8+4 físico ou soco 2d6+4 mágico, este podendo empurrar Muito Próximo em lugar de +4. **Onda flamejante:** foco/1 Estresse, linha até Próximo, reação Finesse (CD 15), falha 2d8 mágico/sucesso metade. **Explosão próxima:** foco/1 Estresse, todos Muito Próximos, reação Finesse (CD 15), falha 2d6+3 mágico/sucesso metade. **Rajada explosiva:** foco/1 Estresse, ponto Próximo/área Muito Próxima, mesma reação/dano e falha Vulnerável até agir para firmar-se. Objetos inflamáveis desprotegidos podem pegar fogo; não destrua armaduras automaticamente.

**Perseguição quente:** foco para deslocar Próximo e socar, como única ofensiva. **Cinzas nos olhos:** após acertarem-no de perto, 1 Medo/1 Estresse, reação Instinto (CD 15), falha desvantagem no próximo ataque dependente de visão; sem dano extra. **Aquecer metal:** 1 Medo/1 Estresse após ferido por arma metálica, usuário escolhe soltar ou marcar 1 Estresse e ter desvantagem no próximo uso da arma; termina após esse uso/ação de resfriar. Não se soma automaticamente a cinzas e soco. Fogo mundano não o fere na forma II; capacidade de fogo mágico pode convertê-lo em pressão/Estresse com justificativa, não invalide uma personagem inteira sem avisar imunidade.

**Ajuste:** três PJ, 4 PV em cada forma e danos sem bônus fixo; quatro, valores acima; cinco, +1 PV em cada; seis, +2 em cada. Solo 5 PB, mas duas formas e ações de área aumentam desgaste. Sem veneno/apoio, sinalize confronto perigoso e deixe retirada; não importe porcentagens D&D como garantia de equilíbrio. Ireena pode uma vez por cena auxiliar teste/retirada ou criar abertura que dá vantagem ao próximo ataque, sem turno completo de personagem adicional.

**Vitória/saque:** machado de prata usável conforme arma DH compatível, pequena provisão de ouro e fragmento de âmbar de **Seriach, Sussurrador dos Cães Infernais**. Apenas portar não concede cães ou imunidade; regras de vestígios/consentimento da oferta aplicam-se. Sem impor morte de PJ ao último PV: use movimentos de morte DH.

**Registro:** destino de Izek, prova obtida, testemunhas, prata, fragmento, desgaste e tempo. F5; G não continua com Izek vivo se morreu.

**Origem:** Reloaded, Arco F, e áreas N2/N4/L do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "F5": """## Roteiro Completo · F5 · Mudança de governo e pagamento

**Objetivo:** Conduzir as consequências da morte de Izek em Vallaki, testemunhar o golpe de estado de Lady Wachter com o apoio do povo revoltado, e receber a recompensa prometida em Wachterhaus.

**Contexto & Segredo (DragnaCarta Lore):** Sem Izek para protegê-lo, o Barão Vargas é cercado em sua mansão pelo povo furioso liderado pelos Wachter. Lady Fiona assume o governo de Vallaki, cancela os festivais obrigatórios e recompensa os heróis com ouro, salvo-conduto e informações privilegiadas sobre as relíquias de Baróvia.

**Ambiente & Sensações:**
- *Visão:* A praça central apinhada de cidadãos quebrando os pelourinhos e queimando as bandeiras roxas de Vargas; Lady Fiona discursando nos degraus da prefeitura sob aplausos calorosos; um baú de moedas de prata entregue aos heróis.
- *Sons:* Gritos de libertação do povo; sinos tocando em júbilo; e o discurso firme e magnético de Lady Fiona instaurando a nova ordem.
- *Cheiro:* Madeira queimada das efígies do festival, vinho novo distribuído nas ruas e o ar fresco de mudança política.
- *Tato:* O peso reconfortante das bolsas de ouro e a gratidão palpável de cidadãos que não precisam mais sorrir sob ameaça de prisão.

**Para narrar:** “A notícia da queda de Izek espalha-se como pólvora pelas ruelas de Vallaki. Ao amanhecer, a praça central é tomada por uma multidão enfurecida que arranca as faixas de 'Tudo Ficará Bem' e incendeia os pelourinhos. O Barão Vargas é deposto sem que uma única lança seja erguida em sua defesa. No palanque municipal, Lady Fiona Wachter ergue os braços sob os vivas do povo: 'O reinado do medo e da loucura acabou! Vallaki agora é livre para governar a si mesma!' Nos bastidores, ela entrega aos heróis a bolsa pesada de moedas prometida com um aceno de cumplicidade respeitosa.”

### Transição

À noite, Fiona e três seguidores vão à mansão. Vargas tenta fugir ao ver que perdeu o protetor; um comando ritual o detém e ele cede o governo. Mantém título, bens/renda e propriedade. Se jogadores intervêm, jogue suas ações, não uma cutscene imutável.

Pela manhã guardas reúnem moradores na praça/palanque do festival. Vargas abdica; Fiona reconhece o grupo apenas com aceno discreto, liberta os presos nos troncos e cancela festivais salvo dias santos. Seu discurso defende segurança, respeito e prudência diante do mundo real e encerra pedindo “santuário na misericórdia das névoas”. Aplauso contido. Lucian nota alusão a Ezra e acredita que ela pode encontrar esperança; lamenta dificuldades da irmã Lydia.

### Recompensa prometida

Entrega até trinta virotes prateados, quatro lanças prateadas, duas armaduras básicas do patamar e uma opção melhor apropriada ao nível, mais prata para revestir duas armas. Escolha modelos oficiais DH compatíveis no catálogo, **sem CA, preço D&D ou bônus mágico adicional pela prata**. Proveniência: arsenal antigo perdido por negligência de Izek. Dinheiro adicional só se negociado; pagamento não duplica se também completaram G.

### Profecia, Leo e história

Na biblioteca N4p, *A Nobre Casa de Wachter*, de Lovina, informa: parente Dilisnya, recebeu terras/título por lealdade a Strahd; escreveu história familiar. No relato do casamento Sergei/Tatyana, Sergei morreu, noiva teria saltado do mirante; Leo liderou motim, matou Vladislav Wachter e sua mãe, trancou Lovina nas cozinhas. Strahd emergiu com poder sobrenatural, derrotou rebeldes e expulsou Leo. Este acusou Lovina de trair o sangue e de apoiar a fera que abandonou Reinhold, prometendo eliminar os Wachter. Fiona não sabe quem é Reinhold, nem o restante da verdade. A caixa dos ossos em N4o é pista para H, **não conceda automaticamente o Tomo aqui**.

### Governo resultante

Guardas mantêm emprego/salário; doze seguidores viram auxiliares. Refugiados entram e ficam inicialmente na praça aguardando casas; vistanis também podem entrar. Udo é libertado e volta a Willemina. Família Vallakovich fica em prisão domiciliar informal, dois seguidores guardam frente/fundos; Victor se incomoda, mas não inicia guerra sozinho. Dependentes dos doces continuam com necessidade: Morgantha não volta desde a venda dos filhos de Franz, H.

Não introduza massacre/culto diabólico como punição automática por confiar em Fiona: esta revisão a desenvolve como aliada complexa. Relação com Strahd/Ernst causará dificuldades reais em S, resolvidas lá. Seus sentimentos mudam com Stella, farol e Espada Solar.

**Avanço:** marco coletivo para progresso de Vallaki; nesta conversão não somar 1.500 XP nem importar subida D&D ao nível 5 imediatamente. Coordenar com H/J e guia de níveis DH.

**Registro:** governo, prisioneiros/refugiados, recompensas, relações, data. D6 só se Fiona no poder e ossos restaurados; H e outras rotas ficam abertas.

**Origem:** Reloaded, Arco F, e áreas N2/N4/L do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "G1": """## Roteiro Completo · G1 · Izek invade a estalagem

**Objetivo:** Vivenciar o momento aterrorizante em que Izek Strazni invade a Estalagem Água Azul com seus guardas após avistar Ireena Kolyana pela janela, gerando um impasse tenso no salão comunal.

**Contexto & Segredo (DragnaCarta Lore):** Izek avistou Ireena da rua e entrou em choque absoluto: o rosto da mulher de seus sonhos de infância está vivo diante dele. Ele entra na taverna exigindo levá-la consigo para 'sua própria segurança', sem saber ainda que são irmãos de sangue separados no ataque dos lobos que arrancou seu braço quando crianças.

**Ambiente & Sensações:**
- *Visão:* A porta da estalagem escancarada com violência batendo contra a parede; seis guardas da cidade armados com lanças bloqueando a saída; Izek parado no vão da porta com o olhar fixo e alucinado cravado em Ireena.
- *Sons:* Copos caindo e quebrando no chão; clientes calando-se em pânico; o ranger pesado das botas blindadas de Izek; e a respiração ofegante do capitão em choque.
- *Cheiro:* Cerveja derramada, fumaça de cachimbos apagados e o odor metálico de ferro e chuva que entra pela porta aberta.
- *Tato:* O arrepio paralisante de dezenas de homens prendendo a respiração diante de uma tragédia iminente.

**Para narrar:** “A porta da Estalagem Água Azul é escancarada com um estrondo violento que faz as canecas tremerem sobre as mesas. Seis guardas armados com alabardas posicionam-se nos batentes com ordens de cercar o salão. E entre eles avança a silhueta colossal de Izek Strazni. O capitão ignora Urwin, ignora os clientes, ignora tudo ao redor: seus olhos arregalados e fixos estão cravados em Ireena Kolyana. Seu braço monstruoso fumega levemente sob a capa e seus lábios tremem como se visse um fantasma: 'Você... É você... O rosto dos meus sonhos... Você vem comigo agora!'”

### Visita à Água Azul, preferencialmente durante F2

Izek demanda busca de quartos. Urwin/Danika negam saber localização e ganham tempo no estábulo N2f. Se Ireena está ali, Brom/Bray a levam ao corredor/escada secretos N2i. No sótão dos corvos N2h, a abertura do baú permite desviar sua atenção; confisca economias dos Martikov como “impostos atrasados”. Para DH, registre uma reserva substancial perdida, não importação de 140 electrum/70 platina.

Frustrado, quebra mesa, duas cadeiras e janela e vai embora. Essa é a sequência se personagens estão ausentes; se presentes, suas intervenções podem prevenir/adaptar danos. Não destrua o quarto nem tome bens do grupo sem a ação ocorrer.

### Retorno

Estalagem fechada ao público, portas/venezianas fechadas, detritos recolhidos, corrente fria pela janela. Urwin varre, explica busca e lamenta quartos revirados; garante limpeza para dormir. Minimiza perda das economias e agradece que ninguém se feriu. Alerta que atacar Izek com guardas é perigoso; sugere Fiona e oferece investigar rotina por “amigos discretos”, sem revelar os Guardiões da Pena.

**Na manhã seguinte, informação de Urwin:** dois guardas de escolta, almoço na praça, dorme na mansão, bebe sozinho ao entardecer; empregado de Fiona o segue há semanas. Pode encaminhar a F sem presumir que aceitarão assassinato.

### Ireena reage e decide

Se escondida, Danika a acolhe na cozinha N2e com vinho quente; crianças foram ao quarto para segurança e ganharão brinquedos pela coragem. Ireena informa passagem secreta se necessário e pede sigilo. Se estava na igreja, vê estragos na manhã seguinte.

Ela sente culpa e indignação e **quer acompanhar** ação contra Izek. Não aceita ser tratada como porcelana ou propriedade: pai/irmão a treinaram. Conversa pode definir função segura e apoio; não retire sua agência com teste de persuasão. Se grupo tenta deixá-la enganada, Presença (CD 18) para mentira coerente; sair ocultamente, Finesse (CD 15), ambos com consequências de confiança. Em combate usa apoio limitado F4, sem turno extra de personagem completo.

**Registro:** quando foi vista, ataque, dinheiro/danos, posição e escolhas de Ireena, ajuda dos Martikov. G2 no dia seguinte à visita, salvo Izek removido.

**Origem:** Reloaded, Arco G, e áreas N2/N3 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "G2": """## Roteiro Completo · G2 · Cartazes pela cidade

**Objetivo:** Navegar pelas ruas de Vallaki sob estado de sítio após o confronto na taverna, evitar as patrulhas agressivas da guarda municipal e encontrar cartazes de recompensa com o retrato de Ireena espalhados pela cidade.

**Contexto & Segredo (DragnaCarta Lore):** Se Ireena fugir ou for escondida, Izek declara toque de recolher e espalha cartazes com o retrato dela desenhado pelo próprio Blinsky, oferecendo 100 PO por informações. O grupo precisa se mover pelas sombras para protegê-la.

**Ambiente & Sensações:**
- *Visão:* Ruas desertas sob chuva fina; cartazes de papel úmido pregados com pregos em postes e portas de lojas com o desenho de Ireena; patrulhas de quatro guardas com tochas e cães de caça farejando becos.
- *Sons:* Latidos furiosos de cães de guarda ecoando pelas esquinas; passos de botas pesadas correndo em rondas contínuas; e o sussurro tenso dos heróis escondidos em beirais.
- *Cheiro:* Chuva fria sobre lamaçal, tochas de alcatrão e o cheiro acre de cola de trigo dos cartazes.
- *Tato:* Paredes de pedra geladas onde o grupo se encosta nas sombras para escapar dos fachos de luz das tochas.

**Para narrar:** “Vallaki transformou-se em uma jaula sufocante. A mando de Izek, as ruas estão sob toque de recolher absoluto e a cada esquina há cartazes úmidos pregados nos postes exibindo o retrato fiel de Ireena com os dizeres: 'PROCURADA POR ORDEM DO BURGOMESTRE — 100 PEÇAS DE OURO'. O latido cavernoso de mastins farejadores e o clarão trêmulo de tochas forçam o grupo a rastejar por becos lamacentos e telhados de enxaimel para evitar a captura.”

**Registro:** cartazes, denúncias plausíveis, informantes, esconderijo/escolta, precauções e data. G3 só se ele tiver meios reais de encontrá-la e estiver vivo/livre.

**Origem:** Reloaded, Arco G, e áreas N2/N3 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "G3": """## Roteiro Completo · G3 · Sequestro

**Objetivo:** Descobrir o rapto súbito de Ireena por Izek através de uma emboscada traiçoeira nas ruas ou na estalagem, interrogar testemunhas e rastrear os passos do monstro até a Mansão do Burgomestre.

**Contexto & Segredo (DragnaCarta Lore):** Izek conseguiu emboscar a comitiva ou invadir o esconderijo, arrastando Ireena em direção à mansão do Barão. Urwin Martikov ou um dos caçadores viu a direção da fuga e alerta os heróis antes que seja tarde demais.

**Ambiente & Sensações:**
- *Visão:* Móveis virados e sinais de luta desesperada; a espada de Ireena caída na lama com o cabo quebrado; rastros pesados de botas afundando na direção da mansão do Barão.
- *Sons:* Urwin falando aos sussurros e com extrema urgência; o som da chuva batendo no chão; e trovões distantes rolando sobre o vale.
- *Cheiro:* Lama revolvida, sangue de um guarda ferido no confronto e chuva torrencial.
- *Tato:* O cabo gelado da espada de Ireena apanhada no chão como prova de seu rapto.

**Para narrar:** “O pior cenário concretizou-se: um rastro de destruição e sangue marca o beco onde Ireena foi subjugada. Sua adaga jaz abandonada na lama com a lâmina manchada de fuligem demoníaca, e pegadas pesadas e profundas seguem sem hesitação em direção aos portões de ferro da Mansão do Burgomestre. Urwin Martikov segura o ombro de vocês com urgência cortante: 'Izek a levou para a mansão! Ele a trancou em seus aposentos privados no andar de cima. Se vocês não entrarem agora, nunca mais a verão viva!'”

### Locais possíveis

**Estalagem:** aviso de um homem-corvo permite tentar o esconderijo novamente. Izek nota fio de cabelo na passagem apenas se a busca realmente puder encontrá-lo; cuidados novos podem evitar. Se vence resistência, prende Urwin nos troncos e tenta incendiar o prédio. Danika e seis Guardiões da Pena usam poço para apagar; danos estruturais seguem ação real, não destruição total inevitável.

**Igreja:** interrompe sermão, exige paradeiro, busca no escritório/quarto improvisado de Lucian e Yeska. Proteção contra mortos-vivos não impede sua entrada. Se leva Ireena, promete voltar para punir a igreja e sai sem outro ataque naquele momento. Personagens presentes, fuga planejada ou aviso podem impedir.

### Se capturada

Leva ao quarto **N3j** na mansão, amarra/amordaça na cama e fica ao lado com cadeira/vinho. Revela parentesco se ainda ignorado. Ao ver que ela escolhe família Kolyana e não aceita sua obsessão, acusa-a de ser uma impostora. Quer queimá-la para recuperar a irmã imaginada: doença/obsessão não concede razão ou posse sobre ela.

**Escalada do festival:** ao amanhecer do Festival do Sol Flamejante, troca ofertas dentro do sol de vime por Ireena presa. Escolta pessoalmente; estrutura chega à praça às 9h e seria queimada ao meio-dia. Esse é um prazo para resgate com pistas/avisos, **não morte decretada antes de jogarem**. Se não investigam mansão, permita testemunha observar troca/abafados pedidos de ajuda e abrir possibilidade na praça. Incêndio aplica perigo DH e chance de salvar, sem declarar morte por cair o ponteiro.

**Registro:** local/captura ou prevenção, orelha, danos, Urwin preso, Ireena em N3j ou sol de vime, horários. G4 imediato; D/H/F continuam sem pausar.

**Origem:** Reloaded, Arco G, e áreas N2/N3 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "G4": """## Roteiro Completo · G4 · Infiltrar ou atacar a mansão

**Objetivo:** Invadir ou infiltrar a Mansão do Burgomestre de Vallaki, lutar ou contornar as patrulhas de guardas, arrombar os aposentos privados de Izek Strazni, resgatar Ireena e desvendar a revelação bombástica de que Izek e Ireena são irmãos biológicos.

**Contexto & Segredo (DragnaCarta Lore):** Nos aposentos de Izek, o grupo encontra dezenas de bonecas idênticas a Ireena alinhadas em prateleiras (feitas por Blinsky). Ao confrontar Izek, Ireena reconhece a canção de ninar que ele murmura e a marca de nascença que ambos compartilham no ombro: Izek é o irmão mais velho que ela julgava morto quando os lobos atacaram sua caravana na infância e arrancaram o braço do garoto.

**Ambiente & Sensações:**
- *Visão:* Quarto de casal austero com paredes de madeira escura; prateleiras cobrindo três paredes repletas de dezenas de bonecas de porcelana de tamanhos diferentes, todas vestindo cópias dos trajes de Ireena; Ireena amarrada em uma poltrona, chorando em choque diante de Izek de joelhos.
- *Sons:* A respiração pesada e soluçante de Izek murmurando uma cantiga infantil antiga; o ranger de tábuas de assoalho; e o choro emocionado de Ireena ao reconhecer as palavras.
- *Cheiro:* Cera de vela, alfazema de bonecas, cinzas de lareira e o cheiro metálico de sangue e emoção contida.
- *Tato:* A madeira esculpida das bonecas e o contato comovente de duas mãos que se tocam através de anos de pesadelo e separação.

**Para narrar:** “Ao arrombarem a porta dos aposentos de Izek no segundo andar da mansão, o horror dá lugar a um choque avassalador. Três paredes inteiras estão cobertas de prateleiras onde descansam mais de quarenta bonecas de porcelana com o rosto idêntico ao de Ireena em todas as idades de sua vida. No centro do quarto, Ireena está sentada em uma poltrona de veludo com os olhos arregalados, enquanto o temível capitão — a besta que aterrorizava Vallaki — está de joelhos diante dela, soluçando como uma criança e cantando baixinho com voz rouca a mesma cantiga de ninar que Kolyan cantava na infância: 'Irmãzinha... Eu procurei por você nas brumas por toda a minha vida...'”

### Mansão, acesso e alarme

Use a planta N3 do mestre; jogadores veem apenas cômodos visitados. De dia: Vargas na biblioteca N3l com Fang/Claw; Lydia na sala de jantar N3c; Tereska na cozinha N3g; Clavdia no segundo andar pela manhã/primeiro à tarde. À noite Vargas/Lydia no quarto N3o, empregados em N3f. Victor permanece N3t.

Vargas solta cães e pede ajuda se derrotados; Lydia de dia acha que são convidados, de noite grita/desmaia; Victor conversa e não alarma com explicação razoável; Tereska manda sair e alarma se recusam; Clavdia alarma imediatamente. Doze guardas chegam cerca de dois minutos após grito. Não entram todos atacando em um foco: use grupo de lacaios Dificuldade 12, 1 PV cada, ataque +1/5 físico; quatro concentrados somam +2 físico por participante extra, nunca doze ataques gratuitos. Captura exige resultado real, não último PV convertido em prisão sem movimento de morte.

### Quarto N3j · oportunidade de resgate silencioso

Porta trancada: Finesse (CD 15) com ferramenta ou chave elimina risco. Se Izek acordado, também lidar com som/distração; um teste Finesse (CD 15) pode representar ambos quando mesmo plano, sem rolar redundâncias. No quarto, cama, coleção de bonecas e cadeira junto ao caminho. Izek nega acesso até a Vargas.

**Sono:** d20 de preparo, 15–20 dorme; à noite role dois e escolha maior. É sorte de cenário, não ação de PJ, sem gerar Esperança/Medo. Passar perto da cadeira provoca tentativa sonolenta de segurar pulso: Finesse (CD 10) extrai sem despertar. Libertar Ireena não exige rolagem com lâmina/acesso. Ao sair, tábua range e murmura “Ireena”; entregar uma boneca mantém sono. Sem solução, desperta no próximo foco do mestre, dando escolha ao grupo.

**Distração criativa:** pode tirá-lo do quarto com situação forte/provocadora; Presença (CD 18) quando resistência social genuína, não “impossível porque roteiro”. Ataque espalhafatoso no primeiro piso o faz sair de machado, criando acesso para segundo grupo.

### Se houver luta

Use **as duas formas e todas as capacidades DH de F4**, uma única instância de Izek, mesmo veneno e orelha se aplicáveis. Referência: [[F4 · Acompanhar e emboscar Izek]]. Não reimporte iniciativa, surpresa D&D ou três reações por rodada. Ele pode gastar foco para atravessar parede interna de madeira, marcando 1 Estresse e sofrendo 1d6 físico, sem ataque adicional; abre rota nova tanto para si quanto para os jogadores.

Ireena, consciente, corta cordas com adaga na bota no primeiro momento seguro, passa a colaborar no próximo foco do grupo. Apoio uma vez por cena como F4. Não é alvo passivo obrigatório de dano de área que poderia evitar.

### Incêndio DH autoral · por zonas, não quadrados

Fogo atingindo painel/assoalho inflamável cria uma zona Muito Próxima. **Uma vez após todos os personagens terem tido oportunidade de agir**, foco do mestre expande para uma zona adjacente; anunciar fumaça antes de expansão. Quem está na zona faz reação Finesse (CD 10): sucesso sai para apoio adjacente; falha sofre 1d8 mágico e pode sair no próprio foco. Não cobrar dano por toda troca de spotlight. Fumaça em zona adjacente: reação Força (CD 10) ao agir ali, falha desvantagem no próximo teste por tosse; mortos-vivos/construtos não sofrem tosse. Balde/água/extintor apropriado e ação reduzem uma zona. Madeira em chamas pode bloquear rota, mas janela/parede rompida oferecem alternativas.

Após aproximadamente um minuto, se livre/consciente, Victor chega, manda todos recuarem e usa sua conjuração de frio para apagar as zonas visíveis; não causa dano inevitável aos aliados. Se impediram-no/está ausente, não aparece por teleporte. Os PJ têm chances de evacuar antes desse evento.

### Resultados e consequências políticas

Ireena agradece e lamenta a criança que Izek foi, sem lamentar seu comportamento adulto. **Escolhe continuar Ireena Kolyana**, não “Strazni” imposta nem qualquer outra identidade decidida pelo mestre.

Se Izek morre, saque como F4: machado de prata, pequena bolsa e fragmento Seriach. Na manhã seguinte, se F não foi aceito, Ernst convida para chá com Fiona; se recusam, ela vem à estalagem à noite de capa azul escura, pede conversa particular. Parabeniza pela libertação, pede apoio para buscar governo e explica que é administração local, não poder absoluto. Pode seguir F5 após transição realmente acordada; recompensas não duplicam.

**Avanço:** resgate seguro é marco coletivo; derrotar Izek/F/G é um mesmo objetivo compartilhado, não duas subidas de nível nem 750/1.500 XP. Se ele sobrevive, registre prisão/fuga e proteção de Ireena: não reinicie sequestro automaticamente.

**Registro:** sobreviventes, resgate, confiança de Ireena, fogo/estrutura, Urwin, guardas, destino de Izek e novo governo. Próximos H/J/D6 conforme estado.

**Origem:** Reloaded, Arco G, e áreas N2/N3 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H1": """## Roteiro Completo · H1 · Erasmus pede ajuda

**Objetivo:** Testemunhar a manifestação espectral comovente do fantasma de Erasmus van Richten (o filho assassinado de Rudolph van Richten) na Igreja de Santo Andral, ouvir seu apelo por libertação e descobrir a conexão com a Mansão do Barão.

**Contexto & Segredo (DragnaCarta Lore):** Erasmus foi transformado em cria de vampiro séculos atrás e executado pelo próprio pai Van Richten por misericórdia. Sua alma vaga presa em Baróvia e reside no espelho espiritual na mansão do Barão. Ele pede que os heróis o libertem do ciclo eterno de tormento.

**Ambiente & Sensações:**
- *Visão:* Uma aparição etérea de luz azul-celeste tomando a forma de um jovem elfo/humano de rosto angelical e olhos tristes flutuando acima dos bancos da igreja vazia.
- *Sons:* Um sussurro melódico e gelado que ressoa diretamente dentro das mentes dos personagens; o estalar de gelo que se forma nos vitrais ao redor do fantasma.
- *Cheiro:* Frio de altitude, ozônio puro e flores de lírio secas em sepultura.
- *Tato:* Uma rajada de ar congelante que faz a pele arrepiar e a respiração condensar em fumaça branca.

**Para narrar:** “No silêncio solene da capela após o cair da noite, as chamas das velas tremulam e adquirem um tom azul-safira sobrenatural. Flutuando a poucos centímetros do chão de pedra, surge a silhueta translúcida e luminosa de um jovem de cabelos claros e olhar repleto de dor ancestral: Erasmus. Sua voz ecoa suave como a brisa de inverno: 'Viajantes da luz... Meu pai ainda vaga por esta terra consumido pelo ódio e pela culpa de ter tirado a minha vida. Minha alma está aprisionada em um espelho no casarão dos governantes. Por favor... libertem-me das correntes do reflexo para que eu possa encontrar a paz eterna.'”

**Registro:** pedido aceito/recusado, nome conhecido, data. H2.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H2": """## Roteiro Completo · H2 · Victor e o espelho espiritual

**Objetivo:** Subir ao sótão secreto da Mansão do Burgomestre, confrontar o jovem aprendiz de mago Victor Vallakovich em seu laboratório, investigar o Espelho Espiritual no guarda-roupa e negociar o ritual para libertar a alma de Erasmus.

**Contexto & Segredo (DragnaCarta Lore):** Victor é arrogante, brilhante e amargurado. Ele descobriu um espelho mágico que aprisiona almas e pode conjurar assassinos espectrais se comandado. Victor possui o Tomo de Strahd em seu baú de pergaminhos, mas só o entrega se os heróis o ajudarem a consertar sua rota de fuga ou libertarem o fantasma.

**Ambiente & Sensações:**
- *Visão:* Sótão amplo iluminado por globos de luz mágica arroxeada; bancadas com tubos de ensaio, crânios de gato e grimórios abertos; o círculo de teletransporte no chão com marcas de corpos queimados; e um grande espelho oval com moldura de prata oxidada coberto por veludo negro.
- *Sons:* O zumbido vibrante de energia mágica no ar; o miado fantasmagórico de esqueletos de gatos animados; e a voz cínica e irritada de Victor segurando sua varinha de teixo.
- *Cheiro:* Ozônio queimado, enxofre, cera de vela de breu e folhas secas de pergaminho antigo.
- *Tato:* Cabelos e pelos do braço eriçando devido à estática mágica que pulsa do espelho espiritual.

**Para narrar:** “O sótão da mansão de Vargas é o santuário sombrio de um gênio perturbado. Sob vigas de carvalho centenárias, bancadas de alquimia com frascos borbulhantes e livros encadernados em couro cercam um círculo arcano desenhado com giz de prata e sangue no assoalho. No canto mais escuro, um grande espelho oval de moldura prateada entalhada com almas agonizantes pulsa com um fulgor espectral sob uma cortina de veludo negro. Victor Vallakovich, um jovem pálido de olheiras fundas e sobretudo manchado de reagentes, aponta sua varinha para vocês: 'Mais espiões de meu pai? Ou vocês têm intelecto suficiente para compreender que este vale é uma sepultura da qual eu pretendo escapar?'”

**Oficina N3t, mansão:** acesso automático com elogio suficiente a Vargas ou Fiona já governando; caso haja resistência, Presença (CD 10) com propósito/história plausível. O acordo de E3 também pode valer. Victor protesta que tinha controle, olha espelho e admite precisar de ajuda.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H3": """## Roteiro Completo · H3 · Refugiados e Franz

**Objetivo:** Visitar o acampamento de refugiados do lado de fora dos muros de Vallaki, ouvir o relato emocionante de Franz e dos camponeses sobreviventes da Vila de Baróvia e compreender o alcance das tortas de sonho das bruxas.

**Contexto & Segredo (DragnaCarta Lore):** Os refugiados sofrem de abstinência das Tortas de Sonho de Morgantha. Franz, um camponês que vendeu o próprio filho por uma torta, chora em delírio e revela os segredos do Velho Moedor de Ossos e os nomes das três bruxas.

**Ambiente & Sensações:**
- *Visão:* Tendas de lona podre e carroças quebradas na lama lamacenta; fogueiras fracas soltando fumaça cinzenta; homens e mulheres tremendo em abstinência com olhares alucinados; Franz amarrado a um poste para não arranhar a própria pele.
- *Sons:* Tosse rouca, gemidos de delírio de camponeses viciados em tortas; o murmúrio de mães chorando filhos perdidos; e o estalar de gravetos úmidos no fogo.
- *Cheiro:* Fumaça de turfa, lama fétida, suor frio e o cheiro doce e enjoativo de açúcar queimado que ainda emana dos trapos dos viciados.
- *Tato:* O aperto trêmulo e febril das mãos de Franz suplicando por perdão e redenção.

**Para narrar:** “Do lado de fora dos muros imponentes de Vallaki, o campo de refugiados é um retrato cru da decadência baroviana. Sob tendas esfarrapadas que mal barram o vento gélido, dezenas de homens e mulheres tremem em delírio febril. Amarrado a um esteio de madeira para não dilacerar os próprios braços em desespero, o camponês Franz chora copiosamente: 'As tortas... Elas tiravam a dor... Mas o preço foram os ossos do meu menininho! A velha Morgantha e suas filhas Bella e Offalia moem as crianças no moinho da colina! Se vocês souberem seus nomes verdadeiros, a magia delas quebra!'”

**Local variável:** até seis horas após posse de Fiona, tendas fora do portão leste; depois, praça de Vallaki enquanto buscam moradia. Revele o mapa de jogadores correspondente, não mantenha dois acampamentos simultâneos. Barracas rasgadas, valas/barricadas, fogueiras pequenas e gente exausta.

**Emeric e Magda:** organizadores informais, cautelosos e preocupados. Primeiro grupo chegou há três meses, expulso por fogo de Izek; subornaram guardas por tendas/necessidades, mas não por entrada. Lobos/morcegos ferem à noite; medo/perdas impedem retorno à vila. Um quarto depende de doces de Morgantha, que não voltou nos últimos dias. Descrição da bruxa lembra pesadelos de Franz.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H4": """## Roteiro Completo · H4 · As duas rotas de Victor

**Objetivo:** Decidir o destino de Victor Vallakovich: convencê-lo a usar seus talentos para o bem da cidade e entregar suas anotações arcanas, ou neutralizá-lo para impedir mais acidentes fatais no sótão.

**Contexto & Segredo (DragnaCarta Lore):** Victor tem duas rotas: se confrontado com empatia e diplomacia por um conjurador (*Presença CD 13*), ele percebe que seus feitiços de teletransporte estavam matando inocentes devido à barreira das brumas de Baróvia e aceita ajudar a decifrar rituais; caso contrário, luta ferozmente para defender seus livros.

**Ambiente & Sensações:**
- *Visão:* Victor abaixando a varinha com lágrimas de frustração nos olhos; grimórios antigos espalhados sobre a mesa; o Tomo de Strahd repousando sob uma pilha de manuscritos astronômicos.
- *Sons:* A respiração trêmula do jovem aceitando a verdade sobre as brumas; o farfalhar de folhas de pergaminho; e o silêncio que se instala no sótão.
- *Cheiro:* Tinta nanquim fresca, chá de camomila frio e poeira.
- *Tato:* O peso secular e a textura de couro humano da capa do Tomo de Strahd ao ser retirado do baú.

**Para narrar:** “A fúria arrogante de Victor desfaz-se quando as falhas de seus cálculos arcanos são expostas: as brumas de Baróvia não podem ser rompidas por teletransporte comum — qualquer um que cruze o círculo é rasgado entre as dimensões. O rapaz desaba em uma cadeira de mogno, cobrindo o rosto com as mãos: 'Eu só queria sair daqui... Este vale sufoca tudo que é belo.' Em troca de ajuda para escapar de forma segura quando Strahd cair, ele abre seu baú de ferro e retira um pesado volume encadernado em couro negro: o lendário Tomo de Strahd.”

### Duas rotas reais

**Negociar:** bruxa empresta coração por promessa de grande valor; honra a letra, não intenção. Sem Fiona podem usar essa rota; termos H7. Conseguir pedra não obriga entregar crianças ou vender doces.

**Tomar à força:** antes é necessário impedir fuga etérea. Um coven de três se fortalece; qualquer bruxa não nomeada pode atravessar e atacar ritualistas. Prata favorece enfrentar suas defesas. Iniciar combate sem prisão pode levá-las a fugir, não garante morte da equipe.

### Mó e círculo

Ao ouvir Franz, Victor identifica pedra preta como coração pessoal da bruxa, mas “coração do moinho” indica outro objeto. Na biblioteca encontra registro de Boris cedendo terra a Gustav/Elisabeth Durst e **planta da mó com compartimento lateral**. Mostre croqui para jogadores; não inclua contrato/tesouro/posição dos guardas num handout arquitetônico. A chave no braço retorcido é pista para acesso.

Grimório ilustra círculo de contenção sem instruções; pesquisa de Victor falha em reproduzi-lo. Stella gesticula que viu um gigante em torno de Wachterhaus, bloqueando sua entrada. Victor protesta por desconfiança das famílias; pode mudar diante da urgência. Ela recomenda pedir ajuda à mãe e baixar barreira para demonstrar sua presença.

**Pré-condições para ataque:** Fiona + quatro ritualistas, nomes verdadeiros **dos três**, crianças fora do risco, Victor em condição de impedir dissipação. Um relógio genérico de ritual não substitui esses requisitos. Grupo pode inventar outra contenção se uma capacidade realmente a permite; diga alcance/duração/risco em vez de conceder automaticamente prisão planar porque alguém desenhou giz.

**Registro:** rota escolhida, planta/pista, recursos de prata, pesquisa, data de saída. H5 ou H6/H7 pela negociação.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H5": """## Roteiro Completo · H5 · Conseguir a ajuda de Fiona

**Objetivo:** Consultar Lady Fiona Wachter em Wachterhaus sobre o ritual lunar de cura mental para sua filha Stella Wachter (que acredita ser um gato devido a um trauma causado por Victor).

**Contexto & Segredo (DragnaCarta Lore):** Stella enlouqueceu após Victor testar nela feitiços de sugestão e crueldade emocional. Fiona mantém a filha trancada em um quarto forrado com trapos, alimentando-a com leite e peixe cru. Fiona revela que um ritual com a flor do luar e a derrota das bruxas pode restaurar a mente da garota.

**Ambiente & Sensações:**
- *Visão:* Quarto acolchoado com colchões velhos e cheiro de animais; Stella encolhida no topo de um guarda-roupa, miando e sibilando com unhas afiadas; Lady Fiona com os olhos marejados de sofrimento materno genuíno.
- *Sons:* Miados assustados e rosnados felinos vindos da jovem; o fechar suave da porta trancada a chave; e a voz embargada de Fiona pedindo socorro.
- *Cheiro:* Leite azedo, peixe cru, serragem e o perfume triste de rosas murchas no vaso.
- *Tato:* As unhas compridas de Stella arranhando quem tentar pegá-la à força.

**Para narrar:** “Atrás de uma porta trancada nos aposentos superiores de Wachterhaus, a fachada aristocrática de Lady Fiona quebra-se completamente. O quarto está forrado de palha e trapos limpos, e no alto de um armário alto, encolhida como um felino selvagem com olhos arregalados e cabelos desgrenhados, está a jovem Stella Wachter. Ao ver os estranhos, a moça sibilha e solta um miado estridente de pânico. Fiona fecha os punhos contra o peito em desespero: 'Victor quebrou a mente da minha menina... Tragam a essência da pedra sagrada do moinho sob a luz da lua cheia, e eu prometo a vocês a gratidão perpétua de toda a minha linhagem!'”

### Acordo e recursos

Leva até quatro horas para reunir **Andrej, Boris, Miruna e Ruxandra**; cinco posições incluindo Fiona cercarão colina do moinho. Nomes verdadeiros são indispensáveis para modo “manter dentro”; círculo pode também “manter fora”, mas um modo não serve ao outro automaticamente. Uma bruxa livre pode sabotar. Fiona insiste em tirar crianças antes da ofensiva e marca encontro no portão leste.

**Segredo histórico para o mestre:** Leo Dilisnya, assassino Ba’al Verzi, vingava Reinhold, irmão sacrificado por Strahd numa batalha. Tentou matar conde na manhã do casamento; depois comandou motim e morte dos Wachter leais. Strahd tornou-o cria e sepultou-o sob Wachterhaus por quatrocentos anos; amuleto rubi podia matá-lo. Fiona, adolescente, quebrou-o sem saber e libertou espírito. Leo voltou unido a guardas mortos, assombrou família. Frederich buscou auxílio em Berez; Fiona, ressentida, mentiu que Lysa não podia ajudar. Uma sessão espírita abriu passagem e Leo matou Balthazar, Lavinia e Frederich. Fiona regressou culpada e fez barreira renovada anualmente; **não conhece toda a identidade de Leo neste momento**. Revelar em H8, conforme provas, em vez de recitar segredo à chegada.

**Registro:** confiança/prova, círculo baixado/restaurado, ritualistas prontos, plano, horário. H6.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H6": """## Roteiro Completo · H6 · Viagem ao moinho

**Objetivo:** Marcha armada de volta à colina do Velho Moedor de Ossos sob céu de tempestade, munidos com os nomes verdadeiros das três bruxas da noite e preparados para o resgate dos órfãos.

**Contexto & Segredo (DragnaCarta Lore):** A jornada até o moinho é decidida: sabendo os nomes verdadeiros de Morgantha, Bella e Offalia, os heróis têm uma arma mágica poderosa que pode quebrar a ligação do coven de bruxas da noite (*Night Hag Coven*).

**Ambiente & Sensações:**
- *Visão:* Céu tempestuoso de outono com nuvens arroxeadas; as pás do moinho girando ferozmente contra o vento forte; a fumaça doce de baunilha e canela subindo com intensidade sinistra da chaminé.
- *Sons:* O gemido ensurdecedor das pás do moinho sob vendaval; trovões que sacodem o chão; e o grasnar agudo de corvos nos monólitos avisando que o combate começou.
- *Cheiro:* Açúcar queimado, gordura rançosa, ozônio elétrico e o cheiro metálico de sangue que escapa das frestas do moinho.
- *Tato:* Chuva gelada chicoteando armaduras e rostos ao subir a colina gramada em direção ao moinho.

**Para narrar:** “A colina do Velho Moedor de Ossos ergue-se contra o horizonte de tempestade como um monumento de pesadelo. Sob relâmpagos violetas que cortam as nuvens pesadas, as pás de madeira carcomida do moinho giram com violência inusitada, rangendo como os dentes de um titã carnívoro. O aroma de tortas doces não mais ilude: agora ele fede a cinzas, sangue infantil e magia negra ancestral. Com as armas em punho e os nomes sagrados na memória, vocês cruzam a cerca em direção à batalha decisiva.”

### Druida a meio caminho

Figura magra de peles, descalça, marcas vermelhas no rosto, numa árvore, chama-os de passarinhos. É observador de Yester Hill/Strahd; provoca, **não pretende ataque**. Fiona exige passagem, fala em sua identidade/sinal; ele reconhece “filha da Mãe Noite”, ironiza dívidas. Ela manda informar mestre que Wachter lembra obrigações; ele some.

Se questionada, explica origem do povo da floresta, adoração de Strahd pelo domínio de terra/clima, aprendiz de Lysa em Berez, incapacidade de ouvir Mãe Noite e adoção de Ezra. Saída foi considerada traição pela mentora; está banida. Dívida familiar a Strahd é Lovina protegida contra Leo. Não revele que Ezra mascara Poderes Sombrios como se Fiona soubesse.

**Intervenção:** negociar, seguir, confrontar ou ignorar altera o encontro; não force dano. Se tentam agarrar druida, Finesse/Instinto (CD 15) conforme posição para alcançar; ele foge pelos galhos e poderá levar relato a Strahd. Não inclui emboscada extra obrigatória.

**Registro:** quem foi visto/relatado, passado de Fiona, viagem, desgastes. H7.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H7": """## Roteiro Completo · H7 · Moinho: nomes verdadeiros, crianças e pedra

**Objetivo:** Confrontar as três bruxas da noite (Morgantha, Bella e Offalia) no interior do Velho Moedor de Ossos, invocar seus nomes verdadeiros para desmantelar o coven, salvar as crianças Freek e Myrtle e reconquistar o monólito corrompido.

**Contexto & Segredo (DragnaCarta Lore):** O combate no moinho é vertical e claustrofóbico através de quatro andares de escadas estreitas. Invocar os nomes verdadeiros das bruxas reduz sua CA e impõe vulnerabilidade a dano psíquico/radiante. As crianças Freek e Myrtle estão presas em caixotes no sótão prestes a serem atiradas no funil do moedor.

**Ambiente & Sensações:**
- *Visão:* O caldeirão fervente no térreo transbordando calda pegajosa; mó de pedra gigantesca moendo ossos humanos no segundo andar; caixotes com crianças chorando no terceiro andar; e as três bruxas com pele púrpura e chifres retorcidos revelando suas verdadeiras formas monstruosas.
- *Sons:* Gargalhadas histéricas e estridentes das três irmãs bruxas; o ranger colossal da pedra da mó triturando ossos; choros agudos de Freek e Myrtle; e o cantar de feitiços arcanos estalando em chamas.
- *Cheiro:* Farinha de ossos suspensa no ar sufocando a respiração, manteiga rançosa, carne crua e o fedor de covil infernal.
- *Tato:* O pó fino de ossos cobrindo rostos e mãos e o calor asfixiante do forno aceso.

**Para narrar:** “Ao ser chutada a porta do moinho, os disfarces de camponesas bondosas rasgam-se em uma transformação monstruosa: a velha Morgantha e suas filhas Bella e Offalia revelam sua verdadeira natureza de bruxas da noite, com pele púrpura coriácea, olhos amarelos de cabra e chifres retorcidos gotejando icor negro! No andar de cima, sobre a mó de pedra que gira triturando ossos com estalos horríveis, os pequenos Freek e Myrtle gritam por socorro de dentro de caixotes amarrados: 'Socorro! Elas vão nos jogar no forno!' Mas ao pronunciarem os nomes verdadeiros das megeras, as paredes do moinho estremecem e as bruxas uivam em agonia sobrenatural!”

### Planta e conteúdo, andar por andar

**O1, térreo/cozinha:** forno com doces, carrinho, louça/ervas/farinha de ossos, armário com mechas de cabelo, galinhas, baú com cem sapos e barril de icor demoníaco. Morgantha verifica forno regularmente. Elixires: “Juventude” muda aparência por 24h; “Riso” transmite febre de gargalhadas; “Leite da Mãe” é veneno debilitante, não cura. Examinar com Conhecimento (CD 15) identifica risco, sem necessidade de provar. Barril permite observação mágica e invocar até nove demônios pequenos, um por foco dedicado; não aparecem nove com ataques extras no mesmo instante.

**O2, mó:** Morgantha trabalha aqui salvo distraída. Um braço mais retorcido é segmentado: girar a ponta destaca-a e revela chave de ferro. Compartimento lateral abre com chave sem teste ou Finesse (CD 15)/ferramentas. Contém contrato, joias e **amuleto de heroísmo coletivo**; tesouro original retirado de O3 para cá. O contrato em Abissal tem nomes **Morgantha Stormreaver, Belladonna Sunbane, Offalia Wormwiggle**. Fiona lê se ninguém souber. Conhecimento (CD 20) identifica que apenas **garras das próprias bruxas** podem rasgá-lo. Se destruído por meio correto, encerra coven, não mata bruxas nem devolve alma automaticamente.

**O3, quarto:** Bella/Offalia, cama mofada, eixo, roupas infantis e armário com três caixas; uma vazia, outras contêm crianças, escada para sótão. Não conhecem Ireena/Ismark. **O4, sótão:** cúpula/eixo, lugar de aprisionamento após derrota. Guarda/tesouro só conforme estado real.

**Amuleto DH autoral:** ação única, aliados Próximos recuperam 1 Estresse e ganham vantagem no próximo teste contra medo/magia das bruxas durante a cena; depois desaparece. Não gera PV temporários D&D ou bênção permanente.

### Plano e ajuda limitada

Fiona/seguidores esperam no bosque. Majesto pode explorar invisível como corvo/aranha/rato e transmitir o que observou, sem detectar automaticamente contrato oculto. Victor tem recursos de voo/ocultação breve para **uma manobra de resgate**; exigir acesso real e avisar se a ajuda o deixa exposto. Reserva sua abjuração principal para proteger círculo, sem slots DH inventados.

**Distrair:** história de compradores de doces, Presença (CD 10); outra cobertura coerente, Presença (CD 18). Morgantha convida a esperar fornada. Chamar filhas para cozinha, Presença (CD 18); elas são menos cautelosas e seguem entretenimento plausível, Presença (CD 15). Relato verdadeiro de sonho com doce acalma sem teste; mentira, Presença (CD 18). Falha deixa-a desconfiada, solicita retorno amanhã, ou chama filhas para “provar fornada” ainda crua. Bella obstrui porta fingindo examinar dobradiça antes de ataque; dê oportunidade de reconhecer cerco/retirar.

### Círculo, dez minutos de oportunidade

Após obter **três nomes e resgatar crianças**, Fiona/seguidores formam cinco pontos na base. Conjuração abrange colina e altura de cerca de cento e cinquenta metros; dura dez minutos. Nomeadas não cruzam ao Etéreo. Se um ritualista perde consciência/posição ou abandona canto, termina. Não cobre Strahd/Bucephalus por reutilizar nomes de bruxas.

**Confronto:** bruxas saem à porta, parabenizam “resgate” e pedem crianças em troca da pedra. Pode haver sapos liberados pelo desaparecimento dos cativos. O grupo pode recusar, negociar garantias ou atacar. Não force entrega porque uma figura alegou “almas já condenadas pela Névoa”.

### Coven DH autoral · uma ficha compartilhada, duas formas

**Patamar 2, Solo**, nível recomendado DH 4. Três corpos com posição/estados próprios, **um conjunto compartilhado de PV/Estresse**. Cada foco escolhe **uma bruxa e uma capacidade**; não três ações + bônus + lair gratuitos. Um efeito de área acertando várias marca PV **uma vez**, usando maior dano aplicável, para evitar multiplicação explosiva de dano DH. Condição de uma não afeta automaticamente irmãs. Se uma sai do círculo, poderá fugir; vínculo persiste a até uma milha, mas sem criar corpo duplicado.

**Forma I, Coven:** Dificuldade 16, limiares 13/24, PV 7, Estresse 6, ataque +3; garras 2d8+3 físico. Prata impede reação defensiva contra aquele ataque. **Resistência arcana:** uma vez por cena, 1 Estresse dá vantagem à reação contra magia; não redução universal de dano.

**Bella:** cegueira/surdez, foco/1 Estresse, reação Força (CD 16), falha 1d8 mágico e desvantagem no próximo teste da percepção escolhida, sucesso metade sem penalidade; radiância pútrida, foco/1 Estresse, área Muito Próxima/alcance Próximo, mesma reação, falha 2d6 mágico e desvantagem no próximo teste físico; coroa de loucura, foco/1 Estresse, reação Instinto (CD 16), falha 1d8 mágico e escolha recuar Muito Próximo ou marcar 1 Estresse para permanecer — não ataque compulsório a aliado; força fantasmagórica, mesmos custo/reação, ilusão assustadora dá desvantagem no próximo teste para atravessar/ignorar cenário falso, desaparece ao investigar com ação.

**Offalia:** raio de enfraquecimento, ataque normal 2d6+2 mágico e troca +2 por desvantagem no próximo teste de Força; flecha ácida, ataque 2d6+2 mágico, alvo escolhe ação para limpar ou marca 1 Estresse no próximo foco e ácido acaba; causar medo, foco/1 Estresse, até dois Próximos reação Instinto (CD 16), falha 1 Estresse e desvantagem no próximo teste para se aproximar dela; maldição, foco/1 Estresse, reação Presença (CD 16), falha 1d8 mágico e desvantagem no próximo teste de traço escolhido, sucesso metade sem estado.

**Morgantha:** raio de doença, ataque 2d6+2 mágico, troca +2 por desvantagem no próximo teste físico; podridão, foco/1 Estresse, reação Força (CD 16), falha 2d8 mágico/sucesso metade; prender pessoa, foco/2 Estresse, até dois Próximos reação Força (CD 16) ou Restrito até ação Força/Finesse (CD 16)/ajuda; raio elétrico, foco/2 Estresse, linha Próxima, reação Finesse (CD 16), falha 3d8 mágico/sucesso metade, **uma vez nesta forma**.

**Defesas alternativas, no máximo uma após o mesmo ataque:** Bella, 1 Medo/1 Estresse, duplicatas impõem desvantagem antes de rolar ataque; Offalia, 1 Medo/1 Estresse, atacante reage Instinto (CD 16) ou perde próximo movimento para conter riso, sem incapacitação completa; Morgantha, 1 Medo/1 Estresse, reação Força (CD 16) evita vínculo, falha marca 1 Estresse, e próximo dano à bruxa marca 1 Estresse no alvo antes de vínculo cessar; qualquer bruxa, 1 Medo/1 Estresse, desloca Muito Próximo após dano, sem ataque. Sem “chance 4/6 de anular golpe” aplicada retroativamente a tudo.

**Em 0 PV:** transformam — Bella crocodilo enorme, Offalia elefante demoníaco, Morgantha sombra negra. Forma II, **Três Pesadelos:** mesmos Dificuldade/limiares, PV 6 novos, Estresse 5 novos, ataque +3; mantém posições/estados plausíveis, dissipando ilusões sustentadas, sem ataque gratuito.

**Bella:** mordida 2d8+4 físico, pode substituir +4 por Restrito de uma presa (Força/Finesse (CD 16) libera); cauda 2d8+3 físico e pode substituir +3 por empurrão Muito Próximo; varredura foco/1 Estresse, Muito Próximos reação Finesse (CD 16), falha 2d6+3 físico/Vulnerável até firmar-se com ação, sucesso metade; névoa alucinante foco/1 Estresse, cone Próximo, reação Instinto (CD 16), falha desvantagem no próximo teste e escolhe mover ou agir nesse foco, não ambos.

**Offalia:** presas 2d8+4 físico; investida em linha desobstruída desde Próximo acrescenta 1d6 e empurra Muito Próximo, custa 1 Estresse; pisoteio foco/1 Estresse, área Muito Próxima reação Finesse (CD 16), falha 2d8 físico/sucesso metade; trombeta foco/1 Estresse, ouvintes Próximos reação Instinto (CD 16), falha desvantagem no próximo teste.

**Morgantha:** olhar de pesadelo foco/1 Estresse, reação Instinto (CD 16), falha impede próximo movimento e marca 1 Estresse, sucesso desvantagem no próximo teste contra ela; anel extenuante foco/1 Estresse, Muito Próximos reação Força (CD 16), falha 2d6 mágico e Vulnerável até agir, sucesso metade; impor pesadelo foco/2 Estresse, reação Instinto (CD 16), falha alvo escolhe ação para despertar ou 1 Estresse e agir com desvantagem; ajuda de aliado elimina efeito.

**Reações da forma II:** Bella/Offalia podem 1 Medo/1 Estresse após feridas mover/ameaçar atacante, mas ataque só em novo foco normal; Morgantha 1 Medo/1 Estresse reduz em 1 PV o dano marcado e desloca Muito Próximo, ou repreende com reação Finesse (CD 16)/1d8 mágico na falha. Absorver elemento: 1 Estresse reduz em 1 PV um dano elemental, uma vez por cena para coven. Não empilhe três retaliações no mesmo ataque.

**Ambiente, uma opção por foco de mestre dedicado:** vento protetor dá desvantagem no próximo ataque de projétil atravessando zona; rajada reação Força (CD 16) empurra Muito Próximo; coro dos sapos reação Presença (CD 10), falha escolhe mover Muito Próximo rumo ao moinho ou 1 Estresse para resistir; dissipar círculo **uma vez no dia**, anunciado antes. Cada opção substitui ataque, não iniciativa 20 extra.

**Victor:** protegido e a alcance Próximo do moinho, impede automaticamente **a única dissipação** se reservou abjuração e está capaz. Pode uma vez por cena ajudar defesa dando vantagem a reação contra raio/olhar; isso não consome reserva, mas requer posição segura. Majesto pode uma vez interromper capacidade sustentada após teste Finesse (CD 16), sem dano adicional gratuito. Ritualistas não atacam enquanto sustentam.

**Escape/ajuste:** quando forma II chega à metade PV, Morgantha tenta fuga etérea e descobre bloqueio; no próximo foco dedicado tentam dissipar. Se Victor foi incapacitado/ausente, círculo cai e cada bruxa precisa de foco para fugir. Três PJ usam PV 5/4, bônus fixos −2; quatro valores base; cinco +1 PV em cada forma; seis +2. Não somar três Solos. Combate ainda é difícil, com fuga/negociação possíveis; porcentagem de desgaste D&D não foi validada aqui.

### Trégua e negócio alternativo

Após dissipação impedida, Morgantha oferece três segredos por liberdade: templo de âmbar foi lugar do pacto de Strahd; ele quer escapar da Névoa usando três santuários antigos, um nos megálitos do moinho; **Sasha Ivliskova**, esposa mais antiga, é traidora oculta. Não conhece rota do templo/detalhes do plano. Ameaça convincente faz contar um segredo de boa-fé; Presença (CD 10) pode exigir coração de Bella antes de baixar círculo. Se recusada, luta até fim; se cumprida, registrar compromissos, não revogar arbitrariamente.

**Negociar sem atacar:** coração emprestado por **três dias**; tarefa em **quatorze dias**: instalar sanguessuga de alma sob mesa de Rahadin em seu escritório subterrâneo de Ravenloft, perto das cozinhas (K72 na planta do mestre). Fica invisível, prende alma dele **quando morrer**, não o mata imediatamente. Presença (CD 10) faz Morgantha explicar finalidade. Fonte de informação é Cyrus, portador involuntário do olho de bruxa; segredo.

**Garantia:** sonhos consentidos ficam em frasco no pescoço. Descansos continuam normais até prazo, mas violar acordo/não devolver pedra em três dias permite devorá-los antes; tarefa não concluída em quatorze permite perda. A regra DH autoral após perda: descanso longo só concede benefícios de curto até recuperar sonhos/desfazer pacto; não elimine para sempre personagem sem rota de recuperação. Destruir/recuperar frasco intacto e libertar sonhos remove garantia; matar portadora encerra vínculo. Dê termos claros antes da escolha; não imponha pacto a quem não aceitou.

### Derrota, cativeiro e fuga

Não substituir movimentos de morte DH por captura automática. Se capturados vivos/rendidos, acordam após 1d4+1 horas em O4, mãos/pernas presas e amordaçados; itens em caixa O3, seis dretches. Um exposto a “Riso”, outro a veneno. **Febre DH:** ao sofrer pressão/dor, reação Força (CD 15) ou 1 Estresse e risos, denunciando presença; contágio só após contato prolongado próximo, reação Força (CD 10), nunca transmissão inevitável a todos por repetidos cortes sem chance de agir. Coração de bruxa cura doença por ação de contato; magia explicitamente capaz de curar doença/Abade também. Recuperação natural exige três descansos longos com cuidado e reação Força (CD 15) bem-sucedida; falha adia, não eleva DC sem fim. **Veneno DH:** desvantagem física por cena, cuidados/antitoxina encerra; não copie exaustão letal D&D.

Morgantha interroga e ameaça crianças à meia-noite; permite negociar liberdade. Cena de “Franz no forno” é **farsa, três dretches num saco**, não pai real. Pode ser descoberto por observação Instinto (CD 15)/voz incoerente; trate ameaça no nível de detalhe combinado pela mesa. Recusa não causa derrota roteirizada sem oportunidade de resistência/fuga. Se aceitam, exige cabelo/unha de cada participante para amuletos-santuário: para atacá-la, reação Presença (CD 16) ou escolher outro alvo/ação; quebrar amuleto interrompe proteção. Essa garantia é separada dos sonhos/tarefa e depende de entrega real.

**Majesto**, se Fiona ali, chega como aranha invisível; ajuda com distração/cordas, recusa sacrifício salvo apelo Stella/Presença (CD 15). Sem ele, deixe ferramenta improvisada, nó acessível e janela como alternativas. Dretches ouvem mal, falam Abissal; dois retornam ao barril a cada vinte minutos por cinco, reduzindo guarda. Morgantha sai ao anoitecer para Franz; filhas distraíveis ficam O3. Cordas Finesse/Força (CD 15); ação com lâmina libera sem teste. Dretch Lacaio Dificuldade 12, 1 PV, ataque +1/4 físico; gás por foco/1 Medo, reação Força (CD 12) ou 1 Estresse e tosse que alerta. Não seis ataques simultâneos grátis.

Se escapam, filhas procuram pelo bosque e recuam ao Etéreo quando atacadas, salvo círculo. Cabelos roubados permitem tentar localizar/assombrar até três personagens por noite; amuleto antidetecção/local protegido pode impedir. Pesadelos usam regra H3, com aviso de vínculo e soluções: matar/pactuar com bruxa, recuperar vínculo, proteção planar. Não obrigar devolver crianças como única solução. Prazo meia-noite é perigo evitável, anunciado; resgate continua possível durante preparação, não mutilação gráfica necessária.

### Megálitos próximos

Demarcam Fane da Montanha/Vidente, encobertos por névoa. Um minuto ali atrai quatro névoas vampíricas; pairam dando aviso, depois uma ataca, demais só se insistem. DH Padrão patamar 2: Dificuldade 14, limiares 9/18, PV 3, Estresse 2, ataque +2, dreno 2d6 mágico/recupera 1 PV ao marcar PV; sem imunidade universal. Retirada evita quatro ativos. Não precisa explorar agora; T revisita.

**Registro:** crianças/guarda segura, contrato/nomes, bruxas, coração/cargas de pacto, sonhos, prazos, doença, segredos, aliado/estrutura. H8 na lua cheia.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H8": """## Roteiro Completo · H8 · Lua cheia: restauração de Stella

**Objetivo:** Realizar o ritual sagrado da lua cheia nos jardins de Wachterhaus, utilizando a essência purificada da pedra do moinho para dissipar a maldição de loucura de Stella Wachter e restaurar sua humanidade.

**Contexto & Segredo (DragnaCarta Lore):** Sob a luz da lua cheia, a flor da Fane e a água benta desfazem o trauma mental imposto por Victor. Stella recobra a consciência, abraça sua mãe em prantos e revela os segredos que ouviu sobre os cultistas e o Tomo de Strahd.

**Ambiente & Sensações:**
- *Visão:* O círculo de velas acesas no pátio interno sob a luz prateada e plena da lua cheia; Stella deitada em um lençol branco; feixes de luz prateada descendo sobre sua testa.
- *Sons:* Cântico suave de cura em harmonia com o silêncio da noite; o som de uma respiração que se acalma; e as primeiras palavras humanas de Stella quebrando meses de silêncio felino.
- *Cheiro:* Incenso de alfazema, orvalho noturno e a pureza de água benta sobre pedras frias.
- *Tato:* A testa febril da garota esfriando para uma temperatura saudável e o abraço comovido de uma mãe que reencontra a filha.

**Para narrar:** “A luz prateada da lua cheia banha o pátio de paralelepípedos de Wachterhaus em um fulgor etéreo. Deitada no centro do círculo de velas e orvalho sagrado, Stella para de se debater conforme a essência da Fane toca sua fronte. O olhar felino e vidrado desfaz-se em lágrimas cristalinas, e seus traços relaxam em uma expressão de pura humanidade. Ela abre os olhos, olha para a mãe que chora de joelhos ao seu lado e sussurra com voz fraca e doce: 'Mãe... O pesadelo finalmente acabou?'”

### Preparar porão de Wachterhaus

Fiona, se aliada, baixa proteção e põe seguidores nos acessos. Sem acordo, entrada clandestina não contorna campo: tentativa de ritual falha e chama Fiona; ainda podem explicar e obter cooperação. Câmara tem pentagrama/cinco cadeiras, velas, marcas antigas “Traidor”, adaga de punho curvo e lema **“Na quietude, a morte”**. Leo arranhou paredes no cativeiro; não são armadilha ativa nem prova de que Fiona já conhece tudo.

Victor põe pedra ao centro e começa. Fiona entra decidida a buscar filha. Sombra de garras tenta interferir, mas preparação transporta ao Etéreo; não exigido teste de todos com risco de perder personagem antes da cena.

### Etéreo em DH · regras locais

Reflexos de paredes/móveis translúcidos dificultam visão e dão cobertura: desvantagem a ataque através de obstáculo, conforme DH. Atravessar exige foco de movimento cuidado; terminar voluntariamente dentro de objeto causa 1d10 mágico e expulsão ao apoio mais próximo. Todos flutuam e movem-se por zonas; não ganha alcance infinito ou altura sem limite. Mover objeto refletido move contraparte material nesta cena. Espíritos agora tangíveis podem receber dano normalmente, sem precisar prata/água benta/presa; isso não permite trazer qualquer fantasma vivo de volta por abraçá-lo.

Stella desce alegre, tenta abraço, mas atravessa Victor: está desaparecendo depressa. Ele desenha círculo de restauração. Erasmus aparece como rapaz luminoso de quatorze anos, conversa e explica espíritos inquietos; não foi sombra. Filho de Van Richten, evita detalhes da morte. Victor sente ciúme da amizade, não romance imposto.

### Defender restauração · dez minutos

Victor precisa permanecer conduzindo; interromper pausa progresso, não mata Stella imediatamente. Tempo narrativo avança durante confrontos e conversa; não conte dez minutos como dez rodadas D&D. Marcador **Restauração 6**: preparação preenche 1, sobreviver à abordagem preenche 1, cada ciclo de oportunidade dos PJ enquanto círculo seguro preenche 1; chega a6 ao resolver ameaça e completar canto. Nenhum teste substitui defender local. Se perderem, fuga/interrupção permite reavaliar antes de ela desaparecer definitivamente; relógio de vínculo continua explícito.

Após um minuto, espectros pedem vida e tentam alcançar círculo. Para três/quatro PJ, quatro; cinco, cinco; seis, seis. **Espectro Padrão patamar2:** Dificuldade13, limiares8/16, PV2, Estresse2, ataque+1, toque2d6 mágico; foco para mover até círculo, não posse automática. Primeiro ciclo suficiente para mostrar risco; sobreviventes recuam quando Leo chega, não continuam como acréscimo de dificuldade ao Solo.

### Leo Dilisnya · revelação e conflito

Crânio/manto de rostos sofrendo, cinco luzes douradas e **Tomo de Strahd** junto do peito. Exige sangue Wachter: Stella, Fiona, depois Nikolai/Karl. Alega ter defendido Tatyana/Sergei contra Strahd e sofrido fome por quatrocentos anos. Instinto15 revela omissão; pressão/provas fazem admitir vingança por Reinhold, adaga Ba’al Verzi e ordem de matar Lovina/família. Compreender crueldade de Strahd não justifica assassinar descendentes. Não entrega Tomo por negociação simples; impedir violência conduz à luta.

**Segredo de origem do Tomo:** Livius o achou há um século enquanto Lugdana/Ismark Antonovich buscavam símbolo solar; aprendiz Wachter roubou-o do encadernador encarregado de abrir. Leo tomou-o ao matar família de Fiona. Ela não conhecia a proveniência.

### Leo DH autoral · duas formas, patamar2, Solo

**Orador da Forca:** Dificuldade16, limiares13/24, PV6, Estresse5, ataque+3. Toque profético2d8+3 mágico e pode trocar+3 por desvantagem no próximo ataque/reação da vítima; luz-fátua2d8+2 mágico Próximo. **Visão mortal:** foco/1Estresse, reação Instinto16, falha escolhe ação para recuperar-se ou 1Estresse/desvantagem ao agir; não paralisia que remove personagem por toda cena. **Açoite de almas:** foco/1Estresse, até dois Muito Próximos, reação Força16, falha2d6 mágico/Restrito, sucesso metade; Força/Finesse16 ou ajuda libera. **Clarão:** foco/1Estresse, zona Muito Próxima/alcance Próximo, reação Força16, falha2d6+2 mágico e desvantagem no próximo teste visual, sucesso metade. **Indomável:** foco/1Estresse remove um estado resistível. **Revelação retaliadora:** após ferido, pode obter novo foco pelo custo normal de Medo, não ataque gratuito. **Passo fantasma:** 1Medo/1Estresse depois de ferido, desloca Muito Próximo; medo no ponto de chegada só se escolher nova ação dedicada, reação Instinto16/desvantagem ao aproximar-se.

**Transição0PV:** luzes revelam cinco adagas vermelhas/pretas/douradas; efeitos ofensivos sustentados cessam, estados plausíveis permanecem. **Vingador Ba’al Verzi:** Dificuldade16, mesmos limiares, PV5 novos, Estresse4 novos, ataque+3. **Adaga espectral**, Próximo,2d8+3 mágico; ao marcarPV, reação Instinto16, falha impede recuperarPV até o próximo foco do alvo e o torna Vulnerável nesse período. Não é adaga física amaldiçoada que impede ressurreição para sempre.

**Garras da sepultura:** ataque corpo a corpo2d8+3 mágico, pode trocar+3 por Restrito; só uma presa. Novo foco para arrastar até Próximo/piso superior; Força/Finesse16 ou aliado libera. No máximo 1Estresse da vítima ao permanecer agarrada por ciclo, não dano a cada spotlight. **Almas gritantes:** foco/1Estresse, Muito Próximos reação Força16, falha2d6 mágico e escolhe mover ou agir no foco, sucesso metade. **Lamento:** foco/1Estresse, Próximos reação Instinto16, falha desvantagem no próximo teste; uma vez na forma.

**Presciência:** 1Medo/1Estresse antes de ataque impõe desvantagem ou vantagem à própria reação, então desloca Muito Próximo, uma vez por ciclo. **Laço traidor:** 1Medo/1Estresse quando alvo de ataque corpo a corpo, reação Instinto16, falha atacante escolhe suspender golpe ou 1Estresse para acertar alvo original; não obrigar ferir aliado. **Ecos:** após dano,1Medo/1Estresse, atacante reage Instinto16, falha1d8 mágico e desvantagem no próximo teste, sucesso sem efeito. Escolha uma reação por evento, não todas. Pode atravessar matéria refletida; mesma regra de terminar em objeto. Vê correspondente no outro plano a Próximo, sem atacar através do véu por isso.

**Ajuste:** três PJ PV4/4, danos bônus−2; quatro acima; cinco+1PV por forma; seis+2. Não somar PV D&D, cinco lacaios luzes e novos ataques independentes. FormaI estática/persegue; II captura e tenta subir. **Nesta cena Leo ataca PJ que o bloqueiam**, não executa Stella durante pausa porque isso pareceria taticamente ótimo; os aliados são parte da defesa ficcional. Ofereça retirada/resgate se recursos esgotados.

**Apoio:** Fiona uma vez por ciclo pode ajudar reação/ataque ou usar capacidade de F2, escolhendo uma; uma vez por cena “Sentinela do Véu” impede uma complicação extra de ataque que tenha acertado, sem anular dano normal. Erasmus uma vez por cena arremessa móvel para dar vantagem a ataque ou impedir avanço de Leo por um foco. Sem duas fichas completas extras atacando em todo turno. Victor sustenta ritual, não bombardeia enquanto canta.

### Vitória, retorno e recompensas

Leo dissipa e diz que Strahd tomou sua adaga e poderá usá-la contra o grupo. Tomo cai; recolher antes de voltar. Stella despede-se de Erasmus e retorna ao corpo quando canto conclui; ele promete não estar longe. Fiona agradece e o convida a casa. Erasmus avisa aranhas de fase em ruínas sudoeste e Strahd num cavalo negro flamejante que cruza planos. Victor traz grupo de volta **dentro de uma hora**, sem deixar alguém preso por uma conversa de segundos.

Na matéria, Stella reencontra Victor/mãe junto da escada, alegra-se, precisa reaprender equilíbrio das pernas. É amizade/gratidão, não cura que exige romance. Fiona oferece conselho/ajuda enquanto não puserem cidade em risco e **lanterna de revelação**: acesa, revela formas invisíveis em alcance Próximo enquanto há óleo e linha de visão, sem dano/imunidade/vista através de paredes. No dia seguinte Victor presenteia **espelho espiritual**, reflete matéria/Etéreo Próximo, sem som; uma vez ao dia ação alterna tamanho de mão/corpo. **Van Richten não enxerga Erasmus nele por sua maldição**, ainda resolvida em T.

**Avanço:** marco coletivo Stella salva, sem1.750XP ou duplicação com Tomo. Se fracasso/interrupção, registrar estado/rota de nova tentativa sem prometer outra lua antes do vínculo acabar. Registre família, corpo/alma, Leo, Tomo, pedra devolvida ou prazo, aliados e recursos. H9.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "H9": """## Roteiro Completo · H9 · Tomo de Strahd

**Objetivo:** Estudar e desvendar os segredos arcanos do Tomo de Strahd, vivenciar as memórias da conquista de Baróvia, o ciúme doentio contra seu irmão Sergei, a morte trágica de Tatyana e os pontos fracos do Lorde de Ravenloft.

**Contexto & Segredo (DragnaCarta Lore):** O Tomo de Strahd é uma das três relíquias sagradas profetizadas pelo Tarokka de Madame Eva. Lê-lo não é apenas obter lore: concede aos personagens bônus de dano de conhecimento contra Strahd e desvenda os segredos de suas Fanes e vulnerabilidades emocionais.

**Ambiente & Sensações:**
- *Visão:* Páginas amareladas de pergaminho encadernadas em couro negro reforçado com cantoneiras de ferro; caligrafia aristocrática impecável escrita pelo punho do próprio Strahd com tinta vermelha; ilustrações detalhadas de Tatyana e do Castelo Ravenloft.
- *Sons:* O farfalhar solene de páginas seculares; ecos psíquicos da voz de Strahd ecoando na mente de quem lê; o som distante de um sino fúnebre de casamento interrompido.
- *Cheiro:* Couro antigo, cinzas frias, rosas secas prensadas entre folhas e o odor sutil de sangue imortal preservado no pergaminho.
- *Tato:* O choque estático e gelado ao folhear as memórias de um lorde que vendeu a própria alma por amor e poder.

**Para narrar:** “O Tomo de Strahd repousa aberto sobre a mesa, exalando o peso esmagador de quatro séculos de dor e tragédia. Ao passarem os dedos pelas páginas encadernadas em couro negro, a caligrafia elegante e precisa de Strahd von Zarovich ganha vida diante de seus olhos: 'Eu sou o Antigo. Eu sou a Terra. Minhas mãos ergueram este castelo e meu aço pacificou estas colinas... Mas toda a glória de um guerreiro transformou-se em cinzas no dia em que ela olhou para Sergei com o amor que nunca dedicou a mim.' Nas entrelinhas de sua amargura, revelam-se as fraquezas secretas do soberano: a dependência do Coração da Tristeza e o poder das Três Fanes que sustentam sua imortalidade.”

### Abrir

Frase **“Venho em memória de Dostron”**, conhecida apenas por Strahd/Sasha, suprime selo. Força25 rompe ou Finesse25/ferramenta abre enquanto encantado; tentativa de abrir leva um minuto. Na antimagia da torre de Khazan, ou após capacidade de supressão realmente apropriada, dificuldade15. Não entregue automaticamente spell *knock* por possuir classe DH equivalente. Tentativas com mesma técnica precisam nova abordagem/tempo/consequência, não dados infinitos sem risco.

### Conteúdo legível · handout resumido em português

Strahd se proclama antigo e senhor da terra. Guerras consumiram sua bondade e juventude; conquistou o vale e trouxe família. Invejava Sergei, jovem, e desejava Tatyana, que o tratava apenas como irmão mais velho. Para evitar envelhecimento fez pacto com a Morte, **matou Sergei no dia do casamento** e perseguiu Tatyana; ela saltou das muralhas e seu corpo não foi encontrado. Guardas o flecharam, mas tornou-se morto-vivo. Sol verdadeiro o fere; estaca imobiliza, não o destrói. Teme a espada de Sergei, acredita-a perdida.

Reivindicou poderes dos **Fanes do Pântano, Floresta e Montanha**, antigos deuses e servos, tornando-se “a Terra”. Persegue reencarnações de Tatyana, possui tempo para esperar. Diz dormir sob Ravenloft entre mortos; escondeu riquezas sob sino, atrás de lembrança do amor perdido. O texto é memória egoísta de Strahd, não validação de que amor dá direito de possuir Tatyana/Ireena.

### Páginas cifradas e próximos passos

Diagramas de coração cristalino, círculos de pedras, equações/símbolos e notas em língua comum repetindo **Exethanter**. Sigilo: triângulo grosso, dentro triângulo invertido, dentro linha ondulada vertical. Não é simples idioma traduzível com linguagem universal; cifra pessoal, **Exethanter possui chave**. Dados altos de Conhecimento podem identificar padrão/assunto, não saltar S/U entregando plano completo.

Kasimir reconhece símbolo de sonhos; Godfrey da antiga guarda; Victor do grimório. Kasimir/Godfrey sabem templo e localização, mas só Kasimir, **após Q**, está disposto a guiar. Não transformar silêncio em recusa impossível: razões/vínculos pertencem àquelas cenas.

**Valor prático:** prova da origem de Strahd, pista de Fanes/tesouro/espada/templo e futura decifração. Guardar discreto; definir quem carrega e quem leu. Não concede XP750 nem nova subida imediata: mesmo marco de progresso coletivo.

**Registro:** fecho aberto/técnica, leitores, citações/sigilo identificados, segredo de posse, próximo destino e material entregue aos jogadores.

**Origem:** Reloaded, Arco H, e áreas N3/N4/O1–O4 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I1": """## Roteiro Completo · I1 · Viagem para Krezk

**Objetivo:** Conduzir a travessia das terras ocidentais de Vallaki até as imponentes muralhas de pedra calcária da vila de Krezk, enfrentando as névoas gélidas da subida da serra e as patrulhas de espantalhos corrompidos.

**Contexto & Segredo (DragnaCarta Lore):** A jornada para o oeste cruza o Rio Corvo e aproxima-se dos contrafortes montanhosos de Krezk. As matas aqui são mais silenciosas e o ar é visivelmente mais frio, descendo dos picos nevados.

**Ambiente & Sensações:**
- *Visão:* Estrada pedregosa subindo entre pinheiros cobertos de líquen branco; neblina espessa cobrindo ravinas profundas; e o vulto colossal de muralhas medievais de pedra calcária surgindo no fim da garganta.
- *Sons:* O vento glacial uivando através das agulhas de pinheiro; o crocitar de corvos nas árvores; e o ranger abafado de espantalhos mórbidos plantados na beira da estrada.
- *Cheiro:* Gelo, resina pura, terra congelada e o odor fétido de carniça de animais presos em armadilhas esquecidas.
- *Tato:* Ar gélido que queima as narinas e o bater de dentes com a queda brusca de temperatura.

**Para narrar:** “A estrada para o oeste sobe inexorável em direção às montanhas escarpadas de Krezk. A vegetação torna-se mais austera, com pinheiros cobertos por geada e ravinas de pedra nua cortadas por riachos de degelo. No meio da névoa que rasteja pelo solo congelado, espantalhos com sacos de estopa ensanguentados e dentes humanos costurados vigiam as curvas do caminho como sentinelas macabras. E ao dobrarem a última garganta rochosa, erguem-se contra o céu as ciclópicas muralhas de pedra cinzenta que isolam a comunidade de Krezk do resto do mundo.”

**Origem:** Reloaded, Arco I, e áreas S2–S4/U1–U6 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I2": """## Roteiro Completo · I2 · Dmitri no portão

**Objetivo:** Confrontar o Burgomestre Dmitri Krezkov e os arqueiros da guarda nos portões fechados de Krezk, ouvir suas exigências austeras de quarentena e aceitar a missão de trazer vinho da Vinícola Mago dos Vinhos para obter a abertura dos portões.

**Contexto & Segredo (DragnaCarta Lore):** Krezk é estritamente fechada e auto-suficiente sob o comando sábio e amargurado de Dmitri Krezkov. Ele teme pragas, espiões e zumbis. O único suprimento que falta à vila é o vinho para os funerais e o ânimo do povo. Sem uma carroça de vinho da Vinícola Martikov, os portões jamais serão abertos para estrangeiros.

**Ambiente & Sensações:**
- *Visão:* Portões maciços de carvalho com traves de ferro de seis metros de altura; ameias de pedra onde guardas apontam arcos longos com flechas encordoadas; o Burgomestre Dmitri Krezkov de pé nas passarelas com seu casaco pesado de pele de lobo e olhar severo.
- *Sons:* O som seco de cordas de arco sendo retesadas; o vento batendo nos estandartes cinzentos da vila; e a voz grave e intransigente de Dmitri ecoando do alto da muralha.
- *Cheiro:* Fumaça de lenha de pinho de dentro da vila, geada sobre a pedra e couro ensebado.
- *Tato:* A madeira impenetrável dos portões frios como gelo sob as mãos dos heróis.

**Para narrar:** “Os gigantescos portões de carvalho e ferro de Krezk permanecem hermeticamente fechados. No alto das ameias da muralha de pedra calcária, quatro guardas em trajes pesados de pele apontam flechas prontas para o disparo. Um homem maduro de barba grisalha e postura militar autoritária apoia as mãos na amurada de pedra: o Burgomestre Dmitri Krezkov. Seu tom é calmo, mas frio como o inverno: 'Krezk não recebe estrangeiros e não dá asilo a quem atrai a fúria do demônio do castelo. Nossos muros guardam nossa gente. Mas nossos estoques de vinho estão secos há semanas. Tragam-nos uma carroça cheia de barris da Vinícola Mago dos Vinhos... ou deem meia-volta e enfrentem as florestas.'”

**Registro:** missão, cabelo/pulseira, identidade revelada, negociação e data. I3.

**Origem:** Reloaded, Arco I, e áreas S2–S4/U1–U6 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I3": """## Roteiro Completo · I3 · Estrada para Berez

**Objetivo:** Navegar pelas trilhas lamacentas e alagadas que descem para o sul em direção ao Vale de Berez, enfrentando enxames de insetos do pântano e armadilhas naturais de lodo movediço.

**Contexto & Segredo (DragnaCarta Lore):** A estrada para o pântano de Berez afunda sob a planície úmida. O Rio Luna serpenteia criando charcos viscosos onde a névoa é pesada e ácida. As lendas locais afirmam que Berez é um cemitério afundado governado por uma bruxa colossal.

**Ambiente & Sensações:**
- *Visão:* Salgueiros-chorões com musgo cinzento pendendo como barbas de mortos; poças de água lodosa borbulhando com gases de pântano; ruínas de choupanas de madeira meio afundadas na lama.
- *Sons:* O coaxar monótono e agourento de milhares de rãs carnívoras; o zumbido incessante de mosquitos colossais; e o estalar viscoso de bolhas de metano estourando na lama.
- *Cheiro:* Lodo sulfuroso, matéria orgânica em decomposição, água estagnada e fumaça acre.
- *Tato:* Lama pegajosa que suga as botas até as canelas a cada passo e umidade asfixiante que cola a roupa ao corpo.

**Para narrar:** “A trilha para o sul afunda em um pesadelo pantanoso e desolado. As árvores vigorosas dão lugar a salgueiros retorcidos com musgos negros escorrendo como mortalhas sobre poças de água fétida e estagnada. O ar torna-se pesado e quente, infestado pelo zumbido ensurdecedor de nuvens de insetos carnívoros. Ao longe na neblina, silhuetas de ruínas de pedra semi-afundadas no lodo revelam a entrada dos pântanos malditos de Berez.”

### Criaturas de agulhas

Depois da encruzilhada do Corvo, lobo terrível morto coberto de farpas na estrada, corvos voam alarmados, plantas humanoides marcham para a vinícola. **Ainda não notaram o grupo**. Finesse (CD 10) em ação coordenada permite esconder-se; plano com cobertura adequada pode dispensar teste. Evitar é vitória legítima.

**DH, Horda de agulhas, patamar 2:** Dificuldade 13, limiares 10/18, PV 4, Estresse 3, ataque +1, saraivada 2d6+2 físico Próximo; em metade dos PV ou menos, dano 1d6+2. **Emaranhar**, foco/1 Estresse, reação Finesse (CD 13) ou Restrito; Força/Finesse (CD 13)/ajuda libera. Para três/quatro PJ uma Horda representa seis/oito criaturas; cinco/seis duas Hordas PV 3 cada representam dez/doze. Não oito fichas Padrão somadas; orçamento de Horda 2 PB cada. Fogo impede emaranhar até próximo foco, sem dobro geral de dano.

### Luna e aviso de Lysaga

Ilha de coníferas, tributário, estela de quase dois metros numa península. Inspeção encontra **aranha sobre estrela de três pontas**, símbolo da Tecelã/Rozana. Não requer idioma arcano para descrever. Estrada entra vale de Ghakis, lama/névoa, árvore morta com gaiolas e teias. Um enorme pássaro de madeira/peles, **strix maior**, voa ao sul para alertar Lysaga. Sobe/foge se atacado; não é encontro obrigatório. Se impedido, Wensencia não recebe aviso e chegada à cabana muda.

**Registro:** plantas evitadas/mortas, alerta da strix, símbolo, tempo. I4.

**Origem:** Reloaded, Arco I, e áreas S2–S4/U1–U6 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I4": """## Roteiro Completo · I4 · Berez: negociação e vidência

**Objetivo:** Efetuar o reconhecimento e adivinhação nos arredores das ruínas afundadas de Berez, vislumbrar a colossal Cabana Rastejante de Baba Lysaga caminhando sobre raízes monstruosas e recolher inteligência crucial sobre a gema mágica roubada da vinícola.

**Contexto & Segredo (DragnaCarta Lore):** Berez foi destruída por Strahd séculos atrás e agora é o covil de Baba Lysaga (a antiga ama de leite e mãe adotiva fanática de Strahd). Ela roubou uma das três gemas mágicas da Vinícola Mago dos Vinhos para animar sua colossal cabana de madeira que caminha sobre raízes e crânio de dragão. Atacar Berez agora é mortal; o objetivo é obter informações e escapar.

**Ambiente & Sensações:**
- *Visão:* Ruínas de uma cidade gótica afundada na lama negra; no centro do pântano, uma cabana de madeira de três andares que se ergue sobre raízes colossais animadas que se movem com passadas titânicas; milhares de corvos empalados em estacas na água.
- *Sons:* O impacto estrondoso de raízes de madeira colidindo contra a lama a cada passo da cabana; risadas histéricas e agudas de Baba Lysaga banhando-se em sangue de animais; e o grasnar agoniado de corvos feridos.
- *Cheiro:* Sangue podre em fermentação, lodo sulfuroso, enxofre e carniça velha.
- *Tato:* O tremor na terra a cada passo da cabana viva que faz a água do pântano criar ondas concêntricas.

**Para narrar:** “Através da névoa sulfurosa das ruínas afundadas de Berez, o vislumbre do horror supremo paralisa os sentidos. Entre paredes de pedra carcomidas e arcos de pontes desabadas, ergue-se uma colossal cabana de troncos enegrecidos. Mas a cabana não repousa sobre a terra: ela caminha! Quatro troncos colossais de raízes retorcidas sustentam a estrutura, movendo-se com passos pesados que fazem a lama tremer. No topo da varanda, uma velha decrépita de olhos ensanguentados atira ossos em um caldeirão de cobre, enquanto no coração da cabana brilha uma luz verde-esmeralda pulsante: a gema roubada da vida da vinícola!”

### Chegar e explorar

Dois espantalhos guardam entrada. Não atacam salvo provocados, ordens ou alarme do curral. Se strix avisou, **Wensencia**, aprendiz há três meses de Lysaga, chega sarcástica, exige segui-la para audiência e não responde curiosidades. Há quatro outras alunas; vieram após despertar de Strahd por sugestão de Ludmilla.

**U1:** casas sem tesouro útil, muros baixos. **U2:** solar Ulrich arruinado, jardim selvagem com estátuas, adega soterrada/tonéis vazios. **Não aparece fantasma de Lazlo Ulrich** nesta revisão. **U4:** igreja/cemitério inundados, sino caído. **U5:** monumento de Marina, figura semelhante a Ireena, epitáfio “Levada pelas Névoas”; pista de reencarnação. Sem indicação aleatória de Tarokka, não colocar artefato predestinado extra ali. Retirar/mexer monumento pode atrair sete cadáveres com serpentes: aviso de passos permite retirada; DH lacaios Dificuldade12/1PV/4físico, só dois ativos por foco, romper um libera enxame Padrão Dificuldade13/limiares8–16/PV3/ataque+1/2d6físico. Não obrigar combate com sete enxames por examinar epitáfio.

**Jardim perigoso:** quatro serpentes venenosas, ficção de sinal/fuga possível; uma Horda patamar2 Dificuldade13/limiares8–16/PV4/Estresse2/ataque+1/2d6físico; se marcaPV, reação Força13 ou desvantagem no próximo teste físico por veneno. Cuidados/antitoxina removem. Moscas dificultam descanso em ruínas: proteção contra insetos/campamento seguro torna possível, não rolar quatro enxames a cada conversa.

### Audiência U3 · sem resolver todo Berez agora

Cabana sobre grande toco, raízes servem de escada; gaiolas de corvos, strix no telhado se alertou. Dentro, Lysaga embala ilusão de bebê num berço e canta. **Antes de J** aceita audiência cautelosa; depois de derrotarem ocupantes da vinícola, passa a hostil. Ela não esquece vitória do grupo porque vieram com presente.

Exige pena de corvo no berço como homenagem ao “pequeno Strahd”. Pena atravessa ilusão, ela ignora. Discutir que bebê é falso, insultar Strahd sem retratação ou invadir contra ordem provoca expulsão/conflito. Oferecer alternativa delicada pode ser negociado; não controle moralmente personagem para que maltrate ave.

Aceita pulseira por **uma observação de Ilya**; item equivalente compra segunda de outro alvo. Não cura doença, insinua preço de carne inaceitável. Perguntar por Fiona a enfurece; strixes são criações para capturar/matar corvos.

### Curral e ritual

Busca cabra viva em curral perto U2. Sem portão visível; frase **“Morte a Ravenovia”** a até três metros cria acesso por um minuto. Corda/condução/acalmar resolve captura, Instinto10 se situação incerta. Danificar cerca faz cinquenta crânios uivarem por um minuto e chama Lysaga/espantalhos, não alarme por usar senha certa. Sacrifício animal abastece sangue para ritual: corte a descrição no grau combinado, sem gore necessário. Grupo pode recusar e buscar alternativa, não perder escolha por script.

Lysaga pede silêncio e observa: **rapaz adolescente, cabelo escuro, cicatrizes de garras, coleira de prata preso a poste em caverna. Mulher de cabelo longo/olhar firme acorrentada ao lado, tocada pela Mãe Noite. Estátua de mulher com cabeça de lobo, adornos/tesouros e cadáveres ajoelhados.** Identifica mulher como lobisomem. **Não sabe localização geográfica**, observação mostra arredores do alvo; levar descrição satisfaz tarefa, não exige achar covil neste arco.

### Se conflito/derrota

Sinalize poder muito acima do grupo; fuga/rendição alternativas. Use perfil DH de Lysaga/cabana do confronto de Berez, sem multiplicar raio D&D por foco. Caso sejam capturados vivos, transforma em cabras, acordam no curral após1d4+1h, encontram **Darzin Voltanescu**, explorador também transformado. Diz haver **seis tinturas nulas** no armário de vime, encerrando magia ativa no bebedor. Fuga: passagem pequena/escavar/enganar sentinela, Finesse/Instinto15; entrar furtivo para tinturas Finesse18, apoio/plano oferece vantagem. Uma dose restaura forma, não cura automaticamente pacto/Névoa/vestígio. Não tirar equipamentos permanentemente nem impor captura sobre movimentos de morte DH.

### Pedras da Tecelã, U6

Doze menires, teias, círculo do **Fane do Pântano**; origem anterior era pantanosa, Dostron construiu barragem para cultivo, Strahd a rompeu e afogou Berez após morte de Marina. Pedra lisa de ônix de cerca de um metro e meio é imóvel/indestrutível neste estágio. Teias reduzem deslocamento a uma zona por foco; Finesse15 evita Restrito, ação/ajuda libera. Após minuto, aranha de fase aparece/desaparece; depois outras cinco, só atacam se insistirem. **Aviso para recuar**, sem luta necessária. DH Padrão patamar2: Dificuldade14, limiares10/18, PV4, Estresse3, ataque+2, mordida2d6+2físico; ao marcarPV, reação Força14 ou1Estresse; passo etéreo usa foco, não ataque adicional. Máximo duas ativas simultaneamente antes de escalada anunciada; T/M tratam retorno/preparo. Não importam-se bônus de PV de forma selvagem D&D.

**Registro:** ritual/prova, presente gasto, cabra, alerta/hostilidade, descobertas e hora. I5; J/K/L/T conforme estágio.

**Origem:** Reloaded, Arco I, e áreas S2–S4/U1–U6 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I5": """## Roteiro Completo · I5 · Retorno com a informação

**Objetivo:** Retornar com as informações essenciais de Berez para Krezk e traçar o plano definitivo para obter o carregamento de vinho na Vinícola Mago dos Vinhos (Arc J).

**Contexto & Segredo (DragnaCarta Lore):** Os heróis compreendem que para abrir os portões de Krezk e derrotar a bruxa de Berez no futuro, precisam primeiro libertar a Vinícola Mago dos Vinhos que está sob ataque dos druidas de Yester Hill.

**Ambiente & Sensações:**
- *Visão:* O vale ocidental abrindo-se sob a luz do entardecer; a trilha que sobe de volta para os vinhedos dos Martikov; os portões austeros de Krezk vigiando a serra.
- *Sons:* O vento uivando nas copas dos pinheiros altos; e a voz resoluta de Ismark e Ireena planejando o próximo passo.
- *Cheiro:* Resina de pinho fresca expulsando o odor fétido do pântano.
- *Tato:* A firmeza da rocha sólida sob as botas ao deixar para trás a lama podre de Berez.

**Para narrar:** “Deixando para trás a brenha sulfurosa de Berez, o ar fresco das montanhas ocidentais enche novamente os pulmões com promessa de esperança. Os fatos estão claros: a bruxa de Berez é um monstro imenso alimentado pelo coração roubado da vinícola. Para salvar Krezk e conquistar a confiança de Dmitri, o caminho deve cruzar as colinas rumo à Vinícola Mago dos Vinhos, onde a família dos Guardiões das Penas luta desesperadamente por sobrevivência.”

### Campo de batalha perdido

Na bifurcação do Luna, névoa vira cavaleiros contra piqueiros de elmos com chifres; gritos/metal. **São visões inofensivas**, podem atravessar, não ferir nem ser feridos. Insígnias indistintas, ambos humanos. Se ainda não exploraram Argynvostholt, dragão de névoa prateada dispersa soldados e mostra por instante solar escuro na altura. Revelar apenas direção/visão, não todos os cômodos do solar.

**Registro:** testemunhas/visão, desgaste, destino escolhido, horário. I6 se voltaram a Krezk com relato.

**Origem:** Reloaded, Arco I, e áreas S2–S4/U1–U6 do livro fornecido. Mecânicas DH autorais, sem teste de mesa; substituem os resumos mecânicos abaixo.

---

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

    "I6": """## Roteiro Completo · I6 · Entrada, piscina e abadia

**Objetivo:** Conquistar o acesso final aos portões de Krezk, contemplar a sagrada Piscina Abençoada do Senhor da Manhã, explorar as ruelas serenas da vila e iniciar a subida íngreme para a misteriosa Abadia de Santa Markovia.

**Contexto & Segredo (DragnaCarta Lore):** Uma vez dentro de Krezk, os heróis encontram uma vila pacífica e ordeira que parece isolada da loucura do mundo exterior. No centro da vila repousa a Piscina Abençoada, onde um santuário solar emana águas puras e sagradas com propriedades restauradoras. No topo do penhasco que vigia a vila ergue-se a Abadia de Santa Markovia, governada pelo enigmático e celestial Abade.

**Ambiente & Sensações:**
- *Visão:* Casas de pedra e madeira com telhados de ardósia bem cuidados; hortas férteis irrigadas por canais de pedra; a Piscina Abençoada com águas cristalinas refletindo um raio de sol impossível; e a colossal abadia gótica erguendo-se sobre o penhasco escarpado.
- *Sons:* O murmúrio cristalino de água pura correndo na fonte; crianças brincando com calma inédita em Baróvia; e, vindo do alto da colina da abadia, um cântico perturbador e desafinado de vozes animalescas.
- *Cheiro:* Terra fértil, feno fresco, pão assado e a pureza revigorante de água mineral abençoada.
- *Tato:* A calmaria abençoada das águas da piscina que curam o cansaço dos músculos e renovam o espírito.

**Para narrar:** “Cruzar os portões de Krezk é como entrar em um refúgio esquecido pela maldição de Baróvia. Ruas de cascalho limpo serpenteiam entre casas robustas de pedra e chalés agrícolas com chaminés fumegantes. No coração da vila, cercada por salgueiros prateados, repousa a lendária Piscina Abençoada: uma fonte de águas tão límpidas que refletem o fundo de seixos brancos, onde um raio suave de luz solar parece tocar o altar do Senhor da Manhã. Mas quando vocês erguem os olhos para o penhasco que domina a vila, a silhueta austera da Abadia de Santa Markovia lança uma sombra comprida sobre a paz dos aldeões, enquanto ecos de gritos e uivos desafinados descem da colina do monastério.”

**Entrada:** relato da observação de Ilya satisfaz Dmitri e ele abre portões; não exigir resgate completo para pagar o combinado. Se entraram pela ajuda à vinícola, aplica-se mesma hospitalidade. Casas dispersas entre bosque, moradores autossuficientes, poço/piscina e estrada sinuosa para abadia; pouca circulação externa.

**Família corrigida:** apenas dois filhos: **Ilya13, desaparecido; Kala8, viva**. Não importar quatro filhos mortos/cena de ressurreição original. Dmitri omite que Ilya sumiu na lua cheia **Octyavr22**, catorze dias antes de Neyavr8; calendário lunar local é da campanha, não astronômico real. K aprofunda acordo familiar com Abade.

**Abadia:** alerta história sombria/rumores, oferece rota; Instinto10 nota sombra de preocupação ao falar do Abade, não segredo completo.

**Daggerheart & Mecânicas:** Conduza os testes utilizando a dualidade de Esperança e Medo. Sucessos com Esperança revelam novas pistas e concedem **1 Ponto de Esperança**; falhas com Medo permitem ao Mestre gastar **1 Ponto de Medo** para introduzir complicações imediatas no ambiente ou acelerar os relógios de tensão de Vallaki.""",

}
