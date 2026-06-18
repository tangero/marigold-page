---
slug: "cts-fp"
url: "/mobilnisite/slovnik/cts-fp/"
type: "slovnik"
title: "CTS-FP – Cordless Telephony System - Fixed Part"
date: 2025-01-01
abbr: "CTS-FP"
fullName: "Cordless Telephony System - Fixed Part"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cts-fp/"
summary: "CTS-FP je pevná komponenta základnové stanice systému bezšňůrové telefonie (CTS), což je standard 3GPP pro digitální bezšňůrovou telefonii. Poskytuje rádiové rozhraní a síťovou konektivitu pro mobilní"
---

CTS-FP je pevná komponenta základnové stanice systému bezšňůrové telefonie 3GPP, která zajišťuje rádiové rozhraní a síťovou konektivitu pro mobilní přístroje, a tím umožňuje poskytování služeb digitální bezšňůrové telefonie.

## Popis

Cordless Telephony System - Fixed Part (CTS-FP) je stacionární infrastrukturní prvek definovaný v rámci standardů systému bezšňůrové telefonie 3GPP ([CTS](/mobilnisite/slovnik/cts/)). Funguje jako základnová stanice nebo přístupový bod, která vytváří a udržuje rádiové spojení s Cordless Telephony System - Mobile Part (CTS-MP), což je uživatelský přístroj. Architektonicky CTS-FP tvoří kritický most mezi doménou bezšňůrového rádiového přístupu a jádrem telefonní sítě. Obsahuje rádiový transceiver, jednotky pro zpracování signálu a řídicí logiku nezbytnou pro správu rádiového rozhraní, sestavování hovorů, předávání hovorů mezi buňkami (handover) a šifrování. V typické instalaci může být rozmístěno více jednotek CTS-FP pro pokrytí budovy nebo areálu, přičemž systém podporuje předávání hovorů mezi nimi při pohybu uživatele.

Operačně CTS-FP spravuje celý protokolový zásobník pro rádiové rozhraní CTS, jak je specifikováno v 3GPP TS 43.052. To zahrnuje fyzickou vrstvu (modulaci, rámování), spojovou vrstvu pro spolehlivé připojení a síťovou vrstvu pro řízení hovorů a správu mobility. [FP](/mobilnisite/slovnik/fp/) je zodpovědné za skenování a výběr rádiových kanálů, autentizaci mobilní části ([MP](/mobilnisite/slovnik/mp/)), šifrování komunikace pro zabezpečení a správu rádiových zdrojů během hovoru. Také zajišťuje funkci pro vzájemné propojení (interworking), převádějící signalizaci a protokoly specifické pro CTS používané v rádiovém přenosu na standardní telefonní signalizaci (jako jsou protokoly [ISDN](/mobilnisite/slovnik/isdn/) nebo [PSTN](/mobilnisite/slovnik/pstn/)) používanou na jeho pevném síťovém rozhraní.

Jeho úlohou v síti je role specializovaného přístupového uzlu. Pro rezidenční použití může být jedna CTS-FP připojena přímo k linkě veřejné telefonní sítě (PSTN) přes analogové nebo ISDN rozhraní. V prostředí firemní ústředny ([PBX](/mobilnisite/slovnik/pbx/)) je více jednotek CTS-FP připojeno k PBX, čímž vytvářejí bezdrátové přípojky k firemní telefonní soustavě. Inteligence CTS-FP mu umožňuje představovat se síti jako standardní telefonní terminál, zatímco uživateli poskytuje pokročilé funkce bezšňůrové telefonie, jako je mobilita a předávání hovorů. Specifikace (42.056, 43.020, 43.052, 45.056) podrobně popisují jeho výkonnostní požadavky, rádiové aspekty a protokoly, čímž zajišťují interoperabilitu mezi zařízeními od různých výrobců.

## K čemu slouží

CTS-FP bylo vytvořeno za účelem standardizace pevné části systémů digitální bezšňůrové telefonie, což umožňuje interoperabilitu a podporuje konkurenční trh s příslušenstvím. Před jeho standardizací proprietární systémy bezšňůrových telefonů uzamykaly zákazníky do ekosystému jediného dodavatele pro přístroje i základnové stanice. Standardy [CTS](/mobilnisite/slovnik/cts/), včetně [FP](/mobilnisite/slovnik/fp/), si kladly za cíl replikovat úspěch interoperability GSM v oblasti bezšňůrové telefonie, což umožňuje uživatelům koupit CTS-MP od jednoho výrobce a používat jej s CTS-FP od jiného.

Řešil problém roztříštěné, nekvalitní analogové bezšňůrové technologie zavedením robustního, digitálně šifrovaného a spektrálně efektivního standardu. Historický kontext představuje konvergence telekomunikačních technologií na konci 90. let a počátku 21. století. CTS byla odpovědí 3GPP na populární standard DECT (Digital Enhanced Cordless Telecommunications), se specifickým zaměřením na bezproblémovou interoperabilitu se sítěmi GSM. CTS-FP byla klíčovou komponentou pro umožnění scénářů 'GSM Cordless', kde duální přístroj (CTS-MP/GSM) mohl využívat nízkopříkonové, kvalitní bezšňůrové připojení doma nebo v kanceláři přes CTS-FP a při přesunu venku plynule přejít na makro síť GSM. Tím se řešila omezení čistě celulárních nebo čistě proprietárních bezšňůrových systémů nabídkou integrované, pro uživatele transparentní mobility a optimalizovaného využití síťových zdrojů.

## Klíčové vlastnosti

- Standardizované digitální rádiové rozhraní pro interoperabilitu
- Podpora autentizace a šifrování komunikace na rádiovém rozhraní
- Správa mobility umožňující předávání hovorů mezi více jednotkami CTS-FP
- Funkce pro vzájemné propojení (interworking) pro připojení k sítím PSTN, ISDN nebo PBX
- Dynamický výběr kanálu a adaptivní řízení výkonu
- Implementace protokolového zásobníku pro řízení hovorů a doplňkové služby

## Související pojmy

- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)
- [GAN – Generative Adversarial Network](/mobilnisite/slovnik/gan/)
- [RAN – Radio Access Network](/mobilnisite/slovnik/ran/)

## Definující specifikace

- **TS 42.056** (Rel-19) — GSM Cordless Telephony System (CTS)
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.052** (Rel-19) — GSM Cordless Telephony System (CTS) Radio Interface
- **TS 45.056** (Rel-19) — GSM CTS-FP Radio Requirements

---

📖 **Anglický originál a plná specifikace:** [CTS-FP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cts-fp/)
