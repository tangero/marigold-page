---
slug: "ieidl"
url: "/mobilnisite/slovnik/ieidl/"
type: "slovnik"
title: "IEIDL – Information Element Identifier Data Length"
date: 2025-01-01
abbr: "IEIDL"
fullName: "Information Element Identifier Data Length"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ieidl/"
summary: "Pole protokolu ve specifikacích 3GPP, které definuje délku datové části pro konkrétní informační element (IE). Je základní součástí pro analýzu a konstrukci protokolových zpráv, zajišťuje integritu da"
---

IEIDL je pole protokolu ve specifikacích 3GPP, které definuje délku datové části pro konkrétní informační element, což umožňuje správnou analýzu a konstrukci protokolových zpráv.

## Popis

Information Element Identifier Data Length (IEIDL) je klíčová součást protokolových datových jednotek definovaných v četných technických specifikacích 3GPP. Funguje jako součást strukturovaného schématu kódování typu TLV (Type-Length-Value) nebo podobného, používaného pro informační elementy ([IE](/mobilnisite/slovnik/ie/)). Informační element je samostatný kus dat přenášený v rámci protokolové zprávy, jako je identita uživatele, parametr kvality služby nebo příkaz pro správu relace. Pole IEIDL konkrétně udává velikost části 'Value' IE, která po něm bezprostředně následuje, v oktetech (bytích). Tento indikátor délky je nezbytný pro přijímající entitu, aby mohla správně analyzovat příchozí datový proud. Bez přesné hodnoty IEIDL by síťový uzel nedokázal určit, kde jeden IE končí a druhý začíná, což by vedlo k chybám analýzy, poškození zpráv a potenciálním výpadkům služeb.

Architektura využití IEIDL je zabudována do abstraktní syntaktické notace a pravidel kódování definovaných pro každý protokol. Například v protokolech specifikovaných pomocí ASN.1 (Abstract Syntax Notation One) determinant délky SEQUENCE nebo OCTET STRING často odpovídá konceptu IEIDL při mapování na binární kódování (např. PER, [BER](/mobilnisite/slovnik/ber/)). V jednodušších binárních protokolech je IEIDL explicitně definováno jako pole konkrétní velikosti (např. jeden nebo dva oktety) v rámci struktury hlavičky IE. Délka samotného pole (např. 1 oktet pro délky do 255) je předem definována ve specifikaci. Hodnota obsažená v poli IEIDL určuje, kolik následujících oktetů musí přijímač přečíst a zpracovat jako datovou část pro daný IE.

Jeho role v síti je zásadní pro všechno signalizační provoz na vrstvě 3 a mnohé procedury vrstvy 2. Pokaždé, když se mobilní zařízení připojuje k síti, navazuje hovor nebo provádí předání spojení na novou buňku, jsou mezi UE a sítí (např. [MME](/mobilnisite/slovnik/mme/), SGSN, RNC) vyměněny desítky či stovky IE. IEIDL zajišťuje, že složité datové struktury proměnné délky lze přenášet spolehlivě. Umožňuje rozšiřitelnost protokolů, protože nové IE s novými délkami dat lze zavést v pozdějších vydáních při zachování zpětné kompatibility – starší uzly mohou přeskočit neznámé IE tak, že přečtou IEIDL a zjistí, kolik oktetů mají ignorovat. IEIDL je tedy nenápadným, ale nepostradatelným prvkem umožňujícím robustní, flexibilní a vyvíjející se telekomunikační protokoly.

## K čemu slouží

IEIDL existuje k řešení základního problému přenosu dat proměnné délky v rámci pevně nebo volněji strukturovaných protokolových zpráv. Rané digitální komunikační protokoly často používaly pole pevné délky, což bylo neefektivní pro data, která mohou mít výrazně rozdílnou velikost (např. URL vs. IP adresa). To plýtvalo přenosovou kapacitou u krátkých dat a ukládalo umělá omezení na delší data. Paradigma TLV, využívající explicitní pole délky jako je IEIDL, bylo přijato za účelem zajištění optimální efektivity a flexibility.

K jeho vytvoření vedla potřeba standardizované, jednoznačné metody pro analýzu zpráv napříč mnoha rozhraními v systému 3GPP (např. Lu, S1, [N2](/mobilnisite/slovnik/n2/)). Bez konzistentního indikátoru délky by každý výrobce síťových prvků potřeboval proprietární logiku k dekódování zpráv, čímž by byla zničena interoperabilita. IEIDL tuto konzistenci poskytuje. Řeší omezení předchozích ad-hoc přístupů tím, že činí strukturu zprávy sebe-popisnou; data nesou informaci potřebnou pro svou vlastní interpretaci. To je klíčové pro multi-vendor ekosystém celulárních sítí, kde zařízení od různých výrobců musí komunikovat bezchybně.

Historicky jsou koncepty jako IEIDL zakořeněny v telekomunikačních signalizačních standardech, jako je SS7, a standardech pro datové sítě. 3GPP formalizovalo a zdokonalilo jeho aplikaci napříč celou svou sadou protokolů, od základní sítě po radiový přístup. Řeší problém vývoje protokolů tím, že umožňuje přidávat nové parametry do existujících zpráv bez rozbití stávajících implementací, pokud jsou zachována pravidla pro interpretaci IEIDL. Tato odolnost vůči budoucím změnám je klíčovým důvodem jeho všudypřítomného použití.

## Klíčové vlastnosti

- Definuje přesný počet bajtů datové části informačního elementu.
- Umožňuje analýzu dat proměnné délky v rámci binárních protokolových zpráv.
- Základní pro struktury kódování typu TLV (Type-Length-Value).
- Zajišťuje dopřednou a zpětnou kompatibilitu pro rozšíření protokolů.
- Kritické pro interoperabilitu mezi síťovým zařízením od různých výrobců.
- Specifikováno jako součást základních pravidel kódování protokolu ve specifikacích 3GPP.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 31.115** (Rel-19) — Secured Packet Structure for UICC Applications

---

📖 **Anglický originál a plná specifikace:** [IEIDL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ieidl/)
