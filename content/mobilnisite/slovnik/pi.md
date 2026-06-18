---
slug: "pi"
url: "/mobilnisite/slovnik/pi/"
type: "slovnik"
title: "PI – Paging Indicator"
date: 2026-01-01
abbr: "PI"
fullName: "Paging Indicator"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pi/"
summary: "Hodnota vypočítaná vyššími vrstvami, která označuje pagingové příležitosti (paging occasions) pro UE. Umožňuje efektivní úsporu energie tím, že UEs monitorují pouze specifické podrámce pro pagingové z"
---

PI je hodnota vypočítaná vyššími vrstvami, která označuje konkrétní pagingové příležitosti (paging occasions) pro UE, což umožňuje efektivní úsporu energie tím, že UE monitoruje pouze určené podrámce (subframes) pro pagingové zprávy.

## Popis

Paging Indicator (PI) je základní mechanismus v rádiové přístupové síti 3GPP, konkrétně v kontextu pagingových procedur pro uživatelské zařízení (UE) v klidovém nebo neaktivním stavu. Funguje jako vypočítaná hodnota odvozená z parametrů vyšších vrstev, jako je mezinárodní identifikace mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) UE a čísla systémových rámců, aby určila přesné pagingové příležitosti (paging occasions), kdy se musí UE probudit a naslouchat pagingovým zprávám na pagingovém kanálu ([PCH](/mobilnisite/slovnik/pch-text-pch/)). PI se používá k mapování UE na specifické Paging Indicator Channels ([PICH](/mobilnisite/slovnik/pich/)) v UMTS nebo Paging Occasions ([PO](/mobilnisite/slovnik/po/)) a Paging Frames ([PF](/mobilnisite/slovnik/pf/)) v LTE a NR, což zajišťuje, že pagingové zprávy jsou vysílány pouze v předem stanovených intervalech, a tím efektivně organizuje pagingový provoz v síti.

Architektonicky je PI generován vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) sítě nebo vyšší vrstvou na základě algoritmů definovaných ve specifikacích 3GPP. V UMTS je PI asociován s PICH, fyzickým kanálem, který přenáší pagingové indikátory pro upozornění UE. UE vypočítá svůj vlastní PI pomocí stejného algoritmu a monitoruje odpovídající podrámec PICH. Pokud je indikátor nastaven, UE následně dekóduje přidružený [PCH](/mobilnisite/slovnik/pch/) pro vlastní pagingovou zprávu. V LTE a 5G NR se koncept vyvíjí v Paging Occasions a Paging Frames, kde výpočet podobný PI určuje konkrétní podrámec a rámec pro paging, integruje se s cykly nespojitého příjmu ([DRX](/mobilnisite/slovnik/drx/)) a dále optimalizuje úsporu energie.

Role PI je klíčová pro správu mobility a navazování spojení. Umožňuje síti kontaktovat UE pro příchozí hovory, SMS nebo datové relace bez nutnosti, aby UE nepřetržitě monitorovalo kanály, čímž šetří životnost baterie. Výpočet PI zajišťuje rovnoměrné rozložení UE napříč pagingovými zdroji, předchází zahlcení a umožňuje škálovatelný paging ve velkých sítích. Jeho implementace je standardizována napříč releasy, s vylepšeními v pozdějších verzích pro podporu nových stavů, jako je RRC_INACTIVE v 5G, kde jsou pagingové mechanismy rozšířeny pro efektivní přechody stavů a efektivitu sítě.

## K čemu slouží

Paging Indicator byl zaveden, aby řešil výzvu efektivního upozorňování klidových UE na příchozí komunikaci při minimalizaci jejich spotřeby energie. V raných buněčných systémech musela UE často naslouchat pagingovým signálům, což vedlo k vysokému vybíjení baterie. Mechanismus PI, zavedený v 3GPP R99, poskytl strukturovaný způsob určení konkrétních pagingových okamžiků, což umožnilo UE spát po většinu času a probouzet se pouze ve vypočtených intervalech. Tím byla vyřešena problematika nadměrného energetického využití v mobilních zařízeních, což bylo klíčové omezení v předchozích přístupech, jako je neustálé monitorování nebo jednoduché periodické pagingování.

Historicky, jak se sítě vyvíjely od 2G k 3G s UMTS, rostla potřeba sofistikovanějšího pagingu kvůli zvýšené hustotě uživatelů a datovým službám. PI umožnil deterministické pagingové příležitosti založené na identitě UE, čímž se snížilo riziko kolizí a zlepšila kapacita sítě. Také usnadnil implementaci nespojitého příjmu (DRX), funkce pro úsporu energie, která závisí na přesném načasování pagingu. Bez PI by se sítě potýkaly s neefektivní signalizací, vyšší latencí při kontaktování UE a sníženou životností baterie, což by ovlivnilo uživatelský zážitek a škálovatelnost sítě v éře mobilního broadbandu a nasazení IoT.

V pozdějších releasech koncept PI podpořil vylepšení pro LTE a 5G NR, kde se efektivita pagingu stala ještě kritičtější s masivním IoT a zařízeními s nízkou spotřebou. Řešil omezení dřívějších pagingových metod tím, že poskytl standardizované, škálovatelné řešení, které se integruje s pokročilými RRC stavy a síťovým slicingem, zajišťuje zpětnou kompatibilitu a budoucí flexibilitu pro vyvíjející se telekomunikační standardy.

## Klíčové vlastnosti

- Deterministický výpočet pagingové příležitosti (paging occasion) založený na identitě UE
- Integrace s Paging Indicator Channel (PICH) v UMTS
- Podpora cyklů nespojitého příjmu (DRX)
- Snížení spotřeby energie UE prostřednictvím plánovaného monitorování
- Rovnoměrné rozložení pagingové zátěže napříč síťovými zdroji
- Kompatibilita s více RRC stavy včetně klidového (idle) a neaktivního (inactive)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 25.202** (Rel-19) — 7.68Mcps TDD Option Technical Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.367** (Rel-19) — Home NodeB Mobility Procedures
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [PI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pi/)
