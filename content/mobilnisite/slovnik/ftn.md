---
slug: "ftn"
url: "/mobilnisite/slovnik/ftn/"
type: "slovnik"
title: "FTN – Forwarded To Number"
date: 2025-01-01
abbr: "FTN"
fullName: "Forwarded To Number"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ftn/"
summary: "Parametr používaný v doplňkových službách přesměrování hovorů v sítích GSM/UMTS. Uchovává telefonní číslo, na které je hovor přesměrován při splnění podmínky přesměrování (např. obsazeno nebo bez odpo"
---

FTN je parametr v rámci služeb přesměrování hovorů GSM/UMTS, který uchovává telefonní číslo, na které je hovor přesměrován, když je splněna konkrétní podmínka, například že účastník je nedostupný.

## Popis

Forwarded To Number (FTN, číslo pro přesměrování) je klíčový datový prvek v rámci Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a Visited Mobile Switching Center ([VMSC](/mobilnisite/slovnik/vmsc/)) nebo Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) pro sítě GSM a UMTS. Je součástí dat doplňkové služby přesměrování hovorů uložených v HLR pro každého účastníka. Když účastník aktivuje službu přesměrování hovorů (jako Call Forwarding Unconditional ([CFU](/mobilnisite/slovnik/cfu/)), Call Forwarding on Mobile subscriber Busy ([CFB](/mobilnisite/slovnik/cfb/)), Call Forwarding on No Reply (CFNRy) nebo Call Forwarding on Not Reachable (CFNRc)), síť uloží určené FTN poskytnuté účastníkem. Toto číslo je cílem přesměrovaného hovoru.

Operačně, když dorazí příchozí hovor pro účastníka a je aktivní a splněna podmínka přesměrování, [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/) (Gateway MSC) dotazuje HLR na servisní data účastníka. HLR vrátí příslušné FTN asociované s aktivní podmínkou přesměrování. MSC nebo GMSC poté použije toto FTN k dalšímu směrování hovoru. FTN může být Mobile Station International Subscriber Directory Number (MSISDN), pevné linky nebo servisní číslo. Jeho uložení a správa jsou definovány v servisním profilu účastníka.

Role FTN přesahuje jednoduché přesměrování; je nedílnou součástí interakce služeb a logiky přednosti. Například, pokud je aktivních více služeb přesměrování, síťová logika určí, které FTN použít na základě stavu účastníka a definované přednosti služeb. FTN je přenášeno mezi síťovými uzly pomocí protokolů Mobile Application Part (MAP), konkrétně v operacích jako InsertSubscriberData a ProvideRoamingNumber. Jeho přesné zřízení a získávání v reálném čase jsou nezbytné pro bezproblémové dokončení hovoru a konzistentní uživatelský zážitek za různých síťových podmínek a stavů účastníka.

## K čemu slouží

FTN bylo vytvořeno pro umožnění základních funkcí přesměrování hovorů, což je základní telefonní služba očekávaná mobilními uživateli. Řeší problém zmeškaných hovorů, když je účastník nedostupný, obsazený nebo se rozhodne přesměrovat hovory na jiné číslo, například na hlasovou schránku nebo jiný telefon. Před existencí takových služeb by hovor prostě nebyl dokončen, pokud by volaný neodpověděl, což omezovalo užitečnost a spolehlivost mobilní telefonie.

Jeho zavedení v GSM Release 99 formalizovalo standardizovanou, na síti centrickou metodu pro ukládání a provádění logiky přesměrování hovorů. To byl významný pokrok oproti dřívějším primitivnějším přepojovacím řešením, protože umožnilo, aby logika přesměrování a cílové číslo byly součástí přenosného profilu účastníka uloženého v HLR. To umožnilo konzistentní poskytování služby i když účastník roamoval v různých sítích nebo byl obsluhován různými MSC. Parametr FTN poskytl potřebný datový prvek, aby se řízení hovorů kontrolované účastníkem stalo realitou, a vytvořil tak základ pro sadu služeb dokončování hovorů a osobní mobility.

## Klíčové vlastnosti

- Ukládá se jako součást dat služeb účastníka v HLR
- Asociováno s konkrétními podmínkami přesměrování hovorů (CFU, CFB, CFNRy, CFNRc)
- Může být jakékoliv platné cílové číslo (MSISDN, PSTN, servisní číslo)
- Přenášeno prostřednictvím protokolů MAP mezi HLR, MSC a GMSC
- Podléhá pravidlům interakce služeb a přednosti
- Nezbytné pro implementaci služeb hlasové schránky a přesměrování hovorů

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [FTN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ftn/)
