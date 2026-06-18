---
slug: "mnp"
url: "/mobilnisite/slovnik/mnp/"
type: "slovnik"
title: "MNP – Mobile Number Portability Signalling Relay Function"
date: 2025-01-01
abbr: "MNP"
fullName: "Mobile Number Portability Signalling Relay Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mnp/"
summary: "Síťová funkce umožňující přenositelnost mobilních čísel (MNP) směrováním signalizačních zpráv do správné sítě poté, co účastník přenesl své číslo. Zachycuje dotazy (např. SRI) a využívá databázi přeno"
---

MNP je síťová funkce, která směruje signalizační zprávy pro přenesená čísla do správné sítě tím, že zachycuje dotazy a konzultuje databázi přenositelnosti čísel.

## Popis

Funkce reléového přenosu signalizace pro přenositelnost mobilních čísel (MNP [SRF](/mobilnisite/slovnik/srf/)) je klíčový síťový prvek specifikovaný 3GPP pro implementaci přenositelnosti mobilních čísel (MNP). MNP umožňuje účastníkům zachovat své mobilní telefonní číslo při přechodu k jinému poskytovateli služeb (mobilnímu síťovému operátorovi). Hlavní technický problém, který MNP SRF řeší, je směrování hlasových hovorů a signalizačních zpráv (např. [SMS](/mobilnisite/slovnik/sms/)) do správné příjemcovské sítě poté, co bylo číslo přeneseno z původní "dárčí" sítě.

Z architektonického hlediska se MNP SRF typicky nachází v signalizační cestě, často je integrována s nebo umístěna poblíž signalizačního přenosového bodu ([STP](/mobilnisite/slovnik/stp/)) nebo je součástí signalizačního směrovače na bázi IP. Její činnost je spuštěna během sestavování hovoru nebo relace. Když je uskutečněn hovor na přenesené číslo, ústředna nebo funkce řízení hovorové relace ([CSCF](/mobilnisite/slovnik/cscf/)) volající sítě odešle signalizační dotaz, například dotaz Send Routing Information ([SRI](/mobilnisite/slovnik/sri/)) v protokolu [MAP](/mobilnisite/slovnik/map/), do sítě, kterou na základě číselného rozsahu považuje za domovskou. MNP SRF tento dotaz zachytí. Následně dotazuje centrální nebo distribuovanou databázi přenositelnosti čísel ([NPDB](/mobilnisite/slovnik/npdb/)), aby zjistila, zda bylo volané číslo přeneseno, a pokud ano, ke kterému příjemcovskému operátorovi nyní patří.

Po obdržení odpovědi z NPDB MNP SRF provede klíčovou funkci: upraví signalizační zprávu. Pro přenesené číslo nahradí původní cílovou globální titulaci ([GT](/mobilnisite/slovnik/gt/)) adresu (odkazující na HLR dárčí sítě) GT adresou HLR příjemcovské sítě. Poté upravený dotaz přepošle do správné sítě. Tento proces je pro volající ústřednu transparentní. MNP SRF může být také zapojena do dalších procedur, jako je zpracování chyb nebo správa mezipaměti údajů o přenositelnosti pro optimalizaci výkonu. Její implementace zajišťuje, že všechny sítě, včetně těch, které nejsou přímo zapojeny do transakce přenosu čísla, mohou správně směrovat provoz bez nutnosti univerzálních aktualizací vlastních směrovacích tabulek pro každé přenesené číslo.

## K čemu slouží

MNP a MNP SRF byly vytvořeny za účelem podpory volby spotřebitele a konkurence na trhu odstraněním hlavní překážky při změně poskytovatele: ztráty telefonního čísla. Před zavedením MNP byli účastníci efektivně "uzamčeni" u svého operátora, protože změna čísla znamenala značné nepohodlí a náklady. Regulační orgány v mnoha zemích nařídily MNP, aby stimulovaly konkurenci, což vedlo k potřebě standardizovaného technického řešení.

MNP SRF řeší problém distribuované směrovací logiky. Bez ní by každý síťový operátor musel neustále aktualizovat své interní směrovací tabulky nejnovějšími informacemi o přenosech pro každé číslo v zemi – což je velmi neefektivní a náchylný proces k chybám. SRF tuto inteligenci centralizuje. Poskytuje jediný bod pro dotazování, což umožňuje volající síti směrovat hovory na základě volaných číslic obvyklým způsobem, zatímco SRF zajišťuje přesměrování dotazu do správné síťové databáze. Tato architektura, standardizovaná 3GPP počínaje Release 4, poskytla škálovatelnou a spolehlivou metodu pro implementaci regulačního požadavku a zajištění interoperability mezi všemi operátory na trhu.

## Klíčové vlastnosti

- Zachycuje a upravuje signalizační zprávy (např. MAP SRI) pro přenesená čísla
- Rozhraní k databázi přenositelnosti čísel (NPDB) pro získání směrovacích údajů
- Přeposílá dotazy do správného HLR příjemcovské sítě
- Poskytuje transparentní provoz pro ústředny volající sítě
- Podporuje doručování hovorů, SMS a dalších služeb na přenesená čísla
- Může implementovat mechanismy mezipaměti ke snížení zatížení NPDB dotazy

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [GT – Global Title](/mobilnisite/slovnik/gt/)
- [NPDB – Number Portability Data Base](/mobilnisite/slovnik/npdb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.066** (Rel-19) — Mobile Number Portability Stage 1
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [MNP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnp/)
