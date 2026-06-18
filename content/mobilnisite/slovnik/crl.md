---
slug: "crl"
url: "/mobilnisite/slovnik/crl/"
type: "slovnik"
title: "CRL – Certificate Revocation List"
date: 2025-01-01
abbr: "CRL"
fullName: "Certificate Revocation List"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/crl/"
summary: "Seznam odvolaných certifikátů (Certificate Revocation List, CRL) je bezpečnostní mechanismus v sítích 3GPP, který poskytuje výčet digitálních certifikátů odvolaných před plánovaným koncem jejich platn"
---

CRL je bezpečnostní mechanismus v sítích 3GPP, který poskytuje seznam odvolaných digitálních certifikátů. Síťové entity jej využívají k ověření platnosti certifikátů během autentizace a zabezpečené komunikace.

## Popis

Seznam odvolaných certifikátů (Certificate Revocation List, CRL) je základní součást infrastruktury veřejného klíče ([PKI](/mobilnisite/slovnik/pki/)) používané v systémech 3GPP pro správu zabezpečení. Funguje jako digitálně podepsaný seznam, vydávaný certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)), který vyjmenovává sériová čísla certifikátů, jež byly odvolány a již nejsou považovány za platné. Seznam obsahuje datum odvolání a často i důvod odvolání (např. kompromitace klíče, kompromitace CA, změna příslušnosti, ukončení činnosti, pozastavení certifikátu). Podpis CRL zajišťuje jeho autenticitu a integritu, což umožňuje spoléhajícím stranám důvěřovat jeho obsahu.

V architektuře 3GPP používají CRL různé síťové funkce a uživatelská zařízení (UE) k provádění validace certifikátů během bezpečnostních procedur. Například když se UE autentizuje v síti prostřednictvím rámce Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)) rozšířeného o metody založené na certifikátech, nebo když se síťové funkce vzájemně autentizují (např. v [SBA](/mobilnisite/slovnik/sba/) – Service-Based Architecture), musí být předložené certifikáty ověřeny. Tento validační proces zahrnuje kontrolu podpisového řetězce certifikátu, doby platnosti a jeho stavu odvolání konzultací příslušného CRL. CRL může být distribuován specifickými protokoly nebo stažen z předem nakonfigurovaného distribučního bodu (CRL Distribution Point – [CDP](/mobilnisite/slovnik/cdp/)), který je často vložen přímo do certifikátu.

Správa a distribuce CRL zahrnuje několik klíčových entit: certifikační autoritu (CA), která CRL vydává a podepisuje, úložiště (Repository), které CRL uchovává a šíří, a spoléhající stranu (např. UE, [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/)), která jej získává a zpracovává. Proces funguje tak, že CA periodicky generuje a publikuje aktualizované CRL. Spoléhající strany pak musí tyto aktualizace získávat, typicky přes protokoly [HTTP](/mobilnisite/slovnik/http/)/LDAP, aby udržovaly aktuální přehled o stavu odvolání. Frekvence vydávání CRL (perioda vydávání CRL) je kritickým parametrem, který vyvažuje aktuálnost zabezpečení vůči síťové zátěži a zpracování na straně klienta. Spoléhající strana si CRL ukládá do mezipaměti až do času „nextUpdate“, po kterém musí získat novější verzi, aby zajistila pokračující přesnou validaci.

CRL hrají zásadní roli v celkovém bezpečnostním postoji sítí 3GPP tím, že umožňují včasnou invalidaci přihlašovacích údajů, kterým již nelze důvěřovat. To je nezbytné pro zmírnění rizik spojených s odcizenými privátními klíči, kompromitovanými síťovými funkcemi nebo chybně vydanými certifikáty. Bez efektivního odvolacího mechanismu, jako je CRL, by mohly být potenciálně zneužity i certifikáty s vypršenou platností nebo certifikáty spojené s napadenými entitami, což by podkopalo model důvěry celé PKI. Validace CRL je proto nedílným krokem v procedurách validace certifikačních cest specifikovaných v bezpečnostních specifikacích 3GPP.

## K čemu slouží

Technologie CRL existuje pro řešení kritického problému invalidace přihlašovacích údajů v rámci infrastruktury veřejného klíče (PKI). Digitální certifikáty, které vážou identitu entity k veřejnému klíči, mají dlouhou dobu platnosti (často měsíce nebo roky). Pokud je odpovídající privátní klíč kompromitován, entita již není autorizována, nebo byl certifikát vydán chybně, je nezbytné tento certifikát okamžitě zneplatnit, spíše než čekat na přirozený konec jeho platnosti. CRL poskytuje standardizovanou, škálovatelnou metodu pro šíření těchto informací o odvolání ke všem spoléhajícím stranám v celé síti.

Historicky, bez odvolacího mechanismu, jakmile byl certifikát vydán, zůstával technicky platný až do data vypršení, což vytvářelo významné bezpečnostní okno zranitelnosti. Vytvoření CRL bylo motivováno potřebou toto okno uzavřít a poskytnout certifikační autoritě prostředek, jak deklarovat, kterým certifikátům již nelze důvěřovat. V sítích 3GPP, jak se služby vyvíjely ze 4G na 5G a přijímaly více cloud-nativní, službami založené architektury se zvýšeným využitím autentizace založené na certifikátech (např. pro servisní komunikaci síťových funkcí, onboarding zařízení IoT), se spolehlivá a efektivní správa životního cyklu certifikátů, včetně odvolání, stala ještě důležitější.

CRL řeší omezení předchozích ad-hoc nebo neexistujících odvolacích metod tím, že poskytuje autentizovaný, periodicky aktualizovaný seznam. Řeší problém škálovatelnosti tím, že umožňuje distribuci přes standardní webové protokoly. Zatímco alternativní mechanismy, jako je Online Certificate Status Protocol (OCSP), nabízejí kontrolu v reálném čase, CRL zůstávají základní, široce podporovanou a někdy preferovanou metodou díky své jednoduchosti, schopnosti pracovat offline po uložení do mezipaměti a vhodnosti pro prostředí, kde nejsou trvalé online dotazy proveditelné nebo žádoucí, čímž tvoří základní kámen validačního rámce certifikátů 3GPP.

## Klíčové vlastnosti

- Digitálně podepsaný seznam zajišťující autenticitu a integritu
- Obsahuje sériová čísla odvolaných certifikátů s časem a důvodem odvolání
- Periodicky vydávaný a aktualizovaný certifikační autoritou (CA)
- Distribuován standardními protokoly (např. HTTP, LDAP) z úložiště nebo CDP
- Nedílná součást procedur validace certifikačních cest v zabezpečení 3GPP
- Umožňuje offline validaci při uložení do mezipaměti spoléhajícími stranami

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.310** (Rel-19) — 3GPP Authentication Framework for Network Nodes
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [CRL na 3GPP Explorer](https://3gpp-explorer.com/glossary/crl/)
