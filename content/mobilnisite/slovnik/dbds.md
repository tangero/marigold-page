---
slug: "dbds"
url: "/mobilnisite/slovnik/dbds/"
type: "slovnik"
title: "DBDS – Differential BDS"
date: 2025-01-01
abbr: "DBDS"
fullName: "Differential BDS"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dbds/"
summary: "Differential BDS (DBDS) je funkce 3GPP pro sítě UMTS, která vylepšuje lokalizační služby poskytováním diferenciálních korekcí službě Broadcast Domain Service (BDS). Zvyšuje přesnost a spolehlivost urč"
---

DBDS je funkce 3GPP pro sítě UMTS, která vylepšuje lokalizační služby tím, že poskytuje diferenciální korekce službě Broadcast Domain Service (BDS) za účelem zvýšení přesnosti a spolehlivosti určování polohy.

## Popis

Differential [BDS](/mobilnisite/slovnik/bds/) (DBDS) je standardizovaný mechanismus v architektuře 3GPP UMTS ([UTRAN](/mobilnisite/slovnik/utran/)) navržený k rozšíření služby Broadcast Domain Service (BDS). Samotná BDS je služba, která vysílá pomocná data, jako jsou efemeridy satelitů a časové informace, k uživatelskému zařízení (UE) pro podporu satelitního určování polohy (např. pomocí [GPS](/mobilnisite/slovnik/gps/) nebo jiných globálních navigačních satelitních systémů – [GNSS](/mobilnisite/slovnik/gnss/)). DBDS funguje tak, že poskytuje diferenciální korekce k těmto vysílaným datům. Tyto korekce zohledňují společné chyby ovlivňující signály GNSS v konkrétní geografické oblasti, jako jsou ionosférická zpoždění, chyby satelitních hodin a nepřesnosti efemerid. Aplikací těchto korekcí může UE výrazně zlepšit přesnost své vypočítané polohy, a to ze standardní přesnosti samostatného GNSS na úroveň diferenciálního GNSS ([DGNSS](/mobilnisite/slovnik/dgnss/)).

Architektura DBDS zahrnuje několik síťových prvků definovaných v odkazovaných specifikacích (25.331, 25.423, 25.433, 25.453). Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) nebo podobný lokalizační server generuje data diferenciálních korekcí na základě měření ze sítě referenčních přijímačů s přesně známou polohou. Tato data jsou poté formátována a doručována prostřednictvím UTRAN. Konkrétně Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) přijímá informace DBDS přes rozhraní Iupc (podle 25.453) od SMLC. RNC následně spravuje vysílání těchto dat přes rozhraní vzduch k UE ve své buňce nebo konkrétní servisní oblasti. Vysílání se obvykle provádí pomocí System Information Blocks ([SIB](/mobilnisite/slovnik/sib/)) na BCCH (Broadcast Control Channel), jak je podrobně popsáno ve specifikaci protokolu Radio Resource Control (RRC) (25.331).

Z pohledu UE musí zařízení podporovat funkci DBDS. Přijímá standardní pomocná data BDS spolu s diferenciálními korekcemi DBDS. Polohovací modul UE poté kombinuje vlastní nezpracovaná satelitní měření s vysílanými korekcemi, aby vypočítal přesnější polohový fix. Proces je transparentní pro aplikace vyšších vrstev, které jednoduše obdrží přesnější odhad polohy. DBDS je síťově asistovaná metoda určování polohy, což znamená, že snižuje výpočetní zátěž a čas do prvního fixu na UE ve srovnání s autonomními metodami, a zároveň zlepšuje přesnost nad rámec toho, co může poskytnout samostatný asistovaný GNSS (A-GNSS). Jeho role je nedílnou součástí plnění požadavků 3GPP na vysokou přesnost určování polohy, zejména pro regulatorní služby jako Enhanced 911 (E911) a komerční služby založené na poloze (LBS).

## K čemu slouží

DBDS byl zaveden, aby řešil rostoucí poptávku po přesném a spolehlivém určování polohy v rámci mobilních sítí, zejména pro UMTS. Před jeho zavedením standardní Assisted-GNSS (A-GNSS) poskytoval zlepšení v čase do prvního fixu a citlivosti, ale stále byl omezen inherentními chybami samostatného GNSS, jako jsou atmosférická zpoždění a chyby satelitní dráhy/hodin. Tato omezení vedla k přesnosti určování polohy typicky v řádu několika metrů až desítek metrů, což bylo nedostatečné pro nově vznikající aplikace, jako je navigace, sledování majetku a přesné služby založené na poloze pro účtování, stejně jako pro splnění přísnějších požadavků nouzových služeb (E911).

Hlavní motivací pro DBDS bylo přinést výhody diferenciálního GNSS (DGNSS), což je dobře zavedená technika v geodézii a letectví, do oblasti mobilních sítí bez nutnosti vyhrazeného komunikačního spojení ke každému UE. Vysíláním korekcí přes stávající buněčné vysílací kanály umožňuje DBDS neomezenému počtu UE v oblasti pokrytí současný přístup k vysoce přesným korekcím. Tím byly vyřešeny problémy škálovatelnosti a nákladů spojené s bodově-bodovým doručováním korekčních dat. Umožnilo to síťovým operátorům nabízet hodnotově přidanou službu vysoce přesného určování polohy jako součást jejich schopností základní sítě, čímž obohatili svou servisní nabídku a pomohli splnit vyvíjející se požadavky na přesnost polohy pro nouzová volání.

## Klíčové vlastnosti

- Vysílá diferenciální GNSS korekce (např. pro GPS) přes rozhraní vzduch UMTS
- Pro doručování dat využívá System Information Blocks (SIB) na BCCH
- Definovaná rozhraní mezi RNC a SMLC (Iupc) pro přenos korekčních dat
- Významně zlepšuje přesnost určování polohy ve srovnání se standardním A-GNSS
- Síťově asistovaný přístup snižuje výpočetní zátěž a spotřebu energie UE
- Škálovatelné řešení obsluhující současně všechna UE ve vysílací oblasti pokrytí

## Související pojmy

- [BDS – BeiDou Navigation Satellite System](/mobilnisite/slovnik/bds/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.453** (Rel-19) — PCAP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DBDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbds/)
