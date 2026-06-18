---
slug: "xres"
url: "/mobilnisite/slovnik/xres/"
type: "slovnik"
title: "XRES – Expected Response"
date: 2025-01-01
abbr: "XRES"
fullName: "Expected Response"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/xres/"
summary: "XRES je očekávaná hodnota autentizační odpovědi vygenerovaná HLR/AuC sítě během 3G autentizace. Používá se VLR/SGSN k ověření legitimity SIM/USIM karty uživatele porovnáním s uživatelem vypočtenou odp"
---

XRES je očekávaná hodnota autentizační odpovědi vygenerovaná sítí pro ověření SIM karty uživatele porovnáním s uživatelem vypočtenou odpovědí během 3G autentizace.

## Popis

Očekávaná odpověď (XRES) je klíčovou součástí rámce pro autentizaci a dohodu klíčů ([AKA](/mobilnisite/slovnik/aka/)) 3GPP, konkrétně pro sítě 3G (UMTS). Generuje ji Home Location Register/Authentication Center ([HLR](/mobilnisite/slovnik/hlr/)/AuC) spolu s dalšími autentizačními vektory ([AV](/mobilnisite/slovnik/av/)), které zahrnují náhodnou výzvu ([RAND](/mobilnisite/slovnik/rand/)), autentizační token sítě ([AUTN](/mobilnisite/slovnik/autn/)) a šifrovací/integritní klíče ([CK](/mobilnisite/slovnik/ck/)/[IK](/mobilnisite/slovnik/ik/)). Tento vektor je odeslán do obsluhujícího síťového uzlu, jako je Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)) nebo Serving GPRS Support Node (SGSN). Hlavní funkcí XRES je sloužit jako referenční hodnota sítě pro ověření identity uživatele. Když se uživatelské zařízení (UE) pokusí připojit k síti, VLR/SGSN přepošle RAND a AUTN do UE. Universal Subscriber Identity Module (USIM) v UE použije sdílený tajný klíč (K) s HLR/AuC ke zpracování těchto vstupů. Nezávisle vypočte hodnotu odpovědi zvanou RES. UE pak tuto RES odešle zpět VLR/SGSN. Síťový uzel provede přímé porovnání: pokud přijatá RES odpovídá předem uložené XRES z autentizačního vektoru, je uživatel autentizován. Neshoda signalizuje selhání autentizace a přístup je odepřen. Tento proces zajišťuje, že pouze UE disponující správným tajným klíčem K může vygenerovat správnou RES, čímž ověří identitu účastníka a chrání proti útokům založeným na zosobnění. XRES je dočasná hodnota platná pro jeden autentizační proces, což zvyšuje bezpečnost tím, že brání opakovaným útokům. Její generování a ověřování jsou ústřední pro proces vzájemné autentizace v 3G, kde síť autentizuje UE a UE autentizuje síť (prostřednictvím AUTN).

## K čemu slouží

XRES byl zaveden, aby řešil bezpečnostní slabiny v autentizačním systému 2G (GSM), který poskytoval pouze jednosměrnou autentizaci (sítě vůči uživateli). Primárním účelem XRES je umožnit robustní vzájemnou autentizaci v sítích 3G UMTS. Řeší problém ověření, že uživatel je tím, za koho se vydává, na základě kryptograficky zabezpečeného mechanismu výzva-odpověď. Tím, že síť vygeneruje očekávanou hodnotu (XRES) odvozenou z tajného klíče známého pouze domovské síti a SIM kartě uživatele, může systém definitivně potvrdit identitu uživatele před udělením síťového přístupu. To byl významný vývoj oproti použití SRES (Signed Response) v GSM, jako součást komplexnějšího AKA postupu, který také poskytoval silnější šifrovací klíče (CK/IK) a autentizaci sítě. Vytvoření XRES bylo motivováno potřebou zvýšené bezpečnosti v mobilní komunikaci pro ochranu proti podvodům, odposlechu a neoprávněnému přístupu, což se stalo s nástupem mobilních datových služeb stále kritičtějším. Tvoří základní kámen ověření v rámci protokolu UMTS AKA, standardu, který ovlivnil všechny následné bezpečnostní architektury 3GPP.

## Klíčové vlastnosti

- Generována HLR/AuC jako součást pětičlenného autentizačního vektoru (RAND, XRES, CK, IK, AUTN).
- Slouží jako referenční hodnota sítě pro ověření uživatelem vypočtené odpovědi (RES).
- Umožňuje autentizaci uživatele obsluhující sítí (VLR/SGSN) prostřednictvím přímého porovnání hodnot.
- Platná pouze pro jeden autentizační případ, čímž brání opakovaným útokům.
- Integrální součást procedury vzájemné autentizace a dohody klíčů (AKA) v 3G.
- Odvozena ze sdíleného tajného klíče (K) a náhodné výzvy (RAND) pomocí algoritmu f2.

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)
- [RES – Authentication Response](/mobilnisite/slovnik/res/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report

---

📖 **Anglický originál a plná specifikace:** [XRES na 3GPP Explorer](https://3gpp-explorer.com/glossary/xres/)
