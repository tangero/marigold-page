---
slug: "tnap"
url: "/mobilnisite/slovnik/tnap/"
type: "slovnik"
title: "TNAP – Trusted non-3GPP Access Peers"
date: 2026-01-01
abbr: "TNAP"
fullName: "Trusted non-3GPP Access Peers"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tnap/"
summary: "Síťové funkce nebo entity v rámci důvěryhodné ne-3GPP přístupové sítě, které přímo rozhraní s 5G Core. Slouží jako koncové body (peers) pro spojení řídicí roviny (N2) a uživatelské roviny (N3) a usnad"
---

TNAP je síťová funkce v rámci důvěryhodné ne-3GPP přístupové sítě, která slouží jako koncový bod (peer) pro připojení N2 a N3 k 5G Core a umožňuje integraci Wi-Fi a pevných sítí.

## Popis

Trusted non-3GPP Access Peers (TNAPy) je logický souhrnný termín pro síťové funkce v důvěryhodné ne-3GPP přístupové síti, které slouží jako přímé spojovací body k síti 5G Core. V praktickém nasazení je hlavním TNAPem funkce Trusted Non-3GPP Gateway Function ([TNGF](/mobilnisite/slovnik/tngf/)) pro obecný důvěryhodný přístup, nebo funkce Wireline Access Gateway Function ([W-AGF](/mobilnisite/slovnik/w-agf/)) pro specifické scénáře s pevnými sítěmi. Tyto funkce ukončují rozhraní definovaná 3GPP ze strany 5GC a efektivně překládají mezi signalizací 3GPP a nativními protokoly ne-3GPP přístupu (např. [IEEE](/mobilnisite/slovnik/ieee/) 802.11 pro Wi-Fi nebo [PPP](/mobilnisite/slovnik/ppp/)/802.1X pro pevné sítě).

Architektonicky se TNAP nachází na hranici mezi doménou důvěryhodného ne-3GPP přístupu a 5GC. Na své severní straně implementuje rozhraní [N2](/mobilnisite/slovnik/n2/) (k [AMF](/mobilnisite/slovnik/amf/)) pro signalizaci řídicí roviny a rozhraní N3 (k [UPF](/mobilnisite/slovnik/upf/)) pro data uživatelské roviny. Na své jižní straně se připojuje k ne-3GPP přístupovým bodům (např. Wi-Fi [AP](/mobilnisite/slovnik/ap/)) nebo agregačním sítím. Klíčovou rolí TNAP je fungovat jako proxy a adaptér. Přeposílá zprávy NGAP mezi UE/přístupovou sítí a AMF a přeposílá pakety uživatelské roviny mezi přístupovou sítí a UPF. Také se účastní procesu autentizace a pomáhá vytvořit vztah důvěry mezi přístupovou sítí a operátorem 5GC.

Provoz zahrnuje několik klíčových procedur. Během počáteční registrace TNAP usnadňuje autentizaci UE vůči 5GC, často přeposíláním zpráv EAP. Získává kontext UE od AMF a spravuje nastavení prostředků pro PDU session. Při mobilitě TNAP podporuje procedury předávání (handover) mezi 3GPP a ne-3GPP přístupem. Zásadní je, že protože je přístup důvěryhodný, TNAP nemusí s UE pro uživatelskou rovinu zakládat tunel IPSec; zabezpečení je poskytováno podpůrnou linkovou vrstvou (např. zabezpečení Wi-Fi) a zabezpečeným přenosem N3. TNAP zajišťuje, aby se pravidla politiky (policy) a QoS od SMF vynucovala v rámci důvěryhodné ne-3GPP přístupové sítě, což poskytuje konzistentní uživatelský zážitek.

## K čemu slouží

Koncept TNAP byl formalizován, aby poskytl jasnou architektonickou definici pro koncové body, které integrují důvěryhodné ne-3GPP přístupy do 5G systému. Řeší nejednoznačnost, která by mohla vzniknout z existence více gateway funkcí (TNGF, W-AGF) plnících podobné role pro různé typy důvěryhodného přístupu. Účelem je vytvořit jednotný logický referenční bod pro 5GC, který zjednodušuje návrh systému a specifikaci. Řeší problém, jak může monolitické 5GC rozhranit s různorodým ekosystémem ne-3GPP technologií standardizovaným, avšak flexibilním způsobem.

Jeho vytvoření bylo motivováno principem návrhu 5G, kterým je přístupově agnostické poskytování služeb jádrové sítě. Předchozí přístupy, jako ePDG v 4G, byly navrženy specificky pro nedůvěryhodný Wi-Fi a vytvářely izolovanou integraci. TNAP, jako součást vývoje od Release 12 pro důvěryhodný přístup založený na S2a a plně realizovaný v Release 16 pro 5G, umožňuje efektivnější a nativnější integraci. Umožňuje operátorům využívat jejich stávající nebo partnerskou infrastrukturu Wi-Fi a pevného širokopásmového připojení jako bezproblémové rozšíření jejich 5G sítě, podporuje případy užití jako odlehčování provozu přes Wi-Fi operátora (carrier Wi-Fi offload), pevný bezdrátový přístup (fixed wireless access) a konvergované nabídky bez redundantní bezpečnostní enkapsulace pro důvěryhodné cesty.

## Klíčové vlastnosti

- Slouží jako logický spojovací bod 5GC pro důvěryhodné ne-3GPP přístupy, jako jsou Wi-Fi a pevné širokopásmové sítě.
- Implementuje standardizovaná rozhraní N2 (řídicí rovina) a N3 (uživatelská rovina) směrem k 5GC.
- Funguje jako funkce pro vzájemné propojení protokolů mezi 3GPP NGAP a protokoly specifickými pro ne-3GPP přístup.
- Usnadňuje procedury autentizace a registrace UE bez nutnosti zakládat s UE tunel IPSec.
- Umožňuje vynucování pravidel QoS a politiky (policy) 5G v rámci domény důvěryhodného ne-3GPP přístupu.
- Podporuje události mobility a kontinuitu session pro UE pohybující se mezi 3GPP a ne-3GPP přístupem.

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.413** (Rel-19) — NGAP for Non-3GPP Access
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.519** (Rel-19) — UDR Usage for Policy & Exposure Data
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.807** (Rel-16) — 5G Wireline-Wireless Convergence Security Study
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [TNAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/tnap/)
