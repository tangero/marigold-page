---
slug: "rsu"
url: "/mobilnisite/slovnik/rsu/"
type: "slovnik"
title: "RSU – Road Side Unit"
date: 2025-01-01
abbr: "RSU"
fullName: "Road Side Unit"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsu/"
summary: "Road Side Unit (RSU) je komunikační infrastrukturní komponenta instalovaná na straně vozovky, která umožňuje služby Vehicle-to-Everything (V2X). Zprostředkovává přímou a síťovou komunikaci mezi vozidl"
---

RSU je komunikativní infrastrukturní komponenta na straně vozovky, která umožňuje služby Vehicle-to-Everything (V2X) pro přímou a síťovou komunikaci mezi vozidly, chodci a dopravními systémy.

## Popis

Road Side Unit (RSU) je klíčový element v ekosystémů Cellular Vehicle-to-Everything (C-V2X), standardizovaný 3GPP pro podporu inteligentních dopravních systémů ([ITS](/mobilnisite/slovnik/its/)). Typicky je instalován na straně vozovky, například na křižovatkách, dálnicích nebo parkovacích zónách, a funguje jako komunikační hub. RSU využívá přímou komunikaci (PC5 interface) i síťovou komunikaci (Uu interface) pro výměnu zpráv s vozidly ([V2V](/mobilnisite/slovnik/v2v/)), chodci (V2P), infrastrukturou (V2I) a sítí (V2N).

Architektonicky se RSU skládá z hardwarových a softwarových komponent, zahrnujících procesorové jednotky, paměť, moduly pro bezdrátovou komunikaci (podporující LTE nebo NR), senzory (např. kamery, radar) a backhaulovou konektivitu (např. optická vlákna, bezdrátová). Provozuje aplikace pro řízení dopravy, bezpečnostní varování a agregaci dat. RSU využívá protokoly definované ve specifikacích 3GPP, jako je aplikační vrstva [V2X](/mobilnisite/slovnik/v2x/) pro formát zpráv (např. Cooperative Awareness Messages, Decentralized Environmental Notification Messages) a protokoly přístupové vrstvy pro radiový přenos.

Jak funguje: RSU vysílají bezpečnostní informace (např. stav světelného signalizačního zařízení, varování o nebezpečí na vozovce) do blízkých vozidel prostřednictvím PC5 sidelink komunikace, která pracuje ve vyhrazených ITS kmitočtových pásmech jako 5,9 GHz. Také přenášejí data do centrálních systémů řízení dopravy prostřednictvím Uu interface využívající mobilní síť. Klíčové funkce zahrnují přeposílání zpráv, služby na základě polohy a caching dat. Například RSU může detekovat nehodu pomocí senzorů a ihned rozšířit varování k přibližujícím vozidlům, snížující riziko kolize.

V síti se RSU integrují s V2X aplikačními servery, edge computing platformami a funkcemi core networku. Podporují komunikaci s nízkou latencí, kritickou pro real-time bezpečnostní aplikace. Pokročilé RSU v novějších releasech 3GPP mohou obsahovat [MEC](/mobilnisite/slovnik/mec/) (Multi-access Edge Computing) schopnosti pro lokální zpracování dat, minimalizující latenci. Jejich role se rozšiřuje na podporu autonomního řízení tím, že poskytují high-definition mapy a data o prostředí, což je činí nezbytnými pro budoucí dopravní síť.

## K čemu slouží

RSU byly vyvinuty k řešení rostoucí potřeby zvýšení bezpečnosti silničního provozu, efektivity dopravy a podpory autonomních vozidel. Tradiční dopravní systémy závisely na pasivní infrastruktuře s omezenou komunikací, vedoucí k vysoké míře nehod a kongescí. RSU umožňují proaktivní, connected prostředí, kde vozidla a infrastruktura sdílí real-time informace k prevenci nehod a optimalizaci dopravního proudu.

Vytvoření RSU ve standardech 3GPP bylo motivováno evolucí [V2X](/mobilnisite/slovnik/v2x/) komunikace od dedicated short-range communication (DSRC) k řešení na základě mobilních sítí. Od Release 14 3GPP zaváděl C-V2X pro využití existujících mobilních sítí k širšímu pokrytí a reliabilitě. RSU řeší omezení ad-hoc vozidlových sítí tím, že poskytují pevné, napájené uzly, které zajišťují kontinuální dostupnost služby, rozšířený komunikační dosah a integraci s síťovými služby.

Historicky, rané [ITS](/mobilnisite/slovnik/its/) systémy postrádaly interoperabilitu a škálovatelnost. RSU standardizované 3GPP poskytují unifikovaný framework pro globální nasazení, podporující bezpečnostní i nebezpečnostní aplikace jako platooning a řízení křižovatky. Řeší problémy jako awareness mimo dosah pohledu a kongesci síť tím, že fungují jako reliabilní intermediáři, nakonec přispívající k vizi smart cities a snížení silničních fatality.

## Klíčové vlastnosti

- Podporuje přímou PC5 sidelink komunikaci pro V2V/V2I
- Integruje s mobilními sítěmi prostřednictvím Uu interface pro V2N
- Vysílá bezpečnostní zprávy (CAM, DENM) v real-time
- Umožňuje komunikaci s nízkou latencí pro kritická varování
- Může obsahovat MEC schopnosti pro lokální zpracování dat
- Interoperabilní s různými V2X aplikačními servery

## Definující specifikace

- **TS 22.185** (Rel-19) — LTE Support for V2X Services Requirements
- **TS 22.186** (Rel-19) — Service requirements for enhanced V2X support
- **TR 22.885** (Rel-14) — LTE support for V2X services
- **TS 22.886** (Rel-16) — eV2X Use Cases and Requirements
- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.287** (Rel-19) — 5G V2X Architecture Enhancements
- **TR 23.785** (Rel-14) — Architecture enhancements for LTE V2X services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TR 26.985** (Rel-19) — Media Handling for Advanced V2X Services
- **TS 33.885** (Rel-14) — Security Study for V2X Services
- **TR 37.885** (Rel-15) — Study on V2X Evaluation Methodology for LTE/NR
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR
- **TR 38.913** (Rel-19) — Next Gen Access Tech Scenarios & Requirements

---

📖 **Anglický originál a plná specifikace:** [RSU na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsu/)
