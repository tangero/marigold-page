---
slug: "psi"
url: "/mobilnisite/slovnik/psi/"
type: "slovnik"
title: "PSI – Provide Subscriber Information"
date: 2026-01-01
abbr: "PSI"
fullName: "Provide Subscriber Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/psi/"
summary: "Provide Subscriber Information (PSI, poskytnutí informací o účastníkovi) je služba jádra sítě, která autorizované entitě (jako je Gateway Mobile Location Centre - GMLC) umožňuje vyžádat si a přijmout"
---

PSI je služba jádra sítě, která autorizované entitě umožňuje vyžádat si data o účastníkovi z HSS nebo HLR pro služby založené na poloze, zákonné odposlechy a další přidané služby.

## Popis

Provide Subscriber Information (PSI, poskytnutí informací o účastníkovi) je standardizovaná služba v rámci architektury jádra sítě 3GPP, definovaná jako součást protokolu Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) a později rozhraní založených na Diameteru Sh a S6a/S6d. Jedná se o proceduru iniciovanou sítí, při které dotazující uzel, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)) nebo uzel pro zákonný odposlech, dotazuje domovskou databázi účastníka – Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) ve 2G/3G nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) v 4G/5G – aby získal konkrétní informace o účastníkovi.

Procedura zahrnuje dobře definovanou výměnu zpráv typu požadavek/odpověď. Dotazující entita odešle zprávu PSI (např. MAP_PSI nebo Diameter PSI-Request) obsahující identifikátor účastníka (jako [MSISDN](/mobilnisite/slovnik/msisdn/) nebo [IMSI](/mobilnisite/slovnik/imsi/)) a indikaci požadovaných informací. HSS/HLR požadavek zpracuje, což typicky zahrnuje ověření autorizace žadatele vůči nastavením soukromí účastníka a regulačním požadavkům (např. pro služby polohy). Po úspěšném autorizačním řízení HSS/HLR odpoví zprávou PSI-Answer obsahující požadovaná data. Tato data mohou zahrnovat široké spektrum informací: aktuální obsluhující síťový uzel účastníka ([MSC](/mobilnisite/slovnik/msc/), SGSN, MME, AMF), stav účastníka (např. připojený, odpojený), informace o poloze (pokud jsou dostupné a povolené), předplacené služby a mapování IMSI-MSISDN.

Klíčovými komponentami v architektuře jsou Dotazující uzel (klient služby), HSS/HLR (server uchovávající data) a příslušná signalizační rozhraní. Pro 4G/5G je primárním rozhraním S6a (mezi MME a HSS) a Sh (mezi Application Server/SCEF a HSS) využívající protokol Diameter. HSS funguje jako centrální úložiště a bod pro vynucování politik, zajišťující, že data účastníka jsou poskytnuta pouze autorizovaným síťovým funkcím na základě souhlasu účastníka a síťových politik.

Role PSI je klíčová pro umožnění mnoha přidaných a regulačních služeb. Je základní procedurou pro síťové služby polohy, umožňující GMLC zjistit, který Mobility Management Entity (MME) nebo Access and Mobility Management Function (AMF) obsluhuje cílové UE, než vydá požadavek na polohu. Používá se také pro obnovu dat účastníka v případě selhání MME, podporu směrování doručování SMS, usnadnění zřizování zákonných odposlechů a umožnění vystavení schopností služeb pro aplikace třetích stran. Její vývoj napříč releasy znamenal adaptaci z okruhově spínaného MAP na paketově spínaný Diameter a její integraci s novými síťovými funkcemi jako SCEF a Network Exposure Function (NEF) v 5G, čímž si udržela pozici základní služby pro přístup k datům účastníka.

## K čemu slouží

Služba PSI byla vytvořena, aby řešila základní potřebu autorizovaných síťových entit přistupovat k centralizovaným informacím o účastníkovi standardizovaným, bezpečným a řízeným způsobem. V raných mobilních sítích různé síťové uzly (jako přepínače a servisní platformy) potřebovaly data účastníka k výkonu svých funkcí, ale ad-hoc metody sdílení těchto dat byly neefektivní a nejisté. PSI poskytla jednotný, protokolem založený mechanismus pro dotazování se na hlavní databázi účastníků (HLR), čímž řešila problémy související se spouštěním služeb, směrováním (např. pro SMS nebo hovory) a rodícím se odvětvím služeb založených na poloze.

Historická motivace vychází z oddělení databáze účastníků (HLR) od přepínacích funkcí v architektuře GSM. Toto oddělení vytvořilo potřebu signalizační služby, která by je propojila. PSI, jako součást protokolu MAP, byla jednou z klíčových služeb umožňujících tuto distribuovanou architekturu. Vyřešila omezení plynoucí z izolovaného nebo nekonzistentně replikovaného ukládání dat účastníka napříč síťovými prvky. Centralizací dat v HLR a poskytnutím řízeného přístupu prostřednictvím PSI mohli operátoři sítí zajistit konzistenci dat, zjednodušit nasazování služeb a implementovat kontrolu soukromí účastníků.

Jak se sítě vyvíjely přes 3G, 4G a 5G, účel PSI se rozšířil. Stala se nezbytnou pro umožnění regulačních služeb, jako jsou zákonné odposlechy, kde orgány vyžadují informace o připojení k síti. Snaha o vystavení služeb a síťových API pro vývojáře třetích stran dále využívala PSI (prostřednictvím SCEF/NEF) k poskytování informací o stavu účastníka autorizovaným aplikacím, což podněcovalo vznik nových služeb. PSI tak přetrvává jako klíčový enabler, vyvíjející se z nástroje pro základní síťové operace na klíčovou komponentu v doručování služeb, zabezpečení a inovacích napříč celým vývojem systému 3GPP.

## Klíčové vlastnosti

- Standardizovaná procedura pro dotazování dat účastníka v HSS/HLR
- Podporuje více typů informací: poloha, stav, obsluhující uzel, mapování identit účastníka
- Zahrnuje vestavěné mechanismy autorizace a kontroly soukromí
- Funguje napříč více generacemi protokolů (MAP pro 2G/3G, Diameter pro 4G/5G)
- Základní pro služby založené na poloze, směrování SMS a zákonné odposlechy
- Umožňuje obnovu dat účastníka a kontinuitu služeb během výpadků sítě

## Související pojmy

- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)

## Definující specifikace

- **TS 23.079** (Rel-19) — Support of Optimal Routeing (SOR) Phase 1
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.206** (Rel-7) — Voice Call Continuity (VCC) Functional Architecture
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.141** (Rel-19) — Presence Service Protocol Details
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- … a dalších 29 specifikací

---

📖 **Anglický originál a plná specifikace:** [PSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/psi/)
