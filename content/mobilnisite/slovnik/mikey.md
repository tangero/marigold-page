---
slug: "mikey"
url: "/mobilnisite/slovnik/mikey/"
type: "slovnik"
title: "MIKEY – Multimedia Internet KEYing"
date: 2025-01-01
abbr: "MIKEY"
fullName: "Multimedia Internet KEYing"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mikey/"
summary: "Protokol pro správu klíčů zabezpečující multimediální relace v reálném čase, jako je VoIP a videohovory, v IMS a dalších 3GPP službách. Vytváří kryptografické klíče a bezpečnostní asociace mezi koncov"
---

MIKEY je protokol pro správu klíčů zabezpečující multimediální relace v reálném čase v 3GPP službách, jako je IMS, prostřednictvím vytvoření kryptografických klíčů mezi koncovými body před zahájením toku médií.

## Popis

MIKEY (Multimedia Internet KEYing) je protokol pro správu klíčů standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro zabezpečení multimediálních relací, primárně v rámci IP Multimedia Subsystem (IMS). Jeho hlavní funkcí je vyjednat a vytvořit kryptografické klíče a bezpečnostní parametry (bezpečnostní asociace) mezi dvěma nebo více komunikujícími stranami před zahájením toků médií v reálném čase, jako je VoIP (Voice over IP) nebo videotelefonie. Protokol funguje peer-to-peer, často za asistence signalizačního protokolu, jako je [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol), který přenáší datové jednotky MIKEY uvnitř zpráv SIP během navazování relace.

Architektura MIKEY je navržena jako flexibilní a podporuje několik režimů provozu, aby vyhověla různým scénářům nasazení a modelům důvěry. Hlavní režimy zahrnují režim předem sdíleného klíče ([PSK](/mobilnisite/slovnik/psk/)), kde je tajný klíč předem distribuován komunikujícím entitám; režim šifrování veřejným klíčem (PKE), který pro přenos klíče používá asymetrickou kryptografii (např. [RSA](/mobilnisite/slovnik/rsa/)) bez nutnosti předem sdíleného tajemství; a režim Diffie-Hellman (DH) pro ověřenou výměnu klíčů. Zprávy MIKEY přenášejí kryptografické parametry, včetně klíčového materiálu, kryptografických algoritmů (šifry, autentizační algoritmy), identifikátorů bezpečnostní politiky ([SPI](/mobilnisite/slovnik/spi/)) a informací o životnosti. Tyto zprávy jsou typicky kódovány v binárním formátu a přenášeny jako těla [MIME](/mobilnisite/slovnik/mime/) v rámci signalizace SIP.

V rámci ekosystému 3GPP hraje MIKEY klíčovou roli při implementaci zabezpečení médií typu end-to-end, zejména pro Secure Real-time Transport Protocol ([SRTP](/mobilnisite/slovnik/srtp/)). Po dokončení handshake MIKEY jsou odvozené klíče použity k inicializaci kontextů SRTP na obou koncích, což umožňuje šifrování a ověřování paketů [RTP](/mobilnisite/slovnik/rtp/) médií. Tento proces je nedílnou součástí služeb, jako je IMS-based Voice over LTE (VoLTE) a Video over LTE (ViLTE), kde je důvěrnost uživatelské roviny požadavkem. Protokol je definován tak, aby fungoval ve spojení s dalšími bezpečnostními mechanismy 3GPP, jako jsou ty poskytované rámcem Authentication and Key Agreement (AKA) pro přístup k síti, ale MIKEY se konkrétně zabývá správou klíčů na aplikační vrstvě pro samotnou multimediální relaci.

## K čemu slouží

MIKEY byl vytvořen, aby vyřešil nedostatek standardizovaného, lehkého a efektivního protokolu pro správu klíčů specificky uzpůsobeného pro multimediální aplikace v reálném čase na internetu. Před jeho vývojem zabezpečení multimediálních relací často spoléhalo na obecné bezpečnostní protokoly, jako je IPsec nebo TLS, které nebyly optimalizovány pro nízkou latenci a nespojovanou povahu toků médií RTP. Tyto protokoly mohly zavádět významné zpoždění při navazování a režii, což je pro komunikaci v reálném čase nevýhodné. Účelem MIKEY je poskytnout specializovaný mechanismus pro vytváření bezpečnostních asociací pro multimediální toky s minimálním dopadem na dobu navazování relace.

Motivace pro jeho přijetí v rámci 3GPP vycházela z potřeby standardizovaného zabezpečení médií v architektuře IMS. Když 3GPP definovalo sítě typu all-IP pro poskytování hlasových a video služeb, zajištění důvěrnosti a integrity těchto mediálních toků se stalo prvořadým. MIKEY nabídl řešení, které mohlo být čistě integrováno do postupů navazování relací založených na SIP v IMS. Vyřešil problém bezpečného inicializačního nastavení klíčů SRTP mezi uživatelským zařízením (UE) a sítí nebo mezi dvěma UE způsobem, který byl škálovatelný a interoperabilní mezi různými implementacemi výrobců. Jeho návrh umožňuje využít existující vztahy důvěry, jako jsou ty vytvořené 3GPP AKA, k ověření výměny klíčů, čímž poskytuje komplexní bezpečnostní řešení od přístupu k síti až po aplikační média.

## Klíčové vlastnosti

- Podporuje více režimů správy klíčů: předem sdílený klíč (PSK), šifrování veřejným klíčem (PKE) a Diffie-Hellman (DH)
- Navržen pro navazování s nízkou latencí, aby vyhovoval multimediálním relacím v reálném čase
- Přenáší kryptografické parametry, identifikátory bezpečnostní politiky (SPI) a životnost klíčů
- Typicky přenášen uvnitř signalizačních zpráv SIP jako datová část MIME
- Přímo poskytuje klíčový materiál a parametry pro inicializaci kontextu SRTP
- Umožňuje end-to-end šifrování médií mezi uživatelskými zařízeními nebo mezi UE a síťovými uzly

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRTP – Secure Real-time Transport Protocol](/mobilnisite/slovnik/srtp/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [MIKEY na 3GPP Explorer](https://3gpp-explorer.com/glossary/mikey/)
