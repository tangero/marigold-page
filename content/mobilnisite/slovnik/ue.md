---
slug: "ue"
url: "/mobilnisite/slovnik/ue/"
type: "slovnik"
title: "UE – User Equipment"
date: 2026-01-01
abbr: "UE"
fullName: "User Equipment"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ue/"
summary: "User Equipment (UE) je koncové uživatelské zařízení, například smartphone, tablet nebo modul pro IoT, které se připojuje k mobilní síti 3GPP. Obsahuje USIM pro autentizaci a podporuje rádiové rozhraní"
infografika: "/assets/slovnik/ue.svg"
infografikaAlt: "Schéma architektury 5G sítě se zvýrazněním UE"
---

UE je koncové uživatelské zařízení, například smartphone nebo modul pro IoT, které se připojuje k mobilní síti 3GPP pomocí rádiového rozhraní Uu a obsahuje USIM pro autentizaci.

## Popis

User Equipment (UE) je základní koncové uživatelské zařízení v mobilní síti 3GPP, které zahrnuje širokou škálu terminálů od smartphonů a tabletů po IoT senzory, modemy a komunikační jednotky ve vozidlech. V jádru je UE definováno podporou modulu Universal Subscriber Identity Module ([USIM](/mobilnisite/slovnik/usim/)) a rádiového rozhraní Uu, což je rozhraní mezi UE a pozemní rádiovou přístupovou sítí [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network) nebo, v pozdějších generacích, rozvinutým NodeB ([eNB](/mobilnisite/slovnik/enb/)) v LTE nebo gNB v 5G NR. Architektura UE je modulární a typicky se skládá z Mobile Equipment ([ME](/mobilnisite/slovnik/me/)), které obsahuje hardware a software pro rádiovou komunikaci, a USIM, což je aplikace na čipové kartě, která bezpečně ukládá identitu účastníka, autentizační klíče a profily služeb.

Z pohledu protokolového zásobníku UE implementuje kompletní uživatelské a řídicí protokoly potřebné pro komunikaci. To zahrnuje fyzickou vrstvu (Layer 1), která zajišťuje modulaci, kódování a [RF](/mobilnisite/slovnik/rf/) přenos; linkovou vrstvu (Layer 2) zahrnující podvrstvy jako [MAC](/mobilnisite/slovnik/mac/), [RLC](/mobilnisite/slovnik/rlc/) a [PDCP](/mobilnisite/slovnik/pdcp/) pro plánování, opravu chyb a zabezpečení; a síťovou vrstvu (Layer 3) včetně protokolu RRC pro řízení spojení a NAS protokolů pro signalizaci v jádru sítě. Schopnosti UE jsou hlášeny síti během registrace a mohou zahrnovat podporovaná kmitočtová pásma, rádiové přístupové technologie (RAT), maximální datové rychlosti a funkce jako agregace nosných nebo duální konektivita.

Úlohou UE je navazovat, udržovat a ukončovat spojení se sítí a poskytovat rozhraní pro přístup uživatele k hlasovým, datovým a multimediálním službám. Provádí klíčové procedury, jako je výběr a převýběr buňky, náhodný přístup, předávání spojení a řízení výkonu. V architektuře sítě je UE protistranou pro uzel rádiové přístupové sítě (RAN) (NodeB, eNB, gNB) a prostřednictvím NAS protokolů pro Mobility Management Entity (MME) nebo Access and Mobility Management Function (AMF) v jádru sítě. Jeho chování je řízeno specifikacemi, které zajišťují interoperabilitu, zabezpečení a efektivní využití rádiových prostředků napříč různými výrobci a operátory.

## K čemu slouží

UE existuje jako standardizovaný koncový bod, který účastníkům umožňuje přístup ke službám mobilní sítě. Jeho primárním účelem je poskytovat konzistentní, interoperabilní rozhraní mezi uživatelem a složitou síťovou infrastrukturou, které abstrahuje podkladové rádiové a síťové technologie jádra. Před standardizovanými UE proprietární terminály uzamkly uživatele ke konkrétním sítím, což bránilo konkurenci a roamingu. Definice UE v 3GPP, počínaje UMTS ve verzi 99, vytvořila globální ekosystém, kde zařízení od libovolného výrobce mohla fungovat na jakékoli kompatibilní síti, což podpořilo masové přijetí mobilních služeb.

UE řeší základní problém připojení mobilního účastníka k síti bezpečně a efektivně. Musí zvládat výzvy bezdrátového prostředí, jako je útlum signálu, interference a mobilita, a zároveň poskytovat spolehlivou službu aplikacím. Začlenění USIM je klíčové pro oddělení identity účastníka od hardwaru zařízení, což umožňuje přenositelnost předplatitelských dat a robustní zabezpečení založené na sdílených tajemstvích uložených na SIM a v Home Subscriber Server (HSS) sítě. Vývoj UE napříč verzemi 3GPP byl hnán potřebou podporovat nové služby, vyšší datové rychlosti, lepší spektrální účinnost a nižší latenci, od základního hlasu v 3G po rozšířené mobilní širokopásmové připojení a ultra-spolehlivou komunikaci s nízkou latencí v 5G.

## Klíčové vlastnosti

- Podporuje rádiové rozhraní Uu pro komunikaci s UTRAN, E-UTRAN nebo NG-RAN
- Obsahuje USIM pro bezpečnou autentizaci účastníka a uložení klíčů
- Implementuje kompletní protokolový zásobník 3GPP (Layer 1, Layer 2, Layer 3 včetně RRC a NAS)
- Hlásí síti podrobné informace o rádiových schopnostech (UE Capability Enquiry/Information)
- Provádí mobilní procedury jako výběr buňky, převýběr a předání spojení
- Podporuje více rádiových přístupových technologií (Multi-RAT) a režimy provozu (např. připojený, nečinný)

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 22.038** (Rel-19) — USIM Application Toolkit (USAT) Stage 1
- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1
- **TS 22.101** (Rel-20) — Service Principles for PLMNs
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.121** (Rel-5) — Virtual Home Environment Requirements
- **TS 22.129** (Rel-19) — Service Requirements for Handover & Service Continuity
- **TS 22.146** (Rel-19) — MBMS Stage 1 Description
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.233** (Rel-19) — Packet-switched Streaming Service (PSS) Stage 1
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TS 22.240** (Rel-19) — 3GPP Generic User Profile Requirements
- … a dalších 522 specifikací

---

📖 **Anglický originál a plná specifikace:** [UE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ue/)
