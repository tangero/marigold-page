---
slug: "hpm"
url: "/mobilnisite/slovnik/hpm/"
type: "slovnik"
title: "HPM – HP Module"
date: 2025-01-01
abbr: "HPM"
fullName: "HP Module"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/hpm/"
summary: "HP Module je standardizovaná bezpečnostní komponenta definovaná v 3GPP pro hostování a provádění citlivých aplikací a služeb. Poskytuje zabezpečené, izolované prostředí k ochraně kritických funkcí a d"
---

HPM (modul s vysokou úrovní ochrany) je standardizovaná bezpečnostní komponenta 3GPP, která poskytuje zabezpečené, izolované prostředí pro hostování a provádění citlivých aplikací za účelem ochrany kritických funkcí a dat.

## Popis

[HP](/mobilnisite/slovnik/hp/) Module, jak je specifikováno v 3GPP TS 33.320 a TS 33.545, je základní bezpečnostní stavební blok navržený tak, aby poskytoval chráněné prováděcí prostředí v rámci síťového uzlu nebo uživatelského zařízení. Architektonicky se jedná o logický nebo fyzický modul, který zajišťuje izolaci, ochranu integrity a důvěrnost pro hostované aplikace a data. Funguje tak, že vytváří zabezpečenou hranici, často využívající hardwarové bezpečnostní prvky jako Trusted Execution Environments (TEE) nebo vyhrazené bezpečnostní čipy, aby chránil svůj vnitřní stav a procesy před neoprávněným přístupem nebo manipulací ze strany hostitelské platformy nebo jiných aplikací.

Klíčové součásti HP Module zahrnují jasně definovaný bezpečnostní perimetr, zabezpečené úložiště pro klíče a citlivá data a důvěryhodné běhové prostředí pro provádění aplikací. S hostitelským systémem komunikuje prostřednictvím řízených a ověřených kanálů. Jeho úlohou v síti je sloužit jako kořen důvěry pro kritické funkce, jako je správa přihlašovacích údajů, autentizační procedury, provádění zabezpečené servisní logiky a ochrana proprietárních algoritmů. Poskytnutím standardizovaného zabezpečeného prostředí umožňuje nasazení přidaných služeb a síťových funkcí, které vyžadují vysokou úroveň záruk, aniž by byla ohrožena bezpečnost celého systému.

Provoz modulu se řídí přísnými bezpečnostními politikami a postupy správy životního cyklu definovanými ve specifikacích. Podporuje zabezpečené načítání, inicializaci a atestaci, což umožňuje externím entitám ověřit jeho autenticitu a integritu. Tato schopnost je klíčová pro scénáře, jako je síťová autentizace, kde HP Module může bezpečně ukládat a zpracovávat přihlašovací údaje účastníka, nebo pro edge computing, kde může hostovat citlivé síťové funkce v potenciálně nedůvěryhodném prostředí. Jeho návrh zajišťuje, že i když je hostitelská platforma kompromitována, zůstane bezpečnost aplikací a dat uvnitř HP Module nedotčena.

## K čemu slouží

[HP](/mobilnisite/slovnik/hp/) Module byl zaveden, aby řešil rostoucí potřebu standardizovaných, vysoce zabezpečených prostředí v čím dál složitějších a otevřenějších telekomunikačních systémech. Před jeho standardizací byla bezpečnostní funkcionalita často implementována ad-hoc, specifickým způsobem pro každého dodavatele, což vedlo k problémům s interoperabilitou a nekonzistentní úrovni zabezpečení. Rozšíření softwarových síťových funkcí a přechod k virtualizovaným a cloud-nativním architekturám (jako [NFV](/mobilnisite/slovnik/nfv/) a [MEC](/mobilnisite/slovnik/mec/)) vytvořily nové útočné plochy, což si vyžádalo společný, robustní mechanismus pro ochranu citlivých operací.

K jeho vytvoření vedl požadavek na bezpečné hostování aplikací třetích stran, proprietárních algoritmů a kritických síťových funkcí na obecných hardwarových platformách. Tradiční bezpečnostní modely, které spoléhaly pouze na zabezpečení podkladového operačního systému, byly pro aktiva s vysokou hodnotou nedostatečné. HP Module poskytuje hardwarově podporované nebo silně izolované softwarové prostředí, které vytváří jasnou hranici důvěry, a umožňuje tak zabezpečené poskytování služeb, správu digitálních práv a důvěryhodné provádění ve scénářích s více nájemci. Řeší problém, jak zachovat důvěrnost a integritu ve sdílené infrastruktuře, což je zásadní pro důvěru operátorů, dodržování předpisů a umožnění nových obchodních modelů zahrnujících zpracování citlivých dat na síťové hraně nebo v uživatelských zařízeních.

## Klíčové vlastnosti

- Poskytuje standardizované zabezpečené prováděcí prostředí (např. založené na TEE) pro aplikace a data
- Zajišťuje izolaci a ochranu integrity před hostitelskou platformou a jinými aplikacemi
- Podporuje zabezpečené úložiště pro kryptografické klíče a citlivé informace
- Umožňuje zabezpečené načítání, inicializaci a vzdálenou atestaci stavu modulu
- Definuje rozhraní a správu životního cyklu pro hostované bezpečnostní funkce
- Usnadňuje nasazení důvěryhodných služeb ve virtualizovaných prostředích a prostředích edge computingu

## Související pojmy

- [MEC – Multi-Access Edge Computing](/mobilnisite/slovnik/mec/)

## Definující specifikace

- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem

---

📖 **Anglický originál a plná specifikace:** [HPM na 3GPP Explorer](https://3gpp-explorer.com/glossary/hpm/)
