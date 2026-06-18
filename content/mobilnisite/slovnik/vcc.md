---
slug: "vcc"
url: "/mobilnisite/slovnik/vcc/"
type: "slovnik"
title: "VCC – Voice Call Continuity"
date: 2025-01-01
abbr: "VCC"
fullName: "Voice Call Continuity"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/vcc/"
summary: "Voice Call Continuity (VCC) je služba 3GPP, která umožňuje plynulé předávání hovorů mezi sítěmi s přepojováním okruhů (CS) (jako GSM/UMTS) a sítěmi s přepojováním paketů (PS) založenými na IP Multimed"
---

VCC je služba 3GPP, která umožňuje plynulý předávání hovorů mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů založenými na IMS, aby byla zajištěna nepřerušená hlasová služba napříč různými přístupovými technologiemi.

## Popis

Voice Call Continuity (VCC) je standardizovaná služba definovaná 3GPP pro zajištění kontinuity hlasových hovorů při přechodu uživatelského zařízení (UE) mezi doménami s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) (např. tradiční mobilní sítě používající GSM nebo UMTS) a doménami s přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)) (např. sítě založené na IMS přes LTE, Wi-Fi nebo pevný broadband). Základní funkcí je přenos probíhajícího hovoru z jedné domény do druhé bez přerušení, což poskytuje plynulý zážitek. Z architektonického hlediska se VCC opírá o jádro IMS pro řízení a využívá specifické funkční entity: aplikační server VCC (VCC [AS](/mobilnisite/slovnik/as/)) slouží jako kotvící bod hovoru a spravuje výběr domény a logiku předávání; funkce adaptace na CS ([CSAF](/mobilnisite/slovnik/csaf/)) usnadňuje interakci se staršími CS sítěmi; a UE obsahuje VCC schopnosti pro pomoc při detekci domény a procedurách předávání. Služba je specifikována napříč více vydáními 3GPP, s podrobnými protokoly ve specifikacích jako 23.206 a 24.206.

Jak VCC funguje, zahrnuje několik fází: zahájení hovoru, výběr domény a provedení předávání. Nejprve, když UE uskuteční nebo přijme hovor, VCC AS určí optimální doménu (CS nebo PS) na základě faktorů jako dostupnost sítě, uživatelské preference a zásady služby. Hovor je ukotven ve VCC AS, což znamená, že veškerá média a signalizace jím procházejí. Během aktivního hovoru, pokud UE zjistí, že je dostupná lepší doména (např. při přechodu z Wi-Fi na mobilní pokrytí), zahájí předávání. Při předávání z CS na PS UE vytvoří PS větev k VCC AS při zachování CS větve; VCC AS poté propojí média a přepne vzdálenou stranu na novou větev před uvolněním staré. Naopak při předávání z PS na CS se nastaví CS větev. Mezi klíčové protokoly patří [SIP](/mobilnisite/slovnik/sip/) pro signalizaci IMS, [ISUP](/mobilnisite/slovnik/isup/)/BICC pro CS signalizaci a [RTP](/mobilnisite/slovnik/rtp/) pro přenos médií, s vylepšeními pro synchronizaci minimalizující přerušení zvuku.

Role VCC v síti spočívá v překlenutí mezery mezi staršími CS hlasovými službami a nově vznikajícími plně IP sítěmi, což usnadňuje přechod na hlasová řešení založená na IMS, jako je VoLTE. Zajišťuje kontinuitu služby při mobilitě, což je klíčové pro přijetí nových přístupových technologií uživateli. VCC také podporuje funkce jako provoz s dvojím rádiem (kdy UE může komunikovat současně přes CS i PS) a provoz s jedním rádiem (kdy UE přepíná rádia, což vyžaduje rychlejší předávání). Oddělením služby od přístupové sítě umožňuje VCC operátorům využívat heterogenní sítě (HetNets) a přesouvat provoz na Wi-Fi, čímž zlepšuje kapacitu a pokrytí při zachování kvality hlasu. Jeho implementace zahrnuje těsnou integraci s IMS podpůrnými prvky, jako je aplikační server Service Centralization and Continuity ([SCC](/mobilnisite/slovnik/scc/) AS), který se z konceptů VCC vyvinul v pozdějších vydáních pro podporu bohatší kontinuity multimédií.

## K čemu slouží

Voice Call Continuity (VCC) byla vytvořena, aby řešila výzvu udržení kontinuity hlasové služby při vývoji mobilních sítí od architektur s přepojováním okruhů k architekturám s přepojováním paketů. Se zavedením IMS a plně IP sítí jako LTE čelili operátoři problému přerušování hovorů při pohybu uživatelů mezi CS pokrytím (např. 2G/3G) a PS pokrytím (např. LTE nebo Wi-Fi). To byla významná překážka pro přijetí nových technologií, protože uživatelé očekávali spolehlivou hlasovou službu. VCC, zavedená ve vydání 3GPP Release 7, to vyřešila poskytnutím standardizovaného mechanismu pro plynulé předávání mezi doménami, čímž zajistila, že hlas – kritická služba – zůstal nepřerušený během přechodů.

Historický kontext VCC zahrnuje raná nasazení IMS a potřebu konvergence mezi pevnými a mobilními sítěmi. Před VCC existovala proprietární řešení, ale postrádala interoperabilitu a škálovatelnost. VCC standardizovala procedury, což umožnilo nasazení od více dodavatelů a snížilo složitost pro operátory. Také řešila omezení předchozích přístupů, jako je Voice over IP (VoIP) přes Wi-Fi, které často trpěly zpožděním nebo selháním předávání při opuštění Wi-Fi pokrytí. Ukotvením hovorů v jádru IMS poskytlo VCC síťově řízené předávání, které mohlo využívat jak CS, tak PS zdroje, čímž zlepšilo spolehlivost a uživatelský zážitek.

Motivováno snahou o konvergenci sítí a konečným vyřazením CS sítí, VCC usnadnilo migraci k plně IP službám. Umožnilo operátorům zavádět hlas založený na IMS postupně, přičemž se stále mohli spoléhat na CS pro pokrytí v oblastech, kde byly PS sítě nedostatečně rozvinuté. To snížilo náklady a rizika nasazení. V průběhu vydání se koncepty VCC vyvinuly v širší řešení kontinuity, jako je Single Radio Voice Call Continuity (SRVCC) pro předávání z LTE na 3G a vylepšené VCC pro multimediální služby. Účel VCC se tedy rozšiřuje za bezprostřední předávání – podkládá dlouhodobou strategii pro jednotné komunikace, umožňuje operátorům poskytovat konzistentní kvalitu hlasu napříč různými přístupovými technologiemi a připravuje cestu pro pokročilé služby jako VoLTE a VoWi-Fi.

## Klíčové vlastnosti

- Plynulé předávání aktivních hlasových hovorů mezi CS a PS doménami
- Kotvení založené na IMS prostřednictvím aplikačního serveru VCC pro řízení hovoru
- Podpora pro režimy provozu s dvojím i jedním rádiem
- Výběr domény na základě stavu sítě a zásad
- Integrace se staršími CS sítěmi prostřednictvím adaptačních funkcí
- Minimalizované přerušení zvuku během předávání

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 22.892** (Rel-8) — IMS Centralized Services Study
- **TR 22.937** (Rel-13) — FMC requirements for 3GPP-WLAN service continuity
- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.826** (Rel-9) — Voice Call Continuity for Emergency Calls
- **TS 23.892** (Rel-8) — IMS Centralized Services Control
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.216** (Rel-19) — Communication Continuity Management Object
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.849** (Rel-13) — IMS Roaming Charging Study
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study
- **TS 33.838** (Rel-11) — Study on Protection against Unsolicited Communication for IMS

---

📖 **Anglický originál a plná specifikace:** [VCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vcc/)
