---
slug: "ini"
url: "/mobilnisite/slovnik/ini/"
type: "slovnik"
title: "INI – Internal Network Interface"
date: 2025-01-01
abbr: "INI"
fullName: "Internal Network Interface"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ini/"
summary: "INI je interní síťové rozhraní definované v 3GPP pro zabezpečenou komunikaci mezi síťovými funkcemi v rámci domény operátora. Umožňuje důvěryhodnou výměnu, například pro autentizaci a správu klíčů, a"
---

INI je interní síťové rozhraní 3GPP pro zabezpečenou, důvěryhodnou komunikaci mezi síťovými funkcemi v rámci domény operátora, které zajišťuje ochranu citlivých dat, jako je autentizace a správa klíčů.

## Popis

Interní síťové rozhraní (INI) je standardizované rozhraní v sítích 3GPP, specifikované primárně v dokumentu 33.108, navržené pro zabezpečenou interní komunikaci mezi síťovými entitami. Funguje v rámci důvěryhodné domény operátora a umožňuje interakce, jako je autentizace, autorizace a distribuce klíčů mezi funkcemi jádra sítě, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Authentication Centre (AuC) a dalšími uzly souvisejícími se zabezpečením. INI zajišťuje, že citlivé informace, včetně přihlašovacích údajů účastníka a kryptografických klíčů, jsou přenášeny přes chráněný kanál, čímž zmírňuje rizika z vnějších útoků. Z architektonického hlediska definuje protokoly, formáty zpráv a bezpečnostní mechanismy – jako je šifrování a ochrana integrity – přizpůsobené pro interní použití, což jej odlišuje od externích rozhraní směřujících k nedůvěryhodným sítím. V praxi INI podporuje procedury, jako je proces Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)), při kterém HSS komunikuje s AuC za účelem generování autentizačních vektorů pro uživatelská zařízení. Rozhraní je implementováno pomocí IP protokolů, často se specifickými bezpečnostními vrstvami, aby se zabránilo odposlechu nebo manipulaci. Jeho role je klíčová pro udržení důvěrnosti a integrity operací jádra sítě, protože zpracovává kritická data, která jsou základem uživatelské autentizace a přístupu ke službám. Standardizací tohoto interního rozhraní 3GPP zajišťuje interoperabilitu mezi zařízeními různých dodavatelů v rámci sítě operátora, čímž podporuje bezpečný a soudržný ekosystém.

## K čemu slouží

INI bylo vytvořeno pro uspokojení potřeby zabezpečeného, standardizovaného rozhraní pro interní komunikaci v rámci sítě mobilního operátora, zejména pro funkce citlivé na zabezpečení. Před jeho definicí mohla proprietární rozhraní mezi síťovými prvky vést k problémům s interoperabilitou a potenciálním bezpečnostním zranitelnostem, protože každý dodavatel mohl implementovat různé ochranné mechanismy. INI tento problém řeší tím, že poskytuje společný rámec pro důvěryhodnou výměnu, například během autentizačních procesů, kdy musí být data účastníka bezpečně přenesena mezi [HSS](/mobilnisite/slovnik/hss/) a AuC. Tím je zajištěno, že citlivé operace jsou chráněny před vnějšími hrozbami, což zvyšuje celkové zabezpečení sítě. Rozhraní také podporuje škálovatelnost a flexibilitu, což operátorům umožňuje integrovat řešení od více dodavatelů při zachování vysoké úrovně důvěry. Jeho zavedení v Release 8 bylo v souladu s vývojem směrem k plně IP sítím v LTE, kde interní rozhraní potřebovala robustní zabezpečení, aby odpovídala zvýšené expozici útokům založeným na IP.

## Klíčové vlastnosti

- Zabezpečené rozhraní pro interní síťovou komunikaci
- Používá se pro procedury autentizace a správy klíčů
- Definuje protokoly a formáty zpráv ve specifikaci 3GPP 33.108
- Funguje v rámci důvěryhodné domény operátora
- Podporuje šifrování a ochranu integrity pro citlivá data
- Umožňuje interoperabilitu mezi zařízeními různých dodavatelů

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [INI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ini/)
