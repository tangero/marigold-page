---
slug: "ta"
url: "/mobilnisite/slovnik/ta/"
type: "slovnik"
title: "TA – Terminal Adaptor"
date: 2026-01-01
abbr: "TA"
fullName: "Terminal Adaptor"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ta/"
summary: "Terminálový adaptér (TA) je zařízení, které adaptuje ne-ISDN koncové zařízení pro připojení k síti ISDN, často používané v raných mobilních datových řešeních, jako jsou GSM datové karty. Funguje jako"
---

TA je zařízení, které adaptuje ne-ISDN koncové zařízení pro připojení k síti ISDN a funguje jako zařízení pro ukončení datového okruhu (DCE), aby umožnilo přenos dat po digitálních sítích.

## Popis

Terminálový adaptér (TA) je síťové rozhraní definované ve standardech 3GPP a [ITU-T](/mobilnisite/slovnik/itu-t/), používané primárně k usnadnění připojení mezi koncovým zařízením ([TE](/mobilnisite/slovnik/te/)) a rozhraním digitální sítě integrovaných služeb ([ISDN](/mobilnisite/slovnik/isdn/)). V kontextu mobilních komunikací často odkazuje na adaptéry, jako jsou GSM datové karty, které umožňují počítačům nebo jiným zařízením přístup k mobilním datovým službám. TA funguje jako zařízení pro ukončení datového okruhu ([DCE](/mobilnisite/slovnik/dce/)), které zajišťuje převod signálu, adaptaci protokolů a fyzickou konektivitu pro umožnění přenosu dat po digitálních sítích.

Z architektonického hlediska se TA nachází mezi TE (např. laptopem) a síťovým ukončením ([NT](/mobilnisite/slovnik/nt/)) nebo mobilní stanicí. Převádí data z nativního rozhraní TE, jako je RS-232 nebo [USB](/mobilnisite/slovnik/usb/), do formátů vhodných pro protokoly sítě ISDN nebo mobilní sítě. Například v systémech GSM může TA zapouzdřit data do protokolů definovaných v 3GPP TS 27.007 pro řízení pomocí AT příkazů a spravovat aspekty jako modulaci, opravu chyb a navázání hovoru. To umožňuje TE komunikovat se sítí bezproblémově bez vestavěných ISDN schopností.

Klíčové součásti TA zahrnují mikroprocesor pro zpracování protokolů, paměť pro firmware a obvody rozhraní pro fyzická připojení (např. sériové porty nebo sloty [PCMCIA](/mobilnisite/slovnik/pcmcia/)). Při provozu TA zajišťuje úkoly jako vytáčené připojení k síti, autentizaci a adaptaci datové rychlosti, podporující služby jako přepojování okruhů v raných sítích 2G/3G. Jeho role sahá až k mobilním scénářům, kde může při použití s mobilními sítěmi spravovat připojení rádiových zdrojů a předávání hovorů.

Význam TA spočívá v propojení staršího zařízení s moderními sítěmi, což umožnilo rozšířený přístup k datům předtím, než se staly běžnými integrované modemy. Ve specifikacích 3GPP je na něj odkazováno v mnoha dokumentech, což zdůrazňuje jeho roli v interoperabilitě a umožňování služeb. Jak se sítě vyvíjely, byla funkčnost TA integrována do pokročilejších zařízení, ale koncept zůstává relevantní pro pochopení historických datových adaptérů a jejich dopadu na mobilní konektivitu.

## K čemu slouží

Terminálový adaptér byl vytvořen k řešení potřeby připojení ne-ISDN koncových zařízení k sítím [ISDN](/mobilnisite/slovnik/isdn/) a raným mobilním datovým sítím, čímž řešil problémy interoperability při přechodu na digitální komunikace. Koncem 20. století, s nástupem sítí ISDN a GSM, mnoho stávajících zařízení postrádalo vestavěná digitální rozhraní, což vyžadovalo adaptér pro přístup k vysokorychlostním datovým službám. TA poskytl standardizované řešení, které umožnilo zařízením, jako jsou počítače, používat mobilní data prostřednictvím datových karet.

Historicky, před TA, byl přenos dat po mobilních sítích omezený nebo vyžadoval proprietární řešení, což bránilo jeho širokému přijetí. TA standardizoval rozhraní mezi TE a DCE podle doporučení ITU-T, což umožnilo konzistentní implementaci napříč dodavateli. Tím byly vyřešeny problémy s kompatibilitou a snadností použití, což usnadnilo růst mobilního internetu a obchodních aplikací v éře 2G/3G.

Podněcována poptávkou po přístupu k mobilním datům začlenila 3GPP specifikace TA pro podporu služeb, jako je fax a vytáčené připojení k síti. Řešila omezení analogových modemů tím, že nabízela digitální spolehlivost a vyšší rychlosti. Vývoj TA odráží širší trend integrace adaptačních funkcí, jako je převod protokolů a zpracování signálu, které byly nezbytné pro spolehlivá data v sítích zaměřených na hlas.

Motivace pro vývoj TA pramenila z poptávky po přístupu k mobilním datům v obchodním i osobním kontextu, podporující aplikace jako e-mail a přenos souborů. Řešením omezení přímých analogových připojení umožnily TA vyšší datové rychlosti a lepší kvalitu v éře 2G/3G, což připravilo cestu pro integrované datové schopnosti v pozdějších návrzích UE.

## Klíčové vlastnosti

- Adaptuje ne-ISDN zařízení pro sítě ISDN/mobilní sítě
- Funguje jako zařízení pro ukončení datového okruhu (DCE)
- Podporuje převod protokolů (např. RS-232 na ISDN)
- Umožňuje vytáčené datové služby v GSM/UMTS
- Konfigurovatelný pomocí AT příkazů (3GPP TS 27.007)
- Umožňuje fyzickou konektivitu prostřednictvím rozhraní jako PCMCIA

## Související pojmy

- [DCE – Data Circuit-terminating Equipment](/mobilnisite/slovnik/dce/)
- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.766** (Rel-13) — Network-Assisted Interference Cancellation for UMTS
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 27.007** (Rel-19) — AT Command Set for UE
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [TA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ta/)
