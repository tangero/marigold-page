---
slug: "hsr"
url: "/mobilnisite/slovnik/hsr/"
type: "slovnik"
title: "HSR – Higher Symbol Rate"
date: 2025-01-01
abbr: "HSR"
fullName: "Higher Symbol Rate"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hsr/"
summary: "Evoluční funkce GSM/EDGE, která zvyšuje symbolovou rychlost na rozhraní rádiového přenosu za účelem zvýšení datové propustnosti. Přenosem více symbolů za sekundu ve stejném kanálovém pásmu HSR zvyšuje"
---

HSR je evoluční funkce GSM/EDGE, která zvyšuje symbolovou rychlost na rozhraní rádiového přenosu, aby přenesla více symbolů za sekundu, čímž zvyšuje datovou propustnost v rámci stejné šířky kanálového pásma.

## Popis

Higher Symbol Rate (HSR, vyšší symbolová rychlost) je funkce definovaná ve specifikacích 3GPP pro sítě GSM/[EDGE](/mobilnisite/slovnik/edge/), konkrétně jako součást projektu EDGE Evolution. Upravuje základní parametr fyzické vrstvy rozhraní GSM rádiového přenosu – symbolovou rychlost. Standardní GSM používá symbolovou rychlost přibližně 271 kilosymbolů za sekundu (ksps) na nosné o šířce 200 kHz. HSR tuto rychlost zvyšuje, typicky na 325 ksps nebo 407 ksps, což umožňuje přenos většího počtu datových symbolů ve stejném časovém slotu 200 kHz a ve stejné šířce kanálového pásma.

Technicky zvýšení symbolové rychlosti zkracuje dobu trvání symbolu. Aby se modulovaný tvar vlny vešel do stejné masky kanálu a nedocházelo k nadměrnému rušení sousedních kanálů, používá HSR spektrálně účinnější filtry pro tvarování impulsu. Modulace Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) používaná v základním GSM je zachována kvůli zpětné kompatibilitě v některých režimech, ale HSR je často kombinována s modulačními schématy vyššího řádu, jako jsou [QPSK](/mobilnisite/slovnik/qpsk/), [16QAM](/mobilnisite/slovnik/16qam/) a 32QAM, definovanými pro EDGE Evolution ([EGPRS2](/mobilnisite/slovnik/egprs2/)). Přijímač vyžaduje sofistikovanější ekvalizaci, aby zvládl zvýšené mezisymbolové rušení způsobené vyšší symbolovou rychlostí a z toho vyplývající časovou disperzi v mnohacestných kanálech.

Provoz HSR je definován pro downlink i uplink. Funguje ve spojení s dalšími funkcemi EDGE Evolution, jako je snížená latence díky zkrácenému Transmission Time Interval ([TTI](/mobilnisite/slovnik/tti/)) a turbokódování. Aby bylo možné HSR využít, musí jej podporovat jak mobilní stanice, tak síť. Síť může signalizovat podporu HSR a mobil může hlásit měření kvality kanálu pro kanály s HSR. Jeho úlohou bylo poskytnout významný přírůstkový výkonnostní boost sítím GSM/EDGE, vytěžit maximální možnou datovou kapacitu z existujícího spektra a infrastruktury jako nákladově efektivní alternativa nebo doplněk k nasazení 3G [HSPA](/mobilnisite/slovnik/hspa/), zejména na trzích, kde bylo spektrum GSM hojné, ale licence pro 3G nebyly k dispozici.

## K čemu slouží

HSR byl vyvinut jako klíčová součást standardu [EDGE](/mobilnisite/slovnik/edge/) Evolution, aby řešil rostoucí poptávku po vyšších datových rychlostech v sítích GSM. Před EDGE Evolution narážely datové služby GSM (GPRS, EDGE) na základní limity dané pevnou symbolovou rychlostí 271 ksps a modulací GMSK/8PSK. Operátoři, zejména ti s hlubokým pokrytím GSM, ale omezeným spektrem pro 3G, potřebovali cestu k nabídce vylepšených mobilních datových služeb bez kompletní obnovy sítě. HSR poskytlo zpětně kompatibilní evoluční cestu v rámci frameworku nosné GSM.

Řešil problém omezených špičkových datových rychlostí zvýšením hrubé propustnosti symbolů na rádiovém rozhraní. Díky nacpání více symbolů do stejného časového slotu a kombinaci tohoto přístupu s modulací vyššího řádu (EGPRS2) mohlo EDGE Evolution s HSR dosáhnout teoretických špičkových datových rychlostí několikanásobně vyšších než u staršího EDGE. To umožnilo operátorům nabízet vylepšené služby mobilního širokopásmového přístupu, jako je rychlejší prohlížení webu a streamování videa, na své stávající infrastruktuře GSM, čímž prodloužili její komerční životaschopnost a poskytli konkurenceschopnou datovou službu v oblastech, kde nebylo pokrytí 3G ještě dostupné nebo ekonomicky proveditelné k nasazení. Představovalo poslední velkou optimalizaci výkonu fyzické vrstvy GSM založené na TDMA.

## Klíčové vlastnosti

- Zvýšená symbolová rychlost (např. 325 nebo 407 ksps oproti standardním 271 ksps)
- Provoz ve standardní šířce kanálového pásma GSM 200 kHz
- Použití s pokročilou modulací (QPSK, 16QAM, 32QAM) pro EGPRS2
- Vyžaduje pokročilé tvarování impulsu a ekvalizaci přijímače
- Definováno pro přenos downlink i uplink
- Součást sady funkcí EDGE Evolution pro vyšší špičkové datové rychlosti

## Související pojmy

- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)
- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 45.860** (Rel-11) — Precoded EGPRS2 Downlink Study

---

📖 **Anglický originál a plná specifikace:** [HSR na 3GPP Explorer](https://3gpp-explorer.com/glossary/hsr/)
