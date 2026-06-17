---
slug: "ivr"
url: "/mobilnisite/slovnik/ivr/"
type: "slovnik"
title: "IVR – Interactive Voice Response"
date: 2025-01-01
abbr: "IVR"
fullName: "Interactive Voice Response"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ivr/"
summary: "Telefonní technologie, která umožňuje počítačovému systému interagovat s volajícími prostřednictvím hlasových výzev a vstupu tónů DTMF (dual-tone multi-frequency). Automatizuje obsluhu hovorů, získává"
---

IVR je telefonní technologie, která umožňuje počítačovému systému interagovat s volajícími prostřednictvím hlasových výzev a vstupu DTMF tónů za účelem automatizace obsluhy hovorů, získávání informací a směrování hovorů.

## Popis

Interactive Voice Response (IVR) je automatizovaný telefonní systém, který interaguje s volajícími, shromažďuje informace prostřednictvím hlasových a klávesnicových vstupů a směruje hovory na příslušné zdroje nebo poskytuje informace z databází. V kontextu 3GPP je IVR standardizováno jako síťová služba, často umístěná v architektuře Intelligent Network ([IN](/mobilnisite/slovnik/in/)) nebo IP Multimedia Subsystem (IMS). Funguje jako specializovaný aplikační server, který rozhraní s funkcemi řízení hovorové relace v jádru sítě.

Z architektonického hlediska systém IVR podle 3GPP typicky zahrnuje několik klíčových komponent. Jádrem je IVR Application Server ([AS](/mobilnisite/slovnik/as/)), který hostí servisní logiku a hlasové výzvy. Rozhraní s Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), která poskytuje schopnosti zpracování médií: přehrávání předem nahraných oznámení, nahrávání vstupů volajícího, provádění rozpoznávání řeči (pro pokročilé systémy) a detekci [DTMF](/mobilnisite/slovnik/dtmf/) tónů. IVR AS komunikuje s jádrem sítě (např. s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) v okruhově spínaných doménách nebo s Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS) za použití protokolů jako [CAMEL](/mobilnisite/slovnik/camel/) Application Part ([CAP](/mobilnisite/slovnik/cap/)) nebo Session Initiation Protocol (SIP). Síť směruje hovor na IVR na základě spouštěcích bodů, jako je konkrétní volané číslo (např. zákaznická linka).

Princip fungování: Když účastník zavolá na číslo s podporou IVR, síť pozastaví běžné zpracování hovoru a směruje hovor na IVR Application Server. IVR AS dá pokyn připojené MRF, aby přehrála úvodní výzvu (např. 'Stiskněte 1 pro zůstatek na účtu, stiskněte 2 pro technickou podporu'). MRF shromáždí DTMF odezvu volajícího nebo analyzuje řeč. Tento vstup je odeslán zpět do IVR AS, který provede servisní logiku – například dotaz na back-endovou databázi prostřednictvím webových služeb. Na základě logiky může IVR přehrát další informace, přepojit hovor na živého operátora (pokynem síti, aby směrovala na operátorovo číslo) nebo zahájit zpětné volání. Jeho úlohou je automatizovat opakované dotazy s vysokým objemem, poskytovat služby 24/7 a efektivně třídit hovory před tím, než se dostanou k lidským operátorům.

## K čemu slouží

Technologie IVR byla vytvořena za účelem automatizace telefonických interakcí se zákazníky, čímž snižuje provozní náklady kontaktních center a zlepšuje dostupnost služeb mimo pracovní dobu. Před IVR vyžadovaly všechny dotazy živého operátora, což vedlo k dlouhým čekacím dobám, vysokým nákladům na personál a omezeným servisním hodinám. Původním účelem byla jednoduchá automatizace: přehrávání nahraných informací (jako zůstatky na účtu) nebo směrování hovorů na správné oddělení na základě výběru z menu.

V ekosystému 3GPP, počínaje Release 99, bylo IVR standardizováno, aby byla zajištěna interoperabilita a umožněny pokročilé síťové služby. Vyřešilo problém, jak konzistentně poskytovat automatizované hlasové služby napříč různými operátorskými sítěmi a typy koncových zařízení. Pro mobilní operátory jsou systémy IVR klíčové pro implementaci standardních doplňkových služeb, jako je přístup k hlasové schránce ('Stiskněte 1 pro poslech zpráv'), doplňování kreditu u předplacených služeb a síťová oznámení. Omezení dřívějších proprietárních IVR systémů byla v nedostatku standardizace, což ztěžovalo nasazení služeb, které by bezproblémově fungovaly pro roamující účastníky nebo přes hranice sítí.

IVR se dále vyvinulo, aby řešilo složitější potřeby. Umožňuje zákazníkům samoobslužné služby, čímž uvolňuje lidské operátory pro složité problémy. Poskytuje konzistentní uživatelské rozhraní pro přístup ke službám. V kontextu IMS se IVR stává multimediálním aplikačním serverem schopným zpracovávat také video a textové interakce, čímž tvoří základ pro interaktivní multimediální responsní systémy. Jeho vytvoření a standardizace byly motivovány ekonomickými přínosy a přínosy pro kvalitu služeb plynoucími z automatizace v telekomunikacích.

## Klíčové vlastnosti

- Vstup DTMF a řeči: Přijímá vstup od uživatele prostřednictvím tónů telefonní klávesnice (DTMF) a v pokročilých systémech prostřednictvím automatického rozpoznávání řeči (ASR).
- Přednahrané a text-to-speech výzvy: Přehrává volajícím zvukové pokyny pomocí uložených nahrávek nebo dynamicky generované řeči z textu.
- Směrování a přepojení hovorů: Dokáže směrovat hovory na různá místa určení (operátory, fronty, jiná IVR menu) na základě vstupu volajícího nebo obchodní logiky.
- Integrace s databází: Propojuje se s back-endovými databázemi a obchodními systémy pro získávání nebo aktualizaci informací v reálném čase (např. zůstatky na účtu).
- Síťová integrace: Rozhraní s prvky jádra sítě (MSC, CSCF) za použití standardizovaných protokolů (CAP, SIP) pro řízení hovorů.
- Provádění servisní logiky: Hostí přizpůsobitelné skripty nebo aplikace, které definují průběh interaktivního dialogu a obchodní pravidla služby.

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 23.039** (Rel-5) — SMSC to SME Interface Protocols
- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [IVR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ivr/)
