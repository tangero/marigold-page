---
slug: "nra"
url: "/mobilnisite/slovnik/nra/"
type: "slovnik"
title: "NRA – Non-Aggregated RUCI Report Answer"
date: 2025-01-01
abbr: "NRA"
fullName: "Non-Aggregated RUCI Report Answer"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nra/"
summary: "NRA je specifický typ hlášení v rámci architektury RAN and User Plane Congestion Information (RUCI) od 3GPP. Jedná se o odpovědní zprávu z uzlu RAN (např. gNB) do jádra sítě, která poskytuje podrobná"
---

NRA je podrobná neagregovaná odpovědí zpráva uzlu RAN v rámci architektury RUCI, která hlásí konkrétní události kongesce uživatelské roviny do jádra sítě pro správu provozu.

## Popis

Non-Aggregated RUCI Report Answer (NRA) je protokolová zpráva definovaná v rámci mechanismu hlášení RAN and User Plane Congestion Information (RUCI) od 3GPP, specifikovaná v architektuře Policy and Charging Control (PCC). Je přenášena z uzlu rádiové přístupové sítě (RAN), jako je [eNB](/mobilnisite/slovnik/enb/) nebo gNB, do funkce jádra sítě, typicky Traffic Detection Function (TDF) nebo Policy and Charging Rules Function (PCRF) prostřednictvím Policy and Charging Enforcement Function (PCEF). Zpráva je přímou odpovědí na žádost o informace o kongesci a obsahuje podrobná data na úrovni jednotlivých událostí nebo toků, na rozdíl od agregovaných statistik.

Jak to funguje, je součástí širší smyčky povědomí o kongesci. Když RAN zaznamená kongesci uživatelské roviny (např. vysokou latenci, ztrátu paketů na konkrétním přenosovém kanálu nebo QoS Flow), může být nakonfigurován, aby to hlásil. Jádro sítě prostřednictvím TDF/PCRF může odeslat RUCI Report Request žádající o konkrétní informace. Uzel RAN následně vygeneruje zprávu NRA. Tato zpráva obsahuje detailní pole, jako je identifikátor uživatelského zařízení (UE) (např. [IMSI](/mobilnisite/slovnik/imsi/) nebo [GPSI](/mobilnisite/slovnik/gpsi/)), identifikátor zasaženého přenosového kanálu/QoS Flow, úroveň kongesce (např. závažnost), časová razítka a potenciálně i informace o poloze UE. Tato data jsou formátována podle Diameter referenčních bodů Rx nebo Gx (specifikovaných v 29.213, 29.217) nebo jiných rozhraní pro správu.

Klíčové komponenty zapojené do procesu jsou uzel RAN (reportér), PCEF (často v PGW/[UPF](/mobilnisite/slovnik/upf/), který vynucuje politiky), PCRF (který činí rozhodnutí o politikách) a TDF (který provádí detekci aplikací). Role zprávy NRA je poskytnout nejjemnější úroveň detailu dat o kongesci. To umožňuje jádru sítě přesně pochopit, který konkrétní datový tok uživatele způsobuje nebo zažívá kongesci. S těmito informacemi může PCRF činit inteligentní, cílená rozhodnutí o politikách. Například může dynamicky upravit parametry QoS pro tento konkrétní tok, iniciovat přesměrování provozu na jinou přístupovou síť nebo spustit akce účtování specifické pro aplikaci. To umožňuje vysoce detailní a reaktivní správu provozu v rámci sítě 3GPP.

## K čemu slouží

NRA existuje k řešení problému hrubého a reaktivního řízení kongesce v mobilních sítích. Tradiční metody se často spoléhaly na agregované metriky na úrovni buňky, což ztěžovalo identifikaci konkrétních uživatelů nebo aplikací způsobujících kongesci. To vedlo k všeobecným politikám omezování přenosové rychlosti, které zhoršovaly uživatelský zážitek pro všechny, místo aby cíleně řešily problematický provoz. Architektura RUCI a konkrétně NRA byly vytvořeny proto, aby poskytly jádru sítě hluboký, akční přehled o kongesci uživatelské roviny na úrovni RAN pro jednotlivé toky.

Historický kontext vychází z rostoucí složitosti provozu s nástupem různorodých internetových aplikací a potřeby chytřejšího Policy and Charging Control (PCC). Dřívější mechanismy PCC mohly pravidla vynucovat, ale často byly slepé k reálným podmínkám v RAN. Motivací pro NRA bylo tuto smyčku uzavřít a umožnit PCRF aplikovat politiky na základě skutečného výkonu rádiové sítě, nikoli pouze předplatitelských dat nebo obecného vytížení sítě. To umožňuje efektivnější využití vzácných rádiových zdrojů a lepší uživatelský zážitek pro všechny.

Dále NRA řeší potřebu síťování a optimalizace provozu s ohledem na aplikace. Hlášením neagregovaných dat mohou operátoři korelovat události kongesce s konkrétními aplikacemi (detekovanými TDF). To umožňuje pokročilé případy užití, jako je sponzorovaný přenos dat, kde může poskytovatel aplikace zaplatit za zajištění určité úrovně QoS i během kongesce, nebo rodičovské kontroly, které omezují šířku pásma pro konkrétní služby. V podstatě NRA poskytuje kritický datový zdroj, který transformuje mobilní síť ze statické trubky na dynamicky optimalizovanou a zpeněžitelnou služební platformu.

## Klíčové vlastnosti

- Poskytuje podrobné neagregované hlášení kongesce na úrovni jednotlivých toků/uživatelů z RAN do jádra sítě
- Součást architektury hlášení RAN and User Plane Congestion Information (RUCI)
- Přenášeno přes rozhraní založená na Diameter (např. Rx, Gx) nebo rozhraní pro správu
- Obsahuje identifikátory pro UE, přenosový kanál/QoS Flow, úroveň kongesce a časové razítko
- Umožňuje detailní rozhodnutí o politikách v reálném čase ze strany PCRF/TDF
- Podporuje správu provozu a zmírňování kongesce s ohledem na aplikace

## Definující specifikace

- **TS 29.213** (Rel-19) — PCC Signalling Flows and QoS Mapping
- **TS 29.217** (Rel-19) — Policy and Charging Control (PCC) for Np Interface
- **TS 32.828** (Rel-10) — Study on 3GPP-TMF NRM/SID Alignment
- **TS 32.829** (Rel-10) — Fault Management Alignment Study
- **TS 32.831** (Rel-10) — 3GPP-TMF PM Alignment Study
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access

---

📖 **Anglický originál a plná specifikace:** [NRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nra/)
