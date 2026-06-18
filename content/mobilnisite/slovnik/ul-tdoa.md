---
slug: "ul-tdoa"
url: "/mobilnisite/slovnik/ul-tdoa/"
type: "slovnik"
title: "UL-TDOA – Uplink Time Difference of Arrival"
date: 2025-01-01
abbr: "UL-TDOA"
fullName: "Uplink Time Difference of Arrival"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul-tdoa/"
summary: "Metoda určení polohy realizovaná na straně síťové infrastruktury, při níž více přijímačů Location Management Function (LMF), typicky na různých gNB, měří čas příchodu známého uplinkového signálu z UE."
---

UL-TDOA je metoda určení polohy realizovaná na straně síťové infrastruktury, při níž se k výpočtu polohy zařízení využívají časové rozdíly příchodu uplinkového signálu UE na více přijímacích bodů.

## Popis

Uplink Time Difference of Arrival (UL-TDOA) je síťově orientovaná technika určení polohy standardizovaná v 3GPP pro 5G NR a LTE-M/NB-IoT. Na rozdíl od metod využívající downlink, jako je Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), kde UE měří signály z více základnových stanic, v UL-TDOA je měření realizováno na straně síťové infrastruktury. Cílové UE je instruováno síťovou infrastrukturou (pomocí Location Management Function - [LMF](/mobilnisite/slovnik/lmf/)) k vysílání specifického referenčního signálu pro určení polohy, Uplink Positioning Reference Signal (UL-PRS) v NR nebo podobného sondážního signálu (například [SRS](/mobilnisite/slovnik/srs/) nakonfigurovaného pro určení polohy).

Více přijímacích bodů, což může být obsluhující gNB a několik sousedních gNB, zachytí tento uplinkový přenos. Každý přijímací bod, synchronizovaný na společný časový referenční zdroj (například [GPS](/mobilnisite/slovnik/gps/) nebo síťovou synchronizaci), přesně časově označí příchod signálu. Základním měřením je Time of Arrival ([TOA](/mobilnisite/slovnik/toa/)). LMF, který shromažďuje tyto TOA měření ze všech participujících přijímačů, pak vypočítá Time Difference of Arrival (TDOA) mezi páry přijímačů. Každé měření TDOA definuje hyperbolickou linii (nebo plochu ve 3D), na kterém se UE musí nacházet, protože rozdíl vzdálenosti ke dvěma přijímačům je konstantní (rychlost světla * TDOA).

Kombinací měření TDOA ze alespoň tří přijímačů (což vede ke dvěma nezávislým TDOA párům) může LMF vypočítat 2D polohu UE pomocí hyperbolické trilaterace. Pro určení 3D polohy jsou potřebná měření ze čtyř nebo více přijímačů. Přesnost UL-TDOA kriticky závisí na přesnosti synchronizace mezi přijímacími body, na šířce pásma vysílaného signálu (která ovlivňuje časovou rozlišovací schopnost), na geometrii přijímačů vůči UE (Dilution of Precision - DOP) a na schopnosti přesně detekovat první příchozí cestu signálu v prostředí s mnoha cestami. Pro zlepšení přesnosti a spolehlivosti se používají pokročilé techniky, jako multilaterace a kombinace dat s jinými metodami (například Assisted [GNSS](/mobilnisite/slovnik/gnss/), downlink TDOA).

## K čemu slouží

UL-TDOA byla vyvinuta pro splnění striktních regulatorních a komerčních požadavků na přesné určení polohy zařízení v 5G sítích, zejména pro služby tísňového volání (E911/E112), sledování majetku a IoT aplikace. I když jsou metody využívající downlink, jako [OTDOA](/mobilnisite/slovnik/otdoa/), rozšířené, mají omezení, obzvláště pro zařízení s omezenými přijímacími schopnostmi (například nízkonákladové IoT moduly) nebo v prostředích, kde jsou downlinkové signály slabé.

Primární motivací pro UL-TDOA je přesunout komplexnost přesného měření signálu z zařízení na síťovou infrastrukturu. To je výhodné z několika důvodů. Za prvé umožňuje určení polohy zařízení, které nemá sofistikované měřící schopnosti nebo je v energeticky úsporných módech, kde časté měření downlinkových signálů není možné. Zařízení pouze potřebuje vyslat jeden nakonfigurovaný signál. Za druhé, síťové přijímače (gNB) typicky mají lepší synchronizaci (pomocí [GNSS](/mobilnisite/slovnik/gnss/) nebo přesných síťových časových protokolů), stabilnější hodiny a pokročilejší schopnosti zpracování signálu než UE, což může vést k přesnějšímu a spolehlivějšímu časovému měření.

Navíc UL-TDOA doplňuje jiné metody určení polohy, aby poskytla redundanci a zvýšenou dostupnost. Ve scénářích jako indoor nebo husté městské prostředí, kde jsou signály satelitů (GNSS) nedostupné, může UL-TDOA poskytnout záložní nebo hybridní řešení. Také řeší use case, kdy síť potřebuje lokalizovat zařízení bez jeho aktivní spolupráce mimo vyslání požadovaného signálu, což může být relevantní pro bezpečnostní nebo síťové managementové účely. Jeho zavádění v Rel-16 bylo částí širšího rámce 5G určení polohy zaměřeného na dosažení přesnosti na úrovni metrů nebo dokonce submeterů, aby podpořilo nové aplikace vertikálních průmyslových segmentů.

## Klíčové vlastnosti

- Určení polohy realizované na straně síťové infrastruktury, snižující komplexnost a spotřebu energie UE
- Využívá Uplink Positioning Reference Signal (UL-PRS) nebo nakonfigurovaný SRS jako sondážní signál
- Vyžaduje přesnou časovou synchronizaci mezi všemi participujícími přijímacími gNB/přijímači LMF
- Výpočet polohy prováděn centrálně Location Management Function (LMF)
- Podporuje 2D a 3D určení polohy pomocí hyperbolické trilaterace
- Může být kombinována s jinými metodami (DL-TDOA, A-GNSS) v hybridním určení polohy pro zvýšení přesnosti

## Související pojmy

- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.855** (Rel-16) — Study on NR Positioning Support
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [UL-TDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul-tdoa/)
