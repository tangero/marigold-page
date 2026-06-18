---
slug: "al-sdu"
url: "/mobilnisite/slovnik/al-sdu/"
type: "slovnik"
title: "AL-SDU – Application Layer - Service Data Unit"
date: 2025-01-01
abbr: "AL-SDU"
fullName: "Application Layer - Service Data Unit"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/al-sdu/"
summary: "Application Layer - Service Data Unit (AL-SDU) je datová jednotka vyměňovaná mezi aplikační vrstvou a podpůrnou transportní vrstvou v multimediálních službách založených na IMS. Představuje kompletní"
---

AL-SDU je kompletní datová náplň (payload) aplikace vyměňovaná mezi aplikační a transportní vrstvou v IMS multimediálních službách; představuje data před segmentací nebo po znovusložení.

## Popis

Application Layer - Service Data Unit (AL-SDU) je základní koncept v architektuře IP Multimedia Subsystem (IMS) dle 3GPP, konkrétně definovaný v rámci Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)) ve specifikaci TS 26.114. Představuje kompletní, nesegmentovanou datovou jednotku, kterou aplikační vrstva hodně vysílat nebo kterou přijala ze sítě. AL-SDU obsahuje skutečný multimediální obsah – například zakódované audio rámce, video rámce nebo textová data – spolu s případnými hlavičkami aplikační vrstvy potřebnými pro správné zpracování na přijímací straně.

V protokolovém zásobníku existuje AL-SDU na rozhraní mezi aplikační a transportní vrstvou. Když aplikace generuje multimediální data, vytvoří AL-SDU, který zahrnuje mediální náplň a potřebné řídicí informace specifické pro aplikaci. Tento AL-SDU je následně předán transportní vrstvě, která jej může segmentovat na menší pakety (Transport SDUs) pro přenos po síti. Naopak na přijímací straně transportní vrstva znovuskládá příchozí pakety do kompletních AL-SDU před jejich předáním aplikační vrstvě pro dekódování a prezentaci.

Velikost a struktura AL-SDU se liší v závislosti na typu média a charakteristikách kodeku. Například ve Voice over LTE (VoLTE) typicky odpovídá jeden AL-SDU jednomu zakódovanému řečovému rámci (např. 20 ms audia pomocí kodeku [AMR-WB](/mobilnisite/slovnik/amr-wb/)), zatímco ve videotelefonii může představovat video rámec nebo jeho část. Koncept AL-SDU umožňuje aplikační vrstvě udržovat povědomí o logických hranicích dat, což je klíčové pro mechanismy synchronizace, maskování chyb a adaptace kvality. Toto povědomí umožňuje přijímači správně rekonstruovat časovou osu média a efektivně řešit ztrátu paketů nebo kolísání zpoždění.

Z pohledu sítě jsou AL-SDU důležité pro správu kvality služby (QoS) a optimalizaci rádiových zdrojů. Charakteristiky velikosti a časování AL-SDU ovlivňují, jak síť přiděluje zdroje a aplikuje algoritmy plánování paketů. V systémech LTE a 5G znalost hranic AL-SDU pomáhá vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)) implementovat vhodné strategie komprese hlaviček a segmentace, zatímco vrstva Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) může optimalizovat svou segmentaci na základě velikostí AL-SDU, aby minimalizovala režii a zlepšila spektrální účinnost.

Koncept AL-SDU také hraje klíčovou roli v monitorování a optimalizaci výkonu end-to-end. Sledováním statistik doručování AL-SDU – jako je poměr doručení, zpoždění a kolísání zpoždění – mohou operátoři a poskytovatelé služeb vyhodnocovat skutečný uživatelský zážitek, nikoli pouze metriky na úrovni sítě. Tento uživatelsky orientovaný pohled umožňuje přesnější řešení problémů a optimalizaci multimediálních služeb napříč heterogenními sítěmi.

## K čemu slouží

Koncept AL-SDU byl zaveden, aby řešil základní výzvu zachování sémantiky aplikační vrstvy napříč paketově přepínanými sítěmi v architektuře IMS dle 3GPP. Před IMS a LTE si okruhově přepínané hlasové služby udržovaly jasné hranice mezi řečovými rámci prostřednictvím vyhrazených časových slotů, ale paketové multimediální služby potřebovaly způsob, jak tyto logické hranice zachovat, a zároveň těžit ze statistického multiplexování a efektivního využití zdrojů.

V tradičních IP sítích aplikace jednoduše odesílaly data jako proudy paketů bez explicitních značek pro logické datové jednotky, což přijímačům ztěžovalo správnou rekonstrukci časové osy média a aplikaci technik maskování chyb. AL-SDU poskytuje tuto zásadní informaci o hranicích, což umožňuje přijímající aplikaci přesně vědět, kde jedna mediální jednotka končí a další začíná, což je obzvláště důležité pro časově citlivé aplikace, jako je hlasová a videokomunikace.

Vytvoření konceptu AL-SDU bylo motivováno potřebou optimalizovat využití rádiových zdrojů při zachování vysoce kvalitního multimediálního zážitku. Díky tomu, že je aplikační vrstvě známo, kde jsou hranice logických datových jednotek, může systém implementovat efektivnější algoritmy segmentace, prioritizace a plánování. To síťovým prvkům umožňuje činit inteligentní rozhodnutí o tom, jak zacházet s různými typy mediálních dat, což vede k lepšímu využití vzácných rádiových zdrojů a zlepšené kvalitě zážitku pro koncové uživatele.

## Klíčové vlastnosti

- Představuje kompletní datové jednotky aplikace před segmentací nebo po znovusložení
- Udržuje logické hranice mezi mediálními rámci pro správnou rekonstrukci časové osy
- Umožňuje správu kvality služby (QoS) a optimalizaci zdrojů s ohledem na aplikaci
- Podporuje efektivní strategie komprese hlaviček a segmentace ve vrstvách PDCP a RLC
- Usnadňuje přesné monitorování výkonu end-to-end a hodnocení uživatelského zážitku
- Poskytuje základ pro mechanismy synchronizace a maskování chyb v multimediálních aplikacích

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling

---

📖 **Anglický originál a plná specifikace:** [AL-SDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/al-sdu/)
