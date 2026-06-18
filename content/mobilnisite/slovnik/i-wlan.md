---
slug: "i-wlan"
url: "/mobilnisite/slovnik/i-wlan/"
type: "slovnik"
title: "I-WLAN – Interworking Wireless Local Area Network"
date: 2025-01-01
abbr: "I-WLAN"
fullName: "Interworking Wireless Local Area Network"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/i-wlan/"
summary: "I-WLAN označuje standardizovanou architekturu a procedury 3GPP pro propojení mezi mobilními sítěmi 3GPP (jako GSM, UMTS, LTE) a bezdrátovými lokálními sítěmi (WLAN, např. Wi-Fi). Umožňuje bezproblémov"
---

I-WLAN je standardizovaná architektura 3GPP pro propojení mezi mobilními sítěmi a sítěmi WLAN, která umožňuje bezproblémový přístup k paketovým službám 3GPP a funkcím jádra sítě prostřednictvím Wi-Fi.

## Popis

Interworking Wireless Local Area Network (I-WLAN) je komplexní rámec 3GPP, původně zavedený ve verzi 6, který definuje, jak může uživatelské zařízení (UE) získávat přístup ke službám sítě 3GPP prostřednictvím přístupové sítě [WLAN](/mobilnisite/slovnik/wlan/). Nejde pouze o technologii vykládání přes Wi-Fi, ale o plnohodnotný systém propojení, který integruje WLAN do ekosystému jádra sítě 3GPP. Architektura zahrnuje několik klíčových síťových prvků: přístupovou síť WLAN (WLAN [AN](/mobilnisite/slovnik/an/)), bránu přístupu WLAN ([WAG](/mobilnisite/slovnik/wag/)), bránu paketových dat ([PDG](/mobilnisite/slovnik/pdg/)) a server 3GPP [AAA](/mobilnisite/slovnik/aaa/) (Authentication, Authorization, and Accounting).

Jádrem fungování I-WLAN je vytvoření tunelu [IPsec](/mobilnisite/slovnik/ipsec/) mezi UE a PDG umístěným v domovské síti 3GPP. Tento tunel, vytvořený přes přístup WLAN a jakékoli mezilehlé IP sítě, poskytuje zabezpečené spojení pro UE pro přístup k paketovým službám 3GPP a k internetu. Proces začíná autentizací přístupu k WLAN, která může být založena na metodách EAP-SIM/[AKA](/mobilnisite/slovnik/aka/), využívajících přihlašovací údaje [SIM](/mobilnisite/slovnik/sim/)/USIM z UE a zahrnujících server 3GPP AAA. Po úspěšné autentizaci UE zahájí proceduru navázání tunelu s PDG, což vede k vytvoření zabezpečeného tunelu IPsec. Veškerý provoz v uživatelské rovině je pak směrován tímto tunelem k PDG, která slouží jako brána k externím paketovým datovým sítím (PDN), včetně internetu a služeb operátora 3GPP, jako je IMS.

I-WLAN podporuje dva hlavní modely připojení: 'Přímý IP přístup' a 'IP přístup 3GPP'. Přímý IP přístup umožňuje UE dosáhnout internetu přímo přes WLAN, přičemž síť 3GPP je primárně zapojena do přístupové autentizace a účtování. IP přístup 3GPP je integrovanější model, kde je provoz z UE tunelován k PDG v domovské síti, což mu umožňuje přístup ke službám 3GPP (jako IMS) a přidělení IP adresy z pulu domovského operátora. Rámec také zahrnuje mechanismy pro účtování, řízení politik a mobilitu, ačkoli původní důraz byl kladen na nomadický nebo statický přístup spíše než na bezproblémový předávání spojení. I-WLAN položil základní základy pro pozdější, bezproblémovější integraci přístupu mimo 3GPP definovanou pro EPS a 5GS.

## K čemu slouží

I-WLAN byl vyvinut v polovině roku 2000 (verze 6) jako řešení rostoucího rozšíření hotspotů WLAN (Wi-Fi) a snahy mobilních operátorů integrovat tuto technologii v nelicencovaném spektru do své nabídky služeb. Před I-WLAN bylo používání Wi-Fi pro mobilní data většinou neřízené 'vykládání' bez integrace s jádrem sítě operátora, což vedlo k nesourodému uživatelskému zážitku, samostatným předplatným a žádné jednotné bezpečnosti či účtování. Operátoři chtěli využít stávající identitu předplatitele (SIM), autentizační infrastrukturu a fakturační systémy k nabídce integrovaných služeb WLAN.

Standardy I-WLAN to vyřešily tím, že poskytly zabezpečenou, operátorem řízenou metodu, jak předplatitelé mohou přistupovat k internetu i službám 3GPP přes WLAN. Umožnily operátorům nabízet jednotný balíček služeb, používat SIM-bazovanou autentizaci pro přístup k WLAN, uplatňovat konzistentní účtovací politiky a udržovat zabezpečené spojení zpět do domovské sítě. Zatímco I-WLAN původně nepodporoval bezproblémovou mobilitu (předávání spojení) mezi 3GPP a WLAN, stanovil klíčové architektonické principy – jako použití EAP-AKA pro autentizaci, tunelování k bráně domovské sítě (PDG) a ústřední roli serveru AAA – které byly později rozvíjeny a zdokonalovány. Řešil klíčový problém, jak zacházet s nedůvěryhodnými přístupovými sítěmi IP mimo 3GPP jako s rozšířením důvěryhodného mobilního jádra, což je koncept, který se stal základním pro Evolved Packet Core (EPC) s důvěryhodným/nedůvěryhodným přístupem mimo 3GPP a později pro 5G Core.

## Klíčové vlastnosti

- Umožňuje autentizaci pro přístup k WLAN založenou na SIM/USIM (EAP-SIM/AKA) prostřednictvím serveru 3GPP AAA
- Vytváří zabezpečené tunely IPsec mezi UE a bránou paketových dat (PDG) v domovské síti
- Podporuje dva režimy: Přímý IP přístup (pro internet) a IP přístup 3GPP (pro služby operátora)
- Poskytuje integrované účtování a řízení politik pro přístup přes WLAN prostřednictvím jádra 3GPP
- Pokládá základy pro přístup k IMS 3GPP a dalším paketovým službám přes WLAN
- Definuje bránu přístupu WLAN (WAG) a PDG jako klíčové síťové funkce pro propojení

## Související pojmy

- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)
- [PDG – Packet Data Gateway](/mobilnisite/slovnik/pdg/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.935** (Rel-13) — LCS Feasibility Study for 3GPP-WLAN Interworking
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 23.826** (Rel-9) — Voice Call Continuity for Emergency Calls
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 24.235** (Rel-12) — I-WLAN Interworking Management Object
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 29.161** (Rel-12) — 3GPP-WLAN Interworking Requirements
- … a dalších 3 specifikací

---

📖 **Anglický originál a plná specifikace:** [I-WLAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/i-wlan/)
