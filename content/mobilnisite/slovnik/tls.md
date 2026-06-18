---
slug: "tls"
url: "/mobilnisite/slovnik/tls/"
type: "slovnik"
title: "TLS – Transport Layer Security"
date: 2026-01-01
abbr: "TLS"
fullName: "Transport Layer Security"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tls/"
summary: "Kryptografický protokol určený k zajištění zabezpečené, ověřené komunikace a ochrany soukromí dat v síti. V systémech 3GPP je TLS široce používán k ochraně signalizační a uživatelské roviny mezi síťov"
---

TLS je kryptografický protokol používaný v systémech 3GPP k zajištění zabezpečené, ověřené komunikace s integritou a důvěrností pro signalizační a uživatelskou rovinu mezi síťovými funkcemi a uživatelským zařízením.

## Popis

Transport Layer Security (TLS) je základní bezpečnostní protokol přijatý 3GPP k ochraně dat přenášených přes různé síťová rozhraní. Funguje nad transportní vrstvou (typicky TCP) a vytváří zabezpečený tunel mezi dvěma koncovými body ještě předtím, než aplikační protokol (např. [HTTP](/mobilnisite/slovnik/http/), [SIP](/mobilnisite/slovnik/sip/), Diameter) vymění jakákoli citlivá data. Protokol tento zabezpečený kanál navazuje pomocí handshake procedury, při níž si koncové body vyjednávají kryptografické algoritmy, vzájemně se ověřují (často pomocí digitálních certifikátů X.509) a odvozují sdílené relací klíče používané pro šifrování a ochranu integrity.

Architektura TLS v rámci sítě 3GPP je všudypřítomná. Zabezpečuje webová rozhraní, jako je referenční bod T8 používaný funkcí Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) pro služby IoT, a chrání northbound [API](/mobilnisite/slovnik/api/). Zabezpečuje spojení Diameter mezi prvky jádra sítě, například mezi funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)). V IP Multimedia Subsystem (IMS) chrání TLS rozhraní Mw, Mg a Mx přenášející signalizaci SIP. Pro uživatelské zařízení je TLS klíčové pro zabezpečení připojení [HTTPS](/mobilnisite/slovnik/https/) k aplikačním serverům, včetně těch používaných pro správu zařízení, ověřování (např. pro EAP-TLS) a přístupu k IMS službám přes referenční bod Ut.

Fungování TLS zahrnuje odlišné fáze. Handshake protokol spravuje ověřování a navázání klíčů. Klient a server si vymění zprávy 'ClientHello' a 'ServerHello', aby se dohodli na verzi TLS a šifrovací sadě. Server pak typicky odešle svůj certifikát k ověření. Pro vzájemný TLS (mTLS), jak je vyžadováno na mnoha servisně orientovaných rozhraních ([SBI](/mobilnisite/slovnik/sbi/)) v 5G jádru, předloží certifikát i klient. Po ověření je vyměněno 'Premaster Secret', které je spolu s náhodnými hodnotami použito k vygenerování 'Master Secret', ze kterého jsou odvozeny symetrické šifrovací klíče a klíče pro Message Authentication Code (MAC). Po dokončení handshake převezme kontrolu Record protokol, který pomocí dohodnutých klíčů šifruje aplikační data, zajišťuje integritu zpráv prostřednictvím MAC (nebo autentizovaného šifrování jako AES-GCM) a volitelně komprimuje data.

Úlohou TLS je zmírnit hrozby jako odposlech, falšování a padělání zpráv. Zajištěním důvěrnosti zabraňuje útočníkům číst citlivé informace, jako jsou identity uživatelů, polohová data nebo záznamy o účtování. Ochrana integrity zajišťuje, že příkazy nebo data nemohou být přenášeny změněny bez detekce. Ověřování, zejména vzájemné ověřování pomocí certifikátů, je klíčové v cloud-nativní, servisně orientované architektuře 5G, aby se zabránilo interakci neautorizovaných síťových funkcí mezi sebou. TLS je často kombinován se základním IPsec, což poskytuje strategii obrany do hloubky, nebo je používán samostatně tam, kde IPsec není proveditelné, například pro provoz procházející veřejným internetem mezi sítí operátora a serverem třetí strany.

## K čemu slouží

TLS byl integrován do standardů 3GPP, aby řešil kritickou potřebu zabezpečení signalizace a datového provozu založeného na paketech, jak se sítě vyvíjely od okruhově přepínaných architektur k plně IP architekturám. Rané mobilní sítě spoléhaly na bezpečnost na síťové úrovni v rámci rádiového přístupu a perimetru jádra sítě. S zavedením IMS ve verzi 5 a rostoucím využíváním služeb založených na IP však provoz začal procházet méně důvěryhodnými cestami, včetně připojení k externím aplikačním serverům a mezi datovými centry. To vystavilo citlivou signalizaci řídicí roviny (např. SIP, Diameter) a uživatelská data odposlechu a manipulaci.

Protokol řeší problém poskytování robustní, standardy založené bezpečnosti pro aplikační protokoly, kterým chybí vlastní ochrana. Před jeho rozšířeným přijetím byly někdy používány proprietární nebo slabší bezpečnostní mechanismy, což vytvářelo zranitelnosti a problémy s interoperabilitou. TLS poskytuje důkladně prověřené, průmyslové standardní řešení pro ověřování, důvěrnost a integritu. Jeho vytvoření a vývoj (od jeho předchůdce SSL) byly motivovány bezpečnostními potřebami širšího internetu, které 3GPP využilo k zabezpečení vlastního ekosystému.

V pozdějších verzích, zejména s 5G, se účel TLS dále rozšířil. Přechod na Service-Based Architecture (SBA) s API HTTP/2 (např. Nnrf, Nausf) vyžadoval transportně agnostický bezpečnostní mechanismus, který by mohl efektivně fungovat v cloudových prostředích. Vzájemný TLS (mTLS) se stal povinným pro mnoho servisně orientovaných rozhraní, čímž vyřešil problém strojového ověřování v dynamickém, na mikroslužbách založeném jádru sítě, kde jsou síťové funkce efemérní. TLS 1.3, povinný v pozdějších verzích 5G, řeší omezení starších verzí poskytováním silnějších kryptografických algoritmů, rychlejších handshake přes režimy 1-RTT a 0-RTT a lepší odolnosti proti downgrade útokům, což je v souladu s moderními bezpečnostními osvědčenými postupy a výkonnostními požadavky.

## Klíčové vlastnosti

- Zajišťuje důvěrnost prostřednictvím symetrického šifrování (např. AES, ChaCha20)
- Zajišťuje integritu a autenticitu zpráv pomocí Message Authentication Codes (MAC) nebo autentizovaného šifrování
- Podporuje ověřování koncových bodů pomocí digitálních certifikátů X.509, včetně vzájemného ověřování (mTLS)
- Vyjednává kryptografické parametry pomocí rozšiřitelného handshake protokolu
- Nabízí dopřednou utajenost prostřednictvím metod výměny efemérních klíčů (např. DHE, ECDHE)
- Široce nasazen napříč rozhraními 3GPP pro ochranu signalizace (Diameter, SIP, HTTP/2) a uživatelské roviny

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.322** (Rel-19) — IMS Tunneling over Restrictive Networks
- … a dalších 39 specifikací

---

📖 **Anglický originál a plná specifikace:** [TLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tls/)
