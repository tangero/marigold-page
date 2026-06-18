---
slug: "lai"
url: "/mobilnisite/slovnik/lai/"
type: "slovnik"
title: "LAI – Location Area Identity"
date: 2025-01-01
abbr: "LAI"
fullName: "Location Area Identity"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lai/"
summary: "Jedinečný identifikátor pro oblast polohy (LA) ve veřejné pozemní mobilní síti (PLMN). Používá se ve správě mobility ke sledování a vyvolávání (paging) UE. Skládá se z mobilního kódu země (MCC), mobil"
---

LAI je jedinečný identifikátor pro oblast polohy (Location Area) v mobilní síti, který se skládá z mobilního kódu země (MCC), mobilního kódu sítě (MNC) a kódu oblasti polohy (LAC). Používá se pro správu mobility, například pro vyvolávání (paging).

## Popis

Location Area Identity (LAI) je základní identifikátor v okruhově spínané doméně a správě mobility sítí 2G (GSM), 3G (UMTS) a 4G (LTE). Jednoznačně identifikuje oblast polohy ([LA](/mobilnisite/slovnik/la/)), což je skupina buněk definovaná za účelem sledování polohy účastníka a efektivního vyvolávání (paging). LAI je klíčovou součástí kontextu polohy účastníka a síť jej vysílá v systémových informacích každé buňky. UE tyto vysílané informace čte a používá je k určení, zda vstoupila do nové LA, což spustí proceduru aktualizace oblasti polohy ([LAU](/mobilnisite/slovnik/lau/)), aby informovala síť o své nové poloze.

Struktura LAI je definována doporučením [ITU-T](/mobilnisite/slovnik/itu-t/) E.212 a skládá se ze tří částí: mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)), mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)) a kódu oblasti polohy ([LAC](/mobilnisite/slovnik/lac/)). MCC je tříciferný kód identifikující zemi (např. 234 pro Spojené království). MNC je dvou- nebo tříciferný kód identifikující mobilního operátora v dané zemi (např. 30 pro [EE](/mobilnisite/slovnik/ee/) UK). Společně tvoří MCC a MNC identitu [PLMN](/mobilnisite/slovnik/plmn/). LAC je kód pevné délky (obvykle 16 bitů, umožňující hodnoty od 0 do 65535) přidělený operátorem sítě k jednoznačné identifikaci oblasti polohy v rámci tohoto PLMN. Hodnoty LAC 0 a 65535 jsou často rezervovány.

Z pohledu provozu sítě je LAI uloženo v UE, ve Visitor Location Register (VLR) v 2G/3G a v Mobility Management Entity (MME) v 4G pro účely CSFB. Když je UE v klidovém stavu, síť zná pouze její aktuální oblast polohy, nikoliv konkrétní buňku. Pro doručení příchozího hovoru nebo SMS vyšle síť zprávu pro vyvolání (paging) do všech buněk v této LA. Tím se vyvažuje potřeba lokalizovat UE se signalizační zátěží potřebnou pro sledování. Když se UE pohybuje a detekuje změnu vysílaného LAI, iniciuje proceduru aktualizace oblasti polohy (LAU). Ta aktualizuje záznam v síti (ve VLR/MME) a může zahrnovat i autentizaci a šifrování. LAI je také klíčovým parametrem v Temporary Mobile Subscriber Identity (TMSI), které přiděluje VLR a které je v rámci dané oblasti LAI jedinečné pro zachování soukromí účastníka.

Přestože jeho role poklesla v paketově spínaném jádru 4G/5G, kde se pro správu mobility používají oblasti sledování (TA), zůstává LAI zásadní pro Circuit-Switched Fallback (CSFB) v LTE, kde jej LTE sítě používají pro mapování na oblasti polohy 2G/3G pro hlasové služby. Používá se také při zákonně povolených žádostech o informace o poloze. LAI je základním kamenem tradiční mobilní správy mobility v celulárních sítích, který umožňuje efektivní sledování účastníků a vyvolávání (paging) v rozsáhlých sítích.

## K čemu slouží

LAI bylo vytvořeno k vyřešení základního problému správy mobility v celulárních sítích: efektivně lokalizovat mobilního účastníka v klidovém stavu pro doručení příchozích hovorů nebo zpráv bez nutnosti neustálého sledování na úrovni buněk. Před zavedením takových konceptů založených na oblastech by síť musela vyvolávat účastníka v každé jednotlivé buňce, což by vytvářelo obrovskou a neudržitelnou signalizační režii.

Zavedení oblasti polohy a její identity (LAI) poskytlo elegantní řešení. Seskupením buněk do oblastí polohy potřebuje síť vědět pouze LA, kde je UE aktuálně registrována. Když přijde hovor, síť vyvolá UE ve všech buňkách této LA, což představuje zvládnutelnou signalizační zátěž. UE pomáhá tím, že hlásí překročení hranice LA prostřednictvím aktualizace oblasti polohy (LAU). Tato rovnováha mezi zátěží vyvolávání a aktualizační signalizací je optimalizována plánováním sítě. LAI jako strukturovaný, globálně jedinečný identifikátor zajišťuje jednoznačnou identifikaci těchto oblastí napříč různými zeměmi a operátory, což je nezbytné pro mezinárodní roaming. Tvořilo základ správy mobility v sítích 2G a 3G a ovlivnilo návrh pozdějších oblastních konceptů, jako jsou oblasti směrování (RA) pro GPRS a oblasti sledování (TA) v LTE/5G.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor pro oblast polohy (Location Area) v rámci PLMN
- Struktura: MCC (3 číslice) + MNC (2-3 číslice) + LAC (16 bitů)
- Vysíláno v systémových informacích buňky pro detekci UE
- Při změně spouští procedury aktualizace oblasti polohy (LAU)
- Používá se pro síťové vyvolávání (paging) UE v klidovém stavu v dané oblasti
- Integrální součást dočasné identity mobilního účastníka (TMSI)

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 43.020** (Rel-19) — Security Procedures for GSM
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [LAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lai/)
