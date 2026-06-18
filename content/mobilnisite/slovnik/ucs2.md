---
slug: "ucs2"
url: "/mobilnisite/slovnik/ucs2/"
type: "slovnik"
title: "UCS2 – Universal two byte coded Character Set"
date: 2025-01-01
abbr: "UCS2"
fullName: "Universal two byte coded Character Set"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ucs2/"
summary: "16bitový standard kódování znaků používaný v sítích 3GPP pro reprezentaci textu, zejména pro SMS a signalizaci v řídicí rovině. Umožňuje konzistentní mezinárodní zpracování textu tím, že poskytuje pev"
---

UCS2 je 16bitový standard kódování znaků používaný v sítích 3GPP pro SMS a signalizaci, který poskytuje pevné dvoubajtové vyjádření pro každý znak, aby podporoval mezinárodní zpracování textu.

## Popis

UCS2, Universal two byte coded Character Set (univerzální znaková sada s dvoubajtovým kódováním), je základní schéma kódování znaků standardizované v rámci 3GPP. Vychází z univerzální znakové sady [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) 10646 ([UCS](/mobilnisite/slovnik/ucs/)) a používá pevné 16bitové (dvoubajtové) vyjádření pro každý znak. Toto kódování se přímo mapuje na základní vícejazyčnou rovinu (BMP) standardu Unicode, pokrývající kódové body od U+0000 do U+FFFF. V architektuře 3GPP se UCS2 primárně používá v Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) a pro služby zasílání zpráv, jako je Short Message Service ([SMS](/mobilnisite/slovnik/sms/)), aby bylo zajištěno, že textová data jsou přenášena v konzistentním, univerzálně interpretovatelném formátu mezi různými síťovými prvky a uživatelskými zařízeními od různých výrobců.

Technicky UCS2 funguje tak, že každému znaku přiřadí jedinečnou 16bitovou kódovou jednotku. To je v protikladu k kódováním s proměnnou délkou, jako je [UTF-8](/mobilnisite/slovnik/utf-8/). Když zařízení nebo síťový prvek potřebuje odeslat text, převede řetězec na sekvenci těchto 16bitových hodnot. Pro SMS je toto kódování specifikováno v poli TP-User-Data, což umožňuje, aby zprávy obsahovaly znaky z různých jazyků, jako je arabština, čínština, řečtina nebo cyrilice, za předpokladu, že všechny znaky spadají do BMP. Kódování je zpracováváno protokolovými vrstvami odpovědnými za adaptaci uživatelských dat a konstrukci signalizačních zpráv.

Jeho role v síti je klíčová pro interoperabilitu a globální roaming. Síťové uzly jádra, jako jsou [MSC](/mobilnisite/slovnik/msc/), [SGSN](/mobilnisite/slovnik/sgsn/) a HSS, stejně jako samotné UE, se musí shodnout na reprezentaci znaků, aby správně zobrazily jména účastníků, obsah SMS a další řetězce související se službami. UCS2 poskytuje tento společný jazyk. Nepodporuje však znaky mimo BMP (jako některé emotikony nebo historická písma), což vedlo k přijetí UTF-16 v pozdějších vydáních. Kódování je specifikováno v řadě technických specifikací 3GPP (TS), které upravují slovník, služby a bezpečné aplikace.

## K čemu slouží

UCS2 byl zaveden, aby vyřešil problém nekonzistentního a omezeného kódování znaků v raných systémech mobilní telekomunikace. Před jeho standardizací sítě často používaly proprietární nebo regionální 7bitová či 8bitová kódování (jako výchozí 7bitovou abecedu GSM), což výrazně omezovalo rozsah reprezentovatelných znaků a bránilo globální interoperabilitě. Růst mezinárodního roamingu a poptávka po vícejazyčných službách si vyžádaly jednotnou, rozsáhlou znakovou sadu.

Hlavní motivací bylo umožnit mobilním službám, zejména SMS, podporovat prakticky jakýkoli psaný jazyk používaný na celém světě, a tím učinit sítě GSM a UMTS skutečně globálními. Přijetím 16bitového kódování sladěného se standardem Unicode zajistilo 3GPP, že textová data mohou být vyměňována mezi libovolnými kompatibilními zařízeními a sítěmi bez poškození nebo ztráty významu. Toto byl základní krok pro personalizaci služeb, mezinárodní identitu účastníka a rozvoj hodnotově přidaných služeb závislých na textu.

## Klíčové vlastnosti

- Pevné 16bitové kódování pro každý znak
- Přímé sladění se základní vícejazyčnou rovinou (BMP) standardu Unicode
- Zásadní pro SMS (pole TP-User-Data) a signalizaci v řídicí rovině
- Umožňuje konzistentní vícejazyčnou reprezentaci textu
- Základ pro globální interoperabilitu a roaming
- Specifikováno v klíčových specifikacích služeb a slovníku

## Související pojmy

- [UTF-16 – Unicode Transformation Format - 16-bit](/mobilnisite/slovnik/utf-16/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.042** (Rel-19) — Network Identity and Timezone (NITZ)
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification

---

📖 **Anglický originál a plná specifikace:** [UCS2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/ucs2/)
