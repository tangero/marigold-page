---
slug: "bvci"
url: "/mobilnisite/slovnik/bvci/"
type: "slovnik"
title: "BVCI – BSS GPRS Protocol Virtual Connection Identifier"
date: 2025-01-01
abbr: "BVCI"
fullName: "BSS GPRS Protocol Virtual Connection Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bvci/"
summary: "BVCI je jedinečný identifikátor používaný na rozhraní Gb mezi podsystémem základnové stanice (BSS) a uzlem podpory GPRS (SGSN) v sítích 2G/3G. Identifikuje virtuální spojení pro přenos GPRS dat a umož"
---

BVCI je jedinečný identifikátor na rozhraní Gb mezi BSS a SGSN, který identifikuje virtuální spojení pro multiplexování více kontextů GPRS dat přes jeden fyzický spoj.

## Popis

[BSS](/mobilnisite/slovnik/bss/) [GPRS](/mobilnisite/slovnik/gprs/) Protocol Virtual Connection Identifier (BVCI) je základním prvkem v architektuře rozhraní Gb, které spojuje GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiovou přístupovou síť ([GERAN](/mobilnisite/slovnik/geran/)) s GPRS jádrem sítě. Funguje v rámci protokolu BSS GPRS Protocol ([BSSGP](/mobilnisite/slovnik/bssgp/)), což je protokol vrstvy 3 definovaný v 3GPP TS 48.016. BVCI slouží jako lokální identifikátor na rozhraní Gb, který jednoznačně označuje virtuální spojení mezi konkrétní BSS a SGSN. Toto virtuální spojení je v podstatě logická cesta používaná pro přenos signalizace GPRS a paketů uživatelských dat spojených s mobilními stanicemi ([MS](/mobilnisite/slovnik/ms/)) obsluhovanými danou BSS.

Z architektonického hlediska BVCI funguje ve spojení s dalšími identifikátory, jako je Network Service Access Point Identifier (NSAPI) a Temporary Logical Link Identity (TLLI). Zatímco TLLI identifikuje konkrétní MS na rádiovém rozhraní (Um) a vrstvě [LLC](/mobilnisite/slovnik/llc/) a NSAPI identifikuje konkrétní PDP kontext pro dané MS, BVCI poskytuje kontext směrování na rozhraní Gb. Pro danou BSS a SGSN je zřízeno jediné BVCI, ale toto BVCI nese multiplexovaný provoz pro všechna MS a jejich PDP kontexty aktivní v buňkách řízených touto BSS. Vrstva BSSGP používá BVCI ke správnému směrování downlink paketů ze SGSN do správné BSS a následně do správné buňky a MS. Naopak uplink pakety z BSS do SGSN jsou také označeny BVCI.

Klíčovými komponentami jsou BSS (zahrnující [BTS](/mobilnisite/slovnik/bts/) a BSC) a SGSN. BVCI je přiřazeno během inicializace rozhraní Gb nebo konfigurace BSS. Není signalizováno přes rádiové rozhraní k MS; jde čistě o identifikátor na síťové straně pro správu rozhraní Gb. Jeho role spočívá v abstrakci fyzického spoje Gb (často na bázi Frame Relay nebo IP) do logických spojení, což umožňuje, aby jediné fyzické rozhraní efektivně obsluhovalo provoz pro tisíce mobilních uživatelů. Tato schopnost multiplexování je klíčová pro škálovatelnost a optimalizaci zdrojů v přístupové síti.

Při provozu, když má SGSN downlink data pro MS, použije BVCI spojené s BSS, která obsluhuje aktuální buňku tohoto MS. PDU BSSGP obsahující data zahrnuje BVCI. BSS toto PDU přijme, ověří BVCI, aby potvrdila, že je určeno pro ni, a poté použije přidružené TLLI a další informace ke směrování dat ke správnému rádiovému zdroji (např. ke konkrétnímu PDTCH). Toto oddělení funkcí – směrování na rozhraní Gb pomocí BVCI a směrování na rádiovém rozhraní pomocí TLLI – zjednodušuje návrh sítě a zvyšuje její spolehlivost.

## K čemu slouží

BVCI bylo vytvořeno k řešení základního problému efektivní správy a směrování paketově přepínaného datového provozu přes stávající infrastrukturu GSM orientovanou na přepojování okruhů při zavedení GPRS. Před GPRS byly sítě GSM navrženy primárně pro hlasová volání s vyhrazenými fyzickými kanály (TCH) přiřazenými na A-rozhraní pro každé volání. Tento model byl neefektivní pro přerušovaný, nárazový datový provoz. Zavedení přepojování paketů vyžadovalo metodu pro multiplexování datových relací mnoha uživatelů přes sdílené síťové zdroje.

BVCI tento problém řeší tím, že poskytuje logický multiplexní identifikátor na kritickém spoji mezi rádiovou přístupovou sítí (BSS) a paketovým jádrem (SGSN). Bez takového identifikátoru by síť musela pro každé MS nebo PDP kontext zřídit samostatný fyzický nebo permanentní virtuální okruh (v kontextu Frame Relay), což by bylo nepřiměřeně složité a náročné na zdroje. BVCI umožňuje existenci jediného, spravovaného virtuálního spojení (reprezentujícího agregovaný provoz pro všechny uživatele GPRS v oblasti BSS) na rozhraní Gb. To dramaticky snižuje signalizační režii a zjednodušuje konfiguraci a správu sítě.

Historicky bylo jeho vytvoření motivováno potřebou škálovatelné a nákladově efektivní cesty migrace k mobilním datům v rámci architektury 3GPP Release 99. Umožnilo opětovné využití stávající infrastruktury BSS s minimálními hardwarovými změnami při současném zavedení paketově přepínaného jádra. BVCI jako součást protokolu BSSGP bylo klíčovým prvkem pro model 'vždy připojen' (always-on) u GPRS, který umožňuje síti spravovat stav uživatele a směrování dat bez nutnosti udržovat vyhrazené end-to-end okruhy.

## Klíčové vlastnosti

- Jednoznačně identifikuje virtuální spojení mezi konkrétní BSS a SGSN na rozhraní Gb
- Umožňuje multiplexování veškerého uživatelského a řídicího provozu GPRS pro BSS přes jedinou logickou cestu
- Spolupracuje s TLLI a NSAPI pro end-to-end směrování paketů ze SGSN k mobilnímu zařízení
- Je identifikátorem na síťové straně, který není vystaven uživatelskému zařízení (UE), čímž zjednodušuje provoz mobilního zařízení
- Je nezbytné pro směrovací funkci protokolu BSSGP, která směruje downlink pakety do správné BSS
- Podporuje škálovatelnost abstrakcí fyzické vrstvy, což umožňuje mnoha uživatelům sdílet zdroje přístupové sítě

## Související pojmy

- [BSSGP – Base Station System GPRS Protocol](/mobilnisite/slovnik/bssgp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [BVCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/bvci/)
