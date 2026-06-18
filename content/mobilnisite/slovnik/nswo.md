---
slug: "nswo"
url: "/mobilnisite/slovnik/nswo/"
type: "slovnik"
title: "NSWO – Non-Seamless Wireless Offload"
date: 2026-01-01
abbr: "NSWO"
fullName: "Non-Seamless Wireless Offload"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nswo/"
summary: "Mechanismus pro přímý přesun datového provozu uživatele do místní sítě (např. internetu) na úrovni bodu rádiového přístupu, který obchází mobilní páteřní síť. Poskytuje lokální breakout pro provoz, kt"
---

NSWO je mechanismus pro přímý přesun datového provozu uživatele do místní sítě na úrovni bodu rádiového přístupu, který obchází mobilní páteřní síť za účelem snížení jejího zatížení a zlepšení latence pro místní přístup.

## Popis

Non-Seamless Wireless Offload (NSWO) je síťová schopnost, která umožňuje uživatelskému zařízení (UE) směrovat vybraný IP provoz přímo do místní datové sítě prostřednictvím rádiové přístupové sítě, aniž by byl tunelován přes paketovou bránu páteřní sítě mobilního operátora (např. [PGW](/mobilnisite/slovnik/pgw/) v EPC, [UPF](/mobilnisite/slovnik/upf/) v 5GC). Termín 'non-seamless' (neseamless) označuje, že tento přesunutý provoz nevyužívá podporu mobility ani jiné služby páteřní sítě, jako je účtování, řízení politik nebo plynulý přechod (handover) k jiným typům přístupu. Provoz je v podstatě považován za best-effort přístup k internetu poskytovaný přímo přístupovým bodem. V architekturách 3GPP je NSWO podporováno přes důvěryhodný non-3GPP přístup (jako Wi-Fi) integrovaný s páteřní sítí a je definováno i pro 3GPP rádiový přístup.

Z architektonického hlediska v EPC, když se UE připojí přes důvěryhodný non-3GPP přístup (jako operátorská Wi-Fi síť), naváže IP spojení s Evolved Packet Data Gateway (ePDG) nebo přímo s přístupovým bodem. Pro provoz určený pro NSWO si UE vyžádá samostatné spojení nebo použije specifické pravidlo směrování. Přístupový bod na základě politik přijatých z páteřní sítě ([AAA](/mobilnisite/slovnik/aaa/) server, [PCRF](/mobilnisite/slovnik/pcrf/)) identifikuje provoz pro NSWO (např. na základě Destination-Based Packet Filters) a přeposílá jej přímo do místní sítě, čímž obchází rozhraní S2a/S2b směrem k PGW. V 5GC je tento koncept rozšířen pomocí Non-3GPP InterWorking Function ([N3IWF](/mobilnisite/slovnik/n3iwf/)) pro nedůvěryhodný přístup a důvěryhodný non-3GPP přístup. UE může navázat [PDU](/mobilnisite/slovnik/pdu/) session pro NSWO, která je ukotvena lokálně na přístupovém bodě/N3IWF a nikoli v UPF v páteřní datové síti.

Fungování je založeno na řízení politik. Páteřní síť poskytne UE a přístupovému bodu politiky NSWO, často definované jako pravidla [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function) v EPC nebo jako UE Route Selection Policy ([URSP](/mobilnisite/slovnik/ursp/)) v 5GC. Tyto politiky určují, které Application ID nebo IP toky mají být směrovány na NSWO spojení. IP vrstva UE implementuje principy IP flow mobility (IFOM) nebo multi-access PDU connectivity (MAPCON) pro rozdělení provozu mezi PDN spojení/PDU session ukotvené v páteřní síti a NSWO spojení. Klíčovou součástí je schopnost přiřadit UE pro NSWO spojení samostatnou IPv4 adresu a/nebo IPv6 prefix, odlišnou od IP adresy přidělené páteřní sítí. Tím je zajištěno oddělení provozu. NSWO je transparentní pro koncovou uživatelskou aplikaci, která jednoduše využívá IP vrstvu, zatímco rozhodnutí o směrování zajišťují síťové vrstvy.

## K čemu slouží

NSWO bylo vyvinuto k řešení rostoucího zahlcení páteřních sítí mobilních operátorů způsobeného exponenciálním nárůstem datového provozu, zejména od internetových služeb jako je streamování videa a prohlížení webu. Přesun takového provozu lokálně snižuje zatížení bran páteřní sítě a přenosových tras (backhaul), což vede k úsporám nákladů operátorů a potenciálně lepšímu výkonu pro uživatele přistupující k místnímu obsahu. Řeší problém neefektivního směrování veškerého provozu přes centralizovanou bránu, když je k dispozici a dostačuje přímá lokální cesta, zejména pro provoz, který nevyžaduje operátorské specifické služby jako IMS hovory nebo garantovanou QoS (Quality of Service).

Motivace vycházela z rozšíření integrovaných Wi-Fi a celulárních sítí. Operátoři chtěli využít svá nasazená Wi-Fi hotspoty nejen jako alternativní přístup, ale jako skutečný nástroj pro přesun provozu. Před NSWO mechanismy pro přesun často vyžadovaly tunelování veškerého provozu zpět do páteřní sítě (seamless offload), což nesnižovalo zatížení páteřní sítě. NSWO poskytlo funkci 'breakout'. Také řeší aplikace citlivé na latenci tím, že poskytuje kratší cestu k místním službám nebo internetu a obchází potenciální úzká místa v páteřní síti.

Historicky bylo NSWO standardizováno v 3GPP Release 11 jako součást práce na integraci Wi-Fi. Představovalo posun od vnímání non-3GPP přístupu pouze jako alternativy k jeho chápání jako doplňkového zdroje pro správu provozu. Umožnilo operátorům implementovat politiky 'řízení provozu' (traffic steering) podrobněji. V následujících release se jeho mechanismy řízení politik vyvinuly z ANDSF k více integrovaným politickým rámcům v 5GC. NSWO zůstává relevantní v 5G pro přesun provozu z Fixed Wireless Access (FWA) nebo podnikových nasazení, kde je požadován lokální internetový breakout, čímž podporuje princip 5G návrhu distribuovaných user plane funkcí a sítí místní oblasti (LADNs).

## Klíčové vlastnosti

- Přesouvá vybraný IP provoz přímo do místní sítě v místě přístupu a obchází tak mobilní páteřní síť.
- Funguje na bázi jednotlivých toků podle politik poskytovaných sítí (např. URSP, ANDSF).
- Neposkytuje pro přesunutý provoz podporu mobility ani služby páteřní sítě (jako je účtování založené na PCRF).
- Podporováno přes důvěryhodný non-3GPP přístup (např. operátorská Wi-Fi) i přes 3GPP rádiový přístup.
- UE udržuje současnou konektivitu: PDN spojení/PDU session ukotvená v páteřní síti a NSWO spojení.
- Používá samostatné IP adresování pro přesunutý provoz, aby bylo zachováno oddělení od služeb páteřní sítě.

## Definující specifikace

- **TS 23.139** (Rel-19) — 3GPP-Fixed Broadband Interworking Stage 2
- **TS 23.203** (Rel-19) — Policy and charging control architecture
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 23.852** (Rel-12) — Study on GTP-based S2a for WLAN Access
- **TS 23.896** (Rel-12) — Policy & Charging Control for Fixed Broadband Convergence
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.212** (Rel-19) — Gx/Gxx/Sd/St Diameter Protocol
- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.215** (Rel-19) — S9 Reference Point Stage 3 Specification
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [NSWO na 3GPP Explorer](https://3gpp-explorer.com/glossary/nswo/)
