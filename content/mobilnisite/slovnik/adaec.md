---
slug: "adaec"
url: "/mobilnisite/slovnik/adaec/"
type: "slovnik"
title: "ADAEC – Application Data Analytics Enablement Client"
date: 2026-01-01
abbr: "ADAEC"
fullName: "Application Data Analytics Enablement Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/adaec/"
summary: "Application Data Analytics Enablement Client (ADAEC) je funkční entita zavedená ve specifikaci 3GPP Release 18, která sídlí v uživatelském zařízení (UE). Jejím hlavním úkolem je usnadňovat sběr, zprac"
---

ADAEC je klientská funkční entita v uživatelském zařízení (UE), která sbírá, zpracovává a hlásí data aplikační vrstvy síťovému ADAES, aby umožnila analýzy pro optimalizaci výkonu, uživatelského zážitku a služeb.

## Popis

Application Data Analytics Enablement Client (ADAEC) je standardizovaná klientská funkce definovaná v architektuře 3GPP, speciálně navržená pro provoz v uživatelském zařízení (UE). Působí jako koncový bod pro sběr analytických dat aplikací v systému 5G a dalších generacích. ADAEC je zodpovědný za rozhraní s aplikacemi běžícími na UE, shromažďování relevantních analytických dat podle definice analytických předplatných nebo konfigurací poskytovaných sítí a hlášení těchto dat Application Data Analytics Enablement Serveru (ADAES) umístěnému v síti. Jeho činnost se řídí politikami a instrukcemi přijatými od ADAES, což zajišťuje, že sběr dat je v souladu s ochranou soukromí, efektivní z hlediska zdrojů a sladěný s analytickými požadavky autorizovaných subjektů.

Z architektonického hlediska je ADAEC součástí frameworku Application Data Analytics Enablement, který zahrnuje ADAES v síti. ADAEC komunikuje s ADAES přes rozhraní Nadae, jak je specifikováno v 3GPP TS 24.559. Toto rozhraní podporuje procedury pro analytické předplatné, doručování konfigurace a hlášení analýz. Klíčové vnitřní komponenty ADAEC zahrnují funkci vynucování politik pro interpretaci a aplikaci pravidel sběru dat od ADAES, engine sběru dat, který komunikuje s aplikačními programovými rozhraními (API) nebo operačním systémem UE za účelem shromáždění specifikovaných metrik (např. latence aplikace, propustnost, míry chyb, události interakce uživatele), a hlášecí funkci, která formátuje a přenáší sebraná data na server.

Jak funguje: pracuje na základě modelu s předplatným. Spotřebitel analýz (např. síťový operátor, poskytovatel aplikace třetí strany) požaduje specifické analýzy přes ADAES. ADAES poté zřídí odpovídající analytické předplatné cílovým ADAEC v UE. Předplatné zahrnuje typ analýzy, parametry sběru, podmínky hlášení (např. spouštěné událostí, periodické) a případná pravidla pro filtrování nebo agregaci dat. ADAEC po přijetí konfigurace zahájí monitorování specifikovaných aplikací a metrik. Zpracovává nezpracovaná data lokálně podle instrukcí – což může zahrnovat filtrování, agregaci nebo odvozování klíčových ukazatelů výkonu (KPI) – a poté odešle analytické hlášení ADAES, když jsou splněny podmínky pro hlášení. Tento klient-serverový model přesouvá část zpracování na okraj sítě (UE), čímž snižuje síťovou zátěž spojenou s přenosem nezpracovaných dat.

Jeho role v síti je klíčová pro umožnění automatizace s uzavřenou smyčkou a vylepšeného řízení kvality uživatelského zážitku (QoE). Tím, že ADAEC poskytuje detailní, na aplikaci specifická data z koncového uživatelského zařízení, zásobuje síťové analytické a AI/ML enginy klíčovým vstupem. Tato data lze použít pro mnoho účelů: diagnostiku problémů s výkonem aplikací, optimalizaci parametrů rádiové a jádrové sítě pro specifické služby (jako je streamování videa nebo hraní her), umožnění síťového vystavení kontextu aplikace autorizovaným třetím stranám a podpora nových obchodních modelů kolem smluv o úrovni služeb (SLA) a smluv o úrovni zážitku (ELA). ADAEC tedy mění UE z pasivního koncového bodu na aktivní zdroj inteligence pro síť.

## K čemu slouží

ADAEC byl vytvořen, aby řešil rostoucí potřebu detailních, na aplikaci zaměřených přehledů v mobilních sítích, které tradiční, na síť zaměřené čítače výkonu nemohou plně poskytnout. Před jeho standardizací bylo monitorování výkonu aplikací často dosahováno prostřednictvím nestandardizovaných proprietárních řešení – jako je hloubková inspekce paketů (DPI) v síti nebo SDK vestavěná do aplikací – která vyvolávala obavy o soukromí, byla neefektivní a postrádala interoperabilitu. DPI zápasí s šifrovaným provozem a poskytuje pouze pohled ze strany sítě, což postrádá skutečný uživatelsky vnímaný zážitek na zařízení. Proprietární SDK vytvářejí fragmentaci a zvyšují složitost vývoje aplikací. ADAEC standardizuje metodu sběru analýz zaměřenou na zařízení, respektující soukromí a vstřícnou k aplikacím.

Hlavní problém, který řeší, je absence standardizovaného, efektivního a bezpečného mechanismu pro sběr hodnotných analytických dat přímo z aplikační vrstvy na UE. Tato data jsou pro operátory a poskytovatele služeb zásadní k pochopení a optimalizaci skutečné kvality uživatelského zážitku (QoE) od konce ke konci. Motivací pro jeho vytvoření v Release 18 je evoluce směrem k 5G-Advanced a rostoucí důležitost vertikálních služeb (např. XR, cloud gaming, průmyslový IoT), které mají přísné a rozmanité požadavky na výkon. Optimalizace sítí pro tyto služby vyžaduje detailní znalost chování aplikací a interakce uživatele, což ADAEC umožňuje.

Dále ADAEC řeší omezení předchozích analytických frameworků 3GPP, jako jsou ty definované pro minimalizaci jízdních testů (MDT) nebo sběr měření kvality uživatelského zážitku (QoE), které byly více zaměřené na rádiové podmínky nebo specifické streamování médií. ADAEC poskytuje obecnější, flexibilnější a na aplikaci zaměřený framework. Je navržen s principy ochrany soukromí již při návrhu, protože klientská část na UE funguje pod explicitním souhlasem uživatele a síťovými politikami, což dává uživatelům větší kontrolu nad tím, jaká data jsou sdílena, ve srovnání s neprůhlednými síťovými sondovacími technikami. Jeho vytvoření bylo motivováno posunem průmyslu směrem k síťové automatizaci řízené daty, optimalizaci založené na AI/ML a potřebou podporovat nové obchodní modely, kde je výkon aplikace klíčovým diferenciátorem.

## Klíčové vlastnosti

- Standardizované klient-serverové rozhraní (Nadae) pro sběr analytických dat aplikací
- Řízení sběru a hlášení dat pomocí politik konfigurovatelných ze sítě (ADAES)
- Podpora různých typů analýz včetně výkonu aplikací, uživatelského zážitku a kontextu zařízení
- Možnosti lokálního zpracování na UE pro filtrování dat, agregaci a odvozování KPI
- Vynucování ochrany soukromí prostřednictvím mechanismů souhlasu uživatele a přístupu k datům založeného na předplatném
- Režimy hlášení spouštěné událostí a periodické pro flexibilní doručování dat

## Definující specifikace

- **TS 23.436** (Rel-20) — ADAEnabler Functional Architecture and Information Flows
- **TS 24.559** (Rel-19) — Application Data Analytics Enablement Services

---

📖 **Anglický originál a plná specifikace:** [ADAEC na 3GPP Explorer](https://3gpp-explorer.com/glossary/adaec/)
