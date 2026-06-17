---
slug: "dls"
url: "/mobilnisite/slovnik/dls/"
type: "slovnik"
title: "DLS – Downloadable Sounds"
date: 2025-01-01
abbr: "DLS"
fullName: "Downloadable Sounds"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/dls/"
summary: "Služba 3GPP umožňující bezdrátové stahování zvukových souborů (jako vyzvánění a upozornění) do mobilního zařízení uživatele. Standardizuje formát, doručování a správu těchto zvukových souborů, čímž ob"
---

DLS je služba 3GPP, která standardizuje bezdrátové stahování, formát a správu zvukových souborů (např. vyzvánění) do mobilního zařízení za účelem personalizace.

## Popis

Downloadable Sounds (DLS) je standardizovaná služba v architektuře 3GPP, která umožňuje uživatelskému zařízení (UE) získávat a ukládat zvukový obsah primárně pro účely personalizace, jako jsou vyzvánění, tóny upozornění na zprávy a zvuky her. Služba je definována v několika specifikacích pokrývajících kodeky, formáty souborů a aplikační protokoly. Základní koncept spočívá v přenosu zvukového souboru, který odpovídá specifickému formátu (jako [AMR-WB](/mobilnisite/slovnik/amr-wb/)+ nebo MPEG-4 Audio), ze serveru poskytovatele služeb (nebo obsahového portálu) do UE prostřednictvím datových přenosů mobilní sítě (např. [GPRS](/mobilnisite/slovnik/gprs/), UMTS packet data).

Architektura zahrnuje několik klíčových komponent: UE s klientskou aplikací nebo schopností DLS, síť poskytující IP konektivitu (paketově spínaná doména) a obsahový server. Proces stahování typicky využívá standardní internetové protokoly jako [HTTP](/mobilnisite/slovnik/http/) nebo WAP pro přenos souborů. Specifikace 3GPP (TS 26.140, 26.141) však konkrétně definují zvukové kodeky a formáty souborů, aby zajistily interoperabilitu. Například TS 26.141 specifikuje formát 3GPP Sound File, což je kontejner založený na [ISO](/mobilnisite/slovnik/iso/) Base Media File Format, který zapouzdřuje kódované zvukové proudy. TS 26.234 (Transparent end-to-end Packet-switched Streaming Service - PSS) poskytuje protokoly, které lze použít pro stahování takového obsahu jako součást streamovací nebo stahovací služby.

Po stažení je zvukový soubor uložen v paměti UE. Operační systém nebo aplikační rámec UE pak uživateli umožňuje přiřadit stažený zvuk konkrétním událostem (příchozí hovor od kontaktu, nová SMS, budík). Správa těchto souborů – včetně výpisu, výběru, mazání – je řešena uživatelským rozhraním ([MMI](/mobilnisite/slovnik/mmi/)) UE. Role sítě je primárně transparentní, poskytuje datový přenos. Standardizace však zajišťuje, že zvukový soubor zakoupený nebo stažený z kompatibilního portálu bude správně přehrán na jakémkoli kompatibilním UE, čímž se předchází problémům s nekompatibilitou formátů, které byly běžné v raných fázích mobilního multimédia.

## K čemu slouží

DLS byl vytvořen za účelem standardizace a komercializace trhu s personalizovaným zvukem na mobilních telefonech, což představovalo posun od monofonních nebo polyfonních vyzvánění vestavěných ve firmwaru zařízení. Před standardizací výrobci používali proprietární formáty, což uzamykalo uživatele v ekosystému konkrétního dodavatele pro stahovatelný obsah a vytvářelo fragmentaci pro poskytovatele obsahu. To omezovalo růst odvětví mobilního obsahu. DLS tento problém vyřešil definováním otevřených, bezlicenčních (nebo široce licencovaných) zvukových kodeků (jako [AMR-WB](/mobilnisite/slovnik/amr-wb/)+) a společného formátu souborů.

Reagoval na uživatelskou poptávku po větší personalizaci a na zájem operátorů/poskytovatelů služeb o nový zdroj příjmů z prodeje obsahu. Standardizací technického mechanismu doručování umožnil vznik živého ekosystému tvůrců a distributorů obsahu třetích stran. Dále využil zlepšujících se datových schopností sítí 2.5G ([GPRS](/mobilnisite/slovnik/gprs/)) a 3G (UMTS) a proměnil je v platformy pro distribuci médií. Služba také zlepšila uživatelský zážitek tím, že umožnila vyšší kvalitu a bohatší zvuky (včetně skutečných úryvků nahrané hudby) ve srovnání s jednoduchými syntetizovanými tóny. Její vývoj byl součástí širšího úsilí 3GPP o definování multimediálních služeb (jako [MMS](/mobilnisite/slovnik/mms/), Streaming, DLS), které měly podpořit adopci paketově spínaných mobilních dat.

## Klíčové vlastnosti

- Standardizované zvukové kodeky pro mobilní zařízení (např. AMR-WB+, MPEG-4 AAC)
- Definovaný formát 3GPP Sound File pro kontejnerizaci a metadata
- Bezdrátové stahování prostřednictvím paketově spínaných síťových přenosů
- Umožňuje personalizaci vyzvánění, upozornění a dalších systémových zvuků
- Interoperabilita mezi různými výrobci telefonů a obsahovými servery
- Integrace s dalšími službami 3GPP, jako je Multimedia Messaging (MMS) a Packet-switched Streaming (PSS)

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification

---

📖 **Anglický originál a plná specifikace:** [DLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/dls/)
