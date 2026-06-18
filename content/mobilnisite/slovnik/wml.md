---
slug: "wml"
url: "/mobilnisite/slovnik/wml/"
type: "slovnik"
title: "WML – Wireless Mark-up Language"
date: 2025-01-01
abbr: "WML"
fullName: "Wireless Mark-up Language"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wml/"
summary: "Wireless Mark-up Language (WML) je značkovací jazyk založený na XML, navržený pro specifikaci obsahu a uživatelských rozhraní pro mobilní zařízení s omezenými možnostmi. Byl součástí sady protokolů Wi"
---

WML je značkovací jazyk založený na XML, navržený pro specifikaci obsahu a uživatelských rozhraní pro mobilní zařízení s omezenými možnostmi, jako součást sady protokolů Wireless Application Protocol (WAP).

## Popis

Wireless Mark-up Language (WML) je jazyk založený na [XML](/mobilnisite/slovnik/xml/), který definuje strukturu, prezentaci a interakci obsahu doručovaného do mobilních zařízení. Je klíčovou součástí architektury Wireless Application Protocol ([WAP](/mobilnisite/slovnik/wap/)) verze 1.x. WML dokumenty, nazývané 'decky' (balíčky), se skládají z více 'karet' (card). Deck je jednotkou přenosu, zatímco karta představuje jednu obrazovku informací nebo interakce na zařízení. Tato struktura je optimalizována pro omezenou paměť a výpočetní výkon starších mobilních telefonů tím, že umožňuje přenos více obrazovek obsahu v jedné transakci.

WML funguje tak, že je vytvářen poskytovateli obsahu a následně doručován prostřednictvím WAP brány. WAP telefon uživatele obsahuje WML prohlížeč (mikroprohlížeč). Zařízení požádá o [URL](/mobilnisite/slovnik/url/), což je směrováno přes WAP bránu. Brána získá WML obsah ze zdrojového serveru (s případnou konverzí z [HTTP](/mobilnisite/slovnik/http/) na WAP protokoly) a přenese jej do zařízení pomocí Wireless Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)). Mikroprohlížeč poté analyzuje WML, vykreslí specifikované karty a zpracuje uživatelské interakce, jako je navigace mezi kartami nebo odesílání vstupů. WML obsahuje elementy pro text, obrázky, vstupní pole, kotvy pro navigaci a obsluhu událostí pro úkoly jako stisknutí soft kláves.

Klíčovými součástmi ekosystému WML jsou samotný WML skript, WML prohlížeč na klientovi, WAP brána fungující jako zprostředkovatel a překladač protokolů a obsahové servery. Úlohou WML v síti bylo poskytnout odlehčený, standardizovaný způsob dodávání interaktivních informačních služeb – jako jsou zprávy, e-mail, jednoduché transakce a podnikové aplikace – masovým mobilním telefonům před nástupem plnohodnotných [HTML](/mobilnisite/slovnik/html/) prohlížečů a vysokorychlostních datových připojení. Byl to klíčový krok v přenosu internetové zkušenosti do mobilního světa.

## K čemu slouží

WML byl vytvořen, aby řešil základní omezení starších mobilních zařízení a sítí pro přístup k informačním službám. Mobilní telefony na konci 90. let a počátku 21. století měly velmi malé obrazovky, omezenou paměť, nízký výpočetní výkon a datová připojení byla pomalá a drahá (používala GSM [CSD](/mobilnisite/slovnik/csd/) nebo raný [GPRS](/mobilnisite/slovnik/gprs/)). Plné HTML a robustní webové protokoly byly nepraktické. Sada protokolů Wireless Application Protocol (WAP), včetně WML, byla vyvinuta jako odlehčená alternativa.

Jejím účelem bylo definovat formát obsahu optimalizovaný pro tato omezení: binárně kódovaný pro efektivní přenos, strukturovaný do karet/decků pro minimalizaci počtu interakcí a s jednoduchou sadou tagů vhodných pro základní zobrazení a interakce. Tím bylo vyřešeno, jak doručit interaktivní obsah milionům základních telefonů, a umožněna tak první vlna mobilních internetových služeb. Poskytl standardizovaný jazyk, aby vývojáři obsahu, výrobci telefonů a síťoví operátoři mohli vzájemně spolupracovat, což podpořilo růst ekosystému mobilních dat, než se technologie vyvinula tak, aby podporovala skutečné mobilní webové prohlížení.

## Klíčové vlastnosti

- Syntaxe založená na XML pro definování struktury mobilního obsahu
- Model decku a karet pro sdružování více obrazovek
- Podpora textu, obrázků, vstupních polí a navigačních kotev
- Obsluha událostí pro interakce specifické pro zařízení (např. soft klávesy)
- Binární kódování (WMLC) pro kompaktní přenos přes bezdrátové spoje
- Navrženo pro vykreslování na mikroprohlížečích s nízkou pamětí

## Související pojmy

- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)
- [WMLS – Wireless Markup Language Script](/mobilnisite/slovnik/wmls/)

## Definující specifikace

- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [WML na 3GPP Explorer](https://3gpp-explorer.com/glossary/wml/)
