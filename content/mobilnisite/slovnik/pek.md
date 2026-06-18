---
slug: "pek"
url: "/mobilnisite/slovnik/pek/"
type: "slovnik"
title: "PEK – ProSe Encryption Key"
date: 2025-01-01
abbr: "PEK"
fullName: "ProSe Encryption Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pek/"
summary: "Kryptografický klíč používaný v Proximity Services (ProSe) pro zabezpečení přímé komunikace mezi blízkými uživatelskými zařízeními (UE). Šifruje uživatelská data vyměňovaná přes rozhraní PC5, čímž zaj"
---

PEK je kryptografický klíč používaný v Proximity Services (ProSe) pro šifrování uživatelských dat přes rozhraní PC5, což zajišťuje důvěrnost přímé komunikace typu Device-to-Device a Vehicle-to-Everything.

## Popis

[ProSe](/mobilnisite/slovnik/prose/) Encryption Key (PEK) je základní bezpečnostní prvek v architektuře 3GPP Proximity Services (ProSe), poprvé standardizovaný ve vydání 12. Konkrétně se používá k zajištění ochrany důvěrnosti uživatelských dat přenášených přímo mezi UE přes postranní spojení (sidelink) referenčního bodu PC5. PEK je generován a spravován jako součást bezpečnostního kontextu ProSe. Tento kontext je typicky vytvořen během autorizačních procedur a procedur navázání klíčů pro ProSe Direct Discovery nebo Direct Communication, které mohou zahrnovat ProSe Function v síti. Klíč je odvozen pomocí funkcí pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) specifikovaných v 3GPP TS 33.303, často z kořenového klíče, jako je ProSe Key (PK). Po odvození je PEK poskytnut zúčastněným UE. V protokolovém zásobníku je PEK používán vrstvou Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), jak je specifikováno v TS 36.323 pro ProSe založené na LTE a v odpovídajících specifikacích pro NR sidelink. Vrstva PDCP používá PEK k provádění šifrování (a potenciálně i ochrany integrity, i když ta může používat samostatný klíč) na paketech uživatelské roviny před jejich přenosem přes rozhraní PC5. Vrstva PDCP přijímajícího UE používá stejný PEK k dešifrování dat. Životní cyklus PEK, včetně jeho odvození, aktivace, použití a odstranění, je přísně řízen bezpečnostními management funkcemi UE, aby se zabránilo opakovanému použití klíče a zajistila dopředná důvěrnost. Jeho role je klíčová ve scénářích, jako je veřejná bezpečnostní [D2D](/mobilnisite/slovnik/d2d/) komunikace a [V2X](/mobilnisite/slovnik/v2x/), kde musí být přímé spoje mezi UE stejně bezpečné jako spojení zprostředkovaná sítí.

## K čemu slouží

PEK byl zaveden, aby řešil bezpečnostní požadavky přímé komunikace Device-to-Device ([D2D](/mobilnisite/slovnik/d2d/)), která je základním kamenem Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)). Před ProSe bylo veškerá komunikace UE směrována přes síťovou infrastrukturu (např. [eNB](/mobilnisite/slovnik/enb/), gNB), která inherentně poskytovala bod pro aplikaci standardních mechanismů buněčné bezpečnosti. Zavedení přímé PC5 komunikace pro veřejnou bezpečnost, komerční D2D a později V2X vytvořilo novou útočnou plochu, kde odposlouchávající strany mohly zachytit přenosy mezi blízkými zařízeními. Tradiční klíče buněčné bezpečnosti (jako K_{eNB}) na tento přímý spoj nebyly použitelné. PEK tento problém řeší tím, že poskytuje vyhrazený šifrovací klíč pro uživatelskou rovinu PC5. Jeho vytvoření bylo motivováno potřebou zabezpečené komunikace mimo síť, která je zásadní pro záchranné složky, když je buněčná infrastruktura poškozena. Také umožňuje zabezpečené V2X aplikace, kde vozidla přímo vyměňují bezpečnostní zprávy (např. varování před kolizí), což vyžaduje silnou důvěrnost pro ochranu soukromí řidičů a prevenci podvržení. PEK zaplňuje bezpečnostní mezeru pro přímou komunikaci a zajišťuje, že služby ProSe splňují přísné požadavky na důvěrnost očekávané od systémů 3GPP.

## Klíčové vlastnosti

- Zajišťuje důvěrnost uživatelských dat na postranním spojení (sidelink) rozhraní PC5
- Odvozen jako součást hierarchie bezpečnostních klíčů ProSe definované v TS 33.303
- Používán vrstvou PDCP pro procedury šifrování/dešifrování
- Podporuje komunikaci ProSe založenou na LTE i NR sidelink (V2X)
- Spravován prostřednictvím procedur navázání a správy klíčů ProSe
- Umožňuje zabezpečenou přímou komunikaci nezávislou na síťové infrastruktuře

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)

## Definující specifikace

- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pek/)
