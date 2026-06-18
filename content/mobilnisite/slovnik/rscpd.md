---
slug: "rscpd"
url: "/mobilnisite/slovnik/rscpd/"
type: "slovnik"
title: "RSCPD – Reference Signal Carrier Phase Difference"
date: 2025-01-01
abbr: "RSCPD"
fullName: "Reference Signal Carrier Phase Difference"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rscpd/"
summary: "RSCPD je měření relativního fázového rozdílu mezi nosnými fázemi dvou přijatých referenčních signálů. Zavedeno v Release 18, umožňuje vysoce přesné relativní určování polohy a časovou synchronizaci dí"
---

RSCPD je měření relativního fázového rozdílu mezi nosnými fázemi dvou přijatých referenčních signálů, používané pro přesné určování polohy a časové synchronizace díky eliminaci chyb společného oscilátoru.

## Popis

Reference Signal Carrier Phase Difference (RSCPD) je specializované měření zavedené ve specifikaci 3GPP Release 18. Na rozdíl od [RSCP](/mobilnisite/slovnik/rscp/), které měří absolutní fázi, RSCPD kvantifikuje rozdíl v nosné fázi mezi dvěma různými referenčními signály přijatými stejným zařízením. Tyto signály mohou pocházet z různých vysílacích bodů (např. ze dvou různých gNB nebo [TRP](/mobilnisite/slovnik/trp/)), z různých anténních panelů stejné základnové stanice, nebo se může jednat o stejný typ referenčního signálu přijatého ve dvou různých časových okamžicích. Proces měření zahrnuje nezávislý výpočet RSCP pro každý cílový signál a následné určení jejich rozdílu, typicky modulo 2π pro řešení fázového přechodu přes hranici 2π.

Z architektonického hlediska je měření RSCPD funkcí vyšší vrstvy postavenou nad základní schopnost měření RSCP. Je implementováno v měřicím modulu fyzické vrstvy UE a v souvisejících protokolech pro hlášení ve vrstvě 3 ([RRC](/mobilnisite/slovnik/rrc/)). Síť měření konfiguruje pomocí RRC nebo [MAC](/mobilnisite/slovnik/mac/) řídicích prvků, přičemž specifikuje pár referenčních signálů (identifikovaných jejich vzory prvků zdroje, ID buněk nebo časovými instancemi), mezi nimiž musí být fázový rozdíl vypočítán. Tato konfigurace je složitější než u RSCP, protože definuje vztah mezi dvěma entitami. Klíčovými komponentami jsou dvojice přijímačů sledujících fázi (nebo časově multiplexovaná měření na jediném přijímači) a aritmetická jednotka, která provádí odečítání, často včetně sofistikovaných algoritmů pro řešení cyklické nejednoznačnosti.

V kontextu sítí 5G-Advanced a budoucích 6G je role RSCPD transformativní pro přesné snímání a relativní určování polohy. Měřením fázového rozdílu jsou efektivně eliminovány společné zdroje chyb, které ovlivňují obě měření stejně – například nedokonalosti místního oscilátoru UE nebo určité atmosférické zpoždění. Díky tomu je RSCPD mimořádně stabilní a přesná metrika. Jejím primárním uplatněním je síťové snímání, kde lze fázový rozdíl signálů odražených od objektu použít k odhadu rychlosti objektu a nepatrných změn jeho polohy. Také zlepšuje kooperativní určování polohy mezi zařízeními (device-to-device positioning) tím, že poskytuje přímé měření jejich relativního fázového posunu, který přímo koreluje s jejich relativní vzdáleností a orientací, což umožňuje relativní lokalizaci s přesností pod centimetr pro roje robotů nebo vozidlové soupravy.

## K čemu slouží

RSCPD bylo vytvořeno, aby řešilo omezení měření absolutní fáze ([RSCP](/mobilnisite/slovnik/rscp/)) v nových případech použití pro 5G-Advanced a 6G, zejména ve sdružené komunikaci a snímání (JCAS) a ultra-přesném relativním určování polohy. Zatímco RSCP je výborné pro určení absolutní polohy vzhledem k síti, jeho přesnost je omezena stabilitou vlastního vnitřního hodinového zdroje zařízení. Jakýkoli drift nebo chvění v oscilátoru UE přímo zkresluje měření RSCP. RSCPD tento problém elegantně řeší tím, že jde o diferenciální měření, kde se společná chyba hodin odečte.

Historický kontext souvisí s průzkumem schopností 6G v rámci 3GPP, kde se snímání fyzického prostředí stává nativní síťovou funkcí. Tradiční radarové systémy používají měření fázového rozdílu (např. interferometrii) pro přesnou analýzu rychlosti a mikro-Dopplerova jevu. RSCPD přináší tuto radarovou techniku do oblasti buněčných sítí. Před Release 18 mohly sítě podobné informace odvozovat porovnáváním samostatně hlášených hodnot RSCP od UE, ale to bylo neefektivní, méně přesné kvůli latenci hlášení a kvantizaci a nebylo standardizované. RSCPD pro tento účel poskytuje přímou, optimalizovanou a standardizovanou měřicí primitivu.

Dále RSCPD podporuje vývoj směrem k extrémně hustým sítím a integrovanému přístupu a propojení ([IAB](/mobilnisite/slovnik/iab/)). V takovém prostředí je znalost přesného relativního fázového zarovnání mezi více vysílacími/přijímacími body klíčová pro koherentní sdružené vysílání. Měření RSCPD od UE může síti pomoci kalibrovat a zarovnat své vlastní distribuované vysílače, čímž řeší klíčovou výzvu v architekturách distribuovaného [MIMO](/mobilnisite/slovnik/mimo/) a celulárního massive MIMO bez buněk. Motivací byla potřeba standardizované, UE asistované metody pro dosažení a udržení této ultra-těsné fázové synchronizace napříč sítí.

## Klíčové vlastnosti

- Měří diferenciální fázi nosné mezi dvěma referenčními signály
- Eliminuje chyby společného místního oscilátoru v měřícím zařízení
- Standardizovaná primitiva pro sdruženou komunikaci a snímání v 5G-Advanced/6G
- Umožňuje vysoce přesné relativní určování polohy a odhad rychlosti
- Konfigurováno pro specifické páry signálů (např. z různých TRP nebo časových instancí)
- Podporuje síťovou kalibraci pro koherentní distribuované MIMO systémy

## Související pojmy

- [RSCP – Reference Signal Carrier Phase](/mobilnisite/slovnik/rscp/)
- [PRS – Positioning Reference Signal](/mobilnisite/slovnik/prs/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning

---

📖 **Anglický originál a plná specifikace:** [RSCPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rscpd/)
