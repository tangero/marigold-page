---
slug: "uuid"
url: "/mobilnisite/slovnik/uuid/"
type: "slovnik"
title: "UUID – Universally Unique IDentifier"
date: 2026-01-01
abbr: "UUID"
fullName: "Universally Unique IDentifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uuid/"
summary: "UUID je standardizovaný 128bitový identifikátor používaný v systémech 3GPP k jednoznačnému pojmenování zdrojů, služeb nebo entit bez nutnosti centralizované koordinace. Je klíčový pro síťové krájení ("
---

UUID je standardizovaný 128bitový identifikátor používaný v systémech 3GPP k jednoznačnému pojmenování zdrojů, služeb nebo entit bez nutnosti centralizované koordinace, což umožňuje jednoznačnou identifikaci napříč distribuovanými systémy.

## Popis

Universally Unique Identifier (UUID), jak je standardizován 3GPP, je 128bitová značka používaná pro jednoznačnou identifikaci informací v síťových systémech. Jeho struktura a metody generování jsou založeny na [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 4122, což zajišťuje s extrémně vysokou pravděpodobností globální jedinečnost. V rámci architektur 3GPP se UUID používají jako perzistentní, neprůhledné identifikátory pro širokou škálu entit, včetně, ale ne pouze, instancí síťového krájení (Network Slice Instances), instancí podsítě síťového krájení (Network Slice Subnet Instances), aplikačních funkcí (Application Functions), konzumentů služeb a specifických servisních dat. 128bitová hodnota je typicky reprezentována jako 32místný hexadecimální řetězec zobrazený v pěti skupinách oddělených pomlčkami (např. 123e4567-e89b-12d3-a456-426614174000).

Z architektonického hlediska fungují UUID jako klíčové prvky v rozhraních založených na službách (SBIs) a síťovém krájení. V jádru sítě 5G (5G Core) je například každé instanci síťového krájení (Network Slice Instance) přiřazen UUID ([S-NSSAI](/mobilnisite/slovnik/s-nssai/) je identifikátor, ale není UUID; [NSI](/mobilnisite/slovnik/nsi/) ID může být UUID). Konkrétněji se UUID používají k identifikaci šablon síťového krájení nebo specifických instancí služeb v rámci funkce správy síťového krájení ([NSMF](/mobilnisite/slovnik/nsmf/)) a funkce správy podsítě síťového krájení (NSSMF). Když se komponenta architektury založené na službách, jako je funkce síťového repozitáře ([NRF](/mobilnisite/slovnik/nrf/)), registruje nebo vyhledává službu, identifikátor instance služby může být UUID. Generování UUID nevyžaduje centrální vydávající autoritu; může být vytvořeno lokálně libovolnou systémovou komponentou pomocí algoritmů, které zahrnují jedinečné prvky, jako je časová značka, náhodná čísla a identifikátor uzlu (často [MAC](/mobilnisite/slovnik/mac/) adresa). Toto decentralizované generování je klíčové pro jeho škálovatelnost.

Jak to funguje v praxi, zahrnuje vložení UUID do protokolových zpráv a datových modelů. Například v systému 5G používá společný aplikační rozhraní ([CAPIF](/mobilnisite/slovnik/capif/)) UUID k jednoznačné identifikaci vyvolavatelů, poskytovatelů a služeb API. V řízení síťového krájení, definovaném v TS 28.531, identifikují UUID řídicí služby a zdroje. UUID je přenášeno v hlavičkách HTTP/2 nebo v datových částech JSON v RESTful API voláních mezi síťovými funkcemi. Jeho úlohou je poskytnout úchyt odolný proti kolizím, který lze použít pro odkazování, korelaci a správu životního cyklu distribuovaných zdrojů bez nejednoznačnosti, což je zásadní pro automatizaci, orchestraci a provoz ve více doménách v komplexních sítích 5G a budoucích.

## K čemu slouží

UUID bylo do standardů 3GPP zavedeno, aby vyřešilo problém generování globálně jedinečných identifikátorů decentralizovaným a škálovatelným způsobem pro architektury sítí nové generace. Předchozí přístupy často spoléhaly na hierarchická, centrálně spravovaná číslovací schémata (jako IP adresy nebo rozsahy IMSI), která mohla vytvářet úzká místa, jednotné body selhání a režii koordinace. Jak se sítě vyvíjely směrem k cloud-nativním, na službách založeným architekturám se síťovým krájením a masivním IoT, potřeba lehkého, samostatně generovaného a statisticky zaručeného jedinečného identifikátoru se stala prvořadou.

Historicky byly UUID zavedeny od 3GPP Release 8, což se časově shodovalo s ranými pracemi na vývoji systémové architektury (SAE) a rozvinutém paketovém jádru (EPC), kde našly využití v řídicích rozhraních. Jejich význam prudce vzrostl s návrhem 5G, konkrétně pro síťové krájení a rozhraní založená na službách. UUID řeší omezení předchozích ad-hoc nebo operátorsky specifických identifikačních schémat tím, že poskytují standardizovaný formát, který zajišťuje, že žádné dva nezávisle vygenerované identifikátory nebudou v konfliktu, a to ani napříč různými dodavateli a operátory. To je klíčové pro umožnění automatizované orchestrace, bezproblémového zjišťování služeb a jednoznačné správy milionů dynamických instancí síťového krájení a koncových bodů služeb v prostředí více dodavatelů a více domén.

## Klíčové vlastnosti

- 128bitový identifikátor zajišťující globální jedinečnost s zanedbatelnou pravděpodobností kolize
- Decentralizované generování bez potřeby centrální registrační autority
- Standardizovaná řetězcová reprezentace (formát 8-4-4-4-12 hex) pro interoperabilitu
- Používá se jako klíčový identifikátor v architektuře 5G založené na službách a RESTful API
- Zásadní pro jednoznačnou identifikaci instancí síťového krájení (Network Slice Instances) a řídicích služeb
- Podporován v četných specifikacích 3GPP pro řízení, zabezpečení a architekturu

## Související pojmy

- [NSSAI – Network Slice Selection Assistance Information](/mobilnisite/slovnik/nssai/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)
- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TR 33.876** (Rel-18) — Technical Report on Certificate Management

---

📖 **Anglický originál a plná specifikace:** [UUID na 3GPP Explorer](https://3gpp-explorer.com/glossary/uuid/)
