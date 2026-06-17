---
slug: "iwk-scef"
url: "/mobilnisite/slovnik/iwk-scef/"
type: "slovnik"
title: "IWK-SCEF – InterWorking - Service Capability Exposure Function"
date: 2025-01-01
abbr: "IWK-SCEF"
fullName: "InterWorking - Service Capability Exposure Function"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iwk-scef/"
summary: "Síťová funkce definovaná pro Cellular IoT (CIoT), která zajišťuje vzájemné propojení mezi SCEF a dalšími síťovými entitami, zejména MME/SGSN, pro doručování ne-IP dat (NIDD). Funguje jako přenosový uz"
---

IWK-SCEF je síťová funkce 3GPP pro Cellular IoT, která zajišťuje vzájemné propojení mezi SCEF a entitami, jako je MME, pro přenos ne-IP dat, což umožňuje vystavení služeb pro zařízení v optimalizovaných CIoT architekturách.

## Popis

IWK-SCEF (Interworking - Service Capability Exposure Function) je funkční entita zavedená ve 3GPP Release 13 jako součást vylepšení pro Cellular Internet of Things (CIoT). Jejím hlavním úkolem je usnadnit propojení mezi funkcí pro vystavení schopností služeb (SCEF) a uzly mobility jádrové sítě – konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node (SGSN) – pro určité CIoT služby. SCEF sama je klíčovým uzlem pro bezpečné vystavení síťových služeb a schopností aplikačním serverům třetích stran ([AS](/mobilnisite/slovnik/as/)), přímá rozhraní mezi SCEF a MME/SGSN však původně nebyla definována pro všechny procedury.

Architektonicky je IWK-SCEF logicky umístěn mezi SCEF a MME/SGSN. Funguje jako zprostředkovatel nebo proxy pro rozhraní T6a/T6b, které se používá pro doručování ne-IP dat ([NIDD](/mobilnisite/slovnik/nidd/)). NIDD je optimalizace pro CIoT, která umožňuje efektivní přenos malých, nepravidelných datových paketů z IoT zařízení bez režie plné IP vrstvy nebo PDP kontextu. Když chce aplikační server odeslat nebo přijmout NIDD data z/do IoT zařízení, komunikuje se SCEF přes [API](/mobilnisite/slovnik/api/) rozhraní T8. Pro vlastní přenos dat a správu relace se zařízením musí SCEF komunikovat s MME (pro LTE) nebo SGSN (pro 2G/3G). IWK-SCEF poskytuje tento propojovací bod a přeposílá zprávy související s NIDD mezi SCEF a MME/SGSN.

Jak to funguje, zahrnuje specifické signalizační procedury. Například pro NIDD iniciované mobilním zařízením odešle zařízení data do MME. MME pak tato data přepošle přes rozhraní T6a do IWK-SCEF. IWK-SCEF je pak směruje do příslušného SCEF, který je doručí cílovému aplikačnímu serveru. Opačná cesta platí pro NIDD směřující do mobilního zařízení. IWK-SCEF zajišťuje mapování identifikátorů, spravuje kontexty NIDD relací a zajišťuje bezpečný a spolehlivý přenos malých datových paketů. Je to kritická komponenta v CIoT EPS architektuře pro umožnění efektivní, síťově vystavené komunikace IoT, zejména pro zařízení využívající optimalizaci CIoT EPS přes řídicí rovinu, kde jsou data přenášena v [NAS](/mobilnisite/slovnik/nas/) signalizaci.

## K čemu slouží

IWK-SCEF byl vytvořen, aby vyřešil konkrétní architektonickou mezeru v původním rámci CIoT a SCEF definovaném v dřívějších releasech. SCEF byla navržena pro vystavení síťových schopností, ale její přímé propojení s [MME](/mobilnisite/slovnik/mme/) a SGSN pro klíčovou službu Non-IP Data Delivery ([NIDD](/mobilnisite/slovnik/nidd/)) nebylo plně specifikováno, což vytvářelo překážku pro implementaci efektivní přepravy IoT dat.

Problém, který řeší, je umožnění modelu vystavení služeb založeného na SCEF pro nové, optimalizované CIoT architektury. IoT zařízení často využívají energeticky účinné, na latenci tolerantní komunikační metody, jako je NIDD přes řídicí rovinu. Aby byly tyto služby zařízení dostupné externím aplikacím přes API rozhraní T8 SCEF, byla nutná standardizovaná a bezpečná cesta ze SCEF do MME/SGSN. Bez IWK-SCEF by operátoři potřebovali proprietární integrace nebo alternativní, méně optimální datové cesty pro CIoT zařízení využívající NIDD, což by podkopalo zisky v efektivitě z CIoT optimalizací.

Jeho zavedení v Release 13 bylo motivováno potřebou dokončit end-to-end architekturu pro vystavení CIoT služeb. Zajistilo, že výhody SCEF – jako je bezpečný přístup přes API, abstrakce síťových schopností a zjednodušený vývoj aplikací – mohou být plně využity pro segment masivního IoT. Definováním IWK-SCEF poskytla 3GPP jasný, standardizovaný propojovací bod, který umožnil škálovatelné nasazení služeb NIDD, a tím podpořila nízkonákladové případy užití s dlouhou životností baterií, které jsou ústřední pro Cellular IoT.

## Klíčové vlastnosti

- Poskytuje funkci vzájemného propojení/proxy mezi SCEF a MME/SGSN pro CIoT služby
- Umožňuje doručování ne-IP dat (NIDD) pro IoT zařízení prostřednictvím vrstvy pro vystavení SCEF
- Podporuje rozhraní T6a (směrem k MME) a T6b (směrem k SGSN) pro signalizaci NIDD
- Přeposílá a mapuje zprávy správy NIDD relací mezi jádrovou sítí a SCEF
- Integruje se s optimalizací CIoT EPS přes řídicí rovinu pro efektivní přenos dat
- Umožňuje bezpečné vystavení služeb IoT zařízení externím aplikačním serverům

## Související pojmy

- [NIDD – Non-IP Data Delivery](/mobilnisite/slovnik/nidd/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)

## Definující specifikace

- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.128** (Rel-19) — MME/SGSN-SCEF Diameter Interfaces for PDN Interworking
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [IWK-SCEF na 3GPP Explorer](https://3gpp-explorer.com/glossary/iwk-scef/)
