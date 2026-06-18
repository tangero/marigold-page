---
slug: "ntn"
url: "/mobilnisite/slovnik/ntn/"
type: "slovnik"
title: "NTN – Non-Terrestrial Networks"
date: 2026-01-01
abbr: "NTN"
fullName: "Non-Terrestrial Networks"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ntn/"
summary: "Síťová architektura začleňující satelity, stanice na vysokohorských platformách (HAPS) a další vzdušné platformy jako přístupové uzly pro poskytnutí všudypřítomného pokrytí, včetně odlehlých oblastí,"
---

NTN je síťová architektura 3GPP, která využívá satelity a vzdušné platformy jako přístupové uzly pro globální rozšíření pokrytí sítě 5G, včetně odlehlých oblastí, oceánů a vzdušného prostoru.

## Popis

Neterestrické sítě (NTN) označují komplexní architekturu 3GPP, kde přístupovou síť poskytují neterestrické platformy bezproblémově integrované s pozemskou 5G Core sítí. Primární platformy zahrnují geostacionární ([GEO](/mobilnisite/slovnik/geo/)), střední ([MEO](/mobilnisite/slovnik/meo/)) a nízké ([LEO](/mobilnisite/slovnik/leo/)) oběžné dráhy satelitů, stejně jako stanice na vysokohorských platformách ([HAPS](/mobilnisite/slovnik/haps/)), jako jsou balóny nebo drony fungující jako kvazistacionární základnové stanice. V této architektuře satelit nebo HAPS nese užitečné zatížení (payload), které funguje jako 3GPP gNB (základnová stanice 5G) nebo ng-eNB (LTE základnová stanice připojená k 5GC), často označované jako 'satelitní uzel' nebo 'neterestrický uzel'. Tento uzel komunikuje s uživatelským zařízením (UE) prostřednictvím servisního spoje (např. pomocí adaptovaných vlnových forem 5G NR ve specifických kmitočtových pásmech jako S-pásmo nebo Ka-pásmo) a připojuje se k pozemním bránám, známým jako pozemní stanice nebo brány (gateway), prostřednictvím přenosového spoje (feeder link). Brána pak komunikuje s 5G Core sítí přes standardní rozhraní [N2](/mobilnisite/slovnik/n2/)/N3.

Jak to funguje, zahrnuje významné adaptace standardních 5G procedur kvůli jedinečným charakteristikám satelitních spojů. Nejzásadnější výzvou je velmi dlouhá doba šíření (propagation delay), která se může pohybovat od několika milisekund pro LEO až po stovky milisekund pro GEO. Aby se s tím vyrovnalo, zavedlo 3GPP vylepšení procedur časového předstihu (timing advance), časování hybridního automatického opakovaného dotazu ([HARQ](/mobilnisite/slovnik/harq/)) a procedur náhodného přístupového kanálu ([RACH](/mobilnisite/slovnik/rach/)). Pro mobilitu NTN podporuje jak pokrytí buňkou fixované vůči Zemi (kde je stopa buňky na zemi pevná a satelitní svazek se pohybuje), tak pokrytí buňkou pohybující se vůči Zemi (kde je svazek natáčen tak, aby stopa buňky zůstala stacionární), což vyžaduje nové schémata správy mobility. Architektura také definuje transparentní užitečná zatížení (bent-pipe), která signály pouze zesilují a přeposílají, a regenerativní užitečná zatížení (on-board processing), která mohou signály dekódovat, přepínat a znovu kódovat, což ovlivňuje latenci a složitost.

Klíčové komponenty zahrnují NTN terminál (UE s rozšířenými schopnostmi pro satelitní spoje), neterestrický síťový uzel (užitečné zatížení satelitu/HAPS), bránu (pozemskou stanici s funkcí přenosu síťových dat) a 5G Core síť. Jejím úkolem je poskytovat kontinuitu služeb, všudypřítomné pokrytí a služby vysílání/vícebodového vysílání (broadcast/multicast). Umožňuje případy užití jako přímé satelitní připojení k zařízení (direct-to-device) pro smartphony, monitorování senzorů masivního IoT v odlehlých oblastech, přenosové spoje (backhaul) pro pozemské sítě a spolehlivou komunikaci pro námořní a letecké služby. Integrací NTN se systémy 5G skutečně stanou jednotnou globální sítí, zajišťující konektivitu všude a zvyšující odolnost tím, že poskytují alternativu, když pozemské sítě selžou kvůli katastrofám.

## K čemu slouží

NTN byly vyvinuty k řešení základního omezení pozemských mobilních sítí: jejich neschopnosti poskytnout nákladově efektivní, bezproblémové pokrytí na celém zemském povrchu, včetně oceánů, pouští, polárních oblastí a odlehlých venkovských oblastí. Tradiční mobilní sítě jsou ekonomicky životaschopné pouze v oblastech s dostatečnou hustotou obyvatelstva, což zanechává rozsáhlé geografické regiony nepokryté. Tato mezera bránila vizi skutečně globální konektivity pro aplikace internetu věcí (IoT), letectví, námořnictví a služeb záchranného systému. Navíc jsou pozemské sítě zranitelné vůči přírodním katastrofám, které mohou zničit infrastrukturu.

Motivace pro standardizaci NTN v rámci 3GPP, počínaje studijní položkou ve verzi 15 (Release 15), byla využít rychlý pokrok v satelitní technologii, zejména nástup velkých konstelací na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) (jako je Starlink), a rostoucí poptávku po globálních širokopásmových a IoT službách. Vytvořením jednotného standardu chtělo 3GPP podpořit ekosystém nízkonákladových, hromadně vyráběných zařízení, která mohou přistupovat k pozemským i neterestrickým sítím bez nutnosti proprietárních technologií. Tím se řeší problém fragmentace a umožňují se úspory z rozsahu. NTN řeší potřebu odolnosti sítě poskytováním záložní nebo komplementární cesty, podporují regulatorní požadavky na nouzovou komunikaci (např. EU eCall) a otevírají nové obchodní modely pro konektivitu v odvětvích dopravy, zemědělství a energetiky po celém světě.

## Klíčové vlastnosti

- Integrace satelitů (GEO/MEO/LEO) a HAPS jako přístupových uzlů 3GPP připojených k 5G Core síti
- Vylepšené protokoly pro zvládání dlouhých dob šíření (např. adaptované HARQ, RACH, časování plánování)
- Podpora jak transparentních (bent-pipe), tak regenerativních (on-board processing) satelitních užitečných zatížení
- Správa mobility pro scénáře pokrytí buňkou fixovanou vůči Zemi a pohybující se vůči Zemi
- Provoz ve specifických kmitočtových pásmech (např. S, Ka, Ku) pro servisní a přenosové spoje
- Podpora IoT NTN (NB-IoT, eMTC) a širokopásmových služeb, včetně přímého připojení k zařízení (direct-to-device)

## Související pojmy

- [HAPS – High Altitude Platform Station](/mobilnisite/slovnik/haps/)

## Definující specifikace

- **TR 22.926** (Rel-19) — 5G Extraterritorial Access Guidelines
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 28.657** (Rel-19) — E-UTRAN NRM IRP Requirements
- **TS 28.874** (Rel-19) — Study on Management Aspects of NTN Phase 2
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.700** — 3GPP TR 33.700
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node
- **TS 36.214** (Rel-19) — E-UTRA Physical Layer Measurements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- … a dalších 22 specifikací

---

📖 **Anglický originál a plná specifikace:** [NTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ntn/)
