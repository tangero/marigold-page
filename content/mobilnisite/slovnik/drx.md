---
slug: "drx"
url: "/mobilnisite/slovnik/drx/"
type: "slovnik"
title: "DRX – Discontinuous Reception"
date: 2026-01-01
abbr: "DRX"
fullName: "Discontinuous Reception"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/drx/"
summary: "Mechanismus pro úsporu energie, při kterém uživatelské zařízení (UE) periodicky vypíná svůj přijímač podle nakonfigurovaného cyklu. Naslouchá přiřazení plánování pouze během aktivních period, což výra"
---

DRX je mechanismus pro úsporu energie v mobilních sítích 3GPP, při kterém uživatelské zařízení (UE) periodicky vypíná svůj přijímač a naslouchá přiřazení plánování pouze během nakonfigurovaných aktivních period, čímž prodlužuje výdrž baterie.

## Popis

Discontinuous Reception (DRX) je základní technika pro úsporu energie používaná v radiových přístupových sítích 3GPP, včetně UTRAN, [E-UTRAN](/mobilnisite/slovnik/e-utran/) (LTE) a NG-RAN (5G NR). Hlavní princip umožňuje uživatelskému zařízení (UE) deaktivovat obvody svého rádiového přijímače na předem definovaná období, čímž přechází do stavu nízké spotřeby („spánku“), a probouzet se pouze v určitých intervalech, aby zkontrolovalo možná přiřazení plánování downlink dat ze sítě na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Tento cyklus je řízen časovači a parametry nakonfigurovanými sítí prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Provoz DRX je úzce integrován s procedurami Radio Resource Management (RRM) a mobility UE, jako je převýběr buňky a handover.

Architektura DRX zahrnuje několik klíčových časovačů a cyklů. Základní struktura obsahuje časovač 'On Duration', během kterého musí UE monitorovat PDCCH. Pokud jsou data naplánována, UE zůstane vzhůru a spustí 'Inactivity Timer', který se resetuje s každým novým přiřazením plánování. Po vypršení tohoto časovače UE vstoupí do 'DRX cyklu', který střídá krátká spánková období s krátkými obdobími naslouchání. Pro agresivnější úsporu energie lze nakonfigurovat delší 'Long DRX Cycle'. Síť má přesnou znalost vzoru DRX UE, což jí umožňuje buffrovat downlink data a plánovat přenosy pouze během aktivních naslouchacích oken UE, a zajistit tak, že žádná data nejsou ztracena. V připojeném režimu (Connected Mode) je to známé jako C-DRX, které vyvažuje latenci a spotřebu energie. V nečinném režimu (Idle Mode) platí podobný koncept prostřednictvím Paging Discontinuous Reception, kde se UE probouzí pouze na specifických Paging Occasions v rámci Paging Frame, aby zkontrolovalo pagingové zprávy.

Z perspektivy fyzické vrstvy DRX ovlivňuje plán demodulace a dekódování UE. UE musí synchronizovat svá probouzení s přenosovými časovými intervaly (TTI) sítě. Pokročilé funkce zavedené v jednotlivých release zahrnují zarovnání DRX s měřicími mezerami (measurement gaps) a vylepšenou podporu funkcí jako Carrier Aggregation a Dual Connectivity, kde mohou být DRX vzory koordinovány napříč více komponentními nosiči nebo skupinami buněk. V 5G NR jsou principy DRX rozšířeny o flexibilnější sady parametrů pro podporu různorodých požadavků služeb, od ultra-spolehlivé komunikace s nízkou latencí (URLLC) až po massive IoT, což umožňuje velmi krátké cykly pro kritická data nebo extrémně dlouhé cykly pro provoz senzorů na pozadí.

## K čemu slouží

DRX bylo vytvořeno, aby řešilo zásadní výzvu spotřeby baterie UE v celulárních sítích. Nepřetržité monitorování řídicích kanálů pro možná přiřazení dat je extrémně energeticky náročné. Před zavedením DRX by baterie UE ve stavech vyhrazeného kanálu rychle klesala i během období nečinnosti. Primárním účelem DRX je dramaticky prodloužit provozní výdrž baterie mobilních zařízení, což je klíčový faktor pro uživatelský zážitek a přijetí zařízení. Řeší problém neefektivního využití energie během nečinných nebo poloaktivních stavů tím, že umožňuje zařízení přejít do stavu nízké spotřeby bez ztráty síťového připojení nebo schopnosti přijímat příchozí data s přijatelnou latencí.

Vývoj DRX odráží vývoj mobilních služeb. V raném 3G (Release 99) byl zaveden základní DRX pro nečinný režim (Idle Mode). Jak se staly běžnými služby paketových dat vždy připojené (always-on), byl pro [HSPA](/mobilnisite/slovnik/hspa/) vyvinut Connected Mode DRX (C-DRX) a později vylepšen v LTE, což umožnilo smartphonům udržovat IP konektivitu pro push notifikace a synchronizaci na pozadí při současné úspoře energie. Každý nový release přinesl optimalizace: kratší časy nastavení, zarovnání s dalšími procedurami, jako jsou měření, a adaptaci na nové síťové architektury jako je agregace nosičů (carrier aggregation). Motivací bylo vždy vyvážit protichůdné požadavky nízké latence (vyžadující časté naslouchání) a dlouhé výdrže baterie (vyžadující dlouhá spánková období) a přizpůsobit mechanismus různorodým případům užití od hlasových hovorů až po neustále připojené cloudové aplikace.

## Klíčové vlastnosti

- Konfigurovatelné DRX cykly (krátký a dlouhý) pro kompromis mezi latencí a úsporou energie.
- Inactivity Timer pro dynamické prodloužení aktivního času při přenosu dat.
- On Duration Timer definující povinné naslouchací okno na začátku každého cyklu.
- Podpora pro DRX v nečinném režimu (Idle Mode DRX, pro paging) i v připojeném režimu (Connected Mode DRX, C-DRX).
- Zarovnání s měřicími mezerami (measurement gaps), handovery a dalšími RRM procedurami, aby se předešlo konfliktům.
- Flexibilní parametrizace v 5G NR pro podporu různorodých požadavků služeb (eMBB, URLLC, mMTC).

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.720** (Rel-13) — Cellular IoT Architecture Enhancement Study
- **TR 23.776** (Rel-17) — V2X Architecture Enhancements Phase 2
- **TR 23.799** (Rel-14) — Study on Next Generation System Architecture
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.324** (Rel-19) — Broadcast/Multicast Control Protocol
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- … a dalších 42 specifikací

---

📖 **Anglický originál a plná specifikace:** [DRX na 3GPP Explorer](https://3gpp-explorer.com/glossary/drx/)
