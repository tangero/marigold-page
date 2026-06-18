---
slug: "cli"
url: "/mobilnisite/slovnik/cli/"
type: "slovnik"
title: "CLI – Common Language Infrastructure"
date: 2026-01-01
abbr: "CLI"
fullName: "Common Language Infrastructure"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cli/"
summary: "Standardizovaný rámec pro správu síťových prvků a služeb telekomunikačních sítí v prostředí více dodavatelů. Poskytuje společnou syntaxi a sémantiku pro konfiguraci, správu chyb a monitorování výkonu,"
---

CLI je Common Language Infrastructure, standardizovaný rámec pro správu síťových prvků a služeb telekomunikačních sítí více dodavatelů, který využívá společnou syntaxi a sémantiku pro konfiguraci, správu chyb a výkonu.

## Popis

Common Language Infrastructure (CLI) je komplexní rámec pro správu definovaný 3GPP, který standardizuje rozhraní mezi systémy provozu a údržby (O&M) a síťovými prvky ([NE](/mobilnisite/slovnik/ne/)) od různých dodavatelů. Stanovuje společnou syntaxi příkazového řádku, strukturu příkazů a sémantický význam pro správní operace, což umožňuje operátorům sítí používat konzistentní postupy napříč heterogenním síťovým vybavením. Tato infrastruktura je klíčová pro automatizaci úloh správy sítě, provádění hromadných konfigurací a zajištění jednotného fungování provozních skriptů a nástrojů bez ohledu na podkladovou hardwarovou nebo softwarovou implementaci.

Z architektonického hlediska CLI funguje jako rozhraní pro správu, k němuž se typicky přistupuje prostřednictvím relací secure shell ([SSH](/mobilnisite/slovnik/ssh/)) nebo telnet k síťovým prvkům, jako jsou základnové stanice (gNB, [eNB](/mobilnisite/slovnik/enb/)), funkce jádra sítě ([AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/), [UPF](/mobilnisite/slovnik/upf/)) a uživatelská zařízení. Rámec definuje hierarchickou strukturu příkazů s módy (jako je globální konfigurační mód, konfigurační mód rozhraní), kontextovou nápovědu, doplňování příkazů a standardizované výstupní formáty. Mezi klíčové komponenty patří parser příkazů, který interpretuje vstup uživatele podle definované syntaxe; modul autorizace a autentizace, který řídí přístup na základě uživatelských oprávnění; a prováděč příkazů, který překládá platné příkazy do konkrétních akcí na řídicí rovině síťového prvku.

Role CLI v síti přesahuje základní konfiguraci a zahrnuje správu chyb (příkazy show pro alarmy a logy), monitorování výkonu (načítání čítačů a statistik), správu zabezpečení (řídicí seznamy přístupu, správa certifikátů) a správu softwaru (aktualizace obrazů, správa záplat). Infrastruktura podporuje jak interaktivní relace pro manuální operace, tak skriptované relace pro automatizaci, přičemž výstupní formáty jsou navrženy jak pro čitelnost člověkem, tak pro strojové zpracování (např. [XML](/mobilnisite/slovnik/xml/), [JSON](/mobilnisite/slovnik/json/) v novějších vydáních). Tato dvojí schopnost činí CLI nezbytnou pro každodenní provoz sítě i pro systémy orchestrace velkého měřítka.

Z pohledu implementace jsou příkazy CLI mapovány na podkladové správní protokoly a datové modely, jako jsou NETCONF/YANG nebo proprietární rozhraní. Zatímco CLI prezentuje operátorovi jednotné textové rozhraní, funguje jako fasáda, která překládá příkazy na operace specifické pro protokol na spravované entitě. Rámec také definuje konvence pro seskupování příkazů (např. všechny příkazy související s rádiovým rozhraním pod hierarchií 'radio'), standardizované názvy parametrů (např. cellId, plmnId) a konzistentní chybové zprávy, což výrazně snižuje křivku učení pro inženýry pracující s vybavením od více dodavatelů.

## K čemu slouží

CLI bylo vytvořeno, aby řešilo kritický problém provozní složitosti v telekomunikačních sítích více dodavatelů. Před standardizací každý výrobce zařízení implementoval proprietární rozhraní příkazového řádku s odlišnou syntaxí, strukturou příkazů a chováním, což nutilo operátory sítí udržovat samostatné dovednosti, provozní postupy a automatizační nástroje pro vybavení každého dodavatele. Tato fragmentace zvyšovala provozní náklady, zvyšovala riziko lidské chyby při změnách konfigurace a bránila automatizaci sítí velkého měřítka. Common Language Infrastructure poskytuje jednotnou vrstvu správy, která abstrahuje implementace specifické pro dodavatele, a umožňuje tak konzistentní provoz sítě.

Historicky, jak se sítě 2G vyvíjely v 3G (UMTS) s R99, potřeba standardizované správy se stala zřejmou kvůli rostoucí diverzitě síťových prvků a vzniku nasazení více dodavatelů. CLI bylo zavedeno, aby vytvořilo společný provozní jazyk, který přetrvá technologické generace od 3G přes 4G až po 5G. Řeší základní výzvu správy síťových prvků, které mohou mít odlišné vnitřní architektury, ale potřebují prezentovat konzistentní rozhraní pro správu operátorům sítí.

Infrastruktura řeší omezení předchozích přístupů tím, že poskytuje nejen standardizaci příkazů, ale také sémantickou konzistenci – zajišťuje, že příkazy se stejným názvem napříč různými dodavateli produkují ekvivalentní výsledky. To umožňuje operátorům psát znovupoužitelné skripty, vyvíjet standardizované provozní postupy a školit personál na jediném paradigmatu rozhraní. Snížením závislosti na dodavateli na provozní úrovni CLI podporuje zdravější konkurenci na trhu telekomunikačního vybavení a zároveň dává operátorům větší flexibilitu v návrhu sítě a výběru dodavatele.

## Klíčové vlastnosti

- Standardizovaná syntaxe příkazů a hierarchická struktura napříč dodavateli
- Kontextová nápověda a doplňování příkazů pro provozní efektivitu
- Řízení přístupu na základě rolí s konfigurovatelnými úrovněmi oprávnění
- Podpora jak interaktivních manuálních operací, tak skriptované automatizace
- Konzistentní výstupní formáty pro čitelnost člověkem a strojové zpracování
- Integrace s podkladovými správními protokoly (NETCONF, CORBA atd.)

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.420** (Rel-19) — Introduction to Xn interface specifications
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [CLI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cli/)
