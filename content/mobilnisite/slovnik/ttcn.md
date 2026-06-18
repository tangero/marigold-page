---
slug: "ttcn"
url: "/mobilnisite/slovnik/ttcn/"
type: "slovnik"
title: "TTCN – Tree and Tabular Combined Notation"
date: 2025-01-01
abbr: "TTCN"
fullName: "Tree and Tabular Combined Notation"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ttcn/"
summary: "TTCN je standardizovaný, abstraktní a protokolově nezávislý testovací jazyk vyvinutý organizací ETSI a přijatý organizací 3GPP. Používá se k specifikaci testovacích případů a sad pro shodnostní testov"
---

TTCN je standardizovaný, abstraktní a protokolově nezávislý testovací jazyk používaný organizací 3GPP k specifikaci spustitelných testovacích případů pro shodnostní testování telekomunikačních protokolů a systémů.

## Popis

Tree and Tabular Combined Notation (TTCN) je formální jazyk speciálně navržený pro specifikaci testovacích případů a procedur pro komunikační protokoly a systémy. V kontextu 3GPP je to primární jazyk používaný pro psaní specifikací shodnostních testů (TS), které ověřují, zda implementace standardu 3GPP (např. pro UE nebo síťový uzel) funguje správně podle normativních požadavků. TTCN není programovací jazyk jako C++ nebo Java, ale deklarativní jazyk, který popisuje testovací chování z hlediska podnětů odeslaných testovanému systému ([SUT](/mobilnisite/slovnik/sut/)), očekávaných odpovědí a verdiktů (Pass, Fail, Inconclusive). Jeho základní filozofií je abstrakce, oddělující testovací logiku od detailů podkladové komunikační platformy.

TTCN funguje modelováním interakce testovacího systému s SUT prostřednictvím abstraktních komunikačních portů. Testovací případ je v podstatě posloupnost událostí: odeslání protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) na port, přijetí PDU z portu, nastavení časovačů a vyhodnocení podmínek. Chování je často reprezentováno ve stromové struktuře (odtud 'Tree' v názvu), která ukazuje alternativní cesty, které test může následovat na základě odpovědí SUT. Aspekt 'Tabular' odkazuje na jeho historický prezentační formát, kde byly testovací sady publikovány jako velké tabulky definující šablony zpráv, omezení (definující konkrétní obsah zpráv) a popisy chování. TTCN testovací sada je kompilována a spouštěna prostředím TTCN runtime (TRE), které zajišťuje konkrétní kódování/dekódování zpráv a komunikaci s reálným SUT prostřednictvím testovacího adaptéru.

Klíčové komponenty TTCN testovací sady zahrnují: Testovací případy (hlavní spustitelné procedury), Testovací komponenty (modulární entity, které mohou běžet paralelně pro simulaci více rolí), Porty (abstraktní body komunikace), Šablony zpráv a omezení (pro definici struktury a obsahu PDU) a Verdikty. Jazyk podporuje jak zprávami založené, tak procedurálně založené komunikační paradigma. Pro 3GPP jsou TTCN testovací sady vyvíjeny pro prakticky všechny protokoly rozhraní vzduchu a jádra sítě (např. [RRC](/mobilnisite/slovnik/rrc/), [NAS](/mobilnisite/slovnik/nas/), [SIP](/mobilnisite/slovnik/sip/), Diameter). Tyto testovací sady jsou klíčové pro certifikační programy jako Global Certification Forum ([GCF](/mobilnisite/slovnik/gcf/)) a PTCRB, kde zařízení musí projít baterií shodnostních testů založených na TTCN, aby byla schválena pro nasazení na trhu.

## K čemu slouží

TTCN byl vytvořen k vyřešení základního problému zajištění interoperability v telekomunikačních sítích více dodavatelů. Před standardizovanými testovacími jazyky mohl každý dodavatel zařízení nebo testovací dům vyvíjet ad-hoc, proprietární testovací skripty, což vedlo k nekonzistentnímu testování, obtížím s reprodukováním výsledků a žádnou zárukou, že různé implementace budou spolupracovat. TTCN poskytl dodavatelsky neutrální, přesný a jednoznačný způsob, jak definovat, co znamená 'správné' chování podle standardu, a transformovat textové specifikace protokolů na spustitelné testovací případy.

Jeho přijetí organizací [ETSI](/mobilnisite/slovnik/etsi/) a následně 3GPP bylo motivováno potřebou důkladného shodnostního testování pro komplexní digitální mobilní systémy jako GSM. Jak se protokoly stávaly složitějšími, ruční testování bylo nedostatečné. TTCN umožnil specifikaci komplexních, stavových sekvencí interakcí a zpracování všech normativních chování a chybových stavů definovaných ve standardu. To umožnilo vytváření komplexních testovacích sad, které mohly být používány nezávislými testovacími laboratořemi po celém světě, a poskytlo tak společný benchmark pro kvalitu implementace.

Po desetiletí byl TTCN páteří certifikace mobilních zařízení a síťové infrastruktury. Zajišťuje, že UE od výrobce A se může úspěšně připojit, uskutečnit hovory a použídat datové služby v síti postavené ze zařízení výrobců B, C a D. Tím, že poskytuje jediný autoritativní zdroj testovacích případů odvozených přímo ze specifikací 3GPP, TTCN snižuje čas uvedení nových technologií na trh a dává operátorům a spotřebitelům důvěru v kompatibilitu a spolehlivost nasazených produktů.

## Klíčové vlastnosti

- Abstraktní, deklarativní jazyk pro specifikaci testovacího chování nezávislého na implementaci a platformě.
- Používá stromovou a tabulkovou strukturu k definici testovacích sekvencí, alternativ a verdiktů.
- Podporuje souběžné testovací komponenty pro modelování komplexních, víceúčastnických protokolových interakcí.
- Definuje šablony zpráv a omezení pro přesné ověření PDU.
- Integruje se s běhovými prostředími (TRE) a adaptéry pro spouštění proti reálným systémům.
- Základ pro oficiální specifikace shodnostních testů 3GPP a globální certifikaci.

## Související pojmy

- [ETSI – European Telecommunication Standardization Institute](/mobilnisite/slovnik/etsi/)

## Definující specifikace

- **TR 21.801** (Rel-19) — 3GPP Specification Drafting Rules
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TTCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/ttcn/)
