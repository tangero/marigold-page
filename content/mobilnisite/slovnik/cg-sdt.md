---
slug: "cg-sdt"
url: "/mobilnisite/slovnik/cg-sdt/"
type: "slovnik"
title: "CG-SDT – Configured Grant Small Data Transmission"
date: 2025-01-01
abbr: "CG-SDT"
fullName: "Configured Grant Small Data Transmission"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cg-sdt/"
summary: "CG-SDT je mechanismus 3GPP umožňující efektivní přenos malých datových paketů v NR bez režie dynamického plánování. Používá předem nakonfigurované uplinkové prostředky, což zařízením umožňuje vysílat"
---

CG-SDT je mechanismus 3GPP, který využívá předem nakonfigurované uplinkové prostředky pro efektivní přenos malých objemů dat, čímž odstraňuje nutnost plánovacích žádostí za účelem snížení latence, signalizace a spotřeby energie pro IoT a periodické aplikace.

## Popis

Configured Grant Small Data Transmission (CG-SDT) je funkce zavedená ve specifikaci 3GPP Release 17 pro New Radio (NR), která umožňuje uživatelskému zařízení (UE) přenášet malé objemy dat v uplinku pomocí předem nakonfigurovaných rádiových prostředků bez nutnosti dynamického přidělování ze strany gNB. Funguje ve stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE, což UE umožňuje setrvat v tomto stavu s nízkou spotřebou při provádění datových přenosů, a tím se vyhnout přechodu do stavu RRC_CONNECTED a s ním spojené režie signalizace. gNB poskytne UE konfiguraci configured grantu prostřednictvím RRC signalizace, která zahrnuje parametry jako časové prostředky (periodicita, offset), frekvenční prostředky (Resource Blocks), modulaci a kódové schéma ([MCS](/mobilnisite/slovnik/mcs/)) a nastavení řízení výkonu. Tuto konfiguraci si UE uloží a může ji opakovaně používat pro více přenosů podle definované periody.

Z architektonického hlediska se CG-SDT integruje do existujícího uplinkového rámce NR a využívá mechanismus Configured Grant Type 1, kde jsou prostředky plně nakonfigurovány přes RRC a aktivovány bez signalizace na vrstvě 1. UE autonomně vybere vhodný configured grant ze své uložené konfigurace na základě příchodu dat a vysílá pomocí Physical Uplink Shared Channel (PUSCH). Mezi klíčové komponenty patří protokol RRC pro doručení konfigurace, vrstva [MAC](/mobilnisite/slovnik/mac/) pro zpracování priority logických kanálů a multiplexování v rámci grantu a vrstva PHY pro samotný přenos. gNB monitoruje předem nakonfigurované prostředky pro přenosy od UE a pro případné retransmise využívá s nakonfigurovaným grantem asociovaný [HARQ](/mobilnisite/slovnik/harq/) proces, přičemž v některých scénářích mohou retransmise vyžadovat přechod na procedury s dynamickým grantem.

Fungování CG-SDT zahrnuje vyhodnocení datové fronty UE vůči parametrům configured grantu, jako je maximální velikost transportního bloku, aby se určila vhodnost přenosu. Pokud data vyhovují a časování souhlasí, UE vytvoří MAC PDU, aplikuje nakonfigurované MCS a vysílá. gNB, který zná konfiguraci, přenos dekóduje. Tento proces odstraňuje nutnost Scheduling Request (SR), Buffer Status Report (BSR) a dynamického plánování UL grantu, což výrazně snižuje latenci pro malé dávky dat. Je navržen zejména pro sporadické provozy s malým objemem dat, typické pro IoT, nositelná zařízení a senzorové aplikace, kde by režie spojení byla nepřiměřená velikosti užitečné zátěže.

V širším síťovém kontextu CG-SDT zlepšuje využití rádiových prostředků minimalizací signalizace řídicí roviny, což uvolňuje prostředky pro další uživatele a snižuje zahlcení sítě. Podporuje efektivitu sítě tím, že umožňuje obsloužit více zařízení s omezenou signalizační kapacitou. Tato funkce je součástí širšího rámce Small Data Transmission (SDT) v 3GPP, který zahrnuje i jiné metody, jako je RA-SDT (Random Access based SDT), což poskytuje flexibilitu v závislosti na scénářích nasazení a schopnostech UE. Koncepce CG-SDT zajišťuje koexistenci s ostatními funkcemi NR a zachovává spolehlivost pomocí nakonfigurovaných HARQ procesů a případných záložních mechanismů.

## K čemu slouží

CG-SDT byl vyvinut, aby řešil neefektivitu tradičního spojově orientovaného přenosu dat pro malé, přerušované datové pakety v sítích 5G. Před jeho zavedením musela UE potřebující odeslat data, byť minimálního objemu, provést úplný přechod ze stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE do RRC_CONNECTED, což zahrnovalo proceduru náhodného přístupu, RRC resume a dynamické plánovací žádosti. Tento proces znamenal značnou režii signalizace, latenci a spotřebu energie, což bylo nepřiměřené pro aplikace odesílající pravidelně pouze několik bajtů, jako jsou IoT senzory, chytré měřicí přístroje nebo nositelné zdravotní monitory. Omezení předchozích přístupů bránila škálovatelnosti pro masivní IoT nasazení a zhoršovala uživatelský zážitek u aplikací s malými daty citlivými na latenci.

Motivace pro CG-SDT vychází z rostoucí poptávky po scénářích massive Machine-Type Communication (mMTC) a ultra-reliable low-latency communication (URLLC) v 5G, kde je efektivní zpracování malých dat klíčové. 3GPP zjistilo, že existující mechanismy byly optimalizovány pro velké, souvislé datové toky, ale ne pro sporadické malé pakety. CG-SDT to řeší tím, že umožňuje schopnost přenosu dat v režimu „always-on“ bez režie spojení, což je v souladu s cíli 5G, jako je efektivita sítě, nízká latence a úspora energie. Snižuje zatížení řídicí roviny na gNB, což umožňuje současnou podporu většího počtu zařízení, což je zásadní pro hustá IoT prostředí.

Historicky LTE zavedlo podobné koncepty, jako je Semi-Persistent Scheduling (SPS) pro Voice over LTE, ale CG-SDT rozšiřuje tento princip speciálně pro stav RRC_INACTIVE v NR a využívá vylepšený neaktivní stav zavedený v 5G. Řeší konkrétní výzvu přenosu malých dat ve složitější rámcové struktuře a širších šířkách pásma NR. Předkonfigurací prostředků CG-SDT minimalizuje signalizaci na rozhraní, snižuje spotřebu energie zařízení vyhýbáním se přechodům mezi stavy a snižuje latenci, aby splnila přísné požadavky pro průmyslové IoT a aplikace monitorování v reálném čase, čímž zaplňuje klíčovou mezeru v portfoliu schopností 5G.

## Klíčové vlastnosti

- Předem nakonfigurované uplinkové prostředky bez dynamického plánování
- Fungování ve stavu RRC_INACTIVE, aby se předešlo navazování spojení
- Snížená latence a režie signalizace pro malé pakety
- Podpora periodických a sporadických typů provozu
- Autonomní přenos UE na základě uložené konfigurace
- Integrace s HARQ procesy pro spolehlivost

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive

---

📖 **Anglický originál a plná specifikace:** [CG-SDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cg-sdt/)
