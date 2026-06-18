---
slug: "pna"
url: "/mobilnisite/slovnik/pna/"
type: "slovnik"
title: "PNA – Presence Network Architecture"
date: 2025-01-01
abbr: "PNA"
fullName: "Presence Network Architecture"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pna/"
summary: "Standardizovaná architektura 3GPP pro správu a distribuci informací o přítomnosti, které udávají dostupnost, ochotu a schopnost uživatele komunikovat. Definuje funkční entity jako Presence Server a Wa"
---

PNA je standardizovaná architektura 3GPP pro správu a distribuci informací o přítomnosti uživatele, jako je dostupnost a ochota komunikovat, která definuje funkční entity umožňující služby jako instant messaging.

## Popis

Presence Network Architecture (PNA) je rámec specifikovaný 3GPP pro službu přítomnosti, což je klíčový prvek pro rich komunikaci. Informace o přítomnosti jsou dynamická data popisující komunikační stav prezentující entity (např. uživatele nebo služby). To zahrnuje dostupnost (online/offline), komunikační prostředky (hlas, video, zasílání zpráv), ochotu komunikovat, aktuální činnost a polohu (je-li povolena). PNA definuje logické entity, referenční body a procedury pro sběr, zpracování, ukládání a distribuci těchto informací autorizovaným konzumentům, známým jako pozorovatelé (watchers).

Architektura je v zásadě založena na modelu klient-server a je hluboce integrována s IP Multimedia Subsystem (IMS). Mezi klíčové funkční entity patří Presence Server ([PS](/mobilnisite/slovnik/ps/)), což je centrální úložiště a zpracovatelský engine pro informace o přítomnosti. Přijímá aktualizace publikací od Presence User Agents ([PUA](/mobilnisite/slovnik/pua/)) asociovaných s zařízeními nebo službami prezentující entity. PS autentizuje publikace, uplatňuje autorizační politiky pro odběry a generuje složený pohled na přítomnost agregací dat z více PUA. Poté upozorní přihlášené pozorovatele (prostřednictvím jejich Presence User Agents) na jakékoli změny. Resource List Server ([RLS](/mobilnisite/slovnik/rls/)) je optimalizační entita, která umožňuje pozorovateli přihlásit se k odběru seznamu prezentujících entit („buddy list“) jediným odběrem, čímž se snižuje signalizační zátěž.

Jak to funguje: Zařízení uživatele (PUA) publikuje svůj lokální stav (např. „mobilní telefon, registrovaný, ochotný přijímat hlas“) na Presence Server prostřednictvím jádra IMS. PS agreguje tyto informace s publikacemi z dalších zařízení uživatele (laptop, tablet) a vytvoří tak jednotný stav přítomnosti. Když jiný uživatel (pozorovatel) chce tento stav vidět, jeho klient se přihlásí k odběru informací o přítomnosti dané prezentující entity. PS zkontroluje autorizační pravidla definovaná prezentující entitou a, je-li to povoleno, odešle oznámení obsahující aktuální dokument o přítomnosti (typicky ve formátu Presence Information Data Format - [PIDF](/mobilnisite/slovnik/pidf/)). Celý tento proces používá pro signalizaci protokol [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), konkrétně metody SIP PUBLISH, SUBSCRIBE a NOTIFY, což z něj činí nativní aplikaci IMS.

## K čemu slouží

PNA byla vyvinuta za účelem standardizace a škálování služby přítomnosti, která byla zpopularizována internetovými aplikacemi pro instant messaging, ale postrádala interoperabilitu a spolehlivost na úrovni operátora (carrier-grade). Proprietární systémy přítomnosti vytvářely uzavřené ekosystémy. 3GPP uznala přítomnost za základní stavební kánek pro služby telekomunikací nové generace, nezbytný pro umožnění inteligentních komunikačních voleb (např. zjištění, zda je někdo zaneprázdněn, před voláním) a pro obohacení služeb, jako jsou hlasové hovory, o kontext.

Její vytvoření řešilo omezení ad-hoc implementací tím, že poskytlo robustní, bezpečnou a škálovatelnou architekturu využívající řídicí rovinu IMS. To umožnilo operátorům mobilních sítí nabízet přítomnost jako standardizovanou, zpoplatnitelnou službu se zaručenou kvalitou a integrovanou správu účastníků. Řešila problémy fragmentace, zabezpečení (prostřednictvím autentizace a autorizace IMS) a efektivity sítě (prostřednictvím optimalizací jako [RLS](/mobilnisite/slovnik/rls/)). PNA umožnila širokou škálu služeb nad rámec jednoduchého stavu v chatu, včetně služeb síťového adresáře s přítomností, obohaceného směrování hovorů na základě dostupnosti volaného a integrace s multimediální telefonii, čímž položila základy pro Rich Communication Services ([RCS](/mobilnisite/slovnik/rcs/)).

## Klíčové vlastnosti

- Centralizovaný Presence Server pro agregaci, ukládání a distribuci dat o přítomnosti
- Podpora více Presence User Agents (PUA) na jednu prezentující entitu pro agregaci stavu zařízení
- Resource List Server (RLS) pro efektivní odběr seznamů přítomnosti (buddy listů)
- Využívá SIP (PUBLISH, SUBSCRIBE, NOTIFY) jako základní signalizační protokol v rámci IMS
- Definuje komplexní autorizační politiky umožňující prezentujícím entitám kontrolovat, kdo jaké informace vidí
- Standardizovaný datový model přítomnosti využívající formáty jako PIDF (Presence Information Data Format) a RPID (Rich Presence Information Data)

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 29.234** (Rel-11) — WLAN-3GPP Interworking Stage-3 Protocol
- **TS 32.409** (Rel-19) — IMS Performance Management Measurements
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [PNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/pna/)
