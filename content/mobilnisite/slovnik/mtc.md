---
slug: "mtc"
url: "/mobilnisite/slovnik/mtc/"
type: "slovnik"
title: "MTC – Machine Type Communications"
date: 2026-01-01
abbr: "MTC"
fullName: "Machine Type Communications"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtc/"
summary: "MTC je rámec 3GPP pro umožnění komunikace mezi stroji (M2M) přes mobilní sítě. Poskytuje optimalizované funkce pro připojení obrovského počtu nízkonákladových a nízkopříkonových zařízení, jako jsou se"
---

MTC je rámec 3GPP pro umožnění komunikace mezi stroji (machine-to-machine) přes mobilní sítě, optimalizovaný pro připojení obrovského počtu nízkonákladových a nízkopříkonových zařízení, jako jsou senzory a měřiče.

## Popis

Komunikace mezi stroji (Machine Type Communications, MTC) je komplexní rámec 3GPP navržený pro usnadnění efektivní, rozsáhlé komunikace mezi stroji (M2M) přes mobilní sítě. Zahrnuje sadu architektonických vylepšení, síťových funkcí a optimalizovaných procedur přizpůsobených pro zařízení, která přenášejí data autonomně bez přímé lidské interakce. Základní architektura zavádí MTC zařízení (MTC Device), MTC server (MTC Server) a MTC-InterWorking funkci ([MTC-IWF](/mobilnisite/slovnik/mtc-iwf/)). MTC zařízení je koncový bod, například senzor nebo aktuátor, který komunikuje přes veřejnou pozemní mobilní síť ([PLMN](/mobilnisite/slovnik/plmn/)). MTC server, umístěný v doméně poskytovatele služeb nebo na internetu, je entita, která s těmito zařízeními komunikuje přes PLMN a poskytuje rozhraní pro uživatele MTC (entitu využívající službu MTC). MTC-IWF, zavedená později, funguje jako zabezpečená brána mezi PLMN a externími MTC servery a zajišťuje autorizaci, překlad protokolů a spouštění komunikace. MTC funguje tak, že definuje specifické profily předplatného pro zařízení, což umožňuje funkce jako nízká mobilita, časově řízená komunikace a občasný přenos dat. Síť identifikuje provoz MTC a může aplikovat optimalizované politiky pro signalizaci, správu mobility a úsporu energie, což je klíčové pro zařízení napájená bateriemi. Klíčové procedury zahrnují spouštění zařízení (kdy síť může probudit spící zařízení), optimalizace pro přenos malých objemů dat a mechanismy pro řízení přetížení, které brání zahlcení sítě při současném pokusu o připojení obrovského počtu zařízení. Jeho úlohou je transformovat standardní mobilní síť, postavenou pro lidsky orientovaný hlas a data, na platformu schopnou efektivně obsluhovat jedinečné požadavky ekosystému internetu věcí.

## K čemu slouží

MTC bylo vytvořeno za účelem řešení zásadního nesouladu mezi tradičním návrhem mobilních sítí – optimalizovaným pro lidské účastníky s kontinuální mobilitou a relativně vysokými datovými rychlostmi – a potřebami aplikací komunikace mezi stroji. Před standardizací MTC bylo používání standardních mobilních předplatných pro stroje neefektivní a nákladné, což vedlo k nadměrné signalizační režii, neoptimální spotřebě energie a problémům se škálovatelností. Primární motivací bylo umožnit masivní rozsah IoT definováním standardizovaného, síťově nativního přístupu. To řeší problémy, jako je zahlcení sítě periodickými registracemi zařízení, vysoká cena a složitost modulů zařízení a absence specifických funkcí pro vzdálenou správu a monitorování. Historicky byla raná řešení M2M proprietární nebo používala neupravené moduly GSM/[GPRS](/mobilnisite/slovnik/gprs/), což nebylo udržitelné pro plánovaná nasazení IoT s miliony zařízení. Práce 3GPP, začínající ve verzi 10 a následně významně rozšířená, si kladla za cíl vytvořit dlouhodobě životný základ v rámci standardů mobilních sítí pro podporu různých vertikálních odvětví, jako jsou utility, automobilový průmysl a zdravotnictví, a zajistit tak bezpečnost, spravovatelnost a globální interoperabilitu.

## Klíčové vlastnosti

- Definuje optimalizované profily předplatného pro nízkopříkonová zařízení s nízkou mobilitou
- Zavádí služby spouštění zařízení pro síťově iniciovanou komunikaci se spícími zařízeními
- Specifikuje mechanismy pro řízení přetížení a zahlcení (např. Access Class Barring pro MTC) k ochraně sítě
- Umožňuje funkce pro občasný přenos dat a časově řízenou komunikaci
- Podporuje optimalizace pro přenos malých objemů dat prostřednictvím řídicí i uživatelské roviny
- Architektonicky definuje MTC Server a MTC-IWF pro zabezpečenou integraci na vrstvě služeb

## Související pojmy

- [MTC-IWF – Machine Type Communications - InterWorking Function](/mobilnisite/slovnik/mtc-iwf/)
- [PSM – Protocol State Machine](/mobilnisite/slovnik/psm/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.368** (Rel-19) — Network Improvements for Machine Type Communications
- **TR 22.988** (Rel-19) — Study on MTC Numbering Alternatives
- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.708** (Rel-13) — Service Capability Exposure Framework (SCEF) Architecture
- **TS 23.720** (Rel-13) — Cellular IoT Architecture Enhancement Study
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TR 23.730** (Rel-14) — Study on extended CIoT architecture
- **TS 23.789** (Rel-13) — 3GPP Monitoring Service Architecture Study
- … a dalších 32 specifikací

---

📖 **Anglický originál a plná specifikace:** [MTC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtc/)
