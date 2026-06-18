---
slug: "uar"
url: "/mobilnisite/slovnik/uar/"
type: "slovnik"
title: "UAR – User Authorization Request"
date: 2025-01-01
abbr: "UAR"
fullName: "User Authorization Request"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/uar/"
summary: "Příkaz protokolu Diameter používaný v jádrové síti IMS (IP Multimedia Subsystem). Odesílá jej Interrogating-CSCF (I-CSCF) na Home Subscriber Server (HSS) pro vyžádání autorizačních informací o uživate"
---

UAR je příkaz Diameter odesílaný z I-CSCF na HSS za účelem vyžádání autorizačních informací o uživateli pro registraci v IMS nebo zřízení relace.

## Popis

User Authorization Request (UAR) je klíčový příkaz Diameter definovaný ve specifikaci rozhraní Cx (TS 29.229) mezi [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating Call Session Control Function) a [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) v IP Multimedia Subsystem (IMS). Je základní součástí procedur registrace do IMS a zahájení relace. Když User Equipment (UE) naváže kontakt se sítí IMS, je počáteční požadavek [SIP](/mobilnisite/slovnik/sip/) REGISTER směrován na I-CSCF. I-CSCF, který nemá data o účastnících, použije příkaz UAR k dotazování HSS na informace potřebné k směrování požadavku na příslušný [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-CSCF), který bude uživatele obsluhovat.

Příkaz UAR nese ve svém požadavku specifické dvojice atribut-hodnota (AVPs), včetně veřejné identity uživatele ([IMPU](/mobilnisite/slovnik/impu/)), soukromé identity ([IMPI](/mobilnisite/slovnik/impi/)) a identifikátoru navštívené sítě. Po přijetí UAR provede HSS ověření a autorizační kontroly účastníka. Ověří stav jeho předplatného, služební profil a rozhodne, zda je uživateli povolena registrace v požadující síti. Na základě toho HSS odpoví příkazem User Authorization Answer ([UAA](/mobilnisite/slovnik/uaa/)). Odpověď UAA obsahuje klíčové směrovací informace, jako je název (nebo schopnosti) S-CSCF přiděleného k obsluze uživatele, nebo indikaci, že má [I-CSCF](/mobilnisite/slovnik/icscf/) vybrat S-CSCF na základě specifických schopností.

Tento mechanismus zajišťuje bezpečné a efektivní směrování IMS relací. Umožňuje vyrovnávání zatížení mezi více S-CSCF, podporuje roamingové scénáře autorizací přístupu z navštívených sítí a tvoří základ pro následné transakce Diameter, jako je Location Information Request (LIR) a Server-Assignment Request (SAR). Výměna UAR/UAA je tedy prvním krokem k navázání důvěryhodného dialogu mezi uživatelem a jádrem IMS, který střeží přístup k multimediálním službám, jako jsou VoLTE, VoNR a RCS.

## K čemu slouží

Příkaz UAR byl vytvořen, aby řešil základní potřebu centralizovaného, bezpečného a standardizovaného autorizačního mechanismu v architektuře IMS, která byla zavedena pro poskytování IP multimediálních služeb přes paketové sítě. Před IMS a jeho definovanými rozhraními Diameter se tradiční telefonie spoléhala na signalizaci SS7 a HLR pro mobilitu, ale neexistovala jednotná metoda pro autorizaci a směrování požadavků na multimediální relace založené na SIP ve škálovatelném, operátorském měřítku.

Hlavní problém, který UAR řeší, je bezstavová povaha I-CSCF. I-CSCF, který se často nachází na okraji sítě, funguje jako brána a neuchovává data o účastnících. Potřebuje dynamický způsob, jak zjistit, který S-CSCF má zpracovat registraci nebo relaci konkrétního uživatele. Protokol UAR toto zajišťuje dotazem na centrální databázi účastníků (HSS). Tento návrh odděluje směrovací logiku od dat účastníků, čímž zvyšuje škálovatelnost, bezpečnost a flexibilitu. Umožňuje síťové architektury, ve kterých lze fondy S-CSCF dynamicky vybírat na základě zatížení nebo schopností, a poskytuje v HSS jediný bod pro vynucování politik přístupu uživatele. Jeho vytvoření bylo motivováno potřebou robustního, rozšiřitelného rámce pro ověřování a autorizaci, který by mohl podporovat složité poskytování služeb, roamingové dohody a interoperabilitu mezi síťovými prvky různých dodavatelů v víceúčelovém IP prostředí.

## Klíčové vlastnosti

- Příkaz Diameter používaný na rozhraní Cx mezi I-CSCF a HSS
- Nese identity uživatele (IMPU, IMPI) pro autorizační kontroly
- Spouští v HSS ověření předplatného a služebního profilu uživatele
- V odpovědi vrací směrovací informace (název nebo schopnosti S-CSCF)
- Základní pro procedury registrace do IMS a počátečního směrování relace
- Podporuje roamingové scénáře prostřednictvím kontrol identifikátoru navštívené sítě

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 23.380** (Rel-19) — IMS Restoration Procedures

---

📖 **Anglický originál a plná specifikace:** [UAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/uar/)
