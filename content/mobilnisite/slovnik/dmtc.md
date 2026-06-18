---
slug: "dmtc"
url: "/mobilnisite/slovnik/dmtc/"
type: "slovnik"
title: "DMTC – Discovery Signal Measurement Timing Configuration"
date: 2025-01-01
abbr: "DMTC"
fullName: "Discovery Signal Measurement Timing Configuration"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dmtc/"
summary: "DMTC je periodická konfigurace časového okna poskytovaná sítí uživatelskému zařízení (UE), která definuje, kdy se má UE pokusit detekovat a měřit signály pro objevování referenčních signálů (DRS) ze s"
---

DMTC je periodická konfigurace časového okna ze sítě, která uživatelskému zařízení (UE) určuje, kdy se má pokusit detekovat a měřit signály pro objevování referenčních signálů (Discovery Reference Signals) ze sousedních buněk za účelem objevování malých buněk a mobility.

## Popis

Discovery Signal Measurement Timing Configuration (DMTC) je klíčový parametr řízený sítí v systémech 3GPP LTE a NR, který usnadňuje efektivní objevování buněk, zejména malých buněk, jako jsou femtobuňky, pikobuňky, a v nasazeních se sdíleným spektrem. Jedná se o konfigurační zprávu odesílanou obsluhující buňkou (pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/)) uživatelskému zařízení (UE), která definuje periodické časové okno – DMTC okno – během kterého by mělo UE provádět rádiová měření.

Operačně síť konfiguruje DMTC s konkrétními parametry: periodicita (např. 40 ms, 80 ms, 160 ms), délka trvání (typicky 1–6 ms) a časový posun. UE používá tuto konfiguraci k přesnému určení, kdy má naladit svůj přijímač pro vyhledání a měření signálů pro objevování referenčních signálů ([DRS](/mobilnisite/slovnik/drs/)) ze sousedních buněk. DRS je složený signál, který může v LTE zahrnovat primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)), sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)) a buněčně specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/)), nebo v NR blok synchronizačního signálu (SSB). DMTC okno je navrženo tak, aby bylo synchronizováno s periodickými okamžiky vysílání těchto DRS z potenciálních cílových buněk, zejména těch, které mohou vysílat nespojitě pro úsporu energie (např. v režimech zapnutí/vypnutí malých buněk).

V rámci nakonfigurovaného DMTC okna UE provádí úkoly jako měření síly signálu ([RSRP](/mobilnisite/slovnik/rsrp/)) a kvality ([RSRQ](/mobilnisite/slovnik/rsrq/)) na detekovaných DRS. Tato měřená data jsou následně hlášena zpět obsluhující síti, která je používá pro klíčová rozhodnutí správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)). Tato rozhodnutí zahrnují přípravu předávání hovoru, převýběr buňky a aktivaci/deaktivaci sekundárních buněk ve scénářích agregace nosných. Mechanismus DMTC je zásadní pro mobilitu v heterogenních sítích (HetNets), kde musí UE připojené k makrobuňce efektivně objevovat podkladové vrstvy malých buněk bez nepřetržitého, energeticky náročného vyhledávání.

Jeho role sahá až k energetické účinnosti sítě a koexistenci ve sdíleném spektru. Tím, že se vysílání DRS a měřicí činnost UE omezí na tato definovaná periodická okna, mohou malé buňky vypnout své vysílací obvody po většinu času, čímž drasticky sníží spotřebu energie. Dále v licenčně asistovaném přístupu (LAA) nebo NR v nelicencovaném pásmu (NR-U) DMTC pomáhá koordinovat příležitosti pro měření mezi zařízeními různých operátorů sdílejících stejné nelicencované pásmo, čímž snižuje interferenci a zlepšuje spolehlivost objevování.

## K čemu slouží

DMTC bylo zavedeno ve 3GPP Release 13, primárně v rámci rámce vylepšeného objevování malých buněk pro LTE. Hlavním problémem byla neefektivita nepřetržitého vyhledávání buněk v hustých, vícevrstvých nasazeních HetNet. Bez DMTC by muselo UE neustále vyhledávat sousední buňky na mnoha frekvencích, což by vedlo k vysoké spotřebě baterie. Kritičtější bylo, že malé buňky nasazené pro zvýšení kapacity často používaly nespojité vysílání (DTX) pro úsporu energie, což znamenalo, že jejich pilotní signály nebyly vždy přítomny. UE vyhledávající v náhodný čas by je pravděpodobně minulo.

Tato technologie problém řeší poskytnutím časového místa setkání. Síť ví, kdy sousední malé buňky (zejména ty v jejím koordinačním clusteru) budou vysílat své signály pro objevování. Tento rozvrh sdělí UE prostřednictvím konfigurace DMTC. To umožňuje UE uspávat své přijímací obvody mimo tato okna, čímž šetří baterii, a zároveň zajišťuje, že aktivně měří přesně v době, kdy jsou požadované signály přítomny. To je nezbytné pro dosažení benefitů úspory energie technik zapnutí/vypnutí malých buněk bez kompromisů v mobilitním výkonu.

Historicky bylo jeho vytvoření motivováno prací na vylepšení heterogenních sítí LTE a malých buněk a později se stalo stejně důležité pro NR, zejména pro provoz ve vysokofrekvenčních pásmech (mmWave), kde se používají beamformingové paprsky, a pro přístup ke sdílenému/nelicencovanému spektru. Řeší základní výzvu vyvážení energetické účinnosti sítě, spotřeby energie UE a robustního řízení mobility v stále složitějším a hustším rádiovém prostředí.

## Klíčové vlastnosti

- Definuje periodické měřicí okno pro objevování sousedních buněk UE
- Konfigurovatelná periodicita, délka trvání a posun prostřednictvím signalizace RRC
- Synchronizuje měřicí aktivitu UE s periodickým vysíláním DRS/SSB z buněk
- Umožňuje energeticky účinné objevování malých buněk prostřednictvím nespojitého vysílání
- Podporuje mobilitu a převýběr buňky v heterogenních sítích
- Zásadní pro provoz ve sdíleném spektru (LAA, NR-U) a s agregací nosných

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [DMTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/dmtc/)
