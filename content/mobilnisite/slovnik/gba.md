---
slug: "gba"
url: "/mobilnisite/slovnik/gba/"
type: "slovnik"
title: "GBA – Generic Bootstrapping Architecture"
date: 2026-01-01
abbr: "GBA"
fullName: "Generic Bootstrapping Architecture"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/gba/"
summary: "Bezpečnostní architektura, která umožňuje uživatelskému zařízení (UE) a síťovému aplikačnímu serveru navázat sdílené autentizační klíče. Využívá stávající 3GPP autentizační infrastrukturu (AKA) k 'nas"
---

GBA je bezpečnostní architektura, která umožňuje uživatelskému zařízení a síťovému aplikačnímu serveru navázat sdílené klíče využitím protokolu 3GPP AKA k nastartování zabezpečení pro aplikace nad HTTP.

## Popis

Generic Bootstrapping Architecture (GBA), označovaná také jako Generic Authentication Architecture ([GAA](/mobilnisite/slovnik/gaa/)), je standardizovaná bezpečnostní architektura definovaná 3GPP, která poskytuje metodu pro odvození sdílených relacích klíčů mezi uživatelským zařízením (UE) a síťovými aplikačními servery ([NAF](/mobilnisite/slovnik/naf/)). Znovu využívá robustní procedury autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)), které jsou již navázány mezi UE a Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) mobilní sítě. Hlavní myšlenkou je 'nastartovat' zabezpečení na aplikační vrstvě z této prověřené autentizace na síťové vrstvě, čímž vzniká důvěryhodné bezpečnostní spojení pro služby bez nutnosti, aby uživatelé spravovali další uživatelská jména a hesla.

Architektura zahrnuje několik klíčových funkčních entit: Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)), Network Application Function (NAF), Home Subscriber Server (HSS) a User Equipment (UE). Proces začíná bootstrapovací procedurou mezi UE a BSF. UE a BSF provedou vzájemnou autentizaci pomocí protokolu 3GPP AKA, kterou zprostředkovává HSS poskytující autentizační vektory. Po úspěšné autentizaci odvodí jak UE, tak BSF sdílený, relaci specifický klíč nazvaný Bootstrapping Transaction Identifier ([B-TID](/mobilnisite/slovnik/b-tid/)) a související klíčový materiál Ks. B-TID slouží jako reference k tomuto sdílenému tajemství.

Následně, když UE potřebuje přístup ke službě poskytované NAF (např. streamovací server nebo firemní portál), předloží NAF identifikátor B-TID. NAF se pak obrátí na BSF pomocí rozhraní Zn a poskytne mu B-TID. BSF ověří B-TID a pokud je platný, odvodí z hlavního klíče Ks a identifikátoru NAF klíč specifický pro daný NAF, Ks_NAF. BSF pak tento klíč Ks_NAF bezpečně zašle NAF. Nyní mají jak UE (které si může stejný Ks_NAF nezávisle odvodit), tak NAF sdílený tajný klíč. Mohou tento klíč použít k zabezpečení své komunikace, například jeho využitím v rámci TLS-PSK (Pre-Shared Key) nebo k vygenerování klíčů pro šifrování a ochranu integrity na aplikační vrstvě. Celý tento proces umožňuje jednotné přihlašování napříč různými službami hostovanými různými NAF, které jsou všechny zabezpečeny přihlašovacími údaji z uživatelovy [SIM](/mobilnisite/slovnik/sim/) karty.

## K čemu slouží

GBA byla vytvořena, aby řešila rostoucí potřebu bezpečné autentizace k internetovým aplikačním službám (jako je video streamování, e-mail nebo bankovnictví) přistupovaným z mobilních zařízení, aniž by byli uživatelé nuceni pamatovat si a zadávat samostatné přihlašovací údaje pro každou službu. Před GBA aplikační servery buď spoléhaly na slabé kombinace uživatelského jména a hesla, vyžadovaly složité nasazení infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) na UE, nebo neměly integrované zabezpečení s doménou důvěry mobilního operátora. To vedlo ke špatné uživatelské zkušenosti, bezpečnostním zranitelnostem a fragmentované správě identit.

Primární motivací bylo využít silnou, SIM kartou založenou autentizaci již přítomnou v mobilních sítích. Protokol 3GPP AKA poskytuje vzájemnou autentizaci a silné navázání klíče mezi UE a jádrem sítě. GBA přizpůsobuje tuto infrastrukturu k vytvoření obecné služby distribuce klíčů pro aplikační vrstvu. Tím se řeší problém množení přihlašovacích údajů a umožňuje mobilním operátorům nabízet nadstandardní služby s vestavěným, vysokým stupněm zabezpečení odvozeným od SIM karty.

Dále GBA umožňuje nové obchodní modely tím, že umožňuje poskytovatelům aplikací třetích stran (NAF) spoléhat se na autentizační infrastrukturu mobilního operátora. Poskytovatel obsahu může nabízet službu zabezpečeně předplatiteli bez nutnosti provozovat vlastní autentizační systém; jednoduše se integruje s operátorovým BSF. To vytvořilo důvěryhodný ekosystém, usnadnilo nasazení služeb IP Multimedia Subsystem (IMS) a poskytlo základ pro zabezpečenou komunikaci mezi stroji (M2M), čímž se vyřešila omezení předchozích ad-hoc a méně bezpečných metod autentizace aplikací.

## Klíčové vlastnosti

- Využívá stávající 3GPP AKA a SIM/USIM pro silnou autentizaci
- Nastartuje zabezpečení aplikační vrstvy z přihlašovacích údajů síťové vrstvy
- Umožňuje jednotné přihlašování napříč více aplikačními servery (NAF)
- Definuje jasné funkční entity: BSF, NAF, HSS, UE
- Podporuje odvozování klíčů pro konkrétní aplikační servery (Ks_NAF)
- Umožňuje zabezpečený přístup ke službám jak pro služby založené na HTTP, tak pro služby nezávislé na HTTP

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [NAF – Network Application Function](/mobilnisite/slovnik/naf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 22.978** (Rel-19) — Feasibility of All-IP Network (AIPN) in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.862** (Rel-12) — Interworking Solutions for Mobile Operators & Data Apps
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.309** (Rel-19) — Nbsp Service Based Interface for GBA BSF
- **TS 31.213** (Rel-18) — Test specification for (U)SIM
- **TR 31.822** (Rel-18) — Technical Report on GBA_U based APIs
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [GBA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gba/)
