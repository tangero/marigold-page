---
slug: "cco"
url: "/mobilnisite/slovnik/cco/"
type: "slovnik"
title: "CCO – Capacity and Coverage Optimization"
date: 2025-01-01
abbr: "CCO"
fullName: "Capacity and Coverage Optimization"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/cco/"
summary: "CCO je funkce samoorganizující sítě (SON), která automaticky optimalizuje kapacitu a pokrytí rádiové sítě úpravou parametrů buněk. Řeší mezery v pokrytí, interferenci a kapacitní omezení za účelem zle"
---

CCO (Capacity and Coverage Optimization) je funkce samoorganizující sítě (SON), která automaticky optimalizuje kapacitu a pokrytí rádiové sítě úpravou parametrů buněk za účelem řešení mezer v pokrytí, interference a kapacitních omezení.

## Popis

Capacity and Coverage Optimization (CCO) je základní funkcí v rámci architektury samoorganizujících sítí (SON) podle 3GPP, konkrétně definovanou v rámci architektury Operations, Administration, and Maintenance (OAM). Jejím hlavním cílem je autonomně řídit základní kompromis mezi rádiovým pokrytím a síťovou kapacitou dynamickou konfigurací a laděním rádiových parametrů na úrovni buňky. Funkce pracuje v systému uzavřené smyčky řízení, který kontinuálně monitoruje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) ze sítě, analyzuje je vůči definovaným cílům a prahovým hodnotám a provádí změny parametrů, aby síť přivedla do optimálního provozního stavu. Tento proces minimalizuje manuální zásahy, snižuje provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a zajišťuje, že se síť přizpůsobuje denním, týdenním a sezónním změnám provozu i dlouhodobým změnám v rádiovém prostředí.

Architektonická implementace CCO zahrnuje několik klíčových komponent v systému OAM a v rádiové přístupové síti (RAN). Vrstva Network Management ([NM](/mobilnisite/slovnik/nm/)) nebo Element Management ([EM](/mobilnisite/slovnik/em/)) hostí algoritmy a logiku CCO. Shromažďuje širokou škálu měřených dat, včetně měření Radio Resource Management (RRM), měření výkonu (PM) a potenciálně dat Minimization of Drive Tests ([MDT](/mobilnisite/slovnik/mdt/)). Tyto datové body poskytují přehled o síle signálu (RSRP/RSRQ), úrovních interference, úspěšnosti handoverů, míře ztráty hovorů, propustnosti a zatížení buňky. Na základě těchto vstupů funkce CCO vypočítá optimální úpravy konfigurovatelných parametrů buňky. Mezi nejčastěji laděné parametry patří výkon vysílání referenčního signálu, individuální offset buňky (CIO) pro robustnost mobility, sklon antény (elektrický nebo mechanický) a prahové hodnoty pro handover. Tyto úpravy jsou následně zaslány příslušným síťovým elementům, jako je eNodeB v LTE nebo gNB v 5G NR, prostřednictvím standardizovaných rozhraní jako je Itf-N.

Pracovní postup CCO typicky následuje cyklus monitorování-analýza-plánování-provedení. Ve fázi monitorování systém shromažďuje data o výkonu v reálném čase i historická. Fáze analýzy identifikuje suboptimální podmínky, jako jsou mezery v pokrytí (oblasti se slabým signálem), pilot pollution (nadměrné překrývání pokrytí způsobující interferenci) nebo kapacitní přetížení v buňkách s vysokým provozem. Fáze plánování určuje konkrétní změny parametrů potřebné k řešení těchto problémů, často za použití optimalizačních algoritmů, které předpovídají dopad změn na sousední buňky, aby se předešlo vytvoření nových problémů. Nakonec fáze provedení změny aplikuje, často postupně nebo po krocích, a cyklus se restartuje pro ověření účinnosti úprav. Tento automatizovaný, daty řízený přístup je mnohem efektivnější a rychlejší než tradiční procesy manuální optimalizace a umožňuje sítím trvale udržovat vysoký výkon a kvalitu služeb (QoS).

## K čemu slouží

CCO bylo vytvořeno k řešení významných provozních výzev a nákladů spojených s manuální optimalizací moderních, hustých a heterogenních rádiových přístupových sítí. Před příchodem SON a CCO byla optimalizace sítě pracně náročný, reaktivní proces prováděný týmy pro měření z vozidel a inženýry pro rádiové plánování. Tento přístup byl pomalý, drahý a nedokázal držet krok s rychlými změnami v chování uživatelů, poptávce po provozu nebo rádiovém frekvenčním prostředí. Mezery v pokrytí, problémy s interferencí a nedostatek kapacity přetrvávaly dny nebo týdny, dokud nebyly manuálně identifikovány a opraveny, což vedlo ke špatnému uživatelskému komfortu, ztrátám hovorů a neefektivnímu využití zdrojů. Rozmach menších buněk (mikro, piko, femto) a rostoucí složitost síťových topologií učinily manuální optimalizaci prakticky neudržitelnou.

Zavedení CCO jako součásti sady SON v 3GPP Release 8 bylo motivováno potřebou provozní automatizace ke snížení [CAPEX](/mobilnisite/slovnik/capex/) a [OPEX](/mobilnisite/slovnik/opex/) při současném zlepšení síťového výkonu. Řeší základní problém staticky konfigurovaných sítí, které nejsou vhodné pro dynamické reálné podmínky. CCO umožňuje proaktivní a kontinuální optimalizační cyklus. Automatickým vyvažováním pokrytí a kapacity zajišťuje efektivní využití rádiových zdrojů, rozšiřuje efektivní oblast služeb, zlepšuje propustnost pro uživatele na okraji buňky a snižuje interferenci. To přímo vede k vyšší spokojenosti a udržení zákazníků. Dále umožňuje operátorům rychleji nasazovat sítě („plug-and-play“) s jistotou, že SON funkce automaticky vyladí počáteční nastavení pro konkrétní prostředí nasazení, čímž se urychlí uvedení nových lokalit a technologií na trh.

## Klíčové vlastnosti

- Automatizované řízení v uzavřené smyčce pro ladění parametrů
- Kontinuální optimalizace založená na analýze KPI a měřených dat
- Dynamické nastavování výkonu buňky, sklonu antény a parametrů mobility
- Odstranění mezer v pokrytí a interference (pilot pollution)
- Vyvažování zátěže a optimalizace kapacity napříč buňkami
- Podpora vícevýrobcových prostředí prostřednictvím standardizovaných rozhraní

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 32.836** (Rel-12) — NM Centralized Coverage and Capacity Optimization Study
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification

---

📖 **Anglický originál a plná specifikace:** [CCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/cco/)
