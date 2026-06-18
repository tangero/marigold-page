---
slug: "xdmc"
url: "/mobilnisite/slovnik/xdmc/"
type: "slovnik"
title: "XDMC – XML Document Management Client"
date: 2025-01-01
abbr: "XDMC"
fullName: "XML Document Management Client"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/xdmc/"
summary: "XML Document Management Client (XDMC) je funkční entita v rámci 3GPP XDM, která umožňuje uživatelskému zařízení nebo aplikačním serverům komunikovat s XDM servery za účelem správy XML dokumentů. Použí"
---

XDMC je funkční klient v rámci 3GPP XDM, který umožňuje uživatelskému zařízení (UE) nebo aplikačním serverům spravovat XML dokumenty (např. seznamy kontaktů) na XDM serverech s využitím protokolu XCAP.

## Popis

[XML](/mobilnisite/slovnik/xml/) Document Management Client (XDMC) je klientská komponenta v rámci architektury 3GPP XML Document Management ([XDM](/mobilnisite/slovnik/xdm/)), která je zodpovědná za iniciaci požadavků na správu XML dokumentů uložených na XDM serverech ([XDMS](/mobilnisite/slovnik/xdms/)). Typicky je implementována v uživatelském zařízení (UE), jako jsou chytré telefony nebo zařízení IoT, nebo v aplikačních serverech, které vyžadují přístup k uživatelským datům služeb. XDMC komunikuje s XDM serverem pomocí protokolu XML Configuration Access Protocol ([XCAP](/mobilnisite/slovnik/xcap/)) přes [HTTP](/mobilnisite/slovnik/http/) a podporuje operace jako HTTP GET (načtení), PUT (vytvoření/aktualizace) a DELETE (odstranění) nad XML dokumenty. Tyto dokumenty obsahují konfigurační data pro různé služby, například pravidla autorizace pro službu presence, definice skupin pro zasílání zpráv nebo uživatelské preference pro multimediální aplikace.

Fungování XDMC zahrnuje několik kroků: nejprve se autentizuje v síti, často přes agregační proxy (Aggregation Proxy), která slouží jako brána k XDM serveru. Po autentizaci XDMC vytváří XCAP požadavky cílené na konkrétní XML dokumenty identifikované pomocí [URI](/mobilnisite/slovnik/uri/) (Uniform Resource Identifier). Například pro aktualizaci seznamu kontaktů služby presence odešle XDMC HTTP PUT požadavek s upraveným XML obsahem na příslušný XDMS. XDMC také zpracovává odpovědi ze serveru, včetně chybových kódů a řešení konfliktů, čímž zajišťuje konzistenci dat. Dále může XDMC odebírat informace o změnách dokumentů pomocí notifikací založených na [SIP](/mobilnisite/slovnik/sip/), což mu umožňuje přijímat aktualizace, když jiní klienti upravují sdílené dokumenty, a tím umožnit synchronizaci napříč službami v reálném čase.

Klíčové součásti XDMC zahrnují XCAP klienta, který implementuje logiku protokolu; správce dokumentů (Document Manager), který zajišťuje lokální ukládání do mezipaměti a zpracování XML dat; a rozhraní (Interface Layer), které se integruje s aplikační vrstvou zařízení nebo s podpůrnými službami (service enablers). Funkce XDMC jsou podrobně popsány v technických specifikacích, jako je TS 24.481 pro detaily protokolu XCAP a TS 24.549 pro chování XDM klienta. Jeho role je klíčová pro umožnění uživatelsky orientovaných služeb, neboť poskytuje prostředky pro přímou správu dat uživateli z jejich zařízení. Například ve službě skupinového chatu umožňuje XDMC uživateli přidávat kontakty do skupinového seznamu uloženého v síti, k němuž pak mohou přistupovat více aplikací. Standardizací chování klienta XDMC zajišťuje interoperabilitu mezi různými zařízeními a síťovými implementacemi a podporuje širokou škálu služeb 3GPP, od základního hlasového přenosu přes LTE (VoLTE) až po pokročilé multimediální aplikace 5G.

## K čemu slouží

[XML](/mobilnisite/slovnik/xml/) Document Management Client (XDMC) byl vyvinut, aby poskytoval standardizované klientské rozhraní pro správu dat služeb založených na XML v sítích 3GPP, a řešil tak potřebu uživatelsky řízené a aplikacemi přístupné konfigurační správy. Před zavedením XDMC byla správa dat služeb často centralizovaná na serverech nebo spoléhala na proprietární klientské implementace, což omezovalo autonomii uživatelů a způsobovalo problémy s kompatibilitou. XDMC tento problém řeší definicí společného klientského protokolu (XCAP), který umožňuje jakémukoliv kompatibilnímu zařízení nebo aplikaci komunikovat s XDM servery, čímž posiluje možnost uživatelů přizpůsobovat si své služby a umožňuje hladkou integraci napříč různými podpůrnými službami (service enablers).

Historicky, s rozšířením IMS a pokročilých komunikačních služeb, vzrostla poptávka po klientech schopných efektivně zpracovávat data služeb bez nutnosti složité integrace na straně sítě. XDMC, představený v 3GPP Release 13 jako vývoj dřívějších konceptů XDM, byl motivován rozšířením chytrých telefonů a potřebou konzistentní správy dat napříč různými aplikacemi. Řeší omezení ad-hoc klientských implementací tím, že poskytuje jednotnou metodu pro operace s dokumenty, snižuje tak vývojovou náročnost a zlepšuje uživatelský zážitek. Například před XDMC mohla správa skupinových seznamů vyžadovat samostatné klienty pro zasílání zpráv, službu presence a konferenční hovory, což vedlo k fragmentaci dat.

Účel XDMC sahá také k podpoře regulatorních a soukromí se týkajících požadavků, neboť umožňuje uživatelům řídit přístup ke svým datům prostřednictvím aktualizací iniciovaných klientem. Také napomáhá síťové efektivitě přesunutím zpracování dokumentů na stranu klienta, čímž se snižuje zatížení serverů. V kontextu 5G a IoT umožňuje XDMC lehkovějším klientům pro zařízení s omezenými prostředky spravovat konfigurační data, čímž podporuje případy užití jako jsou nasazení v chytrých městech. Tím, že XDMC slouží jako uživatelské koncové rozhraní architektury XDM, hraje zásadní roli při naplňování vize personalizovaných a interoperabilních služeb v moderních sítích 3GPP.

## Klíčové vlastnosti

- Implementace protokolu XCAP pro správu dokumentů založenou na HTTP
- Podpora operací CRUD (vytvořit, přečíst, aktualizovat, smazat) nad XML dokumenty
- Integrace s agregační proxy (Aggregation Proxy) pro autentizaci a směrování
- Odběr notifikací o změnách dokumentů pomocí SIP
- Lokální ukládání do mezipaměti a řešení konfliktů pro možnost práce offline
- Spolupráce s podpůrnými službami (service enablers) jako jsou presence a zasílání zpráv

## Definující specifikace

- **TS 24.481** (Rel-19) — Mission Critical Services (MCS) group management
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.549** (Rel-19) — SEAL Network Slice Capability Enablement Protocol

---

📖 **Anglický originál a plná specifikace:** [XDMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/xdmc/)
