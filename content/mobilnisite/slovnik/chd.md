---
slug: "chd"
url: "/mobilnisite/slovnik/chd/"
type: "slovnik"
title: "CHD – Channel Decoder"
date: 2025-01-01
abbr: "CHD"
fullName: "Channel Decoder"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/chd/"
summary: "Základní komponenta fyzické vrstvy v systémech 3GPP, která obnovuje přenášené informační bity z přijatých, chybami zatížených kanálových symbolů. Je klíčová pro spolehlivou komunikaci tím, že opravuje"
---

CHD je komponenta fyzické vrstvy v systémech 3GPP, která obnovuje přenášené informační bity z přijatých kanálových symbolů opravou chyb zavedených během přenosu přes šumové bezdrátové kanály.

## Popis

Dekodér kanálu (CHD) je základní procesní blok v řetězci přijímače fyzické vrstvy uživatelského zařízení (UE) a základnových stanic (např. [eNB](/mobilnisite/slovnik/enb/), gNB). Jeho primární funkcí je inverzní operace ke kanálovému kodéru na straně vysílače. Přijímá symboly s měkkým nebo tvrdým rozhodováním (běžnými vstupy jsou poměry logaritmické věrohodnosti, LLR) demodulované z přijímaného rádiového signálu a aplikuje sofistikované dekódovací algoritmy k rekonstrukci původních dat transportního bloku nebo kódového bloku. Tento proces je nezbytný, protože přenášený signál je vždy narušen šumem, interferencí a útlumovými jevy vlastními bezdrátovému prostředí. Dekodér využívá strukturovanou redundanci (paritní bity) záměrně přidanou kanálovým kodérem k detekci a opravě bitových chyb a usiluje o výstup bezchybné verze informačních bitů odeslaných z vyšších vrstev.

Činnost CHD je úzce provázána s konkrétním schématem kanálového kódování stanoveným specifikacemi 3GPP pro různé kanály a datové typy. V LTE (od Rel-8) a 5G NR patří mezi hlavní kódovací schémata Turbo kódování pro datové kanály (např. [PDSCH](/mobilnisite/slovnik/pdsch/), PUSCH), konvoluční kódování s uzavřením do kruhu (TBCC) pro řídicí kanály (např. [PDCCH](/mobilnisite/slovnik/pdcch/)) a Polar kódování pro specifické řídicí kanály v NR (např. PBCH). Každé schéma vyžaduje vlastní implementaci dekodéru. Například Turbo dekodér typicky používá iterativní algoritmus se dvěma komponentními dekodéry (často založenými na algoritmu [MAP](/mobilnisite/slovnik/map/) nebo Log-MAP), které si vyměňují externí informaci, aby konvergovaly k nejpravděpodobnější přenesené sekvenci. Pro TBCC se používá Viterbiho dekodér, který provádí odhad sekvence s maximální věrohodností pomocí prohledávání grafu (trellis).

Z architektonického hlediska se CHD nachází za demodulátorem a před derandomizátorem a moduly zpracování vyšších vrstev. Jeho výkon je charakterizován metrikami jako je bitová chybovost ([BER](/mobilnisite/slovnik/ber/)), bloková chybovost ([BLER](/mobilnisite/slovnik/bler/)) a výpočetní složitost. Volba dekódovacího algoritmu a jeho implementace (např. počet iterací pro Turbo dekódování) představuje kompromis mezi schopností opravy chyb, zpracovatelskou latencí a spotřebou energie – což jsou klíčové aspekty pro návrh UE. Pokročilé implementace mohou využívat kombinování v rámci hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)), kdy dekodér využívá dříve přijaté chybné verze paketu spolu s retransmisemi ke zvýšení úspěšnosti dekódování. CHD tedy není jediná entita, ale kategorie dekodérů, jejichž konkrétní provedení je určeno zpracovávaným fyzickým kanálem a souvisejícími technickými specifikacemi 3GPP (TS).

## K čemu slouží

Dekodér kanálu existuje proto, aby zajistil spolehlivou digitální komunikaci přes inherentně nespolehlivé bezdrátové kanály. Bez něj by vysoké bitové chybovosti způsobené šumem, vícestopým útlumem a interferencí znemožnily praktické datové služby. Jeho účelem je využití principů teorie informace, konkrétně kanálového kódování (předběžná oprava chyb), k rekonstrukci přenášených dat s pravděpodobností chyby, která splňuje přísné požadavky na kvalitu služeb (QoS) hlasových, video a datových aplikací. Řeší základní problém fyzické vrstvy: převod šumového analogového průběhu zpět na přesné digitální bity generované zdrojem.

Historicky motivací pro pokročilé dekodéry kanálu, jako je Turbo dekodér (zavedený v 3G UMTS a dále používaný), bylo přiblížení se Shannonově limitě kapacity kanálu – teoretickému maximu spolehlivé komunikace přes šumový kanál. Před Turbo kódy se používaly konvoluční kódy a Reedovy-Solomonovy kódy, které však za Shannonovým limitem zaostávaly. Zavedení Turbo kódování v 3G představovalo významný skok, umožňující vyšší datové rychlosti při stejném poměru signálu k šumu nebo udržení rychlostí v horších kanálových podmínkách. Pro 5G NR zavedení Polar kódů pro řídicí kanály odpovědělo na potřebu scénářů komunikace s ultra-spolehlivým nízkým zpožděním (URLLC), protože Polar kódy mohou dosahovat lepšího výkonu při krátkých délkách bloků ve srovnání s jinými schématy. Vývoj technologie CHD je tedy přímo hnán potřebou vyšší spektrální účinnosti, nižší latence a podpory různorodých požadavků služeb.

## Klíčové vlastnosti

- Implementuje inverzní funkci kanálového kódování k obnovení původních informačních bitů
- Podporuje více dekódovacích algoritmů (např. pro Turbo, konvoluční, LDPC, Polar kódy) dle specifikací 3GPP
- Zpracovává vstupy s měkkým rozhodováním (poměry logaritmické věrohodnosti) pro maximalizaci výkonu dekódování
- Opravuje přenosové chyby zavedené kanálovým šumem, útlumem a interferencí
- Umožňuje procesy hybridního ARQ (HARQ) dekódováním a kombinací retransmisí
- Klíčový pro dosažení cílové blokové chybovosti (BLER) a spolehlivosti spoje

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 26.071** (Rel-19) — AMR Speech Codec Introduction
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.171** (Rel-19) — Introduction to AMR-WB Speech Processing
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation

---

📖 **Anglický originál a plná specifikace:** [CHD na 3GPP Explorer](https://3gpp-explorer.com/glossary/chd/)
