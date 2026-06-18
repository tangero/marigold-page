---
slug: "imdn"
url: "/mobilnisite/slovnik/imdn/"
type: "slovnik"
title: "IMDN – Instant Message Disposition Notification"
date: 2025-01-01
abbr: "IMDN"
fullName: "Instant Message Disposition Notification"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imdn/"
summary: "Instant Message Disposition Notification (IMDN) je mechanismus specifikovaný 3GPP, který poskytuje hlášení o stavu doručení a přečtení pro IP instant zprávy, podobně jako potvrzení o doručení a přečte"
---

IMDN je mechanismus specifikovaný 3GPP pro IP instant messaging, který odesílatelům poskytuje hlášení o stavu doručení a přečtení zprávy, čímž zlepšuje uživatelský zážitek v rámci architektury IMS.

## Popis

Instant Message Disposition Notification (IMDN) je protokolový mechanismus definovaný v rámci messagingové architektury IMS dle 3GPP (specifikovaný v TS 24.247 a odkazovaný ve specifikacích jako 23.204), který umožňuje hlášení stavu zpracování zprávy. Zpracování (disposition) označuje stav nebo osud doručené instant zprávy na straně příjemce. Primárními stavy jsou 'doručeno' (zpráva dorazila na zařízení nebo službu příjemce) a 'zobrazeno' (zpráva byla prezentována příjemci, tj. přečtena). IMDN funguje jako rozšíření základního messagingového protokolu, kterým je typicky Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) používaný s metodou MESSAGE nebo Message Session Relay Protocol ([MSRP](/mobilnisite/slovnik/msrp/)) pro session-based messaging.

Architektura zahrnuje tři hlavní entity: odesílající uživatelské zařízení (UE) nebo aplikaci, příjemcovo UE/aplikaci a prvky IMS core sítě (jako [CSCF](/mobilnisite/slovnik/cscf/)), které zprávy směrují. Proces je zahájen odesílatelem, který do původní žádosti o instant zprávu zahrne specifické hlavičkové pole (např. 'Disposition-Notification' v SIP MESSAGE), čímž indikuje typy notifikací (doručení, zobrazení), které si přeje obdržet. Když klient příjemce zprávu úspěšně přijme, vygeneruje zpět směrem k odesílateli SIP MESSAGE požadavek. Tato notifikační zpráva obsahuje hlavičku 'Message-ID', která ji koreluje s původní zprávou, a hlavičku 'Disposition' s hodnotou jako 'delivered' nebo 'displayed'. Tato notifikace je směrována přes IMS core stejně jako běžná instant zpráva.

Fungování IMDN zahrnuje pečlivé řízení stavu a zprostředkování sítí. Pro notifikaci 'doručeno' ji typicky generuje terminující IMS uzel příjemce (např. [S-CSCF](/mobilnisite/slovnik/s-cscf/) příjemce nebo Application Server) po úspěšném doručení do domény služby příjemce. Notifikaci 'zobrazeno' explicitně generuje messagingová klientská aplikace příjemce poté, co zprávu zobrazí uživateli. IMS síť může zahrnovat mezilehlé Application Servery (např. messaging [AS](/mobilnisite/slovnik/as/)), které mohou zprávy ukládat a přeposílat, a tyto servery mohou také generovat nebo přeposílat notifikace o stavu. Specifikace definují přesný formát [XML](/mobilnisite/slovnik/xml/) těla (application/imdn+xml), který nese notifikační data včetně původního ID zprávy, adresy příjemce a stavu. Tím je zajištěna interoperabilita mezi klienty a síťovými servery různých dodavatelů. IMDN je klíčovým prvkem pro spolehlivé messagingové služby v ekosystému IMS, který uživatelům poskytuje jistotu podobnou jako v oblíbených internetových messagingových aplikacích.

## K čemu slouží

IMDN byl vytvořen, aby řešil klíčovou mezeru v uživatelském zážitku u raných standardizovaných IP messagingových služeb ve srovnání s nově vznikajícími Over-The-Top ([OTT](/mobilnisite/slovnik/ott/)) messagingovými aplikacemi. Před jeho specifikací poskytoval instant messaging založený na IMS, jak byl definován v dřívějších releasech, pouze základní schopnost 'odeslat a zapomenout' bez jakéhokoli vestavěného mechanismu, aby odesílatel věděl, zda byla zpráva úspěšně přijata nebo viděna. Tento nedostatek zpětné vazby byl významnou nevýhodou oproti internetovým messagingovým aplikacím nabízejícím potvrzení o doručení a přečtení, což činilo IMS messaging méně spolehlivým a atraktivním pro uživatele.

Primární problém, který IMDN řeší, je poskytnutí zpětné vazby odesílateli a zvýšení vnímání spolehlivosti IMS messengingu. Umožňuje odesílatelům vyžádat si a přijímat kladné potvrzení, že jejich komunikační pokus byl na různých stupních úspěšný. To je obzvláště důležité pro potenciálně důležité nebo časově citlivé zprávy. Z pohledu poskytovatele služeb také napomáhá řešení problémů a představuje přidanou funkci, která může být zpoplatněna nebo využita k odlišení jejich messagingové služby od jednoduché [SMS](/mobilnisite/slovnik/sms/). V tomto ohledu přibližuje messaging založený na operátorech funkční paritě s OTT službami.

Historicky bylo jeho zavedení v 3GPP Release 8 součástí širšího úsilí učinit z IMS konkurenceschopnou platformu pro rich communication services. Byl to základní prvek pro pozdější vývoj a standardizaci Rich Communication Services (RCS), jejichž cílem bylo vytvořit globálně interoperabilní messagingovou službu založenou na operátorech s funkcemi přesahujícími SMS. IMDN poskytl standardizovanou 'kostru' pro potvrzení o přečtení, funkci, která se stala charakteristickým znakem moderního messengingu. Odstranil omezení dřívější služby Open Mobile Alliance (OMA) Instant Messaging, které takový standardizovaný notifikační mechanismus chyběl, definováním čistého protokolu založeného na SIP v rámci architektury IMS, což zajišťuje jeho bezproblémovou spolupráci s dalšími IMS službami, jako je hlas a video.

## Klíčové vlastnosti

- Podporuje dva primární typy stavů: 'doručeno' (zpráva dorazila do služby příjemce) a 'zobrazeno' (zprávu uživatel přečetl).
- Používá metodu SIP MESSAGE nebo MSRP se specifickými hlavičkami ('Disposition-Notification', 'Disposition') a XML formátem těla pro notifikace.
- Poskytuje korelaci mezi původní zprávou a notifikací prostřednictvím hlavičky 'Message-ID'.
- Může být vyžádána selektivně odesílatelem (např. pouze potvrzení o doručení, nebo obojí – o doručení i přečtení).
- Funguje v rámci architektury IMS, je směrována přes CSCF a může být zprostředkována Application Servery.
- Definována jako součást messagingového rámce IMS, což zajišťuje interoperabilitu napříč sítěmi a zařízeními.

## Související pojmy

- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [RCS – Return Channel via Satellite](/mobilnisite/slovnik/rcs/)
- [CPM – Collective Perception Message](/mobilnisite/slovnik/cpm/)
- [MSRP – Multiple Stream Registration Protocol](/mobilnisite/slovnik/msrp/)

## Definující specifikace

- **TS 23.204** (Rel-19) — SMS over generic IP access; Stage 2
- **TS 23.824** (Rel-10) — IP-SM-GW enhancements for CPM-SMS Interworking
- **TS 29.311** (Rel-19) — Service Level Interworking for Messaging

---

📖 **Anglický originál a plná specifikace:** [IMDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/imdn/)
