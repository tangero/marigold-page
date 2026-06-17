---
slug: "mch"
url: "/mobilnisite/slovnik/mch/"
type: "slovnik"
title: "MCH – Multast Channel"
date: 2025-01-01
abbr: "MCH"
fullName: "Multast Channel"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mch/"
summary: "Downlinkový transportní kanál v LTE a NR navržený pro přenos typu point-to-multipoint, primárně používaný pro službu Multimedia Broadcast Multicast Service (MBMS). Přenáší data určená pro více uživate"
---

MCH je downlinkový transportní kanál v LTE a NR navržený pro přenos typu point-to-multipoint, primárně používaný pro MBMS k přenosu dat k více uživatelským zařízením (UE) v určité oblasti.

## Popis

Multicast Channel (MCH) je downlinkový transportní kanál definovaný ve specifikacích 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a převzatý do NR pro podobné účely. Jeho hlavní funkcí je doručovat obsah služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) více uživatelům současně v určené oblasti pokrytí MBMS. Jako transportní kanál se v protokolovém zásobníku nachází nad fyzickou vrstvou a pod vrstvou [MAC](/mobilnisite/slovnik/mac/). Je charakteristický svou povahou point-to-multipoint, což znamená, že jediný přenos ze sítě přijímají všechna přihlášená uživatelská zařízení (UE) v oblasti pokrytí, na rozdíl od unicastových kanálů věnovaných jedinému UE. Díky tomu je spektrálně efektivní pro populární obsah, jako je živé TV vysílání, sportovní události nebo aktualizace softwaru.

V architektuře LTE pro MBMS (eMBMS) je MCH mapován na specifické prostředky fyzické vrstvy. V časové doméně využívá subrámečky Multicast-Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)). V těchto subrámečcích více buněk synchronizovaně vysílá identické signály, což umožňuje uživatelským zařízením (UE) kombinovat signály z více vysílačů jako jeden silnější signál, čímž efektivně vytváří velkou oblast jedné frekvence (SFN). Tento MBSFN režim je klíčový pro dosažení dobrého pokrytí a kvality signálu pro vysílací služby. MCH přenáší jeden nebo více Multicast Traffic Channels ([MTCH](/mobilnisite/slovnik/mtch/)), což jsou logické kanály, z nichž každý je věnován konkrétní MBMS službě. Přenáší také Multicast Control Channel ([MCCH](/mobilnisite/slovnik/mcch/)), který poskytuje řídicí informace potřebné pro příjem MTCH uživatelskými zařízeními, jako jsou plánovací informace a oznámení služeb.

Vrstva MAC zajišťuje multiplexování více MTCH a MCCH na MCH. Plánování MCH je polostatické, což znamená, že přidělení prostředků (MBSFN subrámečků) je konfigurováno vyššími vrstvami ([RRC](/mobilnisite/slovnik/rrc/)) a zůstává relativně stabilní. V rámci přidělených prostředků používá MAC specifickou plánovací strukturu definovanou MCH Scheduling Information ([MSI](/mobilnisite/slovnik/msi/)) přenášenou v MCCH, která informuje uživatelská zařízení (UE) o tom, které subrámečky nesou data pro který MTCH. Na fyzické vrstvě procházejí data na MCH kanálovým kódováním (v LTE Turbo kódováním), modulací a jsou mapována na bloky fyzických prostředků (PRB) v MBSFN subrámečcích. V 5G NR je koncept multicast/broadcast podporován a zatímco termín MCH je používán v některých základních specifikacích, rámec NR pro multicast (často označovaný jako NR Multicast and Broadcast Services) definuje nové fyzické kanály, jako je Physical Downlink Shared Channel (PDSCH) se skupinovým společným plánováním pro multicast, což představuje vývoj oproti přístupu LTE-MCH.

## K čemu slouží

MCH byl vytvořen pro umožnění efektivního hromadného doručování obsahu přes mobilní sítě, čímž řeší neefektivitu použití více unicastových datových toků pro doručení stejného obsahu (např. živého zpravodajského přenosu) mnoha uživatelům ve stejné oblasti. Před vyhrazenými vysílacími/skupinovými kanály by síť musela pro každého uživatele vytvářet individuální přenosové cesty (bearery), což by spotřebovávalo nadměrné množství rádiových a jádrových síťových prostředků. MCH jako součást sady funkcí MBMS to řeší tím, že umožňuje jediný přenos obsloužit neomezený počet uživatelů v jeho oblasti pokrytí, což dramaticky zlepšuje spektrální účinnost pro služby vysílacího typu.

Historicky byla MBMS představena v 3G UMTS, ale eMBMS v LTE s technologií MCH a MBSFN představovala významný vývoj. Poskytovala vyšší datové rychlosti, lepší pokrytí díky zisku SFN a flexibilnější definice služebních oblastí. Motivací byl zájem operátorů nabízet služby mobilní televize a streamování obsahu jako zdroj příjmů, stejně jako aplikace pro veřejnou bezpečnost, kde jsou skupinové komunikace zásadní. Návrh MCH s MBSFN subrámečky mu umožňuje koexistovat s unicastovým provozem na stejném nosiči, což poskytuje flexibilitu nasazení sítě.

V éře 5G přetrvává potřeba efektivní skupinové komunikace pro aplikace jako veřejná bezpečnost, skupinové zprávy vehicle-to-everything (V2X), streamování živých událostí a aktualizace IoT softwaru. Zatímco NR se zpočátku zaměřovalo na rozšířené mobilní širokopásmové připojení (eMBB), rámec pro multicast a broadcast v NR, stavící na konceptu MCH, je vyvíjen pro podporu těchto nových případů užití se vylepšenými výkonnostními charakteristikami 5G, jako je nižší latence a podpora širších šířek pásma. Vývoj z MCH v LTE k multicastovým mechanismům v NR řeší potřebu dynamičtějšího plánování a integrace s architekturou 5G Core založenou na službách.

## Klíčové vlastnosti

- Downlinkový transportní kanál typu point-to-multipoint pro efektivní doručování vysílacích (broadcast) a skupinových (multicast) dat.
- Primárně používán pro službu Multimedia Broadcast Multicast Service (MBMS) v LTE a NR.
- Využívá provoz MBSFN (Multicast-Broadcast Single Frequency Network) pro zlepšené pokrytí a kombinování signálů.
- Přenáší logické kanály: Multicast Traffic Channels (MTCH) pro uživatelská data a Multicast Control Channel (MCCH) pro řídicí informace.
- Má polostatické přidělování prostředků konfigurované pomocí signalizace RRC.
- Zajišťuje spektrální účinnost tím, že obsluhuje více uživatelských zařízení (UE) jediným rádiovým přenosem.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MTCH – MBMS point-to-multipoint Traffic Channel](/mobilnisite/slovnik/mtch/)
- [MCCH – MBMS point-to-multipoint Control Channel](/mobilnisite/slovnik/mcch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 26.881** (Rel-15) — MBMS FEC for Mission Critical Services Study
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [MCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/mch/)
