---
slug: "olpc"
url: "/mobilnisite/slovnik/olpc/"
type: "slovnik"
title: "OLPC – Outer Loop Power Control"
date: 2025-01-01
abbr: "OLPC"
fullName: "Outer Loop Power Control"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/olpc/"
summary: "Outer Loop Power Control (OLPC) je algoritmus řízení rádiových zdrojů v mobilních sítích, který dynamicky upravuje cílový poměr signálu k interferenci (SIR) pro spojení. Funguje pomaleji než vnitřní s"
---

OLPC je algoritmus řízení rádiových zdrojů, který dynamicky upravuje cílový poměr signálu k interferenci pro spojení, aby udržel požadovanou kvalitu služby.

## Popis

Outer Loop Power Control (OLPC) je klíčovou součástí mechanismů řízení výkonu v uplinku a downlinku v rádiových přístupových technologiích 3GPP, jako jsou UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)), LTE a NR. Funguje ve spojení s rychlejší vnitřní smyčkou řízení výkonu (ILPC). Zatímco ILPC (neboli rychlé řízení výkonu) pracuje rychlostí 1500 Hz v UMTS nebo v každém podrámci v LTE/NR, aby rychle kompenzovala útlumy úpravou výkonu pro dosažení cílového [SIR](/mobilnisite/slovnik/sir/), OLPC pracuje v mnohem pomalejším časovém měřítku, typicky v řádu stovek milisekund až sekund.

Primární funkcí OLPC je určit vhodný cílový SIR (nebo ekvivalentní metriku, jako je cílová hodnota [SINR](/mobilnisite/slovnik/sinr/) v LTE/NR) pro ILPC. Děje se tak monitorováním kvality přijatých dat, například blokové chybovosti ([BLER](/mobilnisite/slovnik/bler/)) nebo chybovosti paketů. Algoritmus OLPC, který se typicky nachází v radiové síťové řadiči ([RNC](/mobilnisite/slovnik/rnc/)) pro UMTS nebo v základnové stanici ([eNB](/mobilnisite/slovnik/enb/)/gNB) pro LTE/NR, porovnává naměřenou BLER s cílovou BLER nastavenou entitou řízení rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) na základě požadované QoS pro službu (např. 1 % pro hlas, 10 % pro best-effort data). Je-li naměřená BLER vyšší než cílová, OLPC zvýší cílový SIR, čímž nařídí ILPC usilovat o silnější signál. Naopak, pokud je BLER nižší, než je potřeba, sníží cílový SIR, aby se šetřil výkon a snížila síťová interference.

Tento adaptivní proces zajišťuje, že je použito minimálního nutného výkonu pro dosažení požadované kvality spojení, což je zásadní pro kapacitu sítě a životnost baterie. Ve scénářích agregace nosných a duální konektivity definovaných v pozdějších vydáních se OLPC stává složitějším, neboť spravuje řízení výkonu napříč více komponentními nosnými nebo spojovacími body. Algoritmy a parametry pro OLPC jsou podrobně specifikovány v řadě 25.7xx pro UMTS/[HSPA](/mobilnisite/slovnik/hspa/) a v řadě 38.8xx pro NR a pokrývají různé scénáře nasazení a fyzické kanály.

## K čemu slouží

OLPC byl vyvinut k řešení omezení spoléhání se pouze na rychlou vnitřní smyčku řízení výkonu založenou na SIR. Zatímco ILPC výborně kompenzuje rychlé útlumy, nemá žádnou vlastní znalost o tom, zda výsledná kvalita spoje (BLER) je pro poskytovanou službu dostatečná nebo nadbytečná. Pevně nastavený cílový SIR by byl neefektivní: pokud je nastaven příliš nízko, vede ke špatné kvalitě a přerušovaným hovorům; pokud je nastaven příliš vysoko, plýtvá vysílacím výkonem, zvyšuje interferenci ostatním uživatelům a snižuje celkovou kapacitu sítě i životnost baterie.

Účelem OLPC je dynamicky a autonomně najít optimální cílový SIR, který právě splňuje požadovanou BLER pro danou službu a podmínky rádiového kanálu. Tím se řeší problém udržování konzistentní kvality služby (např. srozumitelnosti hlasu, datové propustnosti) pro mobilního uživatele pohybujícího se různými prostředími (od otevřeného prostoru po hustou městskou zástavbu) bez nutnosti manuálního nastavení sítě. Jeho vznik byl motivován potřebou robustního a adaptivního řízení rádiových zdrojů v systémech založených na CDMA, jako je UMTS, kde je interference hlavním limitujícím faktorem kapacity, a tento princip se přímo přenáší do systémů založených na OFDMA, jako je LTE a NR, pro řízení uplinku.

Historicky umožnil systémům WCDMA naplnit jejich kapacitní potenciál a podporovat smíšené služby s různými požadavky na QoS na stejné nosné. Je to základní algoritmus pro dosažení jednoho z klíčových cílů mobilních sítí: spolehlivé kvality služby kdekoli, při současné maximalizaci počtu současných uživatelů, které síť dokáže podporovat.

## Klíčové vlastnosti

- Dynamicky upravuje cílový SIR/SINR pro vnitřní smyčku řízení výkonu
- Funguje na základě měřených metrik kvality spoje (např. BLER, PER)
- Pomalejší časové měřítko (stovky ms až sekundy) ve srovnání s rychlou vnitřní smyčkou
- Přizpůsobuje se dlouhodobým změnám kanálu, mobilitě a QoS služby
- Nachází se v RNC (UMTS) nebo základnové stanici (LTE/NR)
- Klíčový pro vyvážení kvality spoje, interference a spotřeby výkonu

## Související pojmy

- [SIR – Signal-to-Interference Ratio](/mobilnisite/slovnik/sir/)
- [BLER – Block Error Rate](/mobilnisite/slovnik/bler/)
- [RRM – Radio Resource Management](/mobilnisite/slovnik/rrm/)

## Definující specifikace

- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TR 38.785** (Rel-17) — UE radio transmission for enhanced NR sidelink
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TS 38.787** (Rel-19) — UE Radio Transmission for Sidelink CA in ITS Band
- **TR 38.859** (Rel-18) — Technical Report
- **TR 38.868** (Rel-17) — Optimizations of pi/2 BPSK uplink power in NR
- **TR 38.886** (Rel-16) — NR V2X UE Radio Transmission & Reception

---

📖 **Anglický originál a plná specifikace:** [OLPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/olpc/)
