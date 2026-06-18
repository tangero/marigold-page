---
slug: "atd"
url: "/mobilnisite/slovnik/atd/"
type: "slovnik"
title: "ATD – Absolute Time Difference"
date: 2025-01-01
abbr: "ATD"
fullName: "Absolute Time Difference"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/atd/"
summary: "Absolute Time Difference (ATD) je metoda určování polohy v sítích 3GPP, která měří časový rozdíl příchodu signálů z více základnových stanic za účelem stanovení polohy mobilního zařízení. Umožňuje urč"
---

ATD je metoda určování polohy podle 3GPP, která stanovuje polohu zařízení měřením časového rozdílu příchodu signálů z více základnových stanic.

## Popis

Absolute Time Difference (ATD) je síťová technika určování polohy standardizovaná v 3GPP, která vypočítává zeměpisnou polohu mobilního zařízení měřením časového rozdílu mezi signály přicházejícími z více synchronizovaných základnových stanic. Metoda je založena na principu hyperbolického určování polohy, kde každý změřený časový rozdíl definuje hyperbolickou křivku, na které musí mobilní zařízení ležet, a průsečík více takových křivek z různých párů základnových stanic určuje přesnou polohu.

Architektura určování polohy ATD zahrnuje několik klíčových komponent: mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) neboli uživatelské zařízení (UE), které přijímá signály z více základnových stanic; subsystém základnové stanice ([BSS](/mobilnisite/slovnik/bss/)) nebo NodeB/eNodeB/gNB, které vysílají referenční signály; centrum polohy obsluhující mobilní síť ([SMLC](/mobilnisite/slovnik/smlc/)) nebo funkci správy polohy ([LMF](/mobilnisite/slovnik/lmf/)), která vypočítává polohu; a centrum polohy brány ([GMLC](/mobilnisite/slovnik/gmlc/)), které zprostředkovává rozhraní pro externí aplikace služeb založených na poloze. Proces určování polohy začíná tím, že síť nařídí mobilnímu zařízení, aby změřilo čas příchodu signálů z více sousedních základnových stanic vzhledem k jeho obsluhované buňce.

Technická implementace vyžaduje přesnou časovou synchronizaci mezi základnovými stanicemi, obvykle dosaženou pomocí [GPS](/mobilnisite/slovnik/gps/) přijímačů na každém místě základnové stanice nebo prostřednictvím síťových časových protokolů. Mobilní zařízení měří pozorovaný časový rozdíl ([OTD](/mobilnisite/slovnik/otd/)) mezi přijatými signály, který se skládá ze dvou složek: geometrického časového rozdílu (GTD) způsobeného rozdíly fyzické vzdálenosti a reálného časového rozdílu ([RTD](/mobilnisite/slovnik/rtd/)) představujícího skutečný časový posun mezi základnovými stanicemi. Síť poskytuje kalibrační data RTD polohovému serveru, který následně vypočítá GTD a převede jej na rozdíly vzdáleností pro hyperbolické určování polohy.

ATD funguje ve dvou hlavních režimech: v režimu s asistencí UE, kde zařízení provádí měření a hlásí je síti k výpočtu, a v režimu založeném na UE, kde zařízení vypočítává svou vlastní polohu pomocí asistenčních dat ze sítě. Přesnost určování polohy ATD závisí na faktorech včetně počtu viditelných základnových stanic, jejich geometrického rozložení vzhledem k mobilnímu zařízení, podmínek šíření signálu a přesnosti synchronizace mezi základnovými stanicemi. Typická přesnost se pohybuje od 50 do 150 metrů v městském prostředí s dobrou hustotou a geometrií základnových stanic.

## K čemu slouží

ATD byl vyvinut, aby poskytoval spolehlivé síťové možnosti určování polohy v celulárních sítích a řešil několik kritických potřeb: regulatorní požadavky na lokalizaci nouzových volajících (jako je E911 ve Spojených státech a E112 v Evropě), komerční služby založené na poloze a funkce optimalizace sítě. Před ATD a podobnými metodami určování polohy měly celulární sítě omezenou schopnost určit polohu účastníka mimo základní informaci o identitě buňky, která poskytovala pouze hrubou přesnost polohy v řádu několika kilometrů.

Vznik ATD byl motivován omezeními dřívějších přístupů k určování polohy, jako je Cell-ID, které nabízely nedostatečnou přesnost pro nouzové služby, a nepraktičností požadavku, aby všechna mobilní zařízení obsahovala GPS přijímače. ATD poskytl nákladově efektivní řešení, které fungovalo s existující síťovou infrastrukturou a standardními mobilními zařízeními, a umožnil určování polohy bez nutnosti hardwarových úprav telefonů. To bylo zvláště důležité na počátku roku 2000, kdy byla integrace GPS v mobilních telefonech stále drahá a energeticky náročná.

ATD řešil konkrétní technické výzvy včetně požadavků na synchronizaci sítě, přesnost měření v prostředích s vícecestným šířením a integraci s existujícími síťovými architekturami. Tím, že poskytl standardizované možnosti určování polohy, umožnil ATD konzistentní implementaci napříč různými síťovými operátory a dodavateli zařízení, usnadnil interoperabilitu a dodržování předpisů a zároveň podpořil rostoucí trh aplikací a služeb založených na poloze.

## Klíčové vlastnosti

- Určování polohy založené na síti nevyžadující GPS v mobilním zařízení
- Hyperbolické určování polohy využívající měření časového rozdílu příchodu
- Podpora režimů určování polohy s asistencí UE i založeného na UE
- Integrace s požadavky nouzových služeb (E911/E112)
- Využití existující celulární infrastruktury s časovou synchronizací
- Standardizované postupy měření a formáty hlášení

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [ATD na 3GPP Explorer](https://3gpp-explorer.com/glossary/atd/)
