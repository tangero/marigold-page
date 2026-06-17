---
slug: "fbc"
url: "/mobilnisite/slovnik/fbc/"
type: "slovnik"
title: "FBC – Flow Based bearer Charging"
date: 2026-01-01
abbr: "FBC"
fullName: "Flow Based bearer Charging"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fbc/"
summary: "Zpoplatňovací mechanismus v 3GPP paketových jádrových sítích, kde je účtování založeno na jednotlivých IP datových tocích nebo tocích služebních dat (SDF) namísto na celém přenosovém kanálu (beareru)."
---

FBC je 3GPP zpoplatňovací mechanismus, kde je účtování založeno na jednotlivých IP datových tocích, což umožňuje detailní, službám přizpůsobené zpoplatnění korelací využití s konkrétními aplikacemi nebo úrovněmi QoS.

## Popis

Flow Based bearer Charging (FBC) je architektonický rámec v 3GPP doméně paketového přenosu (PS), který umožňuje zpoplatnění založené na detekci a měření jednotlivých IP toků nebo toků služebních dat (SDF). Posouvá se tak za hranice zpoplatnění na úrovni přenosového kanálu (beareru), kde je veškerý provoz v rámci PDP kontextu účtován jednotně, k detailnějšímu modelu. Uzly jádrové sítě, konkrétně Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) v GPRS/UMTS nebo Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) v EPS, jsou rozšířeny o funkce v uživatelské rovině, které zahrnují možnosti hluboké kontroly paketů (DPI) a klasifikace toků. Tyto brány identifikují jednotlivé toky na základě paketových filtrů definovaných pravidly politiky, která jsou typicky poskytována funkcí Policy and Charging Rules Function (PCRF).

Proces zpoplatnění funguje tak, že každý detekovaný SDF je asociován s konkrétním Charging Key. Brána následně měří parametry pro daný tok, jako je objem dat v uplinku/downlinku, doba trvání nebo specifické události. Tato data o využití jsou formátována do Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo připravena pro online zpoplatnění přes referenční bod Gy. Záznamy jsou odesílány funkci Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) pro offline zpoplatnění nebo do Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy pro řízení kreditů v reálném čase. Jeden přenosový kanál (bearer, PDP kontext nebo EPS bearer) tak může obsahovat více samostatně zpoplatňovaných SDF. Například výchozí bearer uživatele může přenášet základní internetový tok zpoplatněný jedním tarifem, tok video streamu zpoplatněný prémiovým tarifem a nulově tarifovaný tok komunikační aplikace.

FBC je nedílnou součástí architektury Policy and Charging Control (PCC) definované v 3GPP. PCRF používá rozhraní Sp (nebo Gx) k provizionování brány pravidly PCC. Každé PCC pravidlo obsahuje filtry toku pro identifikaci SDF, asociovaný Charging Key a další charakteristiky zpoplatnění (např. zda je zpoplatnění online nebo offline, rating group). Tato těsná integrace umožňuje dynamické, službami řízené zpoplatnění. Architektura podporuje jak offline, tak online modely zpoplatnění, což umožňuje scénáře předplaceného i následného účtování s vysokou mírou detailu. FBC je zásadní pro implementaci sofistikovaných služebních plánů, jako je vrstvený přístup k datům, sponzorovaná data nebo zpoplatnění založené na kvalitě služby (QoS).

## K čemu slouží

FBC bylo zavedeno, aby řešilo omezení zpoplatnění na úrovni přenosového kanálu (beareru) v kontextu vývoje služeb mobilních dat. Rané sítě [GPRS](/mobilnisite/slovnik/gprs/)/UMTS účtovaly na základě celkového objemu dat na PDP kontextu, což zacházelo se vším internetovým provozem stejně. Tento model se stal nevyhovujícím, když operátoři začali nabízet rozmanité služby jako VoIP, video streaming a obsah partnerů, z nichž každá vyžadovala jiný model účtování (např. za minutu, prémiové datové balíčky nebo data sponzorovaná poskytovatelem obsahu). FBC bylo vytvořeno, aby umožnilo službám přizpůsobené zpoplatnění.

Hlavní motivací bylo umožnit operátorům pružněji monetizovat síťové služby a vytvářet nové zdroje příjmů. Řešilo problém neschopnosti rozlišit pro účely účtování mezi různými typy provozu protékajícího stejným IP připojením. Tím, že umožnilo zpoplatnění na úrovni IP toku, mohli operátoři zavést diferencované ceny, nulové tarifování a služebně specifické nabídky. Dále poskytlo technický základ pro propojení zpoplatnění s kvalitou služby (QoS), což operátorům umožnilo účtovat prémii za služby se zaručenou přenosovou rychlostí. FBC jako součást širšího rámce PCC bylo klíčovým prvkem pro přechod od jednoduchého přístupu k datům k bohatým, zpoplatnitelným službám v sítích 3G a 4G, přímo podporujícím obchodní modely jako oboustranné trhy, kde mohou poskytovatelé obsahu platit za datovou spotřebu uživatelů.

## Klíčové vlastnosti

- Detailnost zpoplatnění na úrovni toku služebních dat (SDF) nebo IP toku
- Integrace s architekturou Policy and Charging Control (PCC) prostřednictvím PCRF
- Využívá hlubokou kontrolu paketů (DPI) a paketové filtry pro klasifikaci toků
- Podporuje jak offline (založené na CDR), tak online (řízení kreditů) modely zpoplatnění
- Asociuje toky s Charging Keys pro flexibilní stanovení cen a účtování
- Umožňuje zpoplatnění založené na více metrikách: objem, doba trvání a události

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.803** (Rel-7) — PCC Architecture Harmonization Study
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.279** (Rel-19) — 5G MBS Session Converged Charging
- **TS 32.296** (Rel-19) — Online Charging System (OCS) Architecture
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [FBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/fbc/)
