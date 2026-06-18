---
slug: "qcl"
url: "/mobilnisite/slovnik/qcl/"
type: "slovnik"
title: "QCL – Quasi Co-Location"
date: 2025-01-01
abbr: "QCL"
fullName: "Quasi Co-Location"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qcl/"
summary: "Vztah mezi anténními porty, kdy si UE může předpokládat, že rozsáhlé vlastnosti kanálu (jako rozptyl doby zpoždění, Dopplerův rozptyl, průměrné zpoždění, průměrné zesílení) odhadnuté z jednoho portu l"
---

QCL je vztah mezi anténními porty, kdy si UE může předpokládat, že rozsáhlé vlastnosti kanálu odhadnuté z jednoho portu lze využít pro podporu příjmu na jiném portu.

## Popis

Quasi Co-Location (QCL) je základní koncept v 3GPP New Radio (NR), který definuje předpokládaný vztah mezi různými referenčními signálovými anténními porty nebo mezi referenčním signálovým portem a portem datového kanálu. Pokud jsou dva anténní porty nakonfigurovány jako QCL, může UE předpokládat, že určité rozsáhlé vlastnosti rádiového kanálu zjištěné na prvním portu lze odvodit a použít pro podporu příjmu signálů na druhém portu. Mezi tyto rozsáhlé vlastnosti patří parametry jako Dopplerův posuv, Dopplerův rozptyl, průměrné zpoždění, rozptyl doby zpoždění a prostorové Rx parametry (které souvisejí s přijímacím svazkem). Tento předpoklad výrazně snižuje složitost a čas potřebný pro odhad kanálu, zejména pro kanály jako Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)).

Specifikace definuje několik typů QCL (Typ A, B, C, D) v dokumentu 38.214, přičemž každý umožňuje odvodit jinou podmnožinu těchto rozsáhlých parametrů. Například Typ A zahrnuje Dopplerův posuv, Dopplerův rozptyl, průměrné zpoždění a rozptyl doby zpoždění. Typ D je obzvláště kritický pro správu svazků, protože zahrnuje prostorové Rx parametry, což znamená, že UE může předpokládat, že pro porty s QCL vztahem typu D lze použít stejný přijímací svazek. V praxi gNB konfiguruje UE pomocí stavů Transmission Configuration Indicator ([TCI](/mobilnisite/slovnik/tci/)) prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) a/nebo aktivace [MAC](/mobilnisite/slovnik/mac/) [CE](/mobilnisite/slovnik/ce/). Každý stav TCI obsahuje informace, které propojují cílový referenční signál (jako [CSI-RS](/mobilnisite/slovnik/csi-rs/) nebo blok [SS](/mobilnisite/slovnik/ss/)/[PBCH](/mobilnisite/slovnik/pbch/)) s typem QCL a zdrojovým referenčním signálem. UE pak využívá měření ze zdrojového RS k odvození odhadů kanálu pro cílové RS nebo PDSCH.

Z architektonického hlediska je QCL nezbytné pro efektivní přenos s formováním svazku, zejména ve frekvenčním rozsahu 2 (FR2 – mmWave). Kvůli vysokým ztrátám na dráze při těchto frekvencích komunikace závisí na úzkých svazcích s vysokým ziskem. QCL Typ D umožňuje gNB indikovat, že PDSCH je vysílán pomocí stejného svazku (a tedy podobných prostorových charakteristik) jako dříve změřený CSI-RS nebo SSB. UE pak může použít stejné váhy pro formování přijímacího svazku, čímž se vyhne vyčerpávajícímu hledání svazku pro každý přenos. To je řízeno prostřednictvím postupů správy svazků (P-1, P-2, P-3) a je úzce integrováno s řídicí signalizací pro plánovací povolení (kde je stav TCI indikován v DCI).

## K čemu slouží

QCL bylo zavedeno v NR (Rel-15) k řešení významných výzev odhadu kanálu a správy svazků v pokročilých MIMO a milimetrových vlnových systémech, které nebyly dostatečně pokryty rámcem quasi co-location anténních portů v LTE. V LTE byly QCL předpoklady jednodušší a pro mnoho portů implicitní, ale využití masivního formování svazků, širších šířek pásma a vyšších frekvencí v NR vytvořilo scénář, kdy charakteristiky kanálu pro různé referenční signály mohly být značně odlišné, zejména pokud byly vysílány z různých analogových svazků nebo různých TRP (Transmission Reception Points). Bez explicitních QCL vztahů by musela UE provádět nezávislý, složitý odhad kanálu pro každý signál, což by zvyšovalo latenci, spotřebu energie a snižovalo spolehlivost.

Hlavní problém, který QCL řeší, je umožnění efektivního zpracování v přijímači UE v dynamickém prostředí s formováním svazků. Umožňuje síti explicitně informovat UE o tom, které referenční signály jsou si „podobné“ z hlediska statistik kanálu, takže UE může znovu použít předchozí měření. To je klíčové pro dosažení nízké latence při přepínání a sledování svazků, což je zásadní pro udržení konektivity pro mobilní uživatele v mmWave pásmech, kde jsou svazky úzké. Také usnadňuje pokročilé operace s více TRP a koordinovaný multipoint (CoMP) tím, že umožňuje síti definovat vztahy mezi signály z různých geografických bodů, čímž poskytuje flexibilní rámec pro správu prostorové diverzity a zisků multiplexování v 5G sítích.

## Klíčové vlastnosti

- Definuje předpokládané vztahy mezi anténními porty pro rozsáhlé vlastnosti kanálu
- Podporuje více typů QCL (A, B, C, D) pro různé podmnožiny parametrů
- Umožněno konfigurací stavů TCI prostřednictvím signalizace RRC a MAC CE
- Klíčové pro správu svazků, zejména QCL Typ D pro prostorové Rx parametry
- Snižuje složitost odhadu kanálu a latenci v UE
- Usnadňuje operace s více TRP a agregaci nosných

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.106** (Rel-19) — NR Repeater Radio Transmission and Reception
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.831** (Rel-16) — UE RF Requirements for FR2 Enhancements
- **TR 38.833** (Rel-17) — NR Demodulation Performance Enhancement
- **TR 38.878** (Rel-18) — Technical Report on Advanced Receiver for MU-MIMO

---

📖 **Anglický originál a plná specifikace:** [QCL na 3GPP Explorer](https://3gpp-explorer.com/glossary/qcl/)
