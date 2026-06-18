---
slug: "rcd"
url: "/mobilnisite/slovnik/rcd/"
type: "slovnik"
title: "RCD – Rich Call Data"
date: 2026-01-01
abbr: "RCD"
fullName: "Rich Call Data"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rcd/"
summary: "Rozšíření služby IP Multimedia Subsystem (IMS), které během hovoru poskytuje doplňková data, jako je kontext volajícího, poloha nebo média. Obohacuje hlasovou a videokomunikaci o další informace a umo"
---

RCD je rozšíření služby IMS standardizované 3GPP, které během hovoru poskytuje doplňková data, jako je kontext volajícího nebo jeho poloha, aby obohatilo hlasovou a videokomunikaci o nové interaktivní funkce.

## Popis

Rich Call Data (RCD) je servisní schopnost standardizovaná v 3GPP Release 17 jako součást vývoje komunikačních služeb v IP Multimedia Subsystem (IMS). Zásadně rozšiřuje tradiční hlasové nebo videohovory tím, že umožňuje výměnu strukturovaných doplňkových dat spolu s hlavním mediálním proudem. Tato data jsou přenášena v rámci signalizace hovoru nebo zpráv během relace, typicky s využitím protokolů jako Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a Session Description Protocol ([SDP](/mobilnisite/slovnik/sdp/)), často zapouzdřených ve formátech jako [JSON](/mobilnisite/slovnik/json/) nebo [XML](/mobilnisite/slovnik/xml/). RCD umožňuje širokou škálu případů užití: například během hovoru se zákaznickým servisem může firma odeslat své logo, název a účel; při tísňových hovorech lze přenášet přesnou polohu a lékařské údaje; nebo v sociálních hovorech mohou uživatelé sdílet svůj stav, fotografii nebo interaktivní tlačítka. Z architektonického hlediska RCD zahrnuje podporu na straně klienta v uživatelském zařízení (UE) a funkce na straně serveru v jádru IMS, včetně aplikačních serverů, které data mohou zpracovávat nebo obohacovat. Výměna dat se řídí servisními profily IMS a řízením politik, aby byla zajištěna bezpečnost, soukromí a interoperabilita. RCD funguje definováním nových SIP metod, hlaviček nebo částí těla pro přenos obohacených dat, které jsou vyjednány během sestavování hovoru nebo vyměněny v jeho průběhu. Využívá stávající mechanismy autentizace a autorizace IMS, čímž zajišťuje, že jsou sdílena pouze autorizovaná data. Služba je navržena zpětně kompatibilně, takže základní hovory fungují i v případě, že jedna strana RCD nepodporuje. Klíčové komponenty zahrnují UE s podporou RCD, prvky jádra IMS (jako [CSCF](/mobilnisite/slovnik/cscf/)) a případně vyhrazené RCD aplikační servery, které poskytují obohacení nebo ukládání dat. Jejím úkolem je transformovat telefonii z jednoduchého audio/video kanálu na bohatou, kontextovou komunikační platformu, která tvoří základ pro budoucí interaktivní služby.

## K čemu slouží

RCD bylo vyvinuto, aby řešilo stagnaci tradičních telefonních služeb tváří v tvář over-the-top ([OTT](/mobilnisite/slovnik/ott/)) komunikačním aplikacím, které nabízejí bohaté funkce, jako je sdílení souborů, označení polohy nebo interaktivní obsah během hovoru. Standardní hlasové a videohovory v IMS, ačkoli kvalitní a spolehlivé, postrádaly standardizovaný mechanismus pro výměnu doplňkových dat, což omezovalo inovace služeb a zapojení uživatelů. Motivací bylo vylepšit nativní zkušenost s voláním v mobilních sítích, aby konkurovala OTT službám, a umožnit nové komerční a tísňové aplikace. Pro firmy RCD řeší problém neosobních interakcí se zákazníky tím, že umožňuje sdílet identitu značky a kontextová data, čímž zlepšuje zákaznickou zkušenost. V tísňových službách řeší kritická omezení, kdy pouze hlasové hovory nemusí přenést dostatek informací, a umožňuje automatický přenos polohy, lékařských údajů nebo fotografií incidentu záchranářům. Historicky předchozí přístupy spoléhaly na proprietární řešení nebo oddělené datové kanály, které nebyly interoperabilní mezi sítěmi a zařízeními. RCD poskytuje univerzální, standardy založený rámec uvnitř IMS, který zajišťuje globální interoperabilitu a bezpečnost. Také připravuje cestu pro integrované komunikační sady, které plynule propojují telefonii s datovými službami, a podporuje regulatorní požadavky na pokročilé tísňové volání (např. NG911).

## Klíčové vlastnosti

- Umožňuje výměnu strukturovaných dat (např. JSON/XML) během IMS hovorů
- Používá rozšíření SIP pro vyjednání a přenos dat během hovoru
- Podporuje případy užití, jako je obohacení identifikace volajícího, tísňová data a interaktivní tlačítka
- Zachovává zpětnou kompatibilitu se staršími hlasovými/videohovory
- Integruje se s autentizací IMS a řízením politik pro zajištění bezpečnosti
- Usnadňuje vylepšení komunikace pro podnikové i spotřebitelské účely

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [URN – Uniform Resource Name](/mobilnisite/slovnik/urn/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.175** (Rel-19) — IMS AS Service-Based Interface Protocol
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.203** (Rel-19) — IMS Security Specification
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2

---

📖 **Anglický originál a plná specifikace:** [RCD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcd/)
