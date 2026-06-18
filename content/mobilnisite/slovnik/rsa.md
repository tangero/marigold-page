---
slug: "rsa"
url: "/mobilnisite/slovnik/rsa/"
type: "slovnik"
title: "RSA – Rivest-Shamir-Adleman"
date: 2025-01-01
abbr: "RSA"
fullName: "Rivest-Shamir-Adleman"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsa/"
summary: "RSA je široce používaný kryptosystém s veřejným klíčem pro zabezpečený přenos dat, digitální podpisy a výměnu klíčů v sítích 3GPP. Poskytuje důvěrnost, autentizaci a integritu a tvoří základ bezpečnos"
---

RSA je kryptosystém s veřejným klíčem používaný v sítích 3GPP pro zabezpečený přenos dat, digitální podpisy a výměnu klíčů za účelem zajištění důvěrnosti, autentizace a integrity.

## Popis

RSA (Rivest-Shamir-Adleman) je asymetrický kryptografický algoritmus, který tvoří základní součást bezpečnostních architektur ve standardech 3GPP. Funguje na principu páru veřejného a privátního klíče, přičemž veřejný klíč se používá pro šifrování nebo ověřování podpisu a privátní klíč je utajený a slouží k dešifrování nebo generování podpisu. V systémech 3GPP se RSA používá v různých bezpečnostních mechanismech, včetně autentizace, dohod o klíčích a digitálních podpisů pro síťové prvky a uživatelské zařízení (UE). Bezpečnost algoritmu je založena na výpočetní náročnosti faktorizace velkých celých čísel, která jsou odvozena od dvou velkých prvočísel.

V sítích 3GPP RSA funguje prostřednictvím integrace do protokolů a rozhraní vyšších vrstev. Například v procedurách autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) může být RSA použita pro zabezpečení výměny klíčů mezi UE a sítí, zejména v raných vydáních 3G. Architektura zahrnuje komponenty jako Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Authentication Centre (AuC) a univerzální integrovaný obvodovou kartu (UICC) nebo [SIM](/mobilnisite/slovnik/sim/) v UE. Klíče RSA jsou generovány a spravovány certifikačními autoritami ([CA](/mobilnisite/slovnik/ca/)) a distribuovány prostřednictvím systémů infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)), což zajišťuje, že se do zabezpečené komunikace mohou zapojit pouze autorizované entity. Specifikace jako 3GPP TS 33.303 (pro PKI) a TS 31.113 (pro zabezpečení UICC) podrobně popisují implementaci a použití RSA.

Role algoritmu se rozšiřuje na zabezpečení signalizačních a uživatelských dat. V protokolech jako [IPsec](/mobilnisite/slovnik/ipsec/) a [TLS](/mobilnisite/slovnik/tls/) používaných pro rozhraní jádra sítě (např. N1, [N2](/mobilnisite/slovnik/n2/) v 5G) může být RSA využita pro výměnu klíčů při navazování tunelu. Dále digitální podpisy RSA ověřují pravost softwarových aktualizací, certifikátů a síťových zpráv, čímž zabraňují manipulaci a podvržení. Jeho integrace do systémů 3GPP zajišťuje end-to-end zabezpečení napříč doménami rádiového přístupu a jádra sítě a chrání před odposlechem, útoky typu man-in-the-middle a neoprávněným přístupem.

## K čemu slouží

RSA byla přijata do standardů 3GPP počínaje vydáním 6, aby řešila rostoucí potřebu robustního zabezpečení v celulárních sítích, zejména s přechodem na paketově orientované služby a internetovou konektivitu. Předchozí asymetrické kryptosystémy byly méně standardizované nebo efektivní a samotné algoritmy se symetrickým klíčem nemohly poskytnout škálovatelnou autentizaci a distribuci klíčů. Zavedení RSA umožnilo zabezpečenou výměnu klíčů bez předem sdílených tajemství, což usnadnilo rozsáhlá nasazení a interoperabilitu mezi různými dodavateli a operátory.

Motivace pro zahrnutí RSA pramenila z omezení dřívějších bezpečnostních mechanismů v systémech 2G a raného 3G, které se silně spoléhaly na symetrickou kryptografii a byly zranitelné vůči určitým útokům. RSA poskytla způsob, jak implementovat digitální podpisy pro síťovou autentizaci a nepopiratelnost, čímž zvýšila důvěru v roamingových scénářích a přístupu ke službám. Také podpořila vývoj směrem k IP sítím, kde se infrastruktura veřejných klíčů stala nezbytnou pro zabezpečení rozhraní, jako jsou ta mezi síťovými funkcemi.

Dále se role RSA v 3GPP vyvinula tak, aby podporovala pokročilé funkce, jako je zabezpečené poskytování služeb, zákonné odposlouchávání a ověřování integrity zařízení. Jak sítě postupovaly k 4G a 5G, RSA zůstala relevantní pro autentizaci založenou na certifikátech a zpětnou kompatibilitu, i když novější algoritmy, jako je kryptografie eliptických křivek (ECC), získaly na významu díky vyšší efektivitě. Její trvalá přítomnost podtrhuje její důležitost pro udržení vrstveného přístupu k zabezpečení v architekturách 3GPP.

## Klíčové vlastnosti

- Asymetrické šifrování využívající páry veřejného a privátního klíče
- Podpora digitálních podpisů pro autentizaci a integritu
- Umožňuje zabezpečenou výměnu klíčů bez předem sdílených tajemství
- Založeno na matematické náročnosti faktorizace celých čísel
- Integruje se s PKI pro správu certifikátů
- Používá se v AKA procedurách a pro zabezpečení síťových rozhraní

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [PKI – Public Key Infrastructure](/mobilnisite/slovnik/pki/)
- [ECC – European Electronic Communications Committee](/mobilnisite/slovnik/ecc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [RSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsa/)
