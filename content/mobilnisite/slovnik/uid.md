---
slug: "uid"
url: "/mobilnisite/slovnik/uid/"
type: "slovnik"
title: "UID – User Identifier for MIKEY-SAKKE"
date: 2026-01-01
abbr: "UID"
fullName: "User Identifier for MIKEY-SAKKE"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/uid/"
summary: "Kryptografický identifikátor používaný v protokolu MIKEY-SAKKE (Multimedia Internet Keying - Sakai-Kasahara Key Encryption) pro zabezpečenou skupinovou komunikaci. Jednoznačně identifikuje uživatele v"
---

UID je kryptografický identifikátor, který jednoznačně identifikuje uživatele v rámci domény služby správy klíčů (Key Management Service) pro distribuci klíčů a šifrování založené na identitě v protokolu MIKEY-SAKKE.

## Popis

Uživatelský identifikátor (UID) je základní komponentou bezpečnostního rámce MIKEY-SAKKE standardizovaného 3GPP pro ochranu skupinové komunikace, jako je například Mission Critical Push-To-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) a další zabezpečené multimediální služby. Technicky je UID řetězec, který jednoznačně identifikuje uživatele (nebo zařízení) v rámci konkrétní domény služby správy klíčů ([KMS](/mobilnisite/slovnik/kms/)). Používá se v protokolu MIKEY-SAKKE, což je schéma šifrování založené na identitě (IBE). UID slouží jako veřejný klíč uživatele; odpovídající privátní klíč je generován službou KMS na základě tohoto identifikátoru a hlavního tajemství KMS. Při navazování zabezpečené relace odesílatel použije UID příjemce spolu s parametry od KMS k zašifrování klíče pro šifrování provozu ([TEK](/mobilnisite/slovnik/tek/)). Tento zašifrovaný klíč, zapouzdřený ve zprávě MIKEY-SAKKE I_MESSAGE, je odeslán příjemci. Příjemce po autentizaci u KMS může odvodit svůj privátní klíč a dešifrovat TEK, čímž naváže zabezpečenou mediální komunikaci. Architektura zahrnuje KMS jako důvěryhodnou entitu, která spravuje kryptografické parametry a uživatelské identity (UID). UID je typicky formátován jako Uniform Resource Identifier ([URI](/mobilnisite/slovnik/uri/)), například [SIP](/mobilnisite/slovnik/sip/) URI (např. sip:user@domain.com), což zajišťuje kompatibilitu s existujícími schématy adresování uživatelů ve službách založených na IMS. Jeho role je klíčová pro umožnění škálovatelné a efektivní správy klíčů bez nutnosti předem sdílených certifikátů nebo složité infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) pro každého člena skupiny.

## K čemu slouží

UID a protokol MIKEY-SAKKE byly vytvořeny k řešení kritické potřeby efektivní a bezpečné správy skupinových klíčů v službách komunikace v reálném čase, zejména pro misi-kritické uživatele, jako jsou složky integrovaného záchranného systému. Tradiční metody výměny klíčů, jako je Diffie-Hellman nebo [PKI](/mobilnisite/slovnik/pki/) založené na certifikátech, mohou při navazování skupinových hovorů s mnoha účastníky způsobit významnou latenci a správní režii, což je pro zásahy v nouzových situacích nepřijatelné. MIKEY-SAKKE využívající šifrování založené na identitě tento proces zjednodušuje. UID využívá existující identifikátor uživatele (jako telefonní číslo nebo [SIP](/mobilnisite/slovnik/sip/) URI) jako jeho veřejný klíč, čímž odstraňuje nutnost distribuce a validace individuálních certifikátů před komunikací. Tím je vyřešen problém rychlého navázání zabezpečené relace pro velké, dynamické skupiny. Historicky byla zabezpečená skupinová komunikace v mobilních sítích omezená nebo závisela na složité infrastruktuře. Zavedení UID a MIKEY-SAKKE ve 3GPP Release 8 poskytlo standardizovanou, kryptograficky bezpečnou metodu přizpůsobenou nárokům na nízkou latenci a škálovatelnost pro vznikající misi-kritické služby založené na LTE, což umožnilo zabezpečený push-to-talk, video a data s okamžitým sestavením hovoru.

## Klíčové vlastnosti

- Slouží jako veřejný klíč ve schématech šifrování založeného na identitě (IBE)
- Jednoznačně identifikuje uživatele v rámci domény služby správy klíčů (KMS)
- Umožňuje šifrování klíčů pro provoz bez nutnosti předem sdílených certifikátů
- Typicky formátován jako URI (např. SIP URI) pro integraci s IMS
- Usnadňuje škálovatelnou distribuci klíčů pro dynamickou skupinovou komunikaci
- Klíčová komponenta protokolu MIKEY-SAKKE pro zabezpečené služby 3GPP

## Definující specifikace

- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.879** (Rel-13) — MCPTT Security Study
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TR 33.980** (Rel-19) — GAA & Liberty Alliance Interworking Guidelines
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements

---

📖 **Anglický originál a plná specifikace:** [UID na 3GPP Explorer](https://3gpp-explorer.com/glossary/uid/)
