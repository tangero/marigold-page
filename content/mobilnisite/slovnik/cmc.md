---
slug: "cmc"
url: "/mobilnisite/slovnik/cmc/"
type: "slovnik"
title: "CMC – Certificate Management Messages over CMS"
date: 2025-01-01
abbr: "CMC"
fullName: "Certificate Management Messages over CMS"
category: "Security"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cmc/"
summary: "CMC je protokol pro správu digitálních certifikátů využívající Cryptographic Message Syntax (CMS). Definuje standardizované zprávy pro registraci, obnovu a odvolání certifikátů v rámci sítí 3GPP, což"
---

CMC je protokol pro správu digitálních certifikátů využívající CMS, který definuje standardizované zprávy pro registraci, obnovu a odvolání certifikátů, čímž umožňuje bezpečnou autentizaci a správu klíčů v rámci sítí 3GPP.

## Popis

Certificate Management Messages over [CMS](/mobilnisite/slovnik/cms/) (CMC) je protokol standardizovaný [IETF](/mobilnisite/slovnik/ietf/) (RFC 5272, RFC 5273, RFC 5274) a přijatý organizací 3GPP pro bezpečnou správu životního cyklu digitálních certifikátů. Funguje nad rámcem Cryptographic Message Syntax (CMS), který poskytuje strukturu pro digitální podepisování, vytváření otisků a šifrování zpráv. CMC definuje sadu formátů zpráv pro žádosti a odpovědi, které umožňují entitám (jako uživatelskému zařízení nebo síťovým funkcím) komunikovat s certifikační autoritou ([CA](/mobilnisite/slovnik/ca/)) nebo registrační autoritou (RA). Tyto zprávy se používají pro základní operace PKI, jako je registrace certifikátu (počáteční certifikace), obnova, odvolání a dotaz na stav certifikátu.

Architektura protokolu zahrnuje klienta (entitu žádající o certifikační služby) a server (CA/RA). Klient vytvoří CMC zprávu žádosti, která je typicky zapouzdřena ve struktuře CMS SignedData nebo AuthenticatedData, aby byla zajištěna integrita a autentizace. Tato žádost je poté přenesena na server pomocí spolehlivého protokolu, často [HTTP](/mobilnisite/slovnik/http/) nebo [HTTPS](/mobilnisite/slovnik/https/), jak je specifikováno v kontextech 3GPP. Server žádost zpracuje, provede potřebné validace a kontrolu politik a vrátí CMC zprávu odpovědi. Tato odpověď obsahuje nový certifikát, indikaci selhání nebo důkaz držení soukromého klíče, opět zabalený v CMS z bezpečnostních důvodů.

Klíčové součásti CMC zahrnují typ obsahu PKIData, který může zabalit více certifikačních žádostí (CertReqMessages) a dalších řídicích atributů do jediné zprávy. Protokol podporuje složité scénáře, jako je odložené zpracování, kdy může CA vrátit odpověď o čekající žádosti, pokud okamžité vydání není možné. Dále definuje mechanismy pro prokázání držení soukromých klíčů, což je klíčové pro zabránění neoprávněnému vydání certifikátu. V systémech 3GPP je CMC integrován do bezpečnostních architektur pro služby jako doručování klíčů pro Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), zákonné odposlechy a zabezpečené poskytování služeb, což zajišťuje, že zařízení a síťové prvky mohou získat důvěryhodné přihlašovací údaje automatizovaným a škálovatelným způsobem.

Úloha CMC v síti je základní pro umožnění důvěryhodné komunikace založené na kryptografii s veřejným klíčem. Automatizuje tradičně manuální procesy správy certifikátů, což je nezbytné pro rozsáhlá nasazení, jako jsou mobilní sítě s miliony zařízení. Tím, že poskytuje standardizovaný, bezpečný a flexibilní formát zpráv, umožňuje CMC sítím 3GPP implementovat robustní systémy PKI, které podporují autentizaci pro přístup k síti, autorizaci služeb a zabezpečenou skupinovou komunikaci, čímž tvoří kritickou vrstvu celkového bezpečnostního rámce sítě.

## K čemu slouží

CMC byl vytvořen, aby řešil potřebu standardizovaného, bezpečného a škálovatelného protokolu pro automatizovanou správu certifikátů v rámci infrastruktur veřejného klíče (PKI). Před jeho standardizací se registrace a správa certifikátů často spoléhaly na proprietární protokoly nebo manuální procesy, které byly náchylné k chybám, obtížně škálovatelné a postrádaly interoperabilitu mezi systémy různých výrobců. Růst internetových služeb a rostoucí závislost na digitálních certifikátech pro autentizaci v telekomunikacích si vyžádaly robustní řešení na bázi protokolu.

V kontextu sítí 3GPP bylo přijetí CMC motivováno požadavkem na bezpečnou distribuci klíčů a správu přihlašovacích údajů v nově vznikajících službách. Například služba Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) vyžaduje bezpečné doručení šifrovacích klíčů velké skupině uživatelů, což je závislé na PKI. Manuální distribuce certifikátů pro takové služby je nepraktická. CMC poskytuje automatizovaný mechanismus, kterým zařízení mohou žádat a přijímat potřebné certifikáty od důvěryhodné [CA](/mobilnisite/slovnik/ca/), což umožňuje škálovatelnou a bezpečnou skupinovou komunikaci. Podobně pro zákonné odposlechy a další citlivé síťové funkce jsou důvěryhodné certifikáty nezbytné pro autentizaci monitorovacího zařízení a zajištění integrity zachycených dat.

CMC tyto problémy řeší definováním společného jazyka pro transakce správy certifikátů. Zajišťuje, že žádosti a odpovědi jsou kryptograficky chráněny pomocí CMS, čímž zabraňuje manipulaci a falšování. Jeho flexibilita mu umožňuje podporovat různé scénáře registrace (jako počáteční, obnova a aktualizace klíče) a složitá vyjednávání politik. Integrací CMC umožňují standardy 3GPP konzistentní, na výrobci nezávislý přístup ke správě životního cyklu certifikátů, což je klíčové pro udržení důvěry, umožnění automatizace a snížení provozních nákladů v rozsáhlých, heterogenních mobilních sítích.

## Klíčové vlastnosti

- Standardizované formáty zpráv pro žádosti o registraci, obnovu a odvolání certifikátů
- Postaveno na Cryptographic Message Syntax (CMS) pro integritu, autentizaci a důvěrnost
- Podpora hromadného zpracování více certifikačních žádostí v jedné zprávě
- Mechanismy pro prokázání držení soukromých klíčů k zabránění neoprávněnému vydání
- Možnost odloženého zpracování a čekajících odpovědí od certifikační autority
- Nezávislost na transportu, umožňující fungování nad protokoly jako HTTP/S používané v systémech 3GPP

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 33.221** (Rel-19) — Subscriber Certificate Distribution via GBA
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 45.009** (Rel-19) — GSM AMR Link Adaptation & Control

---

📖 **Anglický originál a plná specifikace:** [CMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cmc/)
