---
slug: "ddds"
url: "/mobilnisite/slovnik/ddds/"
type: "slovnik"
title: "DDDS – Downlink Data Delivery Status"
date: 2025-01-01
abbr: "DDDS"
fullName: "Downlink Data Delivery Status"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ddds/"
summary: "DDDS je mechanismus 5G Core Network, který poskytuje oznámení o stavu doručení dat ve směru downlink, když na UPF dochází k bufferingu. Umožňuje efektivní úsporu energie pro UE tím, že jim dovoluje př"
---

DDDS je mechanismus 5G Core Network, který poskytuje oznámení o stavu doručení dat ve směru downlink, když na UPF dochází k bufferingu.

## Popis

DDDS (Downlink Data Delivery Status) je sofistikovaný oznamovací mechanismus v rámci 5G Core Network, který funguje ve spojení s bufferingovými schopnostmi User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Když pro UE v idle nebo inactive módu dorazí data ve směru downlink, UPF tato data uloží do bufferu a spustí oznamovací proceduru, aby informovala UE o čekajícím doručení dat. Mechanismus zahrnuje koordinovanou signalizaci mezi UPF, Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) pro správu přechodů stavu UE a načasování doručení dat.

Architektura zahrnuje detekci dat ve směru downlink pro UE, která není v connected módu, na straně UPF. Namísto okamžitého pagingu UE UPF data uloží do bufferu a pošle Downlink Data Notification ([DDN](/mobilnisite/slovnik/ddn/)) k SMF. SMF poté vyhodnotí, zda spustit okamžitý paging, nebo využít DDDS, na základě konfigurovaných politik, schopností UE a síťových podmínek. Když je DDDS vyvolán, síť pošle oznámení UE, které indikuje, že jsou k dispozici data v bufferu, a vyzve UE k přechodu do connected módu pro jejich převzetí.

Klíčové komponenty zahrnují bufferingovou schopnost UPF, funkci SMF pro rozhodování o politikách pro spuštění DDDS a roli AMF v řízení mobility a přechodů stavu UE. UPF udržuje bufferingové kontexty pro UE, včetně správy timerů pro dobu, po kterou mají být data bufferována, než jsou zahozena nebo doručena alternativními prostředky. SMF tyto bufferingové parametry konfiguruje a rozhoduje na základě dat o předplatném, síťových politik a podmínek v reálném čase.

DDDS funguje prostřednictvím specifických procedur rozhraní N4 mezi UPF a SMF, definovaných v 3GPP TS 29.244. UPF hlásí události bufferingu a stav doručení prostřednictvím procedur modifikace [PFCP](/mobilnisite/slovnik/pfcp/) (Packet Forwarding Control Protocol) session. Mechanismus podporuje různé režimy oznamování, včetně okamžitého oznámení, odloženého oznámení na základě timerů a podmíněného oznámení na základě charakteristik dat nebo vzorců chování UE.

Tato technologie hraje klíčovou roli v funkcích pro úsporu energie v 5G, zejména pro IoT zařízení a smartphony s přerušovaným datovým provozem. Snížením zbytečného pagingu a procedur navazování spojení minimalizuje DDDS signalizační režii při zachování efektivního doručování dat. Bufferingová schopnost na UPF zajišťuje integritu dat a správné řazení, i když jsou UE v úsporných stavech po delší dobu.

## K čemu slouží

DDDS byl vytvořen, aby řešil základní výzvu vyvážení spotřeby energie UE a efektivního doručování dat v mobilních sítích. V předchozích generacích (4G/LTE), když pro idle UE dorazila data ve směru downlink, síť okamžitě pagingovala UE a nutila ji navázat spojení bez ohledu na to, zda byla data časově kritická. Tento přístup způsoboval zbytečnou spotřebu energie, zejména u IoT zařízení a smartphonů s přerušovaným provozem na pozadí.

Technologie řeší problém požadavků na 'vždy zapojené' spojení, které vyčerpávají baterie UE. Zavedením inteligentního bufferingu na síťové hraně ([UPF](/mobilnisite/slovnik/upf/)) a selektivních oznamovacích mechanismů umožňuje DDDS UE zůstat déle v úsporných stavech, a zároveň zajišťuje včasné doručení důležitých dat. To je obzvláště cenné pro nasazení massive IoT, kde zařízení mohou přenášet nebo přijímat data pouze sporadicky, ale potřebují udržet výdrž baterie po celé roky.

Historický kontext ukazuje, že dřívější přístupy jako Power Saving Mode ([PSM](/mobilnisite/slovnik/psm/)) v LTE poskytovaly prodloužená období spánku, ale činila zařízení během těchto dob nedosažitelnými. DDDS představuje evoluci, která zachovává dosažitelnost při optimalizaci spotřeby energie. Motivací byly požadavky 5G na podporu různých případů užití s různými potřebami latence a spotřeby energie, od ultra-spolehlivých nízkolatentních komunikací po massive machine-type komunikace s extrémními požadavky na energetickou účinnost.

## Klíčové vlastnosti

- Buffering dat na UPF pro UE v idle/inactive módu
- Selektivní spouštění oznámení na základě rozhodnutí politik
- Správa bufferingu na základě timerů s konfigurovatelnou expirací
- Integrace s funkcemi pro úsporu energie v 5G a informacemi o asistenci od UE
- Podpora různých režimů oznamování (okamžité, odložené, podmíněné)
- Procedury rozhraní N4 pro koordinaci událostí bufferingu mezi UPF a SMF

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.303** (Rel-19) — DNS Procedures for Evolved Packet System
- **TS 38.823** (Rel-16) — Enhancement Study for Disaggregated gNB

---

📖 **Anglický originál a plná specifikace:** [DDDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ddds/)
