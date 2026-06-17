---
slug: "ivs"
url: "/mobilnisite/slovnik/ivs/"
type: "slovnik"
title: "IVS – In-Vehicle System"
date: 2026-01-01
abbr: "IVS"
fullName: "In-Vehicle System"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ivs/"
summary: "In-Vehicle System (IVS) je terminál a přidružené podsystémy instalované ve vozidle pro podporu nouzové služby eCall. Umožňuje automatické nebo manuální zahájení nouzového volání a přenos kritických da"
---

IVS je terminál a přidružené podsystémy instalované ve vozidle pro podporu nouzové služby eCall prostřednictvím zahájení nouzového volání a přenosu kritických dat, jako je poloha.

## Popis

In-Vehicle System (IVS) je komplexní vozidlový terminál definovaný standardy 3GPP pro podporu celoevropské nouzové služby eCall a jejích odvozenin. Jedná se o fyzickou a logickou entitu integrovanou ve vozidle, která je zodpovědná za detekci vážné nehody (prostřednictvím senzorů, jako je aktivace airbagu nebo nárazové senzory) nebo umožňuje manuální spuštění posádkou. Po aktivaci IVS naváže okruhově přepínané hlasové volání k nejbližšímu tísňovému přijímacímu centru (PSAP) přes mobilní síť. Zásadní je, že také přenáší tzv. Minimální soubor dat ([MSD](/mobilnisite/slovnik/msd/)), standardizovaný datový paket obsahující klíčové informace, jako je přesná poloha vozidla (z [GNSS](/mobilnisite/slovnik/gnss/)), identifikační číslo vozidla (VIN), typ paliva, počet cestujících a čas události. Tento MSD je odeslán buď v pásmu jako modemový signál během fáze navazování hovoru (pomocí modemových tónů v pásmu), nebo mimopásmově pomocí SMS nebo paketových dat, v závislosti na možnostech sítě a regionální implementaci.

Z architektonického hlediska IVS integruje několik klíčových komponent: mobilní modem (podporující 2G, 3G nebo 4G pro původní eCall), přijímač globálního navigačního satelitního systému (GNSS) pro určení polohy, rozhraní pro akcelerometr nebo nárazový senzor, mikrofon a reproduktor pro hlasovou komunikaci a řídicí jednotku, která spravuje celý postup nouzového volání. Systém musí být odolný, často disponuje záložním napájením, aby zajistil provoz i při výpadku hlavního zdroje vozidla. Jeho činnost je vysoce automatizovaná; po detekci vážné nehody spustí sekvenci volání bez nutnosti lidského zásahu, ačkoli obvykle obsahuje tlačítko pro manuální přerušení nebo zrušení pro posádku.

V širším ekosystému eCall IVS komunikuje s mobilní sítí (např. GSM/UMTS/LTE), která směruje nouzové volání a data na příslušné PSAP. Role IVS je striktně definována jako koncový bod na straně vozidla. Standardizace IVS a formátu MSD zajišťuje interoperabilitu mezi různými výrobci vozidel, mobilními sítěmi a systémy PSAP v celé Evropě a dalších přijímajících regionech, čímž vytváří bezproblémový automatizovaný mechanismus pro nouzovou reakci, který významně zkracuje dobu potřebnou k příjezdu pomoci na místo nehody.

## K čemu slouží

IVS byl vytvořen, aby řešil kritický problém zpožděných dob reakce na tísňová volání po dopravních nehodách, které jsou celosvětově hlavní příčinou úmrtí a vážných zranění. Před zavedením eCall a standardizovaného IVS závisla nouzová volání výhradně na tom, zda jsou osoby ve vozidle při vědomí a schopné sdělit svou polohu, což je při vážných nehodách často nemožné. To vedlo k významným prodlevám při lokalizaci místa nehody a vyslání příslušných záchranných služeb. Primárním motivem byla automatizace procesu nouzového hlášení, která zajistí okamžité přivolání pomoci s přesnými údaji o poloze, čímž zachraňuje životy a snižuje závažnost zranění.

Vývoj IVS byl hnán iniciativou Evropské unie, která vyústila v povinnost vybavit touto technologií všechny nové typy vozidel v EU. 3GPP standardizovalo IVS tak, aby využívalo stávající všudypřítomné mobilní sítě jako přenosové médium, a vyhnulo se tak potřebě samostatné vyhrazené rádiové sítě pro tísňová volání. Tento přístup poskytl široké pokrytí a spolehlivost. IVS řeší omezení předchozích ad-hoc nebo proprietárních systémů pro tísňová volání ve vozidlech vytvořením jednotného celoevropského standardu. Tím je zajištěno, že jakékoli vozidlo vybavené eCall se může spojit s jakýmkoli PSAP v kterékoliv členské zemi, čímž se překonávají bariéry interoperability, které by existovaly u mnoha nekompatibilních systémů specifických pro jednotlivé výrobce.

## Klíčové vlastnosti

- Automatická detekce nehody a spuštění pomocí integrovaných vozidlových senzorů
- Manuální zahájení nouzového volání pomocí vyhrazeného tlačítka
- Přenos standardizovaného Minimálního souboru dat (MSD)
- Integrace GNSS pro přesné hlášení polohy vozidla
- Odolný design se záložním napájením
- Podpora pro přenos MSD modemem v pásmu a mimopásmově (SMS/data)

## Definující specifikace

- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TR 22.967** (Rel-19) — eCall Emergency Data Transmission
- **TS 26.267** (Rel-19) — eCall In-band Modem Specification
- **TS 26.268** (Rel-19) — eCall In-band Modem ANSI-C Code
- **TS 26.269** (Rel-19) — eCall In-band Modem Conformance Testing
- **TR 26.967** (Rel-19) — eCall via CTM Suitability Analysis
- **TR 26.969** (Rel-19) — eCall In-band Modem Performance Characterization

---

📖 **Anglický originál a plná specifikace:** [IVS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ivs/)
