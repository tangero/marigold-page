---
slug: "glms"
url: "/mobilnisite/slovnik/glms/"
type: "slovnik"
title: "GLMS – Group and List Management Server"
date: 2025-01-01
abbr: "GLMS"
fullName: "Group and List Management Server"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/glms/"
summary: "GLMS je síťový prvek v subsystému IP multimédií (IMS), který spravuje definice skupin a uživatelské seznamy pro služby, jako je instant messaging a služba přítomnosti. Umožňuje uživatelům vytvářet, up"
---

GLMS je síťový prvek IMS, který spravuje definice skupin a uživatelské seznamy. Umožňuje uživatelům vytvářet, upravovat a ukládat skupiny kontaktů a autorizační seznamy pro služby, jako jsou zasílání zpráv a služba přítomnosti.

## Popis

Group and List Management Server (GLMS) je funkční entita v architektuře subsystému IP multimédií (IMS), definovaná ve specifikacích 3GPP. Je zodpovědná za ukládání a správu informací souvisejících se skupinami jménem uživatelů. Tyto informace se primárně skládají ze skupin (např. "pracovní kolegové" nebo "rodina") a seznamů (konkrétně autorizačních seznamů, které definují pravidla pro to, kdo může vidět informace o přítomnosti uživatele nebo mu posílat zprávy). GLMS poskytuje standardizované rozhraní, typicky založené na XML Configuration Access Protocol (XCAP), které umožňuje klientům IMS tyto data manipulovat. Když uživatel chce vytvořit novou skupinu kontaktů nebo upravit, kdo může vidět jeho stav online, jeho klientská aplikace odešle požadavek XCAP ([HTTP](/mobilnisite/slovnik/http/) PUT, GET, DELETE) na GLMS, který pak data uloží ve své interní databázi.

Architektura GLMS je navržena jako centralizované úložiště pro data spravovaná uživatelem, na která odkazují další aplikační servery IMS. Například Presence Server se dotáže GLMS, aby získal "autorizační seznam pro přítomnost" uživatele a určil, kterým pozorovatelům jsou povoleny aktualizace stavu přítomnosti. Podobně může Instant Messaging ([IM](/mobilnisite/slovnik/im/)) server využívat definice skupin uložené v GLMS pro správu chatovacích místností nebo distribučních seznamů. Server autentizuje požadavky pomocí identit předplatitele IMS (jako je Privátní uživatelská identita) a zajišťuje integritu a soukromí dat pro každého uživatele. Nespouští vlastní servisní logiku, ale poskytuje trvalé úložiště dat, které umožňuje personalizaci služeb a řízení přístupu.

Z pohledu síťové integrace je GLMS často implementován jako samostatný uzel nebo společně s dalšími aplikačními servery IMS. Komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) ohledně dat uživatelských profilů, ale je odlišný tím, že spravuje dynamický, uživateli vytvořený obsah, nikoli statické profily předplatného. Jeho role je klíčová pro služby zaměřené na uživatele, neboť dává předplatitelům možnost řídit své komunikační prostředí. Správa těchto dat prostřednictvím XCAP je v souladu s principem IMS využívat internetové protokoly, což usnadňuje interoperabilitu s klienty a službami mimo 3GPP.

## K čemu slouží

GLMS byl zaveden, aby vyřešil potřebu personalizace služeb a řízení přístupu spravovaného uživatelem v rámci vznikajícího subsystému IP multimédií (IMS). Před IMS měly mobilní služby, jako jsou SMS nebo [MMS](/mobilnisite/slovnik/mms/), pouze omezené možnosti pro definování složitých skupin kontaktů nebo podrobných pravidel sdílení. Jelikož IMS cílilo na poskytování služeb ve stylu internetu (přítomnost, instant messaging, konferenční hovory) s provozní spolehlivostí na úrovni operátora, stal se standardizovaný mechanismus pro správu dat stojících v základu těchto služeb nezbytným.

Vytvoření GLMS vyřešilo problém, kde a jak ukládat uživatelsky definovaná servisní data škálovatelným a interoperabilním způsobem. Bez něj by si každý aplikační server (např. pro přítomnost nebo zasílání zpráv) musel implementovat vlastní proprietární metodu ukládání uživatelských seznamů, což by vedlo k datovým izolátům, nekonzistenci a špatné uživatelské zkušenosti. GLMS poskytuje jednotné, síťové úložiště, které zajišťuje konzistentní uplatnění skupin kontaktů a pravidel soukromí uživatele napříč všemi IMS službami, které využívá. Toto oddělení správy dat od provádění služby je klíčovým architektonickým principem, který podporuje agilitu služeb a zjednodušuje vývoj nových skupinových aplikací.

## Klíčové vlastnosti

- Ukládá a spravuje uživatelsky definované skupiny kontaktů a autorizační seznamy (např. seznamy povolených/blokovaných pro přítomnost).
- Poskytuje standardizovaná rozhraní XCAP (XML Configuration Access Protocol) pro přístup klientů a manipulaci s daty.
- Integruje se s aplikačními servery IMS, jako jsou Presence Server a Instant Messaging Server, pro uplatňování uživatelských preferencí.
- Podporuje autentizaci založenou na identitách předplatitele IMS pro zabezpečený přístup k datům.
- Umožňuje konzistentní personalizaci služeb napříč více IMS aplikacemi z jediného zdroje dat.
- Usnadňuje vytváření pokročilých komunikačních služeb, jako je skupinový chat, seznamy prostředků pro přítomnost a konferenční hovory.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements

---

📖 **Anglický originál a plná specifikace:** [GLMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/glms/)
