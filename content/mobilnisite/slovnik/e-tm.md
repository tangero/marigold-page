---
slug: "e-tm"
url: "/mobilnisite/slovnik/e-tm/"
type: "slovnik"
title: "E-TM – E-UTRA Test Model"
date: 2025-01-01
abbr: "E-TM"
fullName: "E-UTRA Test Model"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-tm/"
summary: "Sada standardizovaných referenčních signálů a průběhů definovaných pro konformní testování rádiových kmitočtových (RF) a výkonnostních charakteristik uživatelských zařízení (UE) a základnových stanic"
---

E-TM je sada standardizovaných referenčních signálů a průběhů používaných pro konformní testování rádiových kmitočtových a výkonnostních charakteristik uživatelských zařízení LTE a základnových stanic.

## Popis

[E-UTRA](/mobilnisite/slovnik/e-utra/) Test Models (E-TM) jsou souborem předdefinovaných konfigurací signálů fyzické vrstvy pro downlink specifikovaných v 3GPP TS 36.141 (testování základnových stanic) a TS 36.143 (testování UE). Nepoužívají se v komerčním provozu sítě, ale jsou klíčovými nástroji pro laboratorní testování, typové schvalování a certifikaci shody. E-TM definuje specifickou kombinaci fyzických kanálů a signálů pro vytvoření deterministického testovacího průběhu. To typicky zahrnuje specifické alokace pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)) s definovanou modulací (např. [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/), [64QAM](/mobilnisite/slovnik/64qam/), 256QAM), kódovacím poměrem a alokací zdrojových bloků. Zahrnuje také standardní Cell-Specific Reference Signals ([CRS](/mobilnisite/slovnik/crs/)), synchronizační signály ([PSS](/mobilnisite/slovnik/pss/)/[SSS](/mobilnisite/slovnik/sss/)) a řídicí kanály (PDCCH/EPDCCH) nakonfigurované známým způsobem. Modely jsou navrženy tak, aby zatěžovaly specifické aspekty testovaného zařízení. Například E-TM1.1 může definovat plnou alokaci zdrojových bloků s QPSK pro test maximálního výkonu, zatímco E-TM3.1 může definovat signál 64QAM na vysoké úrovni výkonu pro testování EVM vysílače a spektrálních emisí. Pro testování přijímače tester základnové stanice generuje přesný E-TM průběh a výkonnostní metriky UE, jako je propustnost, chybovost bloků (BLER) nebo citlivost, se měří vůči očekávaným hodnotám. Modely pokrývají různá šířky pásma, přenosové režimy (např. TM2, TM3) a scénáře, aby zajistily komplexní testování RF parametrů, jako je výstupní výkon, regulace výkonu, kvalita vysílaného signálu, nežádoucí emise a citlivost přijímače.

## K čemu slouží

E-UTRA Test Models byly vytvořeny za účelem poskytnutí jednotné, jednoznačné a reprodukovatelné metodologie pro testování zařízení LTE vůči přísným požadavkům na RF výkonnost stanoveným 3GPP. Před standardizací mohli výrobci a testovací laboratoře používat proprietární testovací signály, což vedlo k nekonzistentním výsledkům a obtížím při certifikaci shody zařízení. E-TM tento problém řeší poskytnutím společné reference. Jejich účel je trojí: Za prvé, umožnit konzistentní a spravedlivé konformní testování pro regulační schvalování (např. GCF, PTCRB). Za druhé, poskytnout spolehlivý etalon pro testování ve výzkumu a vývoji a pro ověřování během vývoje produktu, což inženýrům umožňuje izolovat a měřit specifické RF nedostatky. Za třetí, definovat absolutní limity výkonu (např. maximální povolená velikost chybového vektoru nebo výkon úniku do sousedního kanálu), které komerční produkt nesmí překročit. Řeší složitost flexibilní OFDMA zdrojové mřížky LTE tím, že pro testovací účely poskytují její specifické, plně definované instance. To zajišťuje, že všechny strany – výrobci čipových sad, výrobci zařízení, operátoři sítí a certifikační orgány – testují vůči naprosto stejnému podnětu, což garantuje interoperabilitu a výkon sítě.

## Klíčové vlastnosti

- Standardizované referenční průběhy pro konformní testování RF pro LTE.
- Definovány pro testování základnových stanic (eNB) i uživatelských zařízení (UE).
- Pokrývají více šířek pásma, přenosových režimů a modulačních schémat.
- Používají se k ověření charakteristik vysílače (např. EVM, ACLR, výstupní výkon).
- Používají se k ověření charakteristik přijímače (např. citlivost, propustnost, BLER).
- Poskytují deterministický a reprodukovatelný podnět pro laboratorní měření.

## Související pojmy

- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [EVM – Error Vector Magnitude](/mobilnisite/slovnik/evm/)
- [ACLR – Adjacent Channel Leakage Power Ratio](/mobilnisite/slovnik/aclr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing

---

📖 **Anglický originál a plná specifikace:** [E-TM na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-tm/)
