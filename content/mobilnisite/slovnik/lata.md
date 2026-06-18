---
slug: "lata"
url: "/mobilnisite/slovnik/lata/"
type: "slovnik"
title: "LATA – Local Access and Transport Area"
date: 2025-01-01
abbr: "LATA"
fullName: "Local Access and Transport Area"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lata/"
summary: "Geografická oblast definovaná v rámci Severoamerického číslovacího plánu (NANP) pro regulační a administrativní účely v telekomunikacích. Vymezuje hranice pro poskytování místních služeb a propojení m"
---

LATA je severoamerický regulační okrsek vymezující hranice pro místní služby při směrování hovorů a fakturaci mezi telekomunikačními operátory.

## Popis

Local Access and Transport Area (LATA) je koncept převzatý z regulačního rámce telekomunikací v USA a odkazuje se na něj ve specifikacích 3GPP, zejména v kontextu roamingu mezi veřejnými pozemními mobilními sítěmi (inter-PLMN) a směrování hovorů. LATA definuje geografický region, v jehož rámci může místní telefonní operátor (LEC) poskytovat služby. Hlavní architektonický význam v systémech 3GPP se týká způsobu směrování hovorů a datových relací, když uživatelé roamují mimo svou domovskou síť, zvláště v Severní Americe.

V rámci jádra sítě, konkrétně v domovském registračním centru ([HLR](/mobilnisite/slovnik/hlr/)) a bránovém ústředně [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)), mohou být informace o LATA použity jako součást profilu účastníka nebo analýzy směrování. Při směrování mobilně ukončeného hovoru může GMSC použít aktuální polohu volaného účastníka (získanou z návštěvnického registračního centra - [VLR](/mobilnisite/slovnik/vlr/)) k určení, zda se jedná o hovor v rámci LATA (intra-LATA), nebo mezi LATA (inter-LATA). Toto rozlišení může ovlivnit výběr tranzitních linek a zapojení meziměstských operátorů (IXC). Protokol Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) může přenášet identifikátory související s LATA obsluhující sítě.

Klíčovými komponentami, které pracují s koncepty LATA, jsou HLR (ukládající servisní profily účastníků), GMSC (provádějící směrování hovorů) a fakturační systémy. Jeho role se méně týká rádiové technologie a více administrativního směrování, vyúčtování mezi operátory a dodržování regulatorních požadavků. Zajišťuje, že hovory jsou správně kategorizovány pro aplikaci tarifů a že smlouvy o propojení mezi místními a dálkovými operátory jsou řádně dodržovány, a to i v mobilním prostředí.

## K čemu slouží

LATA byl původně zaveden ve Spojených státech po rozdělení společnosti AT&T za účelem oddělení místních telefonních služeb od služeb dálkového spojení. Jeho cílem bylo vytvořit jasné regulatorní hranice. V kontextu 3GPP byl začleněn, aby podpořil mobilní sítě fungující v regionech (jako je Severní Amerika), kde takové regulační konstrukty existují, a zajistil, že sítě GSM/UMTS mohou bezproblémově spolupracovat s regulovaným prostředím pevných sítí.

Problém, který řeší, je potřeba správného administrativního a fakturačního zacházení s hovory na základě geografických hranic, které nejsou definovány pouze kódy mobilních sítí. Bez povědomí o LATA by mobilní síť mohla směrovat všechny hovory stejným způsobem, což by mohlo vést k porušování regulatorních pravidel nebo ke sporům mezi operátory o fakturaci hovorů překračujících hranice LATA. Poskytuje vrstvu logiky směrování založenou na poloze, která doplňuje směrování založené na [PLMN](/mobilnisite/slovnik/plmn/).

K jeho vytvoření vedla nutnost integrace mobilních sítí do stávajících telekomunikačních infrastruktur a regulačních režimů. Řeší omezení směrování zaměřeného pouze na mobilní sítě tím, že začleňuje geografické konstrukty pevných sítí, což umožňuje přesné poskytování služeb, zákonné propojení a odpovídající fakturaci hovorů, které procházejí různými místními servisními oblastmi.

## Klíčové vlastnosti

- Definuje regulační geografickou oblast pro telekomunikační služby.
- Slouží k rozlišení mezi místním a dálkovým směrováním hovorů v jádru sítě.
- Ovlivňuje fakturaci a vyúčtování mezi různými operátory.
- Odkazuje se na něj v profilech účastníků a směrovacích tabulkách v HLR/GMSC.
- Podporuje dodržování regulatorních požadavků v konkrétních regionech, jako je Severní Amerika.
- Integruje směrování v mobilní síti s dědictvím administrativních hranic pevných sítí.

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description

---

📖 **Anglický originál a plná specifikace:** [LATA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lata/)
