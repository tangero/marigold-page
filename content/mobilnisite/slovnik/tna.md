---
slug: "tna"
url: "/mobilnisite/slovnik/tna/"
type: "slovnik"
title: "TNA – Trusted Node Authentication"
date: 2025-01-01
abbr: "TNA"
fullName: "Trusted Node Authentication"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tna/"
summary: "Bezpečnostní mechanismus definovaný v 3GPP pro autentizaci důvěryhodných uzlů v síti, jako jsou síťové prvky nebo brány. Vytváří zabezpečený důvěryhodný vztah mezi entitami, který zajišťuje, že se na"
---

TNA je bezpečnostní mechanismus 3GPP pro autentizaci důvěryhodných síťových prvků za účelem navázání zabezpečených vztahů a zajištění, že se na síťových operacích mohou podílet pouze autorizované uzly.

## Popis

Trusted Node Authentication (TNA) je základní bezpečnostní koncept v architekturách 3GPP navržený pro autentizaci a autorizaci konkrétních síťových uzlů. Funguje na principu, že určité síťové prvky, jako jsou [MME](/mobilnisite/slovnik/mme/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/) nebo [PCRF](/mobilnisite/slovnik/pcrf/), jsou předem nakonfigurovány jako důvěryhodné entity. Proces autentizace typicky zahrnuje výměnu digitálních certifikátů nebo předem sdílených klíčů, které jsou ověřovány proti důvěryhodné certifikační autoritě nebo zabezpečenému systému správy klíčů. Tato vzájemná autentizace zajišťuje, že obě komunikující strany mohou ověřit identitu druhé strany před navázáním zabezpečeného spojení pro signalizaci a přenos uživatelských dat.

Architektura TNA je integrována do protokolů řídicí roviny a rozhraní mezi funkcemi jádrové sítě. Když uzel iniciuje spojení, předloží své přihlašovací údaje. Přijímající uzel ověří tyto údaje proti politice nebo důvěryhodné databázi. Úspěšná autentizace vede k navázání zabezpečeného spojení, často s využitím protokolů jako [TLS](/mobilnisite/slovnik/tls/) nebo [IPsec](/mobilnisite/slovnik/ipsec/), které následně chrání veškerou další komunikaci. Tento mechanismus je klíčový pro rozhraní jako S6a (mezi MME a [HSS](/mobilnisite/slovnik/hss/)), S5/S8 (mezi SGW a PGW) a Rx (mezi [PCEF](/mobilnisite/slovnik/pcef/) a PCRF), kde se vyměňují citlivá data účastníků a informace o politikách.

Klíčové součásti TNA zahrnují infrastrukturu Authentication, Authorization, and Accounting (AAA), Public Key Infrastructure (PKI) pro správu certifikátů a bezpečnostní politiky definované v každém síťovém prvku. Jeho úlohou je vytvořit zesílený bezpečnostní perimetr uvnitř jádrové sítě a oddělit ji od nedůvěryhodného přístupu. Tím, že zajišťuje komunikaci pouze mezi ověřenými a autorizovanými uzly, TNA zmírňuje rizika, jako jsou útoky typu man-in-the-middle, zosobnění uzlu a neoprávněné odposlechy signalizace, a tvoří tak kritickou vrstvu v strategii obrany do hloubky (defense-in-depth) pro mobilní sítě.

## K čemu slouží

TNA bylo zavedeno jako reakce na rostoucí potřebu robustní vnitřní síťové bezpečnosti s tím, jak se mobilní sítě vyvíjely směrem k plně IP architekturám. Před jeho formalizací se bezpečnost často zaměřovala primárně na rozhraní radiového přístupu a autentizaci uživatele, s méně standardizovanou ochranou rozhraní jádrové sítě mezi důvěryhodnými uzly. To činilo síťovou páteř zranitelnou vůči útokům, pokud by útočník získal přístup k IP transportní síti. Účelem TNA je zajistit, aby samotná jádrová síť byla důvěryhodnou doménou, kde je identita každého prvku ověřována.

Vznik TNA byl motivován přechodem na ploché IP architektury ve 3GPP Release 8 (EPC), což zvýšilo počet IP rozhraní mezi síťovými funkcemi. Toto rozšíření zvětšilo potenciální cílovou plochu pro útoky. TNA poskytuje standardizovanou metodu pro autentizaci těchto spojení a brání zavedení falešných síťových prvků do jádra. Řeší problém implicitní důvěry v rámci domény operátora a nahrazuje ji explicitní, kryptograficky ověřenou důvěrou, která je nezbytná pro umožnění bezpečného sdílení sítí, meziodběratelských spojení a ochrany před hrozbami zevnitř.

## Klíčové vlastnosti

- Vzájemná autentizace síťových uzlů pomocí certifikátů nebo předem sdílených klíčů
- Integrace s signalizačními protokoly a rozhraními jádrové sítě
- Základ pro navazování zabezpečených tunelů (např. IPsec) pro provoz řídicí roviny
- Ochrana proti zosobnění uzlů a útokům typu man-in-the-middle uvnitř jádra
- Podpora scénářů zabezpečené konektivity jak v rámci jednoho operátora, tak mezi operátory
- Umožňuje dodržování regulatorních a korporátních bezpečnostních politik pro síťovou infrastrukturu

## Definující specifikace

- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [TNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/tna/)
