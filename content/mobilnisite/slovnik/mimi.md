---
slug: "mimi"
url: "/mobilnisite/slovnik/mimi/"
type: "slovnik"
title: "MIMI – More Instant Messaging Interoperability"
date: 2025-01-01
abbr: "MIMI"
fullName: "More Instant Messaging Interoperability"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mimi/"
summary: "Rámec 3GPP umožňující interoperabilitu mezi různými službami okamžitého zasílání zpráv. Definuje standardizované protokoly a rozhraní, aby uživatelé na různých platformách mohli vyměňovat zprávy, a ře"
---

MIMI je rámec 3GPP, který umožňuje interoperabilitu mezi různými službami okamžitého zasílání zpráv definováním standardizovaných protokolů a rozhraní.

## Popis

More Instant Messaging Interoperability (MIMI) je servisní rámec 3GPP zavedený ve vydání Release 18, který usnadňuje přímou komunikaci mezi uživateli různých proprietárních služeb okamžitého zasílání zpráv ([IM](/mobilnisite/slovnik/im/)). Jeho architektura je založena na federovaném modelu, kde se účastnící poskytovatelé služeb (SP) vzájemně propojují prostřednictvím standardizovaných rozhraní definovaných ve specifikacích 3GPP. Jádro MIMI tvoří MIMI Application Server ([AS](/mobilnisite/slovnik/as/)), který sídlí v síti poskytovatele služeb a funguje jako brána pro interoperabilitu. Tento AS komunikuje s nativním IM systémem poskytovatele a, což je klíčové, s MIMI AS dalších poskytovatelů pomocí protokolů specifikovaných v 3GPP TS 26.143 a souvisejících specifikacích. Rámec definuje základní funkce pro směrování zpráv, mapování identit, zabezpečení a hlášení stavu doručení napříč administrativními doménami.

Z technického pohledu MIMI funguje tak, že mezi poskytovateli služeb vytváří důvěru a standardizované komunikační kanály. Když uživatel ve službě A odešle zprávu uživateli ve službě B, zpráva je nejprve zpracována nativním systémem služby A a poté předána jejímu MIMI AS. MIMI AS provede potřebné převody protokolů, aplikuje end-to-end šifrování podle bezpečnostního modelu rámce a směruje zprávu na MIMI AS příjemce na základě federované identity. MIMI AS příjemce pak zprávu doručí do nativního IM systému služby B pro zobrazení koncovému uživateli. Tento proces zajišťuje, že formát zprávy, zabezpečení a funkce jsou vhodně převedeny mezi dvěma potenciálně odlišnými základními technologiemi.

Klíčovými součástmi architektury MIMI jsou MIMI Application Server, funkce MIMI Gateway Function pro adaptaci protokolů a funkce Identity Management Function pro mapování uživatelských identit mezi různými doménami (např. převod telefonního čísla na identifikátor specifický pro službu). Rámec také specifikuje společnou sadu základních funkcí zasílání zpráv – jako je zasílání zpráv jeden na jednoho a ve skupinách, přenos souborů, potvrzení o přečtení a indikátory psaní – které musí být pro interoperabilitu podporovány. Jeho role v síti je jako nadstavbový služební enabler, který se nachází nad základní konektivitou poskytovanou 5G systémem (5GS) nebo jinými přístupovými sítěmi, využívá síť pro přenos, ale přidává aplikační logiku pro komunikaci mezi službami.

## K čemu slouží

MIMI byl vytvořen k řešení všudypřítomného problému izolovaných ekosystémů zasílání zpráv (silosů), kde jsou uživatelé omezeni na komunikaci pouze s ostatními na stejné proprietární platformě (např. WhatsApp, iMessage, WeChat). Tato fragmentace představuje významný problém uživatelského zážitku a překážku pro univerzální komunikaci. V minulosti byla interoperabilita zkoušena prostřednictvím neoficiálních mostů nebo klientů podporujících více protokolů, ty však byly často neschválené, nezabezpečené a nespolehlivé. MIMI poskytuje standardizovanou, zabezpečenou a na úrovni telekomunikačních operátorů (carrier-grade) alternativu schválenou normalizační organizací.

Motivace vychází z regulatorních tlaků v různých regionech požadujících interoperabilitu dominantních služeb zasílání zpráv za účelem podpory konkurence a volby uživatelů, stejně jako z touhy telekomunikačního průmyslu zůstat relevantní v prostoru zasílání zpráv ovládaném [OTT](/mobilnisite/slovnik/ott/) službami. Předchozí přístupy postrádaly jednotný technický standard, což vedlo k nekonzistentním implementacím a bezpečnostním slabinám. MIMI tyto nedostatky řeší tím, že poskytuje komplexní specifikaci pokrývající celý zásobník interoperability – od identity a zjišťování přes formát zprávy, transport až po end-to-end šifrování – a zajišťuje, že se služby mohou vzájemně propojovat předvídatelným a bezpečným způsobem, přičemž umožňuje poskytovatelům diferencovat se na funkcích ve vlastních ekosystémech.

## Klíčové vlastnosti

- Federovaná architektura umožňující propojení mezi nezávislými poskytovateli služeb
- Standardizovaná sada protokolů (specifikovaná v 3GPP TS 26.143) pro výměnu zpráv mezi MIMI Application Servery
- Rámec pro end-to-end šifrování zajišťující důvěrnost zpráv napříč doménami
- Mechanismy pro mapování identit a jejich zjišťování k překladu uživatelských identifikátorů mezi různými službami
- Podpora základní sady funkcí včetně 1:1 chatu, skupinového zasílání zpráv a oznámení o stavu doručení
- Zpětná kompatibilita a vyjednávání funkcí pro zvládnutí rozdílů v podporovaných schopnostech mezi službami

## Definující specifikace

- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TS 26.854** (Rel-19) — Study on Haptics in 5G Media Services

---

📖 **Anglický originál a plná specifikace:** [MIMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/mimi/)
