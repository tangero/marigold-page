---
slug: "mea"
url: "/mobilnisite/slovnik/mea/"
type: "slovnik"
title: "MEA – MCPTT Emergency Alert"
date: 2025-01-01
abbr: "MEA"
fullName: "MCPTT Emergency Alert"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mea/"
summary: "Kritická funkce v rámci služby Mission Critical Push-To-Talk (MCPTT), která autorizovanému uživateli umožňuje zahájit celosíťové upozornění vysoké priority během mimořádné události. Zajišťuje rychlé a"
---

MEA je klíčová funkce služby MCPTT, která autorizovanému uživateli umožňuje zahájit celosíťové nouzové upozornění vysoké priority pro rychlé rozšíření informací mezi všechny relevantní pracovníky.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Emergency Alert (MEA) je specializovaná služba definovaná v rámci specifikací 3GPP pro služby Mission Critical Services ([MCS](/mobilnisite/slovnik/mcs/)), konkrétně v rámci Mission Critical Push-To-Talk. Jedná se o mechanismus pro zahájení nouzového upozornění, které je šířeno s nejvyšší prioritou napříč systémem MCPTT. Když uživatel spustí MEA, vygeneruje se upozornění, které je distribuováno předdefinované skupině nebo všem uživatelům v určitém kontextu, například všem členům týmu pro mimořádné události nebo celé organizaci. Upozornění nese metadata včetně typu upozornění, polohy iniciujícího uživatele, časového razítka a jedinečného identifikátoru.

Z architektonického hlediska se funkce MEA týká několika komponent systému MCPTT. Klient MCPTT na zařízení uživatele poskytuje rozhraní pro spuštění upozornění. Po zahájení odešle klient přes signalizační cestu [MC](/mobilnisite/slovnik/mc/) služeb zprávu MCPTT EMERGENCY ALERT request na server MCPTT. Server MCPTT, který spravuje skupinovou komunikaci a servisní logiku, žádost ověří, uplatní případné nastavené politiky (např. ověření autorizace uživatele pro odesílání upozornění) a následně orchestruje distribuci. Distribuce obvykle probíhá kombinací navázání skupinového hovoru MCPTT s nouzovou prioritou a/nebo prostřednictvím samostatného signalizačního kanálu pro upozornění, aby bylo zajištěno doručení i v případě, že hovor nelze navázat. Server může také komunikovat s dalšími entitami MC služeb, jako je MC Gateway, pro propojení s dalšími systémy upozornění.

Jak to funguje, zahrnuje prioritní přidělování prostředků. Síť zachází se signalizací MEA a přidruženým médiem (jako je tón upozornění nebo hlasové oznámení) s přednostní (pre-emptivní) prioritou. To znamená, že síť využívá mechanismy Quality of Service (QoS), jako je přidělování přenosů se zaručenou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) s vysokou prioritou pro přidělení a udržení ([ARP](/mobilnisite/slovnik/arp/)), aby zajistila, že upozornění obchází přetížení. Upozornění je doručeno na cílové uživatelské zařízení, které pak poskytuje výrazné indikace – jako jsou specifické vyzváněcí tóny, vyskakovací okna na obrazovce a vibrace – aby upoutalo okamžitou pozornost. Systém také podporuje potvrzení přijetí upozornění, což příjemcům umožňuje potvrdit jeho doručení, a udržuje záznamy pro audit a analýzu po události.

## K čemu slouží

MEA byla vytvořena, aby splňovala přísné požadavky na spolehlivost a bezprostřednost u organizací veřejné bezpečnosti a pro služby kritické pro plnění mise. Řeší problém pomalého nebo nespolehlivého nouzového oznamování v tradičních systémech skupinové komunikace. Ve vysoce rizikových scénářích, jako jsou přírodní katastrofy, teroristické incidenty nebo průmyslové havárie, může schopnost okamžitě upozornit všechny relevantní pracovníky zachránit životy a koordinovat účinnou reakci.

Motivace vychází z omezení dřívějších systémů profesionální mobilní rádiové komunikace (PMR) a komerčních buněčných služeb, kterým chybělo standardizované, prioritní a globálně interoperabilní nouzové upozorňování v kontextu skupinové komunikace. Práce 3GPP na službách Mission Critical Services přes LTE (počínaje Release 13) měla za cíl poskytnout kritické funkce podporované širokopásmovým přenosem. MEA je přímou odpovědí na požadavky uživatelů z agentur veřejné bezpečnosti na garantovaný mechanismus upozornění vysoké priority, který funguje přes komerční síťovou infrastrukturu a poskytuje lepší alternativu k sirénám, pagerům nebo neprioritním SMS upozorněním.

## Klíčové vlastnosti

- Spuštění a síťové šíření s vysokou, přednostní (pre-emptivní) prioritou
- Konfigurovatelná distribuce upozornění jednotlivcům, skupinám nebo všem uživatelům
- Obsahuje kritická metadata (poloha, typ upozornění, ID iniciátora)
- Zaručené doručení pomocí prioritního QoS (GBR přenosy s vysokým ARP)
- Výrazné uživatelské upozornění (zvukové, vizuální, vibrace) na zařízeních příjemců
- Podpora pro potvrzení přijetí upozornění a auditní logování

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mea/)
