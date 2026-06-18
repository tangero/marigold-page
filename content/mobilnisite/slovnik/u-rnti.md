---
slug: "u-rnti"
url: "/mobilnisite/slovnik/u-rnti/"
type: "slovnik"
title: "U-RNTI – UTRAN Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "U-RNTI"
fullName: "UTRAN Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-rnti/"
summary: "Dočasný identifikátor přidělený UTRANem pro jednoznačnou identifikaci uživatelského zařízení (UE) v kontextu rádiové přístupové sítě, konkrétně pro komunikaci mezi UE a řadičem rádiové sítě (RNC). Je"
---

U-RNTI je dočasný identifikátor přidělený UTRANem pro jednoznačnou identifikaci uživatelského zařízení (User Equipment) v rámci rádiové přístupové sítě pro komunikaci s řadičem rádiové sítě (Radio Network Controller).

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Radio Network Temporary Identifier (U-RNTI) je základní dočasný identifikátor používaný v 3GPP UMTS sítích. Slouží jako jedinečná adresa uživatelského zařízení (UE) v rámci UTRANu, konkrétně z pohledu obsluhujícího řadiče rádiové sítě ([SRNC](/mobilnisite/slovnik/srnc/)). U-RNTI se skládá ze dvou hlavních komponent: identity obsluhujícího [RNC](/mobilnisite/slovnik/rnc/) (SRNC-ID) a dočasné identity rádiové sítě obsluhujícího RNC ([S-RNTI](/mobilnisite/slovnik/s-rnti/)). SRNC-ID jednoznačně identifikuje SRNC v síti, zatímco S-RNTI je jedinečná hodnota přidělená tímto SRNC danému UE. Tato kombinace zajišťuje globální jedinečnost v rámci celé sítě.

U-RNTI je přiděleno UE, když vstoupí do stavu CELL_[DCH](/mobilnisite/slovnik/dch/) nebo CELL_[FACH](/mobilnisite/slovnik/fach/), což indikuje aktivní spojení s vyhrazenými nebo sdílenými kanálovými prostředky. Je hojně využíváno v signalizačních zprávách mezi UE a UTRANem přes rozhraní vzduchu. Například během procedur navázání, rekonfigurace, předání spojení (handover) a aktualizace buňky v rámci řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) jsou zprávy adresovány pomocí U-RNTI k identifikaci cílového UE. Identifikátor je zahrnut v hlavičkách protokolových datových jednotek RRC.

Klíčová architektonická role U-RNTI spočívá v umožnění efektivní identifikace UE bez nutnosti spoléhat se na trvalé identifikátory, jako je [IMSI](/mobilnisite/slovnik/imsi/), čímž se zvyšuje ochrana soukromí uživatele na rádiovém rozhraní. Umožňuje také síti spravovat mobilitu. Během procedury přemístění SRNC (typu předání spojení, kdy se změní obsluhující RNC) může být U-RNTI přiděleno novým SRNC. U-RNTI zůstává platné, dokud má UE RRC spojení s UTRANem, a je uvolněno při uvolnění RRC spojení. Jeho návrh je nedílnou součástí řídicí roviny UTRANu a zajišťuje spolehlivé a adresované doručování RRC zpráv.

## K čemu slouží

U-RNTI bylo vytvořeno, aby splnilo potřebu bezpečné, efektivní a dočasné metody identifikace UE v rámci signalizačních procedur rádiové přístupové sítě. Používání trvalého identifikátoru, jako je Mezinárodní identifikace mobilního účastníka (IMSI), na rádiovém rozhraní pro častou signalizaci by představovalo významná bezpečnostní a soukromostní rizika, protože by mohl být odposlechnut a sledován. U-RNTI tento problém řeší poskytnutím dočasného aliasu, který je mimo konkrétní síťový kontext a relaci bezvýznamný.

Jeho účel sahá až k usnadnění robustního řízení mobility. Ve složité hierarchii UMTS buněk a RNC poskytuje U-RNTI konzistentní úchop pro SRNC ke správě spojení UE, když se pohybuje. Je nezbytné pro procedury, jako je tvrdé předání spojení (hard handover) a přemístění SRNC, kdy síť potřebuje jednoznačně identifikovat, které spojení UE se přenáší. Vytvoření U-RNTI, standardizovaného od Release 4, bylo klíčovou součástí definování vyspělého a škálovatelného protokolu RRC pro UMTS, které odděluje problematiku identity účastníka v jádru sítě od identity spojení na úrovni RAN.

## Klíčové vlastnosti

- Globálně jedinečný dočasný identifikátor pro UE v rámci UTRANu
- Skládá se z identity obsluhujícího RNC (SRNC-ID) a S-RNTI
- Používá se pro adresování signalizačních zpráv RRC přes rozhraní vzduchu
- Přiděluje se během navázání RRC spojení ve stavech CELL_DCH/FACH
- Zvyšuje soukromí tím, že se vyhne přenosu trvalých identit UE po rádiu
- Nezbytné pro procedury mobility, jako je předání spojení (handover) a přemístění SRNC

## Související pojmy

- [S-RNTI – Serving Radio Network Temporary Identifier](/mobilnisite/slovnik/s-rnti/)
- [C-RNTI – Cell Radio Network Temporary Identifier](/mobilnisite/slovnik/c-rnti/)
- [SRNC – Serving Radio Network Controller](/mobilnisite/slovnik/srnc/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [U-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-rnti/)
