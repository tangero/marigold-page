---
slug: "tld"
url: "/mobilnisite/slovnik/tld/"
type: "slovnik"
title: "TLD – Top Level Domain"
date: 2005-01-01
abbr: "TLD"
fullName: "Top Level Domain"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tld/"
summary: "Top Level Domain (TLD, doména nejvyšší úrovně) v kontextu 3GPP označuje nejvyšší úroveň v hierarchickém systému doménových jmen (DNS), například .com nebo .org. Používá se pro síťové adresování a vyhl"
---

TLD (doména nejvyšší úrovně) je nejvyšší úroveň v hierarchickém systému doménových jmen (DNS), například .com nebo .org, používaná pro síťové adresování, vyhledávání služeb a směrování zpráv v IP komunikacích podle 3GPP.

## Popis

Top Level Domain (TLD, doména nejvyšší úrovně) je poslední segment doménového jména v systému [DNS](/mobilnisite/slovnik/dns/), následující za poslední tečkou, například .com, .org nebo národní domény jako .uk. Ve standardech 3GPP jsou TLD nedílnou součástí síťového adresování, vyhledávání služeb a směrování v rámci IP architektur, včetně IP Multimedia Subsystem (IMS) a obecného připojení k internetu. Hierarchie DNS se skládá z kořenových serverů, TLD serverů a autoritativních jmenných serverů, přičemž TLD spravují organizace jako ICANN. V sítích 3GPP se TLD používají v plně kvalifikovaných doménových jménech ([FQDN](/mobilnisite/slovnik/fqdn/)) k identifikaci síťových funkcí, uživatelských zařízení (UE) a služeb, což umožňuje překlad na IP adresy prostřednictvím DNS dotazů. Klíčové komponenty zahrnují DNS rezolvery v uživatelských zařízeních a síťových prvcích, které komunikují s TLD servery za účelem procházení stromu DNS a nalezení konkrétních zdrojů.

Operačně, když zařízení nebo síťová funkce v 3GPP potřebuje přístup ke službě, zahájí DNS dotaz pro FQDN, například example.com. Resolver nejprve kontaktuje kořenový server, aby identifikoval TLD server pro .com, poté dotazuje tento TLD server o autoritativní jmenný server domény a nakonec získá IP adresu. Tento proces podporuje vyhledávání služeb v IMS, kde TLD pomáhají směrovat zprávy Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) ke správnému proxy nebo registrátorovi. TLD také hrají roli při výběru sítě a roamingu, protože mohou naznačovat geografické nebo organizační hranice, což napomáhá efektivnímu směrování a vynucování politik napříč mobilními i pevnými sítěmi.

Role TLD v 3GPP spočívá v poskytování škálovatelného, globálně uznávaného systému pojmenování, který usnadňuje interoperabilitu mezi různorodými sítěmi a službami. Je základem uživatelsky přívětivého adresování, umožňujícího účastníkům přístup ke službám prostřednictvím zapamatovatelných doménových jmen namísto číselných IP adres. V kontextech jako IMS zajišťují TLD správné navázání a směrování multimediálních relací napříč doménami operátorů. Spoléháním na standardizované DNS protokoly využívá 3GPP TLD ke zvýšení spolehlivosti sítě, podpoře mobility a umožnění hladké integrace s internetem, což je zásadní pro moderní mobilní komunikace a multimediální aplikace.

## K čemu slouží

TLD byly začleněny do standardů 3GPP, aby řešily potřebu standardizovaného, hierarchického pojmenování v IP sítích, které se stalo klíčovým s migrací na plně IP architektury jako IMS a LTE. Historicky telekomunikační sítě používaly číselné adresovací schémata (např. čísla E.164), která nebyla ze své podstaty kompatibilní s internetovými protokoly. Jak se mobilní sítě vyvíjely, aby podporovaly přístup k internetu a multimediální služby, byl vyžadován jednotný systém pojmenování pro směrování zpráv, vyhledávání služeb a identifikaci entit napříč heterogenními doménami. TLD jako součást [DNS](/mobilnisite/slovnik/dns/) poskytly pro tento účel globálně přijímaný rámec, který vyřešil omezení proprietárních nebo neškálovatelných metod pojmenování.

Motivace pro zahrnutí TLD do 3GPP vychází z konvergence telekomunikačních a internetových technologií, kde bezproblémové poskytování služeb závisí na interoperabilním adresování. Předchozí přístupy postrádaly flexibilitu a škálovatelnost potřebnou pro rostoucí počet zařízení a služeb. TLD umožňují efektivní organizaci doménových jmen, podporují mezinárodní roaming tím, že indikují kódy zemí, a usnadňují uživatelsky přívětivý přístup k síťovým zdrojům. Tato integrace pomáhá operátorům spravovat složité sítě, zlepšovat vyhledávání služeb a zajišťovat spolehlivou komunikaci, což je v souladu s širším trendem konvergence pevných a mobilních sítí a poskytování služeb založených na internetu.

## Klíčové vlastnosti

- Nejvyšší úroveň v hierarchii DNS pro organizaci doménových jmen
- Podporuje překlad FQDN na IP adresy v sítích 3GPP
- Umožňuje vyhledávání služeb a směrování v IMS a službách založených na IP
- Zahrnuje generické TLD (gTLD) a národní TLD (ccTLD)
- Usnadňuje interoperabilitu s internetovými protokoly a systémy
- Používá se pro adresování síťových funkcí a identifikaci uživatelských zařízení (UE)

## Související pojmy

- [DNS – Directory Name Service](/mobilnisite/slovnik/dns/)
- [FQDN – Fully Qualified Domain Name](/mobilnisite/slovnik/fqdn/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition

---

📖 **Anglický originál a plná specifikace:** [TLD na 3GPP Explorer](https://3gpp-explorer.com/glossary/tld/)
