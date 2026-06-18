---
slug: "lcs-up"
url: "/mobilnisite/slovnik/lcs-up/"
type: "slovnik"
title: "LCS-UP – Location Services User Plane"
date: 2025-01-01
abbr: "LCS-UP"
fullName: "Location Services User Plane"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcs-up/"
summary: "Location Services User Plane (LCS-UP) je architektonický koncept a funkční framework 3GPP zaváděný pro 5G. Definuje přenosovou cestu a procedury na uživatelské rovině pro transport lokalizačních měřen"
---

LCS-UP je 3GPP 5G framework, který definuje přenosovou cestu a procedury na uživatelské rovině pro transport lokalizačních dat mezi UE, sítí a externími klienty, aby umožnil lokalizační služby s vysokou přesností a nízkou latencí.

## Popis

Location Services User Plane (LCS-UP) je základní architektonická komponenta v systému 5G, definovaná speciálně pro zpracování přenosu dat potřebných pro pokročilé lokalizační služby. Narozdíl od řídicí roviny [LCS-AP](/mobilnisite/slovnik/lcs-ap/), která řídí signalizaci a řízení session, je LCS-UP zodpovědná za skutečný přenos lokalizačních měřených dat, asistenčních dat a výsledků lokalizace přes uživatelskou rovinu. Toto oddělení umožňuje vyšší propustnost a přenos dat s nižší latencí, což je klíčové pro aplikace real-time lokalizace s vysokou přesností, jako autonomní řízení, rozšířená realita a průmyslový IoT.

Architektonicky zahrnuje LCS-UP několik síťových funkcí. Klíčovou entitou je Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G Core (5GC), která řídí lokalizační session. Přenosová cesta na uživatelské rovině typicky zahrnuje UE, gNB (nebo ng-eNB) v Radio Access Network (RAN), User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) a LMF. Pro UE-assisted nebo UE-based lokalizační metody (např. Assisted [GNSS](/mobilnisite/slovnik/gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/), senzorová lokalizace) generuje UE měřená data (např. satelitní pseudorange, měřené časové rozdíly). Tyto data jsou zabalena do LCS-UP Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) a odeslána přes dedikovanou Packet Data Unit (PDU) Session nebo QoS Flow zřízenou pro lokalizační služby. Data prochází přes gNB a UPF do LMF. Opačně může LMF zaslat asistenční data (např. GNSS ephemeris nebo informace o positioning reference signal ([PRS](/mobilnisite/slovnik/prs/)) z buněk) do UE přes stejnou přenosovou cestu na uživatelské rovině, aby pomohla jeho výpočtu pozice.

Fungování LCS-UP řídí [LCS](/mobilnisite/slovnik/lcs/) User Plane Protocol (LCS-UPP), který definuje formát PDU a procedury pro jejich výměnu. Lokalizační session je nejprve zřízena signalizací na řídicí rovině (pomocí protokolů jako LPP přes NAS). Když je session aktivní, může LMF instruovat UE a/nebo RAN, aby aktivovala spojení na uživatelské rovině pro přenos lokalizačních dat. Toto spojení využívá standardní mechanismy 5G uživatelské roviny (GTP-U tunely mezi gNB a UPF, N3/N9 interface), což zajišťuje, že může využívat možnosti network slicing a QoS 5G. Framework LCS-UP podporuje unicast (point-to-point mezi LMF a jedním UE) i multicast/broadcast (pro doručení společných asistenčních dat více UE) přenos dat, což ho činí velmi škálovatelným pro služby masového trhu.

## K čemu slouží

LCS-UP byl vytvořen, aby řešil omezení lokalizace pouze na řídicí rovině v předchozích releasech 3GPP, které nemohly efektivně podporovat masivní objemy dat a striktní požadavky na latenci vznikající 5G use cases. Signalizace řídicí roviny, ač spolehlivá pro řízení session, není optimalizována pro streamování velkých datasetů, jako raw GNSS měření, hustá asistenční data nebo časté updaty pozice. Historický přístup silně závisel na LPP (LTE Positioning Protocol) přenášeném přes NAS, což mohlo vytvořit bottleneck. LCS-UP to řeší přesunutím přenosu velkých dat na výkonnou 5G uživatelskou rovinu.

Motivace pochází z požadavků vertikálních průmyslů na přesnost na centimetrové úrovni a real-time kinematickou lokalizaci, klíčové pro automotive V2X, navigaci dronů a precizní zemědělství. Tyto aplikace potřebují kontinuální výměnu bohatých sensor fusion dat (z UE a síťových senzorů), což je nepraktické přes řídicí rovinu. LCS-UP využívá inherentní síly 5G uživatelské roviny: vysokou propustnost, ultra-nízkou latenci a QoS diferenciaci. Poskytnutím dedikované, optimalizované přenosové cesty pro lokalizační data umožňuje síťovým lokalizačním službám dosahovat výkonu na úrovni nebo nad úrovní standalone GNSS, speciálně v náročných prostředích jako urban canyon nebo indoors. Jeho zavádění v Release 18 reprezentuje strategickou evoluci LCS architektury 3GPP, aby plně využívala možnosti 5G-Advanced sítí.

## Klíčové vlastnosti

- Dedikovaná přenosová cesta na uživatelské rovině pro přenos lokalizačních dat s vysokou propustností
- Oddělení od řídicí roviny pro zlepšení latence a efektivity
- Podpora transportu raw lokalizačních měření (např. GNSS, měření RAN)
- Transport asistenčních dat ze sítě (LMF) do UE
- Využívá standardní 5G PDU Sessions a QoS Flows pro garantovanou kvalitu služby
- Umožňuje multicast/broadcast doručení společných asistenčních dat

## Související pojmy

- [LCS-UPP – Location Services User Plane Protocol](/mobilnisite/slovnik/lcs-upp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 24.572** (Rel-19) — 5G LCS User Plane Protocol Specification
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [LCS-UP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcs-up/)
