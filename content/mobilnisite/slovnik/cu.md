---
slug: "cu"
url: "/mobilnisite/slovnik/cu/"
type: "slovnik"
title: "CU – Control Unit"
date: 2026-01-01
abbr: "CU"
fullName: "Control Unit"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cu/"
summary: "Control Unit je funkční entita v architektuře RAN podle 3GPP odpovědná za řízení funkcí řídicí roviny. Je klíčovou součástí rozdělené architektury RAN, která umožňuje centralizované řízení a koordinac"
---

CU je funkční entita v architektuře RAN podle 3GPP odpovědná za řízení funkcí řídicí roviny, která umožňuje centralizované řízení a koordinaci v rozdělené RAN.

## Popis

Control Unit (CU) je logický uzel definovaný v architektuře Next Generation Radio Access Network (NG-RAN) podle 3GPP, konkrétně jako součást gNB (5G NodeB) nebo ng-eNB. Představuje centralizovanou entitu řídicí roviny v disagregovaném modelu RAN. CU je odpovědná za hostování protokolu Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a protokolu Service Data Adaptation Protocol (SDAP) pro řídicí rovinu. Provádí klíčové funkce, jako je správa spojení, správa mobility, řízení rádiových přenosových kanálů a koordinace rušení mezi buňkami. Centralizací těchto náročných inteligentních funkcí umožňuje CU efektivnější sdružování zdrojů a koordinaci napříč širší geografickou oblastí pokrytou více distribuovanými jednotkami ([DU](/mobilnisite/slovnik/du/)).

Architektonicky se CU připojuje k 5G Core Network (5GC) přes rozhraní [NG](/mobilnisite/slovnik/ng/) a k jedné nebo více DU přes rozhraní F1, jak je standardizováno v 3GPP. Rozhraní F1 se dále dělí na část [F1-C](/mobilnisite/slovnik/f1-c/) (řídicí rovina) a [F1-U](/mobilnisite/slovnik/f1-u/) (uživatelská rovina). CU terminuje rozhraní F1-C, přes které zasílá řídicí zprávy pro konfiguraci a správu DU. Tato rozdělená architektura umožňuje nasadit CU na centralizovanějším místě, jako je regionální datové centrum, zatímco DU zůstávají na lokalitách buněk. CU může být implementována jako softwarová funkce běžící na standardním komerčním hardwaru ([COTS](/mobilnisite/slovnik/cots/)), což usnadňuje virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a principy cloud-nativního přístupu.

Z provozní perspektivy CU zpracovává ne-reálné času protokoly a funkce vrstvy 3. Když uživatelské zařízení (UE) zahájí spojení, je CU odpovědná za procedury RRC, včetně vysílání systémových informací, pagingu, navázání, rekonfigurace a uvolnění RRC spojení. Činí rozhodnutí o předávání spojení na základě měřicích hlášení od UE a koordinuje provedení předání se zdrojovou a cílovou DU. CU také spravuje toky kvality služeb (QoS) jejich mapováním na datové rádiové přenosové kanály ([DRB](/mobilnisite/slovnik/drb/)) ve spolupráci s funkcí správy relací (SMF) v jádře sítě. Její centralizovaná povaha je klíčová pro implementaci pokročilých funkcí, jako je koordinovaný vícebodový přenos/příjem (CoMP) a duální konektivita (DC).

Zavedení CU představuje zásadní odklon od monolitického návrhu základnové stanice. Odděluje vývoj softwaru řídicí roviny od hardwarově závislého zpracování fyzické vrstvy a částí vrstvy MAC v reálném čase, které sídlí v DU. Toto oddělení poskytuje významnou flexibilitu nasazení. Operátoři si mohou zvolit rozdělení CU-DU na základě požadavků na latenci a šířku pásma přístupové části sítě, s možnostmi více centralizované CU (podporující mnoho DU) nebo více distribuovaného nasazení. Softwarová povaha CU také zjednodušuje aktualizace, škálování a zavádění nových služeb, což z ní činí základní kámen pro iniciativy open RAN (O-RAN) a síťové segmentace v 5G.

## K čemu slouží

CU byla zavedena, aby řešila omezení tradičních integrovaných základnových stanic (NodeB a eNodeB), které sdružovaly všechny rádiové protokolové vrstvy do jedné jednotky umístěné na lokalitě. Tato monolitická architektura činila sítě nepružnými, obtížně škálovatelnými a nákladnými na modernizaci. Hlavní motivací pro vytvoření CU bylo umožnit flexibilnější, efektivnější a nákladově výhodnější RAN prostřednictvím funkční disagregace. Oddělením řídicí roviny (CU) od uživatelské roviny a zpracování nižších vrstev (DU) získávají operátoři schopnost centralizovat inteligenci, sdružovat zdroje a využívat výhody cloudové ekonomiky. Toto rozdělení je nezbytné pro splnění různorodých a náročných požadavků 5G, jako je vylepšená mobilní širokopásmová komunikace (eMBB), ultra-spolehlivá komunikace s nízkou latencí (URLLC) a komunikace s hromadnými strojovými zařízeními (mMTC).

Historicky každá základnová stanice fungovala z velké části nezávisle, s koordinací omezenou na standardizovaná rozhraní jako X2 v LTE. To činilo optimalizaci v rámci celé sítě a implementaci pokročilých funkcí, jako je koordinované plánování, složitou a neefektivní. Architektura zaměřená na CU poskytuje přirozený bod pro centralizované řídicí a optimalizační algoritmy, které mohou spravovat rádiové zdroje napříč desítkami nebo stovkami lokalit buněk současně. Řeší problém neefektivního využití zdrojů a suboptimálního řízení rušení v hustých síťových nasazeních. Dále řeší výzvu provozních nákladů (OPEX) tím, že umožňuje aplikovat softwarové aktualizace a zavádění nových funkcí centrálně na CU, namísto vyžadování manuálních aktualizací na každé lokalitě buňky.

Vytvoření CU bylo také hnací silou pohybu průmyslu směrem k virtualizaci a otevřeným rozhraním. Umožňuje RAN sladit se se širší transformací telekomunikačního cloudu, kde jsou síťové funkce softwarově definované a běží na univerzálním hardwaru. Tato otevřenost, jejímž příkladem je standardizované rozhraní F1 mezi CU a DU, podporuje interoperabilitu mezi více dodavateli a inovace. Umožňuje operátorům získávat software CU a DU od různých dodavatelů, čímž narušuje závislost na jediném dodavateli a podporuje konkurenční ekosystém. CU v konečném důsledku existuje pro zajištění budoucí životaschopnosti mobilních sítí, poskytuje architektonický základ, který je škálovatelný, agilní a schopný podporovat vyvíjející se požadavky služeb a nové technologické paradigmy, jako je síťové segmentování a optimalizace RAN řízená umělou inteligencí.

## Klíčové vlastnosti

- Hostuje protokoly řídicí roviny Radio Resource Control (RRC) a SDAP
- Centralizuje správu spojení a mobility pro více distribuovaných jednotek (DU)
- Terminuje rozhraní F1 řídicí roviny (F1-C) směrem k DU
- Umožňuje optimalizaci a koordinaci rádiových zdrojů v rámci celé sítě
- Usnadňuje softwarové nasazení a aktualizace prostřednictvím virtualizace
- Poskytuje kotvu řídicí roviny pro síťové segmenty a správu toků QoS

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines
- **TS 28.304** (Rel-19) — PEE Parameters Control & Monitoring Requirements
- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [CU na 3GPP Explorer](https://3gpp-explorer.com/glossary/cu/)
