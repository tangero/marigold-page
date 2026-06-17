---
slug: "cenc"
url: "/mobilnisite/slovnik/cenc/"
type: "slovnik"
title: "CENC – Common Encryption"
date: 2025-01-01
abbr: "CENC"
fullName: "Common Encryption"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cenc/"
summary: "CENC je standardizované šifrování a schéma správy klíčů pro ochranu mediálního obsahu v systémech 3GPP. Umožňuje zabezpečené doručování multimediálních služeb, jako je MBMS a streamování, tím, že posk"
---

CENC je v rámci 3GPP standardizované šifrování a schéma správy klíčů pro ochranu mediálního obsahu. Umožňuje zabezpečené doručování multimédií, jako je MBMS, různými metodami při zachování interoperability.

## Popis

Common Encryption (CENC, Společné šifrování) je komplexní rámec pro ochranu obsahu definovaný ve specifikacích 3GPP, který poskytuje standardizované šifrování a správu klíčů pro multimediální služby. Jeho architektura funguje na principu oddělení šifrování samotného mediálního obsahu od správy a distribuce dešifrovacích klíčů. Obsah je šifrován jednou u zdroje pomocí standardizovaných šifrovacích algoritmů, zatímco odpovídající dešifrovací klíče jsou spravovány a distribuovány samostatným, zabezpečeným systémem distribuce klíčů. Toto oddělení umožňuje flexibilní modely poskytování služeb, kdy může být stejný šifrovaný obsah distribuován více kanály při zachování konzistentní úrovně zabezpečení.

Technická implementace CENC zahrnuje několik klíčových komponent pracujících společně. Komponenta Content Encryption aplikuje šifrování na mediální segmenty pomocí algoritmů specifikovaných ve standardu, typicky AES-128 v [CTR](/mobilnisite/slovnik/ctr/) módu. Systém pro správu klíčů (Key Management System, [KMS](/mobilnisite/slovnik/kms/)) generuje, ukládá a spravuje šifrovací klíče obsahu (Content Encryption Keys, CEK) používané pro šifrování médií. Komponenta License Server vydává licence obsahující CEK oprávněným klientům, často za použití systémů správy digitálních práv (Digital Rights Management, [DRM](/mobilnisite/slovnik/drm/)). Komponenta Media Delivery zajišťuje přenos šifrovaných médií různými kanály včetně [MBMS](/mobilnisite/slovnik/mbms/), unicastového streamování nebo služeb stažení. Nakonec agent DRM na uživatelských zařízeních přijímá licence, získává CEK a provádí dešifrování pro přehrání.

CENC funguje prostřednictvím jasně definovaného pracovního postupu, který začíná přípravou obsahu. Poskytovatel služby zašifruje mediální obsah pomocí šifrovacího klíče obsahu (CEK), čímž vzniknou šifrované mediální segmenty zabalené podle standardů jako [DASH](/mobilnisite/slovnik/dash/) nebo [HLS](/mobilnisite/slovnik/hls/). CEK je poté bezpečně přenesen do systému pro správu klíčů. Když uživatel požádá o přístup k chráněnému obsahu, jeho zařízení kontaktuje licenční server, který uživatele ověří a určí jeho práva. Po úspěšné autorizaci licenční server poskytne klientovi licenci obsahující CEK (často zabalený klíčem specifickým pro dané zařízení). DRM agent klienta extrahuje CEK, dešifruje mediální segmenty a obsah vykreslí pro přehrání.

V architektuře sítí 3GPP hraje CENC klíčovou roli při umožnění zabezpečených multimediálních služeb napříč vysílacími i unicastovými způsoby distribuce. Pro MBMS (Multimedia Broadcast Multicast Service) CENC zajišťuje, aby byl vysílaný obsah chráněn i při efektivním doručování více uživatelům současně. Pro unicastové streamovací služby poskytuje konzistentní ochranu obsahu bez ohledu na podkladový transportní protokol. Standardizace tohoto rámce umožňuje různým DRM systémům interoperovat se stejným šifrovaným obsahem, což poskytovatelům služeb dává flexibilitu ve výběru DRM řešení při zachování zabezpečení obsahu. Tato interoperabilita je zvláště důležitá v heterogenních síťových prostředích, kde obsah může procházet různými sítěmi a být konzumován na různých zařízeních.

## K čemu slouží

CENC byl vytvořen, aby řešil rostoucí potřebu standardizované ochrany obsahu v multimediálních službách 3GPP. Před jeho zavedením čelili poskytovatelé obsahu významným výzvám při zabezpečování médií distribuovaných prostřednictvím mobilních sítí, zejména s nástupem [MBMS](/mobilnisite/slovnik/mbms/) pro vysílací služby. Různí výrobci a poskytovatelé služeb implementovali proprietární šifrovací schémata bez interoperability, což vytvářelo fragmentaci v ekosystému. Pro vlastníky obsahu bylo obtížné distribuovat chráněná média přes více sítí a na různá zařízení bez nutnosti implementace více nekompatibilních ochranných systémů.

Primární motivací pro vývoj CENC bylo vytvoření společného šifrovacího rámce, který by umožnil zabezpečené doručování obsahu při zachování interoperability mezi různými systémy [DRM](/mobilnisite/slovnik/drm/) a poskytovateli služeb. Tradiční přístupy vyžadovaly, aby byl obsah pro každý DRM systém šifrován zvlášť, což zvyšovalo náklady na úložiště a složitost pro distributory obsahu. CENC tento problém řeší tím, že umožňuje obsah zašifrovat jednou pomocí standardizovaných metod, přičemž různé DRM systémy mohou k témuž šifrovanému obsahu přistupovat prostřednictvím svých příslušných systémů správy klíčů. To výrazně snižuje provozní režii pro přípravu a distribuci obsahu.

Dalším klíčovým problémem, který CENC řeší, je bezpečné doručování vysílaného obsahu prostřednictvím MBMS. Vysílací distribuce přináší jedinečné bezpečnostní výzvy, protože stejný obsah je posílán více uživatelům současně, což činí tradiční bezpečnostní mechanismy typu point-to-point neefektivní. CENC poskytuje rámec, kde může být vysílaný obsah efektivně chráněn a zároveň mohou autorizovaní uživatelé získávat dešifrovací klíče prostřednictvím unicastových kanálů. Tento hybridní přístup kombinuje efektivitu vysílací distribuce s bezpečností individualizované správy klíčů a umožňuje škálovatelné zabezpečené multimediální služby napříč sítěmi 3GPP.

## Klíčové vlastnosti

- Standardizované šifrování mediálního obsahu pomocí AES-128 v CTR módu
- Oddělení šifrování obsahu od správy klíčů umožňující interoperabilitu DRM
- Podpora více formátů balení včetně DASH a HLS
- Integrace s MBMS pro zabezpečené doručování vysílaného obsahu
- Flexibilní distribuce klíčů prostřednictvím licenčních serverů a systémů DRM
- Kompatibilita s více systémy DRM včetně PlayReady, Widevine a FairPlay

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [DRM – Data call Routeing Mechanism](/mobilnisite/slovnik/drm/)

## Definující specifikace

- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.953** (Rel-19) — Study on Service Interactivity for Streaming & Download

---

📖 **Anglický originál a plná specifikace:** [CENC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cenc/)
