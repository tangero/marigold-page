---
slug: "a-kid"
url: "/mobilnisite/slovnik/a-kid/"
type: "slovnik"
title: "A-KID – AKMA Key IDentifier"
date: 2025-01-01
abbr: "A-KID"
fullName: "AKMA Key IDentifier"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/a-kid/"
summary: "Identifikátor klíče AKMA (A-KID) jednoznačně identifikuje aplikační klíč AKMA (K_AKMA) vygenerovaný během procedury ověření AKMA. Umožňuje aplikačním funkcím bezpečně získat K_AKMA z AAnF (kotvící fun"
---

A-KID je identifikátor, který jednoznačně identifikuje aplikační klíč AKMA a umožňuje aplikačním funkcím jeho bezpečné získání z kotvící funkce AKMA pro ověření služby.

## Popis

Identifikátor klíče AKMA (A-KID) je kritický bezpečnostní parametr v rámci architektury 3GPP Authentication and Key Management for Applications (AKMA), zavedené ve verzi 16. Slouží jako jednoznačný odkaz nebo ukazatel na konkrétní aplikační klíč AKMA (K_AKMA), který je bezpečně vygenerován a uložen kotvící funkcí AKMA (AAnF) v domovské síti. A-KID je generován AAnF a je vázán na konkrétní UE a instanci AAnF, která K_AKMA vytvořila. Jeho struktura a použití jsou definovány v několika specifikacích 3GPP, včetně TS 33.535 pro procedury AKMA a TS 24.501 pro jeho přenos v signalizaci Non-Access Stratum (NAS).

Z architektonického hlediska je A-KID generován AAnF po úspěšném primárním ověření UE (např. pomocí 5G AKA nebo EAP-AKA'). Během tohoto procesu AAnF odvodí K_AKMA z kotvícího klíče vytvořeného při tomto ověření. AAnF následně vytvoří A-KID, který typicky obsahuje informace pro jednoznačnou identifikaci kontextu klíče, jako je SUPI UE, identifikátor AAnF (AAnF-ID) a případně index klíče nebo parametr aktuálnosti. Tento A-KID je pak poskytnut UE, často v rámci příkazu pro nastavení zabezpečení NAS nebo podobné procedury, což umožňuje UE jej uložit pro budoucí použití s aplikačními službami.

Když se UE chce připojit k aplikační službě s podporou AKMA (hostované aplikační funkcí, AF), předloží A-KID této AF jako součást žádosti o ověření služby. AF, která K_AKMA nedisponuje, použije tento A-KID k dotazování na správnou AAnF (identifikovanou uvnitř A-KID) přes referenční bod N33. AAnF žádost ověří, na základě A-KID načte odpovídající K_AKMA a odvodí aplikačně specifické klíče (jako K_AF), které pak bezpečně poskytne AF. Tento proces umožňuje AF a UE navázat zabezpečenou relaci pomocí klíčů zakořeněných v přihlašovacích údajích 3GPP, aniž by AF kdy musela manipulovat s dlouhodobým klíčem účastníka.

Role A-KID v síti je zásadní pro bezpečnostní model AKMA. Funguje jako zabezpečený token, který autorizuje získání klíče, a zajišťuje, že pouze AF s platnou žádostí odpovídající dané konkrétní UE a kontextu klíče může získat odvozené klíče. Zabrání útokům typu key confusion tím, že jednoznačně váže žádost o získání na jedinou instanci K_AKMA. Návrh také podporuje správu životního cyklu klíčů; například pokud je K_AKMA obnoven nebo zneplatněn, bude vydán nový A-KID, čímž se starý identifikátor stane pro získání klíče neplatným, což poskytuje mechanismus pro forward secrecy na úrovni aplikačního klíče.

## K čemu slouží

A-KID byl vytvořen k řešení problému zabezpečeného a škálovatelného ověřování pro služby aplikací třetích stran (jako streamování, IoT nebo podnikové služby), které chtějí využít silné, na předplatném založené ověření sítí 3GPP, aniž by se přímo integrovaly s uzly jádra sítě jako UDM/AUSF. Před AKMA aplikace často spoléhaly na samostatné databáze přihlašovacích údajů (uživatelská jména/hesla, tokeny OAuth) nebo méně bezpečné metody, což vytvářelo třecí plochy pro uživatele a správní zátěž pro operátory. Účelem A-KID je poskytnout klíčový prvek tohoto nového paradigmatu – zabezpečený, sítí vydaný identifikátor, který odemyká kryptograficky silné, sítí odvozené klíče pro aplikace.

Historický kontext představuje odklon průmyslu k servisně orientovaným architekturám a otevřenému vystavování síťových schopností v 5G. Zatímco řešení jako GBA (Generic Bootstrapping Architecture) existovala již v dřívějších verzích, byla často vnímána jako složitá a ne zcela sladěná s principy cloud-nativního 5G jádra. AKMA, a tím i A-KID, byly navrženy jako integrovanější, na 5G nativně zaměřené řešení. A-KID konkrétně řeší omezení, jak může aplikační funkce, která je vzhledem k domovské síti nedůvěryhodná, bezpečně a jednoznačně požadovat klíče potřebné k ověření uživatele. Nahrazuje potřebu, aby aplikace znala podrobnosti o síťové relaci uživatele v jádru sítě, a poskytuje jednoduchý, neprůhledný identifikátor, který síť dokáže namapovat na bohatý bezpečnostní kontext vytvořený během primárního ověření.

A-KID dále umožňuje důležité bezpečnostní vlastnosti. Řeší problém identifikace a směrování klíčů v distribuovaném systému, kde může existovat více instancí AAnF. Zakódováním směrovacích informací (jako AAnF-ID) zajišťuje, že AF kontaktuje správnou síťovou funkci pro získání klíčů. Také řeší problém správy životního cyklu klíčů z pohledu aplikace. AF nemusí rozumět tomu, kdy je klíč účastníka obnoven; jednoduše předloží A-KID přijatý od UE. Pokud klíč již není platný, AAnF žádost na základě A-KID odmítne, což vyvolá nutnost, aby UE a AF navázaly novou relaci s novým A-KID, čímž je udržována bezpečnost.

## Klíčové vlastnosti

- Jednoznačně identifikuje aplikační klíč AKMA (K_AKMA) v rámci AAnF
- Umožňuje bezpečné získání klíče aplikačními funkcemi přes rozhraní N33
- Obsahuje směrovací informace (např. AAnF-ID) pro lokalizaci správné kotvící funkce klíče
- Vázán na konkrétní identitu UE (SUPI) a instanci primárního ověření
- Podporuje správu životního cyklu klíčů (aktuálnost, odvolání) prostřednictvím vydávání nových identifikátorů
- Neprůhledný pro UE a AF, čímž zachovává síťovou kontrolu nad mapováním klíčů a bezpečnostní politikou

## Definující specifikace

- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3
- **TS 29.535** (Rel-19) — 5G AKMA Anchor Services Stage 3 Protocol
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.535** (Rel-19) — 5G AKMA: Authentication and Key Management for Apps
- **TR 33.741** (Rel-18) — Home Network Triggered Authentication

---

📖 **Anglický originál a plná specifikace:** [A-KID na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-kid/)
