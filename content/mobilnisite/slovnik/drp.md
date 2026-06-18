---
slug: "drp"
url: "/mobilnisite/slovnik/drp/"
type: "slovnik"
title: "DRP – Eardrum Reference Point"
date: 2025-01-01
abbr: "DRP"
fullName: "Eardrum Reference Point"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/drp/"
summary: "Standardizovaný akustický referenční bod definovaný 3GPP pro testování akustiky koncových zařízení. Představuje teoretický bod u vstupu do zvukovodu (simulující polohu bubínku) používaný k měření a sp"
---

DRP je standardizovaný akustický referenční bod u vstupu do zvukovodu používaný organizací 3GPP pro měření metrik akustického výkonu, jako je hlasitost a frekvenční charakteristika, v mobilních zařízeních.

## Popis

Referenční bod bubínku (DRP) je klíčový, standardizovaný koncept ve specifikacích 3GPP pro akustické testování uživatelských zařízení (UE), jako jsou mobilní telefony a sluchátka. Nejde o fyzický bod na zařízení, ale o přesně definovanou teoretickou polohu uvnitř akustické testovací přípravku, konkrétně umělého ucha nebo simulátoru hlavy a trupu ([HATS](/mobilnisite/slovnik/hats/)). DRP je definován jako bod umístěný 25 mm od referenční roviny na konkrétním simulátoru ucha (jako jsou simulátory dle [IEC](/mobilnisite/slovnik/iec/) 60318-4 nebo [ITU-T](/mobilnisite/slovnik/itu-t/) P.57), který modeluje polohu lidského bubínku. To umožňuje reprodukovatelná a srovnatelná akustická měření napříč různými laboratořemi a výrobci zařízení.

V praxi je během testování reproduktor (receiver) mobilního zařízení akusticky spojen s umělým uchem. Mikrofon uvnitř tohoto umělého ucha je umístěn a kalibrován tak, aby jeho měřicí bod odpovídal definovanému DRP. Při testování charakteristik vysílání (send) se používá umělá ústa (reproduktor) k vytváření zvuku z definované pozice vůči mikrofonu zařízení a výsledný elektrický signál je analyzován. DRP slouží jako počátek pro definování akustické dráhy. Klíčové metriky výkonu jsou hodnoceny vůči tomuto bodu. Například hodnocení hlasitosti přijímače ([RLR](/mobilnisite/slovnik/rlr/)) měří, jak moc je akustický signál utlumen od elektrického vstupu zařízení k hladině akustického tlaku v DRP. Podobně měření sidetonu vyhodnocují dráhu od umělých úst k DRP a zpět k elektrickému výstupu zařízení.

Definice a použití DRP zahrnuje komplexní kalibraci celého testovacího uspořádání, včetně umělého ucha, testovací komory a audio analyzátoru. Specifikace jako 3GPP TS 26.131 a 26.132 poskytují podrobné postupy pro seřízení akustického testovacího přípravku, aby bylo zajištěno správné realizování DRP. To zahrnuje použití kalibrovaných zdrojů zvuku pro ověření frekvenční charakteristiky a citlivosti měřicího mikrofonu v místě DRP. Díky ukotvení všech akustických požadavků k tomuto standardizovanému referenčnímu bodu 3GPP zajišťuje, že zařízení, které projde testy v certifikované laboratoři, bude poskytovat konzistentní a přijatelnou kvalitu zvuku pro koncového uživatele, bez ohledu na vnitřní konstrukci zařízení nebo umístění testovací laboratoře.

## K čemu slouží

DRP byl formálně zaveden ve vydání 3GPP Release 8, aby vyřešil dlouhodobý problém nekonzistentního a neopakovatelného akustického testování mobilních terminálů. Před jeho standardizací výrobci a síťoví operátoři často používali různé referenční body a testovací metody, což vedlo k významným rozdílům v měřeném akustickém výkonu. Zařízení považované v jedné laboratoři za přijatelné mohlo v jiné laboratoři selhat, což způsobovalo problémy s kompatibilitou, špatný uživatelský zážitek a zvýšené náklady na přetestování a přepracování. Nedostatek jednotného referenčního bodu ztěžoval prosazování minimálních standardů kvality zvuku v celém odvětví.

Vytvoření DRP bylo motivováno potřebou objektivních, opakovatelných a globálně harmonizovaných testovacích kritérií. Poskytuje společný 'měřicí nástroj' pro akustická měření. Definováním jediného, přesného referenčního bodu navázaného na mezinárodní standardy (jako jsou ty od [IEC](/mobilnisite/slovnik/iec/) a [ITU-T](/mobilnisite/slovnik/itu-t/)) umožnilo 3GPP vývoj testovacích specifikací, které poskytují konzistentní výsledky. To prospívá všem zúčastněným stranám: výrobci mohou konstruovat zařízení podle jasného cíle, operátoři mohou jednotně ověřovat kvalitu zařízení a koncoví uživatelé zažívají předvídatelnou a odpovídající kvalitu hovorů. DRP je základním kamenem specifikací definujících akustické charakteristiky terminálů (TS 26.131), přenosu okolního hluku (TS 26.132) a souvisejících metrik akustického výkonu, tvořícím základ zajištění kvality hlasu v mobilních sítích.

## Klíčové vlastnosti

- Standardizovaný teoretický bod pro akustické měření simulující polohu lidského bubínku
- Umístěný 25 mm od referenční roviny na specifikovaných simulátorech ucha dle IEC/ITU-T
- Umožňuje reprodukovatelné měření klíčových akustických metrik, jako je hodnocení hlasitosti vysílání (SLR) a hodnocení hlasitosti příjmu (RLR)
- Slouží jako reference pro hodnocení maskování sidetonu (STMR) a dalších parametrů kvality hlasu
- Základní pro kalibraci a seřízení akustických testovacích přípravků (umělých uší)
- Zajišťuje konzistentní testování akustického výkonu terminálů napříč různými laboratořemi a výrobci

## Související pojmy

- [HATS – Head and Torso Simulator](/mobilnisite/slovnik/hats/)

## Definující specifikace

- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.295** (Rel-19) — 3GPP Charging: CDR Transfer via GTP' Protocol

---

📖 **Anglický originál a plná specifikace:** [DRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/drp/)
