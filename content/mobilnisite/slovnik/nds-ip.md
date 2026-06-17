---
slug: "nds-ip"
url: "/mobilnisite/slovnik/nds-ip/"
type: "slovnik"
title: "NDS/IP – Network Domain Security for IP based Protocols"
date: 2025-01-01
abbr: "NDS/IP"
fullName: "Network Domain Security for IP based Protocols"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nds-ip/"
summary: "Specifický profil rámce NDS přizpůsobený pro zabezpečení komunikací v rámci jedné důvěryhodné IP síťové domény, jako je vlastní jádrová síť operátora. Typicky používá IPsec v transportním režimu nebo"
---

NDS/IP je specifický profil rámce zabezpečení síťové domény (Network Domain Security) pro zabezpečení komunikací v rámci jedné důvěryhodné IP síťové domény, typicky za použití IPsec nebo TLS.

## Popis

[NDS](/mobilnisite/slovnik/nds/)/IP (Network Domain Security for IP based Protocols) je specializovaný implementační profil širšího rámce zabezpečení síťové domény (NDS). Zatímco NDS obecně pokrývá mezidoménové zabezpečení (např. mezi operátory), NDS/IP se zaměřuje na poskytování zabezpečení *uvnitř* jedné administrativní IP síťové domény, která je považována za určitým způsobem inherentně důvěryhodnou, ale kde je stále vyžadováno dodatečné zabezpečení na vrstvě 3/4. Jeho hlavním cílem je chránit výměny IP protokolů mezi síťovými prvky, jako je například komunikace mezi [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) a [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) v 4G, nebo mezi různými síťovými funkcemi ([NF](/mobilnisite/slovnik/nf/)) v 5G, proti hrozbám pocházejícím z IP transportní sítě.

NDS/IP funguje tak, že aplikuje zabezpečení přímo mezi komunikujícími partnery, bez povinných mezilehlých bezpečnostních bran (SEG), které se používají v mezidoménovém modelu NDS. Nejběžněji specifikovaným mechanismem je použití [IPsec](/mobilnisite/slovnik/ipsec/), konkrétně protokolu [ESP](/mobilnisite/slovnik/esp/) (Encapsulating Security Payload), nakonfigurovaného v transportním režimu. V transportním režimu jsou hlavičky IPsec vloženy mezi původní IP hlavičku a datovou část, čímž chrání protokoly vyšších vrstev (jako je SCTP přenášející Diameter nebo [GTP-U](/mobilnisite/slovnik/gtp-u/)), zatímco původní IP adresy zůstávají viditelné pro směrování. To je pro přímou komunikaci efektivnější než tunelový režim. Správa klíčů je dosažena pomocí protokolu [IKE](/mobilnisite/slovnik/ike/) (Internet Key Exchange). V moderních nasazeních 5G jsou principy NDS/IP realizovány také pomocí TLS (Transport Layer Security) pro rozhraní založená na službách (SBI) využívající HTTP/2, jak to vyžaduje 3GPP pro komunikaci mezi síťovými funkcemi uvnitř domény.

Úlohou NDS/IP je vytvořit bezpečnou nadstavbu na interní IP páteři operátora. Zmírňuje rizika, jako jsou útoky insiderů, chybně nakonfigurované síťové vybavení nebo kompromitované uzly uvnitř domény, které by mohly odposlouchávat nebo manipulovat s citlivou signalizační komunikací (např. Diameter, GTP-C) a daty uživatelské roviny. Vynucením vzájemného ověření partnerů, autentizace původu dat, integrity a důvěrnosti zajišťuje, že i uvnitř „důvěryhodné“ domény kritické komunikace dodržují princip nejnižších oprávnění a obrany v hloubce. Je klíčovým prvkem pro virtualizaci sítě (NFV), kde funkce mohou běžet na sdíleném standardním hardwaru, což činí logickou izolaci pomocí NDS/IP zásadní.

## K čemu slouží

NDS/IP byl vyvinut pro řešení bezpečnostních požadavků vnitřní síťové domény operátora během přechodu na plně IP architekturu. Zatímco mezidoménový rámec NDS s branami SEG byl nezbytný pro hranice, operátoři potřebovali standardizovanou, efektivní metodu pro zabezpečení velkého objemu provozu proudícího *uvnitř* jejich vlastních sítí. Spoléhat se pouze na fyzické zabezpečení páteře bylo nedostatečné, zejména s nástupem distribuovaných architektur a potenciálem pro boční pohyb útočníků, kteří prolomili perimetr.

Před vznikem NDS/IP bylo zabezpečení uvnitř domény často zanedbáváno nebo implementováno nestandardními, dodavatelsky specifickými metodami, což vedlo k potenciálním mezerám a problémům s interoperabilitou. Vytvoření NDS/IP poskytlo standardizovaný 3GPP profil, který definoval, jak správně a konzistentně aplikovat IPsec (a později TLS) pro ochranu uvnitř domény. Vyřešil problém, jak efektivně zabezpečit spojení typu peer-to-peer bez režie plnohodnotných bran v tunelovém režimu, a přitom poskytnout robustní kryptografickou ochranu. To bylo obzvláště důležité pro signalizační protokoly jako Diameter, které přenášejí citlivá data o autentizaci účastníků a politikách, a zajišťovalo, že tyto informace zůstanou chráněny po celé cestě od zdroje k cíli uvnitř cloudu operátora.

## Klíčové vlastnosti

- Profil NDS pro zabezpečení uvnitř domény (v rámci jednoho operátora)
- Primárně používá IPsec ESP v transportním režimu pro přímé zabezpečení mezi partnery
- Využívá IKE pro automatizovanou správu klíčů a vzájemné ověřování partnerů
- Chrání IP řídicí rovinu (např. Diameter, GTP-C) a protokoly uživatelské roviny
- Vývoj směrem k povinnému použití TLS pro rozhraní založená na službách (SBI) v 5G
- Umožňuje obranu v hloubce uvnitř důvěryhodné administrativní domény

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 29.549** (Rel-19) — SEAL API Specification for Vertical Applications
- **TS 33.141** (Rel-19) — Security for Presence Service (Ut reference point)
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS

---

📖 **Anglický originál a plná specifikace:** [NDS/IP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nds-ip/)
