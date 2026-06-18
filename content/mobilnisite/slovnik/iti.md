---
slug: "iti"
url: "/mobilnisite/slovnik/iti/"
type: "slovnik"
title: "ITI – Interrupted Transmission Indication"
date: 2026-01-01
abbr: "ITI"
fullName: "Interrupted Transmission Indication"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iti/"
summary: "Mechanismus v uživatelské rovině protokolu Iu (RANAP) pro indikaci přerušení přenosu dat, typicky z důvodu procedury předání spojení nebo přemístění. Zajišťuje, aby přijímací strana (např. SGSN) byla"
---

ITI je mechanismus v uživatelské rovině protokolu Iu, který indikuje přerušení přenosu dat, typicky z důvodu předání spojení, aby informoval přijímač o možných ztrátách nebo duplikaci dat.

## Popis

Indikace přerušeného přenosu (ITI) je specifický řídicí mechanismus zabudovaný v uživatelské rovině protokolu Iu, který je součástí signalizace [RANAP](/mobilnisite/slovnik/ranap/) (Radio Access Network Application Part). Funguje na rozhraní mezi radiovým síťovým řadičem ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS a podpůrným uzlem pro [GPRS](/mobilnisite/slovnik/gprs/) ([SGSN](/mobilnisite/slovnik/sgsn/)) v jádru sítě. Primární funkcí ITI je signalizovat přerušení toku paketů uživatelských dat přes rozhraní Iu-PS (paketová doména). Toto přerušení není náhodnou poruchou, ale řízenou událostí, nejčastěji vyvolanou mobilními procedurami, jako je přemístění obslužného subsystému radiové sítě ([SRNS](/mobilnisite/slovnik/srns/)) nebo předání spojení mezi RNC. Během takových procedur je datová cesta pro uživatelské zařízení (UE) překonfigurována, což může dočasně zastavit přeposílání paketů ze zdrojového RNC do SGSN.

Technicky je ITI přenášeno pomocí specifického řídicího rámce v rámci datových jednotek protokolu uživatelské roviny Iu. Při zahájení přemístění SRNS odešle zdrojové RNC řídicí rámec ITI do SGSN. Tento rámec slouží jako značka vložená do proudu paketů uživatelských dat. Informuje SGSN, že přenos uživatelských dat z tohoto konkrétního RNC pro tento specifický kontext UE byl záměrně přerušen. SGSN po přijetí této indikace chápe, že jakékoli pakety přijaté po ITI mohou být mimo pořadí, duplikované (pokud jsou přeposlány ze staré i nové cesty), nebo že může dojít k mezeře v sekvenčních číslech dat. To umožňuje SGSN provést potřebné vnitřní úpravy, jako je správa vyrovnávací paměti nebo přealignment sekvenčních čísel, aby správně zpracovalo následný datový tok z nového RNC.

Role ITI je klíčová pro zachování integrity paketových datových služeb během mobilních událostí. Bez ní by jádrová síť mohla přerušení mylně interpretovat jako poruchu spoje nebo nesprávně zpracovat přicházející pakety, což by vedlo k potenciální ztrátě dat, chybám aplikací nebo zhoršení uživatelského zážitku. Poskytnutím této explicitní signalizace v pásmu ITI umožňuje plynulejší a předvídatelnější proces předání spojení. Je to základní prvek pro zajištění robustnosti paketových služeb, jako je prohlížení internetu nebo streamování videa, i když se uživatel pohybuje a síť přesměrovává jeho datovou cestu přes různé síťové uzly.

## K čemu slouží

ITI bylo vytvořeno k řešení specifické výzvy v sítích UMTS týkající se kontinuity paketových dat během aktivních mobilních procedur. V raných verzích 3GPP, jak se sítě vyvíjely pro podporu sofistikovanějších paketových služeb, se ukázalo, že předání spojení a přemístění mohou způsobovat narušení datového toku, která nebyla dostatečně signalizována jádrové síti. [SGSN](/mobilnisite/slovnik/sgsn/), odpovědný za správu relace UE a přeposílání dat do GGSN, potřeboval způsob, jak rozlišit mezi normálním, řízeným přerušením dat (z důvodu plánovaného předání spojení) a abnormálním přerušením způsobeným chybou (jako je porucha spoje).

Před standardizací ITI mohlo SGSN takové události pouze odvozovat z jiných signalizačních zpráv, které nemusely poskytovat přesný časový údaj ani kontext pro přerušení uživatelské roviny. Tato nejednoznačnost mohla vést k neefektivnímu zpracování, jako jsou zbytečné retransmise z vyšších vrstev nebo nesprávné sestavování datových paketů. Zavedení ITI ve verzi 8 poskytlo přímý signalizační mechanismus v pásmu na samotné uživatelské rovině. Vyřešilo problém tím, že dalo [RNC](/mobilnisite/slovnik/rnc/) standardizovaný způsob, jak explicitně notifikovat SGSN v okamžiku, kdy je přenos dat zastaven z řízeného důvodu. To umožnilo jádrové síti optimalizovat zpracování následného datového toku, čímž se zlepšila spolehlivost a výkonnost služeb paketové domény v reálném i nereálném čase během kritických mobilních událostí, a vytvořilo tak klíčovou součást celkového rámce QoS a správy mobility pro UMTS.

## Klíčové vlastnosti

- Řídicí signalizace v pásmu (in-band) v rámci protokolu uživatelské roviny Iu
- Specificky indikuje záměrné přerušení přenosu dat
- Primárně spouštěno procedurami přemístění SRNS nebo předání spojení mezi RNC
- Umožňuje SGSN spravovat sekvenci paketů a vyrovnávací paměť během mobility
- Zvyšuje spolehlivost paketových služeb během předání spojení
- Definováno v rámci sady protokolů RANAP pro rozhraní Iu-PS

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [ITI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iti/)
