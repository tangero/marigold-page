---
slug: "sul"
url: "/mobilnisite/slovnik/sul/"
type: "slovnik"
title: "SUL – Supplementary Uplink"
date: 2025-01-01
abbr: "SUL"
fullName: "Supplementary Uplink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sul/"
summary: "Supplementary Uplink (SUL, doplňkový uplink) je funkce 5G NR, která umožňuje zařízení používat pro uplinkový přenos další nosnou v nižším kmitočtovém pásmu vedle primární TDD nebo vysokofrekvenční FDD"
---

SUL je funkce 5G NR, která využívá další nosnou v nižším kmitočtovém pásmu pro uplinkový přenos za účelem zlepšení pokrytí a kapacity.

## Popis

Supplementary Uplink (SUL, doplňkový uplink) je technika podobná agregaci nosných, definovaná ve specifikaci 3GPP Release 15 a vylepšená v následujících vydáních pro 5G New Radio (NR). Konkrétně řeší omezení uplinku tím, že umožňuje uživatelskému zařízení (UE) využívat dvě samostatné uplinkové nosné: primární uplink (který je součástí spárovaného spektra u duplexu s frekvenčním dělením ([FDD](/mobilnisite/slovnik/fdd/)) nebo pásma s duplexem s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/))) a doplňkovou uplinkovou nosnou, typicky nasazenou v nižším kmitočtovém pásmu (např. pod 1 GHz). Downlinkový přenos probíhá pouze na primární nosné, zatímco uplink může dynamicky nebo semistaticky využívat jednu nebo obě nosné. To se liší od tradiční agregace nosných, protože SUL zahrnuje asymetrické propojení, kde je doplňková nosná pouze pro uplink.

Z architektonického hlediska je SUL konfigurován signalizací řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)). Síť poskytne UE konfigurační parametry pro nosnou SUL, včetně jejího absolutního čísla rádiového kmitočtového kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/)), šířky pásma a přidružených prostředků fyzického kanálu pro náhodný přístup ([PRACH](/mobilnisite/slovnik/prach/)). UE provádí iniciální přístup (např. náhodný přístup) na primární nebo SUL nosné na základě naměřených prahových hodnot výkonu přijímaného referenčního signálu downlinku ([RSRP](/mobilnisite/slovnik/rsrp/)). Během připojeného režimu může gNB plánovat uplinkové přenosy na SUL nosné pomocí formátů řídicích informací downlinku ([DCI](/mobilnisite/slovnik/dci/)) ve fyzickém downlinkovém řídicím kanálu ([PDCCH](/mobilnisite/slovnik/pdcch/)), přičemž nosná je indikována prostřednictvím vyhrazeného pole. Výkon UE je řízen napříč oběma nosnými s dodržováním maximálních limitů výkonu a specifických procedur řízení výkonu pro SUL.

Klíčové komponenty zahrnují plánovač gNB, který rozhoduje o výběru nosné na základě podmínek uplinkového kanálu, schopností UE a vyrovnávání zatížení. Fyzická vrstva zajišťuje samostatný odhad kanálu, modulaci a kódování pro každou uplinkovou nosnou. Transportní bloky mohou být přenášeny nezávisle na každé nosné, ačkoli některá vylepšení umožňují společné zpracování. SUL funguje v rámci specifikací 3GPP upravujících procedury fyzické vrstvy (řada 38.2xx), správu rádiových prostředků (38.3xx) a požadavky na RF (řada 38.1xx). Jeho úlohou je zlepšit uplinkovou propustnost, snížit latenci pro uplinkově náročné aplikace a rozšířit pokrytí, zejména pro TDD pásma s vysokými kmitočty (jako n78 nebo n79), kde je uplinkové pokrytí inherentně omezeno kvůli vyšším ztrátám na trase a nižšímu vysílacímu výkonu UE ve srovnání s základnovými stanicemi.

## K čemu slouží

SUL byl zaveden v 5G NR Release 15, aby řešil kritické výzvy v oblasti uplinkového pokrytí a kapacity, zejména když sítě začaly nasazovat ve středním a vysokém pásmu spektra (např. 3,5 GHz v TDD režimu). Tato vyšší pásma nabízejí velkou šířku pásma pro vysoké rychlosti downlinku, ale trpí většími ztrátami při šíření a omezeným uplinkovým pokrytím kvůli nižšímu vysílacímu výkonu UE a nepříznivému rozpočtu spojení. V hustě zastavěných městských nebo vnitřních scénářích to vede ke špatnému uplinkovému výkonu na okrajích buňky, což zhoršuje uživatelský zážitek u aplikací, jako jsou nahrávání videa, komunikace v reálném čase a přenos dat IoT.

Historicky LTE používalo agregaci nosných a doplňkový uplink v určitých kontextech, ale SUL v 5G je integrovanějším řešením. Umožňuje operátorům využít stávající aktiva v nízkém pásmu spektra (často používaná pro 4G) jako uplinkový doplněk pro 5G, optimalizovat využití spektra bez nutnosti spárovaného spektra pro samostatný provoz 5G v těchto pásmech. Tím se řeší ekonomická a technická omezení spojená s pořizováním nových, symetrických bloků spektra. Oddělením downlinkových a uplinkových nosných poskytuje SUL nákladově efektivní prostředek ke zlepšení uplinku bez kompromisů v downlinkové kapacitě nebo nutnosti plného nasazení FDD v nízkých pásmech.

Motivace vychází z potřeby vyváženého výkonu spojení v 5G, aby uplink nebyl úzkým hrdlem pro vznikající služby, jako je rozšířená realita, průmyslový IoT a síťové segmenty s přísnými požadavky na uplink. SUL umožňuje lepší podporu těchto služeb tím, že poskytuje spolehlivější a vyšší propustnost uplinkových spojení, čímž naplňuje slib 5G v podobě vylepšeného mobilního širokopásmového přístupu a ultra-spolehlivé komunikace s nízkou latencí napříč různými scénáři nasazení.

## Klíčové vlastnosti

- Provoz nosné pouze pro uplink v nízkofrekvenčních pásmech (např. pod 1 GHz)
- Dynamický nebo semistatický výběr nosné pro uplinkové přenosy na základě prahových hodnot RSRP
- Nezávislé zpracování fyzické vrstvy a plánování pro primární a SUL nosné
- Podpora iniciálního přístupu (náhodného přístupu) na primární nebo SUL nosné
- Řízení a správa výkonu napříč více uplinkovými nosnými
- Vylepšené pokrytí a kapacita pro uplink, zvláště výhodné pro nasazení v TDD vysokých pásmech

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [FDD – Frequency Division Duplexing](/mobilnisite/slovnik/fdd/)

## Definující specifikace

- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 37.716** — 3GPP TR 37.716
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.872** (Rel-15) — Technical Report on SUL & LTE-NR DC with SUL
- **TS 37.898** (Rel-19) — Rel-19 HPUE for EN-DC Band Combinations
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.104** (Rel-19) — NR Base Station RF Requirements
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.307** (Rel-19) — NR UE Release Independent Requirements
- … a dalších 15 specifikací

---

📖 **Anglický originál a plná specifikace:** [SUL na 3GPP Explorer](https://3gpp-explorer.com/glossary/sul/)
