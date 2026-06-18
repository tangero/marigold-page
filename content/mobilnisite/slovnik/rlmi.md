---
slug: "rlmi"
url: "/mobilnisite/slovnik/rlmi/"
type: "slovnik"
title: "RLMI – Resource List Meta-Information"
date: 2025-01-01
abbr: "RLMI"
fullName: "Resource List Meta-Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rlmi/"
summary: "Resource List Meta-Information (RLMI) je formát XML dokumentu používaný ve službě IMS Presence. Poskytuje metadata o seznamu prezence zdrojů (tzv. 'buddy list'), včetně jeho verze, indikace úplného st"
---

RLMI je formát XML dokumentu používaný ve službě IMS Presence k poskytnutí metadat o seznamu prezence zdrojů, včetně jeho verze, stavu a položek členů s jejich stavem odběru.

## Popis

Resource List Meta-Information (RLMI) je [XML](/mobilnisite/slovnik/xml/) dokument definovaný ve specifikacích služby IMS (IP Multimedia Subsystem) Presence, zejména v [RFC](/mobilnisite/slovnik/rfc/) 4662 a přijatý 3GPP. Není to protokol, ale datový formát přenášený v těle požadavků [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) NOTIFY. Jeho hlavní úlohou je přenášet metadata o seznamu zdrojů, což je v podstatě odběr informací o přítomnosti více uživatelů (tzv. 'buddy list'). Když pozorovatel (např. klientská aplikace uživatele) odebírá [URI](/mobilnisite/slovnik/uri/) seznamu zdrojů (spravované Resource List Serverem - [RLS](/mobilnisite/slovnik/rls/)), RLS používá RLMI ve svých oznámeních k poskytnutí souhrnu stavu celého seznamu.

Dokument RLMI obsahuje několik klíčových prvků. Prvek 'list' má atributy jako 'uri' (URI seznamu zdrojů) a 'version' (sekvenční číslo verze seznamu). Zásadní je atribut 'fullState', který, když je nastaven na 'true', indikuje, že oznámení obsahuje informace o každém členovi seznamu. Používá se pro počáteční oznámení nebo po synchronizaci seznamu. Uvnitř prvku list jsou jeden nebo více prvků 'resource', z nichž každý reprezentuje člena seznamu.

Každý prvek 'resource' v RLMI obsahuje URI člena a atribut 'state' udávající stav odběru mezi RLS a prezence agentem tohoto člena (např. 'active', 'pending', 'terminated'). Nejvýznamnější je, že každý prvek resource může obsahovat vložený dokument prezence (ve formátu [PIDF](/mobilnisite/slovnik/pidf/)) pro daného člena, pokud došlo ke změně stavu, nebo může být prázdný, pokud se stav člena nezměnil. Tato struktura umožňuje, aby jediné NOTIFY obsahující RLMI poskytlo úplnou, přírůstkovou aktualizaci pro velký seznam kontaktů, přičemž označí, kteří členové se změnili a poskytne jejich nové informace o přítomnosti, zatímco implicitně indikuje žádnou změnu u ostatních.

Použití RLMI umožňuje škálovatelnost a efektivitu sítě. Bez RLMI by RLS musel při jakékoli změně odesílat jednotlivé zprávy NOTIFY za každého člena seznamu, nebo odesílat velký agregovaný dokument bez jasných metadat. RLMI poskytuje standardizovaný, strojově čitelný index, který umožňuje klientské aplikaci pozorovatele efektivně parsovat oznámení, aktualizovat svou interní verzi seznamu a zpracovat pouze data změněných členů. Je to základní prvek pro možnosti správy seznamů ve službě IMS Presence.

## K čemu slouží

RLMI bylo vytvořeno k vyřešení problému efektivního oznamování pozorovatelům o změnách v odebíraném seznamu prezence zdrojů (tzv. 'buddy list'). V raných systémech prezence správa seznamů často vyžadovala více jednotlivých odběrů nebo neefektivní přenosy objemných dat. Hlavní motivací bylo umožnit funkčnost Resource List Serveru ([RLS](/mobilnisite/slovnik/rls/)) definovanou v [SIP](/mobilnisite/slovnik/sip/) pro oznamování událostí, což uživateli umožňuje odebírat jediné URI seznamu namísto individuálního odběru každého kontaktu.

Klíčové problémy, které RLMI řeší, jsou zatížení signalizace sítě a složitost zpracování na straně klienta. Bez RLMI, pokud by jeden člen v seznamu 100 kontaktů aktualizoval svou přítomnost, RLS by možná musel odeslat 100 jednotlivých oznámení nebo monolitický blok dat, který by nutil klienta parsovat vše. RLMI poskytuje strukturovaný souhrn. Řekne klientovi celkovou verzi seznamu a prostřednictvím příznaku 'fullState' a stavu na úrovni zdroje přesně, kteří členové seznamu se změnili. To umožňuje RLS odeslat jediné, kompaktní NOTIFY, které obsahuje úplná data o přítomnosti pouze pro změněné členy, což drasticky snižuje požadavky na šířku pásma a zpracování. Bylo to klíčovým prvkem pro škálovatelné, operátorské služby prezence v IMS.

## Klíčové vlastnosti

- Formát XML dokumentu přenášený v tělech SIP NOTIFY pro odběry seznamů prezence.
- Poskytuje atribut 'version' pro celý seznam zdrojů, což umožňuje synchronizaci.
- Obsahuje booleovský atribut 'fullState' pro rozlišení částečných a úplných aktualizací seznamu.
- Obsahuje seznam prvků 'resource', každý s URI člena a stavem odběru.
- Umožňuje vložení skutečných informací o přítomnosti (PIDF) pro změněné členy do každého prvku resource.
- Umožňuje efektivní, přírůstková oznámení pro velké seznamy prezence, což snižuje zatížení sítě a klienta.

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem

---

📖 **Anglický originál a plná specifikace:** [RLMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlmi/)
