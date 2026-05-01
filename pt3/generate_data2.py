import json
import random

cars_def = {
    "Chevrolet": [
        ("onix", "Onix 1.0/1.4", "Hatchback popular e econômico.", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&q=80&w=800"),
        ("celta", "Celta 1.0", "Hatch compacto e robusto.", "https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?auto=format&fit=crop&q=80&w=800"),
        ("tracker", "Tracker 1.0/1.2 Turbo", "SUV compacto moderno.", "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&q=80&w=800"),
        ("s10", "S10 2.8 Diesel", "Picape média para trabalho pesado.", "https://images.unsplash.com/photo-1559404047-927b5e43a8ce?auto=format&fit=crop&q=80&w=800"),
        ("cruze", "Cruze 1.4 Turbo", "Sedã médio tecnológico.", "https://images.unsplash.com/photo-1550346338-71e860bc8153?auto=format&fit=crop&q=80&w=800")
    ],
    "Fiat": [
        ("palio", "Palio Fire 1.0", "Carro popular clássico no Brasil.", "https://images.unsplash.com/photo-1542362567-b07e54358753?auto=format&fit=crop&q=80&w=800"),
        ("uno", "Uno Mille / Vivace", "Econômico e ágil para a cidade.", "https://images.unsplash.com/photo-1502877338535-766e1452684a?auto=format&fit=crop&q=80&w=800"),
        ("argo", "Argo 1.0/1.3", "Hatch com design moderno.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("strada", "Strada 1.4/1.3", "Picape leve mais vendida.", "https://images.unsplash.com/photo-1563720223185-11003d516935?auto=format&fit=crop&q=80&w=800"),
        ("toro", "Toro 1.8/2.0 Diesel", "Picape intermediária versátil.", "https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?auto=format&fit=crop&q=80&w=800")
    ],
    "Volkswagen": [
        ("gol", "Gol 1.0/1.6", "Líder de vendas histórico.", "https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?auto=format&fit=crop&q=80&w=800"),
        ("fox", "Fox 1.0/1.6", "Hatch de teto alto e espaçoso.", "https://images.unsplash.com/photo-1542282088-fe8426682b8f?auto=format&fit=crop&q=80&w=800"),
        ("polo", "Polo 1.0 TSI", "Hatch premium esportivo.", "https://images.unsplash.com/photo-1583121274602-3e2820c69888?auto=format&fit=crop&q=80&w=800"),
        ("saveiro", "Saveiro 1.6", "Picape leve derivada do Gol.", "https://images.unsplash.com/photo-1559416523-140ddc3d238c?auto=format&fit=crop&q=80&w=800"),
        ("amarok", "Amarok V6", "Picape média potente.", "https://images.unsplash.com/photo-1621007947382-d3119ee5c46b?auto=format&fit=crop&q=80&w=800")
    ],
    "Ford": [
        ("ka", "Ka 1.0/1.5", "Hatch econômico da Ford.", "https://images.unsplash.com/photo-1550524614-ea0d1f753557?auto=format&fit=crop&q=80&w=800"),
        ("fiesta", "Fiesta 1.5/1.6", "Hatch compacto bem equipado.", "https://images.unsplash.com/photo-1582467029213-ce71667c2e28?auto=format&fit=crop&q=80&w=800"),
        ("ecosport", "EcoSport 1.5/2.0", "Pioneiro dos SUVs compactos.", "https://images.unsplash.com/photo-1553440569-bcc63803a83d?auto=format&fit=crop&q=80&w=800"),
        ("ranger", "Ranger 2.2/3.2", "Picape média forte e bruta.", "https://images.unsplash.com/photo-1609521263047-f8f205293f24?auto=format&fit=crop&q=80&w=800")
    ],
    "Hyundai": [
        ("hb20", "HB20 1.0/1.6", "Hatch popular com belo design.", "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&q=80&w=800"),
        ("creta", "Creta 1.6/2.0", "SUV compacto espaçoso.", "https://images.unsplash.com/photo-1633505584501-f1ebbd15cd47?auto=format&fit=crop&q=80&w=800")
    ],
    "Toyota": [
        ("corolla", "Corolla 2.0 / Hybrid", "O sedã médio mais confiável.", "https://images.unsplash.com/photo-1590362891991-f776e747a588?auto=format&fit=crop&q=80&w=800"),
        ("hilux", "Hilux 2.8 Diesel", "Picape indestrutível e líder.", "https://images.unsplash.com/photo-1593055462551-7efd6e245a4a?auto=format&fit=crop&q=80&w=800")
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
        {"name": "Filtro de Cabine", "brands": {"Tecfil": "ACP", "Filtros Mil": "FC", "Mann": "CU", "Wega": "AKX", "Bosch": "0986B"}}
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
    "Toyota": "TOY"
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
                    variant_code = f"{code}{car_idx*7 + part_idx*3 + 120}"
                compatibles.append({"brand": comp_brand, "code": variant_code})
            
            # Select 1-3 compatible cars (mostly from the same brand to be realistic, or generic if Oil)
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

js_content = "const database = " + json.dumps(cars, indent=4, ensure_ascii=False) + ";\n\nwindow.database = database;\n"

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)
