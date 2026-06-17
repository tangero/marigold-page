---
slug: "esc"
url: "/mobilnisite/slovnik/esc/"
type: "slovnik"
title: "ESC – Event State Compositor"
date: 2025-01-01
abbr: "ESC"
fullName: "Event State Compositor"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esc/"
summary: "Funkční entita v rámci IP multimediálního podsystému (IMS), která spravuje a skládá informace o stavu událostí pro služby přítomnosti a další služby založené na událostech. Agreguje informace z více z"
---

ESC je funkční entita v IP multimediální podsystému (IMS), která spravuje a skládá informace o stavu událostí agregací dat z více zdrojů za účelem vytvoření uceleného pohledu na stav uživatele pro pozorovatele.

## Popis

Event State Compositor (ESC) je základní funkce aplikačního serveru v rámci servisní architektury IP multimediálního podsystému (IMS), standardizovaná pro podporu služeb upozorňování na události, především služby Přítomnosti. Funguje jako logický zprostředkovatel mezi publikujícími entitami (entity generující informace o stavu, jako je uživatelské zařízení - UE) a pozorovateli událostí (odběratelé požadující tyto informace). Primární rolí ESC je shromažďovat, zpracovávat a skládat nezpracované informace o stavu událostí z jednoho či více zdrojů do jediného, autoritativního složeného stavu události, který je následně distribuován autorizovaným pozorovatelům.

Z architektonického hlediska je ESC typicky implementován jako součást Presence Serveru nebo vyhrazeného aplikačního serveru ([AS](/mobilnisite/slovnik/as/)) v doméně IMS. Rozhraní využívá protokol Session Initiation Protocol (SIP) pro publikaci a odběr událostí, jak je definováno v RFC 3856 (Přítomnost) a RFC 6665 (SIP-Specific Event Notification). ESC přijímá požadavky PUBLISH obsahující dokumenty stavu události (např. ve formátu PIDF) od Presence User Agents (PUA), které mohou sídlit na uživatelském zařízení, síťové službě nebo jiných aplikacích. Každý PUA může publikovat pouze částečný pohled na celkový stav uživatele (např. stav zařízení, dostupnost z kalendáře, síťová registrace).

ESC funguje tak, že na tyto vstupy aplikuje sadu skládacích pravidel nebo politik. Tato pravidla určují, jak jsou konfliktní nebo doplňující se informace sloučeny. Například, pokud jeden PUA publikuje stav "dostupný" a druhý "na schůzce", skládací politika ESC může určit, že "na schůzce" má přednost, což vede ke složenému stavu "zaneprázdněn". Skladač spravuje stav pro každou prezentitu (entitu, jejíž přítomnost je hlášena). Generuje jediný, složený dokument stavu události, který představuje autoritativní pohled. Když se pozorovatel přihlásí k odběru stavu události prezentity, ESC funguje jako notifikátor, zasílá složený stav v NOTIFY zprávách a následné aktualizace při změně stavu.

Klíčové součásti logiky ESC zahrnují motor skládacích politik, funkci agregace stavu a správce odběrů/notifikací. Jeho role je zásadní pro vytvoření jednotného a smysluplného zážitku z přítomnosti z potenciálně různorodých a redundantních zdrojů dat. Přenesením složitého skládání stavu z koncových uživatelských zařízení a jeho centralizací v síti ESC zajišťuje konzistenci, snižuje signalizační režii a umožňuje pokročilé funkce služeb, jako jsou pohledy založené na rolích nebo filtrování stavu pro různé pozorovatele.

## K čemu slouží

ESC byl vytvořen k řešení základního problému raných implementací služeb přítomnosti: jak spravovat více, potenciálně konfliktních zdrojů informací o přítomnosti pro jednoho uživatele. Bez skladače by se pozorovatelé museli přihlásit k odběru každého zdroje zvlášť a lokálně provádět složitou logiku k odvození skutečné dostupnosti uživatele, což by vedlo k nekonzistentním zážitkům, zvýšené signalizaci a omezeným možnostem služeb.

Historicky, jak se služby přítomnosti založené na IMS a SIP vyvíjely od Rel-6 dále, se koncept síťového skladače stal nezbytným pro škálovatelnou a pokročilou přítomnost. Předchozí přístupy nebo jednodušší modely nemohly efektivně zvládat scénáře, kdy uživatel měl více zařízení (telefon, laptop, tablet) nebo kdy informace o přítomnosti pocházely jak ze senzorů zařízení, tak z externích aplikací (jako jsou kalendářové systémy). ESC poskytuje standardizované, na síť zaměřené řešení pro agregaci těchto informací.

Jeho vytvoření bylo motivováno potřebou umožnit sofistikované komunikační služby, jako je "Find Me/Follow Me", pokročilé instant messagingy a podpůrné funkce pro pokročilé komunikační sady (RCS). Skládáním jediného, autoritativního stavu umožňuje ESC implementaci komplexních obchodních pravidel (např. "nerušit během schůzek") a ochrany soukromí na síťové úrovni. Abstrahuje složitost správy stavu z více zdrojů jak pro publikující klienty, tak pro pozorující klienty, což je klíčový požadavek pro interoperabilní, operátorské služby přítomnosti.

## Klíčové vlastnosti

- Agreguje publikace stavu událostí z více Presence User Agents (PUA)
- Aplikuje konfigurovatelné skládací politiky pro řešení konfliktů a slučování stavů
- Generuje jediný, autoritativní složený stav události pro prezentitu
- Funguje jako notifikátor pro požadavky SIP SUBSCRIBE od pozorovatelů
- Spravuje autorizaci odběrů a filtrování stavu na základě identity pozorovatele
- Centralizuje složitou logiku, aby zajistila konzistentní pohled na stav pro všechny pozorovatele

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem

---

📖 **Anglický originál a plná specifikace:** [ESC na 3GPP Explorer](https://3gpp-explorer.com/glossary/esc/)
