---
slug: "zsa"
url: "/mobilnisite/slovnik/zsa/"
type: "slovnik"
title: "ZSA – Zenith angle Spread of Arrival"
date: 2025-01-01
abbr: "ZSA"
fullName: "Zenith angle Spread of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/zsa/"
summary: "ZSA je parametr kanálu, který kvantifikuje vertikální úhlovou disperzi příchozích vícecestných signálů na přijímací anténní řadu. Charakterizuje rozptylové prostředí v elevanční rovině a je klíčový pr"
---

ZSA je parametr kanálu, který kvantifikuje vertikální úhlové rozptyl příchozích vícecestných signálů, charakterizuje rozptylové prostředí v elevanční rovině a slouží k návrhu robustních přijímačů a vyhodnocování 3D beamforming.

## Popis

Zenith angle Spread of Arrival (ZSA) je statistický parametr definovaný v prostorovém modelu kanálu 3GPP pro New Radio (NR). Měří disperzi neboli rozptyl úhlů příchodu ([ZOA](/mobilnisite/slovnik/zoa/)) pro vícecestné složky dopadající na přijímací anténní řadu. ZSA v podstatě kvantifikuje, jak moc je příchozí signální energie v důsledku odrazů, difrakcí a rozptylu v šířicím prostředí rozprostřena ve vertikální (elevanční) rovině. Velká hodnota ZSA indikuje bohaté rozptylové prostředí s významnou energií přicházející ze širokého rozsahu vertikálních úhlů, zatímco malá hodnota ZSA naznačuje, že příchozí cesty jsou soustředěny kolem úzkého vertikálního směru.

Technicky je ZSA modelován pro každý shluk v geometrickém stochastickém modelu kanálu 3GPP. Každý šířicí shluk má nominální úhel příchodu (ZOA). Jednotlivé paprsky uvnitř tohoto shluku mají hodnoty ZOA, které jsou náhodně odchýleny od tohoto nominálního úhlu, a rozdělení těchto odchylek definuje ZSA shluku. To je typicky modelováno pomocí Laplacova nebo „wrapped“ Gaussova rozdělení s konkrétní hodnotou střední kvadratické ([RMS](/mobilnisite/slovnik/rms/)) šířky. RMS ZSA je klíčový vstup pro generování koeficientů kanálu v systémových simulacích, který přímo ovlivňuje korelační vlastnosti mezi anténními prvky ve vertikální dimenzi přijímací řady.

Z pohledu systémového provozu je ZSA klíčové pro výkon technik příjmu s více anténami. Na straně uživatelského zařízení (UE) poskytuje velká hodnota ZSA významnou prostorovou diverzitu ve vertikální doméně, kterou mohou využít kombinační algoritmy přijímače (např. kombinování [MMSE](/mobilnisite/slovnik/mmse/)) ke zmírnění úniků a zlepšení kvality signálu. Naopak malá hodnota ZSA znamená vysokou korelaci mezi vertikálně oddělenými anténními prvky, což může omezit zisk z diverzity, ale může usnadnit efektivnější beamforming, pokud je kanál stabilní. Pro příjem v uplinku na gNB znalost uplink ZSA (často odvozená z uplink sounding) pomáhá při návrhu optimálních přijímacích svazků, zejména pro systémy FD-MIMO.

Architektonicky je ZSA vlastnost kanálu, kterou odhadují nebo předpokládají algoritmy fyzické vrstvy. Přestože není explicitně signalizováno přes rozhraní, jeho statistické vlastnosti jsou zakotveny v normalizovaných modelech kanálu používaných pro návrh a testování. Algoritmy přijímače, zejména ty pro odhad kanálu, ekvalizaci a správu svazků, musí být robustní v očekávaném rozsahu hodnot ZSA pro různé scénáře nasazení (např. Urban Macro se středním ZSA, Indoor Hotspot s potenciálně větším ZSA). Hodnota tohoto parametru ovlivňuje návrh rozestupu anténní řady a složitost potřebného zpracování signálu k dosažení cílových výkonnostních metrik.

## K čemu slouží

ZSA bylo zavedeno spolu s [ZOD](/mobilnisite/slovnik/zod/) v 3GPP Release 14, aby doplnilo 3D charakterizaci rádiového kanálu. Předchozí standardy buněčných sítí do značné míry ignorovaly vertikální úhlový rozptyl a soustředily se pouze na azimutální rozptyl. Toto zjednodušení přestalo být platné s nasazením základnových stanic využívajících anténní řady s mnoha vertikálními prvky (Massive [MIMO](/mobilnisite/slovnik/mimo/)). Absence definovaného parametru ZSA znemožňoval přesně modelovat nebo předpovídat výkon elevančního beamforming a vertikální sektorizace v reálných rozptylových prostředích.

Jeho zavedení řeší problém nepřesné predikce výkonu pro pokročilé anténní systémy. Kvantifikací vertikální úhlové disperze umožňuje ZSA systémovým návrhářům a plánovačům sítí pochopit, jakého zisku z diverzity nebo multiplexingu lze dosáhnout v elevanční doméně. Odstraňuje tak omezení spočívající v předpokladu jediného deterministického úhlu příchodu, který by nadhodnocoval potenciální zisky úzkého vertikálního beamforming v rozptylových prostředích. Přesné modelování ZSA zajišťuje, že návrhy přijímačů základnových stanic a UE jsou testovány proti realistickým podmínkám kanálu, což vede k robustnějším produktům.

Historický kontext je spojen s tlakem na vyšší kapacitu sítě a praktickým nasazením [AAS](/mobilnisite/slovnik/aas/). Jak se sítě stávaly hustšími a antény složitějšími, pochopení prostorových charakteristik kanálu ve všech dimenzích se stalo komerční nutností. ZSA v kombinaci s [ZOA](/mobilnisite/slovnik/zoa/) poskytuje úplný obraz vertikálního profilu příchozího signálu. Tato informace je kritická pro vyhodnocení klíčových 5G technologií, jako je komunikace v mmWave pásmu (kde je beamforming zásadní) a síťové určování polohy (kde se využívá odhad úhlu příchodu), a zajišťuje, že tyto technologie spolehlivě fungují za různých šířicích podmínek.

## Klíčové vlastnosti

- Kvantifikuje RMS rozptyl úhlů příchodu signálu ve vertikální (zenith) rovině.
- Klíčový statistický parametr v 3D prostorovém modelu kanálu 3GPP (TR 38.901).
- Definován pro každý rozptylový shluk, přičemž úhly jednotlivých paprsků jsou rozděleny kolem nominálního ZOA.
- Ovlivňuje prostorovou korelaci a zisk z diverzity pro vertikálně oddělené anténní prvky.
- Nezbytné pro realistické vyhodnocení výkonu příjmu v uplinku a technik s více anténami na straně UE.
- Liší se podle scénáře nasazení (např. UMa, RMa, InH), aby odráželo různá rozptylová prostředí.

## Související pojmy

- [ZOA – Zenith angle Of Arrival](/mobilnisite/slovnik/zoa/)
- [ASA – Azimuth Spread of Arrival](/mobilnisite/slovnik/asa/)
- [AOD – Azimuth Angle of Departure](/mobilnisite/slovnik/aod/)

## Definující specifikace

- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz

---

📖 **Anglický originál a plná specifikace:** [ZSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/zsa/)
