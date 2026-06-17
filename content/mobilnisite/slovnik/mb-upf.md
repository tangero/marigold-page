---
slug: "mb-upf"
url: "/mobilnisite/slovnik/mb-upf/"
type: "slovnik"
title: "MB-UPF – Multicast/Broadcast User Plane Function"
date: 2026-01-01
abbr: "MB-UPF"
fullName: "Multicast/Broadcast User Plane Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mb-upf/"
summary: "Funkce 5G Core Network, která zpracovává uživatelskou rovinu pro multicastové a broadcastové služby. Efektivně distribuuje stejný obsah více uživatelům, čímž snižuje zatížení sítě a zlepšuje spektráln"
---

MB-UPF je funkce uživatelské roviny 5G Core Network, která efektivně distribuuje stejný multicastový nebo broadcastový obsah více uživatelům.

## Popis

Multicast/Broadcast User Plane Function (MB-UPF) je specializovaná síťová funkce v architektuře 5G Core (5GC), zavedená pro podporu point-to-multipoint přenosu dat. Funguje jako součást frameworku 5G Multicast-Broadcast Service ([5MBS](/mobilnisite/slovnik/5mbs/)). MB-UPF je zodpovědná za zpracování a směrování paketů uživatelské roviny pro multicastový a broadcastový provoz. Rozhraní k Radio Access Network (RAN) má přes rozhraní N3/N9 a k Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) přes rozhraní N4 pro řízení. Její klíčová role spočívá v replikaci a směrování datových paketů přijatých z multicastového zdroje (např. přes rozhraní N6) směrem k příslušným RAN uzlům obsluhujícím uživatelská zařízení (UE) přihlášená ke konkrétní multicastové relaci. Odlišuje se tak od standardní [UPF](/mobilnisite/slovnik/upf/), která primárně zpracovává unicastový provoz, tím, že je optimalizována pro one-to-many distribuci.

Architektonicky může být MB-UPF nasazena jako samostatná funkce nebo integrována se standardní UPF. Podporuje jak multicastový, tak broadcastový režim doručování. V multicastovém režimu doručuje obsah pouze těm UE, která se explicitně připojila k multicastové skupině, řízené přes Multicast Session Management Function (M-SMF) a Multicast Control Plane Function (M-CPF). V broadcastovém režimu tlačí obsah všem UE ve vymezené servisní oblasti. MB-UPF provádí replikaci paketů na základě identifikátorů multicastových skupin a QoS toků, čímž zajišťuje efektivní využití přenosových a rádiových prostředků. Také zpracovává řízení provozu, vynucování přepravních pravidel a sběr účtovacích dat pro multicastové/broadcastové relace v souladu s politikami od Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)).

Z protokolového hlediska využívá MB-UPF [GTP-U](/mobilnisite/slovnik/gtp-u/) tunely přes rozhraní N3 směrem k RAN. Pro multicast může vytvořit jediný GTP-U tunel k RAN uzlu, který pak dále distribuuje provoz přes rozhraní vzduch-pomocí technik Single-Cell Point-To-Multipoint (SC-PTM) nebo Multicast-Broadcast Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)). MB-UPF je klíčovým prvkem pro efektivní doručování obsahu, protože brání síti ve vytváření samostatných unicastových přenosových kanálů pro každého uživatele přijímajícího stejný obsah, čímž šetří prostředky jádra sítě a RAN a snižuje latenci při současném doručování velkému publiku.

## K čemu slouží

MB-UPF byla vytvořena, aby řešila inherentní neefektivitu používání unicastových spojení pro doručování populárního živého nebo na vyžádání obsahu mnoha uživatelům současně. Před jejím zavedením ve 3GPP Release 17 postrádaly 5G sítě standardizovaný, efektivní mechanismus jádra sítě pro multicastové a broadcastové služby. Zatímco LTE mělo vyvinutou službu Multimedia Broadcast Multicast Service (eMBMS), její integrace s 5G Core nebyla plně definována. Vzestup aplikací jako živé přenosy sportovních událostí, nouzová varování, bezdrátové aktualizace softwaru pro IoT zařízení a komunikace pro veřejnou bezpečnost vytvořil jasnou potřebu nativního 5G multicastového/broadcastového řešení.

Primární problém, který MB-UPF řeší, je zahlcení sítě a plýtvání prostředky. V modelu pouze s unicastem, pokud 1000 uživatelů na stadionu požádá o stejný živý videostream, síť vytvoří 1000 samostatných datových toků od obsahového serveru přes jádro sítě a přes rozhraní vzduch, což spotřebovává značnou šířku pásma a výpočetní výkon. MB-UPF jako součást architektury [5MBS](/mobilnisite/slovnik/5mbs/) umožňuje, aby jediný obsahový tok ze zdroje byl inteligentně replikován v optimálních bodech (v jádru sítě a RAN), což dramaticky snižuje přenosové zatížení a zlepšuje spektrální účinnost na rádiovém rozhraní. To umožňuje škálovatelné, vysoce kvalitní poskytování služeb masivnímu publiku, což je klíčové pro komerční životaschopnost nových mediálních služeb a pro důležité varovné systémy.

## Klíčové vlastnosti

- Efektivní point-to-multipoint přeposílání a replikace paketů uživatelské roviny
- Podpora jak multicastového (skupinového), tak broadcastového (oblastního) režimu doručování
- Integrace s řídicí rovinou 5GC přes rozhraní N4 pro správu relací
- Zpracování a vynucování QoS toků pro multicastový/broadcastový provoz
- Sběr a hlášení účtovacích dat pro MBS relace
- Podpora spolupráce s LTE eMBMS pro kontinuitu služby

## Související pojmy

- [5MBS – 5G Multicast-Broadcast Services](/mobilnisite/slovnik/5mbs/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.527** (Rel-19) — 5G System Restoration Procedures
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 29.581** (Rel-19) — MBSTF Service Based Interface Protocol Specification
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.279** (Rel-19) — 5G MBS Session Converged Charging
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [MB-UPF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mb-upf/)
