---
slug: "mmsna"
url: "/mobilnisite/slovnik/mmsna/"
type: "slovnik"
title: "MMSNA – Multimedia Messaging Service Network Architecture"
date: 2025-01-01
abbr: "MMSNA"
fullName: "Multimedia Messaging Service Network Architecture"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmsna/"
summary: "MMSNA je standardizovaný rámec 3GPP, který definuje síťovou architekturu pro službu multimediálních zpráv (Multimedia Messaging Service, MMS). Specifikuje funkční entity, rozhraní a toky zpráv pro umo"
---

MMSNA je standardizovaný rámec 3GPP, který definuje síťovou architekturu, funkční entity, rozhraní a toky zpráv pro službu multimediálních zpráv (Multimedia Messaging Service) za účelem umožnění výměny obsahu s bohatým obsahem mezi uživateli.

## Popis

Multimedia Messaging Service Network Architecture (MMSNA) je komplexní rámec definovaný 3GPP, který popisuje kompletní systém pro poskytování služby multimediálních zpráv ([MMS](/mobilnisite/slovnik/mms/)). Podrobně popisuje logické uspořádání síťových prvků, jejich odpovědnosti a standardizované protokoly používané pro komunikaci mezi nimi. Architektura je navržena jako flexibilní, podporující různé scénáře nasazení včetně integrace se staršími systémy a umožňující služby s přidanou hodnotou od poskytovatelů třetích stran.

Jádro MMSNA tvoří klíčové funkční entity, jako je MMS User Agent (MMS UA) v uživatelském zařízení, MMS Relay/Server (MMS-R/S), který funguje jako centrální uzel pro ukládání a přeposílání zpráv, a externí servery jako MMS Value-Added Service Application (MMS VAS Application). Architektura také definuje rozhraní, jako je MM1 mezi MMS UA a MMS-R/S, MM3 mezi MMS-R/S a externími systémy zasílání zpráv (např. SMTP pro e-mail), MM4 pro komunikaci mezi MMS-R/S různých operátorů, MM5 pro interakce s [HLR](/mobilnisite/slovnik/hlr/) nebo [HSS](/mobilnisite/slovnik/hss/) pro data účastníků a MM7 pro aplikace služeb s přidanou hodnotou. Tato rozhraní používají protokoly jako WAP, [HTTP](/mobilnisite/slovnik/http/) a SMTP pro přenos zpráv a s nimi spojených řídicích informací.

MSS-R/S je hlavním pracovním prvkem architektury a vykonává kritické funkce jako podání zprávy, její načtení, oznámení a doručení. Zpracovává překlad adres, generování údajů pro účtování a adaptaci mezi různými transportními protokoly. Architektura podporuje provoz typu store-and-forward (ulož a přepošli), což umožňuje doručení zpráv i v případě, kdy je příjemce dočasně nedostupný. Do návrhu architektury jsou také integrovány bezpečnostní aspekty, jako je autentizace uživatele a ochrana soukromí zpráv. Úlohou MMSNA je poskytnout vzorový plán, který zajišťuje, že jakákoli kompatibilní implementace MMS může úspěšně vyměňovat multimediální zprávy v prostředí s více dodavateli a operátory, a tvoří tak páteř komerčních služeb MMS nasazených po celém světě.

## K čemu slouží

MMSNA byla vytvořena za účelem standardizace síťové infrastruktury pro službu multimediálních zpráv (Multimedia Messaging Service, [MMS](/mobilnisite/slovnik/mms/)), která byla představena jako vývojový krok nad rámec jednoduchých textových SMS. Před její standardizací by proprietární implementace pro odesílání obrázků, zvuku a videa přes mobilní sítě vedly k fragmentaci a znemožnily by interoperabilitu mezi účastníky různých sítí a výrobci telefonů. Hlavním problémem, který MMSNA řeší, je definice univerzálního architektonického modelu, který zaručuje bezproblémové doručování multimediálních zpráv od konce ke konci napříč různými síťovými infrastrukturami.

Motivace vycházela z komerční potřeby zavést atraktivní službu generující příjmy, která by využívala zlepšující se možnosti telefonů a rychlejší datové sítě ([GPRS](/mobilnisite/slovnik/gprs/), [EDGE](/mobilnisite/slovnik/edge/), UMTS). Standardizovaná architektura byla nezbytná pro urychlení přijetí na trhu, neboť poskytla operátorům, výrobcům zařízení a poskytovatelům obsahu jasný a společný technický základ. Odstranila omezení SMS tím, že umožnila obsah s bohatou strukturou, podpořila doručování typu store-and-forward pro asynchronní komunikaci a poskytla možnosti pro účtování a služby s přidanou hodnotou. Specifikací rozhraní a protokolů MMSNA oddělila vývoj telefonů, síťových serverů a aplikací, což podpořilo konkurenční ekosystém a zároveň zajistilo spolehlivost služby a konzistentní uživatelský zážitek.

## Klíčové vlastnosti

- Definuje funkční entity jako MMS Relay/Server a MMS User Agent
- Specifikuje standardizovaná rozhraní (MM1-MM8) pro interoperabilitu
- Podporuje doručování multimediálního obsahu typu store-and-forward (ulož a přepošli)
- Integruje se s databázemi účastníků (HLR/HSS) pro překlad adres a profilování
- Umožňuje propojení s externími systémy zasílání zpráv (např. e-mail přes SMTP)
- Poskytuje rámec pro aplikace služeb s přidanou hodnotou prostřednictvím rozhraní MM7

## Související pojmy

- [MMS – Multimedia Messaging Service](/mobilnisite/slovnik/mms/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [MMSNA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmsna/)
