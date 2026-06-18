---
slug: "umd"
url: "/mobilnisite/slovnik/umd/"
type: "slovnik"
title: "UMD – Unacknowledged Mode Data"
date: 2025-01-01
abbr: "UMD"
fullName: "Unacknowledged Mode Data"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/umd/"
summary: "Unacknowledged Mode Data (UMD) označuje specifický formát protokolové datové jednotky (PDU), který používá vrstva řízení rádiového spoje (RLC) při provozu v nepotvrzovaném režimu (UM). Jedná se o stru"
---

UMD je formát protokolové datové jednotky používaný vrstvou RLC v nepotvrzovaném režimu (Unacknowledged Mode). Obsahuje hlavičku s pořadovým číslem a segmentačními údaji spolu s užitečným zatížením pro přenos vzdušným rozhraním.

## Popis

Unacknowledged Mode Data (UMD) je označení pro protokolovou datovou jednotku ([PDU](/mobilnisite/slovnik/pdu/)) používanou entitou řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)), pokud je nakonfigurována v nepotvrzovaném režimu ([UM](/mobilnisite/slovnik/um/)). RLC PDU je blok dat předávaný mezi vrstvou RLC a podkladovou vrstvou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) pro přenos přes rádiové rozhraní. UMD PDU má specifickou strukturu definovanou ve specifikacích 3GPP, která umožňuje funkce RLC v nepotvrzovaném režimu. Tato PDU se skládá ze dvou hlavních částí: hlavičky RLC UMD a užitečného zatížení RLC UMD. Užitečné zatížení obsahuje buď celou RLC služební datovou jednotku ([SDU](/mobilnisite/slovnik/sdu/)), nebo segment RLC SDU, v závislosti na tom, zda byla použita segmentace.

Hlavička UMD je klíčová pro činnost přijímače. Její pole zahrnují pořadové číslo ([SN](/mobilnisite/slovnik/sn/)), které se používá pro doručování ve správném pořadí a detekci chybějících PDU. Délka pole SN (např. 5 bitů v některých konfiguracích LTE, 6 nebo 10 bitů v jiných) je konfigurována vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)). Hlavička také obsahuje pole rámcových informací ([FI](/mobilnisite/slovnik/fi/)), která označují, zda PDU obsahuje první a/nebo poslední segment RLC SDU. To umožňuje přijímači správně identifikovat hranice původních SDU při opětovném sestavování. Dále bit rozšíření (E) indikuje, zda následuje sada dalších polí hlavičky (ukazatelů délky). Ukazatele délky (LI) se používají, když UMD PDU obsahuje více než jeden segment RLC SDU nebo kombinaci SDU a segmentu; určují hranice mezi těmito prvky uvnitř užitečného zatížení.

Z architektonického hlediska vysílající entita RLC UM konstruuje UMD PDU. Přijímá RLC SDU z vyšší vrstvy (např. PDCP), ukládá je do vyrovnávací paměti a může je segmentovat a/nebo řetězit na základě velikosti přenosového bloku přiděleného vrstvou MAC. Poté sestaví UMD PDU přidáním příslušné hlavičky se správným SN a rámcovými informacemi. Pořadové číslo se zvyšuje pro každou novou UMD PDU. Na přijímací straně entita RLC UM extrahuje informace SN a LI. Pomocí SN umisťuje přijatá datová zatížení do vyrovnávací paměti pro opětovné sestavení ve správném pořadí. Pole LI a FI přijímači sdělují, jak rekonstruovat původní RLC SDU z uložených segmentů. Jakmile je kompletní SDU znovu sestaveno (což je indikováno příznakem 'poslední segment'), je doručeno ve správném pořadí do vyšší vrstvy. Celý proces funguje bez jakékoli zpětné vazby k vysílači, což činí z UMD PDU na úrovni RLC datovou jednotku typu 'vystřel a zapomeň'.

## K čemu slouží

Formát UMD PDU byl definován, aby poskytl standardizovaný a efektivní kontejner pro data přenášená v nepotvrzovaném režimu. Bez specifické struktury PDU by vrstva RLC nemohla podporovat své základní funkce doručování ve správném pořadí a segmentace/opětovného sestavení. Účelem UMD je zapouzdřit data vyšší vrstvy s právě dostatečnými řídicími informacemi (pořadové číslo, hranice segmentace), aby umožnily správné opětovné sestavení na straně přijímače, a zároveň minimalizovat režii pro zachování šířky pásma pro skutečná uživatelská data. To je obzvláště důležité pro služby v reálném čase, kde režie hlavičky přímo ovlivňuje spektrální účinnost.

Řeší problém přizpůsobení IP paketů (nebo jiných PDU vyšších vrstev) proměnné velikosti přenosovým blokům proměnné velikosti, které poskytuje fyzická vrstva prostřednictvím MAC. Možnosti segmentace a řetězení signalizované prostřednictvím polí hlavičky UMD umožňují efektivní zabalení dat do rádiových zdrojů. Pořadové číslo řeší problém doručování mimo pořadí, ke kterému může dojít přes rádiové rozhraní v důsledku HARQ retransmisí na vrstvě MAC nebo diverzity přenosových cest. Definováním přesné struktury PDU UMD umožňuje interoperabilitu mezi vysílači a přijímači od různých výrobců a zajišťuje, že veškeré zařízení interpretuje datový proud správně. Jeho vytvoření bylo nedílnou součástí specifikace protokolu RLC, což umožnilo realizaci služby UM v praxi.

## Klíčové vlastnosti

- Definovaná struktura PDU pro činnost RLC v nepotvrzovaném režimu
- Hlavička obsahuje pořadové číslo pro doručování ve správném pořadí a detekci ztrát
- Obsahuje rámcové informace pro označení začátku/konce RLC SDU
- Využívá ukazatele délky k vymezení více datových segmentů v rámci jedné PDU
- Podporuje segmentaci a řetězení SDU vyšších vrstev
- Konfigurovatelná velikost hlavičky na základě konfigurace RRC (délka SN)

## Související pojmy

- [RLC-PDU – Radio Link Control - Protocol Data Unit](/mobilnisite/slovnik/rlc-pdu/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification
- **TS 38.322** (Rel-19) — NR Radio Link Control (RLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [UMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/umd/)
