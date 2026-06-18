---
slug: "mscc"
url: "/mobilnisite/slovnik/mscc/"
type: "slovnik"
title: "MSCC – Multiple Services Credit Control"
date: 2025-01-01
abbr: "MSCC"
fullName: "Multiple Services Credit Control"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mscc/"
summary: "Aplikace protokolu Diameter (RFC 4006) používaná pro řízení kreditu v reálném čase v online účtovacích systémech 3GPP. Umožňuje síti vyžádat a spravovat kreditní kvóty pro více služeb (např. hlas, dat"
---

MSCC je aplikace protokolu Diameter používaná v online účtovacích systémech 3GPP k vyžádání a správě samostatných kreditních kvót pro více služeb (např. hlas, data, SMS) z účtovacího serveru.

## Popis

Multiple Services Credit Control (MSCC, řízení kreditu pro více služeb) je základní součástí online účtovacího systému ([OCS](/mobilnisite/slovnik/ocs/)) 3GPP, implementovaná jako aplikace protokolu Diameter podle [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 4006. Poskytuje standardizovaný protokol pro autorizaci a řízení kreditu v reálném čase mezi síťovými funkcemi (jako GGSN, [P-GW](/mobilnisite/slovnik/p-gw/) nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/)) a OCS. Protokol MSCC umožňuje síti vyžádat kreditní kvóty pro využití konkrétních služeb účastníkem před jejich povolením a následně nahlásit spotřebovaný kredit. Každá zpráva MSCC může obsahovat více hodnot Service-Context-Id a více Rating-Groups, což jí umožňuje zpracovávat souběžné účtování různých služeb (např. hlasových hovorů, datových relací, [SMS](/mobilnisite/slovnik/sms/) zpráv) v rámci jedné relace účastníka.

Z architektonického hlediska síťová funkce působící jako klient Diameter (např. Charging Trigger Function, [CTF](/mobilnisite/slovnik/ctf/)) odešle příkaz Credit-Control-Request ([CCR](/mobilnisite/slovnik/ccr/)) do OCS (server Diameter). Požadavek obsahuje atributy MSCC (AVP, Attribute-Value Pairs), které specifikují požadovanou službu, požadovanou kvótu a relevantní účtovací parametry. OCS provede rating a správu zůstatku, poté odpoví příkazem Credit-Control-Answer (CCA) obsahujícím udělené kvóty, doby platnosti a indikace konečné jednotky. Síťová funkce poté umožní uživateli spotřebovávat prostředky až do výše udělené kvóty. Když je kvóta vyčerpána nebo služba ukončena, CTF odešle aktualizační CCR, aby nahlásil využití a požádal o nové kvóty.

Protokol MSCC podporuje různé modely řízení kreditu: účtování na základě událostí pro okamžité služby (jako SMS), účtování na základě relace pro kontinuální služby (jako datová relace) a správu kvót objemu/času. Zahrnuje mechanismy pro řádné ukončení služby při vyčerpání kreditu, včetně přesměrování uživatele na portál pro dobití. MSCC je nedílnou součástí generování záznamů o účtovacích datech (CDR) v 3GPP a zajišťuje přesné odečty zůstatku v reálném čase, což je klíčové pro předplacené služby a kontrolu výdajových limitů v postplatbových tarifech.

## K čemu slouží

MSCC byl vytvořen, aby poskytl standardizovaný mechanismus řízení kreditu v reálném čase pro moderní telekomunikační sítě, nahrazující řešení předplacených služeb specifická pro dodavatele a méně flexibilní. Tradiční offline účtování (po události) bylo nedostatečné pro předplacené služby, které vyžadují okamžitou autorizaci kreditu, aby se zabránilo podvodům a překročení výdajů. Rané systémy předplacených služeb často používaly proprietární protokoly, což vedlo ke složité integraci a omezené agilitě služeb.

Zavedení MSCC, založeného na rozšiřitelném protokolu Diameter, tyto problémy vyřešilo tím, že umožnilo jednotné rozhraní pro online účtování všech síťových služeb (hlas, data, zasílání zpráv, IMS). Umožňuje operátorům nabízet účtování v reálném čase pro více služeb souběžně, implementovat sofistikované ratingové plány a poskytovat okamžitá upozornění účastníkům. Jeho vznik byl motivován růstem trhu předplacených služeb a potřebou konvergence v účtovacích systémech, jak se sítě vyvíjely k nabídce balíčků multimediálních služeb. MSCC je základním kamenem konvergentní účtovací architektury 3GPP, podporující jak předplacené, tak postplatbové obchodní modely v reálném čase.

## Klíčové vlastnosti

- Autorizace a řízení kreditu v reálném čase prostřednictvím protokolu Diameter (RFC 4006)
- Podpora více služeb a ratingových skupin v rámci jedné relace
- Umožňuje účtování na základě událostí, relací a kvót objemu/času
- Poskytuje mechanismy pro udělování kvót, aktualizace a indikace konečné jednotky
- Nedílná součást architektury online účtovacího systému (OCS) 3GPP
- Umožňuje předplacené a postplatbové účtování v reálném čase s vysokou přesností

## Související pojmy

- [OCS – Originating Call Screening](/mobilnisite/slovnik/ocs/)
- [CTF – Charging Trigger Function](/mobilnisite/slovnik/ctf/)

## Definující specifikace

- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 32.869** (Rel-15) — Diameter Overload Control for Charging Interfaces

---

📖 **Anglický originál a plná specifikace:** [MSCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mscc/)
