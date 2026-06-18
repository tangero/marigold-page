---
slug: "iwf"
url: "/mobilnisite/slovnik/iwf/"
type: "slovnik"
title: "IWF – InterWorking Function"
date: 2026-01-01
abbr: "IWF"
fullName: "InterWorking Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iwf/"
summary: "Obecná síťová funkce, která usnadňuje komunikaci a interoperabilitu služeb mezi různými síťovými doménami nebo technologiemi. Funguje jako překladač protokolů, brána nebo adaptér, umožňující bezproblé"
---

IWF je síťová funkce, která umožňuje komunikaci mezi různými síťovými doménami nebo technologiemi tím, že funguje jako překladač protokolů nebo brána pro bezproblémovou interoperabilitu a zpětnou kompatibilitu.

## Popis

InterWorking Function (IWF) je konceptuální a funkční entita v architekturách 3GPP, jejímž hlavním úkolem je zajistit interoperabilitu mezi odlišnými síťovými systémy. Nejde o jediný, monolitický uzel, ale o logickou funkci, která může být implementována v různých fyzických síťových prvcích v závislosti na konkrétním scénáři interoperability. IWF provádí nezbytné adaptace, včetně konverze protokolů, mapování zpráv, překladu signalizace a transkódování médií, aby překlenula technologické rozdíly. V podstatě skrývá rozdíly mezi propojenými sítěmi, což jim umožňuje vyměňovat si informace a poskytovat služby, jako by byly součástí homogenního systému.

Architektonicky se IWF nachází na hranici mezi dvěma síťovými doménami. Například v raných jádrech s přepojováním okruhů se IWF používala pro interoperabilitu mezi signalizací [MAP](/mobilnisite/slovnik/map/) v GSM a signalizací [DSS1](/mobilnisite/slovnik/dss1/) v [ISDN](/mobilnisite/slovnik/isdn/). V kontextu IP Multimedia Subsystem (IMS) může IWF usnadňovat interoperabilitu mezi sítěmi IMS založenými na [SIP](/mobilnisite/slovnik/sip/) a staršími telefonními sítěmi s přepojováním okruhů, přičemž zajišťuje převod mezi zprávami SIP a signalizačními protokoly [ISUP](/mobilnisite/slovnik/isup/)/BICC. Dalším klíčovým příkladem je funkce Interworking IMS (IW IMS) definovaná pro kontinuitu služeb mezi doménami IMS a ne-IMS. IWF obsahuje potřebnou aplikační logiku a stavové automaty pro interpretaci příchozích zpráv z jedné domény, mapování parametrů a informačních prvků na jejich ekvivalenty v cílové doméně a generování odpovídajících odchozích zpráv.

Z implementační perspektivy může být funkce IWF integrována do stávajících uzlů, jako je Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) pro interoperabilinu v rovině médií nebo Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) pro signalizační interoperabilitu v IMS. Spravuje klíčové úkoly, jako je překlad adres, vyjednávání a adaptace kodeků, koordinace zřizování přenosových cest a mapování doplňkových služeb. Její fungování je definováno v četných specifikacích 3GPP pokrývajících oblasti jako signalizace v jádru sítě, IMS, nouzové služby a zasílání zpráv. IWF je základním prvkem umožňujícím kontinuitu služeb, roaming a postupnou migraci ze starších sítí na nové systémy 3GPP, čímž zajišťuje, že účastníci mohou komunikovat a přistupovat ke službám napříč technologickými generacemi.

## K čemu slouží

IWF existuje k řešení základního problému heterogenity v telekomunikacích. Sítě se vyvíjejí přes generace (2G, 3G, 4G, — 5G) a koexistují s dalšími pevnými a bezdrátovými technologiemi. Bez funkcí pro interoperabilitu by tyto sítě byly izolovanými ostrovy, neschopnými komunikovat nebo sdílet služby. Vznik IWF byl motivován potřebou zpětné kompatibility během síťových přechodů a potřebou umožnit bezproblémové poskytování služeb napříč prostředími s více dodavateli a technologiemi.

Historicky jedna z prvních velkých potřeb po IWF vznikla se zavedením GSM, které vyžadovalo propojení s existujícími globálními pevnými sítěmi [PSTN](/mobilnisite/slovnik/pstn/)/ISDN. To vyžadovalo překlad mezi signalizací MAP specifickou pro GSM a signalizací ISUP používanou v pevných sítích. Jak se sítě vyvíjely k jádru s přepojováním paketů a IMS, objevily se nové výzvy interoperability, jako je připojení služeb VoIP založených na SIP k starší hlasové síti s přepojováním okruhů. IWF řeší omezení předchozích izolovaných přístupů tím, že poskytuje standardizovaný bod adaptace, definovaný ve specifikacích 3GPP, který umožňuje předvídatelné a interoperabilní připojení.

Koncept IWF navíc umožňuje konvergenci a inovace služeb. Umožňuje, aby nové síťové schopnosti (jako pokročilé komunikační služby v IMS) byly zpřístupněny uživatelům ve starších sítích, a naopak. Je klíčová pro nouzové volání, zákonný odposlech a roamingové scénáře, kdy musí uživatel v jednom typu sítě přistupovat ke službám v jiné. Tím, že abstrahuje složitost rozdílů v protokolech, IWF snižuje integrační náklady pro operátory a zajišťuje konzistentní uživatelský zážitek, což byl klíčový komerční a technický důvod pro její všudypřítomné použití ve standardech 3GPP.

## Klíčové vlastnosti

- Provádí konverzi protokolů a mapování zpráv mezi různými síťovými doménami (např. MAP na ISUP, SIP na ISUP)
- Umožňuje kontinuitu služeb a interoperabilitu napříč heterogenními sítěmi (3GPP, ne-3GPP, starší)
- Může být implementována jako samostatný uzel nebo integrována do stávajících síťových funkcí (např. MGCF, SGSN)
- Podle potřeby zvládá adaptaci jak v řídicí rovině (signalizace), tak v uživatelské rovině (média)
- Spravuje překlad adres, vyjednávání kodeků a koordinaci přenosových cest pro zřizování služeb od konce ke konci
- Poskytuje standardizovaný bod pro interoperabilitu regulačních funkcí (např. nouzové služby, zákonný odposlech)

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.054** (Rel-4) — Shared Interworking Function (SIWF) Stage 2
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.231** (Rel-19) — SIP-I based CS core network stage 2
- **TS 23.283** (Rel-20) — Mission Critical Communication Interworking
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.525** (Rel-19) — Business Trunking Architecture & Requirements
- **TS 24.883** (Rel-16) — MCPTT Interworking with LMR Systems
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/iwf/)
