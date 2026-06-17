---
slug: "mbsfn"
url: "/mobilnisite/slovnik/mbsfn/"
type: "slovnik"
title: "MBSFN – Multimedia Broadcast multicast service Single Frequency Network"
date: 2026-01-01
abbr: "MBSFN"
fullName: "Multimedia Broadcast multicast service Single Frequency Network"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mbsfn/"
summary: "Přenosové schéma, při kterém více buněk synchronně vysílá stejný obsah na stejném frekvenčním zdroji. Vytváří jednu velkou vysílací oblast, čímž zlepšuje spektrální účinnost a kvalitu signálu pro vysí"
---

MBSFN je přenosové schéma, při kterém více buněk synchronně vysílá stejný obsah na stejné frekvenci, čímž vytváří jednu velkou vysílací oblast, což zvyšuje efektivitu a kvalitu služeb, jako je mobilní televize.

## Popis

MBSFN je základní technologie rádiového přístupového sítě umožňující efektivní doručování typu point-to-multipoint. Funguje tak, že koordinuje více [eNB](/mobilnisite/slovnik/enb/) (v LTE) nebo gNB (v NR), aby vysílaly identické vlnové formy – nesoucí stejná data, na stejných blocích fyzických zdrojů a přesně ve stejný čas. Z pohledu uživatelského zařízení (UE) se tyto synchronizované přenosy z více buněk jeví jako jediný přenos podléhající konstruktivní vícecestné propagaci, čímž se efektivně mění interference na užitečný signál. Tím se typické buňkové prostředí omezené interferencí mění na prostředí vhodné pro vysílání, což výrazně zlepšuje kvalitu přijímaného signálu, zejména na okrajích buněk.

Architektura se opírá o těsnou synchronizaci, dosaženou prostřednictvím globálního navigačního satelitního systému ([GNSS](/mobilnisite/slovnik/gnss/)) nebo síťových metod, a o centralizovaný řídicí bod, Multi-cell/multicast Coordination Entity ([MCE](/mobilnisite/slovnik/mce/)). MCE je zodpovědná za plánování MBSFN přenosů, přidělování stejných časově-frekvenčních zdrojů (MBSFN subframes) napříč účastnícími se buňkami a za zajištění synchronizace dat. Obsah určený k vysílání, jako je například relace [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service), je doručován z Broadcast Multicast-Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) přes MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a následně do každého eNB/gNB v oblasti MBSFN.

Klíčové aspekty fyzické vrstvy zahrnují použití rozšířeného cyklického prefixu ([CP](/mobilnisite/slovnik/cp/)) pro zvládnutí zvýšeného rozprostření zpoždění vyplývajícího z výrazně větší efektivní přenosové oblasti. V časové doméně jsou specifické subframes označeny jako MBSFN subframes. Ve frekvenční doméně se používá vyhrazená část šířky pásma nosné, tzv. MBSFN Area. UE provádí odhad kanálu pomocí speciálních MBSFN referenčních signálů. Tato technologie je základním kamenem pro evolved MBMS (eMBMS) v LTE a byla později vylepšena pro NR multicast a broadcast služby, podporující aplikace od skupinové komunikace pro veřejnou bezpečnost po rozsáhlé doručování obsahu.

## K čemu slouží

MBSFN bylo vytvořeno, aby vyřešilo zásadní neefektivitu používání unicastových přenosů pro doručování populárního, stejného obsahu mnoha uživatelům současně v geografické oblasti. Před MBSFN by doručování živé televize nebo velkých softwarových aktualizací spotřebovávalo obrovské množství individuálních rádiových zdrojů a rychle by zahlcovalo síť. Jeho účelem je umožnit spektrálně efektivní, vysokokvalitní vysílací a multicastové služby přes buňkové sítě.

Řeší omezení dřívějších implementací [MBMS](/mobilnisite/slovnik/mbms/) v 3GPP Release 6, kterým chyběly schopnosti single-frequency sítě. MBMS z Release 6 trpělo špatným výkonem na okrajích buněk kvůli interferencím ze sousedních buněk vysílajících odlišný obsah. MBSFN tento problém přímo řeší synchronizací přenosů, čímž mění interference na užitečnou složku signálu. To bylo motivováno snahou průmyslu nabízet mobilní televizi a multimediální vysílání jako konkurenceschopnou službu, využívající stávající buňkovou infrastrukturu namísto budování samostatných vysílacích sítí, jako je DVB-H.

Navíc MBSFN poskytuje nezbytnou kvalitu a efektivitu pro klíčovou skupinovou komunikaci, jako jsou služby veřejné bezpečnosti, kde je spolehlivé a současné doručení velké skupině uživatelů zásadní. Položilo základy pro všechna následná vylepšení multicastu a broadcastu v 3GPP stanovením základního principu synchronizovaného vícebuněčného přenosu.

## Klíčové vlastnosti

- Synchronní přenos z více buněk na identických časově-frekvenčních zdrojích
- Vytvoření velké, virtuální vysílací oblasti s jedním kmitočtem
- Použití rozšířeného cyklického prefixu pro potlačení velkého rozprostření zpoždění
- Centralizované plánování a koordinace prostřednictvím Multi-cell/multicast Coordination Entity (MCE)
- Vyhrazené MBSFN subframes a MBSFN referenční signály pro odhad kanálu
- Výrazné zlepšení spektrální účinnosti a kvality signálu pro vysílací/multicastový provoz

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MCE – Multi-cell/multicast Coordination Entity](/mobilnisite/slovnik/mce/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [MBSFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbsfn/)
