---
slug: "poc"
url: "/mobilnisite/slovnik/poc/"
type: "slovnik"
title: "POC – Push To Talk Over Cellular"
date: 2025-01-01
abbr: "POC"
fullName: "Push To Talk Over Cellular"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/poc/"
summary: "POC je služba standardizovaná 3GPP, která umožňuje okamžitou poloduplexní hlasovou komunikaci přes mobilní sítě, podobnou vysílačce. Umožňuje hovory jeden na jednoho nebo skupinové hovory s rychlým na"
---

POC (Push To Talk Over Cellular) je služba standardizovaná 3GPP, která umožňuje okamžitou poloduplexní hlasovou komunikaci podobnou vysílačce (walkie-talkie) přes mobilní sítě pro hovory jeden na jednoho nebo skupinové hovory s rychlým navázáním spojení.

## Popis

Push To Talk Over Cellular (POC) je standardizovaná služba definovaná 3GPP, která využívá architekturu IP Multimedia Subsystem (IMS) k poskytování okamžité hlasové komunikace přes mobilní sítě. Na rozdíl od tradičních plně duplexních mobilních hovorů POC funguje v poloduplexním režimu, kdy může vysílat hlas pouze jeden účastník najednou, obvykle aktivovaný stisknutím tlačítka. Tato služba je navržena pro komunikaci jeden na jednoho a jeden na mnoho (skupinovou), umožňuje rychlé navázání hovoru a efektivní využití síťových zdrojů. Jádro POC je postaveno na IMS, využívá Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) pro řízení relace a Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) pro přenos médií. Mezi klíčové síťové komponenty patří POC server, který spravuje relace, řídí právo k vysílání (floor control – určuje, kdo má právo mluvit) a distribuuje média účastníkům. POC klient je umístěn na uživatelském zařízení (UE) a komunikuje s jádrem IMS prostřednictvím signalizace SIP. POC se integruje se stávající mobilní infrastrukturou, včetně LTE nebo 5G NR pro rádiový přístup a Evolved Packet Core (EPC) nebo 5G Core (5GC) pro IP konektivitu, což zajišťuje její funkčnost napříč různými generacemi sítí. Služba podporuje funkce jako správa skupin, informace o přítomnosti (presence) a okamžité osobní upozornění, což ji činí univerzální pro dynamické komunikační potřeby. Při provozu uživatel zahájí POC relaci výběrem kontaktu nebo skupiny a stisknutím tlačítka pro mluvení; POC klient odešle SIP INVITE na POC server, který uživatele autentizuje a naváže relaci. Právo k vysílání je řízeno pomocí SIP nebo Media Burst Control Protocol ([MBCP](/mobilnisite/slovnik/mbcp/)), přičemž právo vysílat je uděleno vždy pouze jednomu uživateli, zatímco ostatní naslouchají. Média jsou streamována jako IP pakety přes přenosovou síť, přičemž mechanismy kvality služby (QoS) zajišťují nízkou latenci a prioritu pro přenos v reálném čase. POC hraje klíčovou roli v umožnění komunikace pro klíčové mise (mission-critical), zejména pro složky veřejné bezpečnosti, kde je spolehlivá a okamžitá hlasová koordinace zásadní během mimořádných událostí. Služba také podporuje komerční aplikace v odvětvích dopravy, stavebnictví a bezpečnosti, zvyšuje provozní efektivitu prostřednictvím okamžité skupinové komunikace bez zpoždění spojených s vytáčením a vyzváněním u konvenčních hovorů.

## K čemu slouží

POC byla vytvořena, aby uspokojila potřebu okamžité, skupinově orientované hlasové komunikace přes mobilní sítě, čímž překlenula mezeru mezi tradičními obousměrnými rádiovými systémy (jako jsou vysílačky) a moderní mobilní telefonii. Před POC organizace spoléhaly na vyhrazené systémy privátní mobilní rádiové komunikace (PMR), které měly omezené pokrytí, vyžadovaly samostatnou infrastrukturu a postrádaly interoperabilitu s veřejnými sítěmi. Motivací pro standardizaci POC v 3GPP Release 13 bylo využít všudypřítomné mobilní pokrytí (LTE a novější) k poskytnutí škálovatelného, nákladově efektivního řešení, které podporuje komunikaci na široké oblasti bez potřeby specializovaného hardwaru. Řeší problémy, jako jsou pomalé časy navázání hovoru u konvenčních mobilních služeb a neefektivní metody skupinové komunikace, a umožňuje téměř okamžitý přenos hlasu s jednoduchostí stisknutí tlačítka. Historicky existovala proprietární řešení POC, ale trpěla problémy s interoperabilitou a závislostí na dodavateli; standardizace 3GPP zajistila síťově agnostický provoz, což usnadnilo globální přijetí a integraci s IMS pro vylepšené poskytování služeb. POC také reaguje na rostoucí poptávku po komunikaci pro klíčové mise typu push-to-talk ([MCPTT](/mobilnisite/slovnik/mcptt/)) ve veřejné bezpečnosti, jak je definováno v následujících vydáních, a poskytuje funkce jako priorita, přednostní přerušení a zabezpečení, které jsou nezbytné pro záchranáře. Využitím stávající mobilní infrastruktury POC snižuje náklady na nasazení a rozšiřuje dosah komunikace za místní oblasti, podporuje bezproblémový roaming a integraci s dalšími službami založenými na IMS, jako je voice over LTE (VoLTE).

## Klíčové vlastnosti

- Poloduplexní komunikační režim s řízením práva k vysílání (floor control)
- Rychlé navázání relace pomocí IMS a signalizace SIP
- Podpora hovorů jeden na jednoho a jeden na mnoho (skupinových)
- Integrace se sítěmi LTE a 5G pro široké pokrytí
- Prioritizace kvality služby (QoS) pro média s nízkou latencí
- Schopnosti správy přítomnosti (presence) a skupin

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.779** (Rel-13) — MCPTT over LTE Stage 2 Study
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [POC na 3GPP Explorer](https://3gpp-explorer.com/glossary/poc/)
