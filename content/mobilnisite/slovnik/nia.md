---
slug: "nia"
url: "/mobilnisite/slovnik/nia/"
type: "slovnik"
title: "NIA – New radio Integrity Algorithm"
date: 2026-01-01
abbr: "NIA"
fullName: "New radio Integrity Algorithm"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nia/"
summary: "NIA je sada kryptografických algoritmů poskytující ochranu integrity pro signalizaci a uživatelská data v 5G. Zajišťuje, že data nejsou během přenosu mezi UE a sítí pozměněna. Její standardizovaná sad"
---

NIA je standardizovaná sada kryptografických algoritmů, která zajišťuje ochranu integrity signalizace a uživatelských dat v 5G, čímž zaručuje, že nejsou během přenosu pozměněna.

## Popis

New radio Integrity Algorithm (NIA) je klíčovou součástí bezpečnostní architektury 5G, definovanou ve specifikaci 3GPP 33.501. Poskytuje ochranu integrity jak pro provoz řídicí roviny (signalizace), tak uživatelské roviny (data) přes rozhraní mezi uživatelským zařízením (UE) a gNodeB (gNB). Ochrana integrity je základní bezpečnostní služba, která garantuje, že přijatá data nebyla během přenosu neoprávněnou stranou změněna, smazána, zopakována nebo vložena. Sada NIA je navržena tak, aby fungovala ve spojení s šifrovacím algoritmem New radio Encryption Algorithm ([NEA](/mobilnisite/slovnik/nea/)) pro důvěrnost, čímž vytváří komplexní kryptografickou ochrannou vrstvu pro 5G NR.

NIA funguje ve vrstvě Packet Data Convergence Protocol (PDCP) v rádiovém protokolovém zásobníku. Pro každý datový paket vysílající entita (UE nebo gNB) vypočítá Message Authentication Code ([MAC-I](/mobilnisite/slovnik/mac-i/)) pomocí integritního algoritmu, integritního klíče (K~RRCint~ pro signalizaci nebo K~UPint~ pro uživatelská data), hodnoty čítače (PDCP COUNT), identity přenosového kanálu a směru přenosu (uplink/downlink). Tento MAC-I je před přenosem připojen k PDCP Protocol Data Unit (PDU). Přijímající entita nezávisle přepočítá MAC-I pomocí stejných vstupů a přijatých dat. Poté porovná vypočítanou hodnotu (XMAC-I) s přijatým MAC-I. Pokud se shodují, integrita dat je ověřena; pokud ne, paket je zahozen a může být zahájen postup řešení bezpečnostní chyby.

Sada NIA není jediný algoritmus, ale rodina algoritmů, což umožňuje jejich agilitu. Počáteční sada ve verzi 15 zahrnovala NIA0, NIA1 a NIA2. NIA0 je 'nulový' integritní algoritmus, který neposkytuje žádnou ochranu a používá se pouze ve specifických, předem definovaných výjimečných případech. NIA1 je založen na proudové šifře SNOW 3G, což je převzatý algoritmus z bezpečnosti 3G a 4G pro zpětnou kompatibilitu a migraci. NIA2 je založen na režimu AES-CTR s použitím 128bitového klíče a nabízí silnou, moderní kryptografickou ochranu. Výběr konkrétního algoritmu NIA pro spojení je dohodnut během procedury příkazu zabezpečeného režimu mezi UE a funkcí správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v jádru sítě na základě bezpečnostních schopností oznámených UE a bezpečnostní politiky sítě.

Tento integritní mechanismus je klíčový pro prevenci útoků, jako je padělání zpráv, opakovací útoky a manipulace typu man-in-the-middle. Chrání kritické signalizační procedury, jako je připojení, předávání spojení a správa relací, a zajišťuje bezpečnou kontrolu sítě nad UE. Pro uživatelská data garantuje, že přijatá aplikační data jsou přesně taková, jaká byla odeslána, což je zásadní pro služby vyžadující vysokou míru jistoty dat. Oddělení integritních klíčů pro řídicí a uživatelskou rovinu (K~RRCint~ a K~UPint~) poskytuje dodatečnou bezpečnostní izolaci. Ochrana integrity je aplikována koncově mezi UE a gNB na rádiovém spoji, což je nejzranitelnější segment spojení.

## K čemu slouží

Hlavním účelem NIA je poskytnout standardizovaný, robustní a budoucím výzvám odolný mechanismus pro ochranu integrity dat v systému 5G. Jak se mobilní sítě vyvíjely směrem k 5G, podporujíce širokou škálu nových služeb, jako je massive IoT, ultra-spolehlivá komunikace s nízkou latencí (URLLC) a vylepšené mobilní širokopásmové připojení (eMBB), významně se rozšířilo spektrum hrozeb. Předchozí generace měly ochranu integrity (např. [EIA](/mobilnisite/slovnik/eia/) v LTE), ale 5G vyžadovalo algoritmy schopné splnit vyšší požadavky na výkon z hlediska latence a propustnosti a zároveň odolávat sofistikovanějším kryptografickým útokům. Vytvoření nové sady algoritmů pod hlavičkou 'NIA' bylo motivováno potřebou agility algoritmů – schopnosti zavádět v průběhu času nové, silnější algoritmy bez nutnosti přestavby celé bezpečnostní architektury, a tím reagovat na pokroky v kryptoanalýze a výpočetním výkonu.

Další klíčovou motivací bylo řešení specifických zranitelností identifikovaných v předchozích systémech. Například v LTE byla ochrana integrity povinná pro signalizaci, ale pro data uživatelské roviny volitelná. To v mnoha nasazeních ponechávalo uživatelská data zranitelná vůči určitým útokům přes rádiové rozhraní. 3GPP v 5G vědomě rozhodlo o povinném zavedení ochrany integrity pro uživatelskou rovinu ve výchozím nastavení, přičemž ji může síťový operátor pro konkrétní datové rádiové kanály ([DRB](/mobilnisite/slovnik/drb/)) v případě potřeby z důvodu výkonu deaktivovat (pomocí NIA0). Tento posun významně zvyšuje základní úroveň zabezpečení. Návrh také explicitně odděluje kryptografické řetězce pro integritu a důvěrnost, čímž zabraňuje potenciálním slabinám v jednom algoritmu ohrozit druhou službu.

Kromě toho byl vývoj NIA součástí holistického přepracování bezpečnosti 5G, které zahrnovalo domácí kontrolu a vylepšenou hierarchii klíčů. Integritní klíče jsou odvozeny z kořenového klíče v domovské síti, což zajišťuje, že i v roamingu je integrita spojení ukotvena k domácímu operátorovi účastníka. Tím se řeší obavy ohledně zabezpečení navštívené sítě. Standardizací jasné sady algoritmů (NIA1, NIA2) a jasného nulového algoritmu (NIA0) zajišťuje 3GPP globální interoperabilitu a zároveň dává operátorům nástroje pro nasazení zabezpečení odpovídajícího jejich posouzení rizik a požadavkům různých síťových řezů.

## Klíčové vlastnosti

- Poskytuje ochranu integrity pro data řídicí roviny (RRC) i uživatelské roviny (UP) v 5G NR
- Implementuje agilitu algoritmů s definovanou sadou zahrnující NIA0 (nulový), NIA1 (SNOW 3G) a NIA2 (AES-128)
- Funguje ve vrstvě PDCP s využitím Message Authentication Code (MAC-I) připojeného ke každému paketu
- Používá samostatné integritní klíče (K_RRCint, K_UPint) odvozené z kotvového klíče jádra 5G sítě
- Chrání proti pozměňování dat, opakování a vkládání útoků na rádiovém rozhraní
- Povinná podpora integrity uživatelské roviny, což zvyšuje základní úroveň zabezpečení ve srovnání s LTE

## Související pojmy

- [NEA – NR Encryption Algorithm](/mobilnisite/slovnik/nea/)
- [MAC-I – Message Authentication Code for Integrity](/mobilnisite/slovnik/mac-i/)

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [NIA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nia/)
