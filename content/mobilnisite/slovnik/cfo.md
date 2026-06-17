---
slug: "cfo"
url: "/mobilnisite/slovnik/cfo/"
type: "slovnik"
title: "CFO – Carrier Frequency Offset"
date: 2026-01-01
abbr: "CFO"
fullName: "Carrier Frequency Offset"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cfo/"
summary: "Carrier Frequency Offset je rozdíl mezi vysílanou a přijímanou nosnou frekvencí v bezdrátovém systému, způsobený nepřesnostmi oscilátorů a Dopplerovým jevem. Jde o zásadní zkreslení, které musí být od"
---

CFO je rozdíl mezi vysílanou a přijímanou nosnou frekvencí, způsobený nepřesnostmi oscilátorů a Dopplerovým jevem, který musí být v systémech jako 5G NR kompenzován, aby se předešlo mezi-nosnému rušení.

## Popis

Carrier Frequency Offset (CFO) je základní zkreslení na fyzické vrstvě v bezdrátových komunikačních systémech, zejména těch využívajících ortogonální multiplex s frekvenčním dělením ([OFDM](/mobilnisite/slovnik/ofdm/)), jako je 5G New Radio (NR). Představuje odchylku mezi nominální nosnou frekvencí generovanou lokálním oscilátorem vysílače a frekvencí vnímanou lokálním oscilátorem přijímače po průchodu prostředím. Tento offset vzniká ze dvou hlavních příčin: statického nesouladu frekvencí v důsledku výrobních tolerancí a teplotou indukovaných odchylek krystalových oscilátorů ve vysílači a přijímači, a dynamické složky způsobené Dopplerovým jevem při relativním pohybu vysílače a přijímače. Ve scénáři s více uživateli nebo buňkami může každé spojení zažívat jedinečný CFO. Absolutní CFO je často normalizován vzhledem k rozteči subnosných (SCS) a vyjádřen v jednotkách ppm (částic na milion) nebo jako poměr Δf/SCS, kde Δf je frekvenční odchylka.

V kontextu OFDM vlnového tvaru 5G NR je přesná frekvenční synchronizace prvořadá. Ortogonalita mezi subnosnými, která zabraňuje mezi-nosnému rušení ([ICI](/mobilnisite/slovnik/ici/)), je zachována pouze tehdy, když přijímač provede okno rychlé Fourierovy transformace ([FFT](/mobilnisite/slovnik/fft/)) na přesně stejné frekvenci jako vysílač. Zbytkový CFO tuto ortogonalitu narušuje, což vede k ICI a výraznému zhoršení poměru signálu k rušení plus šum (SINR). Řetězec zpracování fyzické vrstvy přijímače proto zahrnuje specializované algoritmy pro odhad a korekci CFO. Počáteční hrubý odhad se typicky provádí pomocí referenčních signálů v časové oblasti, jako jsou synchronizační signály (PSS/SSS) nebo specializované frekvenčně korekční signály. Jemný odhad a sledování jsou dosaženy pomocí demodulačních referenčních signálů ([DM-RS](/mobilnisite/slovnik/dm-rs/)) nebo referenčních signálů pro sledování fáze (PT-RS) uvnitř datového kanálu. Odhadnutá odchylka je zpětně přivedena na číslicově řízený oscilátor (NCO) nebo použita k aplikaci fázové rotace v číslicové oblasti pro opravu přijímaného signálu.

Dopad CFO se mění s parametry systému. Vyšší rozteče subnosných (např. pro pásma FR2 v mmWave) jsou tolerantnější k absolutním frekvenčním chybám v Hertzech, ale vyžadují proporcionálně přesný odhad. Požadavek na výkon odhadu CFO je přísný, často je nutná korekce na úrovni 1-2 % rozteče subnosných, aby se předešlo výrazné ztrátě výkonu. Specifikace 3GPP definují požadavky na přesnost oscilátoru UE a gNodeB, které přímo omezují počáteční CFO, který musí být zvládnut. Například TS 38.101 specifikuje požadavky na frekvenční chybu UE. Algoritmy pro odhad CFO, ačkoliv nejsou standardizovány, jsou kritickou součástí návrhu přijímače základního pásma a zahrnují techniky jako korelace s cyklickou předponou, měření fázového rozdílu založené na pilotních signálech a metody neřízeného odhadu. Efektivní správa CFO je tedy základním kamenem pro dosažení vysoké spektrální účinnosti a spolehlivého výkonu spoje, které slibuje 5G NR.

## K čemu slouží

Odhad a korekce CFO existují, aby řešily základní problém frekvenčního nesouladu mezi komunikujícími rádiovými jednotkami, což je nevyhnutelná fyzikální realita. Bez řešení CFO by moderní modulační schémata vysokého řádu a husté mřížky [OFDM](/mobilnisite/slovnik/ofdm/) subnosných používané v 4G LTE a 5G NR byly nepoužitelné kvůli katastrofickému [ICI](/mobilnisite/slovnik/ici/). Účelem je umožnit praktickou implementaci koherentní demodulace, která spoléhá na stabilní a přesný frekvenční referenční signál pro správné mapování přijatých symbolů do konstelace. Kompenzací CFO systém zachovává ortogonalitu OFDM subnosných, čímž chrání rozpočet spoje a umožňuje vysoké přenosové rychlosti.

Motivace pro sofistikované zpracování CFO rostla s každou generací buněčné technologie. V raných úzkopásmových systémech mohla malá frekvenční chyba způsobit pouze konstantní fázovou rotaci, zvládnutelnou jednoduššími technikami. Přechod na širokopásmové OFDM v 3GPP LTE však učinil systém mimořádně citlivým na frekvenční chyby, protože každý Hertz odchylky způsobuje ICI napříč stovkami nebo tisíci subnosných. Omezení předchozích, méně robustních synchronizačních metod se stala překážkou výkonu. 5G NR přineslo nové výzvy: širší šířky pásma, vyšší nosné frekvence (s výraznějšími Dopplerovými jevy) a podporu pro IoT zařízení s nízkým příkonem s levnějšími a méně stabilními oscilátory. Vytvoření a zdokonalení technik CFO v rámci specifikací 3GPP zajišťuje, že zařízení od různých výrobců mohou spolupracovat za společné sady požadavků na výkon, což garantuje robustnost na systémové úrovni navzdory základním hardwarovým nedokonalostem.

## Klíčové vlastnosti

- Zkreslení způsobené nepřesností oscilátorů a Dopplerovým jevem
- Měřeno jako rozdíl mezi vysílanou a přijímanou nosnou frekvencí
- Kritické pro odhad a korekci kvůli integritě systému OFDM/OFDMA
- Způsobuje mezi-nosné rušení (ICI), pokud není korigováno
- Odhadováno pomocí referenčních signálů (např. PSS, SSS, DM-RS, PT-RS)
- Požadavek definován v ppm vzhledem k nosné frekvenci ve specifikacích

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)

## Definující specifikace

- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TS 38.774** (Rel-19) — Rel-19 LP-WUS/WUR RF Requirements TR
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TR 38.859** (Rel-18) — Technical Report
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [CFO na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfo/)
