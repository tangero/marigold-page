---
slug: "iw-mgw"
url: "/mobilnisite/slovnik/iw-mgw/"
type: "slovnik"
title: "IW-MGW – Interworking Media Gateway Function"
date: 2025-01-01
abbr: "IW-MGW"
fullName: "Interworking Media Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/iw-mgw/"
summary: "Funkce Interworking Media Gateway Function (IW-MGW) je síťový prvek, který umožňuje převod médií a jejich přenos mezi sítěmi s přepojováním okruhů (CS) (jako je starší hlasová síť 2G/3G) a paketovými"
---

IW-MGW je síťová funkce zajišťující převod médií a jejich přenos mezi sítěmi s přepojováním okruhů (circuit-switched) a paketovými IP sítěmi, která obstarává překódování a řízení přenosových kanálů pro bezproblémové propojení služeb.

## Popis

Funkce Interworking Media Gateway Function (IW-MGW) je klíčová funkční entita v architektuře IP Multimedia Subsystem (IMS) a jádra sítě dle 3GPP, specifikovaná především v TS 29.164. Jejím hlavním úkolem je fungovat jako most pro přenos médií v uživatelské rovině mezi různými síťovými doménami s nekompatibilními přenosovými a kódovacími formáty. Konkrétně zprostředkovává propojení mezi starší doménou s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), která pro hlas využívá přenosové kanály založené na časové multiplexaci ([TDM](/mobilnisite/slovnik/tdm/)) nebo [ATM](/mobilnisite/slovnik/atm/), a moderní paketovou IP doménou ([PS](/mobilnisite/slovnik/ps/)), jako je IMS, která využívá Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) přes IP. IW-MGW je typicky řízena funkcí Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) za použití protokolů jako H.248 (Megaco).

Z architektonického hlediska obsahuje IW-MGW koncové body pro přenosové kanály jak CS, tak PS. Na straně CS se připojuje k starším sítím [MSC](/mobilnisite/slovnik/msc/) nebo [GMSC](/mobilnisite/slovnik/gmsc/) přes TDM (E1/T1) nebo ATM rozhraní. Na straně PS se připojuje k IMS nebo jiným IP sítím přes IP rozhraní. Její jádrové zpracování spočívá v manipulaci s datovými toky médií: provádí překódování mezi různými hlasovými kodeky (např. z kodeku GSM Full Rate používaného v CS na kodek AMR-WB používaný v IMS), potlačení ozvěn, generování a detekci tónů a v některých případech i překódování videa. Také zajišťuje převod na transportní vrstvě, demultiplexaci TDM časových slotů na jednotlivé RTP toky a naopak.

V typickém průběhu hovoru z CS uživatelského zařízení (UE) do IMS UE přijme MGCF signalizaci CS, vyhodnotí potřebu propojení a přes H.248 dá IW-MGW pokyn k vytvoření kontextu. IW-MGW alokuje prostředky, naváže spojení CS přenosového kanálu k MSC a IP přenosového kanálu směrem k jádru IMS (např. k P-CSCF nebo jiné MGW). Poté nepřetržitě zpracovává obousměrný datový tok médií a v reálném čase provádí veškeré potřebné převody kodeků a adaptace přenosu. To umožňuje účastníkům v legacy sítích transparentně komunikovat s účastníky v VoIP nebo IMS sítích, což je klíčová schopnost během fází migrace sítě.

## K čemu slouží

IW-MGW byla vytvořena, aby vyřešila zásadní problém vývoje telekomunikačních sítí: jak zachovat bezproblémovou kontinuitu hlasových a multimediálních služeb během přechodu ze starších sítí s přepojováním okruhů (CS) (2G GSM, 3G UMTS CS) na plně IP paketové sítě (PS), jako je IMS a nakonec 5G Core. Bez funkce pro propojení by byli účastníci ve starých a nových sítích izolovaní a nemohli by spolu komunikovat, což je komerčně i prakticky nepřijatelné. IW-MGW poskytuje nezbytný "klih" v uživatelské rovině, který umožňuje této různorodé síťové infrastruktuře koexistovat a vzájemně spolupracovat během potenciálně dlouhého přechodného období.

Historicky byly telekomunikační sítě pro hlas postaveny na TDM technologii. Vzestup internetu a potřeba konvergovaných multimediálních služeb vedly k vývoji IMS jako plně IP platformy pro poskytování služeb. IW-MGW spolu s funkcí MGCF pro propojení signalizace řešily omezení okamžitého "big bang" přechodu. Umožnila operátorům postupně nasazovat IMS pro nové služby a účastníky, zatímco jejich rozsáhlá stávající základna starších koncových zařízení a ústředen s přepojováním okruhů nadále fungovala. Vyřešila technickou výzvu převodu médií citlivých na zpoždění v reálném čase mezi zásadně odlišnými přenosovými technologiemi (synchronní TDM vs. asynchronní paketový IP) a mezi různými, často nekompatibilními, hlasovými kompresními kodeky používanými v jednotlivých doménách.

## Klíčové vlastnosti

- Překódování médií mezi kodeky pro sítě s přepojováním okruhů a paketovými sítěmi (např. GSM/UMTS kodeky na AMR, EVS)
- Adaptace přenosu mezi TDM/ATM přenosovými kanály a IP/RTP/UDP přenosovými kanály
- Zpracování pro potlačení ozvěn a vylepšení kvality hlasu
- Podpora generování tónů (např. obsazovací, vyzváněcí) a jejich detekce (DTMF)
- Řízení pomocí protokolu H.248 (Megaco) z funkce MGCF
- Správa a alokace prostředků přenosových kanálů pro souběžné mediální relace

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)

## Definující specifikace

- **TS 29.164** (Rel-19) — CS-LTE Interworking with SIP-I, BICC, ISUP

---

📖 **Anglický originál a plná specifikace:** [IW-MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/iw-mgw/)
