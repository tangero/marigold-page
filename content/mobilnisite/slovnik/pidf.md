---
slug: "pidf"
url: "/mobilnisite/slovnik/pidf/"
type: "slovnik"
title: "PIDF – Presence Information Data Format"
date: 2025-01-01
abbr: "PIDF"
fullName: "Presence Information Data Format"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pidf/"
summary: "Datový formát založený na XML, definovaný IETF a přijatý 3GPP, pro reprezentaci prezence (informace o přítomnosti) – ochoty, dostupnosti a komunikačních schopností uživatele (prezentity). Jedná se o z"
---

PIDF je datový formát založený na XML, definovaný IETF a přijatý 3GPP, pro reprezentaci prezence (informace o přítomnosti) uživatele, jako je ochota, dostupnost a komunikační schopnosti v rámci služby IMS Presence Service.

## Popis

Presence Information Data Format (PIDF) je formát dokumentu v rozšiřitelném značkovacím jazyce ([XML](/mobilnisite/slovnik/xml/)), který zapouzdřuje stav prezence (přítomnosti) uživatele nebo entity, známé jako prezentita. V architektuře IMS dle 3GPP je PIDF standardizovaným užitečným zatížením přenášeným zprávami [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), jako jsou PUBLISH, SUBSCRIBE a NOTIFY, které umožňují službu prezence. PIDF dokument obsahuje povinný kořenový prvek <presence>, který zahrnuje jeden nebo více prvků <tuple>. Každý <tuple> reprezentuje konkrétní komunikační službu nebo adresu (jako je SIP [URI](/mobilnisite/slovnik/uri/)) a její stav, popsaný prvkem <status> obsahujícím podprvky jako <basic> (open/closed).

Fungování PIDF ve službě IMS presence zahrnuje několik entit. User Equipment (UE) prezentity funguje jako Presence User Agent ([PUA](/mobilnisite/slovnik/pua/)), který shromažďuje lokální informace o přítomnosti (např. stav zařízení, aktivita uživatele). Agreguje je do PIDF dokumentu a odesílá jej prostřednictvím SIP PUBLISH požadavku na Presence Server ([PS](/mobilnisite/slovnik/ps/)). PS, což je centrální úložiště, ukládá a spravuje PIDF pro každou prezentitu. Když Watcher (další uživatel přihlášený k odběru prezence prezentity) požaduje aktualizace, odešle SIP SUBSCRIBE. PS poté generuje notifikace (SIP NOTIFY) obsahující aktuální PIDF dokument prezentity všem autorizovaným watcherům.

PIDF je navržen pro bohaté vyjádření. Kromě základního stavu může obsahovat volitelné prvky, jako je priorita <contact>, <note> pro volně psané zprávy čitelné člověkem a <timestamp> udávající čas vygenerování informace o přítomnosti. Rozšíření od 3GPP a [IETF](/mobilnisite/slovnik/ietf/), jako je Presence Data Model (PDM) a Rich Presence Information Data ([RPID](/mobilnisite/slovnik/rpid/)), definují další XML prvky, které mohou být vloženy do PIDF pro sdělení podrobnějšího kontextu, jako je aktivita uživatele (schůzka, cestování), nálada nebo geografická poloha. Tato rozšiřitelnost činí z PIDF výkonný a do budoucna připravený základ pro komunikační služby s podporou prezence.

## K čemu slouží

PIDF byl vytvořen k vyřešení problému fragmentovaných, vzájemně nekompatibilních informací o přítomnosti v raných internetových komunikačních službách. Před jeho standardizací používaly systémy instant messagingu a prezence (například od různých výrobců) proprietární datové formáty, což vytvářelo uzavřené ekosystémy. Vývoj PIDF v [IETF](/mobilnisite/slovnik/ietf/), primárně prostřednictvím RFC 3863, si kladl za cíl vytvořit společný, rozšiřitelný a univerzální formát pro výměnu dat o přítomnosti, což je předpokladem pro všudypřítomné služby prezence napříč sítěmi.

3GPP přijalo PIDF jako základní kámen své služby IMS Presence Service, aby umožnilo bohaté síťové funkce prezence pro mobilní uživatele. Motivací bylo využít konvergence buněčných a IP technologií k nabídnutí pokročilých komunikačních služeb nad rámec hlasu. Standardizovaný formát byl nezbytný k zajištění, aby informace o přítomnosti generované zařízením od jednoho výrobce mohly být správně interpretovány a zobrazeny zařízením nebo aplikací od jiného výrobce a správně zpracovány síťovými servery. Řešil tak omezení předchozích buněčných služeb, kterým chyběl standardizovaný mechanismus pro sdílení dostupnosti v reálném čase nezávislý na konkrétní službě.

PIDF tedy existuje k umožnění interoperability a vytváření bohatých služeb. Poskytuje dobře definovanou sémantiku pro základní koncept 'prezence', což umožňuje sítím, zařízením a aplikacím sdílet společnou představu o stavu uživatele. To usnadňuje inovativní služby, jako jsou rozšířené adresáře s živými stavy, směrování hovorů s ohledem na kontext a integrované zážitky z posílání zpráv. Protože je založen na XML a je rozšiřitelný, standard také připravil služby pro budoucnost tím, že umožňuje přidávat nové atributy a schopnosti bez narušení stávajících implementací, čímž podporuje dlouhodobý vývoj komunikačních služeb.

## Klíčové vlastnosti

- Formát založený na XML pro strojově čitelná data o přítomnosti
- Staví na prvcích <tuple> reprezentujících komunikační služby
- Nese základní stav (open/closed) a volitelné poznámky čitelné člověkem
- Rozšiřitelný pro podporu bohatých informací o přítomnosti (např. aktivita, nálada)
- Standardní užitečné zatížení pro publikaci a notifikaci prezence založené na SIP
- Základ pro interoperabilitu služby IMS Presence Service

## Související pojmy

- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RPID – Rich Presence Information Data](/mobilnisite/slovnik/rpid/)

## Definující specifikace

- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.841** (Rel-6) — Presence Service IP Multimedia Subsystem
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [PIDF na 3GPP Explorer](https://3gpp-explorer.com/glossary/pidf/)
