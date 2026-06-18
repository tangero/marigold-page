---
slug: "lwa"
url: "/mobilnisite/slovnik/lwa/"
type: "slovnik"
title: "LWA – LTE-WLAN Radio Level Aggregation"
date: 2025-01-01
abbr: "LWA"
fullName: "LTE-WLAN Radio Level Aggregation"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lwa/"
summary: "Funkce 3GPP zavedená v Release 13, která umožňuje agregaci rádiových zdrojů LTE a Wi-Fi na rádiové úrovni. Uživatelskému zařízení (UE) umožňuje současně přijímat data přes LTE i WLAN spojení, řízené L"
---

LWA je funkce 3GPP Release 13 pro agregaci na rádiové úrovni zdrojů LTE a Wi-Fi, řízená základnovou stanicí LTE, umožňující současný příjem dat přes obě rádiová spojení za účelem zvýšení propustnosti a efektivity.

## Popis

LTE-WLAN Radio Level Aggregation (LWA) je standardizační funkce 3GPP, která integruje přístupovou technologii Wi-Fi ([WLAN](/mobilnisite/slovnik/wlan/)) jako komplementární rádiový zdroj pod kontrolou LTE evolved NodeB ([eNB](/mobilnisite/slovnik/enb/)). Zavedená v Release 13 umožňuje LWA agregaci nosných LTE a WLAN na vrstvě Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), což umožňuje rozdělení a souběžný přenos dat přes obě rádiová rozhraní k jednomu uživatelskému zařízení (UE). K této agregaci dochází na rádiové úrovni, což znamená, že eNB přímo spravuje zdroje přístupového bodu WLAN pro doručování dat, na rozdíl od řešení odlehčování na vyšších vrstvách.

Z architektonického hlediska LWA zahrnuje několik klíčových síťových prvků. LTE eNB funguje jako hlavní uzel, který řídí jak své vlastní rádiové zdroje LTE, tak přidružené přístupové body WLAN ([AP](/mobilnisite/slovnik/ap/)). Přístupový bod WLAN může být buď společný s eNB (integrovaný scénář), nebo připojený přes standardizované rozhraní (nespolečný scénář). Pro nespolu umístěné nasazení komunikuje eNB s uzlem WLAN Termination ([WT](/mobilnisite/slovnik/wt/)) přes rozhraní Xw, které přenáší řídicí zprávy (Xw-C) a datové pakety uživatelské roviny (Xw-U). UE musí podporovat LWA schopnosti, včetně duální konektivity k LTE a WLAN, a implementovat potřebné úpravy protokolového zásobníku pro zvládnutí agregace PDCP.

Během provozu proces LWA začíná tím, že se eNB na základě rádiových podmínek, vytížení a schopností UE rozhodne aktivovat LWA pro dané UE. eNB nakonfiguruje UE pomocí parametrů WLAN (např. [SSID](/mobilnisite/slovnik/ssid/), bezpečnostní přihlašovací údaje) prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). Po připojení vrstva PDCP eNB rozdělí datový tok: některé PDCP Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) jsou odeslány přes rádiový bearer LTE, zatímco jiné jsou předány přístupovému bodu WLAN (přes WT, pokud je přítomen) pro přenos přes Wi-Fi. UE přijímá pakety z obou spojů, znovu je sestavuje na vrstvě PDCP a doručuje je ve správném pořadí vyšším vrstvám. eNB provádí plánování, řízení toku a přizpůsobování spojení na obou spojích za účelem optimalizace výkonu.

Úlohou LWA v síti je zvýšit uživatelské přenosové rychlosti a kapacitu sítě využitím nelicencovaného spektra (Wi-Fi) spolu s licencovaným spektrem LTE. Poskytuje bezproblémový zážitek z agregace řízený mobilní sítí, což zajišťuje efektivní využití zdrojů a podporu mobility. LWA se liší od agregace LTE-WLAN na IP vrstvě (LWIP) a od integrace LTE-WLAN na rádiové úrovni s IPsec tunelem (LWAAP), protože nabízí různé úrovně integrace. Její specifikace pokrývá více 3GPP dokumentů zahrnujících architekturu, procedury a rozhraní, což zajišťuje interoperabilitu mezi ekosystémy LTE a Wi-Fi.

## K čemu slouží

LWA byla vytvořena, aby řešila rostoucí poptávku po kapacitě mobilních dat a nedostatečné využití dostupných Wi-Fi sítí. Před LWA bylo Wi-Fi typicky používáno jako samostatná přístupová síť s jednoduchým odlehčováním (např. na základě mobility IP toků), což postrádalo těsnou integraci s mobilními sítěmi a vedlo k neoptimálnímu řízení zdrojů a uživatelskému zážitku. Operátoři usilovali o využití hojného nelicencovaného spektra a stávající infrastruktury Wi-Fi pro rozšíření kapacity LTE bez nutnosti získání dalšího licencovaného spektra, které je drahé a nedostatkové.

Hlavní problémy, které LWA řeší, zahrnují zlepšení špičkové propustnosti pro uživatele, vyvažování zatížení mezi LTE a WLAN a poskytnutí bezproblémové agregace pod kontrolou sítě. Agregací na rádiové úrovni umožňuje LWA dynamičtější a efektivnější využití obou spojů ve srovnání s řešeními na vyšších vrstvách, přičemž eNB činí rozhodnutí o plánování v reálném čase. Tato integrace také zachovává rámce kvality služeb (QoS) a zabezpečení mobilní sítě přes Wi-Fi, čímž řeší omezení samostatného Wi-Fi, kterému chybí garantovaná QoS a centralizovaná správa.

Historicky byla LWA součástí širšího úsilí 3GPP o integraci WLAN do mobilního ekosystému, které začalo těsnějším propojením v dřívějších release. Release 13 představoval významný krok s agregací na rádiové úrovni, motivovaný úspěchem agregace nosných v LTE a potřebou podobné agregace více RAT (Radio Access Technology). Umožnil operátorům efektivněji nasazovat heterogenní sítě, kombinující pokrytí a spolehlivost LTE s vysokou kapacitou a nízkou cenou Wi-Fi, což v konečném důsledku zlepšilo celkový výkon sítě a spokojenost uživatelů v hustých městských prostředích.

## Klíčové vlastnosti

- Agregace na rádiové úrovni na vrstvě PDCP mezi LTE a WLAN
- Plánování a řízení zdrojů napříč oběma spoji řízené eNB
- Podpora společného i nespolu umístěného nasazení přístupového bodu WLAN
- Standardizované rozhraní Xw pro komunikaci mezi eNB a WLAN Termination (WT)
- Bezproblémová mobilita a kontinuita relace pro agregované bearery
- Zvýšená propustnost a kapacita využitím nelicencovaného Wi-Fi spektra

## Související pojmy

- [LWIP – LTE WLAN Radio Level Integration with IPsec Tunnel](/mobilnisite/slovnik/lwip/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.729** (Rel-15) — Unlicensed Spectrum Offloading System Enhancements
- **TS 29.272** (Rel-19) — Diameter Interfaces for MME/SGSN
- **TS 32.868** (Rel-15) — OAM aspects of LTE-WLAN integration (LWA/LWIP)
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.463** (Rel-19) — XwAP Protocol Specification
- **TS 36.464** (Rel-19) — Xw Interface User Plane Protocol
- **TS 36.465** (Rel-19) — Xw User Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [LWA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwa/)
