---
slug: "pui"
url: "/mobilnisite/slovnik/pui/"
type: "slovnik"
title: "PUI – Public User Identity"
date: 2026-01-01
abbr: "PUI"
fullName: "Public User Identity"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pui/"
summary: "Globálně směrovatelný identifikátor používaný v IP multimediální podsystému (IMS) k adresování uživatele pro multimediální komunikace, jako je SIP URI nebo TEL URI. Jedná se o externí adresu, kterou o"
---

PUI je globálně směrovatelný identifikátor, například SIP URI nebo TEL URI, používaný v IMS jako externí adresa, na kterou mohou ostatní směrovat požadavky o zahájení multimediálních komunikačních relací k účastníkovi.

## Popis

Veřejná uživatelská identita (Public User Identity – PUI) je základním konceptem v architektuře IP multimediálního podsystému (IMS) 3GPP a slouží jako veřejná kontaktní adresa uživatele. Je to identifikátor, který ostatní uživatelé nebo aplikace používají k zahájení komunikačních relací, jako jsou hovory VoLTE (Voice over LTE), videohovory nebo relace instant messagingu. PUI se liší od privátních identifikátorů a má podobu buď [SIP](/mobilnisite/slovnik/sip/) Uniform Resource Identifier (SIP [URI](/mobilnisite/slovnik/uri/), např. sip:user@domain.com) nebo [TEL](/mobilnisite/slovnik/tel/) URI (např. tel:+1234567890), který odpovídá tradičnímu telefonnímu číslu.

Z architektonického hlediska jsou PUI uloženy v profilu IMS účastníka na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server). K jednomu IMS účastníkovi (reprezentovanému privátní uživatelskou identitou) může být přidruženo více PUI, což umožňuje, aby jedna osoba měla několik kontaktních adres (např. pracovní a osobní číslo). Během registrace v IMS si uživatelské zařízení (UE) zaregistruje přidružené PUI v síti prostřednictvím [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-Call Session Control Function). S-CSCF stáhne z HSS služební profil účastníka včetně seznamu PUI, aby pro tyto identity mohl služby autorizovat a poskytovat.

Při provozu, když je relace zahájena směrem k uživateli, výchozí IMS síť směruje požadavek na základě cílového PUI. [I-CSCF](/mobilnisite/slovnik/i-cscf/) (Interrogating-CSCF) se dotazuje HSS, aby zjistil, který S-CSCF obsluhuje dané PUI, a umožnil tak správné přeposlání požadavku. PUI jsou klíčové pro vyvolání služeb, protože aplikační servery IMS ([AS](/mobilnisite/slovnik/as/)) spouštějí služby na základě volaného nebo volajícího PUI. Používají se také pro prezentaci identity (Caller ID) a jsou klíčovým prvkem v účtovacích mechanismech IMS. Správa PUI, včetně jejich registrace, zrušení registrace a blokování, je nedílnou součástí řízení relací v IMS.

## K čemu slouží

PUI byla vytvořena za účelem vyřešení problému adresování uživatelů v čistě IP, multimédii orientované síti, jako je IMS, která odděluje služby od podkladové přístupové technologie. Před zavedením IMS používala telefonie primárně jako jedinou adresu číslo [MSISDN](/mobilnisite/slovnik/msisdn/) (Mobile Subscriber ISDN Number). To bylo nedostatečné pro bohaté multimediální scénáře a scénáře s více identitami, se kterými se v IMS počítalo, kde by uživatel mohl mít adresy podobné e-mailu (SIP URI) vedle telefonních čísel.

Její vytvoření bylo motivováno potřebou flexibilního schématu adresování, které by bylo v souladu s internetovými standardy a mohlo globálně fungovat přes hranice operátorů. Formát SIP URI, sladěný se standardy IETF, umožňuje bezproblémovou spolupráci s ne-3GPP IP komunikačními službami. PUI poskytuje nezbytnou abstraktní vrstvu, která odděluje veřejnou kontaktní identitu uživatele od jeho privátní identity na úrovni sítě a od fyzického zařízení. Tím řeší problém přenositelnosti služeb a umožňuje pokročilé funkce, jako je současné zvonění více zařízení pod jednou veřejnou identitou, sdílení identity (např. číslo oddělení) a konvergenci telefonie a webových komunikačních paradigmat.

## Klíčové vlastnosti

- Globálně směrovatelná adresa pro multimediální relace v IMS (SIP URI nebo TEL URI)
- Uložena v HSS jako součást profilu IMS účastníka
- Jeden uživatel může mít k jedné privátní identitě přidruženo více PUI
- Používá se pro směrování relací, vyvolávání služeb a účtování v IMS
- Klíčová pro prezentaci volajícího (Caller ID)
- Registrována v síti během procedur registrace v IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP-URI – SIP Uniform Resource Identifier](/mobilnisite/slovnik/sip-uri/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.894** (Rel-11) — IMS Network-Independent Public User Identities Study

---

📖 **Anglický originál a plná specifikace:** [PUI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pui/)
