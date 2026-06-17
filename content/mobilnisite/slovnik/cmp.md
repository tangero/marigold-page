---
slug: "cmp"
url: "/mobilnisite/slovnik/cmp/"
type: "slovnik"
title: "CMP – Certificate Management Protocols"
date: 2026-01-01
abbr: "CMP"
fullName: "Certificate Management Protocols"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cmp/"
summary: "CMP definuje standardizované protokoly pro správu digitálních certifikátů v sítích 3GPP. Umožňuje automatickou registraci, obnovu a odvolání certifikátů pro síťové entity a zařízení, čímž zajišťuje be"
---

CMP je standardizovaný protokol pro správu digitálních certifikátů v sítích 3GPP, který umožňuje automatickou registraci, obnovu a odvolání, čímž zajišťuje bezpečné ověřování a komunikaci.

## Popis

Certificate Management Protocols (CMP) jsou soubor standardizovaných protokolů v rámci specifikací 3GPP, které automatizují správu životního cyklu digitálních certifikátů. Tyto protokoly řídí, jak jsou certifikáty žádány, vydávány, obnovovány, odvolávány a distribuovány mezi certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)) a různými entitami v síti 3GPP, jako je uživatelské zařízení (UE), síťové funkce a systémy správy. Architektura je typu klient-server, kde klient (např. UE nebo síťový uzel) komunikuje s CA nebo registrační autoritou (RA) pomocí definovaných formátů zpráv a procedur přes zabezpečený transport. CMP podporuje více operací včetně počáteční registrace (pro entity bez předchozích certifikátů), obnovy certifikátů před vypršením platnosti, aktualizace klíčů a odvolání prostřednictvím mechanismů jako seznamy odvolaných certifikátů ([CRL](/mobilnisite/slovnik/crl/)) nebo Online Certificate Status Protocol ([OCSP](/mobilnisite/slovnik/ocsp/)).

V jádru CMP funguje tak, že definuje sadu zpráv pro správu PKI, jako je žádost o certifikaci (PKCS#10 nebo CRMF), odpověď na certifikaci, žádost o odvolání a zprávy pro aktualizaci klíčů. Tyto zprávy jsou zapouzdřeny v obálce protokolu CMP a typicky zabezpečeny pomocí kryptografických mechanismů, jako jsou podpisy nebo heslem chráněný [MAC](/mobilnisite/slovnik/mac/) (Message Authentication Code) pro prokázání držení a ověřování. Protokoly specifikují, jak se entity ověřují u CA, často pomocí sdílených tajemství nebo mechanismů mimo pásmo během počátečního zavádění. CMP může pracovat v různých režimech, včetně 'push' modelů, kde CA iniciuje doručení certifikátu, a 'pull' modelů, kde klient certifikáty vyžaduje, čímž se přizpůsobují různé scénáře nasazení od zřizování rozsáhlého množství IoT zařízení až po zabezpečenou správu přihlašovacích údajů síťových funkcí.

Klíčové součásti v ekosystému CMP zahrnují koncovou entitu ([EE](/mobilnisite/slovnik/ee/)), což je klient žádající služby certifikátů, registrační autoritu (RA), která žádosti ověřuje a předává CA, certifikační autoritu (CA), která certifikáty vydává a podepisuje, a volitelně autoritu pro generování klíčů (KGA) pro centralizované generování klíčů. CMP se integruje s širší bezpečnostní architekturou 3GPP, což umožňuje používat certifikáty pro zabezpečení rozhraní (např. pomocí TLS), ověřování zařízení v sítích 5G (zejména pro ochranu SUCI/SUPI) a podporu služeb, jako je síťové dělení (network slicing) a edge computing, kde je vyžadováno dynamické vytváření důvěry. Jeho role je zásadní pro implementaci infrastruktury veřejných klíčů (PKI) v mobilních sítích, neboť zajišťuje konzistentní, bezpečnou a škálovatelnou správu kryptografických přihlašovacích údajů, což je nezbytné pro automatizaci a snížení manuálních zásahů v procesech životního cyklu certifikátů.

## K čemu slouží

CMP bylo zavedeno, aby řešilo rostoucí potřebu automatizované a škálovatelné správy digitálních certifikátů v sítích 3GPP. Před jeho standardizací se správa certifikátů často spoléhala na manuální procesy nebo proprietární protokoly, které byly náchylné k chybám, neefektivní a obtížně škálovatelné pro miliony zařízení, zejména s nástupem IoT a komunikace typu stroj-stroj. Ruční registrace a obnova certifikátů představovaly významnou provozní zátěž a bezpečnostní rizika, jako například vypršené certifikáty způsobující výpadky služeb nebo slabé mechanismy ověřování. Vytvoření CMP bylo motivováno požadavkem na vytvoření jednotného, interoperabilního rámce pro operace PKI, který by umožnil bezpečné zavádění a správu životního cyklu pro síťové entity, jak je definováno ve specifikacích 3GPP, například pro IMS (IP Multimedia Subsystem) a správu sítě.

Historicky, jak se sítě 3GPP vyvíjely směrem k architekturám plně založeným na IP a rostla závislost na webových službách a cloud-nativních funkcích, stala se potřeba silného ověřování a šifrování prvořadou. CMP řeší problém, jak bezpečně distribuovat a spravovat kryptografické identity (certifikáty), které jsou základem těchto bezpečnostních mechanismů. Poskytuje standardizovaný způsob zpracování událostí životního cyklu certifikátů, což je klíčové pro udržení nepřetržitého souladu s bezpečnostními požadavky a pro umožnění funkcí jako zřizování zařízení bez zásahu obsluhy (zero-touch provisioning). Automatizací správy certifikátů CMP snižuje administrativní náklady, minimalizuje lidské chyby a zlepšuje celkovou bezpečnostní pozici sítě tím, že zajišťuje včasné aktualizace a odvolání.

Dále CMP řeší omezení předchozích ad-hoc přístupů definováním jasných toků zpráv, zpracování chyb a bezpečnostních ochran pro transakce správy certifikátů. Podporuje různé případy užití, od výroby zařízení a počátečního připojení k síti až po rutinní rotaci klíčů a nouzové odvolání. Tato schopnost je nezbytná pro moderní sítě 3GPP, včetně 5G a dalších generací, kde dynamické síťové dělení (network slicing), architektury založené na službách a masivní nasazení IoT vyžadují robustní, automatizovanou správu důvěry. CMP tedy poskytuje základní protokoly, které umožňují bezpečné, škálovatelné a budoucím výzvám odolné operace s certifikáty v celém ekosystému.

## Klíčové vlastnosti

- Standardizované zprávy pro správu PKI pro registraci, obnovu a odvolání
- Podpora více mechanismů ověřování včetně sdílených tajemství a podpisů
- Flexibilní provozní režimy (push a pull) pro různé scénáře nasazení
- Integrace s bezpečnostní architekturou 3GPP pro ověřování zařízení a sítě
- Automatizovaná správa životního cyklu snižující manuální zásahy a chyby
- Škálovatelnost pro masivní zřizování IoT zařízení a správu přihlašovacích údajů síťových funkcí

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 28.314** (Rel-20) — Management and Orchestration - Plug and Connect
- **TS 32.501** (Rel-19) — Self-Configuration of Network Elements Concepts
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [CMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmp/)
