---
slug: "tsi"
url: "/mobilnisite/slovnik/tsi/"
type: "slovnik"
title: "TSI – Transport Session Identifier"
date: 2025-01-01
abbr: "TSI"
fullName: "Transport Session Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tsi/"
summary: "Jedinečný identifikátor pro transportní relaci, například pro přenosový kanál služby Multimedia Broadcast/Multicast Service (MBMS), v rámci sítě 3GPP. Je klíčový pro správné směrování a správu datovýc"
---

TSI je jedinečný identifikátor pro transportní relaci, například pro přenosový kanál MBMS, který umožňuje síti 3GPP správně směrovat a spravovat datové toky pro služby typu point-to-multipoint.

## Popis

Identifikátor transportní relace (TSI) je základním prvkem v architektuře služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) 3GPP, konkrétně definovaným pro službu přenosového kanálu MBMS. Slouží jako jedinečný identifikátor konkrétní transportní relace MBMS platný v celé síti. Transportní relace představuje datový tok pro konkrétní službu MBMS, například živý televizní přenos nebo distribuci softwarové aktualizace, po definované časové období. TSI přiřazuje centrum služeb vysílání a skupinového vysílání ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je hlavní síťová entita odpovědná za autorizaci a zahájení relací MBMS.

Architektonicky je TSI přenášen v rámci protokolů řídicí a uživatelské roviny specifických pro MBMS. V řídicí rovině je zahrnut v zprávách o zahájení a ukončení relace odesílaných z BM-SC do brány MBMS ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)) a dále do rádiové přístupové sítě (např. [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v 5G NR). To umožňuje všem síťovým prvkům zapojeným do datové cesty MBMS jednoznačně identifikovat relaci, kterou mají obsluhovat. V uživatelské rovině je TSI typicky součástí hlaviček paketů (např. v klíči Generic Routing Encapsulation ([GRE](/mobilnisite/slovnik/gre/)) pro rozhraní M1 mezi MBMS-GW a eNB/gNB), což umožňuje správné multiplexování a demultiplexování datových paketů patřících k různým relacím MBMS přes sdílené transportní prostředky.

TSI funguje ve spojení s dalšími identifikátory, jako je dočasný identifikátor mobilní skupiny ([TMGI](/mobilnisite/slovnik/tmgi/)), který identifikuje službu MBMS z pohledu uživatelského předplatného. Zatímco TMGI je znám uživatelskému zařízení (UE) a používá se pro vyhledání služby a připojení k ní, TSI je primárně interní síťový identifikátor pro správu relací a směrování. Jeho role je klíčová pro škálovatelnost a efektivitu, protože umožňuje jedné rádiové buňce vysílat více souběžných služeb MBMS. Síť používá TSI pro mapování správných dat na správné rádiové přenosové kanály a pro správu událostí životního cyklu relace, jako je aktivace a deaktivace, bez nejednoznačnosti.

Klíčové komponenty, které pracují s TSI, zahrnují BM-SC (který jej generuje), bránu MBMS (která jej používá pro vazbu přenosového kanálu a přeposílání paketů) a uzly rádiové přístupové sítě (které jej používají k založení příslušných rádiových přenosových kanálů typu point-to-multipoint). Jeho konzistentní použití na těchto rozhraních zajišťuje synchronizovaný stav relace v celé síti. TSI je základním kamenem spolehlivého provozu MBMS, zabraňuje chybnému doručování dat a umožňuje efektivní využití prostředků pro vysílací a skupinový provoz, což je nezbytné pro aplikace jako komunikace pro veřejnou bezpečnost, doručování obsahu velkému publiku a zprávy [V2X](/mobilnisite/slovnik/v2x/).

## K čemu slouží

TSI byl vytvořen k řešení základního požadavku na jedinečnou identifikaci jednotlivých transportních relací v rámci architektury [MBMS](/mobilnisite/slovnik/mbms/) 3GPP. Před zavedením MBMS byly mobilní sítě optimalizovány pro komunikaci typu point-to-point (unicast), kde je mezi sítí a každým uživatelem zřízeno vyhrazené spojení. Tento model je neefektivní pro doručování stejného obsahu mnoha uživatelům současně, protože duplikuje data v jádru sítě a rádiové síti, což plýtvá přenosovou kapacitou a rádiovými prostředky.

Zavedení MBMS ve verzi 3GPP Release 6 vyžadovalo nový paradigma: doručování typu point-to-multipoint. To zavedlo koncept 'relace' – dočasného datového toku pro konkrétní službu. Síť potřebovala robustní mechanismus k rozlišení mezi více souběžnými relacemi, zejména v jedné buňce vysílající několik televizních kanálů nebo datových proudů. TSI tento problém řeší tím, že poskytuje síťové infrastruktuře jedinečný popisovač. Umožňuje BM-SC dát síti pokyn k zahájení nebo ukončení přenosu konkrétního datového toku a umožňuje směrovačům a základnovým stanicím správně přiřadit příchozí IP pakety ke správnému vysílacímu rádiovému přenosovému kanálu.

Bez jedinečného identifikátoru transportní relace by síť nebyla schopna spravovat více vysílacích toků, což by vedlo k potenciálnímu chybnému směrování dat, neschopnosti nezávisle řídit relace a celkové nespolehlivosti služby MBMS. TSI je proto klíčovým prvkem umožňujícím škálovatelnost a spravovatelnost vysílacích a skupinových služeb v sítích 3GPP a tvoří nezbytnou součást oddělení řídicí a uživatelské roviny pro skupinovou komunikaci. Řešil omezení čistě unicastového doručování pro hromadnou distribuci obsahu a položil základy pro vyvinuté služby multimediálního vysílání, jako je eMBMS (Evolved MBMS) a FeMBMS (Further evolved MBMS).

## Klíčové vlastnosti

- Jednoznačně identifikuje transportní relaci MBMS v celé síti
- Přiřazen a řízen centrem služeb vysílání a skupinového vysílání (BM-SC)
- Používán jak v řídicí rovině (signalizace správy relací), tak v uživatelské rovině (hlavičky paketů)
- Umožňuje multiplexování více relací MBMS přes sdílené transportní a rádiové prostředky
- Nezbytný pro správné směrování a vazbu přenosového kanálu v architektuře MBMS
- Funguje ve spojení s TMGI pro korelaci služby a relace

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [TMGI – Temporary Multicast Group Identifier](/mobilnisite/slovnik/tmgi/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.852** (Rel-14) — MBMS user service profiles, APIs and transport enabler study
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point

---

📖 **Anglický originál a plná specifikace:** [TSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tsi/)
