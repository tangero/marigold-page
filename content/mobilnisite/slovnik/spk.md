---
slug: "spk"
url: "/mobilnisite/slovnik/spk/"
type: "slovnik"
title: "SPK – Signalling Protection Key"
date: 2026-01-01
abbr: "SPK"
fullName: "Signalling Protection Key"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/spk/"
summary: "Kryptografický klíč používaný v 5G k specifické ochraně citlivých signalizačních zpráv mezi UE a sítí, zejména pro procedury Řízení roamingu (SoR) a Aktualizace parametrů UE (UPU). Zajišťuje integritu"
---

SPK je kryptografický klíč používaný v 5G k ochraně integrity a důvěrnosti citlivých signalizačních zpráv, jako jsou příkazy pro Řízení roamingu (Steering of Roaming) a Aktualizaci parametrů UE (UE Parameter Update), mezi UE a sítí.

## Popis

Signalling Protection Key (SPK) je bezpečnostní klíč zavedený v 5G, který poskytuje cílenou ochranu určitým signalizačním zprávám ne-přístupové vrstvy ([NAS](/mobilnisite/slovnik/nas/)), jež přenášejí citlivé síťové řídicí pokyny k uživatelskému zařízení (UE). Odlišuje se od primárních klíčů pro autentizaci a dohodu klíčů (jako je K_[AUSF](/mobilnisite/slovnik/ausf/)) a je odvozen speciálně pro zabezpečení doručování informací pro Řízení roamingu (SoR) a Aktualizaci parametrů UE ([UPU](/mobilnisite/slovnik/upu/)). SPK je generován síťovou funkcí Authentication Server Function (AUSF) a bezpečně poskytnut jak funkci Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), která chráněné informace vytváří, tak i UE.

Odvození SPK probíhá během primární autentizační procedury. AUSF jej vypočítá pomocí kotvícího klíče K_AUSF, specifického řetězcového štítku („N5G-SOR“) a dalších parametrů, jako je název obsluhující sítě. Tento klíč je následně odeslán UDM. Když UDM potřebuje odeslat UE zprávu SoR nebo UPU, použije SPK k výpočtu kódu autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)) pro ochranu integrity a případně i pro šifrování. Chráněná zpráva spolu s MAC je odeslána prostřednictvím [AMF](/mobilnisite/slovnik/amf/) k UE. UE, které si nezávisle odvodilo stejný SPK pomocí svého uloženého K_AUSF a přijatých parametrů, může ověřit MAC (a v případě potřeby dešifrovat). To dokazuje, že zpráva pochází z autorizovaného UDM domácí sítě a nebyla pozměněna.

Tento mechanismus je klíčový, protože zprávy SoR a UPU mají schopnost měnit chování UE. Zpráva SoR může aktualizovat seznam preferovaných veřejných pozemních mobilních sítí ([PLMN](/mobilnisite/slovnik/plmn/)) pro roaming, zatímco zpráva UPU může aktualizovat konfigurační parametry, jako je [IMSI](/mobilnisite/slovnik/imsi/) vestavěné SIM karty (eSIM). Bez kryptografické ochrany by útočník mohl takové zprávy padělat a navést UE na podvodnou síť nebo změnit jeho údaje o předplatném. SPK poskytuje vrstvu zabezpečení typu end-to-end mezi UDM a UE, která je nezávislá na bezpečnostním kontextu NAS vytvořeném mezi UE a AMF, a zajišťuje tak přímou kontrolu domácí sítě nad těmito kritickými procedurami.

## K čemu slouží

SPK byl vytvořen k odstranění bezpečnostní mezery v řízení roamingu a parametrů účastníka v 5G. V předchozích generacích se mechanismy jako Řízení roamingu často spoléhaly na méně bezpečné metody nebo nebyly kryptograficky ověřovány přímo od domácí sítě k UE. Protože 5G umožňuje dynamičtější síťové navádění a vzdálenou správu SIM (např. pro IoT zařízení), zvýšilo se riziko zachycení nebo vložení podvodných řídicích příkazů útočníky. Například kompromitovaná nebo falešná zpráva SoR by mohla navést miliony zařízení na škodlivou síť za účelem odposlechu.

Motivace pro SPK vychází z bezpečnostního principu 5G poskytovat službami řízené, granularní zabezpečení. Zatímco primární autentizace zabezpečuje počáteční spojení a zabezpečení NAS chrání obecnou signalizaci, specifické procedury s vysokým dopadem vyžadovaly vyhrazenou, ověřitelnou kontrolu ze strany domácí sítě. Mechanismus SPK zajišťuje, že pouze legitimní operátor domácí sítě prostřednictvím svého UDM může vydávat autoritativní příkazy SoR a UPU. Tím chrání jak účastníka před podvodem, tak operátora před ztrátou kontroly nad roamingovým chováním svých účastníků nebo daty o předplatném. Jde o klíčový prvek pro zabezpečenou, politikami řízenou mobilitu a vzdálenou správu zařízení v 5G, zejména pro nasazení IoT, kde je manuální zásah nemožný.

## Klíčové vlastnosti

- Vyhrazený klíč pro ochranu zpráv Řízení roamingu (SoR)
- Používá se také pro zabezpečení Aktualizace parametrů UE (UPU)
- Odvozen z 5G kotvícího klíče K_AUSF během autentizace
- Poskytnut UDM v domácí síti a UE
- Umožňuje ochranu integrity (MAC) a důvěrnosti pro citlivou NAS signalizaci
- Poskytuje zabezpečení typu end-to-end mezi UDM a UE, nezávislé na obsluhující síti

## Související pojmy

- [SOR – Support of Optimal Routing](/mobilnisite/slovnik/sor/)
- [UPU – UE Parameters Update](/mobilnisite/slovnik/upu/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)

## Definující specifikace

- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 24.380** (Rel-19) — MCPTT Media Plane Control Protocol
- **TS 24.582** (Rel-19) — MCData Media Plane Control Protocols
- **TS 29.380** (Rel-19) — MCPTT-LMR Interworking Media Plane Control
- **TS 29.582** (Rel-19) — MCData Interworking with LMR Systems
- **TS 33.179** (Rel-13) — MCPTT Security Architecture and Procedures
- **TS 33.180** (Rel-20) — Security of Mission Critical (MC) Service
- **TS 33.880** (Rel-15) — Security Study for Enhanced Mission Critical Services
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [SPK na 3GPP Explorer](https://3gpp-explorer.com/glossary/spk/)
