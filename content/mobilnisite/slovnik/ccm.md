---
slug: "ccm"
url: "/mobilnisite/slovnik/ccm/"
type: "slovnik"
title: "CCM – Certificate Configuration Message"
date: 2025-01-01
abbr: "CCM"
fullName: "Certificate Configuration Message"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ccm/"
summary: "Bezpečnostní zpráva používaná k poskytování a správě digitálních certifikátů v sítích 3GPP. Umožňuje zabezpečené rozšíření certifikátů veřejného klíče a informací o stavu certifikátů mezi síťovými ent"
---

CCM je bezpečnostní zpráva používaná k poskytování a správě digitálních certifikátů v sítích 3GPP pro zabezpečené rozšiřování certifikátů a informací o stavu mezi síťovými entitami a uživatelským zařízením.

## Popis

Certificate Configuration Message (CCM) je standardizovaný formát zprávy definovaný 3GPP pro zabezpečené poskytování a správu životního cyklu digitálních certifikátů v mobilních sítích. Funguje jako klíčová komponenta v rámci Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)) a dalších bezpečnostních rámců a usnadňuje výměnu dat souvisejících s certifikáty. Zpráva nese základní informace, jako je samotný certifikát (ve formátu X.509), stav odvolání certifikátu (např. pomocí seznamů odvolaných certifikátů nebo odpovědí protokolu Online Certificate Status Protocol) a související metadata, jako jsou období platnosti a údaje o vystavovateli. Tato strukturovaná datová část umožňuje síťovým funkcím, jako je Bootstrapping Server Function ([BSF](/mobilnisite/slovnik/bsf/)) nebo specializovaný Certificate Management Server, bezpečně doručovat přihlašovací údaje uživatelskému zařízení (UE) nebo mezi síťovými uzly.

Z architektonického hlediska je CCM přenášena přes zabezpečené protokoly, jako je [HTTPS](/mobilnisite/slovnik/https/), nebo v rámci specifických bezpečnostních protokolů 3GPP definovaných v příslušných technických specifikacích (např. 29.333, 29.334). Tok zpráv obvykle pochází z důvěryhodné certifikační autority nebo z řídicí funkce v síti operátora. Například ve scénáři založeném na GBA požádá UE o přihlašovací údaje specifické pro aplikaci; síť může odpovědět CCM obsahující certifikát pro daný aplikační server, což umožní UE se s tímto serverem přímo autentizovat. Struktura zprávy je navržena jako rozšiřitelná a podporuje různé typy certifikátů a mechanismy informací o stavu podle požadavků různých služeb.

Její role v síti je zásadní pro umožnění bezpečnosti založené na certifikátech. Poskytnutím standardizovaného mechanismu pro distribuci certifikátů CCM podporuje vzájemnou autentizaci mezi UE a síťovými aplikačními servery (např. pro služby IMS, [MBMS](/mobilnisite/slovnik/mbms/)), zabezpečuje přístup ke službám a je základem pro integritu a důvěrnost komunikace. Odstraňuje potřebu ručního předzásobení certifikátů na každém zařízení a umožňuje dynamické poskytování certifikátů na vyžádání, což je klíčové pro škálovatelné nasazení služeb a efektivní správu životního cyklu certifikátů včetně aktualizací a odvolání.

## K čemu slouží

CCM byla zavedena, aby řešila rostoucí potřebu škálovatelné, automatizované a bezpečné distribuce digitálních certifikátů v sítích 3GPP. Před jejím standardizováním často vyžadovalo poskytování certifikátů pro služby jako Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo IP Multimedia Subsystem (IMS) ruční metody nebo metody mimo přenosovou cestu, které byly neefektivní, náchylné k chybám a obtížně spravovatelné pro velké množství zařízení. Vzestup architektur založených na službách a potřeba silné autentizace pro prémiové služby si vyžádaly standardizovaný mechanismus v přenosové cestě.

Vytvoření CCM bylo motivováno integrací infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) do mobilních sítí za účelem zvýšení bezpečnosti nad rámec tradiční autentizace založené na [SIM](/mobilnisite/slovnik/sim/) kartě. Řeší problém, jak bezpečně a spolehlivě získat certifikát z důvěryhodného síťového zdroje do UE. To umožňuje širokou škálu bezpečnostních aplikací, včetně zabezpečení doručování obsahu založeného na [HTTP](/mobilnisite/slovnik/http/) (jak je uvedeno ve specifikacích jako 26.114), umožnění autentizace založené na certifikátech pro GBA a podpory ochrany služeb pro vysílací služby. Poskytuje základní vrstvu zasílání zpráv, která operátorům umožňuje dynamicky nasazovat služby závislé na certifikátech.

## Klíčové vlastnosti

- Standardizovaný formát pro přenos certifikátů X.509 v sítích 3GPP
- Podporuje doručování informací o stavu odvolání certifikátu (CRL/OCSP)
- Umožňuje dynamické poskytování certifikátů uživatelskému zařízení (UE) na vyžádání
- Integruje se s Generic Bootstrapping Architecture (GBA) pro správu přihlašovacích údajů
- Usnadňuje vzájemnou autentizaci mezi UE a aplikačními servery
- Používá zabezpečené transportní protokoly (např. HTTPS) pro zajištění integrity a důvěrnosti

## Související pojmy

- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [BSF – Bootstrapping Server Function](/mobilnisite/slovnik/bsf/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.980** (Rel-19) — Multi-stream Multiparty Conferencing Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [CCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccm/)
