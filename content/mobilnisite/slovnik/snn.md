---
slug: "snn"
url: "/mobilnisite/slovnik/snn/"
type: "slovnik"
title: "SNN – Serving Network Name"
date: 2025-01-01
abbr: "SNN"
fullName: "Serving Network Name"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/snn/"
summary: "Identifikátor sítě používaný v systémech 5G pro jednoznačné pojmenování sítě poskytující služby. Jde o klíčový parametr v autentizačních a bezpečnostních procedurách, odvozený z Public Land Mobile Net"
---

SNN je Serving Network Name, jedinečný identifikátor sítě 5G, která poskytuje služby, odvozený z PLMN ID a volitelně z NID, používaný jako klíčový parametr v autentizačních a bezpečnostních procedurách.

## Popis

Serving Network Name (SNN) je klíčový identifikátor v systému 5G (5GS) definovaný ve specifikacích 3GPP Release 15 a novějších. Slouží jako čitelný název pro člověka i strojově zpracovatelný název pro síť, která aktuálně obsluhuje uživatelské zařízení (UE). Primárním účelem SNN je poskytnout jednoznačný identifikátor pro síť poskytující služby během autentizace a procedur odvozování bezpečnostních klíčů, což zajišťuje, že bezpečnostní kontexty jsou vázány ke správné síti.

Z architektonického hlediska je SNN vytvořen a používán jádrem sítě, konkrétně funkcí Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a UE. Je odvozen ze základních identifikátorů sítě. Pro veřejnou síť je SNN typicky konstruován jako "5G:mnc<[MNC](/mobilnisite/slovnik/mnc/)>.mcc<[MCC](/mobilnisite/slovnik/mcc/)>.3gppnetwork.org", kde MNC a MCC jsou Mobile Network Code a Mobile Country Code z [PLMN](/mobilnisite/slovnik/plmn/) ID. Pro neveřejnou síť ([NPN](/mobilnisite/slovnik/npn/)) může SNN navíc zahrnovat Network Identifier ([NID](/mobilnisite/slovnik/nid/)) ve formátu "5G:mnc<MNC>.mcc<MCC>.nid<NID>.3gppnetwork.org". Tato struktura zajišťuje globální jedinečnost.

Během procedur 5G Authentication and Key Agreement (5G-AKA) nebo procedur založených na Extensible Authentication Protocol ([EAP](/mobilnisite/slovnik/eap/)) je SNN zasílán ze sítě do UE. UE i AUSF používají tento SNN jako vstupní parametr (spolu s dalšími hodnotami, jako je Subscription Permanent Identifier ([SUPI](/mobilnisite/slovnik/supi/))) do funkcí pro odvozování klíčů. To váže vygenerované bezpečnostní klíče (jako K_AUSF, K_SEAF) konkrétně k tomuto názvu sítě poskytující služby. Tento mechanismus zabraňuje opětovnému použití klíčů v různých sítích a zvyšuje bezpečnost, zejména ve scénářích zahrnujících síťové řezy nebo roaming, tím, že zajišťuje kryptografické oddělení mezi různými kontexty sítě poskytující služby.

## K čemu slouží

SNN byl zaveden s 5G ve Release 15, aby řešil specifické bezpečnostní a identifikační požadavky, které předchozí mechanismy, jako identita Serving Network (SN) používaná v EPS, plně nesplňovaly. V 4G EPS byla identita sítě implicitně odvozena z PLMN ID, ale nebyla vždy explicitně a konzistentně formátována jako pojmenovaný parametr ve všech bezpečnostních procedurách. Rozšířená bezpečnostní architektura 5G vyžadovala robustnější a explicitnější metodu.

Jeho zavedení bylo motivováno potřebou silnější autentizace sítě, podpory nových modelů nasazení sítí, jako jsou Non-Public Networks (NPN), a základními požadavky na síťové řezy. Díky standardizovanému, strukturovanému názvu může systém 5G bezpečněji ukotvit autentizační proces. Řeší problém zajištění, aby klíče vygenerované během autentizace byly jednoznačně svázány s konkrétní sítí (nebo instancí síťového řezu), ke které UE přistupuje, což je zásadní pro prevenci záměny bezpečnostních kontextů, zejména v komplexních prostředích s více operátory, více řezy nebo privátními sítěmi.

## Klíčové vlastnosti

- Jednoznačně identifikuje veřejnou pozemní mobilní síť nebo neveřejnou síť poskytující služby
- Strukturovaný řetězcový formát založený na PLMN ID (MCC, MNC) a volitelném NID
- Povinný parametr v procedurách autentizace a dohody o klíči v 5G
- Používá se jako vstup pro odvození kotvícího bezpečnostního klíče 5G (K_AUSF)
- Podporuje identifikaci síťových řezů a neveřejných sítí (NPN)
- Umožňuje kryptografické oddělení bezpečnostních kontextů mezi různými sítěmi

## Související pojmy

- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [NID – Network Identifier](/mobilnisite/slovnik/nid/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [SNN na 3GPP Explorer](https://3gpp-explorer.com/glossary/snn/)
