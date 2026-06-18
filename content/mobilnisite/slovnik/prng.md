---
slug: "prng"
url: "/mobilnisite/slovnik/prng/"
type: "slovnik"
title: "PRNG – Pseudo Random Number Generator"
date: 2025-01-01
abbr: "PRNG"
fullName: "Pseudo Random Number Generator"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/prng/"
summary: "Kryptografický algoritmus generující posloupnost čísel se statistickými vlastnostmi podobnými skutečné náhodnosti. V zabezpečení 3GPP je zásadní pro vytváření šifrovacích klíčů, autentizačních výzev a"
---

PRNG je kryptografický algoritmus, který generuje posloupnost čísel připomínající skutečnou náhodnost; používá se v zabezpečení 3GPP k vytváření šifrovacích klíčů, autentizačních výzev a inicializačních vektorů.

## Popis

Generátor pseudonáhodných čísel (PRNG) v architektuře zabezpečení 3GPP je deterministický algoritmus, který po inicializaci výchozí hodnotou (seedem) vytváří posloupnost čísel, jež je výpočetně nerozlišitelná od skutečně náhodné posloupnosti. Jeho hlavní funkcí je poskytovat spolehlivý zdroj náhodnosti pro různé kryptografické operace v síti. V systémech 3GPP jsou PRNG implementovány jak v uživatelském zařízení (UE), tak v síťových prvcích, jako je autentizační centrum (AuC) a server domácích účastníků ([HSS](/mobilnisite/slovnik/hss/)). Kvalita a bezpečnost PRNG jsou prvořadé, protože předvídatelný výstup by mohl vést ke kompromitaci šifrovacích klíčů a prolomení bezpečnostních protokolů.

PRNG funguje tak, že přijme seed s vysokou entropií, který je často odvozen od tajných klíčů (jako je dlouhodobý klíč účastníka K) a náhodných hodnot, například nonces nebo čísel sekvencí. Tento seed inicializuje vnitřní stav generátoru. Algoritmus následně aplikuje kryptografické funkce – například hašovací funkce (jako SHA-256) nebo blokové šifry (jako [AES](/mobilnisite/slovnik/aes/)) v určitém režimu činnosti – na tento stav, aby vytvořil výstupní bity. Tyto výstupní bity tvoří pseudonáhodná čísla používaná v bezpečnostních procedurách. Například v protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) používá AuC PRNG ke generování náhodné výzvy ([RAND](/mobilnisite/slovnik/rand/)) a v kombinaci s klíčem K k výpočtu očekávané odpovědi ([XRES](/mobilnisite/slovnik/xres/)) a šifrovacích/integritních klíčů ([CK](/mobilnisite/slovnik/ck/)/[IK](/mobilnisite/slovnik/ik/)).

Z architektonického hlediska není PRNG samostatný síťový uzel, ale softwarový nebo hardwarový modul zabudovaný do bezpečnostně kritických funkcí. Jeho role je zásadní pro mechanismy ochrany důvěrnosti a integrity definované ve specifikacích jako TS 33.401. Používá se ke generování šifrovacího proudu pro šifrovací algoritmy (např. SNOW 3G, AES, ZUC), k vytváření inicializačních vektorů ([IV](/mobilnisite/slovnik/iv/)) pro šifrování a k produkci dočasných identifikátorů. Bezpečnostní síla závisí na nepředvídatelnosti seedu, velikosti vnitřního stavu a kryptografické odolnosti podkladového algoritmu. Specifikace 3GPP často nařizují nebo doporučují konkrétní schválené algoritmy, například ty definované národními nebo mezinárodními normalizačními orgány (jako NIST), aby zajistily interoperabilitu a vysokou úroveň ochrany proti útokům.

## K čemu slouží

PRNG existuje, aby uspokojil kritickou potřebu bezpečného a spolehlivého zdroje náhodnosti v digitálních celulárních systémech. Kryptografické protokoly zásadně vyžadují náhodná čísla pro klíče, nonces a výzvy, aby zajistily, že bezpečnost nebude ohrožena předvídatelností. Bez kryptograficky bezpečného PRNG by mohlo být šifrování slabé, autentizační protokoly by mohly být náchylné k opakovaným útokům a celková bezpečnost systému by byla iluzorní. Motivací pro jeho standardizaci v rámci 3GPP bylo poskytnout konzistentní, kvalitní zdroj náhodnosti, který mohou implementovat všechny kompatibilní síťové prvky a zařízení, a zajistit tak bezpečnost od konce do konce v síťích více dodavatelů po celém světě.

Historicky časné digitální systémy někdy používaly nekvalitní zdroje entropie nebo jednoduché lineární kongruenciální generátory, které byly zranitelné analýzou. Začlenění standardizovaných požadavků na PRNG v 3GPP, zejména vylepšených ve verzi 8 se specifikacemi System Architecture Evolution (SAE) a EPS zabezpečení, řešilo omezení ad-hoc implementací. Poskytlo jasný rámec pro generování náhodnosti potřebné pro silnější a delší klíče vyžadované pokročilými šifrovacími algoritmy, jako je AES-256. To bylo obzvláště důležité, když sítě začaly přenášet citlivá data a služby, přesahující hlasové spojení k zahrnutí mobilního bankovnictví, podnikového přístupu a vládní komunikace.

PRNG řeší problém generování tajemství v deterministickém výpočetním prostředí, kde je obtížné získat skutečnou náhodnost. Umožňuje vytváření jedinečných relakových klíčů pro každé spojení, čímž zajišťuje předpokládané utajení a ochranu proti hromadnému dešifrování. Jeho účel sahá až k ochraně soukromí uživatelů generováním dočasných identifikátorů (jako GUTI), které brání sledování. Snaha o silnější PRNG je kontinuální, motivovaná rostoucí výpočetní silou dostupnou útočníkům a potřebou kvantově odolné kryptografie v budoucích vydáních.

## Klíčové vlastnosti

- Deterministický algoritmus produkující statisticky náhodné posloupnosti z tajného seedu
- Základní pro generování šifrovacích klíčů (CK, IK), autentizačních výzev (RAND) a inicializačních vektorů
- Implementován jak v UE, tak v síťových bezpečnostních modulech (AuC, HSS, MME)
- Založen na kryptografických primitivech, jako jsou hašovací funkce nebo blokové šifry
- Kritický pro zajištění nepředvídatelnosti a síly protokolů 3GPP AKA
- Podléhá přísným bezpečnostním požadavkům, aby se zabránilo předvídatelnosti a vyčerpání entropie

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [RAND – RANDom number (authentication parameter)](/mobilnisite/slovnik/rand/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [PRNG na 3GPP Explorer](https://3gpp-explorer.com/glossary/prng/)
