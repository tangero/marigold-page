---
slug: "eme"
url: "/mobilnisite/slovnik/eme/"
type: "slovnik"
title: "EME – Encrypted Media Extensions"
date: 2025-01-01
abbr: "EME"
fullName: "Encrypted Media Extensions"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eme/"
summary: "Encrypted Media Extensions (EME, rozšíření pro šifrovaná média) je rámec definovaný 3GPP pro zabezpečené doručování a přehrávání šifrovaného mediálního obsahu, jako je video chráněné DRM, přes mobilní"
---

EME je rámec definovaný 3GPP pro zabezpečené doručování a přehrávání šifrovaného mediálního obsahu, jako je video chráněné DRM, přes mobilní sítě.

## Popis

Encrypted Media Extensions (EME) je specifikace definující JavaScript [API](/mobilnisite/slovnik/api/) pro řízení přehrávání chráněného obsahu ve webových prohlížečích. Funguje jako mezivrstva mezi webovými aplikacemi a moduly pro dešifrování obsahu ([CDM](/mobilnisite/slovnik/cdm/)), které jsou zodpovědné za dešifrování šifrovaných mediálních proudů. Architektura zahrnuje webovou aplikaci, která požaduje MediaKeySession od objektu MediaKeys prohlížeče, který následně komunikuje s CDM za účelem získání licence a provedení dešifrování. Klíčové komponenty zahrnují rozhraní MediaKeys pro správu klíčů, MediaKeySession pro jednotlivé dešifrovací relace a CDM, které provádí vlastní kryptografické operace, často implementované jako platformně specifický modul nebo hardwarový bezpečnostní prvek.

EME funguje tak, že umožňuje webovým aplikacím detekovat podporované [DRM](/mobilnisite/slovnik/drm/) systémy pomocí API requestMediaKeySystemAccess. Jakmile je přístup udělen, aplikace vytvoří MediaKeySession a poskytne šifrovaná mediální data, typicky zabalená ve formátech jako MPEG-DASH nebo [HLS](/mobilnisite/slovnik/hls/) s Common Encryption ([CENC](/mobilnisite/slovnik/cenc/)). CDM prostřednictvím rozhraní EME získá licence z licenčního serveru, dešifruje obsah a předá čistá média do mediálního řetězce prohlížeče k přehrání. Tento proces zajišťuje, že dešifrovaný obsah nikdy neopustí zabezpečené prostředí CDM, čímž je zachována ochrana obsahu.

V ekosystému 3GPP je EME klíčové pro umožnění prémiových mediálních služeb, jako je mobilní TV a streamování videa, přes sítě LTE a 5G. Standardizuje interoperabilitu DRM, což umožňuje poskytovatelům obsahu nasazovat služby na široké škále zařízení bez nutnosti vlastních integrací pro každou DRM technologii. Role EME sahá až k zajištění souladu s požadavky vlastníků obsahu na zabezpečenou distribuci, čímž podporuje komerční životaschopnost médií s vysokou hodnotou přes mobilní broadband. Specifikace jako 26.307, 26.804, 26.857 a 26.907 detailně popisují jeho integraci s multimediálními službami 3GPP, pokrývající aspekty jako streamovací protokoly a kvalitu uživatelského zážitku.

## K čemu slouží

EME bylo vytvořeno, aby vyřešilo absenci standardizované, multiplatformní metody pro přehrávání obsahu chráněného [DRM](/mobilnisite/slovnik/drm/) ve webových prohlížečích. Před EME se poskytovatelé obsahu spoléhali na zásuvné moduly prohlížeče, jako Adobe Flash nebo Silverlight, které byly nezabezpečené, neefektivní a nepodporované na všech zařízeních, zejména mobilních. Tato fragmentace bránila doručování prémiových video služeb přes web a mobilní sítě a omezovala obchodní modely pro streamování médií.

Motivace pro EME vycházela z rostoucí poptávky po šifrovaných streamovacích službách, jako jsou Netflix a Hulu, které vyžadovaly robustní ochranu obsahu pro splnění licenčních dohod. Poskytnutím společného [API](/mobilnisite/slovnik/api/) umožňuje EME prohlížečům komunikovat s různými DRM systémy (např. Widevine, PlayReady, FairPlay) bez vystavení citlivé dešifrovací logiky. Tím se řeší problém rozmanitosti zařízení a platforem v mobilním ekosystému a umožňuje bezproblémové doručování obsahu na chytré telefony, tablety a další připojená zařízení.

Historicky 3GPP začlenilo EME ve vydání 12 pro podporu multimediálních služeb přes LTE, když uznalo potřebu zabezpečeného doručování médií jako součást svých širších multimediálních standardů. Vyřešilo omezení dřívějších přístupů odstraněním závislosti na zásuvných modulech, zlepšením bezpečnosti prostřednictvím izolovaných [CDM](/mobilnisite/slovnik/cdm/) a zvýšením výkonu integrací dešifrování do nativního mediálního řetězce prohlížeče. Tento vývoj byl hnán spoluprácí v odvětví mezi výrobci prohlížečů, poskytovateli obsahu a standardizačními orgány za účelem vytvoření otevřeného webového standardu pro šifrovaná média.

## Klíčové vlastnosti

- Standardizované JavaScript API pro integraci DRM ve webových prohlížečích
- Podpora více modulů pro dešifrování obsahu (CDM) prostřednictvím společného rozhraní
- Zabezpečené získávání licencí a správa klíčů v rámci MediaKeySession
- Kompatibilita s Common Encryption (CENC) pro balení médií
- Integrace s HTML5 video elementy pro plynulé přehrávání
- Multiplatformní podpora napříč mobilními zařízeními, počítači a chytrými TV

## Související pojmy

- [DRM – Data call Routeing Mechanism](/mobilnisite/slovnik/drm/)

## Definující specifikace

- **TS 26.307** (Rel-19) — 3GPP HTML5 Profile Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.857** (Rel-18) — Technical Report on Media Service Enablers
- **TR 26.907** (Rel-19) — HTML5 for 3GPP Services Study

---

📖 **Anglický originál a plná specifikace:** [EME na 3GPP Explorer](https://3gpp-explorer.com/glossary/eme/)
