---
slug: "up-link"
url: "/mobilnisite/slovnik/up-link/"
type: "slovnik"
title: "UL – Up-link"
date: 2025-01-01
abbr: "UL"
fullName: "Up-link"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/up-link/"
summary: "Rádiová přenosová cesta od uživatelského zařízení (UE) k základnové stanici (Node B/gNB). Je základním prvkem všech mobilních komunikací, umožňuje UE odesílat data, řídicí signalizaci a přístupové pož"
---

UL je rádiová přenosová cesta od uživatelského zařízení (User Equipment) k základnové stanici, která mu umožňuje odesílat data, řídicí signalizaci a přístupové požadavky do sítě.

## Popis

Up-link ([UL](/mobilnisite/slovnik/ul/)) je základní koncept v mobilních rádiových přístupových sítích, který konkrétně definuje směr rádiového přenosu od mobilního uživatelského zařízení (UE) k základnové stanici sítě, historicky označované jako Node B v UMTS a v 5G NR vyvinuté na gNB. Tato přenosová cesta je klíčová pro navázání obousměrné komunikace. UL přenáší všechny informace pocházející od uživatele, včetně dat uživatelské roviny (např. hlasové pakety, aplikační data), řídicích informací pro uplink ([UCI](/mobilnisite/slovnik/uci/)), jako jsou indikátory kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)) a požadavky na plánování, a náhodných přístupových preambulí pro počáteční vstup do sítě. Fyzická realizace UL zahrnuje specifická kmitočtová pásma nebo časové sloty (v systémech [TDD](/mobilnisite/slovnik/tdd/)) přidělené sítí, odlišné od Down-linku ([DL](/mobilnisite/slovnik/dl/)), aby umožnila plně duplexní komunikaci a zabránila interferenci.

Z pohledu protokolového zásobníku UL zahrnuje celý řetězec od aplikační vrstvy v UE až po fyzický rádiový přenos. Data proudí z vyšších vrstev přes protokol Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)), kde jsou naplánována k odeslání na základě povolení (grants) přijatých od základnové stanice přes DL. Fyzická vrstva pak tato data zpracuje prostřednictvím kanálového kódování, modulace (např. QPSK, 16-QAM, 64-QAM) a mapování na specifické fyzické kanály, jako je Physical Uplink Shared Channel (PUSCH) pro data nebo Physical Uplink Control Channel (PUCCH) pro řídicí signalizaci. Řízení výkonu je klíčovým aspektem provozu UL, kdy UE upravuje svůj vysílací výkon na základě příkazů od základnové stanice, aby zajistila spolehlivý příjem a zároveň minimalizovala interferenci pro ostatní uživatele.

Výkon a kapacita UL jsou klíčovými faktory celkového výkonu sítě. Mezi hlavní technické výzvy patří řešení problému blízký-vzdálený (near-far problem), kdy musí být UE v různých vzdálenostech od základnové stanice přijímány na srovnatelných úrovních výkonu, a zvládání omezeného vysílacího výkonu a kapacity baterie mobilních zařízení. Pro zvýšení přenosových rychlostí a spektrální účinnosti se používají pokročilé techniky, jako je Uplink Carrier Aggregation, Uplink MIMO (Multiple-Input Multiple-Output) a dynamické plánování. UL není statický koncept; jeho specifikace, včetně podporovaných modulačních schémat, struktury kanálů a referenčních signálů (např. Sounding Reference Signals - SRS), se významně vyvíjely napříč 3GPP releasy, aby podpořily vyšší přenosové rychlosti, nižší latenci a nové požadavky služeb.

## K čemu slouží

Up-link existuje proto, aby umožnil základní schopnost mobilního zařízení přenášet informace do sítě, čímž uzavírá obousměrnou komunikační smyčku nezbytnou pro jakoukoli interaktivní službu. Bez definované cesty UL by byla síť pouze vysílacím systémem. Tento koncept řeší problém umožnění milionům distribuovaných zařízení s omezeným výkonem spolehlivě odesílat data do centralizované síťové infrastruktury, přičemž řídí interferenci a efektivně sdílí rádiové zdroje mezi všechny uživatele.

Historicky byl koncept oddělených cest pro uplink a downlink zaveden již v nejranějších mobilních standardech (1G). 3GPP jej formalizoval a zdokonalil v UMTS (Release 99) a všech následujících technologiích. Motivací pro jeho neustálý vývoj je asymetrická povaha mnoha datových služeb (jako je prohlížení webu nebo streamování videa, kde tradičně nese více dat DL) a rostoucí potřeba vysoké kapacity uplinku pro aplikace, jako je živé vysílání videa, hromadné nahrávání dat ze senzorů v IoT a ultra-spolehlivá nízkolatenční komunikace (URLLC), kde jsou rychlá potvrzení v uplinku klíčová. Každý nový release řeší omezení předchozích implementací UL, jako jsou špičkové přenosové rychlosti, latence, energetická účinnost a podpora nových kmitočtových pásem.

## Klíčové vlastnosti

- Definuje směr rádiového přenosu od UE k základnové stanici.
- Přenáší uživatelská data, řídicí informace pro uplink (UCI) a náhodné přístupové signály.
- Využívá specifické fyzické kanály, jako jsou PUSCH a PUCCH.
- Používá pokročilé techniky, jako je řízení výkonu a uplink MIMO.
- Je dynamicky plánován sítí prostřednictvím Downlink Control Information (DCI).
- Vývoj zahrnuje podporu modulace vyššího řádu a agregace nosných.

## Související pojmy

- [Down-link](/mobilnisite/slovnik/down-link/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [PUCCH – Physical Uplink Control Channel](/mobilnisite/slovnik/pucch/)

## Definující specifikace

- **TS 25.106** (Rel-19) — UTRA FDD Repeater RF Performance Requirements
- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing

---

📖 **Anglický originál a plná specifikace:** [UL na 3GPP Explorer](https://3gpp-explorer.com/glossary/up-link/)
