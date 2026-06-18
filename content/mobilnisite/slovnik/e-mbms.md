---
slug: "e-mbms"
url: "/mobilnisite/slovnik/e-mbms/"
type: "slovnik"
title: "E-MBMS – Evolved Multimedia Broadcast Multicast Service"
date: 2025-01-01
abbr: "E-MBMS"
fullName: "Evolved Multimedia Broadcast Multicast Service"
category: "Services"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/e-mbms/"
summary: "Služba typu point-to-multipoint v sítích LTE a 5G, která efektivně doručuje stejný obsah (např. živé TV vysílání, aktualizace softwaru) více uživatelům současně. Optimalizuje síťové zdroje vysíláním p"
---

E-MBMS je služba typu point-to-multipoint v sítích LTE a 5G, která efektivně doručuje stejný obsah více uživatelům současně vysíláním přes společnou nosnou vlnu.

## Popis

Evolved Multimedia Broadcast Multicast Service (E-MBMS) je architektura služby vysílání/multicastu definovaná 3GPP pro sítě LTE ([E-UTRAN](/mobilnisite/slovnik/e-utran/)) a následné sítě 5G NR. Umožňuje efektivní, současné doručování populárního obsahu velkému počtu uživatelů v určité geografické oblasti, známé jako Broadcast Multicast Service Area (BMSA). Základním principem je přenos jediného datového proudu přes rozhraní rádiového přístupu, který mohou přijímat všechna zainteresovaná uživatelská zařízení (UE) v pokryté zóně, namísto vytváření individuálních unicastových spojení pro každého uživatele. To výrazně zlepšuje spektrální účinnost pro obsah s masovou oblibou.

Architektonicky E-MBMS zahrnuje několik klíčových síťových prvků. Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) je vstupním bodem pro poskytovatele obsahu a zajišťuje oznamování služeb, zabezpečení a plánování dat. V jádru sítě [MBMS](/mobilnisite/slovnik/mbms/) Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) distribuuje IP multicastové pakety příslušným základnovým stanicím (eNBs v LTE, gNBs v NR). Nejzásadnější inovací je řešení v rádiové přístupové síti: buňky synchronizují své přenosy pomocí režimu Multicast Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)). V MBSFN více buněk současně vysílá identické signály na stejné frekvenci, což umožňuje, aby se signály na straně UE konstruktivně sčítaly, čímž se zlepšuje pokrytí a síla signálu na hranicích buněk a efektivně se vytváří jedna velká vysílací buňka.

E-MBMS funguje pomocí specifických fyzických kanálů. Physical Multicast Channel ([PMCH](/mobilnisite/slovnik/pmch/)) nese vlastní multicastová/broadcastová data. Řídicí informace jsou poskytovány přes Multicast Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)) a Multicast Traffic Channel ([MTCH](/mobilnisite/slovnik/mtch/)) na logické úrovni. UE zájemce o službu nejprve získá informace o oznámení služby, poté monitoruje MCCH pro konfigurační podrobnosti před přijímáním dat na MTCH/PMCH. Systém podporuje jak režim broadcastu (přístupný všem UE v oblasti), tak režim multicastu (vyžadující předplatné a potenciálně šifrování). Jeho úlohou je odlehčovat provoz z unicastových nosných, což umožňuje škálovatelné doručování živých událostí, nouzových upozornění a distribuci velkých souborů bez zahlcení sítě.

## K čemu slouží

E-MBMS byl vyvinut k řešení neefektivity používání více unicastových proudů pro doručování identického obsahu mnoha uživatelům v mobilní síti, což plýtvá vzácným rádiovým spektrem a zdroji jádra sítě. Tento problém se stal akutním s rostoucí poptávkou po mobilním videu a distribuci obsahu velkého rozsahu. Tradiční unicast se u populárních živých událostí nebo rozsáhlých aktualizací softwaru dobře neškáluje, což vede k zahlcení sítě a špatnému uživatelskému zážitku během špičkové poptávky.

Vývoj z dřívějšího MBMS v 3G/UMTS (zavedeno v Rel-6) na E-MBMS v LTE (Rel-8/9) byl motivován potřebou vyšších přenosových rychlostí, lepší spektrální účinnosti a vylepšeného pokrytí. Omezení MBMS v UMTS zahrnovala nižší přenosové rychlosti a méně efektivní využití rádiového rozhraní WCDMA. E-MBMS využil OFDMA-based rádiové rozhraní LTE a zavedl revoluční koncept MBSFN, který vyřešil problém s interferencí na hranicích buněk a vytvořil souvislou vysílací oblast. To umožnilo mobilním operátorům nabízet vysílací služby, jako je mobilní TV, s kvalitou a účinností srovnatelnou s dedikovanými vysílacími sítěmi (např. DVB-H), ale integrované v rámci jejich stávající mobilní infrastruktury.

## Klíčové vlastnosti

- Provoz v režimu Multicast Broadcast Single Frequency Network (MBSFN)
- Vysoká spektrální účinnost díky jedinému přenosu pro více uživatelů
- Podpora jak režimu broadcastu, tak multicastu
- Integrované zabezpečení a oznamování služeb prostřednictvím BM-SC
- Využívá specifických fyzických (PMCH) a logických (MCCH, MTCH) kanálů
- Škálovatelné oblasti služeb (Single-Cell Broadcast nebo MBSFN oblasti)

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [PMCH – Physical Multicast Channel](/mobilnisite/slovnik/pmch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)

## Definující specifikace

- **TS 28.707** (Rel-19) — EPC NRM IRP Requirements
- **TS 32.751** (Rel-11) — EPC NRM IRP Requirements
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions

---

📖 **Anglický originál a plná specifikace:** [E-MBMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-mbms/)
