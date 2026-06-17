---
slug: "dpkk"
url: "/mobilnisite/slovnik/dpkk/"
type: "slovnik"
title: "DPKK – MCData Payload Protection Key"
date: 2025-01-01
abbr: "DPKK"
fullName: "MCData Payload Protection Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dpkk/"
summary: "Kryptografický klíč používaný ve službách Mission Critical Data (MCData) k šifrování a ochraně užitečného obsahu datových komunikací. Zajišťuje důvěrnost a integritu citlivých dat vyměňovaných mezi už"
---

DPKK je kryptografický klíč používaný ve službách Mission Critical Data k šifrování a ochraně užitečného obsahu datových komunikací, zajišťující důvěrnost a integritu pro citlivá provozní data.

## Popis

MCData Payload Protection Key (DPKK) je bezpečnostní klíč definovaný v rámci standardů 3GPP, konkrétně v TS 24.582, pro ochranu užitečného obsahu dat ve službách Mission Critical Data. Funguje v rámci bezpečnostní architektury pro služby [MCX](/mobilnisite/slovnik/mcx/) (Mission Critical Communication), které jsou navrženy pro komunikace veřejné bezpečnosti a kritické infrastruktury. DPKK je generován a spravován jako součást hierarchie klíčů, často odvozený z klíčů vyšší úrovně, jako je MCData Service Key (DSK) nebo jiné autentizační údaje, aby poskytoval vyhrazený klíč pro šifrování skutečného obsahu (užitečného zatížení) datových zpráv, souborů nebo jiných datových přenosů. Tím je zajištěno, že citlivé informace, jako jsou polohová data, obrázky nebo textové zprávy, zůstanou během výměny přes sítě 3GPP důvěrné a chráněné proti neoprávněným změnám.

V praxi je DPKK aplikován pomocí standardizovaných šifrovacích algoritmů, jako je [AES](/mobilnisite/slovnik/aes/) (Advanced Encryption Standard), k zabezpečení užitečného obsahu před přenosem. Klíč je typicky vytvořen během fází autorizace služby a nastavení relace, kdy koncové body (např. uživatelské zařízení nebo servery) provádějí autentizaci a vyjednávají bezpečnostní parametry. DPKK spolupracuje s dalšími bezpečnostními mechanismy, jako je ochrana integrity a identifikátory klíčů (např. [DPKK-ID](/mobilnisite/slovnik/dpkk-id/)), a vytváří tak komplexní bezpečnostní vrstvu. Jeho použití je ve scénářích MCData povinné, aby byly splněny vysoké bezpečnostní požadavky komunikací veřejné bezpečnosti, které brání odposlechu a neoprávněnému přístupu.

Role DPKK přesahuje pouhé šifrování; integruje se s celkovým bezpečnostním rámcem MCData, který zahrnuje protokoly pro správu klíčů, distribuci klíčů a správu jejich životního cyklu (např. vypršení platnosti a obnovení klíče). Tím je zajištěno, že ochrana užitečného obsahu se přizpůsobuje dynamickým síťovým podmínkám a hrozbám. Izolací šifrování užitečného obsahu od ostatních bezpečnostních funkcí umožňuje DPKK efektivní a škálovatelné implementace zabezpečení, podporující různé aplikace MCData, jako je skupinová komunikace, přenos souborů a datové streamování v kritických scénářích.

## K čemu slouží

DPKK byl zaveden, aby řešil potřebu robustního zabezpečení užitečného obsahu ve službách Mission Critical Data, které využívají orgány veřejné bezpečnosti, záchranné složky a provozovatelé kritické infrastruktury. Před jeho standardizací se datové komunikace v kritických scénářích často spoléhaly na méně specializovaná bezpečnostní opatření nebo proprietární řešení, která mohla být zranitelná vůči útokům nebo postrádala interoperabilitu. Vytvoření DPKK jako součásti 3GPP Release 14 bylo motivováno rostoucím nasazením sítí LTE a 5G pro aplikace kritické pro plnění mise, které vyžadovaly standardizované šifrování s vysokou mírou jistoty pro ochranu citlivého užitečného obsahu dat před zachycením a manipulací.

Klíčový problém, který DPKK řeší, je zajištění end-to-end důvěrnosti a integrity pro data vyměňovaná v relacích MCData, což je zásadní pro provozní bezpečnost a soukromí. Bez takového vyhrazeného klíče by mohl být užitečný obsah během přenosu vystaven hrozbám, což by ohrozilo efektivitu mise. DPKK poskytuje standardizovaný přístup, který se integruje do širší bezpečnostní architektury 3GPP, umožňuje bezproblémovou interoperabilitu mezi různými dodavateli a sítěmi a podporuje dodržování regulatorních požadavků pro komunikace veřejné bezpečnosti.

## Klíčové vlastnosti

- Poskytuje šifrování užitečného obsahu MCData pomocí algoritmů jako je AES
- Odvozen z klíčů vyšší úrovně v bezpečnostní hierarchii MCData
- Zajišťuje důvěrnost a integritu datových přenosů
- Integruje se s protokoly správy klíčů pro řízení životního cyklu
- Podporuje interoperabilitu v komunikacích veřejné bezpečnosti a kritických komunikacích
- Spolupracuje s DPKK-ID pro identifikaci a správu klíčů

## Související pojmy

- [DPKK-ID – MCData Payload Protection Key Identifier](/mobilnisite/slovnik/dpkk-id/)

## Definující specifikace

- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols

---

📖 **Anglický originál a plná specifikace:** [DPKK na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpkk/)
