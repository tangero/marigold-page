---
slug: "prat"
url: "/mobilnisite/slovnik/prat/"
type: "slovnik"
title: "PRAT – Power Rating"
date: 2025-01-01
abbr: "PRAT"
fullName: "Power Rating"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/prat/"
summary: "PRAT definuje jmenovitý výstupní výkon základnové stanice, což je klíčový parametr pro plánování sítě a soulad s regulacemi. Zajišťuje konzistentní měření výkonu napříč různými typy základnových stani"
---

PRAT je definovaný jmenovitý výstupní výkon základnové stanice, což je klíčový parametr pro konzistentní měření napříč technologiemi, který umožňuje předvídatelné pokrytí sítě, správu rušení a soulad s regulacemi.

## Popis

PRAT neboli Power Rating (hodnocení výkonu) je standardizovaná specifikace v rámci 3GPP, která definuje nominální či jmenovitou výstupní výkonovou schopnost vysílače základnové stanice. Nejde o okamžitý vysílaný výkon, ale o deklarovanou, výrobcem specifikovanou maximální úroveň výkonu za definovaných referenčních podmínek. Tento parametr je zásadní pro plánování rádiových kmitočtů ([RF](/mobilnisite/slovnik/rf/)), neboť přímo ovlivňuje plochu pokrytí buňky, výpočty útlumové bilance a potenciál pro mezibuněčné rušení. Hodnocení se typicky vyjadřuje ve wattech (W) nebo dBm a vztahuje se k celkovému výstupnímu výkonu v celém provozním kmitočtovém pásmu základnové stanice.

Specifikace PRAT zahrnuje přísné testovací a měřicí postupy uvedené v technických specifikacích 3GPP (TS), jako je TS 25.104 pro základnové stanice [UTRA](/mobilnisite/slovnik/utra/) a TS 36.104 pro základnové stanice [E-UTRA](/mobilnisite/slovnik/e-utra/). Tyto postupy zajišťují, že deklarované hodnocení výkonu je měřitelné a ověřitelné, čímž poskytují společný základ pro výrobce zařízení, provozovatele sítí a regulační orgány. Měření zohledňuje kombinovaný výkon všech nosných a anténních portů s přihlédnutím ke konfigurovanému provoznímu režimu základnové stanice.

Z architektonického hlediska je PRAT klíčovým atributem hardwaru základnové stanice ([BS](/mobilnisite/slovnik/bs/)) neboli NodeB/eNodeB/gNodeB. Je svázán s možnostmi výkonového zesilovače a celkovým RF návrhem. Nástroje pro plánování sítí používají PRAT spolu se ziskem antény, ztrátami ve feederu a modely šíření k předpovědi síly signálu v geografické oblasti. To umožňuje operátorům navrhovat sítě, které splňují cíle pokrytí a kapacity, a zároveň dodržují regulační limity pro expozici elektromagnetickému poli ([EMF](/mobilnisite/slovnik/emf/)) a nežádoucí vyzařování mimo pásmo.

Jeho role přesahuje rámec počátečního nasazení a zasahuje do průběžné optimalizace a správy sítě. Konzistentní definice hodnocení výkonu umožňují přesné srovnávání výkonnosti mezi zařízeními různých dodavatelů a usnadňují interoperabilitu v prostředí více dodavatelů. V kontextu sdílení sítí nebo densifikace (přidávání malých buněk) je pochopení PRAT každého síťového prvku klíčové pro správu celkového RF prostředí a zajištění kvality služeb.

## K čemu slouží

Primárním účelem definice standardizovaného hodnocení výkonu (PRAT) je vytvoření jasného, jednoznačného a technicky rigorózního referenčního bodu pro vysílací výkon základnových stanic. Před takovou standardizací mohli výrobci používat různé definice nebo podmínky pro specifikaci výstupního výkonu, což vedlo k nejasnostem, neporovnatelným tvrzením o výkonu a obtížím v plánování sítí. Tento nedostatek konzistence představoval významné výzvy pro operátory pořizující zařízení i pro regulátory prosazující pravidla pro spektrum a [EMF](/mobilnisite/slovnik/emf/).

3GPP zavedlo PRAT k řešení těchto problémů vytvořením společného 'jazyka' pro specifikaci výkonu. Reaguje tak na potřebu předvídatelného a reprodukovatelného výkonu sítě. Definováním přesného způsobu měření jmenovitého výkonu (např. za specifických signálových podmínek, v definovaném pásmu) zajišťuje, že základnová stanice inzerovaná s určitým PRAT bude dodávat známý a ověřitelný výstupní výkon. To je zásadní pro výpočet realistických dosahů buněk, provádění přesné koordinace rušení mezi sousedními buňkami a zajištění souladu s národními a mezinárodními rádiovými předpisy.

Historicky, jak se mobilní technologie vyvíjela od 2G přes 3G (UMTS) a dále, rostla složitost vysílačů základnových stanic s funkcemi jako provoz s více nosnými a pokročilé anténní systémy ([MIMO](/mobilnisite/slovnik/mimo/)). Koncept PRAT, zavedený ve 3GPP Release 4 pro UMTS, poskytl připravený rámec pro specifikaci výkonu těchto vyvíjejících se architektur. Převedl základní složitost na jediný, životně důležitý plánovací parametr, což umožnilo škálovatelné a spolehlivé nasazování stále sofistikovanějších rádiových přístupových sítí.

## Klíčové vlastnosti

- Definuje nominální maximální výstupní výkon základnové stanice za referenčních podmínek
- Standardizovaná metodika měření zajišťuje konzistenci a srovnatelnost napříč dodavateli
- Kritický vstup pro plánování RF sítě a nástroje pro predikci pokrytí
- Základ pro dodržování regulací souvisejících s expozicí EMF a spektrálními maskami
- Použitelné napříč více rádiovými přístupovými technologiemi 3GPP (UTRAN, E-UTRAN)
- Podporuje definice pro součet výkonu v systémech s více nosnými a více anténami

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements

---

📖 **Anglický originál a plná specifikace:** [PRAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/prat/)
