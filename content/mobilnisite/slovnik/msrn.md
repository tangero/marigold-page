---
slug: "msrn"
url: "/mobilnisite/slovnik/msrn/"
type: "slovnik"
title: "MSRN – Mobile Subscriber Roaming Number"
date: 2025-01-01
abbr: "MSRN"
fullName: "Mobile Subscriber Roaming Number"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msrn/"
summary: "Dočasné číslo ve formátu E.164 přidělené roamujícímu mobilnímu účastníkovi. Umožňuje veřejné pozemní mobilní síti (PLMN) směrovat příchozí hovory k ústředně MSC (Mobile Switching Center) navštívené sí"
---

MSRN je dočasné číslo ve formátu E.164 přidělené roamujícímu účastníkovi, které umožňuje směrování příchozích hovorů k navštívené ústředně MSC.

## Popis

Mobile Subscriber Roaming Number (MSRN) je klíčový identifikátor v okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) doméně sítí GSM a UMTS, primárně používaný pro směrování hovorů při volání mobilnímu účastníkovi v režimu roamingu. Jedná se o dočasné telefonní číslo odpovídající standardu E.164, které se přiděluje z fondu spravovaného navštívenou ústřednou [MSC](/mobilnisite/slovnik/msc/) ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) v síti, kde se účastník aktuálně nachází. MSRN není účastníkovi známo a používá se výhradně pro interní účely směrování v síti.

Při volání roamujícímu mobilnímu účastníkovi se Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) v síti volajícího dotazuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) účastníka na informace pro směrování. HLR, který zná aktuálně obsluhující VLR/MSC, od něj vyžádá přidělení MSRN. VLR přidělí dočasné MSRN ze svého číselného rozsahu a odešle jej zpět HLR, který jej předá GMSC. GMSC poté toto MSRN použije k směrování hovoru přes veřejnou telefonní síť ke konkrétní VMSC, která v daném okamžiku obsluhuje volaného účastníka.

Po úspěšném sestavení hovoru nebo po uplynutí časového limitu se MSRN uvolní zpět do fondu VLR pro opětovné použití. Tento mechanismus odděluje skutečné, trvalé telefonní číslo účastníka ([MSISDN](/mobilnisite/slovnik/msisdn/)) od směrovací logiky navštívené sítě, čímž vytváří vrstvu abstrakce, která zvyšuje soukromí a zjednodušuje správu sítě. MSRN je klíčovou součástí protokolu [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part), konkrétně se používá v procedurách Send Routing Information (SRI) a Provide Roaming Number (PRN) mezi HLR a VLR.

## K čemu slouží

MSRN bylo zavedeno, aby vyřešilo základní problém směrování hlasových hovorů k mobilnímu účastníkovi nacházejícímu se mimo geografické pokrytí jeho domovské sítě. V raných dobách mobilní telefonie bylo pevné telefonní číslo (MSISDN) vázáno na ústřednu v domovské síti účastníka. Bez dočasného směrovacího čísla by domovská síť neměla způsob, jak příchozí hovor nasměrovat k ústředně cizí sítě, kde se účastník fyzicky nachází.

Řeší omezení statického směrování zavedením dynamického přidělování čísel na bázi relace. To umožňuje efektivní využití číselných zdrojů, protože fond MSRN může být sdílen mezi všemi roamujícími účastníky v oblasti navštívené sítě, namísto vyžadování vyhrazeného trvalého čísla pro směrování při roamingu. Mechanismus MSRN také poskytuje určitou úroveň ochrany soukromí týkající se polohy účastníka, protože dočasné číslo volající síti prozradí pouze aktuálně obsluhující MSC/VLR, nikoliv přesnou polohu účastníka na úrovni buňky.

## Klíčové vlastnosti

- Dočasné přidělení čísla ve formátu E.164 pro účely směrování
- Dynamicky přidělováno z fondu VLR/MSC navštívené sítě
- Používáno výhradně pro doručení hovoru mobilnímu účastníkovi v režimu roamingu
- Klíčové pro MAP procedury, jako je Provide Roaming Number (PRN)
- Uvolněno po sestavení hovoru nebo časovém limitu pro opětovné použití
- Umožňuje abstrakci směrování mezi MSISDN a fyzickým obsluhujícím uzlem

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [MSRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/msrn/)
