---
slug: "inc"
url: "/mobilnisite/slovnik/inc/"
type: "slovnik"
title: "INC – INcoming Call"
date: 2025-01-01
abbr: "INC"
fullName: "INcoming Call"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/inc/"
summary: "INC označuje síťovou událost a související procedury pro zpracování příchozího hovoru k mobilnímu účastníkovi. Jde o základní koncept telefonie ve specifikacích 3GPP, který řídí zřízení hovoru, směrov"
---

INC je standardizovaná síťová událost a procedura 3GPP pro zpracování příchozího hovoru k mobilnímu účastníkovi, která řídí zřízení hovoru, směrování a notifikaci.

## Popis

INcoming Call (INC) je klíčový koncept služby ve specifikacích 3GPP, podrobně popsaný v TS 27.002. Představuje kompletní sadu síťových procedur a signalizačních interakcí spuštěných při příchodu hovoru k mobilnímu účastníkovi (volanému). Proces INC není jedinou entitou, ale popisem služby, který zahrnuje sekvenci od okamžiku vstupu hovoru do mobilní sítě až po jeho přijetí, přesměrování nebo odmítnutí. Definuje očekávané chování síťových prvků, jako je Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo uzly IP Multimedia Subsystem (IMS), v reakci na tuto událost.

Technické fungování INC zahrnuje několik klíčových fází. Nejprve funkce směrování hovoru identifikuje obsluhující síť a uzel (např. MSC nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro volaného účastníka. Obsluhující uzel následně načte profil služeb účastníka, který obsahuje klíčová data, jako jsou nastavení přesměrování hovorů, seznamy zákazů a aktuální registrační stav (např. volný, obsazený, nedostupný). Na základě tohoto profilu síť provede servisní logiku. To může zahrnovat odeslání žádosti o paging pro lokalizaci mobilního zařízení, aplikaci bezpodmínečného přesměrování hovoru ([CFU](/mobilnisite/slovnik/cfu/)) nebo přesměrování při obsazení ([CFB](/mobilnisite/slovnik/cfb/)), nebo přehrání hlášení, pokud je účastníkovi zakázáno přijímat hovory.

V kontextu architektury jádra sítě jsou procedury INC nedílnou součástí protokolů Call Control ([CC](/mobilnisite/slovnik/cc/)) a Mobility Management ([MM](/mobilnisite/slovnik/mm/)). Pro hovory v přepojování okruhů ([CS](/mobilnisite/slovnik/cs/)) je ústřední entitou MSC, která používá signalizaci [ISUP](/mobilnisite/slovnik/isup/) nebo BICC pro propojení trunek a protokoly MAP pro dotazování HLR na informace o směrování. Pro IMS-based Voice over LTE (VoLTE) nebo Voice over NR (VoNR) je INC zpracováván S-CSCF, který funguje jako bod servisního řízení, provádí initial Filter Criteria (iFC) z profilu účastníka a orchestruje SIP signalizaci směrem k User Equipment (UE). Definice INC zajišťuje, že bez ohledu na podkladový přenos (CS nebo PS) je uživatelský zážitek z pohledu volajícího – vyzváněcí tóny, přesměrování, přesměrování do hlasové schránky – konzistentní a spolehlivý.

## K čemu slouží

Účelem standardizace konceptu INcoming Call (INC) je zajistit interoperabilitu a konzistentní uživatelský zážitek napříč sítěmi různých výrobců a mezi různými generacemi mobilní technologie (např. GSM, UMTS, LTE, 5G). Před takovou standardizací mohla proprietární řešení vést k nekompatibilnímu chování při zpracování hovorů, což způsobovalo neúspěšná zřízení hovorů, neočekávaná přesměrování nebo nekonzistentní poskytování tónů při roamování mezi sítěmi. Definováním INC v technické specifikaci poskytuje 3GPP vzor, který musí výrobci zařízení a síťoví operátoři dodržovat.

Historicky koncept vychází z potřeby abstrahovat složitou logiku zpracování hovorů od fyzického přepojovacího hardware. V raných digitálních ústřednách bylo zpracování hovorů těsně svázáno se softwarem ústředny. Servisně orientovaný přístup 3GPP, patrný od GSM výše, oddělil servisní logiku (jako je zpracování příchozího hovoru) od řízení spojení. Toto oddělení umožnilo flexibilnější zavádění nových služeb a plynulejší vývoj od CS k volání založenému na IMS. Definice INC řeší základní problém, jak má síť lokalizovat mobilního uživatele, aplikovat jeho odebírané služby a vytvořit přenosovou cestu, a to vše při dodržování regulatorních požadavků, jako je zákonné odposlouchávání a priorita tísňových hovorů.

Její pokračující relevance až po Release 19 zdůrazňuje, že navzdory přechodu na plně IP sítě zůstává základní telefonní služba přijetí hovoru prvořadá. Procedury INC se vyvinuly tak, aby zahrnovaly IMS funkce jako interakce s Session Border Controller (SBC), vylepšení směrování tísňových hovorů (např. pro IoT zařízení) a integraci s network slicing pro mission-critical voice, ale základní účel – spolehlivé dokončení hovoru k účastníkovi – zůstává nezměněn.

## Klíčové vlastnosti

- Definuje end-to-end signalizační tok pro zřízení mobilně ukončeného hovoru
- Zahrnuje provedení servisní logiky účastníka (např. přesměrování hovoru, zákazy)
- Integruje se s procedurami mobility managementu, jako je paging a aktualizace polohy
- Podporuje jak protokoly řízení hovorů pro přepojování okruhů (ISUP/BICC), tak přepojování paketů (SIP)
- Poskytuje rámec pro interakci s HLR/HSS pro získání dat účastníka a informací o směrování
- Umožňuje konzistentní uživatelský zážitek prostřednictvím standardizovaných tónů a hlášení o postupu hovoru

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 27.002** (Rel-19) — Terminal Adaptation Functions for Asynchronous Services

---

📖 **Anglický originál a plná specifikace:** [INC na 3GPP Explorer](https://3gpp-explorer.com/glossary/inc/)
