---
slug: "mpea"
url: "/mobilnisite/slovnik/mpea/"
type: "slovnik"
title: "MPEA – MCPTT Private Emergency Alert"
date: 2025-01-01
abbr: "MPEA"
fullName: "MCPTT Private Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpea/"
summary: "MCPTT Private Emergency Alert (MPEA) je klíčová funkce v rámci služby Mission Critical Push-To-Talk (MCPTT), která autorizovanému uživateli umožňuje odeslat vysoce prioritní soukromé upozornění konkré"
---

MPEA je vysoce prioritní soukromá funkce upozornění v rámci služby MCPTT, která autorizovanému uživateli umožňuje odeslat diskrétní, naléhavé oznámení konkrétní osobě nebo předem definované skupině.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Private Emergency Alert (MPEA) je specializovaná servisní komponenta definovaná v rámci sady 3GPP Mission Critical Services, konkrétně pro aplikaci MCPTT. Na rozdíl od běžného skupinového nouzového upozornění, které je vysíláno všem členům talkgroup, je Private Emergency Alert cílená, bod-bod nebo bod-více bodů naléhavá komunikace. Architektura MPEA využívá základní rámec služby MCPTT, který zahrnuje MCPTT klienta na uživatelském zařízení, MCPTT aplikační server a využívá 3GPP IP Multimedia Subsystem (IMS) core pro řízení relace a autentizaci. Upozornění je iniciováno autorizovaným uživatelem MCPTT prostřednictvím jeho klienta, který odešle specifickou žádost SIP MESSAGE nebo využije vyhrazené nouzové procedury k MCPTT serveru.

MCPTT server po přijetí žádosti MPEA ověří autorizaci odesílatele a upozornění zpracuje. Následně směruje upozornění k zamýšlenému příjemci (příjemcům) na základě soukré uživatelské identity nebo identity soukromé skupiny. Signalizace zajišťuje doručení upozornění s nejvyšší prioritou, v případě potřeby s přednostním přerušením jiného provozu. Klíčové specifikace protokolů jsou pokryty v 24.379 (řízení hovorů MCPTT), zatímco aspekty testování shody jsou podrobně popsány v 36.579 a 37.579. MCPTT klient příjemce po přijetí musí poskytnout jednoznačnou a intruzivní indikaci – například odlišný zvuk, trvalé vizuální upozornění a vibrace – aby zajistil okamžitou pozornost, a to i v případě, že je zařízení v tichém režimu nebo je zapojeno do jiného hovoru.

Princip fungování zahrnuje definovanou strukturu zprávy obsahující typ upozornění, identitu odesílatele, časovou značku a volitelné informace o poloze. Server může také zaznamenávat upozornění pro účely auditních stop. Služba zajišťuje soukromí tím, že omezuje zveřejnění obsahu upozornění a seznamu příjemců neoprávněným stranám. Její role v síti spočívá v poskytnutí bezpečného, spolehlivého a okamžitého kanálu pro životně důležitá oznámení v rámci profesionálních organizací, jako jsou policie, hasičské sbory a průmyslové týmy, kde standardní skupinová komunikace nemusí být pro citlivé nouzové situace vhodná.

## K čemu slouží

MPEA byla představena ve 3GPP Release 13 jako součást širší standardizace služeb Mission Critical Services přes LTE (a později 5G). Před její standardizací měly profesionální mobilní rádiové systémy (PMR), jako TETRA nebo P25, proprietární nouzové funkce, ale interoperabilita a integrace širokopásmových služeb byla omezená. Motivace pro MPEA vycházela z operačních potřeb orgánů veřejné bezpečnosti, kde existují scénáře vyžadující diskrétní, vysoce prioritní upozornění konkrétnímu veliteli nebo specializovanému týmu bez vyvolání paniky nebo prozrazení taktických informací širší skupině.

Řeší omezení plošného skupinového nouzového volání, které, ačkoli je účinné pro obecná upozornění, není vhodné pro situace jako jsou utajované operace, osobní tísně nebo oznámení konkrétnímu zdravotníkovi o zraněném. MPEA tento problém řeší poskytnutím cílené, soukromé, ale vysoce prioritní komunikační cesty v rámci standardizovaného rámce [MCPTT](/mobilnisite/slovnik/mcptt/). Její vytvoření bylo hnací silou uživatelských požadavků od organizací veřejné bezpečnosti po celém světě, aby bylo zajištěno, že kritická komunikace založená na LTE/5G může dosáhnout nebo překonat funkční schopnosti starších úzkopásmových systémů, a tím usnadnit přechod na širokopásmové sítě PPDR (Public Protection and Disaster Relief).

## Klíčové vlastnosti

- Cílené doručení upozornění jednotlivým uživatelům nebo soukromým skupinám
- Signalizace s nejvyšší prioritou s přednostním přerušením běžného provozu MCPTT
- Zaručená intruzivní uživatelská notifikace (zvuková, vizuální, vibrace) na zařízení příjemce
- Integrace s autentizačními a autorizačními mechanismy MCPTT
- Podpora zahrnutí informací o poloze a časové značce do upozornění
- Auditní zaznamenávání na MCPTT aplikačním serveru pro účely odpovědnosti

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MPEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpea/)
