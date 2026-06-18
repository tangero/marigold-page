---
slug: "meid"
url: "/mobilnisite/slovnik/meid/"
type: "slovnik"
title: "MEID – Mobile Equipment IDentity"
date: 2025-01-01
abbr: "MEID"
fullName: "Mobile Equipment IDentity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/meid/"
summary: "Globálně jednoznačný identifikátor mobilního zařízení, používaný primárně v systémech 3GPP2 (CDMA), ale také definovaný pro interoperabilitu se sítěmi 3GPP. Slouží podobnému účelu jako IMEI, ale má od"
---

MEID je globálně jednoznačný identifikátor mobilního zařízení, používaný primárně v systémech CDMA a definovaný pro interoperabilitu se sítěmi 3GPP.

## Popis

Mobile Equipment IDentity (MEID) je globálně jednoznačný 56bitový identifikátor přiřazený fyzickým mobilním zařízením, původně definovaný organizací 3GPP2 pro systémy CDMA2000. V kontextu specifikací 3GPP je definován pro podporu scénářů interoperability a spolupráce, kdy je třeba identifikovat zařízení nebo síťový prvek pocházející z ekosystému 3GPP2 v rámci sítě 3GPP (např. LTE, 5G). MEID se strukturálně liší od [IMEI](/mobilnisite/slovnik/imei/) dle 3GPP; typicky je reprezentován jako 14místné hexadecimální číslo (nebo 18místný desítkový ekvivalent) skládající se z kódu regionální autority, kódu výrobce a sériového čísla.

V rámci architektury 3GPP je MEID zpracováván jako alternativní identifikátor zařízení, zvláště relevantní pro zařízení s duálním režimem nebo pro sítě, které migrovaly z [CDMA](/mobilnisite/slovnik/cdma/) na LTE/5G. Protokoly jako 3GPP TS 29.274 (GTPv2-C) a TS 24.229 (řízení multimediálních hovorů přes IP) specifikují, jak může být MEID zapouzdřen a přenášen v signalizačních zprávách. Například ve scénářích zahrnujících mobilitu mezi různými rádiovými přístupovými technologiemi (inter-RAT) nebo roaming mezi sítěmi 3GPP a 3GPP2 mohou síťové funkce použít MEID k jednoznačné identifikaci zařízení. Může být přenášen v informačních prvcích podobně jako IMEI, což umožňuje entitám jádra sítě, jako je [MME](/mobilnisite/slovnik/mme/), [SGSN](/mobilnisite/slovnik/sgsn/) nebo [PCRF](/mobilnisite/slovnik/pcrf/), jej zpracovat.

Jeho funkční role je paralelní k roli IMEI/[MEI](/mobilnisite/slovnik/mei/): identifikace zařízení, prevence krádeží a správa zařízení. Síťový operátor může udržovat Registr identit zařízení ([EIR](/mobilnisite/slovnik/eir/)), který podporuje kontroly jak IMEI, tak MEID. Když se zařízení s MEID připojí, síť může dotazovat EIR, aby zjistila, zda je zařízení v síti povoleno. To je klíčové pro udržování bezpečnostních politik napříč heterogenní populací zařízení. Zařazení MEID do specifikací 3GPP zajišťuje, že sítě mohou bezproblémově identifikovat a spravovat starší CDMA zařízení, zatímco operátoři sbližují své sítě k jednotným standardům 3GPP, což usnadňuje technologický přechod.

## K čemu slouží

MEID byl vytvořen v rámci domény 3GPP2, aby naplnil stejnou základní potřebu jako [IMEI](/mobilnisite/slovnik/imei/) v GSM/UMTS: poskytnout jedinečný, trvalý identifikátor zařízení pro CDMA telefony. Jeho přijetí do specifikací 3GPP bylo motivováno praktickou nutností konvergence sítí a provozu mezi standardy. Když mobilní operátoři začali nasazovat sítě LTE založené na 3GPP a vyřazovat starší CDMA sítě, vznikla jasná potřeba, aby tyto nové sítě rozpoznaly a spravovaly miliony stávajících CDMA zařízení, která k nim mohla získat přístup, zejména během přechodných období nebo prostřednictvím roamingových dohod.

Toto zařazení řeší omezení spočívající v existenci oddělených, nekompatibilních schémat identit zařízení pro různé rádiové technologie, což by bránilo jednotným bezpečnostním politikám (jako jediný černý seznam pro všechna zařízení) a komplikovalo správu zařízení pro operátory provozující více technologické sítě. Definováním MEID ve specifikacích 3GPP umožnila standardizační organizace vytvořit most mezi těmito dvěma světy, což umožňuje funkcím jádra sítě zpracovávat identitu zařízení agnosticky, ať už pochází z nativní 3GPP UE nebo ze zařízení z linie 3GPP2. To podporuje prevenci podvodů, zákonné odposlechy a přesné analytické zpracování zařízení konsolidovaným způsobem.

## Klíčové vlastnosti

- 56bitový jedinečný identifikátor mobilního zařízení, zavedený v 3GPP2 (CDMA)
- Definován v 3GPP pro scénáře interoperability a spolupráce
- Typicky reprezentován jako 14místné hexadecimální číslo
- Používán pro identifikaci zařízení a dotazy do EIR v více technologických sítích
- Přenášen v signalizačních protokolech 3GPP (např. GTPv2-C, Diameter)
- Podporuje správu starších CDMA zařízení v sítích 3GPP

## Související pojmy

- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [EIR – Equipment Identity Register](/mobilnisite/slovnik/eir/)
- [CDMA – Code Division Multiple Access](/mobilnisite/slovnik/cdma/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.277** (Rel-19) — S102 Interface Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MEID na 3GPP Explorer](https://3gpp-explorer.com/glossary/meid/)
