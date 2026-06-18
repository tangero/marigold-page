---
slug: "rte"
url: "/mobilnisite/slovnik/rte/"
type: "slovnik"
title: "RTE – Remote Terminal Emulator"
date: 2025-01-01
abbr: "RTE"
fullName: "Remote Terminal Emulator"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rte/"
summary: "Testovací a validační nástroj, který v kontrolovaném prostředí emuluje chování vzdáleného terminálu (UE). Používá se pro konformní testování, validaci protokolů a testování interoperability síťových z"
---

RTE je testovací nástroj, který emuluje vzdálený terminál (UE) pro konformní testování, validaci protokolů a testování interoperability síťových zařízení v kontrolovaném prostředí.

## Popis

Emulátor vzdáleného terminálu (RTE) je klíčový nástroj v rámci testovacího a validačního rámce 3GPP, specifikovaný primárně v TS 21.905. Funguje jako softwarový nebo hardware-in-the-loop systém navržený k napodobování chování uživatelského zařízení (UE) nebo jiných koncových zařízení z vzdálené lokality. RTE komunikuje s testovanými síťovými prvky, jako jsou základnové stanice (NodeB, eNodeB, gNB) nebo uzly jádra sítě, generováním standardizované signalizace a provozu v uživatelské rovině. To umožňuje výrobcům a operátorům ověřit, že síťová zařízení splňují specifikace 3GPP pro navázání hovoru, mobilní procedury, správu relací a různé služby, aniž by bylo potřeba fyzické UE.

Z architektonického hlediska se RTE typicky skládá z řídicího systému, protokolových zásobníků implementujících vrstvy jako [RRC](/mobilnisite/slovnik/rrc/), [NAS](/mobilnisite/slovnik/nas/) a [PDCP](/mobilnisite/slovnik/pdcp/), a rozhraní pro připojení k testovanému síťovému prvku. Dokáže simultánně emulovat více UE, každé s konfigurovatelnými schopnostmi a chováním, pro provádění zátěžových, stresových a funkčních testů. RTE provádí testovací scénáře definované standardizačními orgány nebo výrobci zařízení, odesílá předdefinované sekvence zpráv a porovnává odezvy sítě s očekávanými výsledky. Tento proces je zásadní pro typové schvalování, certifikaci a zajištění interoperability mezi síťovými komponentami od různých výrobců.

Při provozu je RTE často nasazován v laboratorních podmínkách jako součást testovacího systému, který může zahrnovat emulátory sítě a simulátory přenosového kanálu. Podporuje testování napříč různými releasy a technologiemi 3GPP, od UMTS přes LTE až po 5G NR, implementací příslušných verzí protokolů. Mezi klíčové testovací scénáře patří přechody stavů řízení rádiových prostředků (RRC), procedury předávání hovoru, řízení kvality služeb (QoS) a podpora nouzových služeb. Poskytnutím opakovatelného a kontrolovatelného testovacího prostředí pomáhá RTE identifikovat a řešit chyby v protokolech a problémy s výkonem ještě před nasazením sítě, čímž zvyšuje spolehlivost sítě a kvalitu služeb pro koncové uživatele.

## K čemu slouží

RTE byl zaveden jako odpověď na rostoucí složitost protokolů mobilních sítí a potřebu důkladných, standardizovaných testovacích metodik. Před jeho formální specifikací se testování často opíralo o ad-hoc metody nebo fyzická zařízení, které byly nekonzistentní, obtížně škálovatelné a neschopné spolehlivě simulovat hraniční případy nebo chybové stavy. Vytvoření standardizovaného emulátoru zajišťuje, že všichni výrobci síťových zařízení a operátoři mohou testovat vůči společné referenci, což podporuje interoperabilitu a snižuje náklady na integraci.

Jeho vývoj byl motivován rozšířením systémů 3GPP za rámec základních hlasových služeb o paketově přepínaná data, IMS a později pokročilé funkce jako agregace nosných či síťové segmenty. Každá nová funkce přinesla další protokolové stavy a toky zpráv vyžadující validaci. RTE poskytuje kontrolovanou platformu pro provádění sad konformních testů, které jsou nezbytné pro regulační schválení a komerční nasazení. Řeší problém ověření, že síťové implementace správně interpretují a reagují na signalizaci protokolů podle standardů, čímž předchází selháním sítě a degradaci služeb.

Historicky, jak se sítě vyvíjely od 3G přes 4G k 5G, se testovací požadavky zpřísnily kvůli vyšším přenosovým rychlostem, požadavkům na nízkou latenci a podpoře různých případů užití. RTE se vyvíjel souběžně s těmito technologiemi a umožňoval validaci nových protokolů rádiového rozhraní, bezpečnostních procedur a síťových architektur. Odstraňuje omezení předchozích testovacích přístupů tím, že nabízí přesnou kontrolu nad testovacími scénáři, automatizované provádění a podrobné logování, což je klíčové pro ladění složitých protokolových interakcí v prostředí s více výrobci.

## Klíčové vlastnosti

- Emulace více UE s konfigurovatelnými schopnostmi a profily předplatného
- Podpora protokolových zásobníků 3GPP napříč více releasy (UMTS, LTE, 5G NR)
- Provádění standardizovaných konformních testovacích případů pro signalizaci a procedury
- Generování a validace provozu v uživatelské rovině pro testování výkonu
- Integrace s emulátory sítě a simulátory přenosového kanálu pro komplexní (end-to-end) testování
- Podrobné nástroje pro logování a analýzu pro ladění protokolů a tvorbu certifikačních reportů

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RTE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rte/)
