---
slug: "ru"
url: "/mobilnisite/slovnik/ru/"
type: "slovnik"
title: "RU – Resource Utilization"
date: 2025-01-01
abbr: "RU"
fullName: "Resource Utilization"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ru/"
summary: "RU je klíčový ukazatel výkonu (KPI) a koncept správy v sítích 3GPP, který měří efektivitu využití zdrojů napříč síťovými prvky, jako jsou rádiové kanály, výpočetní kapacita a přenosové spoje. Je zásad"
---

RU je klíčový ukazatel výkonu v sítích 3GPP, který měří efektivitu využití zdrojů napříč prvky, jako jsou rádiové kanály a výpočetní kapacita, za účelem optimalizace a QoS.

## Popis

Využití zdrojů (RU) ve standardech 3GPP označuje měření a správu toho, jak efektivně jsou využívány různé fyzické a logické zdroje v mobilní síti. Jde o široký koncept uplatňovaný napříč více doménami: rádiové přístupové sítě (RAN), základnové sítě (CN) a přenosové sítě. Metriky RU kvantifikují procento nebo poměr spotřebovaných zdrojů k celkovým dostupným zdrojům, což poskytuje přehled o zatížení sítě, možných úzkých místech a celkovém stavu. Tato měření jsou shromažďována síťovými prvky (např. eNodeB, gNB, [MME](/mobilnisite/slovnik/mme/), [UPF](/mobilnisite/slovnik/upf/)) a hlášena systémům pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)), jako je systém správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systém správy prvků ([EMS](/mobilnisite/slovnik/ems/)), k analýze.

V rádiové doméně RU typicky zahrnuje metriky jako využití bloků fyzických zdrojů ([PRB](/mobilnisite/slovnik/prb/)) v LTE/NR, využití kanálových prvků v UMTS nebo využití výkonu nosné. Například v LTE měří využití PRB pro downlink procento časově-frekvenčních bloků zdrojů přidělených uživatelským datům vůči celkově dostupným, což přímo ukazuje spektrální účinnost a úroveň zahlcení. V základnové síti může RU zahrnovat sledování zatížení procesoru na síťových funkcích (např. využití [CPU](/mobilnisite/slovnik/cpu/) na [AMF](/mobilnisite/slovnik/amf/)), využití paměti nebo kapacity relací na UPF (User Plane Function). RU v přenosové síti zahrnuje využití šířky pásma na backhaulových a fronthaulových spojích, jako jsou rozhraní S1, N2, N3 nebo Xn.

Technická implementace zahrnuje kontinuální monitorování čítačů a měřidel v rámci síťového softwaru a hardwaru. Ty jsou standardizovány ve specifikacích 3GPP pro správu výkonu (např. řada TS 32.405), aby byla zajištěna interoperabilita mezi dodavateli. Data RU jsou často agregována za časové intervaly (např. 15minutové nebo hodinové) a mohou při překročení prahových hodnot spouštět alarmy nebo automatizované akce prostřednictvím funkcí samoorganizujících se sítí (SON). Například vysoké RU na buňce může spustit algoritmy vyvažování zátěže pro přesměrování provozu na sousední buňky nebo může vést k doporučení pro rozšíření kapacity. Role RU je nedílnou součástí síťového řezání v 5G, kde musí být monitorováno využití zdrojů specifických pro řez, aby byla zaručena izolace a plnění smluv o úrovni služeb (SLA).

Analýza RU dále podporuje plánování kapacity a optimalizaci. Trendováním metrik RU mohou operátoři předpovídat, kdy budou zdroje vyčerpány, plánovat hardwarové upgrady, optimalizovat konfigurační parametry (např. handoverové okraje) a identifikovat nedostatečně využívaná aktiva pro úsporná opatření, jako jsou režimy spánku buněk. Je to základní kámen datově řízené správy sítě, který umožňuje efektivní rozhodování o kapitálových a provozních výdajích (CapEx/OpEx).

## K čemu slouží

Využití zdrojů jako standardizovaný koncept správy bylo vyvinuto pro řešení rostoucí složitosti a rozsahu mobilních sítí, kde neefektivní využívání zdrojů vede ke špatnému uživatelskému zážitku, zvýšeným nákladům a neschopnosti uspokojit provozní požadavky. Rané mobilní sítě se často spoléhaly na zjednodušené metriky, jako je míra blokování hovorů, které neposkytovaly podrobný přehled o tom, jak jsou spotřebovávány konkrétní zdroje (např. kódové kanály, výpočetní výkon). Jak se sítě vyvíjely pro podporu paketově přepínaných dat a vyšších kapacit, byl potřebný sofistikovanější přístup k optimalizaci vícerozměrných zdrojů.

Hlavním problémem, který RU řeší, je potřeba holistického přehledu o efektivitě sítě. Umožňuje operátorům přejít od reaktivní správy poruch k proaktivní správě výkonu a kapacity. Monitorováním RU se sítě mohou vyhnout nadměrnému dimenzování (které plýtvá kapitálem) a nedostatečnému dimenzování (které způsobuje zhoršení služeb). Například v 3G/4G může vysoké RU na kanálových kartách NodeB indikovat potřebu hardwarového rozšíření, zatímco nízké RU může naznačovat příležitosti pro vypnutí nosné za účelem úspory energie. To je obzvláště kritické s nástupem heterogenních sítí (HetNets) a hustých nasazení malých buněk, kde musí být přidělování zdrojů dynamicky optimalizováno.

Historicky bylo formalizování RU napříč vydáními 3GPP, počínaje specifikacemi z doby UMTS, hnací silou přechodu na plně IP architektury a potřeby automatizované správy sítě. Poskytuje společný jazyk pro měření výkonu napříč dodavateli, usnadňuje interoperabilitu více dodavatelů a pokročilé funkce SON. V éře 5G se účel RU rozšířil o podporu síťového řezání, kde musí být využití zdrojů každého řezu pečlivě sledováno, aby byla zajištěna izolace, předpovídány potřeby kapacity a umožněny obchodní modely typu slice-as-a-service. V konečném důsledku RU umožňuje operátorům poskytovat konzistentní QoS při maximalizaci návratnosti investic do infrastruktury.

## Klíčové vlastnosti

- Měří efektivitu využití rádiových, základnových a přenosových zdrojů (např. PRB, CPU, šířka pásma)
- Standardizované metriky výkonu a čítače pro interoperabilitu dodavatelů
- Umožňuje proaktivní optimalizaci sítě a plánování kapacity
- Podporuje funkce samoorganizujících se sítí (SON), jako je vyvažování zátěže a úspora energie
- Zásadní pro izolaci zdrojů v síťovém řezání a zajištění SLA v 5G
- Integruje se se systémy OAM pro monitorování, analýzy a reportování

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.747** (Rel-14) — Enhanced CRS and SU-MIMO IM Performance Requirements
- **TS 36.825** (Rel-13) — Study on Additional LTE TDD Configurations
- **TS 36.863** (Rel-12) — CRS Interference Mitigation for Homogeneous Networks
- **TR 38.828** (Rel-16) — CLI and RIM for NR
- **TS 38.843** (Rel-19) — Study on AI/ML for NR Air Interface
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation

---

📖 **Anglický originál a plná specifikace:** [RU na 3GPP Explorer](https://3gpp-explorer.com/glossary/ru/)
