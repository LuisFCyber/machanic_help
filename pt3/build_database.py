import json
import random
import time
import os

try:
    from groq import Groq
    HAS_GROQ = True
except ImportError:
    HAS_GROQ = False

# =========================================================================
# CONFIGURAÇÕES DO GERADOR
# =========================================================================
# Se colocar True, ele tentará usar a IA para pesquisar as peças reais.
# Se colocar False, ele usa o gerador estático (rápido e offline).
USE_AI_GENERATION = False 
API_KEY = os.environ.get("GROQ_API_KEY", "YOUR_API_KEY_HERE")

if HAS_GROQ and USE_AI_GENERATION:
    client = Groq(api_key=API_KEY)

# =========================================================================
# VEÍCULOS E MARCAS (Expandido com Imagens Reais)
# =========================================================================
# Utilizando loremflickr para buscar fotos reais correspondentes ao modelo no Flickr
def real_img(brand, model_keyword):
    return f"https://loremflickr.com/800/600/{brand},{model_keyword},car/all"

cars_def = {
    "Chevrolet": [
        ("onix_g1", "Onix G1 1.0/1.4 (2013-2019)", "Hatchback 1ª geração.", real_img("chevrolet", "onix")),
        ("onix_g2", "Onix Plus/Hatch G2 1.0/Turbo (2020+)", "Nova geração global.", real_img("chevrolet", "onix,plus")),
        ("celta_g1", "Celta 1.0 (2000-2006)", "Fase inicial do Celta.", real_img("chevrolet", "celta")),
        ("celta_g2", "Celta 1.0 (2007-2015)", "Fase com frente renovada.", real_img("chevrolet", "celta,2010")),
        ("tracker_g2", "Tracker G2 1.8/1.4T (2014-2020)", "SUV importado do México.", real_img("chevrolet", "tracker,2015")),
        ("tracker_g3", "Tracker G3 1.0/1.2T (2021+)", "SUV fabricado no Brasil.", real_img("chevrolet", "tracker,2022")),
        ("s10_g1", "S10 G1 2.2/2.4/2.8D (1995-2011)", "Primeira geração nacional.", real_img("chevrolet", "s10")),
        ("s10_g2", "S10 G2 2.5/2.8D (2012+)", "Nova geração global com facelift.", real_img("chevrolet", "s10,2018")),
        ("cruze_g1", "Cruze G1 1.8 (2012-2016)", "Sedã e hatch médio.", real_img("chevrolet", "cruze")),
        ("cruze_g2", "Cruze G2 1.4 Turbo (2017-2024)", "Segunda geração turbo.", real_img("chevrolet", "cruze,2018")),
        ("corsa_g1", "Corsa G1 Wind/Super (1994-2002)", "Corsinha clássico.", real_img("chevrolet", "corsa,wind")),
        ("corsa_g2", "Corsa G2 Frente Montana (2002-2012)", "Corsa de plataforma C.", real_img("chevrolet", "corsa,hatch")),
        ("spin", "Spin 1.8 (2012+)", "Minivan espaçosa com 7 lugares.", real_img("chevrolet", "spin")),
        ("equinox", "Equinox 2.0T/1.5T (2018+)", "SUV médio premium esportivo.", real_img("chevrolet", "equinox")),
        ("camaro", "Camaro SS V8 (2010+)", "O famoso Muscle car V8.", real_img("chevrolet", "camaro"))
    ],
    "Fiat": [
        ("palio_g1", "Palio G1 (1996-2000)", "Primeira geração do Palio.", real_img("fiat", "palio,1998")),
        ("palio_g2", "Palio G2 Fire (2001-2006)", "Segunda fase com motor Fire.", real_img("fiat", "palio,fire")),
        ("palio_g3", "Palio G3 (2004-2014)", "Fase Fire Way / Celebration.", real_img("fiat", "palio,celebration")),
        ("palio_g4", "Novo Palio G4 (2012-2017)", "Plataforma moderna (Evo).", real_img("fiat", "novo,palio")),
        ("uno_g1", "Uno Mille (1984-2013)", "O clássico quadrado indestrutível.", real_img("fiat", "uno,mille")),
        ("uno_g2", "Novo Uno Vivace/Evo (2010-2021)", "Geração arredondada.", real_img("fiat", "uno,vivace")),
        ("strada_g1", "Strada G1 a G4 (1998-2020)", "Gerações antigas da picape líder.", real_img("fiat", "strada,adventure")),
        ("strada_g2", "Strada Nova Geração (2021+)", "Renovada com 4 portas e cabine dupla.", real_img("fiat", "nova,strada")),
        ("argo", "Argo 1.0/1.3/1.8 (2017+)", "Hatch premium substituto do Punto e Palio.", real_img("fiat", "argo")),
        ("toro", "Toro 1.8/1.3T/2.0D (2016+)", "Picape SUP moderna e robusta.", real_img("fiat", "toro")),
        ("mobi", "Mobi 1.0 Fire/Firefly (2016+)", "Compacto de entrada para cidade.", real_img("fiat", "mobi")),
        ("punto", "Punto 1.4/1.8 (2007-2017)", "Hatch premium com pegada esportiva.", real_img("fiat", "punto")),
        ("cronos", "Cronos 1.3/1.8 (2018+)", "Sedã elegante derivado do Argo.", real_img("fiat", "cronos")),
        ("fastback", "Fastback 1.0T/1.3T (2022+)", "SUV Coupé nacional estiloso.", real_img("fiat", "fastback")),
        ("fiorino", "Fiorino 1.3/1.4 (1988+)", "O furgão líder absoluto de mercado.", real_img("fiat", "fiorino"))
    ],
    "Volkswagen": [
        ("gol_g2", "Gol G2 Bolinha (1995-1999)", "Clássico redondinho da VW.", real_img("volkswagen", "gol,g2")),
        ("gol_g3", "Gol G3 (2000-2005)", "A geração mais bem acabada da era AP.", real_img("volkswagen", "gol,g3")),
        ("gol_g4", "Gol G4 (2006-2014)", "Frente atualizada, interior simplificado.", real_img("volkswagen", "gol,g4")),
        ("gol_g5", "Gol G5 (2009-2012)", "Projeto PQ24 com motor VHT.", real_img("volkswagen", "gol,g5")),
        ("gol_g6", "Gol G6/G7/G8 (2013-2023)", "Linhas quadradas e forte presença do motor EA211.", real_img("volkswagen", "gol,g7")),
        ("fox_g1", "Fox G1 (2004-2009)", "A primeira geração teto-alto, projetada no Brasil.", real_img("volkswagen", "fox,2008")),
        ("fox_g2", "Fox G2 (2010-2021)", "Frente estilo Golf e muita evolução no acabamento.", real_img("volkswagen", "fox,2015")),
        ("polo_g4", "Polo G4 1.6/2.0 (2002-2014)", "Conforto premium da época.", real_img("volkswagen", "polo,2008")),
        ("polo_g6", "Polo G6 TSI/MSI (2018+)", "A geração global com plataforma MQB.", real_img("volkswagen", "polo,tsi")),
        ("saveiro_g4", "Saveiro G4 (2006-2010)", "Motor AP longitudinal, picape clássica.", real_img("volkswagen", "saveiro,g4")),
        ("saveiro_g5", "Saveiro G5 a G8 (2010+)", "Motor transversal, rival direta da Strada.", real_img("volkswagen", "saveiro,cross")),
        ("amarok", "Amarok 2.0 / V6 (2010+)", "Picape média mais potente do segmento.", real_img("volkswagen", "amarok")),
        ("virtus", "Virtus 1.0/1.4 TSI (2018+)", "Sedã tecnológico e muito espaçoso.", real_img("volkswagen", "virtus")),
        ("jetta", "Jetta 2.0/1.4/2.0 TSI (2006+)", "O sedã médio esportivo dos sonhos.", real_img("volkswagen", "jetta")),
        ("tiguan", "Tiguan 1.4/2.0 TSI (2009+)", "SUV familiar espaçoso e veloz.", real_img("volkswagen", "tiguan")),
        ("nivus", "Nivus 1.0 TSI (2020+)", "Crossover coupé derivado do Polo.", real_img("volkswagen", "nivus")),
        ("up", "Up! 1.0 MPI/TSI (2014-2021)", "O subcompacto mais seguro e ágil.", real_img("volkswagen", "up"))
    ],
    "Ford": [
        ("ka_g1", "Ka G1 Zetec Rocam (1997-2007)", "Visual arredondado e dinâmica de kart.", real_img("ford", "ka,1998")),
        ("ka_g2", "Ka G2 (2008-2013)", "Linhas mais robustas, motor valente.", real_img("ford", "ka,2010")),
        ("ka_g3", "Ka G3 1.0/1.5 (2014-2021)", "Geração global hatch e sedã.", real_img("ford", "ka,2018")),
        ("fiesta_g2", "Fiesta Rocam G2 (2003-2014)", "Fiestinha Rocam super comercializado.", real_img("ford", "fiesta,rocam")),
        ("fiesta_g3", "New Fiesta 1.5/1.6 (2011-2019)", "Geração global Sigma e Ecoboost.", real_img("ford", "new,fiesta")),
        ("ecosport_g1", "EcoSport G1 (2003-2012)", "Criador da categoria SUV compacto no Brasil.", real_img("ford", "ecosport,2008")),
        ("ecosport_g2", "EcoSport G2 (2013-2021)", "Modelo global com estepe na traseira.", real_img("ford", "ecosport,2015")),
        ("ranger_g2", "Ranger G2 (1998-2012)", "Design clássico bruto.", real_img("ford", "ranger,2008")),
        ("ranger_g3", "Ranger G3 T6 (2013-2023)", "Totalmente moderna, rival da Hilux.", real_img("ford", "ranger,2018")),
        ("focus_g2", "Focus G2 (2009-2013)", "Hatch e sedã médios de excelente dirigibilidade.", real_img("ford", "focus,2010")),
        ("focus_g3", "Focus G3 (2014-2019)", "A última geração vendida no Brasil.", real_img("ford", "focus,2016")),
        ("fusion", "Fusion 2.5/2.0T (2006-2019)", "O sedã grande mais amado do Brasil.", real_img("ford", "fusion")),
        ("edge", "Edge V6 / ST (2008-2021)", "SUV importado premium e gigante.", real_img("ford", "edge")),
        ("mustang", "Mustang V8 (2018+)", "O ícone dos muscle cars, importação oficial.", real_img("ford", "mustang")),
        ("territory", "Territory 1.5T (2020+)", "SUV médio luxuoso.", real_img("ford", "territory"))
    ],
    "Hyundai": [
        ("hb20_g1", "HB20 G1 (2012-2019)", "Fenômeno de vendas, mudou o mercado de hatch.", real_img("hyundai", "hb20,2015")),
        ("hb20_g2", "HB20 G2 (2020+)", "Visual atualizado e mecânica turbo.", real_img("hyundai", "hb20,2022")),
        ("creta_g1", "Creta G1 (2017-2021)", "SUV confiável com enorme espaço.", real_img("hyundai", "creta,2018")),
        ("creta_g2", "Creta G2 (2022+)", "Design exótico e nova mecânica.", real_img("hyundai", "creta,2023")),
        ("tucson_g1", "Tucson G1 (2005-2017)", "Guerreiro imortal da Hyundai.", real_img("hyundai", "tucson,2010")),
        ("ix35", "ix35 (2011-2022)", "Substituto de sucesso e muito confortável.", real_img("hyundai", "ix35")),
        ("santa_fe", "Santa Fe V6 (2006-2020)", "SUV premium de 7 lugares.", real_img("hyundai", "santa,fe")),
        ("azera", "Azera V6 (2008-2017)", "A barca V6 coreana de luxo absoluto.", real_img("hyundai", "azera")),
        ("elantra", "Elantra 1.8/2.0 (2012-2018)", "Sedã médio com linhas fluidas.", real_img("hyundai", "elantra")),
        ("i30", "i30 2.0/1.8/1.6T (2009-2016)", "O hatch médio que derrubou o Golf.", real_img("hyundai", "i30")),
        ("veloster", "Veloster 1.6 (2012-2014)", "O famoso hatch de 3 portas.", real_img("hyundai", "veloster")),
        ("hr", "HR 2.5 Diesel (2007+)", "O caminhãozinho de carga mais vendido.", real_img("hyundai", "hr,truck"))
    ],
    "Toyota": [
        ("corolla_brad", "Corolla G9 'Brad' (2003-2008)", "O imortal 1.8.", real_img("toyota", "corolla,2005")),
        ("corolla_g10", "Corolla G10 (2009-2014)", "Evolução do conforto e motor 2.0.", real_img("toyota", "corolla,2012")),
        ("corolla_g11", "Corolla G11 (2015-2019)", "Câmbio CVT espetacular e confiabilidade máxima.", real_img("toyota", "corolla,2018")),
        ("corolla_g12", "Corolla G12 / Hybrid (2020+)", "Primeiro híbrido flex do mundo.", real_img("toyota", "corolla,2022")),
        ("hilux_g7", "Hilux G7 3.0 Diesel (2005-2015)", "Geração blindada nas vendas.", real_img("toyota", "hilux,2012")),
        ("hilux_g8", "Hilux G8 2.8 Diesel (2016+)", "Confiabilidade sem igual no agro.", real_img("toyota", "hilux,2020")),
        ("yaris", "Yaris 1.3/1.5 (2018+)", "Substituto de luxo do Etios.", real_img("toyota", "yaris")),
        ("etios", "Etios 1.3/1.5 (2012-2021)", "Mecânica perfeita, acabamento simples.", real_img("toyota", "etios")),
        ("sw4", "SW4 3.0/2.8 Diesel (2006+)", "O SUV grande derivado da Hilux.", real_img("toyota", "sw4")),
        ("rav4", "RAV4 (2000+)", "O SUV pioneiro e híbrido eficiente.", real_img("toyota", "rav4")),
        ("camry", "Camry V6 (2007+)", "Sedã grande executivo inquebrável.", real_img("toyota", "camry")),
        ("prius", "Prius Hybrid (2013-2019)", "O híbrido mais famoso do planeta.", real_img("toyota", "prius")),
        ("corolla_cross", "Corolla Cross 2.0/Hybrid (2021+)", "A versão SUV do Corolla.", real_img("toyota", "corolla,cross"))
    ],
    "Honda": [
        ("civic_g8", "New Civic G8 (2007-2011)", "Design futurista com painel em dois níveis.", real_img("honda", "civic,2008")),
        ("civic_g9", "Civic G9 (2012-2016)", "Evolução suave focada no conforto.", real_img("honda", "civic,2014")),
        ("civic_g10", "Civic G10 1.5T/2.0 (2017-2022)", "Auge esportivo e motor turbo.", real_img("honda", "civic,2020")),
        ("hrv_g1", "HR-V G1 1.8 (2016-2022)", "Revolucionou a categoria dos SUVs compactos.", real_img("honda", "hrv,2018")),
        ("fit_g1", "Fit G1 (2004-2008)", "Extremamente versátil e econômico.", real_img("honda", "fit,2006")),
        ("fit_g2", "Fit G2/G3 (2009-2020)", "Espaçoso como minivan, ágil como hatch.", real_img("honda", "fit,2012")),
        ("city", "City G2/G3 (2009+)", "Sedã de entrada derivado do Fit.", real_img("honda", "city")),
        ("crv", "CR-V 2.0/1.5T (2000+)", "SUV médio clássico familiar.", real_img("honda", "crv")),
        ("wrv", "WR-V 1.5 (2017-2021)", "O Fit aventureiro mais robusto.", real_img("honda", "wrv")),
        ("accord", "Accord (2008+)", "Sedã executivo gigante e luxuoso.", real_img("honda", "accord")),
        ("civic_si", "Civic Si 2.0/2.4 (2007-2020)", "Versão esportiva pura e giradora.", real_img("honda", "civic,si")),
        ("zrv", "ZR-V 2.0 (2023+)", "O SUV médio que veio cobrir a lacuna do HR-V.", real_img("honda", "zrv"))
    ],
    "Jeep": [
        ("renegade_g1", "Renegade 1.8 E.TorQ/2.0D (2015-2021)", "Ícone quadrado de sucesso.", real_img("jeep", "renegade")),
        ("renegade_g2", "Renegade 1.3 Turbo (2022+)", "Adoção do motor T270 mais forte.", real_img("jeep", "renegade,2023")),
        ("compass_g2", "Compass 2.0 Flex/Diesel (2017-2021)", "Líder absoluto de SUVs médios.", real_img("jeep", "compass,2018")),
        ("compass_g3", "Compass 1.3T T270 (2022+)", "Interior renovado e mais potência.", real_img("jeep", "compass,2023")),
        ("commander", "Commander 1.3T/2.0D (2022+)", "SUV de 7 lugares luxuoso.", real_img("jeep", "commander")),
        ("grand_cherokee", "Grand Cherokee V6/V8 (2011+)", "Luxo imponente americano.", real_img("jeep", "grand,cherokee")),
        ("wrangler", "Wrangler 3.6/2.0T (2008+)", "O 4x4 raiz definitivo.", real_img("jeep", "wrangler")),
        ("cherokee", "Cherokee V6 (1998-2015)", "O SUV com cara de durão.", real_img("jeep", "cherokee")),
        ("gladiator", "Gladiator 3.6 (2022+)", "A picape mais off-road do mundo baseada no Wrangler.", real_img("jeep", "gladiator")),
        ("patriot", "Patriot 2.4 (2007-2017)", "O irmão mais quadradão do antigo Compass.", real_img("jeep", "patriot"))
    ],
    "Nissan": [
        ("kicks_g1", "Kicks 1.6 (2017-2020)", "Crossover leve e econômico.", real_img("nissan", "kicks")),
        ("kicks_g2", "Kicks 1.6 Facelift (2021+)", "Crossover com frente moderna.", real_img("nissan", "kicks,2022")),
        ("versa_g1", "Versa G1 V-Drive (2012-2020)", "Espaço de limusine em tamanho de hatch.", real_img("nissan", "versa")),
        ("versa_g2", "Versa G2 1.6 (2021+)", "Design completamente remodelado.", real_img("nissan", "versa,2022")),
        ("frontier_g13", "Frontier 2.3 Biturbo (2017+)", "Picape moderna com suspensão multilink.", real_img("nissan", "frontier,2018")),
        ("frontier_g12", "Frontier 2.5 Diesel (2008-2016)", "Geração antiga bruta.", real_img("nissan", "frontier,2012")),
        ("march", "March 1.0/1.6 (2011-2020)", "Compacto ágil e super resistente.", real_img("nissan", "march")),
        ("sentra", "Sentra 2.0 (2008-2020)", "Sedã médio robusto de tios.", real_img("nissan", "sentra")),
        ("sentra_g8", "Novo Sentra 2.0 (2023+)", "A volta triunfal com design arrojado.", real_img("nissan", "sentra,2023")),
        ("tiida", "Tiida 1.8 (2008-2013)", "Hatch médio com espaço interno gigantesco.", real_img("nissan", "tiida")),
        ("livina", "Livina 1.6/1.8 (2009-2014)", "Minivan confortável para a família.", real_img("nissan", "livina"))
    ],
    "Renault": [
        ("kwid", "Kwid 1.0 (2018+)", "Subcompacto e queridinho de frotas, o SUV dos compactos.", real_img("renault", "kwid")),
        ("duster_g1", "Duster G1 1.6/2.0 (2012-2020)", "O tanque francês/romeno robusto que topa tudo.", real_img("renault", "duster,2015")),
        ("duster_g2", "Duster G2 1.6/1.3T (2021+)", "Mais tecnológico e com painel moderno.", real_img("renault", "duster,2022")),
        ("sandero_g2", "Sandero G2 / Stepway (2015-2022)", "Muito espaço interno e manutenção barata.", real_img("renault", "sandero")),
        ("logan_g2", "Logan G2 (2014+)", "Visual europeu e porta-malas gigantesco.", real_img("renault", "logan")),
        ("clio", "Clio 1.0/1.6 (2000-2016)", "O guerreiro econômico que rodou todo o Brasil.", real_img("renault", "clio")),
        ("megane", "Megane Grand Tour 1.6/2.0 (2007-2013)", "A perua mais vendida da categoria.", real_img("renault", "megane,tour")),
        ("kangoo", "Kangoo 1.6 (2000-2018)", "Furgão versátil e espaçoso.", real_img("renault", "kangoo")),
        ("fluence", "Fluence 2.0 (2011-2018)", "Sedã médio subestimado e luxuoso.", real_img("renault", "fluence")),
        ("captur", "Captur 1.6/2.0/1.3T (2017+)", "SUV estiloso montado na base do Duster.", real_img("renault", "captur")),
        ("oroch", "Duster Oroch 1.6/2.0/1.3T (2016+)", "A picape que inaugurou o segmento da Toro.", real_img("renault", "oroch")),
        ("master", "Master 2.3/2.5 Diesel (2003+)", "A van líder absoluta do transporte executivo.", real_img("renault", "master,van"))
    ],
    "Peugeot": [
        ("peugeot_206", "206 1.0/1.4/1.6 (1999-2010)", "O hatch que revolucionou o design mundial.", real_img("peugeot", "206")),
        ("peugeot_207", "207 Brasil 1.4/1.6 (2008-2014)", "O 206 com frente maquiada.", real_img("peugeot", "207")),
        ("peugeot_208_g1", "208 G1 1.5/1.6 (2013-2020)", "Painel i-Cockpit inovador, hatch premium.", real_img("peugeot", "208,2015")),
        ("peugeot_208_g2", "208 G2 1.0/1.6 (2021+)", "Design dente de sabre agressivo e luxuoso.", real_img("peugeot", "208,2022")),
        ("peugeot_2008", "2008 1.6/THP (2015+)", "SUV compacto elegante com teto panorâmico.", real_img("peugeot", "2008,suv")),
        ("peugeot_307", "307 1.6/2.0 (2002-2012)", "Hatch e sedã médios marcantes dos anos 2000.", real_img("peugeot", "307")),
        ("peugeot_308", "308 1.6/2.0/THP (2012-2019)", "Hatch médio de condução esportiva.", real_img("peugeot", "308")),
        ("peugeot_408", "408 2.0/THP (2011-2019)", "Sedã imponente da marca leão.", real_img("peugeot", "408")),
        ("peugeot_3008", "3008 1.6 THP (2011-2023)", "SUV que parece uma nave espacial por dentro.", real_img("peugeot", "3008")),
        ("peugeot_partner", "Partner 1.6 (1999-2021)", "Furgão valente para o trabalho diário.", real_img("peugeot", "partner")),
        ("peugeot_boxer", "Boxer Diesel (2000+)", "Van gigante irmã da Ducato e Jumper.", real_img("peugeot", "boxer,van"))
    ],
    "Citroën": [
        ("citroen_c3_g1", "C3 G1 (2003-2012)", "Design em formato de bolha muito querido.", real_img("citroen", "c3,2008")),
        ("citroen_c3_g2", "C3 G2 (2013-2020)", "Com para-brisa Zenith panorâmico.", real_img("citroen", "c3,2015")),
        ("citroen_c3_g3", "Novo C3 G3 (2023+)", "Atitude SUV em formato hatch de entrada.", real_img("citroen", "c3,2023")),
        ("citroen_c4_cactus", "C4 Cactus 1.6/THP (2018+)", "Design irreverente com Airbumps.", real_img("citroen", "c4,cactus")),
        ("citroen_c3_aircross", "Aircross 1.6 (2011-2020)", "Minivan aventureira familiar com estepe.", real_img("citroen", "aircross,2014")),
        ("citroen_c4_pallas", "C4 Pallas 2.0 (2007-2013)", "O sedã gigante com volante de cubo fixo.", real_img("citroen", "c4,pallas")),
        ("citroen_c4_lounge", "C4 Lounge 1.6 THP/2.0 (2014-2020)", "Sedã que substituiu o Pallas com luxo e turbo.", real_img("citroen", "c4,lounge")),
        ("citroen_xsara_picasso", "Xsara Picasso 1.6/2.0 (2001-2012)", "A minivan mãe de todas que cabia tudo.", real_img("citroen", "xsara,picasso")),
        ("citroen_ds3", "DS3 1.6 THP (2012-2017)", "Hot hatch estiloso para diversão pura.", real_img("citroen", "ds3")),
        ("citroen_berlingo", "Berlingo 1.6 (1998-2007)", "Furgão parceiro do trabalho.", real_img("citroen", "berlingo")),
        ("citroen_jumper", "Jumper Diesel (2000+)", "Van de passageiros ou carga irmã da Ducato.", real_img("citroen", "jumper"))
    ],
    "Mitsubishi": [
        ("lancer", "Lancer 2.0 (2011-2019)", "DNA de rali no asfalto com visual agressivo.", real_img("mitsubishi", "lancer")),
        ("asx", "ASX 2.0 (2011-2021)", "SUV compacto robusto que virou Outlander Sport.", real_img("mitsubishi", "asx")),
        ("l200_triton", "L200 Triton (2008-2016)", "Picape clássica do campo e das dunas.", real_img("mitsubishi", "l200,triton")),
        ("l200_triton_sport", "L200 Triton Sport (2017+)", "Nova geração muito mais tecnológica.", real_img("mitsubishi", "l200,sport")),
        ("l200_savana", "L200 Savana", "Versão voltada puramente para Off-Road.", real_img("mitsubishi", "l200,savana")),
        ("outlander", "Outlander 2.0/V6 (2008-2021)", "Crossover imponente com opção 7 lugares.", real_img("mitsubishi", "outlander")),
        ("pajero_tr4", "Pajero TR4 2.0 Flex (2003-2015)", "O jipinho urbano nacional mais guerreiro 4x4.", real_img("mitsubishi", "pajero,tr4")),
        ("pajero_full", "Pajero Full 3.2D/3.8 (2001-2021)", "O verdadeiro jipe blindado em qualidade de construção.", real_img("mitsubishi", "pajero,full")),
        ("pajero_dakar", "Pajero Dakar 3.2D (2009-2017)", "Base de L200 Triton transformada em SUV.", real_img("mitsubishi", "pajero,dakar")),
        ("eclipse_cross", "Eclipse Cross 1.5T (2018+)", "Design exótico com vidro traseiro duplo.", real_img("mitsubishi", "eclipse,cross"))
    ],
    "BMW": [
        ("bmw_118i", "118i (2010-2019)", "Hatch tração traseira puro sangue.", real_img("bmw", "118i")),
        ("bmw_320i_e90", "320i E90 (2006-2012)", "Sedã clássico de motor aspirado valente.", real_img("bmw", "320i,e90")),
        ("bmw_320i_f30", "320i F30 (2012-2018)", "O sedã esportivo turbo mais desejado do Brasil.", real_img("bmw", "320i,f30")),
        ("bmw_320i_g20", "320i G20 (2019+)", "Geração atual tecnológica e moderna.", real_img("bmw", "320i,g20")),
        ("bmw_528i", "Série-5 528i (2011-2016)", "Luxo e desempenho em tamanho grande.", real_img("bmw", "528i")),
        ("bmw_x1_e84", "X1 E84 (2010-2015)", "SUV de entrada da marca com tração traseira.", real_img("bmw", "x1,e84")),
        ("bmw_x1_f48", "X1 F48 (2016+)", "SUV com tração dianteira e muito espaço.", real_img("bmw", "x1,f48")),
        ("bmw_x3", "X3 (2011+)", "O SUV médio perfeito da marca bávara.", real_img("bmw", "x3")),
        ("bmw_x5", "X5 (2007+)", "O grandalhão de luxo que intimida no trânsito.", real_img("bmw", "x5")),
        ("bmw_x6", "X6 (2009+)", "O criador da categoria SUV Coupé gigante.", real_img("bmw", "x6")),
        ("bmw_z4", "Z4 Roadster (2010+)", "Roadster conversível para curtir o final de semana.", real_img("bmw", "z4"))
    ],
    "Audi": [
        ("audi_a1", "A1 1.4 TFSI (2011-2018)", "O menor dos argolas, ágil e premium.", real_img("audi", "a1")),
        ("audi_a3_hatch", "A3 Sportback (2007-2021)", "O hatch médio turbo mais querido dos jovens.", real_img("audi", "a3,sportback")),
        ("audi_a3_sedan", "A3 Sedan 1.4/2.0 TFSI (2014-2020)", "Luxo compacto alemão com mecânica VW forte.", real_img("audi", "a3,sedan")),
        ("audi_a4", "A4 2.0 TFSI (2009+)", "Sedã clássico da Audi sempre moderno.", real_img("audi", "a4")),
        ("audi_a5", "A5 Sportback (2010+)", "Cupê 4 portas de visual arrebatador.", real_img("audi", "a5,sportback")),
        ("audi_q3_g1", "Q3 G1 1.4/2.0 TFSI (2013-2018)", "SUV compacto sofisticado.", real_img("audi", "q3")),
        ("audi_q3_g2", "Q3 G2 (2020+)", "Nova geração muito mais tecnológica.", real_img("audi", "q3,2021")),
        ("audi_q5", "Q5 2.0 TFSI (2009+)", "O SUV médio premium padrão da indústria.", real_img("audi", "q5")),
        ("audi_q7", "Q7 (2007+)", "Luxo para 7 pessoas.", real_img("audi", "q7")),
        ("audi_tt", "TT 2.0 TFSI (2008-2018)", "Coupé esportivo inconfundível.", real_img("audi", "tt"))
    ],
    "Kia": [
        ("picanto", "Picanto 1.0 (2008-2018)", "O subcompacto simpático coreano.", real_img("kia", "picanto")),
        ("cerato_g2", "Cerato G2 (2010-2013)", "Sedã que marcou a revolução de design da Kia.", real_img("kia", "cerato,2011")),
        ("cerato_g3", "Cerato G3/G4 (2014+)", "Evoluções do sedã médio confortável.", real_img("kia", "cerato,2018")),
        ("soul", "Soul 1.6 (2010-2019)", "Carro design quadradão e estiloso.", real_img("kia", "soul")),
        ("sportage_g3", "Sportage G3 (2011-2016)", "Design revolucionário de Peter Schreyer.", real_img("kia", "sportage,2014")),
        ("sportage_g4", "Sportage G4 (2017-2022)", "Mais agressivo, rival direto do Compass.", real_img("kia", "sportage,2018")),
        ("sorento", "Sorento V6/2.4 (2010-2020)", "SUV grande de 7 lugares luxuoso.", real_img("kia", "sorento")),
        ("carnival", "Carnival V6 (2008+)", "Minivan gigante para transporte VIP.", real_img("kia", "carnival")),
        ("bongo", "Bongo K2500 (2008+)", "O caminhãozinho parceiro das empresas.", real_img("kia", "bongo")),
        ("optima", "Optima 2.0/2.4 (2012-2016)", "Sedã gigante super luxuoso e de belas rodas.", real_img("kia", "optima")),
        ("stonic", "Stonic Hybrid (2022+)", "Crossover híbrido super econômico.", real_img("kia", "stonic"))
    ]
}

categories = {
    "Óleo e Fluidos": [
        {"name": "Óleo de Motor 5W30 Sintético", "brands": {"ACDelco": "98550168", "Mobil": "Super 3000 5W30", "Castrol": "Magnatec 5W30", "Motul": "8100 5W30", "Lubrax": "Valora 5W30", "Shell": "Helix HX8 5W30"}},
        {"name": "Óleo de Motor 15W40 Mineral", "brands": {"ACDelco": "98550160", "Mobil": "Super 1000", "Castrol": "GTX 15W40", "Lubrax": "Essencial 15W40"}},
        {"name": "Fluido de Arrefecimento", "brands": {"Paraflu": "Bio Orgânico", "Radiex": "R-1922", "Tirreno": "Original", "Delphi": "RL10012"}},
        {"name": "Fluido de Freio DOT 4", "brands": {"Varga": "DOT4", "Bosch": "DOT 4 500ml", "Controil": "C-200", "ATE": "SL DOT4"}},
        {"name": "Óleo de Câmbio", "brands": {"Isafluid": "556", "Ipiranga": "Ipiranga Gear", "Petronas": "Tutela"}}
    ],
    "Filtros": [
        {"name": "Filtro de Óleo", "brands": {"Tecfil": "PSL", "Mann": "W712", "Fram": "PH47", "Mahle": "OC90", "Wega": "WO"}},
        {"name": "Filtro de Ar do Motor", "brands": {"Tecfil": "ARL", "Fram": "CA", "Mann": "C29", "Wega": "FAP"}},
        {"name": "Filtro de Combustível", "brands": {"Tecfil": "GI0", "Bosch": "0986B", "Mann": "WK", "Fram": "G10"}},
        {"name": "Filtro de Cabine (A/C)", "brands": {"Tecfil": "ACP", "Filtros Mil": "FC", "Mann": "CU", "Wega": "AKX"}}
    ],
    "Motor": [
        {"name": "Vela de Ignição", "brands": {"NGK": "BPR", "Bosch": "SP", "Denso": "W20"}},
        {"name": "Cabo de Vela", "brands": {"NGK": "SC", "Bosch": "902", "Magneti Marelli": "CVM"}},
        {"name": "Bobina de Ignição", "brands": {"Bosch": "F00", "Delphi": "CE", "NGK": "U2"}},
        {"name": "Correia Dentada", "brands": {"Gates": "408", "Contitech": "CT", "Dayco": "111"}}
    ],
    "Arrefecimento": [
        {"name": "Bomba d'Água", "brands": {"Urba": "UB", "Nakata": "NK", "Schadek": "20.0"}},
        {"name": "Válvula Termostática", "brands": {"Wahler": "314", "MTE-Thomson": "VT"}}
    ],
    "Freios": [
        {"name": "Pastilha de Freio Dianteira", "brands": {"Cobreq": "N-", "Fras-le": "PD/", "Syl": "10", "Bosch": "0986"}},
        {"name": "Disco de Freio Dianteiro", "brands": {"Fremax": "BD", "Hipper Freios": "HF", "TRW": "DF"}}
    ],
    "Suspensão": [
        {"name": "Amortecedor Dianteiro", "brands": {"Monroe": "273", "Cofap": "GP", "Nakata": "HG", "Kayaba": "KYB"}},
        {"name": "Bandeja de Suspensão", "brands": {"Nakata": "NB", "Perfect": "BR", "Grazzimetal": "GZ"}}
    ]
}

cars = []
brand_models = {}

# Build the car structure
for brand, models in cars_def.items():
    brand_models[brand] = []
    for m_id, name, desc, img in models:
        brand_models[brand].append(name)
        cars.append({
            "id": m_id,
            "brand": brand,
            "name": name,
            "image": img,
            "description": desc,
            "parts": []
        })

brand_code_prefixes = {
    "Chevrolet": "GM", "Fiat": "FIAT", "Volkswagen": "VW", "Ford": "FORD",
    "Hyundai": "HY", "Toyota": "TOY", "Honda": "HND", "Jeep": "JEEP",
    "Nissan": "NIS", "Renault": "REN", "Peugeot": "PEU", "Citroën": "CIT",
    "Mitsubishi": "MIT", "BMW": "BMW", "Audi": "AUDI", "Kia": "KIA"
}

def generate_base_code(car_idx, part_idx, cat_idx, brand):
    prefix = brand_code_prefixes.get(brand, "COD")
    return f"{prefix} {10000000 + (car_idx * 1000000) + (cat_idx * 10000) + part_idx * 17}"

def build_static_database():
    print("Construindo banco de dados estático profissional...")
    for car_idx, car in enumerate(cars):
        brand = car["brand"]
        
        for cat_idx, (category_name, items) in enumerate(categories.items()):
            for part_idx, item in enumerate(items):
                compatibles = []
                for comp_brand, code in item["brands"].items():
                    if category_name == "Óleo e Fluidos":
                        variant_code = code 
                    else:
                        variant_code = f"{code}{car_idx*7 + part_idx*3 + 120}"
                    compatibles.append({"brand": comp_brand, "code": variant_code})
                
                compatible_cars_names = []
                if category_name == "Óleo e Fluidos":
                    all_other_cars = [c["name"] for c in cars if c["name"] != car["name"]]
                    compatible_cars_names = random.sample(all_other_cars, min(len(all_other_cars), random.randint(2, 4)))
                else:
                    same_brand_cars = [c for c in brand_models[brand] if c != car["name"]]
                    if same_brand_cars:
                        compatible_cars_names = random.sample(same_brand_cars, min(len(same_brand_cars), 1))

                part = {
                    "name": item["name"],
                    "category": category_name,
                    "originalCode": generate_base_code(car_idx, part_idx, cat_idx, brand),
                    "compatibles": compatibles,
                    "compatibleCars": compatible_cars_names
                }
                car["parts"].append(part)

    save_database(cars)

def generate_prompt(car_name, brand):
    return f"""
    Você é um especialista MASTER em catálogos de autopeças automotivas do Brasil.
    Forneça os códigos REAIS (OEM e Aftermarket) com 100% DE CERTEZA para o veículo: {brand} {car_name}.
    Retorne EXATAMENTE e APENAS um objeto JSON válido contendo uma chave "parts" com o array de peças (Filtros, Velas, Óleo, Pastilha).
    O formato EXATO deve ser:
    {{
        "parts": [
            {{
                "name": "Nome da Peça", "category": "Categoria", "originalCode": "CÓDIGO OEM",
                "compatibles": [ {{"brand": "Marca Paralela", "code": "Código"}} ],
                "compatibleCars": ["{car_name}"]
            }}
        ]
    }}
    """

def build_ai_database():
    print("Iniciando construção de banco via IA (pode demorar)...")
    final_database = []
    
    for car in cars:
        print(f"Consultando IA para: {car['brand']} {car['name']}...")
        prompt = generate_prompt(car['name'], car['brand'])
        
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
                response_format={"type": "json_object"}
            )
            response_text = chat_completion.choices[0].message.content.strip()
            
            parts_data = json.loads(response_text)["parts"]
            car["parts"] = parts_data
            final_database.append(car)
            
            print(f"[+ SUCESSO] Peças reais coletadas para {car['name']}!")
            save_database(final_database)
            time.sleep(3) 
            
        except Exception as e:
            print(f"[X ERRO] Falha de comunicação para {car['name']}: {e}")
            if "429" in str(e):
                print("Limites atingidos. Encerrando e salvando o que foi coletado.")
                break
            time.sleep(3)

def save_database(db_data):
    header_comments = """// =========================================================================
// BANCO DE DADOS DE PEÇAS E VEÍCULOS - AUTOPARTS PRO
// Gerado automaticamente com marcas premium e imagens reais.
// =========================================================================

"""
    js_content = header_comments + "const database = " + json.dumps(db_data, indent=4, ensure_ascii=False) + ";\n\nwindow.database = database;\n"
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(js_content)

if __name__ == "__main__":
    if USE_AI_GENERATION and HAS_GROQ:
        build_ai_database()
    else:
        build_static_database()
    print("\nArquivo 'data.js' atualizado com sucesso!")
    print("Abra o 'index.html' no navegador para ver o resultado.")
