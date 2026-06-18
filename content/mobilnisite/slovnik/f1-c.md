---
slug: "f1-c"
url: "/mobilnisite/slovnik/f1-c/"
type: "slovnik"
title: "F1-C – F1 Control Plane Interface"
date: 2025-01-01
abbr: "F1-C"
fullName: "F1 Control Plane Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/f1-c/"
summary: "F1-C je rozhraní řídicí roviny mezi centrální jednotkou gNB (gNB-CU) a distribuovanou jednotkou gNB (gNB-DU) v disagregované 5G NR RAN. Přenáší signalizaci pro správu kontextu UE, zřizování přenosovýc"
---

F1-C je rozhraní řídicí roviny mezi centrální jednotkou gNB (gNB-CU) a distribuovanou jednotkou gNB (gNB-DU) v disagregované 5G RAN, které přenáší signalizaci pro správu kontextu, zřizování přenosových cest a mobilitu.

## Popis

Rozhraní F1-C je klíčovou součástí 3GPP definované disagregované architektury NG-RAN zavedené v 5G. Funguje přes přenosovou síť, typicky využívající IP, a spojuje centrální jednotku ([CU](/mobilnisite/slovnik/cu/)), která zpracovává protokoly vyšších vrstev a centralizované řízení, s jednou nebo více distribuovanými jednotkami ([DU](/mobilnisite/slovnik/du/)), které spravují protokoly nižších vrstev a rádiové kmitočty. Rozhraní je definováno jako otevřené a standardizované, což umožňuje multivendorovou interoperabilitu mezi komponentami CU a DU.

Hlavní funkcí F1-C je přenos signalizačních zpráv protokolu [F1AP](/mobilnisite/slovnik/f1ap/). Tyto zprávy umožňují širokou škálu řídicích procedur nezbytných pro správu rádiových zdrojů. Mezi klíčové procedury patří zřízení, modifikace a uvolnění kontextů UE; nastavení a správa datových rádiových přenosových cest ([DRB](/mobilnisite/slovnik/drb/)); příprava a provedení předání spojení; a transparentní přenos [RRC](/mobilnisite/slovnik/rrc/) zpráv mezi CU a DU. Rozhraní F1-C zajišťuje, že CU, která hostuje vrstvy RRC a [PDCP](/mobilnisite/slovnik/pdcp/) pro řídicí rovinu, může efektivně řídit DU, která hostuje vrstvy [RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/) a PHY.

Z architektonického hlediska je F1-C logické point-to-point rozhraní, ačkoli fyzické spojení prochází IP sítí. Podporuje funkce správy rozhraní, jako je indikace chyb a resetovací procedury, pro zajištění robustnosti. Oddělení provozu řídicí (F1-C) a uživatelské roviny (F1-U) umožňuje nezávislé škálování a optimalizaci síťových funkcí. Tato disagregace je základem pro nasazení Cloud RAN (C-RAN) a virtualizovaného RAN (vRAN), což umožňuje centralizované fondy zpracování a distribuované rádiové jednotky.

## K čemu slouží

Rozhraní F1-C bylo vytvořeno, aby řešilo potřebu flexibilní, škálovatelné a nákladově efektivní architektury rádiového přístupového sítě v 5G. Tradiční základnové stanice (eNB ve 4G) byly monolitické, integrující všechny vrstvy protokolů do jedné fyzické jednotky, což omezovalo flexibilitu nasazení a inovace. Specifikace 5G NR zavedla funkční rozdělení, oddělující základnovou stanici na centrální jednotku (CU) a distribuovanou jednotku (DU), aby umožnila centralizované zpracování, pokročilé koordinační techniky a efektivní sdružování zdrojů.

F1-C konkrétně řeší problém řídicí signalizace mezi těmito oddělenými entitami. Poskytnutím standardizovaného rozhraní řídicí roviny umožňuje síťovým operátorům pořizovat zařízení CU a DU od různých dodavatelů, což podporuje konkurenční ekosystém a zabraňuje závislosti na jediném dodavateli. Také umožňuje pokročilé RAN architektury, jako je C-RAN, kde může být více DU připojeno k centralizovanému, případně virtualizovanému fondu CU. Tato centralizace zlepšuje koordinaci interference, správu mobility a umožňuje implementaci sofistikovaného síťového řezání a politik QoS v širší oblasti pokrytí.

Historicky absence takového otevřeného interního rozhraní ve 4G eNB činila RAN uzavřeným systémem. F1-C spolu s F1-U je základním kamenem hnutí Open RAN (O-RAN), které staví na funkčních rozděleních 3GPP. Poskytuje nezbytný signalizační kanál k realizaci výhod disagregace RAN, včetně snížení kapitálových a provozních výdajů, zvýšení agility nasazení a možnosti nezávislého upgradu nebo škálování funkcí řídicí a uživatelské roviny.

## Klíčové vlastnosti

- Přenáší signalizační zprávy protokolu F1AP
- Spravuje zřízení, modifikaci a uvolnění kontextu UE
- Řídí zřízení, modifikaci a uvolnění datových rádiových přenosových cest (DRB)
- Podporuje mobilní procedury včetně přípravy a provedení předání spojení
- Umožňuje transparentní přenos RRC zpráv mezi CU a DU
- Poskytuje funkce správy rozhraní (např. indikace chyb, reset)

## Související pojmy

- [F1-U – F1 User Plane Interface](/mobilnisite/slovnik/f1-u/)
- [F1AP – F1 Application Protocol](/mobilnisite/slovnik/f1ap/)

## Definující specifikace

- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.470** (Rel-19) — F1 Interface Introduction

---

📖 **Anglický originál a plná specifikace:** [F1-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/f1-c/)
