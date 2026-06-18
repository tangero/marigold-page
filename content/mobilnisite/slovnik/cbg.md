---
slug: "cbg"
url: "/mobilnisite/slovnik/cbg/"
type: "slovnik"
title: "CBG – Code Block Group"
date: 2025-01-01
abbr: "CBG"
fullName: "Code Block Group"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cbg/"
summary: "CBG (skupina kódových bloků) je jednotka pro retransmise v 5G NR, která sdružuje více kódových bloků pro HARQ zpětnou vazbu. Umožňuje částečné retransmise, čímž snižuje režii a latenci tím, že se retr"
---

CBG (skupina kódových bloků) je jednotka pro retransmise v 5G NR, která sdružuje více kódových bloků, aby umožnila částečné HARQ retransmise, čímž snižuje režii a latenci tím, že se retransmitují pouze chybné skupiny.

## Popis

Skupina kódových bloků (CBG) je základní koncept ve fyzické vrstvě 5G New Radio (NR), konkrétně v rámci procesu Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)) pro řízení chyb. V NR je transportní blok ([TB](/mobilnisite/slovnik/tb/)), což je základní jednotka dat pro přenos přes rozhraní vzduchu, před kanálovým kódováním segmentován na menší kódové bloky ([CB](/mobilnisite/slovnik/cb/)). CBG je soubor jednoho nebo více těchto kódových bloků. Primární funkcí přenosu založeného na CBG je umožnit podrobnější retransmise. Namísto signalizace HARQ zpětné vazby ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) a provádění retransmisí na úrovni celého transportního bloku může síť pracovat na úrovni CBG. To znamená, že přijímač může identifikovat a vyžádat retransmisi pouze těch konkrétních CBG, které obsahovaly chyby, nikoli celého TB.

Provoz zahrnuje několik klíčových komponent a procedur. Během počátečního přenosu gNB (základnová stanice) vysílá TB, který je segmentován na CB, a tyto CB jsou logicky seskupeny do CBG na základě konfigurace. Počet CBG na TB je konfigurovatelný pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/), s maximem definovaným specifikací (např. až 8 CBG pro TB v některých konfiguracích). Každá CBG je nezávisle kanálově kódována. Přijímač (UE) provádí dekódování a generuje HARQ zpětnou vazbu ve formě bitmapy ACK/NACK založené na CBG. Tato bitmapa indikuje úspěch (ACK) nebo selhání (NACK) každé jednotlivé CBG. gNB zpracuje tuto zpětnou vazbu a naplánuje retransmise specificky pro CBG označené jako NACK. Retransmitované CBG mohou používat stejné nebo různé redundantní verze ([RV](/mobilnisite/slovnik/rv/)), jak je definováno v procesu HARQ.

Z architektonického hlediska je zpracování CBG integrováno do zpracování fyzického downlinkového sdíleného kanálu ([PDSCH](/mobilnisite/slovnik/pdsch/)) a fyzického uplinkového sdíleného kanálu (PUSCH) v rámci protokolových zásobníků gNB a UE, primárně ve vrstvách MAC a fyzické vrstvě. Konfigurace, včetně toho, zda je přenos založený na CBG povolen a kolik CBG se použije, je určena RRC a může být přizpůsobena na základě podmínek kanálu. Formáty řídicí informace pro downlink (DCI) obsahují pole pro indikaci informace o přenosu CBG (CBGTI) a informace o proplachování CBG (CBGFI), které řídí, které CBG jsou přenášeny a zda má být propláchnut předchozí obsah soft bufferu. Tento mechanismus je klíčový pro správu paměti soft bufferu v přijímači, protože ukládá logaritmy věrohodnostních poměrů pro kombinování inkrementální redundance.

Role CBG v síti spočívá ve zvýšení účinnosti procesu HARQ, což je klíčové pro dosažení vysoké spolehlivosti a nízké latence v 5G, zejména pro služby rozšířeného mobilního širokopásmového přístupu (eMBB) a ultra-spolehlivé komunikace s nízkou latencí (URLLC). Tím, že se sníží množství dat, která je třeba retransmitovat, když je poškozena pouze část TB, retransmise založená na CBG minimalizuje spotřebu prostředků rozhraní vzduchu, snižuje latenci pro obnovu po chybě a zlepšuje celkovou propustnost a spektrální účinnost. Představuje významný vývoj oproti přístupu LTE, kde byly retransmise primárně založeny na TB, a nabízí jemnější řízení a lepší výkon v náročných rádiových podmínkách.

## K čemu slouží

Přenos založený na CBG byl zaveden v 5G NR, aby řešil omezení HARQ založeného na transportním bloku (TB) používaného v LTE. V LTE, pokud jakákoli část TB selhala při dekódování, musel být retransmitován celý TB – potenciálně velká datová jednotka. To bylo neefektivní, zejména s rostoucí velikostí TB a vyššími datovými rychlostmi v 5G. Retransmise celého TB spotřebovala nadměrný čas a rádiové zdroje, zvyšovala latenci a snižovala spektrální účinnost, což bylo škodlivé pro služby citlivé na latenci, jako je URLLC, a pro udržení vysoké propustnosti ve špatných signálových podmínkách.

Primární problém, který CBG řeší, je granularita retransmisí. Seskupením kódových bloků umožňuje systému identifikovat a retransmitovat pouze poškozené podmnožiny dat. Tato schopnost částečné retransmise významně snižuje režii a zpoždění spojené s obnovou po chybě. Historicky motivace vycházela z potřeby podporovat rozmanité případy užití 5G s přísnými požadavky. Pro eMBB jsou velké TB běžné a CBG zabraňuje tomu, aby malé chyby spouštěly velké retransmise. Pro URLLC je minimalizace latence prvořadá a rychlá oprava chyb prostřednictvím cílených retransmisí je klíčová.

Dále CBG umožňuje efektivnější využití paměti soft bufferu UE pro HARQ kombinování. Namísto ukládání soft bitů pro celý TB pro případnou retransmisi může UE spravovat paměť na úrovni CBG, což umožňuje lepší výkon s omezenou velikostí bufferu. Tím se řeší praktická implementační omezení. Vytvoření CBG bylo hnací silou cíle 3GPP navrhnout flexibilnější a efektivnější rozhraní vzduchu pro NR, s poučením ze zkušeností s LTE a v očekávání potřeb budoucích vysokorychlostních aplikací s nízkou latencí.

## Klíčové vlastnosti

- Umožňuje částečné retransmise na úrovni granularity skupiny kódových bloků namísto retransmise celého transportního bloku
- Konfigurovatelný počet CBG na transportní blok pomocí signalizace RRC pro flexibilitu
- Používá bitmapu zpětné vazby ACK/NACK založenou na CBG pro přesnou indikaci chyb
- Obsahuje pole DCI (CBGTI, CBGFI) pro dynamické řízení retransmisí a správy soft bufferu
- Snižuje latenci HARQ retransmisí a zlepšuje spektrální účinnost
- Podporuje jak downlinkové (PDSCH), tak uplinkové (PUSCH) kanály

## Související pojmy

- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)

## Definující specifikace

- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [CBG na 3GPP Explorer](https://3gpp-explorer.com/glossary/cbg/)
