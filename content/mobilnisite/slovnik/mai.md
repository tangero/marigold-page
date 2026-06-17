---
slug: "mai"
url: "/mobilnisite/slovnik/mai/"
type: "slovnik"
title: "MAI – Measurement Assistance Information"
date: 2025-01-01
abbr: "MAI"
fullName: "Measurement Assistance Information"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mai/"
summary: "Informace poskytovaná sítí mobilnímu zařízení, aby mu pomohla provádět efektivní a přesná rádiová měření na sousedních buňkách, zejména ve scénářích heterogenních sítí (HetNet) a agregace nosných. Opt"
---

MAI je informace, kterou síť poskytuje mobilnímu zařízení, aby mu pomohla provádět efektivní a přesná rádiová měření na sousedních buňkách, čímž optimalizuje výkon měření a životnost baterie.

## Popis

Measurement Assistance Information (MAI) je soubor datových prvků poskytovaných sítí uživatelskému zařízení (UE) k usnadnění a optimalizaci procesu měření pro správu rádiových zdrojů (RRM). Zavedená s UMTS a významně rozšířená v LTE a 5G NR je MAI klíčová pro provoz ve složitých síťových nasazeních, jako jsou heterogenní sítě (HetNety) s malými buňkami, a pro technologie jako agregace nosných ([CA](/mobilnisite/slovnik/ca/)) a duální konektivita ([DC](/mobilnisite/slovnik/dc/)). Síť, konkrétně [E-UTRAN](/mobilnisite/slovnik/e-utran/) (eNodeB) nebo NG-RAN (gNB), tuto informaci doručuje prostřednictvím vyhrazené signalizace [RRC](/mobilnisite/slovnik/rrc/), typicky ve zprávě RRCConnectionReconfiguration nebo v blocích systémové informace (SIB).

Obsah MAI může zahrnovat velmi specifické parametry o sousedních buňkách, které má UE měřit. To často zahrnuje detailní informace o nosné frekvenci, fyzické identifikátory buněk (PCI), konfigurace referenčních signálů buňky ([CRS](/mobilnisite/slovnik/crs/)) pro LTE nebo konfigurace bloků synchronizačních signálů (SSB) pro NR. Pro agregaci nosných může poskytovat frekvence komponentních nosných ([CC](/mobilnisite/slovnik/cc/)) a jejich přidružené šířky pásma. Klíčovým pokročilým aspektem je poskytnutí konfigurace 'měřicích mezer' (measurement gaps), která informuje UE, kdy má dočasně přerušit komunikaci s vlastní obsluhující buňkou, aby naladilo svůj přijímač na jinou frekvenci a provedlo mezifrekvenční nebo mezisystémová (inter-RAT) měření.

Díky přijetí MAI nemusí UE slepě prohledávat celé rádiové spektrum při hledání potenciálních sousedních buněk. Tento cílený přístup přináší několik hlavních výhod. Drasticky snižuje čas potřebný pro UE k identifikaci a změření kandidátských buněk pro předání spojení (handover) nebo přidání sekundární buňky, což vede k rychlejším přesunům a pružnějšímu nastavení CA/DC. Také významně snižuje spotřebu energie UE, protože přijímací obvody jsou aktivovány pro měření pouze ve stanovených časech a na známých frekvencích. Dále zlepšuje přesnost a spolehlivost měření, protože UE přesně ví, jaké signály má hledat, což je obzvláště důležité v hustých nasazeních malých buněk, kde mnoho buněk pracuje na stejné frekvenci.

## K čemu slouží

MAI byla vyvinuta k řešení rostoucí složitosti rádiových přístupových sítí přesahujících základní nasazení makrobuněk. V raném GSM/UMTS byl seznam sousedních buněk ([BA](/mobilnisite/slovnik/ba/) list apod.) relativně jednoduchý. Avšak se zavedením LTE-A, 5G a HetNetů explodoval počet potenciálních nosných frekvencí, šířek pásma a vrstev buněk (makro, mikro, piko, femto). UE provádějící slepé prohledávání tohoto rozsáhlého konfiguračního prostoru by bylo nepřijatelně pomalé, neefektivní z hlediska spotřeby energie a často nepřesné.

Primární problém, který MAI řeší, je optimalizace chování UE při měření v tomto složitém prostředí. Umožňuje síti inteligentně vést UE, říkat mu 'kam se dívat' a 'kdy se dívat'. Tím řeší dvojí problém latence měření a vybíjení baterie UE. Historicky, bez takové asistence, mohla mobilita v HetNetech trpět selháním nebo zpožděním předání spojení a nastavení [CA](/mobilnisite/slovnik/ca/) by bylo pomalejší, což by ovlivnilo propustnost pro uživatele. MAI umožňuje síti proaktivně a efektivněji spravovat rádiové zdroje a zajišťuje, že se UE připojí k nejlepší možné buňce nebo skupině buněk (v CA) na základě téměř reálné znalosti topologie a vytížení sítě, kterou sama UE nemůže mít.

## Klíčové vlastnosti

- Poskytuje cílené parametry sousedních buněk (frekvence, PCI, konfiguraci CRS/SSB) pro UE.
- Konfiguruje vzory měřicích mezer (measurement gaps) pro mezifrekvenční a mezisystémová (inter-RAT) měření.
- Nezbytná pro efektivní provoz při agregaci nosných (CA) a duální konektivitě (DC).
- Kritická pro správu mobility v hustých nasazeních heterogenních sítí (HetNet).
- Snižuje spotřebu baterie UE tím, že se vyhne slepému prohledávání celého spektra.
- Doručována prostřednictvím signalizace RRC (např. RRCConnectionReconfiguration, SIBy).

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.193** (Rel-19) — ATSSS Procedures Specification

---

📖 **Anglický originál a plná specifikace:** [MAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mai/)
