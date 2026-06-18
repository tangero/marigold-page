---
slug: "lfe"
url: "/mobilnisite/slovnik/lfe/"
type: "slovnik"
title: "LFE – Low Frequency Enhancement"
date: 2025-01-01
abbr: "LFE"
fullName: "Low Frequency Enhancement"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lfe/"
summary: "Soubor funkcí a specifikací 3GPP navržených ke zlepšení výkonu a efektivity provozu 5G New Radio (NR) v nízkofrekvenčních pásmech (např. pod 1 GHz). Zaměřuje se na zvýšení pokrytí, kapacity a podpory"
---

LFE je soubor funkcí 3GPP navržených ke zlepšení výkonu 5G NR v nízkofrekvenčních pásmech, které zvyšují pokrytí, kapacitu a podporu pro hromadný IoT a kritické komunikace.

## Popis

Low Frequency Enhancement (LFE) označuje soubor technických vylepšení standardizovaných v 3GPP, primárně od Release 15, která optimalizují 5G New Radio (NR) pro provoz ve frekvenčních pásmech pod 1 GHz (např. 600 MHz, 700 MHz, 800 MHz, 900 MHz). Tato pásma, často označovaná jako Sub-1 GHz nebo nízká pásma, jsou ceněna pro své vynikající šířicí charakteristiky, které nabízejí širší pokrytí a lepší průnik budovami ve srovnání se středními a vysokými pásmy. Nasazení 5G NR v těchto pásmech však přináší specifické výzvy, které LFE řeší, včetně užších dostupných šířek pásma, koexistence se stávajícími službami 4G LTE ve stejném pásmu (často prostřednictvím Dynamic Spectrum Sharing - DSS) a potřeby podpory širokého spektra služeb od enhanced Mobile Broadband (eMBB) až po massive Machine-Type Communications (mMTC).

Z architektonického hlediska LFE zahrnuje úpravy a optimalizace napříč protokolovou sadou 5G NR. Na fyzické vrstvě zahrnuje definici specifických numerologií (rozestupů podnosných) a přenosových šířek pásma vhodných pro typicky menší souvislé alokace šířky pásma v nízkých pásmech (např. 5, 10, 15, 20 MHz). Vylepšuje referenční signály, jako je Tracking Reference Signal ([TRS](/mobilnisite/slovnik/trs/)) a Channel State Information Reference Signal ([CSI-RS](/mobilnisite/slovnik/csi-rs/)), aby se zlepšilo odhadování kanálu a správa paprsků ve scénářích, kde je zisk beamformingu více omezen kvůli menšímu počtu anténních prvků, které se vejdou do dané fyzické velikosti při nižších frekvencích. Mechanizmy plánování a alokace zdrojů jsou optimalizovány pro efektivitu v užších šířkách pásma.

Klíčovým aspektem LFE je zajištění efektivní koexistence a synergie s LTE. Toho je dosaženo vylepšeními DSS, která umožňují NR a LTE dynamicky sdílet stejný nosič v nízkém pásmu. LFE také zahrnuje funkce pro zlepšení pokrytí řídicích kanálů a vysílacích signálů, což je klíčové pro poskytnutí robustního zážitku na okraji buňky a podporu služeb jako multicast/broadcast. Dále specifikace LFE zahrnují vylepšení pro úsporu energie, zejména pro IoT zařízení, a zlepšený výkon pro scénáře vysokorychlostních vlaků, kde Dopplerův posun, i když méně závažný než na vyšších frekvencích, stále vyžaduje správu. Úlohou LFE je zajistit, aby byly výhody pokrytí nízkopásmového spektra plně realizovány v 5G, což přináší konzistentní uživatelský zážitek a umožňuje nákladově efektivní nasazení v širokých oblastech.

## K čemu slouží

LFE bylo vytvořeno, aby řešilo specifické technické a ekonomické výzvy nasazení vysokovýkonných 5G sítí ve velmi hodnotném, ale omezeném nízkofrekvenčním spektru. Zatímco střední a vysoká pásma spektra (např. 3,5 GHz, mmWave) poskytují masivní šířky pásma potřebné pro špičkové rychlosti 5G, jejich omezené pokrytí vyžaduje hustou a nákladnou síť základnových stanic. Nízkofrekvenční spektrum je nezbytné pro poskytnutí všudypřítomného pokrytí, zejména ve venkovských a příměstských oblastech, a pro hluboký průnik do budov. Pouhé převedení stávajícího nízkopásmového spektra 4G LTE na 5G NR však bylo neefektivní, protože rané specifikace NR byly optimalizovány pro větší šířky pásma.

Primární problém, který LFE řeší, je maximalizace výkonu a kapacity 5G v rámci úzkých šířek pásma typických pro nízkopásmové alokace. Bez vylepšení by 5G NR v 10 MHz kanálu nenabízelo výraznou výhodu oproti 4G LTE ve stejné šířce pásma, což by učinilo upgrade neodůvodnitelným. LFE zavádí optimalizace na fyzické vrstvě a vyšších vrstvách, které z těchto úzkých kanálů vytěží více kapacity a lepší spektrální účinnost. To činí nasazení 5G v nízkých pásmech konkurenceschopným a připraveným na budoucnost.

Další klíčovou motivací bylo usnadnění plynulého přechodu z LTE na NR prostřednictvím Dynamic Spectrum Sharing. Operátoři potřebovali způsob, jak během migračního období provozovat současně 4G i 5G ve svém nízkopásmovém spektru, aniž by obětovali výkon pro kteroukoli skupinu uživatelů. LFE poskytuje nezbytná vylepšení pro efektivní fungování DSS v těchto pásmech. Nakonec LFE podporuje vizi 5G propojit vše tím, že zajišťuje, aby nízkopásmový NR mohl efektivně podporovat nasazení hromadného IoT a kritické komunikace, které jsou závislé na širokém pokrytí a spolehlivém připojení, a tím odemyká plný společenský a ekonomický potenciál 5G ve všech geografických oblastech.

## Klíčové vlastnosti

- Optimalizace pro provoz NR v šířkách pásma <= 20 MHz pod 1 GHz
- Vylepšené referenční signály (např. TRS, CSI-RS) pro lepší odhad kanálu
- Podpora efektivního Dynamic Spectrum Sharing (DSS) s LTE
- Vylepšení pokrytí pro řídicí kanály a vysílací signály
- Funkce pro úsporu energie přizpůsobené pro IoT zařízení na nízkopásmovém NR
- Zlepšený výkon ve scénářích vysokorychlostní mobility

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [LFE na 3GPP Explorer](https://3gpp-explorer.com/glossary/lfe/)
