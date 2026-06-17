---
slug: "eea"
url: "/mobilnisite/slovnik/eea/"
type: "slovnik"
title: "EEA – EPS Encryption Algorithm"
date: 2025-01-01
abbr: "EEA"
fullName: "EPS Encryption Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/eea/"
summary: "Sada standardizovaných kryptografických algoritmů používaných k šifrování uživatelských dat a signalizačních zpráv na rozhraních LTE Evolved Packet System (EPS). Zajišťuje důvěrnost a integritu komuni"
---

EEA je sada standardizovaných kryptografických algoritmů používaných k šifrování uživatelských dat a signalizačních zpráv na rozhraních LTE Evolved Packet System, které zajišťují důvěrnost a integritu komunikace.

## Popis

EPS Encryption Algorithm (EEA) je soubor kryptografických algoritmů specifikovaných 3GPP, který poskytuje ochranu důvěrnosti pro data uživatelské roviny a signalizaci řídicí roviny v rámci Evolved Packet System (EPS). Funguje ve spojení s EPS Integrity Algorithm ([EIA](/mobilnisite/slovnik/eia/)) a společně tvoří kompletní sadu kryptografických primitiv pro bezpečnostní rámec LTE známý jako bezpečnost [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) a [AS](/mobilnisite/slovnik/as/) (Access Stratum). Algoritmy jsou implementovány v User Equipment (UE) a v bezpečnostních entitách sítě – konkrétně v eNodeB pro bezpečnost AS a v [MME](/mobilnisite/slovnik/mme/) (Mobility Management Entity) pro bezpečnost NAS.

Fungování EEA je nedílnou součástí procesu LTE authentication and key agreement ([AKA](/mobilnisite/slovnik/aka/)). Po úspěšné vzájemné autentizaci mezi UE a sítí je vytvořen kořenový klíč (K_[ASME](/mobilnisite/slovnik/asme/)). Z tohoto kořenového klíče je odvozen šifrovací klíč (K_[eNB](/mobilnisite/slovnik/enb/)), který se dále používá ke generování specifických šifrovacích klíčů (např. K_UPenc, K_RRCenc) pro různé kanály. Algoritmus EEA poté používá tyto dynamicky generované klíče k zašifrování dat. Šifrování je aplikováno pomocí proudové šifry nebo blokové šifry v určitém režimu provozu, čímž se prostý text transformuje na šifrovaný text, aby se zabránilo odposlechu na rozhraní rádiového přístupu a v páteřní síti.

Hlavními algoritmy EEA jsou EEA0 (nulová šifra), 128-EEA1 (založený na SNOW 3G), 128-EEA2 (založený na AES-CTR) a 128-EEA3 (založený na ZUC). EEA0 neposkytuje žádné šifrování a používá se pouze ve specifických, předem definovaných situacích. Výběr toho, který algoritmus použít, je vyjednán během procedury Security Mode Command mezi sítí a UE na základě jejich vzájemně podporovaných možností. Šifrování je aplikováno na úrovni každého přenosového kanálu (bearer) a pro každý směr přenosu (uplink/downlink), což zajišťuje detailní zabezpečení. Role sady EEA je klíčová pro ochranu proti hrozbám na rozhraní vzduchu, čímž se stává základní součástí bezpečnostní architektury LTE podrobně popsané v TS 33.401.

## K čemu slouží

Sada EPS Encryption Algorithm byla vytvořena k řešení bezpečnostních požadavků nové architektury LTE plně založené na IP, která přinesla odlišné modely hrozeb ve srovnání s předchozími 3G sítěmi s přepojováním okruhů. Předchozí bezpečnostní mechanismy z 2G/3G, ačkoli byly ve své době robustní, používaly starší kryptografické algoritmy a měly architektonická omezení. Přechod na plošší, na IP založený EPS vyžadoval novou, silnější a flexibilnější sadu algoritmů, aby byla zajištěna důvěrnost uživatelských dat a ochrana proti sofistikovaným útokům na rádiovou přístupovou síť.

Motivací pro vývoj více algoritmů (SNOW 3G, [AES](/mobilnisite/slovnik/aes/), ZUC) bylo poskytnout kryptografickou agilitu a sladit se s globálními regulačními požadavky. Různé regiony mají preference nebo nařízení pro konkrétní kryptografické standardy (např. AES je standard NIST, zatímco ZUC je čínský standard). Standardizací celé sady zajistil 3GPP globální interoperabilitu, a zároveň umožnil operátorům a regulátorům vybrat algoritmy vyhovující místním předpisům. Tento přístup vyřešil problém jednoho bodu selhání; pokud je u jednoho algoritmu objevena zranitelnost, sítě mohou přejít na jiný bez nutnosti kompletní přestavby bezpečnostní architektury. EEA, jako součást bezpečnostního rámce LTE, byla navržena od základů tak, aby poskytovala robustní ochranu důvěrnosti s kryptografickou agilitou vhodnou pro vysokorychlostní mobilní širokopásmové služby.

## Klíčové vlastnosti

- Sada algoritmů zahrnující EEA1 (SNOW 3G), EEA2 (AES-CTR) a EEA3 (ZUC)
- Poskytuje důvěrnost pro data uživatelské roviny a signalizační zprávy RRC/NAS
- Klíče jsou dynamicky odvozovány z procesu LTE AKA pro každou relaci
- Vyjednání algoritmu prostřednictvím procedury Security Mode Command
- Podporuje kryptografickou agilitu pro regionální a regulatorní shodu
- Aplikováno na úrovni každého rádiového přenosového kanálu (bearer) a pro každý směr přenosu

## Související pojmy

- [EIA – EPS Integrity Algorithm](/mobilnisite/slovnik/eia/)
- [EPS – Evolved Packet System](/mobilnisite/slovnik/eps/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture

---

📖 **Anglický originál a plná specifikace:** [EEA na 3GPP Explorer](https://3gpp-explorer.com/glossary/eea/)
