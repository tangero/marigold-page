---
slug: "3pcc"
url: "/mobilnisite/slovnik/3pcc/"
type: "slovnik"
title: "3PCC – Third Party Call Control"
date: 2026-01-01
abbr: "3PCC"
fullName: "Third Party Call Control"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3pcc/"
summary: "Servisní schopnost, která umožňuje aplikačnímu serveru třetí strany navazovat, spravovat a ukončovat multimediální relace mezi dvěma nebo více koncovými body. Umožňuje síťovým operátorům a poskytovate"
---

3PCC je servisní schopnost, která umožňuje aplikačnímu serveru třetí strany navazovat, spravovat a ukončovat multimediální relace mezi dvěma nebo více koncovými body.

## Popis

Third Party Call Control (3PCC) je standardizovaná servisní architektura definovaná v 3GPP, která umožňuje aplikačnímu serveru ([AS](/mobilnisite/slovnik/as/)) fungovat jako řídicí entita pro navazování a správu multimediálních relací mezi koncovými body uživatelů. AS funguje jako back-to-back uživatelský agent ([B2BUA](/mobilnisite/slovnik/b2bua/)) neboli řídicí jednotka hovoru třetí strany, která iniciuje samostatná [SIP](/mobilnisite/slovnik/sip/) dialogová spojení s každým účastnícím se koncovým bodem a koordinuje parametry relace a toky médií mezi nimi. Tato architektura umožňuje AS udržovat plnou kontrolu nad životním cyklem relace, včetně jejího navázání, změny a ukončení, aniž by koncové body potřebovaly přímou signalizační konektivitu mezi sebou.

Architektura 3PCC využívá jako primární signalizační protokol SIP (Session Initiation Protocol), přičemž aplikační server implementuje funkci 3PCC kontroléru. Při navazování relace AS nejprve iniciuje SIP INVITE k jednomu koncovému bodu (volající strana) s nabídkou [SDP](/mobilnisite/slovnik/sdp/) popisující požadované charakteristiky média. Po přijetí odpovědi od tohoto koncového bodu pak AS iniciuje samostatné SIP INVITE k druhému koncovému bodu (volaná strana), přičemž jako nabídku pro druhý koncový bod použije SDP odpověď od prvního koncového bodu. Tím vzniknou dvě nezávislá SIP dialogová spojení, která AS na signalizační úrovni propojí, což mu umožňuje řídit vyjednávání médií a parametry relace pro obě strany.

Klíčovými komponentami architektury 3PCC jsou aplikační server 3PCC, který implementuje logiku řízení hovoru; Serving Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v jádru sítě IMS, která směruje SIP zprávy mezi koncovými body a AS; a koncové body uživatelských zařízení (UE), které se účastní řízených relací. AS udržuje samostatná SIP dialogová spojení s každým koncovým bodem a může nezávisle měnit parametry relace, což umožňuje funkce jako přesměrování hovoru, čekání hovoru nebo konferenční propojení. AS také v případě potřeby zajišťuje funkce mediálních zdrojů, například pro hlášení nebo mixování médií v konferenčních scénářích.

3PCC hraje klíčovou roli při umožňování síťových služeb, kde servisní logika sídlí v síti, nikoli v koncových bodech. To umožňuje poskytovatelům služeb nasazovat pokročilé telefonní služby bez nutnosti inteligence na straně klienta nebo aktualizací softwaru na uživatelských zařízeních. Architektura podporuje různé servisní scénáře včetně služeb kliknutí a volání (kdy webová aplikace iniciuje hovor mezi dvěma stranami), aplikací pro call centra, služeb předplaceného volání a řešení pro multimediální konference. 3PCC také umožňuje schopnosti zákonného odposlechu a integraci účtování tím, že poskytuje AS úplnou přehlednost a kontrolu nad procesy navazování a ukončování relací.

## K čemu slouží

3PCC byl vyvinut pro řešení omezení tradičního peer-to-peer navazování [SIP](/mobilnisite/slovnik/sip/) relací, kde oba koncové body musí mít přímou signalizační schopnost a inteligenci pro vyjednávání parametrů relace. V raných službách VoIP a multimédií vyžadovaly pokročilé funkce jako přesměrování hovoru, konferenční hovory a síťově iniciované relace složité implementace na koncových bodech nebo proprietární řešení. 3PCC poskytuje standardizovaný mechanismus pro síťové poskytovatele služeb, jak nabízet služby s přidanou hodnotou bez závislosti na schopnostech koncových bodů.

Tato technologie řeší několik klíčových problémů v poskytování telekomunikačních služeb. Za prvé umožňuje poskytovatelům služeb implementovat složitou logiku řízení hovoru v síti namísto požadavku na inteligentní koncové body, což umožňuje konzistentní poskytování služeb napříč různými typy zařízení a jejich schopnostmi. Za druhé poskytuje mechanismus pro aplikace třetích stran (jako webové služby nebo podnikové aplikace) k iniciování a řízení komunikačních relací, což umožňuje integraci mezi komunikačními službami a jinými aplikacemi. Za třetí umožňuje centralizované účtování, vynucování politik a servisní logiku, kterou lze aktualizovat nezávisle na softwaru koncových bodů.

Historicky se 3PCC objevil jako součást architektury IMS (IP Multimedia Subsystem) ve 3GPP Release 8, navazující na dřívější práci v oblasti služeb a řízení hovorů založených na SIP. Řešil rostoucí potřebu síťových operátorů nabízet pokročilé služby standardizovaným a interoperabilním způsobem při zachování kontroly nad kvalitou služeb, účtováním a síťovými zdroji. Architektura také podporuje regulatorní požadavky, jako je zákonný odposlech a služby tísňového volání, tím, že poskytuje centralizovaný bod kontroly pro komunikační relace.

## Klíčové vlastnosti

- Síťové řízení relací bez potřeby inteligence na koncovém bodu
- Podpora relací iniciovaných aplikacemi třetích stran
- Architektura back-to-back uživatelského agenta (B2BUA)
- Nezávislá SIP dialogová spojení s každým koncovým bodem
- Centralizované účtování a vynucování politik
- Integrace s prvky jádra sítě IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [S-CSCF – Serving Call Session Control Function](/mobilnisite/slovnik/s-cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [B2BUA – Back-to-Back User Agent](/mobilnisite/slovnik/b2bua/)

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking
- **TS 32.275** (Rel-19) — MMTel Charging Specification

---

📖 **Anglický originál a plná specifikace:** [3PCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/3pcc/)
