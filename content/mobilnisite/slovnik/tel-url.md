---
slug: "tel-url"
url: "/mobilnisite/slovnik/tel-url/"
type: "slovnik"
title: "TEL-URL – Telephone Uniform Resource Locator"
date: 2025-01-01
abbr: "TEL-URL"
fullName: "Telephone Uniform Resource Locator"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tel-url/"
summary: "Schéma URI pro identifikaci telefonních čísel, standardizované jako 'tel:' v 3GPP. Poskytuje jednotný způsob kódování a adresování telefonních čísel v rámci síťových protokolů a služeb, což umožňuje k"
---

TEL-URL je standardizované schéma URI 'tel:' pro jednotné kódování telefonních čísel, které umožňuje konzistentní směrování hovorů a vyvolávání služeb napříč síťovými protokoly a systémy.

## Popis

Telephone Uniform Resource Locator (TEL-URL) je schéma Uniform Resource Identifier ([URI](/mobilnisite/slovnik/uri/)) definované [IETF](/mobilnisite/slovnik/ietf/) a přijaté ve specifikacích 3GPP, primárně pro použití v IP Multimedia Subsystem (IMS) a dalších telekomunikačních službách. Jeho syntaxe sleduje vzor 'tel:[telephone-subscriber]', kde část telephone-subscriber může být globální číslo (např. +1-555-123-4567) nebo místní číslo, volitelně včetně vizuálních oddělovačů jako pomlčky nebo závorky pro lepší čitelnost, které jsou však během zpracování typicky odstraněny. Schéma podporuje další parametry pro rozšíření, jako je 'phone-context' pro definici místního číslovacího plánu a 'isub' pro [ISDN](/mobilnisite/slovnik/isdn/) subadresu, což mu umožňuje reprezentovat široké spektrum scénářů telefonního adresování přesahující jednoduchá čísla E.164.

V rámci architektury 3GPP je TEL-URL základním identifikátorem používaným v signalizačních protokolech, nejvýznamněji v Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) používaném IMS. Když uživatel zahájí hlasový nebo video hovor, může zpráva SIP INVITE obsahovat Request-URI formátovanou jako TEL-URL, která specifikuje telefonní číslo cíle. Toto URI je pak používáno Call Session Control Functions (CSCFs) a dalšími síťovými prvky k provedení normalizace čísla, rozhodnutí o směrování a spouštění služeb. Například Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) může porovnat TEL-URL s iFC (initial Filter Criteria) pro vyvolání konkrétních aplikačních serverů, což umožňuje služby jako překlad čísel, přesměrování hovorů nebo integrace s legacy okruhově přepínanými sítěmi přes [MGCF](/mobilnisite/slovnik/mgcf/) (Media Gateway Control Function).

Jeho role přesahuje základní sestavení hovoru k prezence službám, zasílání zpráv a doplňkovým službám. V prezence může odběratel (watcher) použít TEL-URL k identifikaci entity, jejíž stav je sledován (presentity). Při zasílání zpráv může být použita jako adresa pro [SMS](/mobilnisite/slovnik/sms/) přes IP nebo multimediální zprávy. Návrh TEL-URL zajišťuje interoperabilitu mezi IP službami a tradičními telefonními sítěmi tím, že poskytuje jasné, standardizované mapování mezi telefonními čísly a adresováním založeným na URI, což je klíčové pro konvergenci pevných, mobilních a VoIP služeb. Jeho specifikace v 3GPP TS 23.271 (Functional stage 2 description of [LCS](/mobilnisite/slovnik/lcs/)) také zdůrazňuje jeho použití v Location Services, kde může identifikovat cíl pro požadavky na polohu.

## K čemu slouží

TEL-URL byl vytvořen, aby řešil potřebu standardizované, jednotné metody pro reprezentaci telefonních čísel v kontextu internetových protokolů a sítí nové generace. Před jeho přijetím byla telefonní čísla často zpracovávána ad-hoc způsobem v různých aplikacích a protokolech, což vedlo k problémům s interoperabilitou, zejména když se sítě vyvíjely směrem k architekturám typu all-IP, jako je IMS. Schéma URI 'tel:' poskytuje konzistentní syntaxi, která odděluje logické telefonní číslo od fyzické sítě nebo služby, a umožňuje tak bezproblémovou integraci mezi okruhově přepínanou telekomunikací a paketově přepínanými službami.

Jeho zavedení bylo motivováno konvergencí telekomunikací a internetu, kde tradiční číslování E.164 potřebovalo být začleněno do IP signalizačních rámců, jako je SIP. Bez standardu jako TEL-URL by vkládání telefonních čísel do SIP zpráv bylo nejednoznačné, což by komplikovalo směrování, vyvolávání služeb a přenositelnost čísel. Definováním jasného schématu URI 3GPP zajistilo, že telefonní čísla mohou být nativně podporována v IMS a dalších službách zaměřených na IP, což usnadňuje funkce jako VoIP hovory, jednotné zasílání zpráv a ENUM (Telephone Number Mapping) dotazy, které překládají TEL-URL na SIP URI nebo jiné záznamy.

Dále TEL-URL řeší problém reprezentace místních čísel a privátních číslovacích plánů v globálním kontextu. Parametr 'phone-context' umožňuje správnou interpretaci čísla v rámci konkrétní domény nebo geografické oblasti, což je klíčové pro podnikové sítě nebo národní číslovací plány, které nepoužívají plný mezinárodní formát. Tato flexibilita podporuje migraci ze starších systémů a umožňuje pokročilé služby, které spoléhají na přesnou identifikaci čísla, jako je zákonné odposlouchávání, nouzové volání (např. mapování na PSAP) a přizpůsobené směrování hovorů založené na analýze čísla, čímž budoucně zajišťuje adresování telekomunikací ve vyvíjejících se sítích.

## Klíčové vlastnosti

- Standardizované schéma URI ('tel:') pro reprezentaci telefonních čísel
- Podporuje globální čísla E.164 (např. +[kód země][číslo účastníka])
- Umožňuje místní čísla s parametrem 'phone-context' pro kontext číslovacího plánu
- Obsahuje volitelnou ISDN subadresu ('isub') pro dodatečné adresovací informace
- Umožňuje interoperabilitu mezi IP signalizací (např. SIP) a legacy telefonními sítěmi
- Používá se pro směrování, spouštění služeb a identifikaci v IMS a dalších službách 3GPP

## Související pojmy

- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [TEL-URL na 3GPP Explorer](https://3gpp-explorer.com/glossary/tel-url/)
