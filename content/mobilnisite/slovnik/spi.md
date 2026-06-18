---
slug: "spi"
url: "/mobilnisite/slovnik/spi/"
type: "slovnik"
title: "SPI – Service Provider Identification"
date: 2025-01-01
abbr: "SPI"
fullName: "Service Provider Identification"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/spi/"
summary: "Jedinečný identifikátor používaný v systémech 3GPP k rozlišení subjektu, který poskytuje službu koncovému uživateli (např. MNO, MVNO nebo agregátor služeb). Je klíčový pro diferenciaci služeb, účtován"
---

SPI je jedinečný identifikátor používaný v systémech 3GPP k rozlišení poskytovatele služeb, který umožňuje diferenciaci služeb, účtování, vynucování politik a aplikaci specifických pravidel na základě tohoto poskytovatele.

## Popis

Service Provider Identification (SPI) je parametr v systémech 3GPP, který jednoznačně identifikuje poskytovatele konkrétní služby nebo souboru služeb pro uživatele. Odlišuje se od identifikátorů účastníků, jako je [IMSI](/mobilnisite/slovnik/imsi/) nebo [MSISDN](/mobilnisite/slovnik/msisdn/). Síťové funkce používají SPI k určení, které zásady, pravidla účtování a zacházení s kvalitou služeb (QoS) mají být aplikovány pro danou datovou relaci nebo tok služeb. Je klíčovým prvkem pro vytváření sítí s povědomím o službách.

Z architektonického hlediska je SPI často konfigurován v profilu předplatného uživatele uloženém v [HSS](/mobilnisite/slovnik/hss/) (pro paketové jádro) nebo [HLR](/mobilnisite/slovnik/hlr/). Při vytváření relace, jako je připojení [PDN](/mobilnisite/slovnik/pdn/) v EPS nebo [PDU](/mobilnisite/slovnik/pdu/) relace v 5GS, příslušný síťový uzel (např. [MME](/mobilnisite/slovnik/mme/), [SMF](/mobilnisite/slovnik/smf/)) získá SPI spolu s dalšími údaji o předplatném. Tento SPI je pak předán funkcím řízení politik a účtování, jako je PCRF (ve 4G) nebo PCF (v 5G). PCRF/PCF použije SPI v kombinaci s dalšími parametry (např. APN nebo DNN) k výběru příslušných pravidel Policy and Charging Control (PCC). Tato pravidla určují aspekty jako omezení šířky pásma, identifikátory třídy kvality služeb (QCI/5QI) a metody účtování specifické pro nabídku daného poskytovatele služeb.

Jak to funguje v praxi: MVNO (virtuální mobilní operátor) pronajímající si kapacitu od MNO (mobilního síťového operátora) bude mít svůj vlastní jedinečný SPI. Když se účastník MVNO připojí k síti, systém politik MNO identifikuje SPI spojený s profilem tohoto účastníka. Poté může aplikovat jinou sadu politik (např. prahové hodnoty pro omezení rychlosti, povolené služby) ve srovnání s vlastními přímými účastníky MNO, i když obě skupiny používají stejnou fyzickou rádiovou infrastrukturu. To hostitelskému MNO umožňuje nabízet diferencované velkoobchodní služby. SPI se také používá ve scénářích směrování roamingu k identifikaci domácího poskytovatele služeb roamingového uživatele.

## K čemu slouží

SPI existuje pro umožnění diferenciace služeb a víceklientského provozu ve sdílených síťových infrastrukturách. Řeší základní problém, kdy jedna fyzická síť (např. RAN a jádro MNO) potřebuje hostit více logických poskytovatelů služeb (jako jsou MVNO, podnikoví zákazníci nebo poskytovatelé IoT služeb) a zacházet s jejich provozem odlišně podle komerčních dohod. Bez SPI by síť mohla aplikovat politiky pouze na základě identity účastníka nebo APN, což je nedostatečné pro složité velkoobchodní modely a modely agregace služeb.

Historicky, jak se mobilní trhy stávaly konkurenčnějšími, regulátoři a komerční tlaky vedly k vzestupu MVNO. To vytvořilo technický požadavek na hostitelského MNO, aby identifikoval, který subjekt je za službu účastníka konečně odpovědný. SPI, zavedený ve 3GPP Release 99, tuto schopnost poskytl. Motivací byla potřeba flexibilního řízení politik a účtování, která se stávala stále důležitější s příchodem paketových datových služeb (GPRS), kde byly úrovně služeb a modely účtování rozmanitější než u prostých hlasových hovorů.

Odstraňuje omezení starších sítí, které byly v podstatě jednoklientské. SPI umožňuje oddělení poskytování služeb od provozu sítě. To umožňuje nové obchodní modely, například kdy poskytovatel IoT platformy (identifikovaný SPI) nabízí konektivitu prostřednictvím více MNO, přičemž MNO jednotně aplikují specifické politiky této platformy. Je to základní kámen pro efektivní a automatizované poskytování služeb v moderních, softwarově definovaných mobilních sítích.

## Klíčové vlastnosti

- Jednoznačně identifikuje subjekt poskytující službu koncovému uživateli
- Používá se jako klíčový vstup pro výběr pravidel Policy and Charging Control (PCC)
- Umožňuje diferencované zacházení s provozem pro MVNO a agregátory služeb
- Konfiguruje se v profilech účastníků v HSS/HLR
- Podporuje víceklientský provoz a velkoobchodní obchodní modely
- Kritický pro sítě s povědomím o službách a směrování roamingu

## Související pojmy

- [MVNO – Mobile Virtual Network Operator](/mobilnisite/slovnik/mvno/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 31.114** (Rel-8) — USAT Interpreter Transmission Protocol
- **TS 31.801** (Rel-15) — Requirements for Secure Platform for 3GPP Apps
- **TS 33.204** (Rel-19) — TCAP Security (TCAPsec) Stage 2 Specification
- **TS 33.210** (Rel-19) — UMTS Security for IP Networks
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility

---

📖 **Anglický originál a plná specifikace:** [SPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/spi/)
