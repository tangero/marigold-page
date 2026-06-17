---
slug: "dece"
url: "/mobilnisite/slovnik/dece/"
type: "slovnik"
title: "DECE – Digital Entertainment Content Ecosystem"
date: 2025-01-01
abbr: "DECE"
fullName: "Digital Entertainment Content Ecosystem"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dece/"
summary: "DECE je standardizovaný ekosystém pro správu a distribuci digitálního zábavního obsahu napříč více zařízeními a platformami. Umožňuje zabezpečené doručování obsahu, správu práv a interoperabilitu mezi"
---

DECE je standardizovaný ekosystém pro zabezpečenou správu a distribuci digitálního zábavního obsahu napříč více zařízeními a platformami v rámci sítí 3GPP.

## Popis

Digital Entertainment Content Ecosystem (DECE) je komplexní rámec definovaný v 3GPP TS 26.949, který stanovuje standardizované mechanismy pro komplexní správu digitálního zábavního obsahu v mobilních sítích. Architektura funguje na základě vícevrstvého přístupu zahrnujícího přípravu obsahu, zabezpečenou distribuci, správu práv a konzumaci na různorodých zařízeních. V jádru DECE implementuje systém úschovy práv (rights locker), kde jsou uživatelská oprávnění uložena nezávisle na samotném obsahu, což umožňuje flexibilní přístup napříč různými zařízeními a poskytovateli služeb při zachování přísné ochrany autorských práv.

DECE funguje prostřednictvím několika klíčových funkčních komponent: Content Preparation System ([CPS](/mobilnisite/slovnik/cps/)), který kóduje a balí média podle specifikací DECE; Rights Management System (RMS), který řeší uživatelskou autentizaci, autorizaci a sledování oprávnění; Content Distribution Network ([CDN](/mobilnisite/slovnik/cdn/)) optimalizovaný pro doručování obsahu DECE; a Device Client, který implementuje potřebné protokoly pro získání obsahu, dešifrování a přehrávání. Ekosystém využívá standardizované šifrovací schémata, protokoly pro výměnu klíčů a technologie správy digitálních práv ([DRM](/mobilnisite/slovnik/drm/)), které jsou interoperabilní mezi různými implementacemi při zachování ochrany obsahu.

V síťové architektuře se DECE integruje s existujícími platformami služeb 3GPP, včetně IP Multimedia Subsystem (IMS) pro autentizaci a řízení služeb, rámce Policy and Charging Control (PCC) pro správu kvality služeb a Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) pro efektivní distribuci obsahu. Systém podporuje jak streamovací, tak stahovací modely doručování s možnostmi adaptivního datového toku, což umožňuje optimální kvalitu na základě síťových podmínek a možností zařízení. Obsah může být doručován prostřednictvím unicastových, multicastových nebo broadcastových mechanismů v závislosti na požadavcích služby a ohledech na síťovou efektivitu.

Role DECE v síti přesahuje pouhé doručování obsahu a zahrnuje sofistikované obchodní modely, jako jsou služby předplatného, platba za přehrání, elektronický prodej a pronájmy s časově omezeným přístupem. Ekosystém podporuje přenositelnost obsahu prostřednictvím společného formátu souboru a specifikací interoperability, což uživatelům umožňuje přístup ke zakoupenému obsahu na různých zařízeních a sítích bez nutnosti opětovného nákupu. Toho je dosaženo prostřednictvím standardizovaných schémat metadat, identifikátorů obsahu a jazyků pro vyjádření práv, které zajišťují konzistentní interpretaci pravidel použití v celém ekosystému.

Technická implementace zahrnuje podporu více systémů DRM prostřednictvím společného šifrovacího schématu ([CENC](/mobilnisite/slovnik/cenc/)), což umožňuje poskytovatelům obsahu zašifrovat obsah jednou a distribuovat jej na zařízení podporující různé technologie DRM. DECE také specifikuje mechanismy pro tzv. superdistribuci obsahu, což uživatelům umožňuje sdílet obsah při zachování kontroly nad právy k použití. Ekosystém obsahuje ustanovení pro vyhledávání obsahu, systémy doporučení a personalizované doručování obsahu na základě uživatelských preferencí a vzorců spotřeby, čímž vytváří komplexní zážitek z digitální zábavy v prostředí sítí 3GPP.

## K čemu slouží

DECE byl vytvořen, aby řešil roztříštěnost v distribuci digitálního obsahu, která se objevila na počátku 10. let 21. století, kdy různí poskytovatelé obsahu, výrobci zařízení a síťoví operátoři implementovali proprietární systémy, které byly vzájemně nekompatibilní. Tato roztříštěnost vytvářela bariéry pro konzumaci obsahu, omezovala výběr uživatelů a zvyšovala náklady pro poskytovatele obsahu, kteří museli podporovat více formátů a systémů [DRM](/mobilnisite/slovnik/drm/). 3GPP uznalo, že se mobilní sítě stávají primární platformou pro konzumaci digitální zábavy, a potřebovalo standardizovaný přístup k zajištění interoperability a škálovatelnosti.

Tato technologie řeší několik kritických problémů: odstraňuje potřebu, aby poskytovatelé obsahu vytvářeli více verzí stejného obsahu pro různé platformy, snižuje složitost pro výrobce zařízení, kteří mohou implementovat jediného standardizovaného klienta, a poskytuje uživatelům bezproblémový přístup k obsahu napříč jejich zařízeními. Před DECE se uživatelé často ocitali uzamčeni v konkrétních ekosystémech, kde k obsahu zakoupenému na jednom zařízení nebylo možné přistoupit na jiném, a to ani v rámci služeb stejného síťového operátora. To způsobovalo frustraci a omezovalo růst trhů s digitálním obsahem v mobilním prostředí.

Historicky distribuce digitálního obsahu v mobilních sítích spoléhala na proprietární řešení od jednotlivých agregátorů obsahu nebo implementace specifické pro dané zařízení. DECE tyto limity řešil vytvořením otevřeného, standardizovaného ekosystému, který mohli přijmout všichni zúčastnění, při zachování silné ochrany obsahu požadované držiteli práv. Motivací byl rostoucí význam multimediálních služeb v sítích 3GPP a potřeba vytvořit udržitelný obchodní model pro všechny účastníky hodnotového řetězce. Standardizací technického rámce DECE umožnil úspory z rozsahu, snížil implementační náklady a vytvořil konkurenceschopnější trh pro služby digitální zábavy v mobilních sítích.

## Klíčové vlastnosti

- Standardizované šifrování obsahu pomocí schématu Common Encryption (CENC)
- Interoperabilní správa práv podporující více systémů DRM
- Společný formát souboru pro konzistentní balení a doručování obsahu
- Architektura úschovy práv (rights locker) pro přenositelnost obsahu napříč zařízeními
- Integrace s 3GPP PCC pro správu kvality služeb
- Podpora více obchodních modelů včetně předplatného a transakčních

## Související pojmy

- [DRM – Data call Routeing Mechanism](/mobilnisite/slovnik/drm/)
- [CENC – Common Encryption](/mobilnisite/slovnik/cenc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [DECE na 3GPP Explorer](https://3gpp-explorer.com/glossary/dece/)
