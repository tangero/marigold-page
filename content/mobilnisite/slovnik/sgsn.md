---
slug: "sgsn"
url: "/mobilnisite/slovnik/sgsn/"
type: "slovnik"
title: "SGSN – Serving GPRS Support Node"
date: 2025-01-01
abbr: "SGSN"
fullName: "Serving GPRS Support Node"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sgsn/"
summary: "Serving GPRS Support Node (SGSN) je prvek jádra sítě v mobilních sítích 2G/3G odpovědný za paketově orientované datové služby. Spravuje mobilitu, správu relací a autentizaci uživatelů pro účastníky GP"
---

SGSN je uzel jádra sítě odpovědný za správu mobility, správu relací a autentizaci pro paketově orientované datové služby v sítích 2G/3G GPRS a UMTS.

## Popis

Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) je základní entita jádra sítě v sítích GSM/GPRS a UMTS, určená pro paketově orientované datové služby. Slouží jako centrální bod řízení a směrování pro datovou relaci mobilního účastníka v rámci pokrytí sítě. Mezi hlavní role SGSN patří správa mobility, správa relací a autentizace a autorizace uživatele pro přístup k paketovým datům. Fyzicky je připojen k rádiové přístupové síti (RAN) – konkrétně k podsystému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)) v GSM/GPRS nebo k řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS – prostřednictvím rozhraní Gb nebo Iu-PS. Také se připojuje k Gateway GPRS Support Node (GGSN) přes rozhraní Gn, které poskytuje bránu k externím paketovým datovým sítím, jako je Internet.

Z funkčního pohledu SGSN funguje tak, že udržuje kontext pro každého připojeného účastníka GPRS/UMTS. Když se mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) připojí k síti pro paketové datové služby, SGSN uživatele autentizuje pomocí informací z domovského registru polohy ([HLR](/mobilnisite/slovnik/hlr/)) nebo z autentizačního centra (AuC). Poté vytvoří [PDP](/mobilnisite/slovnik/pdp/) (Packet Data Protocol) kontext, což je logická asociace mezi MS, SGSN a GGSN, která definuje parametry jako přiřazená IP adresa a profil QoS. Pro správu mobility SGSN sleduje polohu MS na úrovni směrovací oblasti (skupiny buněk) a zpracovává aktualizace směrovací oblasti při pohybu uživatele. Směruje příchozí datové pakety z GGSN ke správnému prvku RAN na základě aktuální polohy uživatele a směruje odchozí pakety z MS směrem k GGSN.

Architektura SGSN zahrnuje několik klíčových logických komponent: funkci správy mobility, která zpracovává připojení/odpojení a aktualizace polohy; funkci správy relací, která řídí aktivaci, modifikaci a deaktivaci PDP kontextu; a funkci směrování a přenosu paketů. Také provádí účtovací funkce, shromažďuje data pro fakturaci na základě objemu nebo času a komunikuje s účtovacími systémy. V UMTS se role SGSN rozšířila o sofistikovanější správu QoS v souladu s přenosovými službami UMTS. Během své dlouhé evoluce od Release 99 byla SGSN nedílnou součástí umožňování mobilního přístupu k internetu, [MMS](/mobilnisite/slovnik/mms/) a dalších paketových datových služeb před úplnou migrací na LTE/EPC. Představuje jádro paketově orientované domény v sítích před 4G a spolupracuje s GGSN k poskytování kompletní datové služby.

## K čemu slouží

SGSN byl vytvořen, aby do původně hlasově orientovaných sítí GSM zavedl možnosti paketově orientovaných dat. Před [GPRS](/mobilnisite/slovnik/gprs/) (General Packet Radio Service) nabízelo GSM pouze okruhově orientovaná data, která byla neefektivní pro přerušovaný internetový provoz. Motivací pro SGSN bylo umožnit efektivní, trvale připojené IP datové služby přes GSM, což vedlo k mobilnímu e-mailu, prohlížení webu a raným mobilním aplikacím. Řešil problém správy paketových datových relací mobilních účastníků, včetně jejich mobility a autentizace, v rámci infrastruktury buněčné sítě.

Historický kontext představuje přechod na mobilní data 2,5G/3G. SGSN spolu s GGSN tvořily jádro sítě GPRS, což umožnilo sítím GSM využívat paketové přepojování a dynamicky sdílet rádiové zdroje mezi uživateli, což dramaticky zlepšilo efektivitu dat oproti vyhrazeným okruhům. Řešil omezení, jako byla neschopnost nativně zpracovat IP mobilitu a kontinuitu relace. Pro UMTS se SGSN vyvinul, aby podporoval novou UMTS RAN a vylepšené mechanismy QoS, což usnadnilo bohatší datové služby. Jeho trvalá přítomnost v mnoha vydáních podtrhuje jeho roli jako základního kamene mobilních paketových dat před novou koncepcí LTE/EPC, kde byly jeho funkce přerozděleny na MME a S-GW.

## Klíčové vlastnosti

- Správa mobility pro účastníky s paketově orientovanými službami (připojení/odpojení, aktualizace polohy/směrovací oblasti)
- Správa relací včetně aktivace, modifikace a deaktivace PDP kontextu
- Autentizace a autorizace uživatele pro přístup k paketovým datům
- Směrování a přenos paketů mezi RAN (Gb/Iu-PS) a GGSN (Gn)
- Sběr účtovacích dat pro paketové datové služby
- Správa QoS pro přenosové služby UMTS

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [MM – Mobility Management](/mobilnisite/slovnik/mm/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.119** (Rel-19) — Gateway Location Register (GLR) Stage 2 Description
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- … a dalších 63 specifikací

---

📖 **Anglický originál a plná specifikace:** [SGSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/sgsn/)
