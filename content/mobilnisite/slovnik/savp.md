---
slug: "savp"
url: "/mobilnisite/slovnik/savp/"
type: "slovnik"
title: "SAVP – Secure Audio-Video Profile"
date: 2025-01-01
abbr: "SAVP"
fullName: "Secure Audio-Video Profile"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/savp/"
summary: "3GPP profil definující bezpečnostní požadavky a mechanismy pro služby komunikace v reálném čase přenášející audio a video. Zajišťuje důvěrnost, integritu a autentizaci mediálních toků, zejména pro slu"
---

SAVP je 3GPP profil, který definuje bezpečnostní požadavky a mechanismy pro zajištění důvěrnosti, integrity a autentizace pro služby komunikace v reálném čase přenášející audio a video.

## Popis

Secure Audio-Video Profile (SAVP) je specifikace v rámci 3GPP, která definuje komplexní bezpečnostní rámec pro služby multimediální komunikace v reálném čase. Je primárně navržen pro podporu služeb kritických pro plnění úkolu (Mission Critical Services – [MCS](/mobilnisite/slovnik/mcs/)), jako je Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), Mission Critical Video ([MCVideo](/mobilnisite/slovnik/mcvideo/)) a Mission Critical Data (MCData). SAVP funguje na aplikační vrstvě a specifikuje, jak musí být média (audio/video) a související signalizace chráněny před odposlechem, manipulací a falšováním. Funguje tak, že ukládá povinné použití konkrétních kryptografických protokolů, postupů správy klíčů a bezpečnostních algoritmů pro koncové zabezpečení mediálních toků mezi uživateli nebo mezi uživatelem a serverem.

Profil podrobně popisuje použití protokolu Secure Real-time Transport Protocol ([SRTP](/mobilnisite/slovnik/srtp/)) a s ním spojeného protokolu pro správu klíčů [MIKEY](/mobilnisite/slovnik/mikey/) (Multimedia Internet KEYing) jako základních technologií. Pro důvěrnost a integritu médií specifikuje SAVP použití SRTP s šifrováním AES-CM (Counter Mode) a autentizací HMAC-SHA1. Pro správu klíčů definuje použití MIKEY v režimech s předem sdíleným klíčem (MIKEY-PSK) a s veřejným klíčem (MIKEY-RSA), s konkrétními profily pro způsob navázání a distribuce klíčů v architektuře služeb kritických pro plnění úkolu. Klíčovou součástí je Key Management Server ([KMS](/mobilnisite/slovnik/kms/)), který usnadňuje distribuci klíčového materiálu autorizovaným uživatelům a skupinám.

Jeho úlohou v síti je poskytovat standardizovanou, interoperabilní a vysoce spolehlivou bezpečnostní vrstvu pro komunikaci kritickou pro plnění úkolu přes systémy 3GPP. Zajišťuje, že i když podkladová přístupová síť (např. LTE, 5G NR) poskytuje vlastní zabezpečení ([AS](/mobilnisite/slovnik/as/) a [NAS](/mobilnisite/slovnik/nas/) security), samotný mediální obsah obdrží dodatečnou, na službu specifickou vrstvu koncového zabezpečení. To je klíčové pro uživatele z oblasti veřejné bezpečnosti a kritické infrastruktury, kde musí být komunikace zabezpečena proti sofistikovaným hrozbám. SAVP se integruje s celkovou architekturou MCPTT/MCVideo, rozhraním se servery řízení hovorů a systémy správy skupin, aby vynucoval bezpečnostní politiky na základě rolí uživatelů a členství ve skupinách.

## K čemu slouží

SAVP byl vytvořen, aby řešil specifické a přísné bezpečnostní požadavky profesionálních komunikačních služeb a služeb kritických pro plnění úkolu (mission-critical) nasazených přes komerční sítě 3GPP. Před jeho zavedením ve verzi Rel-13 se služby komunikace v reálném čase (jako VoLTE) spoléhaly primárně na zabezpečení podkladové přístupové sítě. Pro uživatele služeb kritických pro plnění úkolu (např. policie, hasiči) to však bylo nedostatečné kvůli hrozbám, jako jsou útoky zevnitř sítě operátora, potřeba zabezpečené skupinové komunikace a požadavek na koncové zabezpečení nezávislé na přenosu. Problémem byl nedostatek standardizovaného, vysoce bezpečného profilu pro média, který by mohl zaručit interoperabilitu mezi implementacemi služeb kritických pro plnění úkolu od různých dodavatelů.

Motivace pro SAVP vycházela z globálních projektů veřejné bezpečnosti, jako je práce 3GPP na MCPTT, které vyžadovaly bezpečnostní rámec schopný splnit vládní a regulační standardy pro zabezpečenou komunikaci. Vyřešil omezení používání obecných SRTP profilů definováním striktní podmnožiny algoritmů, povinných bezpečnostních funkcí a specifických postupů správy klíčů přizpůsobených provozním a důvěryhodnostním modelům kritických služeb. Jeho vytvoření zajistilo, že mediální toky kritické pro plnění úkolu jsou chráněny silnou, ověřenou kryptografií a že správa klíčů je integrována s autentizačním a autorizačním rámcem služby, což poskytuje komplexní bezpečnostní řešení pro aplikace, na nichž závisí životy.

## Klíčové vlastnosti

- Ukládá povinné použití SRTP se šifrováním AES-CM a autentizací HMAC-SHA1
- Specifikuje správu klíčů založenou na MIKEY (režimy PSK a RSA)
- Definuje koncové zabezpečení pro audio/video mediální toky
- Integruje se s architekturou služeb kritických pro plnění úkolu (Mission Critical Service – MCS)
- Podporuje zabezpečené klíčování pro skupinovou komunikaci
- Poskytuje profily pro interoperabilitu mezi zařízeními různých dodavatelů

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [MIKEY – Multimedia Internet KEYing](/mobilnisite/slovnik/mikey/)
- [MCVideo – Mission Critical Video](/mobilnisite/slovnik/mcvideo/)

## Definující specifikace

- **TS 26.179** (Rel-19) — Codecs and Media Handling for MCPTT

---

📖 **Anglický originál a plná specifikace:** [SAVP na 3GPP Explorer](https://3gpp-explorer.com/glossary/savp/)
