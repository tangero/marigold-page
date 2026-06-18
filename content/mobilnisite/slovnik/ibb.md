---
slug: "ibb"
url: "/mobilnisite/slovnik/ibb/"
type: "slovnik"
title: "IBB – In-band Blocking"
date: 2025-01-01
abbr: "IBB"
fullName: "In-band Blocking"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ibb/"
summary: "In-band Blocking (IBB) je požadavek na výkon přijímače, který měří schopnost zařízení přijímat požadovaný signál za přítomnosti silného nežádoucího rušivého signálu v rámci stejné provozní šířky kanál"
---

IBB je požadavek na výkon přijímače, který měří schopnost zařízení přijímat požadovaný signál, když je v rámci stejné šířky kanálu přítomen silný nežádoucí rušivý signál.

## Popis

In-band Blocking (IBB) je klíčový metrický ukazatel výkonu definovaný ve specifikacích 3GPP pro přijímače uživatelského zařízení (UE) a síťové infrastruktury, primárně v kontextu New Radio (NR). Kvantifikuje odolnost rádiového přijímače proti specifickému typu ko-kanálového rušení: silnému modulovanému blokujícímu signálu, který spadá do stejné šířky pásma nosné jako požadovaný signál. Testovací scénář zahrnuje aplikaci požadovaného signálu na úrovni referenční citlivosti a následné zavedení nežádoucího rušivého signálu („blokátoru“) na specifikovaném odstupu kmitočtu od středního kmitočtu požadovaného signálu a na mnohem vyšší úrovni výkonu. Přijímač musí za těchto podmínek udržet minimální úroveň demodulačního výkonu (např. maximální povolenou chybovost bloků).

Technické parametry pro IBB jsou detailně definovány, včetně úrovně výkonu požadovaného signálu (často na citlivost + X dB), úrovně výkonu blokátoru (pevná vysoká hodnota jako -35 dBm pro určitá pásma), kmitočtového odstupu blokátoru od středu nosné a modulace blokujícího signálu (což je typicky modulovaný LTE nebo NR signál pro simulaci reálného rušení). Požadavek zajišťuje, že komponenty vstupního obvodu přijímače, jako jsou šumově nízké zesilovače, filtry a míchače, mají dostatečnou linearitu a selektivitu, aby zabránily silnému vnitropásmovému blokátoru v desenzibilizaci přijímače nebo generování intermodulačních produktů, které by přehlušily slabší požadovaný signál.

Požadavky IBB jsou specifikovány pro každé provozní pásmo a pro různé výkonové třídy UE. Jsou základní součástí režimu testování shody (pokryté ve specifikacích jako 38.521-1), aby byla zaručena spolehlivost komerčních zařízení v nasazených sítích. Přítomnost takových blokátorů je běžná v hustých městských nasazeních, ve scénářích s agregací nosných, kde je aktivních více nosných, nebo v prostředích se sdíleným spektrem. Bez přísných požadavků IBB by propustnost UE mohla kolabovat nebo by se spojení mohlo úplně přerušit při blízkosti silného vysílače na sousedním kanálu ve stejném pásmu, což by vážně degradovalo kvalitu sítě a uživatelský zážitek.

## K čemu slouží

Účelem definování požadavků In-band Blocking je zajistit interoperabilitu a spolehlivý výkon bezdrátových zařízení za přítomnosti realistického rušení uvnitř kanálu. Jak se buněčné sítě vyvíjely s širšími šířkami pásma (např. až 100 MHz v NR), agregací nosných a složitějšími scénáři sdílení spektra, pravděpodobnost, že zařízení narazí na silný signál z blízké základnové stanice nebo jiného UE na blízkém kmitočtu ve stejném pásmu, se výrazně zvýšila. Předchozí požadavky na přijímače se často zaměřovaly na mimopásmové blokování, kde je rušič mimo provozní pásmo, ale byly méně přísné pro vnitropásmové scénáře.

IBB řeší omezení dřívějších specifikací, které mohly vést k tomu, že zařízení prošla laboratorními testy, ale selhávala v reálných síťových podmínkách. Zajišťuje, že dynamický rozsah a linearita přijímače jsou dostatečné pro zvládnutí náročného [RF](/mobilnisite/slovnik/rf/) prostředí moderních vysokokapacitních sítí. To je obzvláště klíčové pro udržení výkonnostních slibů 5G NR, zejména ve vysokofrekvenčních pásmech (jako n78, n79) a pro funkce jako dynamické sdílení spektra (DSS), kde koexistují LTE a NR signály. Standardizací těchto testů 3GPP zajišťuje základní úroveň výkonu pro všechna zařízení, což zase umožňuje síťovým operátorům nasazovat sítě s předvídatelným pokrytím a kvalitou, a v konečném důsledku chrání zážitek koncového uživatele před degradací z důvodu ko-kanálového rušení.

## Klíčové vlastnosti

- Definuje odolnost přijímače proti silným modulovaným rušičům v rámci stejné šířky kanálu
- Specifikuje testovací parametry včetně úrovně požadovaného signálu, výkonu blokátoru, kmitočtového odstupu a modulace
- Požadavky jsou specifikovány pro každé NR provozní pásmo a výkonovou třídu UE
- Integrální součást testování shody UE dle 3GPP (TS 38.521-1)
- Kritické pro výkon ve scénářích s agregací nosných a dynamickým sdílením spektra
- Zajišťuje linearitu a selektivitu přijímače za přítomnosti vnitropásmových signálů na sousedních kanálech

## Definující specifikace

- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.741** (Rel-19) — NTN L-/S-band for NR Technical Specification
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TS 38.863** (Rel-19) — NR NTN RF and Co-existence Spec
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties

---

📖 **Anglický originál a plná specifikace:** [IBB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ibb/)
