---
slug: "sakke"
url: "/mobilnisite/slovnik/sakke/"
type: "slovnik"
title: "SAKKE – Sakai-Kasahara Key Encryption"
date: 2025-01-01
abbr: "SAKKE"
fullName: "Sakai-Kasahara Key Encryption"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sakke/"
summary: "SAKKE je šifrovací schéma založené na identitě (IBE), standardizované 3GPP pro zabezpečenou skupinovou komunikaci, zejména ve službách Mission Critical Push-to-Talk (MCPTT). Umožňuje efektivní distrib"
---

SAKKE je šifrovací schéma založené na identitě (identity-based encryption), standardizované 3GPP pro zabezpečenou skupinovou komunikaci, které umožňuje efektivní distribuci klíčů odvozováním veřejných klíčů přímo z identit uživatelů.

## Popis

SAKKE je kryptografický mechanismus založený na párovací kryptografii, konkrétně na algoritmu Sakai-Kasahara Key Encryption. Funguje v rámci kryptografie založené na identitě (IBC), kde veřejně známý identifikátor uživatele (například telefonní číslo nebo skupinové ID) slouží jako jeho veřejný klíč. Tím se odstraňuje tradiční požadavek infrastruktury veřejných klíčů ([PKI](/mobilnisite/slovnik/pki/)) na distribuci a správu digitálních certifikátů. Důvěryhodná třetí strana, nazývaná server pro správu klíčů ([KMS](/mobilnisite/slovnik/kms/)) nebo generátor privátních klíčů (PKG), drží hlavní tajný klíč. KMS používá tento hlavní klíč ke generování privátních klíčů pro uživatele odpovídajících jejich identitám. Tyto privátní klíče jsou bezpečně zřízeny do zařízení uživatele.

Pro šifrování použije odesílatel identitu příjemce (veřejný klíč) a celosystémové veřejné parametry k výpočtu šifrovacího klíče. Tento proces zahrnuje matematické operace na grupách eliptických křivek a bilineární párování. Zašifrovaná zpráva a krátký datový blok zapouzdření klíče jsou odeslány příjemci. Příjemce, který vlastní svůj jedinečný privátní klíč od KMS, může dešifrovat data zapouzdření klíče a obnovit symetrický šifrovací klíč pro obsah, a poté dešifrovat zprávu. To je velmi efektivní pro scénáře jeden-vůči-mnoha, protože stejný zašifrovaný klíč pro obsah může být dešifrován více příjemci pomocí jejich příslušných privátních klíčů.

V rámci architektury 3GPP je SAKKE integrováno do funkce správce zabezpečení (SeMF) a funkce správy klíčů (KMF) definovaných pro služby kritické pro činnost (Mission Critical Services). Je primárně specifikováno pro zabezpečení Group Communication System Enablers ([GCSE](/mobilnisite/slovnik/gcse/)) a [MCPTT](/mobilnisite/slovnik/mcptt/), což zajišťuje, že média a signalizace pro skupinová volání zůstanou důvěrná a že pouze autorizovaní členové skupiny mohou dešifrovat provoz. Schopnost tohoto schématu efektivně zvládat změny dynamického členství ve skupině z něj činí základní kámen pro zabezpečenou skupinovou komunikaci v reálném čase v sítích LTE a 5G pro veřejnou bezpečnost a kritickou infrastrukturu.

## K čemu slouží

SAKKE bylo zavedeno, aby řešilo významné výzvy správy a distribuce klíčů pro zabezpečenou skupinovou komunikaci ve velkých a dynamických prostředích, jako jsou sítě pro veřejnou bezpečnost. Tradiční systémy [PKI](/mobilnisite/slovnik/pki/) založené na certifikátech přinášejí značnou režii, latenci a složitost při správě certifikátů pro tisíce uživatelů, kteří mohou potřebovat okamžitě vytvářet ad-hoc skupiny. Pro službu Mission Critical Push-to-Talk, kde musí dispečer bezpečně komunikovat s velkou skupinou záchranářů, je čekání na ověření certifikátů nebo distribuce jednotlivě šifrovaných proudů nepraktické.

Hlavní motivací pro přijetí SAKKE bylo umožnit efektivní šifrování založené na identitě, které se bezproblémově škáluje. Vázáním šifrovacího klíče přímo na identitu uživatele nebo skupiny systém odstraňuje potřebu předchozí výměny certifikátů nebo složitého online vyjednávacího protokolu. To vede k rychlejšímu sestavování volání a snížení signalizační režie. Řeší problém zabezpečeného multicastu nebo broadcastu, kde odesílatel nemusí předem znát úplný seznam veřejných klíčů příjemců, ale pouze jejich identity, které jsou v kontextu skupiny často již známé. To je ideální pro vizi 3GPP standardizované, interoperabilní a zabezpečené komunikace pro kritické činnosti přes komerční mobilní sítě.

## Klíčové vlastnosti

- Šifrování založené na identitě (IBE): Veřejné klíče jsou odvozeny přímo z identifikátorů uživatele nebo skupiny (např. SIP URI).
- Efektivní distribuce skupinových klíčů: Umožňuje odesílateli zašifrovat zprávu pro více příjemců pomocí jediného vysílání (broadcastu) s zapouzdřením klíče pro každého příjemce.
- Kryptografie založená na eliptických křivkách a párování: Poskytuje silnou bezpečnost s relativně krátkými délkami klíčů ve srovnání s tradičním RSA.
- Žádná správa certifikátů: Odstraňuje potřebu tradiční PKI a seznamů zneplatněných certifikátů (CRL) pro šifrovací klíče.
- Podpora dynamických skupin: Snadno akomoduje uživatele vstupující do skupin nebo je opouštějící, aniž by to vyžadovalo přegenerování klíčů pro celou skupinu ze strany odesílatele.
- Integrace s architekturou 3GPP MCPTT: Specifikováno jako součást KMF/SeMF pro zabezpečení služeb kritických pro činnost (mission critical services) od konce ke konci.

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 23.782** (Rel-15) — Interworking between LTE MC and non-LTE MC systems
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.885** (Rel-14) — Security Study for V2X Services

---

📖 **Anglický originál a plná specifikace:** [SAKKE na 3GPP Explorer](https://3gpp-explorer.com/glossary/sakke/)
