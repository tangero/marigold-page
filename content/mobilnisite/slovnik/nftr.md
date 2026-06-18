---
slug: "nftr"
url: "/mobilnisite/slovnik/nftr/"
type: "slovnik"
title: "NFTR – Near Field Test Range"
date: 2025-01-01
abbr: "NFTR"
fullName: "Near Field Test Range"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nftr/"
summary: "Specifický typ zařízení pro měření antén navržený pro transformace z blízkého pole do dalekého pole (NFTF). Jedná se o řízené prostředí, typicky anechoickou komoru, vybavenou přesnými robotickými polo"
---

NFTR je řízené zařízení pro měření antén, například anechoická komora, které zachycuje data o záření v blízkém poli za účelem odvození charakteristik v dalekém poli pomocí transformace z blízkého pole do dalekého pole (NFTF).

## Popis

Měřící pracoviště v blízkém poli (NFTR) je fyzická implementace a infrastruktura potřebná k provádění měření pro transformaci z blízkého pole do dalekého pole ([NFTF](/mobilnisite/slovnik/nftf/)). Jde o specializované zkušební zařízení, téměř vždy anechoickou komoru, konstruovanou tak, aby poskytovala prostředí bez odrazů pro přesná elektromagnetická měření. Hlavní funkcí NFTR je mechanické skenování měřicí sondy (známé, kalibrované antény) po přesně definované ploše obklopující testovanou anténu (AUT). Během tohoto skenování vektorový analyzátor sítí ([VNA](/mobilnisite/slovnik/vna/)) měří komplexní koeficient přenosu (S21) mezi sondou a AUT v tisících diskrétních bodů, zachycující jak amplitudu, tak fázi vyzařovaného pole v oblasti blízkého pole.

Architektura NFTR je postavena kolem několika klíčových podsystémů. Za prvé, samotná anechoická komora je vyložená materiálem pohlcujícím rádiové vlny ([RAM](/mobilnisite/slovnik/ram/)) pro minimalizaci odrazů a simulaci podmínek volného prostoru. Za druhé, vysoce přesný robotický polohovací systém pohybuje sondou po zvolené skenovací ploše (např. rovině, válci nebo kouli). Přesnost polohování je kritická, protože chyby se přímo přenášejí do nepřesností v transformovaném vyzařovacím diagramu dalekého pole. Za třetí, vysokofrekvenční měřicí systém, založený na VNA, poskytuje budicí signál pro AUT a měří odezvu na sondě. Nakonec, specializovaný software řídí celý proces – koordinuje polohovač, získává data z VNA a provádí výpočetně náročné algoritmy transformace NFTF.

Princip činnosti zahrnuje kalibrovanou měřicí sekvenci. Systém je nejprve kalibrován, aby se odstranily vlivy kabelů, konektorů a vlastní odezvy sondy. AUT je poté umístěna a sonda je skenována přes předdefinovanou mřížku. Naměřená data blízkého pole představují vzorkování vyzařovaného pole na této ploše. Pomocí transformačních algoritmů specifických pro geometrii skenování jsou tato prostorová data převedena na úhlové spektrum rovinných vln, což je matematická reprezentace vyzařovacího diagramu dalekého pole. NFTR, jak je definováno ve specifikacích 3GPP jako TS 37.941, poskytuje standardizované a reprodukovatelné prostředí pro provádění těchto měření, což zajišťuje, že výkonnostní testy pro základnové stanice a UE jsou konzistentní a srovnatelné napříč různými laboratořemi a výrobci.

## K čemu slouží

NFTR existuje, aby poskytlo praktické, přesné a standardizované laboratorní řešení pro testování výkonu antén a [OTA](/mobilnisite/slovnik/ota/), což se stalo nezbytností s rostoucí složitostí anténních systémů 4G a 5G. Před jeho formalizací bylo testování antén méně standardizované a často se spoléhalo na měřicí pracoviště v dalekém poli nebo jednodušší metody, které nedokázaly adekvátně charakterizovat beamforming a prostorové vlastnosti víceanténních systémů. Mezi omezení pracovišť v dalekém poli patří jejich obrovské prostorové nároky a zranitelnost vůči rušení prostředím (počasí, okolní [RF](/mobilnisite/slovnik/rf/) šum).

Vytvoření a standardizace konceptu NFTR v rámci 3GPP byly motivovány přechodem průmyslu k aktivním anténním systémům ([AAS](/mobilnisite/slovnik/aas/)) a integrovaným rádiím. U těchto zařízení je anténa neoddělitelná od rádiového vysílače/přijímače, což znemožňuje tradiční testování vedením přes porty. NFTR tento problém řeší tím, že umožňuje skutečné testování vzduchem (OTA) v řízeném prostředí. Řeší problém s prostorem tím, že zmenšuje potřebnou měřicí vzdálenost ze stovek metrů na pouhých několik metrů, což umožňuje umístit testování do budovy. Dále poskytuje přesnost a reprodukovatelnost potřebnou k ověření přísných výkonnostních metrik 3GPP pro vyzařovaný výkon, citlivost a směrování svazku, které jsou zásadní pro zajištění kvality sítě a interoperability mezi dodavateli.

## Klíčové vlastnosti

- Skládá se z anechoické komory vyložené materiálem pohlcujícím RF záření pro minimalizaci odrazů
- Integruje vysoce přesné robotické polohovací systémy pro rovinné, válcové nebo kulové skenování
- Používá vektorový analyzátor sítí (VNA) pro přesná měření komplexních S-parametrů (amplituda a fáze)
- Využívá kalibrační techniky k odstranění vlivů sondy a měřicího systému
- Spouští specializovaný software pro řízení hardwaru, sběr dat a provádění transformací NFTF
- Poskytuje řízené, reprodukovatelné prostředí pro standardizované OTA testy shody

## Definující specifikace

- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements

---

📖 **Anglický originál a plná specifikace:** [NFTR na 3GPP Explorer](https://3gpp-explorer.com/glossary/nftr/)
