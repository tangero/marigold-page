---
slug: "pagch"
url: "/mobilnisite/slovnik/pagch/"
type: "slovnik"
title: "PAGCH – Packet Access Grant Channel"
date: 2025-01-01
abbr: "PAGCH"
fullName: "Packet Access Grant Channel"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pagch/"
summary: "Společný řídicí kanál v sestupné větvi v sítích GPRS/EDGE, který síť využívá k přidělení rádiových prostředků mobilní stanici zahajující přenos paketů. Doručuje zprávu Packet Uplink Assignment jako od"
---

PAGCH je společný řídicí kanál v sestupné větvi v sítích GPRS/EDGE, který přiděluje rádiové prostředky mobilní stanici tím, že doručí zprávu Packet Uplink Assignment jako odpověď na její žádost o kanál.

## Popis

Packet Access Grant Channel (PAGCH) je logický vysílací řídicí kanál v rámci GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)) pro přepojování paketů. Funguje pouze ve směru downlink a jde o společný kanál, což znamená, že není vyhrazen konkrétnímu uživateli, ale je monitorován všemi GPRS-kompatibilními mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)) v buňce, které jsou v pohotovostním nebo připraveném stavu a chtějí zahájit přenos dat ve směru uplink. PAGCH je klíčovou součástí procedury náhodného přístupu pro pakety. Jeho jediným, definovaným účelem je přenášet zprávu 'Packet Uplink Assignment' ze sítě konkrétní MS.

Z architektonického hlediska je PAGCH namapován na [PCCCH](/mobilnisite/slovnik/pccch/) (Packet Common Control Channel), pokud je tento v buňce nakonfigurován. Pokud PCCCH není přítomen, je PAGCH namapován na [CCCH](/mobilnisite/slovnik/ccch/) (Common Control Channel) systému GSM, konkrétně využívá časové sloty [AGCH](/mobilnisite/slovnik/agch/) (Access Grant Channel). Tato zpětná kompatibilita je nezbytná pro počáteční nasazení [GPRS](/mobilnisite/slovnik/gprs/). Kanál pracuje v těsně provázané sekvenci s [PRACH](/mobilnisite/slovnik/prach/) (Packet Random Access Channel). MS s daty k odeslání vyšle 'Packet Channel Request' na PRACH. Síťový BSC po přijetí této žádosti přidělí rádiové prostředky (jeden či více PDCH - Packet Data Channels) a odešle detaily přidělení, včetně TFI (Temporary Flow Identity) a přidělených časových slotů, ve zprávě Packet Uplink Assignment na PAGCH.

Operace je založena na soupeření (contention-based) kvůli PRACH, proto zpráva na PAGCH obsahuje identifikátory (jako Random Access Reference), které spojují přidělení s konkrétní žádostí. MS musí po odeslání své žádosti průběžně monitorovat PAGCH (nebo AGCH), aby přijalo přidělení. Po úspěšném příjmu MS přepne na přidělený PDCH(y) a zahájí uplink přenos na PDTCH, čímž se ustaví Temporary Block Flow (TBF). PAGCH již neřídí probíhající TBF; tato role je předána kanálu PACCH. Funkce PAGCH je tedy čistě pro počáteční přidělení přístupu a kanál funguje jako vrátný, který převádí pokus o náhodný přístup na vyhrazené (i když dočasné) přidělení prostředků pro paketová data.

## K čemu slouží

PAGCH byl zaveden, aby umožnil řízený a efektivní přístup k prostředkům pro přepojování paketů v síti GSM, původně navržené pro sestavování okruhově přepínaných hovorů. V okruhově přepínané GSM měl AGCH podobnou funkci pro hlasové hovory, kdy přiděloval vyhrazený kanál (TCH). Pro paketová data bylo potřeba jiné paradigma: prostředky nejsou vyhrazeny na dobu trvání 'hovoru', ale jsou dočasně přiděleny pro dávku dat.

Účelem PAGCH je řídit fázi řešení soupeření a počátečního přidělení prostředků paketové datové relace. Bez něj by mobilní stanice neměly definovaný mechanismus, jak zjistit, které rádiové prostředky smějí použít pro uplink přenos po provedení pokusu o náhodný přístup. Řeší problém koordinace více uživatelů soutěžících na sdíleném kanálu pro náhodný přístup o sdílené paketové prostředky. Poskytnutím vysílacího kanálu pro doručení cílených zpráv s přidělením umožňuje síti centrálně řídit a optimalizovat alokaci uplink PDCH.

Tento návrh řešil omezení využití stávajícího hlasově orientovaného AGCH, který nebyl optimalizován pro parametry paketového TBF (jako TFI). Vytvoření přidělovacího kanálu specifického pro pakety, i když byl logicky namapován na stejné fyzické prostředky jako AGCH v počátcích, umožnilo nezbytná signalizační rozšíření a jasné procedurální oddělení mezi okruhovým a paketovým přístupem. Šlo o základní stavební kámen pro přeměnu spojově orientovaného přístupu GSM na dynamičtější, paketově orientovaný přístup, což umožnilo efektivní přidělování prostředků na vyžádání, které charakterizuje služby mobilních dat.

## Klíčové vlastnosti

- Společný řídicí kanál v sestupné větvi pro počáteční přístup v GPRS/EDGE
- Přenáší zprávu Packet Uplink Assignment ze sítě k MS
- Namapován na PCCCH, pokud je dostupný, jinak na GSM CCCH/AGCH
- Klíčová součást procedury náhodného přístupu pro pakety založené na soupeření
- Přiděluje počáteční uplink prostředky PDCH a dočasnou identitu toku (TFI)
- Umožňuje přechod z pohotovostního/připraveného stavu do aktivního TBF pro uplink přenos

## Související pojmy

- [PRACH – Physical Random Access Channel](/mobilnisite/slovnik/prach/)
- [PCCCH – Packet Common Control Channel](/mobilnisite/slovnik/pccch/)
- [AGCH – Access Grant Channel](/mobilnisite/slovnik/agch/)
- [TBF – Temporary Block Flow](/mobilnisite/slovnik/tbf/)
- [PDCH – Packet Data Channel](/mobilnisite/slovnik/pdch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [PAGCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/pagch/)
