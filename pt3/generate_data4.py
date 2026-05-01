import json
import random

cars_def = {
    "Chevrolet": [
        ("onix_g1", "Onix G1 1.0/1.4 (2013-2019)", "Hatchback 1ª geração.", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=800"),
        ("onix_g2", "Onix Plus/Hatch G2 1.0/Turbo (2020+)", "Nova geração global.", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=800"),
        ("celta_g1", "Celta 1.0 (2000-2006)", "Fase inicial do Celta (frente lisa).", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("celta_g2", "Celta 1.0 (2007-2015)", "Fase com frente renovada e motor VHC-E.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("tracker_g2", "Tracker G2 1.8/1.4T (2014-2020)", "SUV importado do México.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("tracker_g3", "Tracker G3 1.0/1.2T (2021+)", "SUV fabricado no Brasil, plataforma GEM.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("s10_g1", "S10 G1 2.2/2.4/2.8D (1995-2011)", "Primeira geração nacional.", "https://images.unsplash.com/photo-1559404047-927b5e43a8ce?auto=format&fit=crop&q=80&w=800"),
        ("s10_g2", "S10 G2 2.5/2.8D (2012+)", "Nova geração global com facelift.", "https://images.unsplash.com/photo-1559404047-927b5e43a8ce?auto=format&fit=crop&q=80&w=800"),
        ("cruze_g1", "Cruze G1 1.8 (2012-2016)", "Sedã e hatch médio.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800"),
        ("cruze_g2", "Cruze G2 1.4 Turbo (2017-2024)", "Segunda geração turbo.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800"),
        ("corsa_g1", "Corsa G1 Wind/Super (1994-2002)", "Corsinha clássico.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("corsa_g2", "Corsa G2 Frente Montana (2002-2012)", "Corsa de plataforma C.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800")
    ],
    "Fiat": [
        ("palio_g1", "Palio G1 (1996-2000)", "Primeira geração.", "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&q=80&w=800"),
        ("palio_g2", "Palio G2 Fire (2001-2006)", "Segunda fase com faróis alongados.", "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&q=80&w=800"),
        ("palio_g3", "Palio G3 (2004-2014)", "Fase Fire Way / Celebration.", "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&q=80&w=800"),
        ("palio_g4", "Palio G4/Novo Palio (2008-2017)", "Plataforma mais moderna (frente Evo).", "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&q=80&w=800"),
        ("uno_g1", "Uno Mille (1984-2013)", "O clássico carro quadrado.", "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&q=80&w=800"),
        ("uno_g2", "Novo Uno Vivace/Evo (2010-2021)", "Geração arredondada (Square Circle).", "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&q=80&w=800"),
        ("strada_g1", "Strada G1 a G4 (1998-2020)", "Gerações antigas.", "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&q=80&w=800"),
        ("strada_g2", "Strada Nova Geração (2021+)", "Totalmente renovada com 4 portas.", "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&q=80&w=800"),
        ("argo", "Argo 1.0/1.3/1.8 (2017+)", "Substituto premium do Punto e Palio.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("toro", "Toro 1.8/1.3T/2.0D (2016+)", "Picape SUP moderna.", "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&q=80&w=800"),
        ("mobi", "Mobi 1.0 Fire/Firefly (2016+)", "Compacto de entrada ágil e pequeno.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800")
    ],
    "Volkswagen": [
        ("gol_g2", "Gol G2 Bolinha (1995-1999)", "Clássico redondinho da VW.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("gol_g3", "Gol G3 (2000-2005)", "A geração mais luxuosa da AP.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("gol_g4", "Gol G4 (2006-2014)", "Frente atualizada, interior simplificado.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("gol_g5", "Gol G5 (2009-2012)", "Projeto PQ24 com motor VHT.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("gol_g6", "Gol G6/G7/G8 (2013-2023)", "Linhas quadradas e motor EA211.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("fox_g1", "Fox G1 (2004-2009)", "A primeira geração teto-alto.", "https://images.unsplash.com/photo-1542282088-fe8426682b8f?auto=format&fit=crop&q=80&w=800"),
        ("fox_g2", "Fox G2 (2010-2021)", "Frente Golf e muita evolução.", "https://images.unsplash.com/photo-1542282088-fe8426682b8f?auto=format&fit=crop&q=80&w=800"),
        ("polo_g4", "Polo G4 1.6/2.0 (2002-2014)", "Conforto premium da época.", "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&q=80&w=800"),
        ("polo_g6", "Polo G6 TSI/MSI (2018+)", "A geração global MQB.", "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&q=80&w=800"),
        ("saveiro_g4", "Saveiro G4 (2006-2010)", "Motor AP longitudinal.", "https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&q=80&w=800"),
        ("saveiro_g5", "Saveiro G5 a G8 (2010+)", "Motor transversal EA111 e EA211.", "https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&q=80&w=800"),
        ("amarok", "Amarok 2.0 / V6 (2010+)", "Picape luxuosa da Volks.", "https://images.unsplash.com/photo-1621007947382-d3119ee5c46b?auto=format&fit=crop&q=80&w=800"),
        ("virtus", "Virtus 1.0/1.4 TSI (2018+)", "Sedã tecnológico derivado do Polo.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800")
    ],
    "Ford": [
        ("ka_g1", "Ka G1 Zetec Rocam (1997-2007)", "Visual marcante arredondado.", "https://images.unsplash.com/photo-1550524614-ea0d1f753557?auto=format&fit=crop&q=80&w=800"),
        ("ka_g2", "Ka G2 (2008-2013)", "Linhas mais robustas, motor Flex.", "https://images.unsplash.com/photo-1550524614-ea0d1f753557?auto=format&fit=crop&q=80&w=800"),
        ("ka_g3", "Ka G3 1.0/1.5 (2014-2021)", "Última geração global fabricada aqui.", "https://images.unsplash.com/photo-1550524614-ea0d1f753557?auto=format&fit=crop&q=80&w=800"),
        ("fiesta_g2", "Fiesta Rocam G2 (2003-2014)", "Fiestinha que dominou o mercado.", "https://images.unsplash.com/photo-1582467029213-ce71667c2e28?auto=format&fit=crop&q=80&w=800"),
        ("fiesta_g3", "New Fiesta 1.5/1.6 (2011-2019)", "Geração global Sigma.", "https://images.unsplash.com/photo-1582467029213-ce71667c2e28?auto=format&fit=crop&q=80&w=800"),
        ("ecosport_g1", "EcoSport G1 (2003-2012)", "O criador da categoria SUV compacto.", "https://images.unsplash.com/photo-1553440569-bcc63803a83d?auto=format&fit=crop&q=80&w=800"),
        ("ecosport_g2", "EcoSport G2 (2013-2021)", "Modelo global com traseira esportiva.", "https://images.unsplash.com/photo-1553440569-bcc63803a83d?auto=format&fit=crop&q=80&w=800"),
        ("ranger_g2", "Ranger G2 (1998-2012)", "Design clássico bruto.", "https://images.unsplash.com/photo-1609521263047-f8f205293f24?auto=format&fit=crop&q=80&w=800"),
        ("ranger_g3", "Ranger G3 T6 (2013-2023)", "Totalmente moderna, diesel e flex.", "https://images.unsplash.com/photo-1609521263047-f8f205293f24?auto=format&fit=crop&q=80&w=800"),
        ("ranger_g4", "Ranger G4 V6 (2024+)", "A nova e brutal plataforma T6.2.", "https://images.unsplash.com/photo-1609521263047-f8f205293f24?auto=format&fit=crop&q=80&w=800")
    ],
    "Hyundai": [
        ("hb20_g1", "HB20 G1 (2012-2019)", "Fenômeno de vendas, motores Gamma/Kappa.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("hb20_g2", "HB20 G2 (2020+)", "Visual atualizado e mecânica turbo.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("creta_g1", "Creta G1 (2017-2021)", "SUV confiável e campeão.", "https://images.unsplash.com/photo-1633505584501-f1ebbd15cd47?auto=format&fit=crop&q=80&w=800"),
        ("creta_g2", "Creta G2 (2022+)", "Design exótico e tecnologias ADAS.", "https://images.unsplash.com/photo-1633505584501-f1ebbd15cd47?auto=format&fit=crop&q=80&w=800"),
        ("tucson_g1", "Tucson G1 (2005-2017)", "Eterno SUV guerreiro da Hyundai.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("ix35", "ix35 (2011-2022)", "Substituto de sucesso do Tucson.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800")
    ],
    "Toyota": [
        ("corolla_brad", "Corolla G9 'Brad' (2003-2008)", "O imortal 1.8 16V VVT-i.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("corolla_g10", "Corolla G10 (2009-2014)", "Evolução do conforto e durabilidade.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("corolla_g11", "Corolla G11 (2015-2019)", "Introdução do câmbio CVT espetacular.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("corolla_g12", "Corolla G12 / Hybrid (2020+)", "Primeiro híbrido flex do mundo.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("hilux_g7", "Hilux G7 3.0 Diesel (2005-2015)", "Geração blindada pelo tempo.", "https://images.unsplash.com/photo-1593055462551-7efd6e245a4a?auto=format&fit=crop&q=80&w=800"),
        ("hilux_g8", "Hilux G8 2.8 Diesel (2016+)", "Conforto e confiabilidade sem igual.", "https://images.unsplash.com/photo-1593055462551-7efd6e245a4a?auto=format&fit=crop&q=80&w=800"),
        ("yaris", "Yaris 1.3/1.5 (2018+)", "Substituto de luxo do Etios.", "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&q=80&w=800"),
        ("etios", "Etios 1.3/1.5 (2012-2021)", "Visual polêmico, mas mecânica perfeita.", "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&q=80&w=800")
    ],
    "Honda": [
        ("civic_g8", "New Civic G8 (2007-2011)", "Design futurista com painel de 2 andares.", "https://images.unsplash.com/photo-1532986422792-7efc90066b26?auto=format&fit=crop&q=80&w=800"),
        ("civic_g9", "Civic G9 (2012-2016)", "Evolução suave e muito confortável.", "https://images.unsplash.com/photo-1532986422792-7efc90066b26?auto=format&fit=crop&q=80&w=800"),
        ("civic_g10", "Civic G10 1.5T/2.0 (2017-2022)", "Auge do sedã esportivo, porta-malas maior.", "https://images.unsplash.com/photo-1532986422792-7efc90066b26?auto=format&fit=crop&q=80&w=800"),
        ("hrv_g1", "HR-V G1 1.8 (2016-2022)", "Revolucionou a categoria dos SUVs.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("hrv_g2", "HR-V G2 1.5/1.5T (2023+)", "A nova e sofisticada geração.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("fit_g1", "Fit G1 (2004-2008)", "Versátil e extremamente econômico.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("fit_g2", "Fit G2 (2009-2014)", "Design arredondado e muito espaçoso.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("fit_g3", "Fit G3 (2015-2021)", "Última fase do ícone no Brasil.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("city", "City G2/G3 1.5 (2009-2022)", "Sedã de entrada para família.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800")
    ],
    "Jeep": [
        ("renegade_g1", "Renegade 1.8 E.TorQ (2015-2021)", "O sucesso do design icônico quadrado.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("renegade_g2", "Renegade 1.3 Turbo T270 (2022+)", "Adoção de turbocompressor fortíssimo.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("compass_g2", "Compass 2.0 Flex/Diesel (2017-2021)", "O maior case de sucesso de vendas SUV.", "https://images.unsplash.com/photo-1633505584501-f1ebbd15cd47?auto=format&fit=crop&q=80&w=800"),
        ("compass_g3", "Compass 1.3T/2.0D (2022+)", "Painel digital e interior refinado.", "https://images.unsplash.com/photo-1633505584501-f1ebbd15cd47?auto=format&fit=crop&q=80&w=800")
    ],
    "Nissan": [
        ("kicks_g1", "Kicks 1.6 HR16DE (2017-2020)", "Crossover leve, econômico com teto flutuante.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("kicks_g2", "Kicks 1.6 Facelift (2021+)", "Nova grade frontal marcante.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("versa_g1", "Versa G1 V-Drive (2012-2020)", "Conhecido pelo espaço traseiro de limusine.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("versa_g2", "Novo Versa G2 (2021+)", "Beleza e aerodinâmica superiores.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("frontier_g12", "Frontier 2.5 Diesel (2008-2016)", "Picape de força e durabilidade Nissan.", "https://images.unsplash.com/photo-1559404047-927b5e43a8ce?auto=format&fit=crop&q=80&w=800"),
        ("frontier_g13", "Frontier 2.3 Biturbo (2017+)", "Chassi em C e suspensão multilink.", "https://images.unsplash.com/photo-1559404047-927b5e43a8ce?auto=format&fit=crop&q=80&w=800")
    ],
    "Renault": [
        ("kwid", "Kwid 1.0 (2018+)", "Subcompacto e queridinho de frotas.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("duster_g1", "Duster G1 1.6/2.0 (2012-2020)", "O tanque francês/romeno robusto.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("duster_g2", "Duster G2 1.6/1.3T (2021+)", "Maturidade de projeto com muita tecnologia.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("sandero_g1", "Sandero G1 (2008-2014)", "Primeira geração de extremo espaço interno.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("sandero_g2", "Sandero G2 / Stepway (2015-2022)", "Mais tecnologia e câmbio CVT (em algumas versões).", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("logan_g1", "Logan G1 (2008-2013)", "Pioneiro da revolução de sedãs enormes.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800"),
        ("logan_g2", "Logan G2 (2014+)", "Visual reformulado com traços europeus.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800")
    ]
}

categories = {
    "Óleo e Fluidos": [
        {"name": "Óleo de Motor 5W30 Sintético", "brands": {"ACDelco": "98550168", "Mobil": "Super 3000 5W30", "Castrol": "Magnatec 5W30", "Motul": "8100 5W30", "Lubrax": "Valora 5W30", "Shell": "Helix HX8 5W30"}},
        {"name": "Óleo de Motor 15W40 Mineral", "brands": {"ACDelco": "98550160", "Mobil": "Super 1000", "Castrol": "GTX 15W40", "Lubrax": "Essencial 15W40"}},
        {"name": "Fluido de Arrefecimento", "brands": {"Paraflu": "Bio Orgânico", "Radiex": "R-1922", "Tirreno": "Original", "Delphi": "RL10012"}},
        {"name": "Fluido de Freio DOT 4", "brands": {"Varga": "DOT4", "Bosch": "DOT 4 500ml", "Controil": "C-200", "ATE": "SL DOT4"}},
        {"name": "Óleo de Câmbio", "brands": {"Isafluid": "556", "Ipiranga": "Ipiranga Gear", "Petronas": "Tutela"}},
        {"name": "Fluido de Direção Hidráulica", "brands": {"ACDelco": "Dexron III", "Texaco": "Texamatic", "Petronas": "Tutela GI/A"}}
    ],
    "Filtros": [
        {"name": "Filtro de Óleo", "brands": {"Tecfil": "PSL", "Mann": "W712", "Fram": "PH47", "Hengst": "H90W", "Mahle": "OC90", "Wega": "WO"}},
        {"name": "Filtro de Ar do Motor", "brands": {"Tecfil": "ARL", "Fram": "CA", "Mann": "C29", "Wega": "FAP", "Bosch": "0986B"}},
        {"name": "Filtro de Combustível", "brands": {"Tecfil": "GI0", "Bosch": "0986B", "Mann": "WK", "Fram": "G10", "Mahle": "KL"}},
        {"name": "Filtro de Cabine (A/C)", "brands": {"Tecfil": "ACP", "Filtros Mil": "FC", "Mann": "CU", "Wega": "AKX", "Bosch": "0986B"}}
    ],
    "Motor": [
        {"name": "Vela de Ignição", "brands": {"NGK": "BPR", "Bosch": "SP", "Denso": "W20", "Champion": "RN"}},
        {"name": "Cabo de Vela", "brands": {"NGK": "SC", "Bosch": "902", "Magneti Marelli": "CVM", "Delphi": "XS"}},
        {"name": "Bobina de Ignição", "brands": {"Bosch": "F00", "Delphi": "CE", "Magneti Marelli": "BI", "NGK": "U2"}},
        {"name": "Correia Dentada", "brands": {"Gates": "408", "Contitech": "CT", "Dayco": "111", "ACDelco": "193"}},
        {"name": "Bomba de Óleo", "brands": {"Schadek": "10.0", "Brosol": "BO", "Anroi": "AT"}},
        {"name": "Coxim do Motor", "brands": {"Axios": "044", "Mobensani": "MB", "Sampel": "302"}}
    ],
    "Arrefecimento": [
        {"name": "Bomba d'Água", "brands": {"Urba": "UB", "Nakata": "NK", "Indisa": "15", "Schadek": "20.0"}},
        {"name": "Radiador", "brands": {"Visconde": "RV", "Denso": "BC", "Notus": "NT"}},
        {"name": "Válvula Termostática", "brands": {"Wahler": "314", "MTE-Thomson": "VT", "Iguaçu": "401"}}
    ],
    "Freios": [
        {"name": "Pastilha de Freio Dianteira", "brands": {"Cobreq": "N-", "Fras-le": "PD/", "Syl": "10", "Bosch": "0986", "Willtec": "PW"}},
        {"name": "Disco de Freio Dianteiro", "brands": {"Fremax": "BD", "Hipper Freios": "HF", "TRW": "DF", "MDS": "D"}},
        {"name": "Tambor de Freio Traseiro", "brands": {"Fremax": "BD", "Hipper Freios": "HF", "TRW": "TB"}},
        {"name": "Lona de Freio", "brands": {"Fras-le": "CB/", "Cobreq": "L-", "Syl": "L"}}
    ],
    "Suspensão": [
        {"name": "Amortecedor Dianteiro", "brands": {"Monroe": "273", "Cofap": "GP", "Nakata": "HG", "Kayaba": "KYB", "Corven": "CV"}},
        {"name": "Amortecedor Traseiro", "brands": {"Monroe": "273", "Cofap": "GB", "Nakata": "HG"}},
        {"name": "Bandeja de Suspensão", "brands": {"Nakata": "NB", "Perfect": "BR", "Grazzimetal": "GZ"}},
        {"name": "Pivô de Suspensão", "brands": {"Nakata": "N1", "Viemar": "V1", "Driveway": "PI"}},
        {"name": "Bieleta", "brands": {"Nakata": "N10", "Viemar": "V10", "Axios": "044"}}
    ],
    "Direção": [
        {"name": "Terminal de Direção", "brands": {"Nakata": "N101", "Viemar": "V101", "Driveway": "TD"}},
        {"name": "Barra Axial", "brands": {"Nakata": "N102", "Viemar": "V102", "Driveway": "BA"}}
    ],
    "Transmissão": [
        {"name": "Kit Embreagem", "brands": {"Luk": "619", "Sachs": "655", "Valeo": "826"}},
        {"name": "Junta Homocinética", "brands": {"Nakata": "NJH", "Spicer": "SP", "Perfect": "JH"}},
        {"name": "Trizeta", "brands": {"Nakata": "NT", "Spicer": "ST", "Perfect": "TR"}}
    ],
    "Elétrica": [
        {"name": "Bateria", "brands": {"Moura": "M60", "Heliar": "HG", "Bosch": "S5", "Zetta": "Z", "ACDelco": "60Ah"}},
        {"name": "Alternador", "brands": {"Bosch": "F00", "Valeo": "VA", "Delphi": "DL"}},
        {"name": "Lâmpada H4", "brands": {"Osram": "641", "Philips": "123", "Gauss": "GL"}},
        {"name": "Sensor de Nível (Boia)", "brands": {"TSA": "T1", "DS": "21", "VDO": "22"}}
    ],
    "Escapamento": [
        {"name": "Silencioso Traseiro", "brands": {"Mastra": "GM", "Tuper": "TP", "Sicap": "SC"}},
        {"name": "Sonda Lambda", "brands": {"Bosch": "025", "NTK": "OZA", "MTE-Thomson": "88", "Delphi": "ES"}}
    ],
    "Acessórios": [
        {"name": "Palheta do Limpador", "brands": {"Bosch": "Aero", "Dyna": "DX", "Valeo": "V1", "Vetor": "PV"}}
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

# Define prefixes by brand for originality
brand_code_prefixes = {
    "Chevrolet": "GM",
    "Fiat": "FIAT",
    "Volkswagen": "VW",
    "Ford": "FORD",
    "Hyundai": "HY",
    "Toyota": "TOY",
    "Honda": "HND",
    "Jeep": "JEEP",
    "Nissan": "NIS",
    "Renault": "REN"
}

def generate_base_code(car_idx, part_idx, cat_idx, brand):
    prefix = brand_code_prefixes.get(brand, "COD")
    return f"{prefix} {10000000 + (car_idx * 1000000) + (cat_idx * 10000) + part_idx * 17}"

for car_idx, car in enumerate(cars):
    brand = car["brand"]
    
    for cat_idx, (category_name, items) in enumerate(categories.items()):
        for part_idx, item in enumerate(items):
            compatibles = []
            for comp_brand, code in item["brands"].items():
                if category_name == "Óleo e Fluidos":
                    variant_code = code # Keep global oil codes realistic
                else:
                    # Randomize slightly based on car and part to mimic real variations
                    # But if the user edits data.js later, they will maintain the structure
                    variant_code = f"{code}{car_idx*7 + part_idx*3 + 120}"
                compatibles.append({"brand": comp_brand, "code": variant_code})
            
            # Select 1-3 compatible cars
            compatible_cars_names = []
            if category_name in ["Óleo e Fluidos", "Bateria", "Lâmpada H4"]:
                # Generic parts fit many cars across brands
                all_other_cars = [c["name"] for c in cars if c["name"] != car["name"]]
                compatible_cars_names = random.sample(all_other_cars, min(len(all_other_cars), random.randint(3, 6)))
            else:
                # Specific parts usually fit similar cars of the same brand
                same_brand_cars = [c for c in brand_models[brand] if c != car["name"]]
                if same_brand_cars:
                    compatible_cars_names = random.sample(same_brand_cars, min(len(same_brand_cars), random.randint(1, 2)))

            part = {
                "name": item["name"],
                "category": category_name,
                "originalCode": generate_base_code(car_idx, part_idx, cat_idx, brand),
                "compatibles": compatibles,
                "compatibleCars": compatible_cars_names
            }
            car["parts"].append(part)

header_comments = """// =========================================================================
// BANCO DE DADOS DE PEÇAS E VEÍCULOS - AUTOPARTS PRO
// =========================================================================
// Este arquivo armazena todos os veículos e peças do sistema.
// É uma base estática e completa, com separação de montadoras e gerações.
//
// PARA ADICIONAR UM NOVO VEÍCULO:
// Basta ir ao final do array "database" (ou procurar a marca), e copiar
// um objeto { id: "...", brand: "...", name: "...", parts: [...] }.
//
// PARA ADICIONAR UMA NOVA PEÇA EM UM CARRO EXISTENTE:
// Localize o carro (ex: "Onix G1") e vá até a lista "parts". Adicione
// um novo objeto com { name, category, originalCode, compatibles, compatibleCars }.
// =========================================================================

"""

js_content = header_comments + "const database = " + json.dumps(cars, indent=4, ensure_ascii=False) + ";\n\nwindow.database = database;\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
