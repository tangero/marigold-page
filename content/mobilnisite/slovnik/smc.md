---
slug: "smc"
url: "/mobilnisite/slovnik/smc/"
type: "slovnik"
title: "SMC – Session Management Client"
date: 2026-01-01
abbr: "SMC"
fullName: "Session Management Client"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/smc/"
summary: "Session Management Client je funkční entita, typicky umístěná v uživatelském zařízení (UE), zodpovědná za zahájení, udržování a ukončení relací paketových datových jednotek (PDU). Interaguje se síťovo"
---

SMC je funkční entita v uživatelském zařízení (UE) zodpovědná za zahájení, udržování a ukončení PDU relací prostřednictvím interakce se síťovou funkcí správy relací (SMF).

## Popis

Session Management Client (SMC) je klíčová entita na úrovni protokolu v uživatelském zařízení (UE), která zvládá všechny aspekty správy relací paketových datových jednotek ([PDU](/mobilnisite/slovnik/pdu/)). V systémové architektuře 3GPP, zejména od EPS (4G) dále a ústředně pro 5G, je SMC koncovým bodem v UE pro signalizační protokol správy relací (např. zprávy správy relací protokolu Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/))). Jeho primárním protějškem v síti je funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) v core networku. SMC je zodpovědný za end-to-end signalizační tok, který zakládá, modifikuje a uvolňuje PDU relace, což jsou logická spojení poskytující IP konektivitu nebo jiné typy datové konektivity k datové síti ([DN](/mobilnisite/slovnik/dn/)).

Operačně SMC funguje výměnou specifických zpráv správy relací ([SM](/mobilnisite/slovnik/sm/)) s SMF přes NAS signalizační spojení. Když aplikace na UE vyžaduje datovou konektivitu, SMC formuluje žádost o založení PDU relace. Tato žádost obsahuje kritické parametry, jako je požadovaný název datové sítě ([DNN](/mobilnisite/slovnik/dnn/)), režim kontinuity relace a služby ([SSC](/mobilnisite/slovnik/ssc/)) a typ PDU relace (např. IPv4, IPv6, IPv4v6, Ethernet, Unstructured). SMC tuto žádost odešle přes Access Stratum (v 5G přes gNB/NG-RAN, v 4G přes [eNB](/mobilnisite/slovnik/enb/)) k SMF. SMF žádost zpracuje, interaguje s dalšími síťovými funkcemi, jako jsou PCF a UPF, a odešle odpověď zpět SMC. SMC poté nakonfiguruje interní zpracování paketů v UE (tzv. PDU Session Anchor v UE) na základě přijatých informací, jako je přidělená IP adresa a pravidla QoS.

Mezi klíčové interní komponenty logiky SMC patří stavový automat protokolu pro správu relací, obslužné rutiny pro různé typy SM zpráv (Založení, Modifikace, Uvolnění), lokální engine pro interpretaci síťových pravidel QoS a účtování a rozhraní k aplikační vrstvě a IP stacku UE. Během životního cyklu PDU relace SMC zvládá modifikační procedury spouštěné síťovými politikami (např. změna QoS, handover) nebo žádostmi UE. Také řídí uvolňování relací, ať už iniciované lokálně nebo sítí. Správná funkce SMC je zásadní pro poskytnutí bezproblémové, politikami řízené a QoS-aware datové konektivity uživateli, což z ní činí základní komponentu protokolového stacku UE.

## K čemu slouží

SMC existuje za účelem poskytnutí standardizovaného řídicího bodu v UE pro správu datových relací v paketově přepínaných mobilních sítích. Před standardizovanou správou relací (v raných vydáních 3GPP) byla konektivita jednodušší, ale méně flexibilní. Vývoj směrem k all-IP sítím a bohatým multimediálním službám si vyžádal sofistikovaný mechanismus pro zakládání relací se specifickými charakteristikami kvality, účtování a kontinuity. SMC byla vyvinuta jako součást NAS protokolu, aby tuto potřebu naplnila, a oddělila řízení správy relací od řízení mobility a řízení rádiových prostředků.

Řeší problém, jak může UE dynamicky žádat a vyjednávat komplexní parametry datového připojení v síti podporující rozmanité služby – od best-effort prohlížení webu po nízkolatenční hraní her nebo vysoce spolehlivý IoT. Protokol SMC umožňuje síti přesně řídit parametry relací UE, což umožňuje pokročilé funkce jako network slicing, diferencovaná QoS a efektivní využití prostředků. Jeho vytvoření bylo motivováno přechodem od circuit-switched dat a jednoduchých PDP kontextů v GPRS k plně IP-based, službami řízené architektuře EPS a 5GS. SMC poskytuje nezbytnou inteligenci v UE, aby se mohla účastnit tohoto vyjednávaného, politikami řízeného procesu zakládání relací, který je základním kamenem moderních mobilních širokopásmových a kritických komunikačních služeb.

## Klíčové vlastnosti

- Iniciuje procedury založení, modifikace a uvolnění PDU relace
- Vyměňuje si zprávy správy relací (SM) protokolu NAS se síťovou funkcí SMF
- Zpracovává a aplikuje síťově přidělená pravidla QoS a paketové filtry
- Spravuje více souběžných PDU relací pro různé DNN/S-NSSAI
- Zpracovává příkazy správy relací iniciované sítí
- Podporuje různé typy PDU relací (IP, Ethernet, Unstructured)

## Definující specifikace

- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.700** — 3GPP TR 33.700
- **TS 33.701** (Rel-19) — Study on mitigations against bidding down attacks
- **TS 33.821** (Rel-9) — LTE/SAE Security Threat Analysis and Countermeasures
- **TR 33.853** (Rel-17) — Study on User Plane Integrity Protection
- **TS 33.859** (Rel-11) — UTRAN Key Hierarchy Enhancement Study
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.300** (Rel-19) — NG-RAN Overall Description

---

📖 **Anglický originál a plná specifikace:** [SMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/smc/)
