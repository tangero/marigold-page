---
slug: "lr"
url: "/mobilnisite/slovnik/lr/"
type: "slovnik"
title: "LR – Low Power Wake-Up Receiver"
date: 2025-01-01
abbr: "LR"
fullName: "Low Power Wake-Up Receiver"
category: "IoT"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lr/"
summary: "Low Power Wake-Up Receiver (LR) je rádiová komponenta s ultranízkou spotřebou používaná v zařízeních IoT. Trvale naslouchá specifickému síťovému signálu pro probuzení, zatímco hlavní rádio zařízení je"
---

LR je rádiová komponenta s ultranízkou spotřebou energie v zařízeních IoT, která při vypnutém hlavním rádiu naslouchá síťovému signálu pro probuzení za účelem úspory energie a prodloužení životnosti baterie.

## Popis

Low Power Wake-Up Receiver (LR) je specializovaný rádiový přijímač definovaný ve specifikacích 3GPP pro internet věcí (IoT) a komunikaci typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)). Jeho hlavní architektonickou rolí je fungovat jako trvale zapnuté zařízení s ultranízkou spotřebou pro naslouchání, které je umístěno společně s hlavním mobilním modemem (např. LTE nebo NB-IoT modulem) uvnitř IoT zařízení. LR pracuje na samostatném, zjednodušeném rádiovém řetězci se spotřebou v řádu mikrowattů (µW), což je o několik řádů méně než spotřeba v řádu miliwattů (mW) hlavního mobilního transceiveru.

Jeho princip fungování je založen na dvoustupňovém procesu aktivace rádiové komunikace. Hlavní rádio zařízení je udržováno v hlubokém spánku nebo vypnutém stavu pro úsporu energie. LR však zůstává aktivní a periodicky skenuje předdefinovaný kanál nebo trvale naslouchá specifickému, jednoduchému signálu pro probuzení (WUS) vysílanému sítí. Tento WUS je typicky velmi základní sekvence, například vzor On-Off Keying ([OOK](/mobilnisite/slovnik/ook/)), navržený pro snadnou detekci s minimální komplexitou obvodu. Když LR detekuje platný signál pro probuzení určený pro dané zařízení (často obsahující identifikátor zařízení nebo skupiny), spustí jednotku pro správu napájení, která aktivuje hlavní mobilní rádio. Hlavní rádio následně naváže spojení se sítí pro příjem downlink dat nebo provedení naplánovaného vysílání.

Klíčovými komponentami systému LR jsou samotný obvod LR, design signálu pro probuzení, související procedury Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) pro přenos WUS a rozhraní správy napájení mezi LR a hlavním modemem. Jeho úlohou v síti je umožnit efektivní downlinkově orientovanou komunikaci pro masivní počty IoT zařízení. Přesouvá nároky na trvalou dostupnost z hlavního rádiového modulu s vysokou spotřebou na zanedbatelně spotřebový LR, čímž řeší klíčový problém životnosti baterie pro stacionární senzory nebo senzory s nečastým hlášením. Síťové funkce jako základnová stanice (gNB v NR, [eNB](/mobilnisite/slovnik/enb/) v LTE) jsou rozšířeny o protokoly pro plánování a vysílání těchto signálů pro probuzení, často způsobem skupinového vysílání (group-cast) pro adresování více zařízení současně.

## K čemu slouží

Technologie Low Power Wake-Up Receiver byla vytvořena, aby řešila základní omezení v mobilním IoT: vysoké energetické náklady na udržování síťové dosažitelnosti. Tradiční mobilní zařízení, dokonce i v režimech úspory energie jako eDRX (extended Discontinuous Reception), musí pravidelně aktivovat své plné rádio, aby naslouchala stránkovacím zprávám. Toto periodické naslouchání, i když nečasté, stále dominuje energetické bilanci bateriově napájeného senzoru, u kterého se předpokládá životnost 10 a více let.

Předchozí přístupy, včetně Power Saving Mode (PSM) v LTE-M/NB-IoT, nabízely hluboký spánek, ale za cenu nedostupnosti zařízení pro downlink provoz, dokud se neprobudilo samo. Tento kompromis mezi životností baterie a downlink latencí byl pro mnoho aplikací vyžadujících přístup k zařízení na požádání nepřijatelný. Koncept LR tento kompromis ruší zavedením specializovaného obvodu s minimální spotřebou pro zajištění dosažitelnosti. Historický kontext představuje snahu 3GPP podporovat scénáře Massive [MTC](/mobilnisite/slovnik/mtc/) v 5G a dalších generacích, kde extrémní životnost baterie je klíčovým požadavkem. LR přímo umožňuje vizi zařízení s 'nulovou spotřebou' nebo 'bez baterie' tím, že snižuje spotřebu energie ve stavu pohotovosti na úroveň, kterou lze podpořit technikami získávání energie z okolí (energy harvesting).

## Klíčové vlastnosti

- Ultranízká spotřeba energie (řád mikrowatty) pro trvalé nebo periodické naslouchání
- Detekce jednoduchých signálů pro probuzení (WUS, např. modulace OOK) pro minimální složitost obvodu
- Hladká integrace se správou napájení hlavního mobilního modemu (LTE, NB-IoT, NR-Light)
- Podpora skupinového signalizačního probouzení pro efektivní adresování více zařízení
- Definované procedury pro plánování a konfiguraci přenosu WUS ze strany sítě
- Umožňuje téměř nulovou energetickou náročnost pro dosažitelnost zařízení a ruší kompromis mezi latencí a životností baterie

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 28.301** (Rel-19) — LSA Controller IRP Requirements
- **TS 28.302** (Rel-19) — LSA Controller IRP Management Operations
- **TS 28.620** (Rel-19) — FMC Federated Network Information Model (FNIM) UIM
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.855** (Rel-14) — Study on OAM Support for Licensed Shared Access
- **TS 38.124** (Rel-19) — NR UE EMC Requirements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.304** (Rel-19) — UE RRC_IDLE and RRC_INACTIVE Procedures
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [LR na 3GPP Explorer](https://3gpp-explorer.com/glossary/lr/)
