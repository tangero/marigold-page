---
slug: "noffs-ul"
url: "/mobilnisite/slovnik/noffs-ul/"
type: "slovnik"
title: "NOffs-UL – Uplink Frequency Offset"
date: 2025-01-01
abbr: "NOffs-UL"
fullName: "Uplink Frequency Offset"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/noffs-ul/"
summary: "Parametr používaný pro výpočet kmitočtu nosné pro uplink (EARFCN) v LTE a NR. Zajišťuje přesné kmitočtové zarování mezi vysíláním UE a příjmem uplinku základnové stanice, což je klíčové pro udržení kv"
---

NOffs-UL je parametr používaný pro výpočet kmitočtu nosné pro uplink v LTE a NR, který zajišťuje přesné kmitočtové zarování mezi UE a její základnovou stanicí.

## Popis

NOffs-UL je technická hodnota offsetu definovaná v rámci specifikací 3GPP pro LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Je základní součástí vzorce používaného pro odvození Absolutního čísla rádiového kmitočtového kanálu ([EARFCN](/mobilnisite/slovnik/earfcn/)) pro uplink. EARFCN je jedinečný identifikátor, který se mapuje na konkrétní kmitočet nosné v rádiovém spektru. Výpočet zahrnuje základní vzorec, který zohledňuje duplexní režim ([FDD](/mobilnisite/slovnik/fdd/) nebo [TDD](/mobilnisite/slovnik/tdd/)) a používané kmitočtové pásmo. NOffs-UL je přidán jako korekční faktor v rámci tohoto vzorce pro přesné určení středního kmitočtu pro vysílání uplinku z uživatelského zařízení (UE) k eNodeB (v LTE) nebo gNB (v NR). Tím je zajištěno, že UE vysílá na přesném kmitočtu očekávaném sítí, což je zásadní pro správnou demodulaci a dekódování signálu uplinku.

Hodnota parametru není libovolná; je definována pro každé kmitočtové pásmo v příslušných technických specifikacích 3GPP (TS), jako je TS 36.101 pro rádiové vysílání a příjem LTE UE. Specifikace tabelují příslušnou hodnotu NOffs-UL pro každé provozní pásmo. Tato definice specifická pro pásmo zohledňuje jedinečné spektrální charakteristiky a regulační přidělení různých kmitočtových rozsahů po celém světě. Síť vysílá systémové informace, včetně EARFCN pro downlink a indikátoru pásma. UE, které zná svá podporovaná pásma a odpovídající hodnoty NOffs-UL ze svých specifikací shody (např. TS 36.521 pro testování [RF](/mobilnisite/slovnik/rf/) shody LTE), pak může autonomně vypočítat správný kmitočet uplinku pro počáteční přístup a následnou komunikaci.

Jeho role přesahuje počáteční přístup a zahrnuje probíhající mobilitu a scénáře agregace nosných. Při předávání spojení nebo při konfiguraci s více komponentními nosnými musí UE rychle a přesně naladit svůj vysílač na nové kmitočty. Předdefinovaný parametr NOffs-UL umožňuje deterministický a standardizovaný výpočet kmitočtu, čímž snižuje riziko nesprávného zarování uplinku, které by mohlo vést k přerušeným hovorům, snížené datové propustnosti nebo emisím mimo pásmo způsobujícím rušení sousedních kanálů. Při plánování a optimalizaci sítě inženýři používají tyto vzorce, které zahrnují NOffs-UL, k mapování logických čísel kanálů na fyzické kmitočty, čímž zajišťují, že rádiové parametry nasazené sítě jsou správně zarovnány s licencí na spektrum.

## K čemu slouží

NOffs-UL byl zaveden, aby poskytl standardizovanou a jednoznačnou metodu pro výpočet kmitočtů nosných pro uplink z jejich odpovídajících čísel kanálů. Před takovými přesnými definicemi mohl být výpočet kmitočtu nejednoznačný nebo závislý na implementaci, což vedlo k problémům s interoperabilitou mezi UE a síťovým zařízením od různých výrobců. Hlavní problém, který řeší, je zajištění spektrální přesnosti a regulační shody. Bezdrátové spektrum je přísně regulovaný zdroj a vysílání musí probíhat v přesně definovaných kanálech, aby nedocházelo k rušení jiných služeb, včetně jiných mobilních operátorů, satelitní komunikace nebo leteckých systémů.

Vznik NOffs-UL byl motivován rostoucí složitostí LTE a rozšířením kmitočtových pásem po celém světě. Jak 3GPP definovalo desítky nových pásem pro LTE, aby umožnilo globální roaming a efektivní využití spektra, se stal jednoduchý lineární vzorec pro výpočet kmitočtu nedostatečný. Různá pásma mají různé duplexní mezery a počáteční body v prostoru číslování kmitočtů. NOffs-UL jako součást výpočetního vzorce po částech nebo založeného na offsetu poskytuje potřebnou flexibilitu pro mapování souvislého rozsahu hodnot [EARFCN](/mobilnisite/slovnik/earfcn/) na někdy nesouvislé a pro pásmo specifické rozsahy kmitočtů uplinku definované [ITU](/mobilnisite/slovnik/itu/) a regionálními regulátory. Řeší tak omezení univerzálního výpočtu a umožňuje jedinému elegantnímu specifikačnímu rámci podporovat širokou škálu globálních kmitočtových nasazení.

## Klíčové vlastnosti

- Hodnota offsetu specifická pro pásmo, definovaná ve specifikacích 3GPP
- Integrální součást výpočetního vzorce pro EARFCN uplinku (N_UL): F_UL = F_UL_low + 0.1*(N_UL - NOffs-UL)
- Zajišťuje přesné kmitočtové zarování vysílače UE s očekáváními sítě
- Klíčové pro testování RF shody a certifikaci UE
- Podporuje duplexní režimy FDD i TDD
- Umožňuje správný provoz ve všech kmitočtových pásmech LTE a NR definovaných 3GPP

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TS 25.116** (Rel-19) — LCR TDD Repeater RF Characteristics
- **TS 25.153** (Rel-19) — LCR TDD Repeater RF Requirements & Testing
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.106** (Rel-19) — E-UTRA FDD Repeater RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.143** (Rel-19) — E-UTRA FDD Repeater RF Testing
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TR 38.892** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [NOffs-UL na 3GPP Explorer](https://3gpp-explorer.com/glossary/noffs-ul/)
