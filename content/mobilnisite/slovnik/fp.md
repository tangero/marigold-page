---
slug: "fp"
url: "/mobilnisite/slovnik/fp/"
type: "slovnik"
title: "FP – Fixed Part"
date: 2025-01-01
abbr: "FP"
fullName: "Fixed Part"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fp/"
summary: "Pevná část (Fixed Part, FP) označuje infrastrukturní komponenty bezdrátového systému na straně sítě, na rozdíl od uživatelského mobilního zařízení. V historických kontextech 3GPP, jako je integrace DE"
---

FP (Fixed Part) je infrastrukturní komponenta bezdrátového systému na straně sítě, která zahrnuje základnové stanice a síťové řadiče a poskytuje síťovou konektivitu a řídicí funkce.

## Popis

Pevná část (Fixed Part, FP) je termín používaný ve specifikacích 3GPP, zejména v těch, které se zabývají integrací jiných rádiových technologií, jako je [DECT](/mobilnisite/slovnik/dect/) (Digital Enhanced Cordless Telecommunications). Označuje stacionární infrastrukturu bezdrátového síťového systému. Z architektonického hlediska je FP protikladem k přenosné části (Portable Part, PP), což je uživatelský mobilní terminál. FP typicky sestává z rádiových pevných částí (Radio Fixed Parts, RFP), což jsou základnové stanice nebo přístupové body, a z centrální řídicí jednotky nebo síťového řadiče, který spravuje více RFP.

Jeho fungování spočívá v tom, že FP poskytuje rádiové pokrytí a síťový přístupový bod pro PP. FP zajišťuje klíčové funkce, jako je řízení rádiových zdrojů, řízení hovorů, správu mobility v rámci své oblasti pokrytí (např. předávání mezi vlastními RFP) a propojení s páteřní sítí (jako je PSTN nebo jádro 3GPP prostřednictvím mezi-funkčních jednotek). Spravuje protokoly rozhraní vzduch, ověřuje PP a šifruje komunikaci. Ve scénáři vzájemného propojení (interworking) 3GPP funguje FP jako přístupová síť, přičemž jeho řadič překládá signalizaci specifickou pro DECT do protokolů páteřní sítě 3GPP.

Jeho úlohou bylo definovat jasnou funkční a architektonickou hranici ve specifikacích pro bezšňůrové systémy a systémy bezdrátové místní smyčky. Tím, že byly povinnosti FP specifikovány odděleně od PP, mohly normy zajistit interoperabilitu mezi infrastrukturou jednoho výrobce a ručními přístroji jiného výrobce. V širším ekosystému 3GPP specifikace podrobně popisující požadavky na FP zajišťovaly, že pokud byly takové přístupové technologie použity, mohly být integrovány standardizovaným způsobem pro poskytování služeb prostřednictvím páteřní sítě 3GPP.

## K čemu slouží

Termín Fixed Part (Pevná část) vznikl ve standardech bezšňůrové telekomunikace, jako je [DECT](/mobilnisite/slovnik/dect/), aby jasně oddělil síťovou infrastrukturu od uživatelského zařízení. Jeho přijetí do specifikací 3GPP mělo za cíl usnadnit standardizaci vzájemného propojení mezi mobilními sítěmi 3GPP a existujícími, široce rozšířenými bezšňůrovými systémy. To operátorům umožnilo využít DECT pro pokrytí v interiérech nebo pro pevný bezdrátový přístup a zároveň integrovat správu účastníků a služeb s jejich jádrem GSM/UMTS.

Řešil potřebu standardizovaného architektonického modelu při začleňování rádiových přístupových technologií nepocházejících od 3GPP. Před takovými definicemi byla integrace proprietární a omezená. Definování FP a jeho rozhraní (např. rozhraní 'A' mezi komponentami FP, rozhraní vzduch k PP a mezifunkční rozhraní k páteřní síti) vytvořilo vzor pro konzistentní implementaci. To podporovalo scénáře, jako je použití DECT jako rádiové části místní smyčky (RLL) k poskytování telefonní služby, kde se FP připojuje k tradiční telefonní síti, nebo později k jádru IMS 3GPP pro služby VoIP.

## Klíčové vlastnosti

- Zahrnuje infrastrukturu, jako jsou základnové stanice (RFP) a řadiče
- Poskytuje rádiové pokrytí a síťový přístup pro přenosné části (Portable Parts, PP)
- Spravuje rádiové zdroje, ověřování a šifrování pro své rozhraní vzduch
- Zajišťuje správu mobility v rámci vlastní sítě RFP
- Obsahuje mezi-funkční jednotky pro připojení k páteřním sítím 3GPP nebo jiným
- Definován v protikladu k uživatelsky ovládané přenosné části (Portable Part, PP)

## Související pojmy

- [DECT – Digital Enhanced Cordless Telecommunications](/mobilnisite/slovnik/dect/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 25.419** (Rel-19) — Service Area Broadcast Protocol (SABP)
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification

---

📖 **Anglický originál a plná specifikace:** [FP na 3GPP Explorer](https://3gpp-explorer.com/glossary/fp/)
