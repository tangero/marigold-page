---
slug: "o-as"
url: "/mobilnisite/slovnik/o-as/"
type: "slovnik"
title: "O-AS – Originating Application Server"
date: 2025-01-01
abbr: "O-AS"
fullName: "Originating Application Server"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/o-as/"
summary: "Aplikační server (AS) v IP multimediální podsystému (IMS), který zpracovává řízení relací a aplikační logiku pro volající stranu (originátor) v multimediální relaci. Je klíčovou funkční entitou pro po"
---

O-AS je aplikační server v IP multimediální podsystému (IMS), který zpracovává řízení relací a aplikační logiku pro volající stranu v multimediální relaci.

## Popis

Originating Application Server (O-AS) je klíčová komponenta v architektuře IP multimediálního podsystému (IMS) dle 3GPP, definovaná v kontextu rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)). Je to aplikační server, který je vyvolán funkcí Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) pro volajícího uživatele (stranu iniciující relaci, jako je hovor nebo služba zasílání zpráv). Když uživatel zahájí IMS relaci, S-CSCF vyhodnotí jeho počáteční filtrační kritéria (iFC), která jsou součástí profilu služeb uživatele staženého z Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Pokud jsou podmínky iFC splněny (např. na základě volaného čísla, typu služby nebo denní doby), S-CSCF přepošle [SIP](/mobilnisite/slovnik/sip/) požadavek (např. INVITE, MESSAGE) na určený O-AS přes rozhraní ISC pomocí protokolu SIP.

Architektonicky je O-AS SIP aplikační server, který hostuje a provádí aplikační logiku. Po přijetí SIP požadavku může fungovat v několika režimech: jako koncový [UA](/mobilnisite/slovnik/ua/) (User Agent), přesměrovací server, SIP proxy nebo back-to-back user agent ([B2BUA](/mobilnisite/slovnik/b2bua/)). Ve své nejběžnější roli funguje jako B2BUA, což mu umožňuje upravit SIP dialog, vložit nové hlavičky, změnit Request-URI nebo komunikovat s dalšími síťovými prostředky (jako je [MRF](/mobilnisite/slovnik/mrf/) pro zpracování médií nebo HSS pro data). Po aplikaci své aplikační logiky – která může zahrnovat překlad čísel, kontrolu volání, uplatnění obchodních pravidel nebo interakci s externí aplikační platformou – O-AS vrátí SIP požadavek zpět S-CSCF pro další směrování, typicky k cílové síti nebo k Terminating [AS](/mobilnisite/slovnik/as/).

Jeho role je klíčová pro poskytování služeb na straně volajícího v oddělené, na službě nezávislé síti. Odděluje základní řízení relace (zpracovávané CSCF) od aplikační logiky. To umožňuje síťovým operátorům a poskytovatelům třetích stran rychle nasazovat a upravovat služby bez dopadu na základní IMS jádro. O-AS spolu se svým protějškem Terminating Application Server (T-AS) umožňují personalizované služby založené na profilu účastníka. Je základní entitou pro implementaci služeb jako je blokování odchozích hovorů (Originating Call Barring), bezpodmínečné přesměrování hovoru (pokud je vyvoláno při odchozím hovoru), identifikace nežádoucí komunikace, odposlech na straně volajícího dle zákona a různé interaktivní hlasové služby před spojením.

## K čemu slouží

Koncept O-AS byl vytvořen jako součást architektury IMS k vyřešení problému monolitického, těsně integrovaného přepínání služeb v tradičních telefonních sítích (jako IN/CAMEL). V před-IMS sítích byla aplikační logika často vestavěna přímo do ústředen pro řízení hovorů (MSC), což zavedení nových služeb zpomalovalo, zdražovalo a uzamykalo k dodavateli. Paradigma IMS, inspirované internetovými protokoly, si kladlo za cíl vytvořit horizontální architekturu, kde by společná vrstva řízení relací (CSCF) mohla spolupracovat s širokou škálou aplikačních serverů přes standardizovaná rozhraní.

Primárním účelem O-AS je poskytnout standardizovaný, na SIP založený integrační bod pro jakoukoli službu, která potřebuje zpracovat nebo ovlivnit relaci při jejím vzniku. Tím se řeší potřeba inovací služeb a interoperability mezi více dodavateli. Definováním jasných spouštěcích bodů (pomocí iFC) a standardního rozhraní ISC umožnilo 3GPP síťovým operátorům kombinovat aplikační servery od různých dodavatelů a vytvářet řetězce služeb. O-AS zpracovává aplikační logiku pro 'odchozí větev' (originating leg), což umožňuje uživatelsky specifické zpracování odchozích relací ještě předtím, než opustí domovskou síť.

Historicky jeho zavedení v 3GPP Release 7 spolu s úplnou specifikací IMS znamenalo posun k plně IP poskytování služeb pro multimediální služby. Bylo motivováno snahou podporovat pokročilé komunikační služby (RCS), VoIP a videotelefonii přes paketové sítě se stejnou spolehlivostí a bohatostí funkcí jako v okruhově spínaných sítích. O-AS poskytuje mechanismus pro replikaci a vylepšení klasických doplňkových telefonních služeb (jako je blokování hovorů) a pro zavádění zcela nových služeb založených na IP, naplňující tak slib IMS o konvergenci mezi buněčnými, pevnými a internetovými službami.

## Klíčové vlastnosti

- Je vyvolán S-CSCF na základě počátečních filtračních kritérií (iFC) volajícího uživatele
- Komunikuje se S-CSCF přes standardizované rozhraní ISC pomocí SIP
- Může fungovat jako Back-to-Back User Agent (B2BUA), proxy, přesměrovací server nebo UA
- Provádí aplikační logiku pro volající stranu (např. kontrolu volání, překlad čísel)
- Může komunikovat s dalšími IMS entitami (HSS, MRF) a externími aplikačními platformami
- Umožňuje vytváření řetězců služeb vrácením kontroly S-CSCF pro další zpracování

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)

## Definující specifikace

- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- **TS 24.628** (Rel-19) — Common Basic Communication Procedures in IMS

---

📖 **Anglický originál a plná specifikace:** [O-AS na 3GPP Explorer](https://3gpp-explorer.com/glossary/o-as/)
