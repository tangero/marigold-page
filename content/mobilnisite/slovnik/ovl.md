---
slug: "ovl"
url: "/mobilnisite/slovnik/ovl/"
type: "slovnik"
title: "OVL – Overload point"
date: 2025-01-01
abbr: "OVL"
fullName: "Overload point"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ovl/"
summary: "Parametr správy sítě používaný v GSM/UMTS sítích s přepojováním okruhů. Označuje nástup zahlcení v řadiči základnových stanic (BSC) nebo řadiči rádiové sítě (RNC) a spouští mechanismy řízení přetížení"
---

OVL je parametr správy sítě používaný v GSM/UMTS sítích s přepojováním okruhů. Označuje nástup zahlcení v BSC nebo RNC a spouští mechanismy řízení přetížení.

## Popis

Bod přetížení (OVL) je kritický prahový parametr definovaný v protokolech Base Station System Management ([BSSMAP](/mobilnisite/slovnik/bssmap/)) a Radio Access Network Application Part ([RANAP](/mobilnisite/slovnik/ranap/)) v sítích GSM a UMTS. Nachází se v řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) pro GSM nebo v řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) pro UMTS. OVL představuje konkrétní úroveň využití zdrojů (např. zátěž procesoru, využití paměti nebo objem provozu), po jejímž překročení je uzel považován za vstupující do stavu přetížení. Při překročení této prahové hodnoty BSC nebo RNC aktivuje interní procedury řízení přetížení. Tyto procedury jsou navrženy tak, aby uzel ochránily před úplným selháním selektivním odmítáním nebo omezováním nových požadavků na službu, jako jsou pokusy o sestavení hovoru nebo aktualizace polohy, a zároveň se snaží zachovat stávající spojení. OVL je proaktivním nástrojem správy; definováním bodu, kdy začíná řízení přetížení, mohou operátoři sítě vyvažovat zatížení provozem a předcházet scénáři kaskádového selhání, při kterém se uzel stane nereagujícím. Konkrétní algoritmy a monitorované zdroje závisí na implementaci, ale koncept OVL poskytuje standardizovaný rámec pro správu zahlcení.

## K čemu slouží

Bod přetížení (OVL) byl vytvořen, aby řešil kritický problém zahlcení a nestability síťových uzlů ve scénářích s vysokým provozem. V raných mobilních sítích mohlo náhlé zvýšení poptávky (např. během hromadné události nebo poruchy sítě) přetížit [BSC](/mobilnisite/slovnik/bsc/) nebo [RNC](/mobilnisite/slovnik/rnc/), což vedlo k úplnému pádu a ztrátě služby pro všechny připojené uživatele. Mechanizmus OVL poskytuje řízenou, pozvolnou degradaci služby. Řeší problém režimu selhání typu "vše nebo nic" tím, že umožňuje síťovému prvku řízeně snížit zatížení. Historický kontext je zakořeněn v principech dopravního inženýrství a správy poruch, které jsou převedeny do konkrétního parametru pro řízení v reálném čase. Řeší omezení spočívající v absenci standardizovaného spouštěče pro řízení zahlcení, což umožňuje interoperabilní a předvídatelné chování sítě při zatížení napříč zařízeními od různých výrobců.

## Klíčové vlastnosti

- Definuje prahovou hodnotu pro spuštění řízení přetížení v BSC/RNC
- Je součástí protokolů správy BSSMAP (GSM) a RANAP (UMTS)
- Umožňuje proaktivní správu zahlcení sítě
- Cílem je zabránit selhání uzlu selektivním odmítáním služeb
- Umožňuje pozvolnou degradaci služeb při vysokém zatížení
- V konkrétním sledovaném zdroji (CPU, paměť, hloubka fronty) závisí na implementaci

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [BSSMAP – Base Station Subsystem Management Application Part](/mobilnisite/slovnik/bssmap/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [OVL na 3GPP Explorer](https://3gpp-explorer.com/glossary/ovl/)
