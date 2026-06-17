---
slug: "enum"
url: "/mobilnisite/slovnik/enum/"
type: "slovnik"
title: "ENUM – E.164 telephone NUmber Mapping"
date: 2025-01-01
abbr: "ENUM"
fullName: "E.164 telephone NUmber Mapping"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/enum/"
summary: "ENUM je systém, který mapuje mezinárodní telefonní čísla (E.164) na internetové zdroje, jako jsou URI (např. SIP adresy), za použití Domain Name System (DNS). Umožňuje propojení a konvergenci tradiční"
---

ENUM je systém, který mapuje telefonní čísla E.164 na internetové zdroje, jako jsou SIP URI, za použití DNS, aby umožnil konvergenci mezi tradiční telefonní sítí a službami založenými na IP.

## Popis

E.164 NUmber Mapping (ENUM) je protokol a infrastrukturní rámec definovaný [IETF](/mobilnisite/slovnik/ietf/) (RFC 6116) a přijatý 3GPP pro telekomunikace. Jeho hlavní funkcí je převod standardního mezinárodního telefonního čísla, formátovaného podle normy [ITU-T](/mobilnisite/slovnik/itu-t/) E.164 (např. +441632960000), na doménové jméno. Toto doménové jméno je následně dotazováno v [DNS](/mobilnisite/slovnik/dns/), aby získalo záznamy Naming Authority Pointer ([NAPTR](/mobilnisite/slovnik/naptr/)). Tyto NAPTR záznamy obsahují jeden nebo více Uniform Resource Identifiers (URI), které určují, jak kontaktovat účastníka pomocí IP služby, jako je Session Initiation Protocol (SIP) URI (sip:user@domain.com), e-mailová adresa nebo webová adresa.

Proces ENUM zahrnuje několik kroků. Nejprve je E.164 číslo kanonizováno odstraněním všech nečíselných znaků (jako '+' a '-'). Číslice jsou následně obráceny a mezi každou je vložena tečka. Výsledný řetězec je doplněn doménou '.e164.arpa' (pro veřejný Tier-1 ENUM) nebo operátorskou doménou (pro privátní, operátorský ENUM). Například +44 1632 960000 se stane 0.0.0.0.6.9.2.3.6.1.4.4.e164.arpa. Na tuto doménu je vydán DNS dotaz pro NAPTR záznamy. Vrácené NAPTR záznamy jsou seřazeny podle polí preference a service. Klient (jako IMS Telephony Application Server nebo SIP proxy) vyhodnotí tyto záznamy, aby určil další krok, kterým je typicky přeložení SRV záznamu nebo přímé použití náhradního URI pro směrování hovoru nebo zprávy přes IP.

V rámci architektury 3GPP IP Multimedia Subsystem (IMS) je ENUM klíčovou komponentou pro přenositelnost čísel, směrování hovorů a propojování služeb. Používají ho funkce Interconnection Border Control Function ([IBCF](/mobilnisite/slovnik/ibcf/)), Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)) a Telephony Application Servers (TAS). Když entita IMS potřebuje směrovat hovor na cíl identifikovaný E.164 číslem, může provést ENUM dotaz. Pokud je nalezeno úspěšné mapování na SIP URI, je hovor směrován přímo přes IP síť (např. do jiné IMS sítě nebo podnikové SIP PBX), čímž se vyhne zbytečnému průchodu přes starší PSTN. To umožňuje efektivní, nákladově výhodnou a funkčně bohatou komunikaci založenou na IP. ENUM také podporuje více záznamů na jedno číslo, což umožňuje mapování jednoho telefonního čísla na různé služby (hlas, video, zasílání zpráv, e-mail) na základě možností a preferencí volajícího.

## K čemu slouží

ENUM byl vytvořen k vyřešení základního problému propojení světa tradiční přepojováním okruhů telefonní sítě (PSTN), identifikované E.164 čísly, a vznikajícího světa paketově přepínané komunikace založené na IP. Před ENUM vyžadovalo směrování hovoru z IP sítě (jako rané VoIP nebo IMS) na telefonní číslo typicky bránu pro přechod do PSTN, i když byl cíl dostupný také přes IP. To bylo neefektivní, přidávalo náklady a latenci a často zbavovalo pokročilých funkcí IP služeb. Hlavní motivací bylo umožnit 'all-IP' směrování tam, kde je to možné, což umožňuje, aby hovory zůstaly od konce do konce na IP sítích.

Historicky se telefonní a internetové adresovací schéma vyvíjely odděleně. ENUM poskytl chybějící článek – standardizovanou, distribuovanou databázi (využívající globálně nasazené [DNS](/mobilnisite/slovnik/dns/)), která zjišťuje, zda telefonní číslo má přidruženou IP adresu. Tím se vyřešila omezení statických směrovacích tabulek a proprietárních řídicích jednotek bran. Jeho přijetí 3GPP bylo poháněno vizí IMS jako sjednocující architektury pro multimediální služby. ENUM umožňuje dotazy na přenositelnost čísel v IP kontextu, usnadňuje přímé směrování mezi IMS sítěmi a podporuje konvergenci komunikačních služeb. Umožňuje operátorům snížit závislost na PSTN propojení, zavádět nové IP služby vázané na telefonní číslo uživatele a připravovat cestu k vyřazení starších TDM sítí.

## Klíčové vlastnosti

- Mapuje telefonní čísla ITU-T E.164 na internetové URI za použití protokolu DNS
- Využívá NAPTR DNS záznamy pro ukládání a získávání informací pro směrování specifické pro službu
- Podporuje jak veřejné (e164.arpa), tak privátní/operátorské ENUM stromy pro různé modely nasazení
- Umožňuje přímé směrování založené na IP (např. SIP) mezi koncovými body, s možností obejít PSTN
- Usnadňuje přenositelnost čísel a objevování služeb v IP multimediálních sítích
- Umožňuje mapování jednoho E.164 čísla na více komunikačních služeb (hlas, video, zasílání zpráv, e-mail)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures

---

📖 **Anglický originál a plná specifikace:** [ENUM na 3GPP Explorer](https://3gpp-explorer.com/glossary/enum/)
