---
slug: "lsp"
url: "/mobilnisite/slovnik/lsp/"
type: "slovnik"
title: "LSP – Link Selector Parameter"
date: 2025-01-01
abbr: "LSP"
fullName: "Link Selector Parameter"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lsp/"
summary: "Parametr používaný v GSM/EDGE Radio Access Network (GERAN) pro adaptaci spoje a řízení výkonu. Pomáhá síti a mobilnímu zařízení vybrat optimální schéma kanálového kódování a vysílací výkon na základě"
---

LSP je parametr používaný v síti GERAN pro adaptaci spoje a řízení výkonu, který slouží k výběru optimálního schématu kanálového kódování a vysílacího výkonu na základě rádiových podmínek.

## Popis

Parametr pro výběr spoje (Link Selector [Parameter](/mobilnisite/slovnik/parameter/), LSP) je základním řídicím mechanismem v architektuře GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), který je speciálně navržen pro optimalizaci přenosu dat přes rádiové rozhraní. Funguje v rámci vrstvy správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)), kde síť průběžně sleduje ukazatele kvality kanálu, jako je síla přijímaného signálu ([RSSI](/mobilnisite/slovnik/rssi/)) a míra chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)). Na základě těchto měření síť vypočítá odpovídající hodnotu LSP. Tato hodnota je následně signalizována mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) a použita k určení nejvhodnějšího schématu modulace a kódování ([MCS](/mobilnisite/slovnik/mcs/)) pro probíhající přenos dat. Například při dobrých rádiových podmínkách může vyšší hodnota LSP odpovídat efektivnější modulaci vyššího řádu, jako je 8-PSK, s méně robustním kanálovým kódováním, čímž se maximalizuje propustnost. Naopak při špatných podmínkách LSP aktivuje přechod na robustnější schéma, jako je GMSK se silnější korekcí chyb, což zajišťuje integritu dat na úkor hrubé rychlosti.

Z architektonického hlediska LSP spravuje řadič základnové stanice (BSC) v síti GERAN. BSC shromažďuje hlášení o měřeních jak od mobilní stanice, tak od základnové přenosové stanice (BTS). Pomocí algoritmů definovaných v příslušných specifikacích 3GPP BSC vypočítá hodnotu LSP. Tento parametr je následně přenášen k MS prostřednictvím signalizačních zpráv vrstvy 3 na pomalém přidruženém řídicím kanálu (SACCH) během vyhrazeného spojení. Fyzická vrstva mobilní stanice přijatý LSP použije k odpovídající konfiguraci svého vysílače a přijímače, čímž vybere předdefinovanou kombinaci typu modulace, kódové rychlosti a implicitně i požadované úrovně vysílacího výkonu. Tento uzavřený regulační okruh je kontinuální a umožňuje dynamickou adaptaci na útlum, interference a pohyb uživatele.

Role LSP je klíčová pro dosažení slibovaných přenosových rychlostí technologie Enhanced Data rates for GSM Evolution (EDGE). Je to zásadní prvek pro funkci přírůstkové redundance (typu Hybrid ARQ), kde LSP ovlivňuje výběr počátečního kódování datového bloku. Díky jemnému ladění procesu adaptace spoje LSP přímo ovlivňuje klíčové ukazatele výkonnosti, jako je propustnost uživatele, míra chybovosti bloků (BLER) a celková kapacita sítě. Jeho správná funkce zajišťuje efektivní využití rádiových zdrojů a poskytuje nejlepší možnou datovou službu v rámci omezení okamžitého rádiového prostředí, což je základním principem moderních celulárních systémů.

## K čemu slouží

Parametr pro výběr spoje (LSP) byl zaveden, aby řešil problém efektivního přenosu paketově orientovaných dat přes inherentně proměnlivý a šumový GSM rádiový kanál. Původní GSM síť primárně obsluhovala okruhově orientovaný hlas, který používal konstantní robustní modulaci (GMSK). Se zavedením vysokorychlostních okruhově orientovaných dat (HSCSD) a později GPRS a EDGE pro paketová data byl zapotřebí dynamičtější přístup. Statická konfigurace spoje by vedla buď k plýtvání kapacitou za dobrých podmínek, nebo k vysoké chybovosti za špatných podmínek. LSP byl vytvořen jako standardizovaný řídicí parametr pro umožnění dynamické adaptace spoje.

Jeho vznik byl motivován potřebou maximalizovat spektrální účinnost – množství přenesených dat na jednotku šířky pásma – což je pro operátory vzácný a drahý zdroj. Tím, že umožňuje síti nařídit mobilní stanici, aby v reálném čase přepínala mezi různými schématy modulace a kódování (MCS-1 až MCS-9 v EDGE), LSP zajišťuje, že je pro aktuální kvalitu kanálu použita nejvyšší možná datová rychlost. Tím se řeší problém buď nadměrné rezervy (použití příliš robustního schématu, plýtvání kapacitou), nebo nedostatečné rezervy (použití příliš agresivního schématu, vedoucího k opakovaným přenosům a zpožděním).

Historicky poskytl potřebnou detailní kontrolu k realizaci výkonnostních zisků EDGE oproti základnímu GPRS. Bez takového parametru by pokročilá 8-PSK modulace EDGE byla nepoužitelná v oblastech s okrajovým pokrytím. LSP byl tedy klíčovou technologickou součástí, která umožnila GSM sítím vyvinout se v konkurenceschopné platformy pro mobilní data ještě před rozsáhlým nasazením 3G sítí UMTS.

## Klíčové vlastnosti

- Dynamický výběr schématu modulace a kódování (MCS) na základě měření rádiových podmínek v reálném čase.
- Uzavřený regulační okruh řízený řadičem základnové stanice (BSC) a prováděný mobilní stanicí (MS).
- Umožňuje efektivní využití modulačních schémat EDGE (GMSK a 8-PSK).
- Nedílná součást algoritmů řízení výkonu pro datové kanály.
- Podporuje přírůstkovou redundanci (IR) definováním počátečního kódování pro datový blok.
- Signalizován přes pomalý přidružený řídicí kanál (SACCH) během vyhrazených spojení.

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 23.802** (Rel-7) — Enhanced End-to-End QoS Architecture
- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.092** (Rel-19) — AMR Comfort Noise for SCR Operation
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec
- **TS 46.062** (Rel-19) — GSM EFR DTX Comfort Noise Specification
- **TS 48.016** (Rel-19) — Gb Interface Network Service Specification

---

📖 **Anglický originál a plná specifikace:** [LSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsp/)
