---
slug: "mgc"
url: "/mobilnisite/slovnik/mgc/"
type: "slovnik"
title: "MGC – Media Gateway Controller"
date: 2025-01-01
abbr: "MGC"
fullName: "Media Gateway Controller"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mgc/"
summary: "Media Gateway Controller (MGC) je základní prvek jádra sítě v doméně s přepojováním okruhů (CS) dle 3GPP. Řídí jeden nebo více Media Gateway (MGW) pomocí protokolu H.248/MEGACO, zpracovává řízení hovo"
---

MGC (Media Gateway Controller) je základní prvek jádra sítě, který řídí Media Gateway pomocí protokolu H.248 za účelem zpracování signalizace hovorů pro konverzi médií mezi sítěmi s přepojováním okruhů a sítěmi s přepojováním paketů.

## Popis

Media Gateway Controller (MGC) je klíčová entita řídicí roviny v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) jádra sítě 3GPP, navržená speciálně pro oddělení řízení hovorů a přenosu médií. Funguje jako 'mozek' subsystému media gateway, implementuje stavový automat hovoru a provádí logiku řízení hovoru. MGC sám nezpracovává přenos dat uživatelské roviny; místo toho udílí pokyny jednomu nebo více Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)), jak navázat, upravit a uvolnit mediální toky. Toto řízení je vykonáváno prostřednictvím protokolu H.248 (známého také jako [MEGACO](/mobilnisite/slovnik/megaco/)), který definuje vztah typu master-slave, kde MGC je hlavním kontrolérem. Protokol umožňuje MGC nařídit MGW vytvářet kontexty, přidávat terminace (které reprezentují fyzické nebo logické porty) a specifikovat požadované zpracování médií (např. transkódování kodeků, potlačení ozvěn a generování tónů) pro hovor.

Z architektonického hlediska MGC spolupracuje s dalšími signalizačními uzly jádra sítě. Komunikuje s [MSC](/mobilnisite/slovnik/msc/) Serverem nebo [GMSC](/mobilnisite/slovnik/gmsc/) Serverem pomocí rozhraní Nc (typicky založeného na BICC - Bearer Independent Call Control) pro signalizaci řízení hovorů mezi síťovými uzly. Pro správu účastníků a služeb komunikuje s Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo starším Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Jeho primární rolí je řídit mediální cestu pro tradiční telefonní služby (jako jsou hlasové hovory) v síti, která přechází na nebo zahrnuje páteřní sítě s přepojováním paketů (jako je IP Multimedia Subsystem nebo [ATM](/mobilnisite/slovnik/atm/) síť). Převádí signalizaci hovorů vyšší úrovně (např. z ISUP nebo SIP) na konkrétní příkazy pro MGW, aby fyzicky propojil okruh z PSTN/PLMN s paketovým proudem, nebo naopak.

Během provozu, při sestavování hovoru, MGC přijme signalizační zprávu (např. přes BICC). Určí požadované charakteristiky médií, vybere vhodný prostředek MGW a zašle tomuto MGW příkazy H.248, aby rezervoval potřebné terminace a nakonfiguroval mediální tok. MGC spravuje celý životní cyklus mediálního spojení, reaguje na události z MGW (jako jsou faxové tóny nebo detekce DTMF) a podle potřeby spojení během hovoru upravuje (např. pro čekání hovoru nebo konferenční hovor). Toto oddělení řízení a médií, známé jako model dekompozice brány, byl zásadním krokem k architektuře softswitch a umožnil flexibilnější, škálovatelnější a nákladově efektivnější síťové návrhy ve srovnání s monolitickými ústřednami.

## K čemu slouží

MGC byl vytvořen, aby řešil omezení tradičních monolitických telefonních ústředen (jako byla starší MSC), které integrovaly jak logiku řízení hovorů, tak fyzickou přepínací strukturu do jediného, proprietárního a drahého zařízení. Primární motivací bylo umožnit síťovým operátorům vyvíjet jejich hlasové sítě s přepojováním okruhů směrem k infrastrukturám založeným na paketech (jako je IP nebo ATM) bez nutnosti kompletní výměny všech systémů. Dekompozicí ústředny mohli operátoři modernizovat řídicí rovinu (software na standardních serverech) a mediální rovinu (brány) nezávisle, což vedlo ke snížení nákladů, zvýšení škálovatelnosti a rychlejší inovaci služeb.

Historicky, když 3GPP Release 99 definovalo počáteční architekturu UMTS, přijalo tento dekomponovaný model pro jádro sítě. MGC řešil problém vzájemného propojení mezi stávající PSTN/PLMN založenou na časovém multiplexu (TDM) a novými přenosovými sítěmi založenými na paketech. Umožnil operátorům vybudovat jedinou, flexibilní paketovou páteř pro všechny služby (hlas i data) při zachování bezproblémového připojení ke starším systémům. Standardizovaný řídicí protokol H.248 pro MGC byl také klíčový, neboť prolomil závislost na jednom dodavateli tím, že umožnil MGC od jednoho dodavatele řídit MGW od jiného, což podpořilo konkurenci a snížilo náklady.

## Klíčové vlastnosti

- Řídí Media Gateway pomocí standardizovaného protokolu H.248/MEGACO
- Implementuje logiku řízení hovorů a stavové automaty pro služby s přepojováním okruhů
- Spolupracuje s MSC Servery/GMSC Servery prostřednictvím rozhraní Nc založeného na BICC
- Spravuje alokaci a konfiguraci mediálních prostředků (kodeky, potlačení ozvěn, tóny)
- Převádí mezi signalizací s přepojováním okruhů (např. ISUP) a příkazy pro paketová média
- Umožňuje oddělení řídicí roviny a uživatelské roviny (dekompozice brány)

## Definující specifikace

- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 29.205** (Rel-19) — BICC Protocols for Bearer-Independent CS Core Network
- **TS 29.231** (Rel-19) — Application of SIP-I Protocols to CS Core Network
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.412** (Rel-8) — Trunking Gateway Control Procedures
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways

---

📖 **Anglický originál a plná specifikace:** [MGC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgc/)
