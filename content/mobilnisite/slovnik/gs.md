---
slug: "gs"
url: "/mobilnisite/slovnik/gs/"
type: "slovnik"
title: "GS – Energy Saving Parameter (GS)"
date: 2025-01-01
abbr: "GS"
fullName: "Energy Saving Parameter (GS)"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gs/"
summary: "Parametr pro úsporu energie v síti, často označovaný jako 'ladicí' parametr, který slouží k řízení kompromisu mezi spotřebou energie a výkonem sítě v rádiové přístupové síti (RAN). Umožňuje operátorům"
---

GS je parametr pro úsporu energie v síti, který slouží k řízení kompromisu mezi spotřebou energie a výkonem dynamickým nastavováním chování základnové stanice během období nízkého provozu.

## Popis

Parametr GS, což znamená obecný parametr pro úsporu energie nebo 'ladicí' parametr, je konfigurovatelná hodnota v systému provozu, správy a údržby (OAM) 3GPP rádiové přístupové sítě (RAN), jako je LTE nebo NR. Nejde o jediný standardizovaný název parametru, ale představuje třídu parametrů používaných k jemné úpravě agresivity a chování funkcí pro úsporu energie ([ES](/mobilnisite/slovnik/es/)) implementovaných v základnových stanicích (eNodeB v LTE, gNB v NR). Tyto funkce mají za cíl snížit spotřebu energie síťové infrastruktury dynamickým přizpůsobováním vzorců přenosu buňky na základě zatížení provozem. Parametr GS typicky funguje jako práh nebo škálovací faktor, který ovlivňuje rozhodnutí, jako kdy aktivovat diskontinuální přenos ([DTX](/mobilnisite/slovnik/dtx/)) buňky, převést buňku do klidového/spacího stavu nebo upravit počet aktivních anténních portů.

Z architektonického hlediska jsou parametry GS součástí funkcí samoorganizující se sítě (SON) a správy úspor energie ([ESM](/mobilnisite/slovnik/esm/)) v RAN. Jsou konfigurovány operátorem sítě prostřednictvím systému správy prvků ([EMS](/mobilnisite/slovnik/ems/)) nebo systému správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a uplatňují se na jednotlivé buňky nebo skupiny buněk. Interní algoritmy uzlu RAN průběžně sledují klíčové ukazatele výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)), jako je zatížení buňky, propustnost uživatele a počet připojených uživatelů. Tyto KPI jsou porovnávány s prahy, které lze upravit parametrem GS. Například běžnou funkcí ES je 'DTX buňky', kdy buňka dočasně vypne své buňkově specifické referenční signály ([CRS](/mobilnisite/slovnik/crs/)) a další neustále vysílané signály během okamžiků bez uživatelské aktivity v dílčích rámcích. Parametr GS může definovat dobu trvání časovače nečinnosti nebo práh zatížení, pod nímž lze DTX aktivovat. Vyšší hodnota GS může funkci učinit agresivnější (dřívější přechod do spánku, delší spánek), což ušetří více energie, ale může potenciálně zvýšit latenci pro příchozí uživatele, protože se buňka musí probudit.

Fungování je řízení v uzavřené smyčce. Síť měří výkon, uplatňuje akce ES na základě politiky nastavené pomocí GS a poté sleduje dopad jak na úspory energie, tak na síťové KPI, jako je míra ztráty hovoru nebo doba zřízení. Pokud se výkon zhorší mimo přijatelné limity, funkce SON mohou automaticky upravit parametr GS nebo dočasně funkci ES deaktivovat. Konkrétní implementace a přesný název parametru (např. EsEnergySavingFactor, SleepModeThreshold) mohou být specifické pro dodavatele, ale koncept nastavitelného 'knoflíku' pro vyvážení energie a výkonu je standardizován v specifikacích správy. V 5G NR jsou tyto koncepty pokročilejší, s podporou mikrospánku v rámci slotů a vypínání na úrovni symbolů, a odpovídající parametry typu GS řídí tyto granulární mechanismy. Konečným cílem je dosáhnout významného snížení uhlíkové stopy RAN a provozních nákladů na elektřinu bez znatelného dopadu na kvalitu služeb, kterou zažívají koncoví uživatelé.

## K čemu slouží

Koncept parametru GS byl zaveden, aby řešil rostoucí provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a environmentální obavy spojené s masivní spotřebou energie mobilních sítí. Základnové stanice patří mezi největší spotřebiče energie v infrastruktuře mobilního operátora a tradičně byly navrženy tak, aby neustále vysílaly na plný výkon, aby zajistily nepřetržité pokrytí, a to i během nocí nebo v oblastech s velmi nízkým provozem. To vede k významnému plýtvání energií. Rané funkce pro úsporu energie byly statické (např. vypínání nosných na pevně stanovené časy), ale postrádaly flexibilitu a mohly způsobit zhoršení služeb, pokud se změnily vzorce provozu. Parametr GS poskytuje potřebnou dynamickou kontrolu, která operátorům umožňuje implementovat 'inteligentní' úsporu energie přizpůsobující se provozním podmínkám sítě v reálném čase.

Motivace vychází z práce 3GPP na SON a automatizaci správy sítí, která naplno začala přibližně od Release 8/9. V rámci iniciativ 'Green Radio' začaly specifikace zahrnovat požadavky a pokyny pro úsporu energie. Nicméně univerzální algoritmus nebyl proveditelný kvůli rozdílům v implementacích dodavatelů, topografii sítě (městské vs. venkovské) a profilech provozu. Parametr GS (nebo sada parametrů) dává operátorům standardizovaný způsob, jak vykonávat kontrolu nad těmito algoritmy specifickými pro dodavatele. Umožňuje jim nastavit politiku, která odpovídá jejich specifickým obchodním cílům – například konzervativní nastavení upřednostňující vždy dostupný výkon, nebo agresivní nastavení maximalizující úsporu energie během předvídatelných období nízkého provozu.

Parametr GS navíc umožňuje kompromis, který je klíčový pro stabilitu sítě. Akce pro úsporu energie, jako je uvedení buňky do spánku, inherentně ovlivňují sousední buňky kvůli změněným interferenčním vzorcům a hranicím pokrytí. Příliš agresivní nastavení by mohlo vést k mezerám v pokrytí nebo zvýšenému zatížení sousedních buněk, což způsobí kongesci. Ladicí parametr umožňuje operátorům najít optimální bod prostřednictvím terénních testů a optimalizace. Představuje klíčový nástroj v arzenálu operátora pro udržitelný provoz sítě, přispívá k cílům společenské odpovědnosti firem a pomáhá splnit regulatorní požadavky na energetickou účinnost. Jeho vývoj probíhá paralelně s rostoucí sofistikovaností hardwaru RAN, který nyní podporuje granulárnější stavy sníženého příkonu, což činí jemně nastavovanou kontrolu prostřednictvím parametrů jako GS ještě cennější.

## Klíčové vlastnosti

- Konfigurovatelný parametr OAM pro řízení chování funkce pro úsporu energie (ES)
- Působí jako práh, časovač nebo škálovací faktor v algoritmech pro úsporu energie v RAN
- Umožňuje dynamický kompromis mezi spotřebou energie a výkonem sítě (latencí, dostupností)
- Aplikuje se na buňku nebo skupinu buněk prostřednictvím systémů správy sítě
- Integruje se s funkcemi SON pro optimalizaci a stabilitu v uzavřené smyčce
- Implementace specifická pro dodavatele, ale dodržuje standardizované principy správy

## Definující specifikace

- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation

---

📖 **Anglický originál a plná specifikace:** [GS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gs/)
