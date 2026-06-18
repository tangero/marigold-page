---
slug: "srvcc"
url: "/mobilnisite/slovnik/srvcc/"
type: "slovnik"
title: "SRVCC – Single Radio Voice Call Continuity"
date: 2025-01-01
abbr: "SRVCC"
fullName: "Single Radio Voice Call Continuity"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/srvcc/"
summary: "SRVCC je funkce 3GPP umožňující plynulý handover hovoru z LTE/5G NR (pomocí VoLTE nebo VoNR) do starších okruhově přepínaných (CS) sítí 2G/3G, když se uživatel pohybuje mimo pokrytí LTE/5G. Zajišťuje"
---

SRVCC je funkce 3GPP umožňující plynulý předání (handover) hovoru z LTE nebo 5G do starších okruhově přepínaných sítí 2G/3G, aby se zabránilo přerušení při pohybu mimo pokrytí.

## Popis

Single Radio Voice Call Continuity (SRVCC) je komplexní procedura mobility definovaná 3GPP pro zachování aktivního hlasového hovoru, když se User Equipment (UE) přesune ze sítě s přístupem s paketovým přepínáním ([PS](/mobilnisite/slovnik/ps/)) LTE nebo 5G NR, která podporuje hlas přes IP (VoIP) prostřednictvím IMS (VoLTE/VoNR), do starší okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) sítě, jako je [GERAN](/mobilnisite/slovnik/geran/), [UTRAN](/mobilnisite/slovnik/utran/) nebo 1xRTT. Hlavní výzva, kterou SRVCC řeší, spočívá v tom, že UE má pouze jeden rádiový transceiver, což znamená, že nemůže současně udržovat VoIP hovor v PS režimu na LTE a provádět měření nebo signalizaci v cílové CS síti. Proceduru orchestruje síť a vyžaduje těsnou koordinaci mezi Evolved Packet Core (EPC) nebo 5G Core (5GC), IMS a okruhově přepínanou jádrovou sítí ([MSC](/mobilnisite/slovnik/msc/)).

Z architektonického hlediska SRVCC zavádí několik klíčových funkčních entit a referenčních bodů. V EPC hraje centrální roli [MME](/mobilnisite/slovnik/mme/). Ta přijímá od eNodeB měřicí zprávy indikující zhoršující se sílu signálu LTE a dostupnost vhodné cílové CS buňky. MME pak zahájí proceduru SRVCC odesláním zprávy SRVCC PS to CS Request k MSC Serveru (rozšířenému pro SRVCC, často označovanému jako MSC Server enhanced for SRVCC nebo eMSC). Tento MSC Server komunikuje se sítí IMS prostřednictvím rozhraní Sv k SRVCC Application Server (SRVCC [AS](/mobilnisite/slovnik/as/)) nebo k Service Centralization and Continuity Application Server ([SCC](/mobilnisite/slovnik/scc/) AS) v IMS. SCC AS je kotvícím bodem pro relaci hlasového hovoru v IMS, což jí umožňuje manipulovat s mediální cestou.

Během provádění handoveru MSC Server provede proceduru CS handoveru s cílovým BSS/RNS a zřídí CS přenosovou cestu. Současně signalizuje SCC AS přes rozhraní Sv (nebo pomocí propojení ISUP/SIP), aby převedla IMS větev hovoru z PS přístupu na nově zřízený CS přístup. SCC AS aktualizuje mediální cestu na vzdálené straně tak, aby směřovala k Media Gateway (MGW) CS sítě. Z pohledu UE přijme příkaz k handoveru ze sítě LTE, naladí svůj jediný vysílač-přijímač na cílovou CS frekvenci/kanál a přistoupí k CS síti, kde odešle zprávu o dokončení handoveru. Hlasová média jsou poté plynule přepnuta z VoIP paketového toku přes LTE na CS hlasový kanál. Pro volající stranu je tento přechod téměř nepostřehnutelný, s pouze velmi krátkým potenciálním přerušením zvuku.

SRVCC také zahrnuje varianty, jako je enhanced SRVCC (eSRVCC), zavedená ve 3GPP Release 10, která výrazně snižuje dobu přerušení při handoveru tím, že kotví hovor lokálně v MSC a IMS architektuře obsluhující sítě, namísto zapojení SCC AS domovské sítě pro aktualizaci médií. Reverse SRVCC (rSRVCC) řeší mobilitu z CS zpět na LTE/5G. V 5G systémech jsou principy SRVCC rozšířeny pro handover z 5G NR (VoNR) na EPS (VoLTE) nebo na UTRAN/GERAN, přičemž AMF a rozhraní N26 (pokud je přítomno) hrají role analogické MME a rozhraní Sv.

## K čemu slouží

SRVCC bylo vytvořeno k řešení kritického obchodního a technického problému během počátečního zavádění sítí 4G LTE. LTE bylo navrženo jako čistě paketově přepínaná (PS) síť optimalizovaná pro vysokorychlostní data, bez nativní okruhově přepínané (CS) domény pro hlasovou telefonii. Řešením průmyslu pro hlas přes LTE bylo použití Voice over IP (VoIP) prostřednictvím IP Multimedia Subsystem (IMS), známé jako VoLTE. Pokrytí LTE však při spuštění nebylo všudypřítomné a často zaostávalo za rozsáhlým pokrytím CS sítí 2G a 3G. Bez mechanismu kontinuity by se VoLTE hovor při pohybu uživatele mimo pokrytí LTE jednoduše přerušil, což by vedlo ke špatné uživatelské zkušenosti, která je pro primární telefonní službu nepřijatelná.

Hlavní motivací bylo umožnit mobilním operátorům nasadit LTE jako datově optimalizovanou síť a zároveň využít jejich stávající, rozšířené CS sítě pro kontinuitu hlasové služby. To umožnilo postupnou migrační strategii. Operátoři mohli spustit LTE pro vysokorychlostní data a VoLTE v hustě obydlených městských oblastech, zatímco se mohli spolehnout na SRVCC pro poskytnutí plynulé hlasové služby v předměstských a venkovských oblastech stále pokrytých pouze 2G/3G. Chránilo to podstatné investice operátorů do CS infrastruktury a kmitočtů a zároveň splňovalo očekávání zákazníků týkající se spolehlivých, nepřerušovaných hlasových hovorů.

Před SRVCC mohla zařízení s duálním rádiem použít Circuit Switched Fallback (CSFB) k uskutečnění nebo přijetí hovorů dočasným přepadem do sítě 2G/3G, to však nebylo vhodné pro předání aktivního hovoru. SRVCC konkrétně řešilo scénář kontinuity aktivního hovoru pro zařízení s jedním rádiem, která jsou kvůli nákladům a složitosti normou. Bylo to základní umožňující technologie pro komerční úspěch VoLTE, protože zaručovala, že kvalita a spolehlivost hlasové služby na LTE bude přinejmenším stejně dobrá jako na starších sítích, čímž odstraňovala hlavní překážku pro přijetí LTE pro hlas.

## Klíčové vlastnosti

- Umožňuje plynulý handover aktivního hlasového hovoru založeného na IMS (VoLTE/VoNR) do starší okruhově přepínané (2G/3G) sítě.
- Navrženo pro User Equipment s jedním rádiovým transceiverem, přechod rádia je řízen koordinací v síti.
- Zahrnuje koordinaci mezi MME/AMF, MSC Serverem (rozšířeným pro SRVCC) a IMS SCC Application Server.
- Využívá referenční bod Sv mezi MME a MSC Serverem pro přístup E-UTRAN a analogickou signalizaci v 5GS.
- Podporuje handover z E-UTRAN na UTRAN/GERAN/1xRTT a z NG-RAN na UTRAN/GERAN.
- Zahrnuje enhanced SRVCC (eSRVCC) pro snížení doby přerušení při handoveru lokalizací kotvícího bodu médií.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 23.272** (Rel-19) — CS Fallback in EPS
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.885** (Rel-11) — SRVCC Feasibility Study for Reverse Handover
- **TS 23.886** (Rel-10) — Feasibility Study on Video SRVCC
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 25.306** (Rel-19) — UE Radio Access Capabilities Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [SRVCC na 3GPP Explorer](https://3gpp-explorer.com/glossary/srvcc/)
