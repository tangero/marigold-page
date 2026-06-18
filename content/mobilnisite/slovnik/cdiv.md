---
slug: "cdiv"
url: "/mobilnisite/slovnik/cdiv/"
type: "slovnik"
title: "CDIV – Communication DIVersion"
date: 2026-01-01
abbr: "CDIV"
fullName: "Communication DIVersion"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdiv/"
summary: "Soubor doplňkových služeb umožňující uživateli přesměrovat příchozí komunikační relace (hovory, zprávy) na základě konfigurovatelných pravidel. Umožňuje flexibilní obsluhu hovorů, zvyšuje dostupnost u"
---

CDIV je soubor doplňkových služeb umožňující uživateli přesměrovat příchozí komunikační relace na alternativní destinace na základě konfigurovatelných pravidel.

## Popis

Communication DIVersion (CDIV) je standardizovaná sada doplňkových služeb v rámci architektury IP Multimedia Subsystem (IMS) dle 3GPP, která poskytuje dynamickou kontrolu nad směrováním příchozích komunikačních relací. Tyto relace primárně zahrnují hlasové hovory, ale v závislosti na konfiguraci služby mohou zahrnovat i další multimediální relace, jako jsou videohovory a zasílání zpráv. Základní princip spočívá v zachycení příchozí žádosti o relaci (např. [SIP](/mobilnisite/slovnik/sip/) INVITE) v síťovém řídicím bodě – typicky ve Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v jádru IMS – a aplikaci uživatelsky definované logiky pro rozhodnutí, zda relaci dokončit k původnímu cíli, nebo ji přesměrovat jinam. Tuto logiku provádí aplikační server (Application Server, [AS](/mobilnisite/slovnik/as/)) hostující servisní logiku CDIV, který dotazuje data účastníka a pravidla uložená v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo v dedikovaném úložišti servisních profilů.

Služba funguje na základě komplexní sady kritérií a podmínek pro přesměrování definovaných ve specifikacích 3GPP. Mezi klíčové spouštěče přesměrování patří Busy (když je linka uživatele obsazena), No Reply (když uživatel neodpoví v konfigurovatelném čase), Not Reachable (když je zařízení uživatele odpojeno od sítě nebo v oblasti bez rádiového pokrytí) a Unconditional (přesměrování všech příchozích relací bez ohledu na stav). Dále lze konfigurovat pokročilejší podmínky, jako je přesměrování při odhlášení uživatele nebo na základě identity volajícího (např. konkrétní čísla nebo anonymní hovory). Když je podmínka splněna, CDIV AS vydá pokyn S-CSCF k přesměrování signalizace relace na novou cílovou adresu, což může být jiné telefonní číslo, server hlasové schránky nebo schránka pro instant messaging. Toto přesměrování se provádí pomocí standardních odpovědí pro přesměrování SIP (např. 302 Moved Temporarily) nebo tím, že AS funguje jako back-to-back user agent ([B2BUA](/mobilnisite/slovnik/b2bua/)) a vytvoří novou větev k cíli přesměrování.

Z architektonického hlediska je CDIV hluboce integrováno s platformou pro poskytování služeb IMS. Počáteční filtrační kritéria (Initial Filter Criteria, iFC) v servisním profilu uživatele, která jsou během registrace stažena z HSS do S-CSCF, zajišťují, že všechny relevantní požadavky na zahájení relace jsou předány určenému CDIV aplikačnímu serveru ke zpracování. Servisní logika na AS vyhodnocuje aktivní nastavení přesměrování účastníka, které si uživatel může typicky spravovat prostřednictvím rozhraní Ut ([XCAP](/mobilnisite/slovnik/xcap/)) pro samoobslužnou správu nebo prostřednictvím profilů spravovaných operátorem. CDIV hraje v servisní vrstvě IMS klíčovou roli tím, že odděluje veřejnou identitu uživatele (volané číslo) od skutečného koncového bodu, což umožňuje bohatou osobní mobilitu a personalizaci služeb. Jeho implementace musí také zvládat interakce s dalšími doplňkovými službami, jako je Communication Waiting ([CW](/mobilnisite/slovnik/cw/)) a Communication Hold ([HOLD](/mobilnisite/slovnik/hold/)), při dodržování standardizovaných pravidel přednosti pro zamezení konfliktů, a zajistit správné generování záznamů o účtování (CDR) pro původní i přesměrovanou větev hovoru.

## K čemu slouží

CDIV bylo vytvořeno za účelem poskytnutí standardizované, na síti založené schopnosti přesměrování hovorů pro IP multimediální služby, čímž řeší omezení starších služeb přesměrování v okruhově přepínaných sítích a umožňuje bezproblémovou kontinuitu služeb v rozvíjející se architektuře IMS. Před IMS byly funkce přesměrování, jako je přesměrování hovoru (Call Forwarding), implementovány v okruhově přepínaných mobilních sítích (GSM) a pevných sítích, ale ty byly často proprietární, omezeného rozsahu a obtížně integrovatelné s novými IP aplikacemi. Přechod na plně IP sítě vyžadoval nový, flexibilní mechanismus, který by mohl fungovat napříč různými přístupovými sítěmi (např. LTE, 5G, WLAN) a podporovat multimediální relace přesahující jednoduché hlasové hovory. CDIV řeší problém dostupnosti uživatele a personalizace služeb v komplexním prostředí s více zařízeními tím, že uživatelům umožňuje definovat inteligentní pravidla směrování, která odrážejí jejich dostupnost a preference.

Primární motivací bylo replikovat a vylepšit oblíbené funkce přesměrování hovorů ze starších systémů v rámci architektury IMS, což zajišťuje zpětnou kompatibilitu pro poskytovatele služeb migrující své sítě a zároveň umožňuje nové, bohatší scénáře přesměrování. Řeší klíčové potřeby uživatelů, jako je vyhýbání se zmeškaným hovorům, filtrování nežádoucí komunikace a vytvoření jediného kontaktního bodu, který může uživatele zastihnout na jakémkoli zařízení. Z pohledu síťového operátora CDIV zlepšuje využití síťových zdrojů efektivním přesměrováním relací, které by jinak vedly k neúspěšným pokusům o spojení a zbytečné signalizační zátěži. Standardizací CDIV v rámci 3GPP počínaje Release 7 byla zajištěna interoperabilita mezi zařízeními IMS od různých dodavatelů a umožněno vytvoření konzistentního uživatelského zážitku napříč různými poskytovateli služeb a typy zařízení, čímž se stala základní službou pro komerční nasazení VoLTE a VoNR.

## Klíčové vlastnosti

- Bezpodmínečné přesměrování všech příchozích relací na předem definovanou adresu
- Podmíněné přesměrování na základě stavu účastníka (Busy, No Reply, Not Reachable)
- Přesměrování na základě identity volajícího (např. z konkrétních čísel nebo anonymních hovorů)
- Podpora přesměrování na různé cílové adresy v závislosti na spouštěcí podmínce
- Integrace s jádrem IMS prostřednictvím počátečních filtračních kritérií (iFC) a aplikačního serveru (AS)
- Správa uživatelských nastavení prostřednictvím rozhraní Ut (XCAP) pro samostatnou správu pravidel přesměrování

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 22.401** (Rel-8) — Videotelephony Service Requirements for NGN
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.196** (Rel-19) — Enhanced Calling Name (eCNAM) Stage 3 Protocol
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.315** (Rel-19) — Operator Determined Barring (ODB) for IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [CDIV na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdiv/)
