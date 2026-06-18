---
slug: "bss"
url: "/mobilnisite/slovnik/bss/"
type: "slovnik"
title: "BSS – Base Station Subsystem"
date: 2026-01-01
abbr: "BSS"
fullName: "Base Station Subsystem"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bss/"
summary: "Subsystém základnových stanic (BSS) je komponenta přístupové sítě GSM odpovědná za správu rádiových zdrojů a konektivitu mezi mobilními stanicemi a jádrem sítě. Skládá se ze základnové přijímací a vys"
---

BSS je komponenta přístupové sítě GSM odpovědná za správu rádiových zdrojů a konektivitu mezi mobilními stanicemi a jádrem sítě, která zahrnuje BTS a BSC.

## Popis

Subsystém základnových stanic (BSS) je klíčová architektonická komponenta systému GSM, která tvoří celou přístupovou rádiovou síť (RAN) 2. generace. Jeho primární funkcí je řídit všechny rádiové aspekty komunikace mezi mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)) a jádrem sítě. BSS je fyzicky i logicky rozdělen na dva hlavní prvky: základnovou přijímací a vysílací stanici ([BTS](/mobilnisite/slovnik/bts/)) a řídicí jednotku základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). BTS, často označovaná jako buňka nebo základnová stanice, obsahuje rádiové transceivery, antény a zařízení pro zpracování signálu, které definují rádiovou buňku. Provádí modulaci/demodulaci, kanálové kódování/dekódování, šifrování/dešifrování pro rozhraní k mobilní stanici (rozhraní Um) a zajišťuje přenos a příjem na fyzické vrstvě.

Řídicí jednotka základnových stanic (BSC) je inteligentní řídicí uzel pro jednu nebo více BTS. Spravuje rádiové zdroje ([RR](/mobilnisite/slovnik/rr/)) pro své přidružené buňky, včetně přidělování a uvolňování rádiových kanálů (časových slotů a frekvencí). BSC je zodpovědná za klíčové funkce správy mobility, jako je zahájení a provedení přechodu spojení (handoveru) mezi buňkami pod její kontrolou (intra-BSC handover) a zpracování měření z MS. Také provádí řízení výkonu pro optimalizaci kvality signálu a minimalizaci interference a koncentruje a směruje provoz a signalizaci mezi BTS a ústřednou mobilního přepojování ([MSC](/mobilnisite/slovnik/msc/)) v jádru sítě prostřednictvím rozhraní A.

Z provozního hlediska BSS funguje tak, že BTS nepřetržitě vysílá systémové informace na kanálech řídicího vysílání. Když mobilní stanice požádá o spojení, BTS tento požadavek přepošle BSC. BSC pak požadavek ověří s jádrem sítě, přidělí prostřednictvím BTS hovorový kanál ([TCH](/mobilnisite/slovnik/tch/)) nebo signalizační kanál a spravuje probíhající hovor nebo datovou relaci. Pro mobilitu BSC přijímá prostřednictvím BTS hlášení o měřeních z MS, vyhodnocuje sílu a kvalitu signálu ze sousedních buněk a rozhoduje, kdy provést handover, ať už v rámci své vlastní skupiny BTS, nebo koordinací s jinou BSC či MSC.

Rozhraní BSS jsou dobře definována: rozhraní Um je rádiové rozhraní k MS; rozhraní Abis je interní, často proprietární rozhraní mezi BTS a BSC; a rozhraní A je standardizované rozhraní spojující BSC s MSC v jádru sítě. Toto jasné oddělení rádiového přenosu (BTS) a řízení/správy (BSC) umožnilo škálovatelné a efektivní nasazení sítě. Architektura BSS a principy centralizované kontroly rádiových zdrojů přímo ovlivnily návrh pozdějších RAN 3GPP, jako je rádiový síťový subsystém ([RNS](/mobilnisite/slovnik/rns/)) UMTS s jeho Node B a [RNC](/mobilnisite/slovnik/rnc/).

## K čemu slouží

BSS byl vytvořen jako standardizovaná přístupová rádiová síť pro digitální buněčný systém GSM, který byl vyvinut v 80. letech 20. století jako náhrada za analogové sítě první generace (1G). Jeho hlavním účelem bylo vyřešit problémy omezené kapacity, špatné kvality hovoru, nedostatku zabezpečení a nekompatibility mezi národními systémy, které sužovaly sítě 1G. Definováním digitálního, okruhově přepínaného přístupového subsystému s centralizovaným řízením umožnilo GSM a jeho BSS zabezpečené, kvalitní hlasové služby, mezinárodní roaming a výrazně lepší spektrální účinnost.

Architektonické rozdělení na BTS a BSC řešilo klíčové provozní a ekonomické výzvy. Umístění relativně jednoduché, na rádiový přenos zaměřené BTS na místo buňky umožnilo nákladově efektivní nasazení a údržbu. Centralizace inteligence a řídicích funkcí v BSC umožnila efektivní správu rádiových zdrojů napříč více buňkami, sofistikované algoritmy pro handover a koncentraci provozu, což snížilo náklady na přenos směrem k jádru sítě. Toto rozdělení úkolů bylo základním konceptem pro návrh buněčných sítí.

Standardizace rozhraní A mezi BSS a jádrem sítě byla navíc revolučním krokem. Oddělila RAN od jádra sítě a umožnila interoperabilitu zařízení od různých dodavatelů. Tím se prolomila vazba na jediného dodavatele, podpořila se konkurence a urychlilo se globální nasazení a úspěch GSM. BSS tak poskytl spolehlivou, škálovatelnou a standardizovanou rádiovou přístupovou vrstvu, která učinila z GSM dominantní technologii 2. generace na světě.

## Klíčové vlastnosti

- Spravuje všechny funkce řízení rádiových zdrojů (RRC) pro buňky GSM
- Centralizované řízení více základnových přijímacích a vysílacích stanic (BTS) prostřednictvím řídicí jednotky základnových stanic (BSC)
- Provádí handovery uvnitř buňky a mezi buňkami na základě hlášení o měřeních z mobilní stanice
- Provádí řízení výkonu a přeskakování frekvencí pro optimalizaci kvality signálu a minimalizaci interference
- Zajišťuje šifrování a dešifrování uživatelských dat a signalizace přes rádiové rozhraní (Um)
- Koncentruje a směruje uživatelský provoz a signalizaci mezi MS a MSC jádra sítě prostřednictvím standardizovaného rozhraní A

## Související pojmy

- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.420** (Rel-19) — Iur Interface Introduction for UTRAN
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- … a dalších 48 specifikací

---

📖 **Anglický originál a plná specifikace:** [BSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bss/)
