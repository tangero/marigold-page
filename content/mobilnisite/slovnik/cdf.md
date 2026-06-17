---
slug: "cdf"
url: "/mobilnisite/slovnik/cdf/"
type: "slovnik"
title: "CDF – Cumulative Distribution Function"
date: 2026-01-01
abbr: "CDF"
fullName: "Cumulative Distribution Function"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cdf/"
summary: "Statistická funkce používaná v 3GPP k analýze a modelování rozdělení metrik výkonnosti sítě, jako je propustnost, latence nebo kvalita signálu. Poskytuje matematický rámec pro hodnocení výkonu systému"
---

CDF je statistická funkce používaná v 3GPP k analýze rozdělení metrik výkonnosti sítě, poskytující matematický rámec pro hodnocení výkonu, návrh algoritmů a stanovení KPI.

## Popis

Kumulativní distribuční funkce (CDF) je základní statistický nástroj v rámci standardů 3GPP, používaný k charakterizaci pravděpodobnostního rozdělení náhodné veličiny. V telekomunikacích tato veličina typicky představuje metrický ukazatel výkonu, jako je propustnost uživatele, koncová latence, míra chybových bloků ([BLER](/mobilnisite/slovnik/bler/)) nebo přijímaný výkon referenčního signálu (RSRP). Formálně pro náhodnou veličinu X udává CDF F(x) pravděpodobnost, že X nabude hodnoty menší nebo rovné x (tj. P(X ≤ x)). Tato funkce nabývá hodnot od 0 do 1 a je neklesající. V praktické práci 3GPP je CDF odvozena z empirických dat získaných simulacemi, testy v terénu nebo měřeními v provozní síti, čímž poskytuje úplný obraz o výkonu napříč všemi uživateli nebo podmínkami, nikoli pouze průměrné hodnoty.

Z architektonického hlediska CDF není fyzickou síťovou komponentou, ale matematickým modelem aplikovaným na data generovaná různými síťovými entitami. Její výpočet je nedílnou součástí metodik hodnocení výkonu definovaných v mnoha technických specifikacích (TS) a technických zprávách (TR). Například ve studiích rádiové přístupové sítě (RAN) generují simulátory na systémové úrovni rozsáhlé datové sady o výkonu vnímaném uživatelem. Tyto datové sady jsou zpracovány pro výpočet CDF, které jsou pak použity k vyhodnocení souladu s požadavky (např. propustnost na 95. percentilu uživatele) nebo k porovnání různých implementací algoritmů, jako je plánování nebo správa mobility. CDF poskytuje vhled do férovosti a výkonu v koncové části rozdělení systému, odhaluje, jak jsou ovlivněni nejhůře výkonnostně umístění uživatelé.

Role CDF v ekosystému 3GPP je mnohostranná. Slouží jako společný jazyk pro definování výkonnostních cílů a porovnávání návrhů během standardizačního procesu. Mnoho [KPI](/mobilnisite/slovnik/kpi/) ve specifikacích 3GPP je definováno pomocí percentilních bodů z CDF, jako je uživatelská datová rychlost na 5. percentilu nebo latence na 95. percentilu. To zajišťuje, že výkonnostní cíle zohledňují celou uživatelskou populaci, včetně uživatelů na okraji buňky. Dále je analýza CDF klíčová pro plánování sítě, optimalizaci a srovnávací hodnocení. Operátoři a výrobci zařízení používají grafy CDF k identifikaci výkonnostních úzkých míst, ověření nasazení sítě vůči smluvním SLA a rozhodování o rozšíření kapacity. Schopnost funkce shrnout celé rozdělení do jediné křivky z ní činí nepostradatelný nástroj pro technické reportování a rozhodování.

Z perspektivy implementace vyžaduje generování přesné CDF pečlivý sběr statisticky významných vzorových dat. Specifikace 3GPP často detailně popisují simulační předpoklady, modely provozu a metodiky hodnocení nezbytné pro produkci srovnatelných a reprodukovatelných výsledků CDF. Například studie [NR-U](/mobilnisite/slovnik/nr-u/) (New Radio v nelicencovaném spektru) může specifikovat délku simulace, počet UE, model mobility a scénáře rušení, což vše vede k CDF špičkové propustnosti nebo zpoždění přístupu ke kanálu. Sklon a inflexní body CDF mohou naznačovat robustnost systému; strmá CDF naznačuje, že většina uživatelů zažívá podobný výkon, zatímco dlouhý ocas značí významný výkonnostní rozdíl. Pokročilé analýzy mohou zahrnovat podmíněné CDF nebo porovnávání CDF za různých síťových konfigurací k posouzení dopadu nové funkce.

## K čemu slouží

CDF existuje jako klíčový analytický koncept, protože průměrné metriky (jako střední hodnota nebo medián) nedostačují k zachycení plných výkonnostních charakteristik komplexního, stochastického systému, jakým je mobilní síť. Síť může mít vysokou průměrnou propustnost, ale trpět výraznou nerovností, kdy malá část uživatelů zažívá velmi špatný servis. CDF tento problém řeší tím, že poskytuje úplné rozdělení, což umožňuje standardizačním orgánům, návrhářům sítí a operátorům hodnotit a garantovat výkon pro všechny uživatele, zejména pro ty v koncové části rozdělení (např. nejhorších 5 %). To je klíčové pro zajištění kvality uživatelského prožitku (QoE) a plnění regulatorních nebo komerčních smluv o úrovni služeb (SLA).

Historicky, jak se buněčné systémy vyvíjely od hlasově orientovaných (2G) k širokopásmovým datovým (3G/4G/5G), se hodnocení výkonu stalo složitějším. Jednoduché metriky, jako je míra zrušení hovoru nebo průměrná spektrální účinnost, byly nedostatečné pro datové služby vyžadující konzistentně nízkou latenci a vysokou propustnost. Společenství 3GPP přijalo CDF jako standardizovanou metodologii pro objektivní porovnávání konkurenčních technických návrhů během fází studijních a pracovních položek. Řeší omezení spočívající ve spoléhání se pouze na špičkové nebo průměrné výkonnostní údaje, které mohou maskovat kritické problémy, jako jsou díry v pokrytí, problémy s rušením nebo předsudky plánovače. Tím, že 3GPP v nesčetných výkonnostních studiích nařizuje hodnocení založené na CDF, zajišťuje, že jsou nové technologie hodnoceny komplexně, což pohání vylepšení prospěšná pro celou uživatelskou populaci.

Motivace pro její všudypřítomné použití napříč releasy od Rel-6 do Rel-20 pramení z rostoucí heterogenity služeb (např. rozšířené mobilní širokopásmové připojení, ultra-spolehlivá komunikace s nízkou latencí, hromadný IoT) a síťových nasazení (např. heterogenní sítě, agregace nosných, síťové řezy). Každý nový typ služby má jedinečné požadavky na výkon, které lze nejlépe vyjádřit pomocí CDF. Například URLLC se zaměřuje na extrémní část rozdělení latence (např. 99,999. percentil), zatímco mMTC může zkoumat rozdělení životnosti baterie zařízení. CDF poskytuje jednotný, rigorózní matematický rámec pro stanovení a ověření těchto různorodých požadavků napříč všemi vrstvami protokolového zásobníku a všemi síťovými doménami, od fyzické vrstvy po koncové služby.

## Klíčové vlastnosti

- Poskytuje úplné pravděpodobnostní rozdělení výkonnostní metriky.
- Umožňuje definici percentilových klíčových ukazatelů výkonnosti (KPI).
- Zásadní pro hodnocení férovosti systému a výkonu v koncové části rozdělení (např. uživatelský prožitek na okraji buňky).
- Standardizovaná metodologie pro porovnávání výkonu ve studiích a simulacích 3GPP.
- Aplikovatelná ve všech síťových doménách: RAN, core, koncové služby.
- Základní pro plánování sítě, optimalizaci a ověřování SLA.

## Definující specifikace

- **TS 22.805** (Rel-12) — RAN User Plane Congestion Management
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 25.706** (Rel-13) — Downlink Enhancements for UMTS Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- … a dalších 49 specifikací

---

📖 **Anglický originál a plná specifikace:** [CDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdf/)
