---
slug: "sip-uri"
url: "/mobilnisite/slovnik/sip-uri/"
type: "slovnik"
title: "SIP-URI – SIP Uniform Resource Identifier"
date: 2025-01-01
abbr: "SIP-URI"
fullName: "SIP Uniform Resource Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sip-uri/"
summary: "SIP-URI je standardizovaný formát adresy, založený na obecné syntaxi URI, používaný k identifikaci komunikačního prostředku v síti založené na protokolu SIP, jako je IMS. Jednoznačně identifikuje uživ"
---

SIP-URI je standardizovaný formát adresy používaný k jednoznačné identifikaci uživatele, služby nebo aplikace pro zahájení multimediálních relací v síti založené na protokolu SIP, jako je IMS.

## Popis

[SIP](/mobilnisite/slovnik/sip/) Uniform Resource Identifier ([URI](/mobilnisite/slovnik/uri/)) je základní adresovací schéma používané v sítích využívajících protokol Session Initiation Protocol (SIP), včetně 3GPP IP Multimedia Subsystem (IMS). Definováno syntakticky v [RFC](/mobilnisite/slovnik/rfc/) 3261 a profilováno ve specifikacích 3GPP, sleduje standardní formát URI: `sip:user@domain`. Část 'user' může být telefonní číslo (v takovém případě je často formátováno jako 'tel-URI' nebo jako numerická uživatelská část) nebo alfanumerický identifikátor (jako 'jan.novak'), zatímco část 'domain' určuje hostitele nebo doménu zodpovědnou za směrování požadavku, například síť operátora (`operator.com`) nebo konkrétní proxy server. SIP-URI může také obsahovat parametry (oddělené středníky) pro předání dodatečných informací o relaci, jako je transportní protokol (`;transport=tcp`), a hlavičky (uvozené `?`) pro předání konkrétních polí SIP hlaviček proxy serveru.

V architektuře 3GPP IMS je SIP-URI primární veřejnou uživatelskou identitou účastníka. Při registraci uživatele v IMS se registruje jedna nebo více SIP-URI (a případně tel-URI) v síti. Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) používá tuto URI k identifikaci uživatele a aplikaci příslušné servisní logiky. Při uskutečnění hovoru vycházející User Equipment (UE) nebo Application Server vyplní Request-URI a pole To hlavičky SIP INVITE SIP-URI zamýšleného příjemce. Směrovací mechanismus IMS, včetně Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)) a S-CSCF, poté používá [DNS](/mobilnisite/slovnik/dns/) procedury (jako záznamy [NAPTR](/mobilnisite/slovnik/naptr/) a SRV) k překladu doménové části URI na příslušný SIP server v domovské síti příjemce za účelem doručení požadavku.

SIP-URI je více než jen adresa; je klíčovým prvkem při identifikaci účastníka, autentizaci a spouštění služeb. Je uložena v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako součást profilu uživatele. URI může být také použita ve spojení s mechanismy ochrany soukromí a službami prokazované identity. Dále, pro interoperabilitu s ne-IMS SIP sítěmi nebo internetem, poskytuje SIP-URI globálně směrovatelný, standardizovaný formát, který umožňuje bezproblémovou komunikaci přes administrativní hranice. Její flexibilita umožňuje reprezentovat nejen koncové uživatele, ale také služby (např. `sip:konference@sluzba.priklad.cz`) a aplikace, čímž tvoří základní kámen správy a směrování relací založených na SIP.

## K čemu slouží

SIP-URI bylo vytvořeno, aby poskytlo univerzální, flexibilní a textově založené adresovací schéma pro SIP relace, které řeší problém, jak jednoznačně identifikovat komunikační koncové body v IP multimediálním světě. Před SIP a jeho URI používala telefonie výhradně čísla E.164, která jsou vázána na konkrétní geografickou nebo servisní hierarchii a nejsou nativně kompatibilní s internetovým hostitelským směrováním. Vývoj SIP jako protokolu pro zahajování interaktivních relací vyžadoval formát adresy, který by se mohl integrovat s internetovou infrastrukturou (jako je DNS), podporoval uživatelsky přívětivé aliasy a fungoval vedle tradičních telefonních čísel.

Motivace vycházela z vize konvergovaných komunikací, kde by bylo možné uživatele kontaktovat pomocí adresy podobné e-mailu (`sip:alice@priklad.cz`) i telefonního čísla. Standard SIP-URI, stanovený v IETF RFC 2543 a později upřesněný v RFC 3261, tuto schopnost poskytl. 3GPP přijalo a profilovalo SIP-URI pro IMS počínaje Release 5, aby sloužilo jako základní identita účastníka, což umožnilo IMS být skutečným systémem založeným na internetových protokolech. Vyřešilo omezení identifikátorů z okruhově přepínaných sítí tím, že umožnilo dynamické přiřazení uživatelů, snadnou integraci s e-mailovými a webovými službami a umožnilo pokročilé služby přítomnosti a zasílání zpráv, které spoléhají na trvalou, osobní online identitu namísto čísla vázaného na zařízení.

## Klíčové vlastnosti

- Standardizovaný textový formát: `sip:[userinfo]@hostport[;parameters][?headers]`
- Podporuje jak numerické (telefonní číslo), tak alfanumerické uživatelské části pro flexibilní adresování
- Umožňuje směrování SIP požadavků založené na DNS prostřednictvím překladu doménové části
- Může nést parametry specifické pro relaci (např. `;user=phone`, `;transport`) pro ovlivnění signalizačního chování
- Slouží jako primární veřejná uživatelská identita (Public User Identity) v 3GPP IMS pro registraci, autentizaci a vyvolání služeb
- Globálně jednoznačné a směrovatelné přes různé domény SIP/IMS sítí a internet

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [SIP-URI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sip-uri/)
