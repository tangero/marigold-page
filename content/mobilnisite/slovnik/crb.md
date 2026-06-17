---
slug: "crb"
url: "/mobilnisite/slovnik/crb/"
type: "slovnik"
title: "CRB – Common Resource Block"
date: 2025-01-01
abbr: "CRB"
fullName: "Common Resource Block"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/crb/"
summary: "Common Resource Block (CRB) je základní jednotkou fyzické alokace prostředků v rádiovém rozhraní 5G NR, definovaná vůči společnému referenčnímu bodu. Poskytuje standardizovanou mřížku pro mapování fyz"
---

CRB je základní jednotkou fyzické alokace prostředků v rádiovém rozhraní 5G NR, definovaná vůči společnému referenčnímu bodu, která poskytuje standardizovanou mřížku pro mapování kanálů a signálů.

## Popis

Common Resource Block (CRB) slouží jako absolutní referenční mřížka pro fyzickou alokaci prostředků v 5G New Radio (NR) a je definován ve specifikaci 3GPP 38.211. Každý CRB se skládá z 12 po sobě jdoucích subnosných ve frekvenční oblasti, přičemž rozteč subnosných (SCS) určuje přesnou šířku pásma každého CRB. Mřížka CRB je ukotvena ve společném referenčním bodě známém jako 'point A', který slouží jako absolutní frekvenční reference pro celou šířku pásma nosné. Tento point A je definován jako střed subnosné 0 nejnižšího CRB (CRB 0) a zůstává pevný bez ohledu na konfiguraci částí šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)) nebo možnosti uživatelského zařízení (UE).

Číslování CRB začíná od 0 a pokrývá celou šířku pásma nosné, čímž poskytuje souvislý číselný systém pro všechny dostupné zdrojové bloky. Tato společná mřížka umožňuje síti konzistentně spravovat prostředky napříč různými uživatelskými zařízeními s rozdílnými možnostmi šířky pásma. Při plánování prostředků pro konkrétní UE mapuje gNodeB přidělené fyzické zdrojové bloky (PRB) v aktivní části šířky pásma (BWP) tohoto UE na odpovídající indexy CRB. Toto mapování je klíčové pro udržení souladu mezi správou prostředků sítě a nakonfigurovanou šířkou pásma UE a zajišťuje, že obě entity odkazují na stejné fyzické prostředky, přestože operují v rámci různých omezení šířky pásma.

Vztah mezi CRB a PRB je zásadní pro alokaci prostředků v 5G. Zatímco CRB poskytují absolutní referenční mřížku pokrývající celou nosnou, PRB představují relativní zdrojové bloky v rámci konkrétní části šířky pásma (BWP). Převod mezi indexy PRB a CRB je definován parametrem offsetu (N_start_BWP), který udává, kde daná BWP začíná vůči společnému referenčnímu bodu. Tato architektura umožňuje flexibilní adaptaci šířky pásma při zachování konzistentního globálního rámce pro správu prostředků. Koncept CRB také podporuje scénáře agregace nosných, kde každá z komponentních nosných má svou vlastní mřížku CRB ukotvenou ve svém vlastním referenčním bodu point A.

V praktické implementaci se CRB používají pro různé funkce fyzické vrstvy, včetně přenosu bloků synchronizačních signálů (SSB), alokace fyzického společně sdíleného kanálu pro downlink ([PDSCH](/mobilnisite/slovnik/pdsch/)), plánování fyzického společně sdíleného kanálu pro uplink (PUSCH) a umisťování referenčních signálů. Společná referenční mřížka zajišťuje, že různé fyzické kanály a signály si zachovávají správné frekvenční zarovnání, což je klíčové pro zachování ortogonality a minimalizaci interference. Architektura CRB také podporuje funkci smíšené numerologie 5G NR, kde v rámci stejné nosné mohou koexistovat různé rozteče subnosných, přičemž každá numerologie má svou vlastní mřížku CRB definovanou vůči společnému referenčnímu bodu point A.

## K čemu slouží

Koncept Common Resource Block byl představen v 5G NR Release 15, aby odstranil omezení architektury zdrojových bloků v LTE, která byla méně flexibilní pro podporu různých scénářů nasazení a kmitočtových pásem. V LTE byly zdrojové bloky definovány vůči střednímu kmitočtu nosné, což způsobovalo problémy při podpoře širokých šířek pásma nosných a flexibilních alokací spektra. Architektura CRB s jejím absolutním referenčním bodem (point A) poskytuje robustnější základ pro správu prostředků v různých konfiguracích šířky pásma a scénářích agregace nosných.

Klíčovou motivací pro koncept CRB byla podpora zvýšených požadavků na flexibilitu v 5G NR, včetně podpory více numerologií, proměnlivých částí šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)) a různých kmitočtových rozsahů od pásem pod 6 GHz až po milimetrové vlny. Společná referenční mřížka umožňuje konzistentní správu prostředků napříč těmito různorodými scénáři a zajišťuje, že rozhodnutí o plánování, koordinace interference a algoritmy správy rádiových prostředků mohou pracovat s jednotným chápáním dostupných spektrálních zdrojů. To je obzvláště důležité pro scénáře dynamického sdílení spektra a agregace spektra, kde mohou být různé části šířky pásma přiděleny různým službám nebo operátorům.

Architektura CRB také řeší potřebu lepší koexistence s LTE a dalšími technologiemi rádiového přístupu. Poskytnutím jasné, absolutní reference pro alokaci prostředků umožňuje systém CRB lepší správu interference mezi 5G NR a staršími systémy operujícími v přilehlém spektru. Toto bylo významným vylepšením oproti předchozím přístupům spoléhajícím se na relativní reference, které mohly vést k nejednoznačnosti v koordinaci prostředků mezi různými síťovými prvky a technologiemi. Standardizovaná mřížka CRB se stala základním kamenem schopnosti 5G efektivně využívat fragmentované spektrum a podporovat různorodé scénáře nasazení.

## Klíčové vlastnosti

- Absolutní referenční frekvenční mřížka ukotvená v bodě point A
- Souvislé číslování napříč celou šířkou pásma nosné
- 12 subnosných na CRB s konfigurovatelnou roztečí subnosných (SCS)
- Podporuje více numerologií (SCS 15, 30, 60, 120, 240 kHz)
- Umožňuje mapování mezi PRB a absolutními frekvenčními prostředky
- Základ pro konfiguraci a správu částí šířky pásma (BWP)

## Související pojmy

- [BWP – Bandwidth Part](/mobilnisite/slovnik/bwp/)

## Definující specifikace

- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CRB na 3GPP Explorer](https://3gpp-explorer.com/glossary/crb/)
