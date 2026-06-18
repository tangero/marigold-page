---
slug: "rnl"
url: "/mobilnisite/slovnik/rnl/"
type: "slovnik"
title: "RNL – Radio Network Layer"
date: 2025-01-01
abbr: "RNL"
fullName: "Radio Network Layer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rnl/"
summary: "Logická vrstva v architektuře protokolů řídicí roviny UTRAN a E-UTRAN, která obsahuje rádiově specifické protokoly jako RRC a RANAP. Je odpovědná za funkce související se správou rádiových zdrojů a mo"
---

RNL je logická vrstva v řídicích rovinách UTRAN a E-UTRAN obsahující rádiově specifické protokoly jako RRC a RANAP, odpovědná za správu rádiových zdrojů a funkce mobility.

## Popis

Rádiová síťová vrstva (RNL) je konceptuální vrstva v zásobníku protokolů řídicí roviny rádiových přístupových sítí 3GPP, konkrétně [UTRAN](/mobilnisite/slovnik/utran/) a [E-UTRAN](/mobilnisite/slovnik/e-utran/). Představuje soubor protokolů a funkcí, které jsou specificky spojeny s provozem rádiové sítě a jsou nezávislé na transportní technologii používané pro přenos signalizačních zpráv. RNL se nachází nad transportní síťovou vrstvou ([TNL](/mobilnisite/slovnik/tnl/)), která poskytuje spolehlivé transportní služby (např. přes IP, [ATM](/mobilnisite/slovnik/atm/) nebo [SCTP](/mobilnisite/slovnik/sctp/)). Toto oddělení je klíčovým architektonickým principem, který umožňuje navrhovat rádiové síťové protokoly bez závislosti na specifikách podkladového transportu.

V UTRAN zahrnuje RNL protokoly jako Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) na rozhraní Uu, Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) na rozhraní Iu, Radio Network Subsystem Application Part ([RNSAP](/mobilnisite/slovnik/rnsap/)) na rozhraní Iur a Node B Application Part (NBAP) na rozhraní Iub. Tyto protokoly provádějí základní funkce rádiové sítě. Například RRC zajišťuje navazování spojení, vysílání systémových informací a signalizaci předávání spojení (handover) s UE. RANAP se používá pro signalizaci mezi RNC a jádrem sítě (CN) a řeší procedury jako přiřazení rádiového přístupového kanálu (RAB), hlášení polohy a správu kontextu UE. Protokoly RNL definují konkrétní zprávy a procedury pro tyto funkce.

RNL komunikuje s transportní síťovou vrstvou přes jasně definované přístupové body služeb (SAP). TNL poskytuje službu přenosu pro zprávy RNL a řeší aspekty jako správa spojení, přenos dat a oprava chyb pro samotný transportní spoj. Tento vrstvený přístup zajišťuje, že logika rádiové sítě (např. jak se rozhodne a provede předání spojení) je oddělena od způsobu fyzického doručení povelu k předání mezi síťovými uzly. Stejný protokol RNL (např. RNSAP) může fungovat nad různými realizacemi TNL (např. na bázi IP nebo ATM). V E-UTRAN (LTE) tento princip pokračuje, přičemž protokoly jako S1-AP (na rozhraní S1) a X2-AP (na rozhraní X2) náleží do RNL a fungují nad TNL založenou na SCTP/IP.

## K čemu slouží

Koncept rádiové síťové vrstvy byl zaveden, aby zajistil jasné oddělení odpovědností při návrhu rádiových přístupových sítí 3GPP, počínaje UTRAN. Hlavní problém, který řeší, je nezávislost funkcí rádiové sítě na vyvíjejících se transportních technologiích. V počátcích 3G byly transportní sítě často založeny na ATM. Průmysl se však rychle posouval k plně IP sítím. Definováním samostatné RNL zajistilo 3GPP, že složité protokoly pro řízení rádiového přístupu (RRC, RANAP atd.) nebude nutné přepracovávat, pokud by se podkladová transportní technologie změnila z ATM na IP.

Tato abstrakce umožnila vytvořit architekturu, která je více připravena na budoucnost a flexibilní. Operátorům sítí umožňuje volbu a vývoj jejich transportních sítí nezávisle na softwaru a funkcích jejich rádiové sítě. TNL může být optimalizována z hlediska nákladů, kapacity a spolehlivosti na základě dostupné technologie (např. přechod z linek T1/E1 na Ethernetovou páteřní síť), aniž by to ovlivnilo logiku správy rádiových zdrojů nebo předávání spojení definovanou v RNL. Toto vrstvení navíc zjednodušuje návrh a testování protokolů, protože protokoly RNL mohou být specifikovány za předpokladu spolehlivé služby přenosu dat od spodní vrstvy. Tento princip byl přenesen z UTRAN do E-UTRAN a NG-RAN, což dokazuje jeho trvalou hodnotu v síťové architektuře.

## Klíčové vlastnosti

- Logická vrstva obsahující všechny rádiově specifické protokoly řídicí roviny (např. RRC, RANAP, S1-AP, X2-AP)
- Poskytuje úplnou nezávislost na technologii podkladové transportní síťové vrstvy (TNL)
- Definuje procedury a zprávy pro správu rádiových zdrojů, mobilitu a správu přenosových kanálů
- Komunikuje s TNL přes standardizované přístupové body služeb (SAP)
- Umožňuje fungování stejných funkcí rádiové sítě nad různými transportními technologiemi (např. ATM, IP)
- Základní architektonický koncept v zásobnících protokolů UTRAN i E-UTRAN

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.820** (Rel-8) — 3G Home NodeB Study Report
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.440** (Rel-19) — E-UTRAN MBMS Architecture Description
- **TS 36.456** (Rel-19) — SLm Interface Introduction
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [RNL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rnl/)
