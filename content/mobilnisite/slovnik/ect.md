---
slug: "ect"
url: "/mobilnisite/slovnik/ect/"
type: "slovnik"
title: "ECT – Explicit Congestion Notification-Capable Transport"
date: 2026-01-01
abbr: "ECT"
fullName: "Explicit Congestion Notification-Capable Transport"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ect/"
summary: "Schopnost transportní vrstvy, primárně pro TCP, která umožňuje síťovým uzlům signalizovat hrozící zahlcení koncovým bodům dříve, než dojde ke ztrátě paketů. Umožňuje efektivnější řízení zahlcení, sniž"
---

ECT je schopnost transportní vrstvy, primárně pro TCP, která umožňuje síťovým uzlům signalizovat hrozící zahlcení koncovým bodům dříve, než dojde ke ztrátě paketů.

## Popis

Explicit Congestion Notification-Capable Transport (ECT) odkazuje na implementaci mechanismu Explicit Congestion Notification ([ECN](/mobilnisite/slovnik/ecn/)) definovaného v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 3168, který byl převzat a odkazován ve specifikacích 3GPP pro transportní protokoly. ECN je rozšíření Internet Protocolu (IP) a Transmission Control Protocolu (TCP), které umožňuje směrovačům označovat pakety kódovým bodem Congestion Experienced ([CE](/mobilnisite/slovnik/ce/)) namísto jejich zahazování, když hrozí zahlcení. Transportní vrstva schopná ECT, jako je TCP, musí při navázání spojení vyjednat použití ECN a následně správně interpretovat a reagovat na tato CE označení ze sítě.

Fungování ECT zahrnuje dvě hlavní fáze: vyjednání schopností a signalizaci zahlcení. Během navazování TCP spojení nastavují koncové body příznaky ECN-Echo (ECE) a Congestion Window Reduced (CWR) v hlavičce TCP, aby indikovaly, že jsou schopné ECN (ECT). Jakmile je spojení navázáno, IP směrovače sledují délky svých front. Když fronta překročí nastavený práh, což signalizuje počínající zahlcení, směrovač označí pole ECN v IP hlavičce procházejících paketů jako CE (Congestion Experienced), za předpokladu, že paket byl odesílatelem odeslán jako ECT(0) nebo ECT(1). Příjemce toto CE označení detekuje a přehraje jej zpět odesílateli nastavením příznaku ECE v následných paketech TCP [ACK](/mobilnisite/slovnik/ack/). Po přijetí tohoto oznámení odesílatel sníží své přenosové okno, jako by došlo ke ztrátě paketu, čímž zmírní zahlcení bez nutnosti zahazování paketů a retransmisí.

V rámci architektury 3GPP je ECT relevantní pro transportní spojení používaná síťovými funkcemi a uživatelským zařízením (UE). Specifikace jako TS 29.165 ([GTP](/mobilnisite/slovnik/gtp/)) a TS 36.750 (rozhraní F1) odkazují na ECN pro správu zahlcení na kritických rozhraních. Použití ECT zlepšuje výkon transportních protokolů přes bezdrátové spoje, kde může být ztráta paketů způsobena rádiovými chybami spíše než zahlcením. Díky rozlišení mezi signály zahlcení (ECN značky) a signály ztráty může TCP reagovat vhodněji a vyhnout se zbytečnému snížení přenosové rychlosti. To vede k vyššímu využití linky, nižší latenci a lepší uživatelské zkušenosti s aplikacemi, zejména na zahlcených spojích páteřní sítě nebo backhaulu.

## K čemu slouží

ECT byl vyvinut, aby řešil omezení tradičního řízení zahlcení založeného na ztrátě, kde TCP interpretuje ztrátu paketu jako známku síťového zahlcení a drasticky sníží svou přenosovou rychlost. V moderních sítích, zejména s velkými vyrovnávacími paměťmi (bufferbloat), může tato reakce způsobovat vysokou latenci a nedostatečné využití. [ECN](/mobilnisite/slovnik/ecn/) poskytuje včasný, explicitní signál zahlcení dříve, než se přeplní vyrovnávací paměti a pakety jsou zahazovány, což umožňuje koncovým bodům plynule snížit přenosovou rychlost.

Motivace pro začlenění ECT do systémů 3GPP vychází z potřeby efektivního transportu v mobilních sítích. Rozhraní 3GPP, jako jsou rozhraní N3/N9 v 5G nebo rozhraní [S1-U](/mobilnisite/slovnik/s1-u/) v LTE, přenášejí obrovská množství dat uživatelské roviny. Zahlcení na těchto spojích může zhoršovat kvalitu služeb. Použití transportu schopného ECT umožňuje síti inteligentněji spravovat zahlcení, snižovat ztrátu paketů a zpoždění retransmisí. To je obzvláště důležité pro služby v reálném čase a citlivé na latenci, které umožňuje 5G. ECT představuje posun od čistě ztrátového paradigmatu řízení zahlcení k paradigmatu založenému na signálech, což je v souladu s širšími snahami internetového inženýrství o zlepšení odezvy sítě a spravedlnosti.

## Klíčové vlastnosti

- Umožňuje IP směrovačům označovat pakety kódovým bodem Congestion Experienced (CE)
- Vyžaduje vyjednání mezi koncovými body při navázání transportní vrstvy (např. TCP SYN)
- Umožňuje odesílatelům reagovat na zahlcení dříve, než dojde ke ztrátě paketů
- Snižuje ztrátu paketů a retransmise, čímž snižuje latenci
- Zlepšuje propustnost a spravedlnost na sdílených úzkých profilech (bottleneck links)
- Integrováno do specifikací 3GPP pro rozhraní založená na GTP a další interní rozhraní

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.315** (Rel-19) — Operator Determined Barring (ODB) for IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [ECT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ect/)
