---
slug: "lte-v"
url: "/mobilnisite/slovnik/lte-v/"
type: "slovnik"
title: "LTE-V – LTE Vehicle-to-Everything"
date: 2025-01-01
abbr: "LTE-V"
fullName: "LTE Vehicle-to-Everything"
category: "IoT"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/lte-v/"
summary: "LTE-V2X (Vehicle-to-Everything) je standard 3GPP, který adaptuje technologii LTE pro přímou a síťovou komunikaci mezi vozidly (V2V), infrastrukturou (V2I), chodci (V2P) a sítěmi (V2N). Umožňuje kritic"
---

LTE-V je standard 3GPP, který adaptuje technologii LTE pro přímou a síťovou komunikaci vozidlo-se-vším (V2X), a umožňuje tak spoje s nízkou latencí a vysokou spolehlivostí pro aplikace v oblasti bezpečnosti, efektivity provozu a autonomního řízení.

## Popis

LTE-V2X, standardizované jako součást vylepšení LTE v 3GPP, je technologie založená na buňkových sítích navržená pro komunikaci vozidel. Funguje ve dvou komplementárních módech: LTE-V2X Mode 3 (řízený sítí) a LTE-V2X Mode 4 (autonomní neboli sidelink). Mode 3 spoléhá na infrastrukturu buňkové sítě (eNodeB/gNB) pro správu a plánování rádiových zdrojů pro přímou komunikaci vozidlo-vozidlo ([V2V](/mobilnisite/slovnik/v2v/)) nebo vozidlo-infrastruktura (V2I). Základnová stanice přiděluje specifické bloky zdrojů a časování, čímž zajišťuje kontrolovaný interference a kvalitu služeb. Tento mód je optimální pro řízená prostředí s dobrým pokrytím sítě.

Mode 4, charakteristický prvek LTE-V2X, umožňuje přímou komunikaci zařízení-zařízení (sidelink) pomocí rozhraní PC5 bez nutnosti pokrytí sítí. Vozidla autonomně vybírají rádiové zdroje z předkonfigurovaného fondu pomocí distribuovaného plánovacího algoritmu nazvaného Sensing-Based Semi-Persistent Scheduling (SB-SPS). Každé vozidlo snímá kanál, aby identifikovalo nevyužité zdroje, vybere jeden a používá jej semi-persistentně, čímž snižuje pravděpodobnost kolizí. Tento mód podporuje bezpečnostní zprávy s nízkou latencí (např. Basic Safety Messages - BSMs) pro předcházení kolizím, a to i mimo oblasti pokrytí buňkovou sítí, jako jsou tunely nebo venkovské silnice. Fyzická vrstva používá modifikovaný LTE tvar signálu s vylepšenými funkcemi pro vysoké Dopplerovy posuvy a časovou synchronizaci vhodnou pro vysokorychlostní mobilitu.

Z architektonického hlediska se LTE-V2X integruje s Evolved Packet Core (EPC) pro komunikaci V2N, kde vozidla komunikují s aplikačními servery (např. centry řízení dopravy) přes rozhraní Uu. Mezi klíčové síťové funkce patří [V2X](/mobilnisite/slovnik/v2x/) Control Function pro poskytování politik a parametrů. Specifikace (např. 33.185, 33.885) detailně popisují bezpečnostní mechanismy, včetně autentizace založené na certifikátech pro integritu zpráv a soukromí. Úlohou LTE-V2X je poskytovat jednotnou komunikační platformu pro kooperativní inteligentní dopravní systémy (C-ITS), podporující aplikace od varování před nouzovým brzděním a asistence pohybu na křižovatkách až po optimalizaci dopravního proudu a infotainment, čímž tvoří základ pro propojené a automatizované řízení.

## K čemu slouží

LTE-V2X bylo vytvořeno, aby řešilo rostoucí potřebu spolehlivé bezdrátové komunikace s nízkou latencí v prostředí vozidel, což je oblast, kde tradiční buňkové sítě (navržené pro služby zaměřené na člověka) a nebuněčné technologie jako [IEEE](/mobilnisite/slovnik/ieee/) 802.11p měly omezení. Před LTE-V2X bezpečnostní systémy vozidel spoléhaly na senzory (radar, kamery) s omezeným dosahem a schopností vidět za překážky. IEEE 802.11p nabízelo přímou komunikaci, ale čelilo výzvám ve škálovatelnosti, řízení kvality služeb a bezproblémové integraci s rozlehlými sítěmi. LTE-V2X využívá globální ekosystém LTE k poskytnutí standardizovaného, budoucím potřebám odolného řešení, které podporuje jak bezpečnostně kritickou přímou komunikaci, tak síťově vylepšené služby.

Primární problém, který LTE-V2X řeší, je umožnění kooperativního povědomí mezi vozidly, infrastrukturou a dalšími účastníky provozu, aby se předešlo nehodám a zlepšila efektivita dopravy. Poskytuje komunikační páteř pro [V2X](/mobilnisite/slovnik/v2x/) aplikace vyžadující ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)), jako je výměna dat o poloze, rychlosti a trajektorii mnohokrát za sekundu. Jeho vznik byl motivován snahou automobilového průmyslu směřující k propojeným a autonomním vozidlům, která vyžadují robustní, bezpečnou a globálně harmonizovanou technologii. Zapojení 3GPP zajistilo úspory z rozsahu díky využití stávajících nasazení LTE a přidělení spektra.

Dále LTE-V2X řeší evoluci směrem k 5G NR-V2X tím, že vytváří migrační cestu. Nabízí možnosti okamžitého nasazení využívající sítě LTE a zároveň se připravuje na vylepšené funkce v 5G. Technologie také řeší problémy s efektivitou využití spektra prostřednictvím síťově koordinovaného plánování (Mode 3) a inteligentního autonomního výběru zdrojů (Mode 4). Integrací přímé a síťové komunikace poskytuje LTE-V2X komplexní řešení pro různé případy užití V2X, od základní bezpečnosti po pokročilé autonomní řízení, a usnadňuje tak přechod k chytřejším dopravním systémům.

## Klíčové vlastnosti

- Podporuje dva provozní módy: řízený sítí (Mode 3) a autonomní sidelink (Mode 4)
- Využívá rozhraní PC5 pro přímou komunikaci V2V/V2I bez pokrytí sítí
- Používá Sensing-Based Semi-Persistent Scheduling (SB-SPS) pro spolehlivé autonomní přidělování zdrojů
- Poskytuje vylepšenou fyzickou vrstvu pro vysokorychlostní mobilitu (až do relativní rychlosti 250 km/h)
- Integruje se s buňkovou páteřní sítí (EPC/5GC) pro komunikaci V2N a umožňování služeb
- Obsahuje robustní bezpečnostní rámec s autentizací založenou na PKI a ochranou integrity zpráv

## Definující specifikace

- **TS 33.185** (Rel-19) — V2X Security in LTE
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [LTE-V na 3GPP Explorer](https://3gpp-explorer.com/glossary/lte-v/)
