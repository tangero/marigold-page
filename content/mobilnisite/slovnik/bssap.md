---
slug: "bssap"
url: "/mobilnisite/slovnik/bssap/"
type: "slovnik"
title: "BSSAP – Base Station Subsystem Application Part"
date: 2025-01-01
abbr: "BSSAP"
fullName: "Base Station Subsystem Application Part"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/bssap/"
summary: "BSSAP je signalizační protokol používaný v sítích GSM a UMTS pro správu komunikace mezi podsystémem základnových stanic (BSS) a ústřednou pro mobilní spojení (MSC). Zpracovává klíčové funkce jako zřiz"
---

BSSAP je signalizační protokol používaný v sítích GSM a UMTS pro správu komunikace mezi podsystémem základnových stanic (Base Station Subsystem) a ústřednou pro mobilní spojení (Mobile Switching Center) pro funkce jako zřizování hovorů a předávání spojení.

## Popis

Base Station Subsystem Application Part (BSSAP) je klíčový signalizační protokol v architektuře sítí GSM a UMTS, který funguje na rozhraní A mezi podsystémem základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) a ústřednou pro mobilní spojení ([MSC](/mobilnisite/slovnik/msc/)). Je součástí zásobníku protokolů signalizačního systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), konkrétně se nachází na aplikační vrstvě (vrstva 7) a využívá Signalizační spojovací řídicí část ([SCCP](/mobilnisite/slovnik/sccp/)) pro spojované i nespojované služby. BSSAP je zodpovědný za přenos veškeré aplikačně specifické signalizační informace potřebné pro správu rádiových prostředků a mobility mezi MSC, která zajišťuje řízení hovorů a přepojování, a BSS, která spravuje rádiové rozhraní s mobilními stanicemi.

BSSAP se dělí na dvě hlavní podkomponenty: Base Station Subsystem Management Application Part ([BSSMAP](/mobilnisite/slovnik/bssmap/)) a Direct Transfer Application Part ([DTAP](/mobilnisite/slovnik/dtap/)). BSSMAP zpracovává zprávy, které jsou vyhodnocovány samotným BSS, jako jsou ty týkající se správy rádiových prostředků, včetně žádostí o předání spojení, přidělování prostředků a vyhledávání. Tyto zprávy jsou interpretovány a realizovány řídicím počítačem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) uvnitř BSS. Naproti tomu DTAP slouží k transparentnímu přenosu zpráv mezi MSC a mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)), jako jsou zprávy pro řízení hovorů (např. zřízení, upozornění, ukončení), správu mobility (např. aktualizace polohy, autentizace) a správu relací. BSS jednoduše přeposílá DTAP zprávy bez interpretace jejich obsahu, čímž zajišťuje koncově-koncovou integritu signalizace mezi jádrem sítě a účastnickým zařízením.

Protokol funguje prostřednictvím řady definovaných procedur a toků zpráv. Například při hovoru iniciovaném mobilním zařízením odešle MS žádost o zřízení přes rádiové rozhraní do BSS, která ji zabalí do DTAP zprávy odeslané přes BSSAP do MSC. MSC následně žádost zpracuje, přidělí prostředky a může použít BSSMAP k pokynu BSS pro přidělení hovorového kanálu. Podobně pro předávání spojení BSSMAP usnadňuje výměnu měřicích hlášení a příkazů k předání mezi BSS a MSC, aby umožnila plynulé přechody mezi buňkami. Návrh BSSAP zajišťuje spolehlivé doručování signalizačních zpráv ve správném pořadí a podporuje základní síťové funkce, jako je řízení šifrování, správa přetížení a hlášení stavu zařízení.

V širší síťové architektuře je BSSAP základním kamenem pro okruhově přepínané služby, protože umožňuje interoperabilitu mezi síťovými prvky od různých výrobců standardizací rozhraní A. Spolupracuje s dalšími protokoly SS7, jako je MTP (Message Transfer Part) a SCCP, aby poskytoval směrování a přenos. Zatímco jeho primární doménou je GSM, BSSAP se používal i v UMTS pro kompatibilitu a operace mezi různými rádiovými přístupovými technologiemi (inter-RAT), ačkoli 3GPP později zavedlo pokročilejší protokoly, jako je RANAP pro rozhraní Iu v čistých sítích UMTS. Porozumění BSSAP je klíčové pro pochopení signalizace v legacy sítích, odstraňování problémů a vývoj směrem k plně IP sítím.

## K čemu slouží

BSSAP byl vytvořen, aby poskytl standardizovaný a spolehlivý signalizační mechanismus mezi podsystémem základnových stanic (BSS) a ústřednou pro mobilní spojení (MSC) v sítích GSM, který řešil potřebu efektivní správy rádiových prostředků a mobility v raných digitálních celulárních systémech. Před jeho zavedením proprietární rozhraní mezi základnovými stanicemi a ústřednami bránila interoperabilitě a nasazení od více dodavatelů, což zvyšovalo náklady a složitost pro operátory. BSSAP jako součást signalizačního rámce založeného na SS7 to vyřešil definováním jasného zásobníku protokolů na rozhraní A, což umožnilo plynulou komunikaci pro řízení hovorů, předávání spojení a správu účastníků.

Protokol byl motivován požadavky okruhově přepínaných hlasových a datových služeb, kde byla nezbytná koordinace mezi rádiovým přístupem a jádrem sítě v reálném čase. Umožnil MSC delegovat úkoly specifické pro rádiové rozhraní na BSS, přičemž si zachoval celkovou kontrolu, čímž optimalizoval výkon sítě a využití prostředků. Například BSSAP umožňoval funkce jako předávání spojení mezi buňkami, které bylo klíčové pro udržení kvality hovoru při pohybu uživatelů, a aktualizaci polohy, která podporovala roaming a kontinuitu služeb. Oddělením BSSMAP (pro správu na úrovni BSS) a DTAP (pro transparentní signalizaci mezi MS a MSC) poskytl flexibilní architekturu, která mohla evolvovat s vylepšeními sítě.

Historicky se BSSAP objevil se standardizací GSM na konci 80. a začátku 90. let 20. století a stal se základním prvkem pro sítě 2G. Řešil omezení analogových systémů, kterým chyběla robustní signalizace pro pokročilou mobilitu a zabezpečení. Jak se sítě vyvíjely směrem k UMTS, BSSAP byl zachován pro zpětnou kompatibilitu a vzájemné propojení mezi GSM a UMTS, což zajišťovalo plynulé přechody během migrace technologií. Jeho vytvoření položilo základy pro pozdější signalizační protokoly v 3GPP a zdůraznilo důležitost standardizovaných rozhraní v telekomunikacích.

## Klíčové vlastnosti

- Standardizovaná signalizace přes rozhraní A mezi BSS a MSC
- Rozdělen na BSSMAP pro správu rádiových prostředků a DTAP pro transparentní přenos zpráv
- Podporuje zřizování hovorů, předávání spojení, aktualizaci polohy a řízení šifrování
- Funguje nad zásobníkem protokolů SS7 s využitím SCCP pro přenos
- Umožňuje interoperabilitu v sítích GSM/UMTS od více dodavatelů
- Usnadňuje správu okruhově přepínaných hlasových a datových služeb

## Související pojmy

- [BSSMAP – Base Station Subsystem Management Application Part](/mobilnisite/slovnik/bssmap/)
- [DTAP – Direct Transfer Application Part](/mobilnisite/slovnik/dtap/)
- [SCCP – Signalling Connection Control Part](/mobilnisite/slovnik/sccp/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study
- **TS 49.008** (Rel-19) — BSSAP on E-interface for inter-MSC handover
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [BSSAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bssap/)
