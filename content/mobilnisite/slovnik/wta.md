---
slug: "wta"
url: "/mobilnisite/slovnik/wta/"
type: "slovnik"
title: "WTA – Wireless Telephony Applications"
date: 2025-01-01
abbr: "WTA"
fullName: "Wireless Telephony Applications"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wta/"
summary: "Framework pro vytváření aplikací zaměřených na telefonii na mobilních zařízeních, umožňující funkce jako řízení hovorů a zpracování síťových událostí. Byl klíčovou součástí raných platform mobilních s"
---

WTA je framework pro vytváření aplikací zaměřených na telefonii na mobilních zařízeních, umožňující funkce jako řízení hovorů a zpracování síťových událostí pro nabídku rozšířených služeb mimo základní hlasové hovory.

## Popis

Wireless Telephony Applications (WTA) je standardizovaný framework definovaný 3GPP, který rozšiřuje možnosti Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)) pro podporu funkcí specifických pro telefonii. Poskytuje sadu služeb a [API](/mobilnisite/slovnik/api/), které umožňují tvůrcům aplikací vytvářet programy schopné interagovat s telefonními funkcemi mobilní síťě. Architektura je postavena na WAP stacku, zavádějíc WTA User Agent na mobilním zařízení, který může provádět knihovny [WTAI](/mobilnisite/slovnik/wtai/) (Wireless Telephony Applications Interface). Tyto knihovny zpřístupňují síťové možnosti, jako například vytváření hovorů, vysílání [DTMF](/mobilnisite/slovnik/dtmf/) tónů, přístup k položkám telefonního seznamu a zpracování síťově iniciovaných událostí, jako příchozí hovory nebo zprávy.

Framework WTA funguje definováním zabezpečeného prostředí pro provádění, ve kterém mohou telefonní aplikace běžet. Obsahuje repository pro WTA služby, často hostované síťovým operátorem, ke kterému zařízení může přistupovat. Když uživatel interaguje s WTA aplikací, WTA User Agent zpracuje obsah [WML](/mobilnisite/slovnik/wml/) (Wireless Markup Language) a provede embedded volání funkcí WTAI. Tyto volání jsou pak přeloženy do nativních příkazů pro telefonní subsystém zařízení. Kritickou komponentou je WTA server, který může pushovat service indications nebo obsahové aktualizace do zařízení, umožňující síťově triggerované chování aplikace.

Role WTA byla překlenout rozdíl mezi základním WAP browsingem a inteligentními telefonními službami, vytvářejíc základní pilíř raných služeb s přidanou hodnotou. Umožnil vytváření aplikací podobných interaktivní hlasové odpovědi ([IVR](/mobilnisite/slovnik/ivr/)) s vizuálním interface, síťově based nástrojů pro řízení hovorů a integrace telefonních událostí do web-like obsahu. Framework obsahoval bezpečnostní mechanismy pro prevenci neautorizovaného přístupu k telefonním funkcím, zajišťující, že pouze důvěryhodné aplikace od operátora nebo schválených zdrojů mohou řídit kritické funkce zařízení. I když je většinou nahrazen modernými smartphone operačními systémy a rich communication API, WTA reprezentoval významný krok v učinění mobilní síťě programovatelnou a service-aware z pohledu aplikace.

## K čemu slouží

WTA byl vytvořen pro řešení potřeb standardizovaných, síťově aware telefonních aplikací v rané éře mobilních dat. Před jeho zavedením byly služby s přidanou hodnotou pro telefonii většinou proprietární, operator-specific a omezené na základní síťové funkce jako hlasová schránka nebo přesměrování hovorů. Vzestup [WAP](/mobilnisite/slovnik/wap/) pro mobilní internet browsing vytvořil příležitost, ale WAP samotný neměl direct hooks do základních telefonních funkcí telefonu. WTA to řešil poskytnutím uniformního interface pro aplikace pro interagování s telefonními subsystémy přes různých výrobců zařízení a síťových operátorů.

Motivace pocházela z touhy vytvořit živý ekosystém služeb rozšířených telefonii, jako například click-to-dial directories, vizuální řízení hovorů a síťově triggerované service alerts. Cílem bylo dát operátorům platformu pro nasazení a řízení pokročilých služeb bez závislosti na proprietárních [API](/mobilnisite/slovnik/api/) výrobců zařízení. Standardizací tohoto interface v rámci 3GPP a WAP Forum podnítil interoperabilitu a redukoval fragmentaci. Framework byl designován s ohledem na bezpečnost a síťovou integritu, zajišťující, že aplikace nemohou zneužívat telefonní resources, což byl kritický problém pro operátory řídící jejich infrastrukturu.

## Klíčové vlastnosti

- Standardizované API pro řízení hovorů (vytvořit, přijmout, odmítnout, ukončit hovory)
- Přístup k telefonním funkcím zařízení jako telefonní seznam a historie hovorů
- Zpracování síťově iniciovaných událostí (například notifikace příchozích hovorů)
- Integrace s WAP browsingem pro hybridní telefonně-webové aplikace
- Zabezpečené prostředí pro provádění s řízením přístupu k telefonním resources
- Podpora pro push service indications ze síťových serverů do zařízení

## Související pojmy

- [WTAI – Wireless Telephony Applications Interface](/mobilnisite/slovnik/wtai/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wta/)
