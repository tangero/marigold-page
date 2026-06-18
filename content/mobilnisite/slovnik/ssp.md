---
slug: "ssp"
url: "/mobilnisite/slovnik/ssp/"
type: "slovnik"
title: "SSP – Satellite Service Provider"
date: 2026-01-01
abbr: "SSP"
fullName: "Satellite Service Provider"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ssp/"
summary: "Satellite Service Provider (SSP) je subjekt, který provozuje a poskytuje komunikační služby prostřednictvím satelitních systémů, a to buď samostatně, nebo ve spolupráci s pozemními mobilními operátory"
---

SSP je Satellite Service Provider, subjekt, který provozuje a poskytuje komunikační služby prostřednictvím satelitních systémů, integrovaný do mobilního ekosystému za účelem poskytnutí všudypřítomného pokrytí.

## Popis

Satellite Service Provider (SSP) v kontextu 3GPP je licencovaný operátor, který spravuje satelitní komunikační infrastrukturu za účelem poskytování služeb doplňujících nebo integrovaných s pozemními mobilními sítěmi. SSP provozuje vesmírný segment (satelity na geostacionární dráze - [GEO](/mobilnisite/slovnik/geo/), střední oběžné dráze - [MEO](/mobilnisite/slovnik/meo/) nebo nízké oběžné dráze - [LEO](/mobilnisite/slovnik/leo/)) a přidružený pozemní segment (brány, řídicí centra sítě). Standardy 3GPP definují architektonické a procedurální rámce pro integraci SSP do mobilní sítě, což jim umožňuje fungovat jako rádiová přístupová síť (RAN) nebo jako přenosový článek pro páteřní síť.

Z architektonického hlediska může SSP plnit více rolí. Ve scénáři transparentní užitečné zátěže satelit funguje jako rádiový frekvenční opakovač, který přenáší signály mezi uživatelským zařízením (UE) a pozemní bránou spojenou se sítí 3GPP Core. Ve scénáři regenerativní užitečné zátěže satelit obsahuje palubní zpracování a vykonává funkce jako základnové pásmo, čímž efektivně funguje jako základnová stanice (gNB) na obloze. Síť SSP se rozhraní s mobilním jádrem prostřednictvím standardizovaných referenčních bodů, jako jsou rozhraní [N2](/mobilnisite/slovnik/n2/) (řídicí rovina) a N3 (uživatelská rovina) v 5G, což zajišťuje plynulý přenos mobility a správu relací.

Integrace funguje tak, že se brána SSP ověří a zaregistruje v páteřní síti mobilního operátora, často prostřednictvím Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) nebo přímo u Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)). SSP je zodpovědný za správu rádiových zdrojů přes satelitní spojení a řeší výzvy jako dlouhé zpoždění šíření, vysoké Dopplerovy posuny a přerušovanou viditelnost. Implementuje specifické adaptace definované v 3GPP pro neterestriální sítě ([NTN](/mobilnisite/slovnik/ntn/)), jako jsou vylepšené postupy časového předstihu a správa mobility pro pohybující se satelitní buňky.

Klíčové komponenty systému SSP zahrnují Satellite Access Node (v podstatě základnovou stanici), Gateway, která ukotvuje uživatelskou a řídicí rovinu k jádru sítě, a Network Management System pro konfiguraci satelitní konstelace. Role SSP spočívá v rozšíření pokrytí, zajištění kontinuity služeb v mobilních scénářích (např. v letadlech nebo na lodích) a poskytování služeb přímo do zařízení. V 5G může být SSP abstrahován jako specifický typ poskytovatele přístupové sítě v rámci širšího konvergenčního rámce.

## K čemu slouží

Formální uznání a standardizace Satellite Service Providers v rámci 3GPP řeší základní omezení terestriálních sítí: jejich neschopnost poskytnout nákladově efektivní, všudypřítomné pokrytí v odlehlých, námořních, leteckých a na katastrofy náchylných oblastech. Před integrací fungovaly satelitní a mobilní sítě odděleně, což vyžadovalo dvou režimová zařízení a složité ruční přepínání, což bránilo plynulému uživatelskému zážitku a omezovalo dostupnost služeb.

Motivace pro začlenění SSP vychází ze strategického cíle poskytnout skutečně globální konektivitu pro 5G a další generace, jak je nastíněno v vizi IMT-2020 organizace [ITU](/mobilnisite/slovnik/itu/). Umožňuje mobilním operátorům (MNO) spolupracovat se SSP na vyplnění mezer v pokrytí bez nutnosti nasazení nákladné terestriální infrastruktury, čímž rozšiřují svůj cílový trh. Vytváří také nový obchodní ekosystém pro SSP, aby se stali nedílnými hráči v mobilním hodnotovém řetězci, ať už nabídkou kapacit hromadně nebo přímých retailových služeb.

Historicky satelitní komunikace používala proprietární protokoly. Integrace v rámci 3GPP, která se intenzivně rozvíjí od Release 15, řeší problém interoperability tím, že umožňuje standardním 3GPP UE připojit se přímo k satelitním sítím s minimálními úpravami. Tuto konvergenci pohání vznik masivních LEO konstelací (jako Starlink, OneWeb), které slibují nižší latenci a vyšší přenosovou kapacitu, čímž se satelit stává životaschopnou součástí heterogenní sítě. Řeší případy užití jako IoT v zemědělství, přenosové spojení pro venkovské základnové stanice a nouzovou komunikaci, a zajišťuje, aby konektivita byla univerzální službou.

## Klíčové vlastnosti

- Provoz satelitních konstelací (GEO, MEO, LEO) pro globální pokrytí
- Integrace se sítěmi 3GPP Core prostřednictvím standardizovaných rozhraní (N2, N3)
- Podpora transparentních i regenerativních architektur satelitní užitečné zátěže
- Implementace adaptací specifických pro NTN pro správu zpoždění a mobility
- Zajištění kontinuity služeb mezi terestriálním a satelitním přístupem
- Umožnění služeb přímo do zařízení a IoT v neobsluhovaných oblastech

## Definující specifikace

- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TR 28.844** (Rel-18) — Technical Report on Charging Aspects of Satellite in 5GS
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity

---

📖 **Anglický originál a plná specifikace:** [SSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssp/)
