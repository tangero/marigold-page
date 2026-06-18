---
slug: "prins"
url: "/mobilnisite/slovnik/prins/"
type: "slovnik"
title: "PRINS – Protocol for N32 Interconnect Security"
date: 2026-01-01
abbr: "PRINS"
fullName: "Protocol for N32 Interconnect Security"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/prins/"
summary: "Bezpečnostní protokol definovaný 3GPP pro ochranu signalizačních zpráv vyměňovaných mezi dvěma samostatnými sítěmi 5G Core přes rozhraní N32. Zajišťuje důvěrnost, integritu a ochranu proti opětovnému"
---

PRINS je bezpečnostní protokol 3GPP, který chrání signalizační zprávy přenášené přes rozhraní N32 mezi samostatnými sítěmi 5G Core, a zajišťuje tak důvěrnost, integritu a ochranu proti opětovnému přehrání pro komunikaci mezi různými veřejnými pozemními mobilními sítěmi (inter-PLMN), například při roamingu.

## Popis

PRINS (Protocol for N32 Interconnect Security) je standardizovaný bezpečnostní mechanismus specifikovaný v 3GPP pro zabezpečení rozhraní N32, které propojuje proxy pro ochranu hran sítě ([SEPP](/mobilnisite/slovnik/sepp/)) dvou různých veřejných pozemních mobilních sítí ([PLMN](/mobilnisite/slovnik/plmn/)). Rozhraní N32 se používá pro signalizaci mezi PLMN, především v situacích roamingu a vzájemného propojení, kdy síťové funkce ([NF](/mobilnisite/slovnik/nf/)) jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) nebo [UDM](/mobilnisite/slovnik/udm/) v jedné PLMN potřebují komunikovat s protějšky v jiné PLMN. PRINS poskytuje těmto signalizačním zprávám mezi SEPP koncovou ochranu, která zajišťuje, že citlivá data procházející přes nedůvěryhodné síťové hranice zůstanou v bezpečí.

Z architektonického hlediska PRINS funguje na aplikační vrstvě a využívá standardy [JSON](/mobilnisite/slovnik/json/) Web Encryption ([JWE](/mobilnisite/slovnik/jwe/)) a JSON Web Signature (JWS) definované v IETF RFC, upravené pro případy užití 3GPP. Protokol funguje tak, že zdrojový SEPP zašifruje a zajistí integritu zpráv založených na HTTP/2 pro rozhraní N32 (přičemž pro mezilehlé zabezpečení používá protokoly jako HTTP/2 s TLS) před jejich předáním cílovému SEPP. Cílový SEPP následně zprávy ověří a dešifruje. PRINS podporuje dva režimy: „přímý režim“, kde je mezi SEPP navázána důvěra založená na předem sdíleném klíči nebo certifikátech, a „nepřímý režim“, který může zahrnovat bezpečnostního zprostředkovatele pro správu klíčů. Mezi klíčové komponenty patří bezpečnostní politiky vyjednané přes rozhraní N32-f, mechanismy odvozování klíčů a algoritmy pro šifrování (např. AES-GCM) a podepisování (např. ES256).

Jak to funguje: Když síťová funkce (NF) v domovské PLMN odešle signalizační zprávu (například aktualizaci předplatného) do navštívené PLMN, dorazí tato zpráva k domovskému SEPP. Domovský SEPP použije PRISN tak, že serializuje zprávu do objektu JWE pro důvěrnost a volitelně ji zabalí do JWS pro integritu. Tato chráněná datová část je poté přenesena přes N32 k SEPP navštívené PLMN, který ověří JWS (pokud je použit) a dešifruje JWE pomocí klíčů navázaných v předchozím bezpečnostním spojení. Dešifrovaná zpráva je předána cílové NF. Tento proces zajišťuje, že i v případě narušení spojení mezi PLMN je obsah zprávy a její původ chráněn, čímž se předchází odposlechu, pozměňování nebo opětovnému přehrání útoků.

## K čemu slouží

PRINS byl vytvořen v 3GPP Release 15, aby řešil bezpečnostní zranitelnosti vlastní signalizaci mezi PLMN, které se staly kritičtějšími s rozšířenými roamingovými schopnostmi a vystavením sítě v 5G. Před 5G se signalizace mezi sítěmi často spoléhala na mezilehlé zabezpečení (např. IPsec nebo TLS mezi uzly), což však zanechávalo zprávy vystavené v mezilehlých bodech uvnitř cizích sítí a riskovalo tak narušení dat a útoky, jako je vkládání zpráv. Motivací bylo poskytnout skutečnou koncovou ochranu mezi PLMN, která zajistí, že obsah signalizace mohou přistupovat pouze zamýšlení SEPP.

Vývoj PRINS byl hnán architekturou založenou na službách (SBA) v 5G, která pro komunikaci NF používá API HTTP/2 sahající přes síťové hranice. Bez PRINS by mohly být citlivé informace, jako jsou identifikátory účastníků, údaje o poloze nebo parametry služby, zachyceny nebo pozměněny, což by ohrozilo soukromí a integritu sítě. PRINS tento problém řeší šifrováním a podepisováním zpráv na aplikační vrstvě nezávisle na zabezpečení podkladového přenosu, čímž chrání data i v případě narušení přenosových spojů.

Historicky měly dřívější generace mobilních sítí méně formalizované zabezpečení mezi PLMN, spoléhaly se na bilaterální dohody a základní šifrování. PRINS zavádí standardizovaný, škálovatelný protokol, který podporuje automatizovanou správu klíčů a vyjednávání politik přes rozhraní N32-f, což umožňuje bezproblémový a bezpečný roaming v prostředí více dodavatelů. Řeší také regulatorní požadavky na ochranu dat (např. GDPR) a posiluje důvěru v ekosystémy 5G, usnadňuje globální interoperabilitu a zároveň zmírňuje rizika stále sofistikovanějších kybernetických hrozeb.

## Klíčové vlastnosti

- Koncové šifrování a ochrana integrity pro signalizační zprávy rozhraní N32
- Používá standardy JWE a JWS pro zabezpečení na aplikační vrstvě
- Podporuje přímý i nepřímý bezpečnostní režim včetně správy klíčů
- Integruje se s SEPP pro ochranu hran mezi PLMN
- Poskytuje ochranu proti opětovnému přehrání a ověření původu
- Umožňuje vyjednávání politik přes rozhraní N32-f

## Související pojmy

- [SEPP – Security Edge Protection Proxy](/mobilnisite/slovnik/sepp/)
- [JWE – JSON Web Encryption](/mobilnisite/slovnik/jwe/)

## Definující specifikace

- **TS 29.573** (Rel-19) — PLMN/SNPN Interconnection Interface Stage 3
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [PRINS na 3GPP Explorer](https://3gpp-explorer.com/glossary/prins/)
