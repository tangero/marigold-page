---
slug: "tel"
url: "/mobilnisite/slovnik/tel/"
type: "slovnik"
title: "TEL – URI TELephone numbers Uniform Resource Identifier"
date: 2025-01-01
abbr: "TEL"
fullName: "URI TELephone numbers Uniform Resource Identifier"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tel/"
summary: "Schéma URI ('tel:') definované IETF (RFC 3966) a profilované 3GPP pro reprezentaci telefonních čísel. Umožňuje jednotnou identifikaci a vytáčení telefonních čísel v rámci IP služeb a aplikací, jako js"
---

TEL je schéma URI, definované IETF a profilované 3GPP, které používá prefix "tel:" pro jednotnou identifikaci a vytáčení telefonních čísel v rámci IP služeb, jako je IMS.

## Popis

TEL [URI](/mobilnisite/slovnik/uri/) je schéma Uniform Resource Identifier speciálně navržené pro reprezentaci telefonních čísel. Jeho syntax je definována [IETF](/mobilnisite/slovnik/ietf/) v [RFC](/mobilnisite/slovnik/rfc/) 3966 a je profilována a používána v řadě specifikací 3GPP, zejména těch souvisejících s IP Multimedia Subsystem (IMS) a rozšířenými komunikačními službami. TEL URI začíná schématem 'tel:' následovaným telefonním číslem, které může být globální číslo (např. tel:+1-555-123-4567) nebo lokální číslo s kontextem (např. tel:4567;phone-context=example.com). Prefix '+' označuje, že číslo je globálně jednoznačné podle mezinárodního číslovacího plánu E.164. URI může také obsahovat parametry pro přípony, isdn-subaddress nebo služebně specifické kontexty.

V architektuře 3GPP hraje TEL URI klíčovou roli v směrování a identifikaci. V IMS může být veřejná uživatelská identita ([IMPU](/mobilnisite/slovnik/impu/)) uživatele [SIP](/mobilnisite/slovnik/sip/) URI (např. sip:user@example.com) nebo TEL URI (např. tel:+441234567890). To umožňuje použití tradičních telefonních čísel nativně v rámci SIP-based IMS ekosystému. Když je volání uskutečněno na TEL URI, síť IMS provede normalizaci čísla a použije [ENUM](/mobilnisite/slovnik/enum/) (E.164 Number Mapping) nebo jiné směrovací databáze k přeložení telefonního čísla na směrovatelné SIP URI (pokud je cílový účastník účastníkem IMS) nebo k přechodu do okruhově přepínané sítě přes Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)).

TEL URI je také rozsáhle používáno v službách zasílání zpráv (např. [SMS](/mobilnisite/slovnik/sms/) over IP, MMS), službách presence a v datech doplňkových služeb (definovaných např. ve specifikaci 24.380 pro konfiguraci UE). Poskytuje standardizovaný způsob, jak mohou aplikace odkazovat na telefonní číslo, což zajišťuje interoperabilitu mezi webovými službami, e-mailovými klienty, kontaktními aplikacemi a síťovými elementy. Jeho definice zahrnuje pravidla pro vizuální formátování a porovnávání (např. odstranění vizuálních separátorů jako pomlček a mezer pro kanonické porovnání), což je klíčové pro funkce jako click-to-dial a porovnávání kontaktních seznamů.

## K čemu slouží

TEL URI bylo vytvořeno, aby překlenulo propast mezi tradičním světem telefonního číslování (E.164) a URI-based adresními schématy internetu. Před jeho přijetím bylo reprezentování telefonního čísla v IP kontextu ad-hoc, často s použitím nestandardních odkazů 'callto:' nebo prostým zobrazením čísla jako textu, který aplikace nemohly spolehlivě interpretovat pro účely vytáčení. Schéma URI 'tel:' poskytuje standardizovaný, strojově čitelný formát, který umožňuje uživatelským agentům (jako webovým prohlížečům nebo e-mailovým klientům) jednoznačně identifikovat řetězec textu jako telefonní číslo a nabídnout příslušné akce (např. iniciovat hlasové volání přes VoIP nebo nativní vytáčení).

Profilace TEL URI ze strany 3GPP byla motivována konvergencí okruhově přepínané telefonie a paketově přepínaných IP služeb v sítích jako IMS. Řeší problém správy identit pro uživatele, kteří se primárně identifikují telefonním číslem. Tím, že TEL URI může být plnohodnotnou veřejnou uživatelskou identitou v IMS, mohou účastníci používat své stávající mobilní číslo pro služby VoIP, videohovorů a zasílání zpráv nové generace, aniž by potřebovali email-like SIP adresu. To bylo klíčové pro přijetí uživateli a interoperabilitu služeb, umožňující bezproblémové směrování mezi legacy sítěmi PSTN/PLMN a doménami IMS. Řeší omezení spočívající v existenci oddělených, nekompatibilních adresních schémat pro telefonii a internet.

## Klíčové vlastnosti

- Schéma URI 'tel:' pro identifikaci telefonních čísel
- Podporuje globální čísla E.164 (s '+') a lokální čísla s kontextem
- Používáno jako veřejná uživatelská identita (Public User Identity) v IMS vedle SIP URI
- Umožňuje směrování mezi IMS a okruhově přepínanými sítěmi přes ENUM
- Standardizovaná syntaxe pro parametry (např. isdn-subaddress, přípona)
- Poskytuje pravidla pro kanonické porovnání čísel (number matching)

## Související pojmy

- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.126** (Rel-19) — Lawful Interception Requirements

---

📖 **Anglický originál a plná specifikace:** [TEL na 3GPP Explorer](https://3gpp-explorer.com/glossary/tel/)
