---
slug: "acpr"
url: "/mobilnisite/slovnik/acpr/"
type: "slovnik"
title: "ACPR – Adjacent Channel Power Ratio"
date: 2025-01-01
abbr: "ACPR"
fullName: "Adjacent Channel Power Ratio"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/acpr/"
summary: "ACPR měří únik výkonu z vysílaného signálu do přilehlých frekvenčních kanálů. Kvantifikuje linearitu vysílače a spektrální růst, což je klíčové pro prevenci interference mezi sousedními kanály v mobil"
---

ACPR je poměr měřící únik výkonu z vysílaného signálu do přilehlých frekvenčních kanálů, který kvantifikuje linearitu vysílače a spektrální růst (spectral regrowth) za účelem prevence interference v mobilních sítích.

## Popis

Adjacent Channel Power Ratio (ACPR, poměr výkonu v přilehlém kanálu) je základní metrika výkonu vysílače v systémech 3GPP, která kvantifikuje množství výkonu, který přetéká z určeného kanálu vysílaného signálu do přilehlých frekvenčních kanálů. Tento jev, známý jako spektrální růst nebo spektrální únik, vzniká primárně v důsledku nelinearit ve výkonovém zesilovači (PA) vysílače a dalších RF komponentách. Když signál prochází nelineárními komponentami, vznikají intermodulační produkty, které přesahují přidělenou šířku pásma kanálu a mohou interferovat se signály v sousedních kanálech. ACPR je definován jako poměr výkonu změřeného v přilehlém (nebo alternativním) kanálu k výkonu v hlavním kanálu, typicky vyjádřený v decibelech (dB).

Metodika měření ACPR je standardizována v 3GPP specifikacích, zejména pro systémy UMTS a LTE. Měření zahrnuje filtrování vysílaného signálu pásmovou propustí se středem na přilehlém kanálu a následné porovnání tohoto výkonu s výkonem v hlavním kanálu změřeným přes identický filtr. Specifikace definují konkrétní měřicí šířky pásma odpovídající šířkám kanálů používaným v systému (např. 3,84 MHz pro UMTS, různé šířky pro LTE). Pro systémy WCDMA se ACPR často měří s odstupem ±5 MHz od nosné frekvence, což odpovídá prvnímu přilehlému kanálu, ačkoli mohou být specifikována i měření s odstupem ±10 MHz (alternativní kanál).

Výkon ACPR je kriticky závislý na linearitě vysílacího řetězce, zejména výkonového zesilovače. Vyšší linearita obvykle vyžaduje provoz PA s větším odstupem od saturace, což snižuje účinnost. To vytváří základní kompromis mezi linearitou (dobrým ACPR) a účinností výkonu, který musí konstruktéři systémů vyvážit. K technikám digitálního předkompenzování (DPD) se běžně přistupuje za účelem zlepšení ACPR při zachování rozumné účinnosti tím, že se předem kompenzují nelineární charakteristiky PA. Požadavky na ACPR se liší v závislosti na třídě základnové stanice (makro, mikro, piko, femto) a scénáři nasazení, přičemž přísnější požadavky jsou typicky aplikovány na základnové stanice s vyšším výkonem.

V plánování a nasazování sítí specifikace ACPR zajišťují, že více operátorů může sdílet spektrum ve stejné geografické oblasti bez nadměrného vzájemného rušení. Regulační orgány často zahrnují požadavky ACPR do podmínek licencování spektra, aby chránily uživatele přilehlých kanálů. U mobilních zařízení specifikace ACPR pomáhají zajistit, aby uživatelské zařízení (UE) nezpůsobovalo interferenci základnovým stanicím pracujícím na sousedních kanálech, což je obzvláště důležité v pásmech s hustým nasazením. Vývoj požadavků na ACPR napříč releasy 3GPP odráží rostoucí nároky na efektivitu spektra a potřebu podporovat složitější modulační schémata s vyššími poměry špičkového a průměrného výkonu (PAPR).

## K čemu slouží

ACPR existuje za účelem kvantifikace a řízení spektrálního růstu od vysílačů, což je nezbytné pro prevenci interference mezi přilehlými frekvenčními kanály v mobilních sítích. Jak se spektrum stává stále více vytíženým a operátoři mají přiděleny sousedící bloky frekvencí, potenciál, že vysílání jednoho operátora bude rušit druhého, se stává významným problémem. ACPR poskytuje standardizovanou metriku k zajištění, že vysílače udržují dostatečnou linearitu, aby většinu své energie udržely v rámci přiděleného pásma, což umožňuje více systémům koexistovat ve stejném frekvenčním pásmu bez vzájemného zhoršování.

Historicky, jak se mobilní systémy vyvíjely z analogových na digitální a přijímaly spektrálně efektivnější, ale méně lineární modulační schémata (jako QPSK, 16QAM, 64QAM a 256QAM), problém spektrálního růstu se stal výraznějším. Tato modulační schémata mají vyšší poměry špičkového a průměrného výkonu (PAPR), což zhoršuje nelineární zkreslení ve výkonových zesilovačích. Bez správné kontroly ACPR by byly zisky spektrální účinnosti slibované pokročilou modulací vykompenzovány potřebou větších ochranných pásem k prevenci interference. Zavedení požadavků na ACPR v 3GPP R99 řešilo tuto výzvu stanovením jasných výkonnostních měřítek pro systémy WCDMA.

Omezení předchozích přístupů k řízení interference, které se často spoléhaly na větší frekvenční ochranná pásma nebo méně účinné lineární zesilovače, motivovalo standardizaci ACPR. Přesným kvantifikováním úniku do přilehlého kanálu mohou operátoři sítí optimalizovat svá nasazení jak z hlediska výkonu, tak spektrální účinnosti. Požadavky ACPR také pohánějí inovace v návrhu RF komponent, zejména ve výkonových zesilovačích a linearizačních technikách, jako je digitální předkompenzace, což umožňuje efektivnější využití vzácných spektrálních zdrojů při zachování provozu bez interference.

## Klíčové vlastnosti

- Kvantifikuje únik výkonu do přilehlých frekvenčních kanálů
- Standardizovaná metodika měření napříč releasy 3GPP
- Klíčové pro řízení interference mezi operátory
- Určuje požadavky na linearitu výkonového zesilovače
- Podporuje sdílení spektra a koexistenci
- Měřicí šířky pásma jsou sladěny se šířkami kanálů systému

## Definující specifikace

- **TS 25.103** (R99) — RF Requirements for RRM
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD

---

📖 **Anglický originál a plná specifikace:** [ACPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/acpr/)
