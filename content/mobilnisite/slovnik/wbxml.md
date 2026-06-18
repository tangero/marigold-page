---
slug: "wbxml"
url: "/mobilnisite/slovnik/wbxml/"
type: "slovnik"
title: "WBXML – WAP Binary XML"
date: 2025-01-01
abbr: "WBXML"
fullName: "WAP Binary XML"
category: "Protocol"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/wbxml/"
summary: "WBXML je kompaktní binární reprezentace XML, standardizovaná WAP Fórem a přijatá organizací 3GPP. Je navržena pro efektivní kódování XML dokumentů pro přenos přes bezdrátové sítě s omezenou přenosovou"
---

WBXML je kompaktní binární reprezentace XML standardizovaná pro efektivní kódování XML dokumentů s cílem snížit velikost přenášených dat a režii parsování při přenosu přes bezdrátové sítě s omezenou přenosovou kapacitou v mobilních službách 3GPP.

## Popis

WBXML ([WAP](/mobilnisite/slovnik/wap/) Binary [XML](/mobilnisite/slovnik/xml/)) je protokol pro binární formátování, který kóduje XML dokumenty do kompaktního proudového zápisu bajtů. Vyvinulo jej WAP Fórum, aby vyřešilo neefektivitu přenosu rozvláčného textového XML přes pomalá a nákladná bezdrátová spojení. Protokol funguje na principu tokenizace struktury XML: značky a názvy atributů jsou nahrazeny předdefinovanými binárními kódy z kódového prostoru specifického pro daný dokument, zatímco tabulky řetězců zpracovávají opakující se řetězce, aby se zabránilo jejich opakování. Zakódovaný dokument se skládá z bajtu s verzí, veřejného identifikátoru typu dokumentu, tabulky řetězců a tokenizovaného těla. Tato binární reprezentace výrazně snižuje velikost zprávy ve srovnání s textovým XML protějškem, což vede k rychlejšímu přenosu a nižším nárokům na zpracování na mobilních zařízeních s omezenými prostředky.

Architektonicky je WBXML protokol prezentační vrstvy, který se nachází nad transportní vrstvou (často [WSP](/mobilnisite/slovnik/wsp/) nebo [HTTP](/mobilnisite/slovnik/http/)) a pod aplikační logikou. Klíčovou součástí je kódový prostor definovaný v Document Type Definition ([DTD](/mobilnisite/slovnik/dtd/)), který mapuje XML značky a atributy na specifické jednobajtové tokeny. Protokol podporuje více stránek tokenů pro rozšiřitelnost, což umožňuje efektivní kódování různých XML slovníků. Tabulka řetězců, umístěná na začátku WBXML proudu, obsahuje literální řetězce použité v dokumentu (jako hodnoty atributů nebo textový obsah), které nejsou tokenizovány, a jsou na ně později odkazováno přes indexové ukazatele.

Během provozu enkodér parsuje XML dokument, nahradí známé značky a atributy odpovídajícími tokeny, přidá neznámé řetězce do tabulky řetězců a vytvoří sekvenční proud bajtů. Dekodér tento proces obrátí a použije stejný kódový prostor k rekonstrukci původní XML struktury. WBXML podporuje kompresi obsahu a může indikovat použité znakové kódování. V rámci sítí 3GPP je primárně specifikováno v TS 23.057 pro služby Mobile Station Application Execution Environment (MExE), což umožňuje doručování kompaktních strukturovaných dat pro aplikace jako poskytování služeb, konfigurace nebo odlehčené prohlížení v prostředí WAP.

## K čemu slouží

WBXML bylo vytvořeno, aby umožnilo efektivní využití datových formátů založených na [XML](/mobilnisite/slovnik/xml/) v éře raného mobilního internetu, charakterizované výrazným omezením přenosové kapacity, vysokou latencí a omezeným výpočetním výkonem zařízení. [WAP](/mobilnisite/slovnik/wap/) Fórum, jehož cílem bylo přinést webové služby na mobilní telefony, potřebovalo způsob přenosu strukturovaných dat bez režie rozvláčného textového XML, které bylo přes pomalá okruhově přepínaná datová spojení nepraktické. WBXML tento problém vyřešilo poskytnutím kompaktního binárního kódování, které zkrátilo dobu přenosu, snížilo náklady na rádiové rozhraní a snížilo složitost parsování a nároky na paměť na zařízeních.

Tato technologie řešila omezení přenosu prostého XML, který spotřebovával nadměrné množství bajtů na opakující se značky a bílé znaky. Tokenizací běžných prvků a použitím sdílené tabulky řetězců dokázalo WBXML často snížit velikost dokumentu o 50–80 %, což učinilo interaktivní služby realizovatelnými. Jeho přijetí do standardů 3GPP, počínaje Release 10 pro MExE, poskytlo standardizovanou metodu pro správu zařízení a poskytování služeb, což zajistilo interoperabilitu napříč sítěmi a telefony. WBXML usnadnilo nasazení mobilních datových služeb před rozšířením vysokorychlostních paketových sítí a výkonných smartphonů.

## Klíčové vlastnosti

- Binární tokenizace XML značek a atributů pro kompaktní reprezentaci
- Mechanismus tabulky řetězců pro zabránění opakování literálních řetězců
- Podpora více kódových stránek pro kódování různých XML slovníků
- Indikace veřejného identifikátoru dokumentu a znakového kódování
- Možnost vložených řetězcových dat a neprůhledných aplikačně specifických dat
- Proudové kódování vhodné pro sekvenční přenos a parsování

## Související pojmy

- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)
- [WSP – Web Service Provider](/mobilnisite/slovnik/wsp/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WBXML na 3GPP Explorer](https://3gpp-explorer.com/glossary/wbxml/)
