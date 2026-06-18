---
slug: "tmgw"
url: "/mobilnisite/slovnik/tmgw/"
type: "slovnik"
title: "TMGW – Trunking Media Gateway"
date: 2025-01-01
abbr: "TMGW"
fullName: "Trunking Media Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/tmgw/"
summary: "Síťový prvek, který provádí převod a zpracování médií mezi okruhově přepínanými (CS) trunky (jako PSTN/ISDN) a paketově přepínanými (PS) IP sítěmi (jako IMS). Je klíčový pro zajištění hlasových a mult"
---

TMGW je síťový prvek, který provádí převod a zpracování médií mezi okruhově přepínanými trunky a paketově přepínanými IP sítěmi, zajišťuje funkce jako překódování a potlačení ozvěn.

## Popis

Trunking Media Gateway (TMGW) je klíčová funkční entita v architektuře 3GPP IP Multimedia Subsystem (IMS), definovaná speciálně pro trunkingové scénáře. Funguje jako uzel v rovině médií, který propojuje tradiční okruhově přepínané trunky založené na časovém multiplexu ([TDM](/mobilnisite/slovnik/tdm/)), jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) nebo [ISDN](/mobilnisite/slovnik/isdn/), s paketově přepínaným IP jádrem IMS. Jejím hlavním úkolem je převádět mediální toky a přenosové kanály mezi těmito odlišnými síťovými doménami. Z architektonického hlediska je TMGW řízen funkcí Media Gateway Controller Function ([MGCF](/mobilnisite/slovnik/mgcf/)) prostřednictvím standardizovaných řídicích protokolů, jako je H.248 (Megaco), jak je definováno v 3GPP TS 29.332. MGCF zpracovává signalizaci relace (např. [SIP](/mobilnisite/slovnik/sip/)/[SDP](/mobilnisite/slovnik/sdp/)), zatímco TMGW provádí její příkazy pro zpracování médií.

Z funkční perspektivy TMGW provádí několik klíčových úloh zpracování médií. Na straně [CS](/mobilnisite/slovnik/cs/) ukončuje TDM trunkové linky (např. rozhraní E1/T1) a na straně IMS ukončuje [RTP](/mobilnisite/slovnik/rtp/)/UDP/IP toky. Mezi základní zpracování patří překódování mezi hlasovými kodeky používanými v doméně CS (jako G.711 A-law/μ-law) a těmi používanými v doméně PS (jako AMR, AMR-WB nebo EVS). Dále implementuje nezbytné funkce kvality hlasu, jako je potlačení ozvěn, detekce hlasové aktivity (VAD), generování komfortního šumu (CNG) a maskování ztrát paketů (PLC). TMGW také zajišťuje funkce řízení přenosových kanálů, včetně navázání, změny a uvolnění mediálních spojení podle pokynů MGCF.

V rámci širší architektury IMS pro propojení TMGW spolupracuje s MGCF a Signalizační bránou (SGW) a poskytuje tak kompletní řešení pro propojení s PSTN/CS. SGW překládá signalizaci nižších vrstev (např. MTP) na SIGTRAN (např. M3UA) přes IP, zatímco MGCF překládá signalizaci řízení hovorů vyšších vrstev (např. ISUP/BICC na SIP). Role TMGW je čistě v uživatelské rovině, zajišťuje správné navázání a zpracování mediální cesty. Toto jasné oddělení řídicí (MGCF) a mediální (TMGW) roviny je v souladu s principy IMS, umožňuje škálovatelnost, nezávislý vývoj a efektivní využití zdrojů. Specifikace jako TS 29.412 a TS 29.424 detailně popisují rozhraní založená na protokolu Diameter (např. Rf/Ro) používaná pro offline a online účtování zdrojů mediální brány, čímž integrují TMGW do ekosystému účtování a řízení politik operátora.

## K čemu slouží

TMGW byl vytvořen k řešení základního problému vzájemného propojení mezi rozsáhlou stávající infrastrukturou okruhově přepínaných telefonních sítí a vznikajícími, flexibilnějšími IP sítěmi IMS. Před IMS se mobilní a pevné sítě silně spoléhaly na monolitické přepínače, které integrovaly jak signalizační, tak mediální funkce. Přechod na plně IP sítě vyžadoval způsob, jak využít stávající investice do PSTN/ISDN a zároveň migrovat služby na paketové jádro. TMGW jako součást dekomponované architektury brány to řeší tím, že poskytuje specializovaný uzel pro zpracování médií, který lze nezávisle řídit pomocí standardizovaných protokolů.

Tento přístup vyřešil významná omezení starších řešení bran, která byla často proprietární, vertikálně integrovaná a obtížně škálovatelná. Oddělením mediální brány od jejího kontroléru (MGCF) umožnilo 3GPP síťovým operátorům pořizovat tyto komponenty od různých dodavatelů, což podpořilo konkurenci a inovace. Také umožnilo efektivnější sdružování zdrojů; farma TMGW mohla být sdílena a dynamicky přidělována více MGCF na základě zatížení provozem, což zlepšilo celkové využití sítě a odolnost. Vytvoření TMGW bylo tedy motivováno potřebou standardizované, škálovatelné a nákladově efektivní migrační cesty od staršího okruhově přepínaného hlasového trunkingu k plně IP budoucnosti, kterou představuje IMS, a zajištění kontinuity služeb a kvality během přechodu.

## Klíčové vlastnosti

- Převod médií mezi TDM okruhy a RTP/IP toky
- Překódování mezi staršími (např. G.711) a IMS/3GPP (např. AMR) kodeky
- Integrované vylepšení kvality hlasu (potlačení ozvěn, VAD, PLC)
- Řízení prostřednictvím protokolu H.248 (Megaco) z MGCF
- Podpora rozhraní pro účtování založených na protokolu Diameter (Rf/Ro)
- Škálovatelná, sdružená architektura nezávislá na signalizačním kontroléru

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.412** (Rel-8) — Trunking Gateway Control Procedures
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways

---

📖 **Anglický originál a plná specifikace:** [TMGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/tmgw/)
