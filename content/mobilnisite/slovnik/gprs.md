---
slug: "gprs"
url: "/mobilnisite/slovnik/gprs/"
type: "slovnik"
title: "GPRS – CSI GPRS CAMEL Subscription Information"
date: 2025-01-01
abbr: "GPRS"
fullName: "CSI GPRS CAMEL Subscription Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gprs/"
summary: "CSI GPRS (informace o předplatném CAMEL pro GPRS) je soubor spouštěčů a dat CAMEL uložených v HLR/HSS, který umožňuje inteligentní řízení relací GPRS a paketových dat v reálném čase řídicím bodem služ"
---

GPRS je informace o předplatném CAMEL, která poskytuje spouštěče a data v HLR/HSS, aby umožnila řídicímu bodu služeb inteligentní řízení paketových datových relací v reálném čase pro přizpůsobené operátorské služby.

## Popis

[CSI](/mobilnisite/slovnik/csi/) GPRS, formálně známé jako informace o předplatném [CAMEL](/mobilnisite/slovnik/camel/) pro GPRS, je klíčovou součástí architektury Customised Applications for Mobile networks Enhanced Logic (CAMEL) aplikované na paketově spínané služby. Nejde o samotné jádro sítě GPRS, ale o předplatitelská data a související spouštěče, které umožňují řízení služeb založené na CAMEL pro předplatitelovy relace GPRS. Tyto informace jsou uloženy jako součást profilu předplatitele v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a jsou staženy do Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) při připojení předplatitele k síti.

Data CSI GPRS zahrnují specifické detekční body ([DP](/mobilnisite/slovnik/dp/)), které slouží jako spouštěče během procedury aktivace nebo modifikace kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)). Když SGSN narazí na nakonfigurovaný DP (např. DP PDP Context Establishment), pozastaví běžnou proceduru a odešle zprávu CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) určenému GSM Service Control Point (gsmSCP). Tento gsmSCP, který hostí inteligentní logiku služeb operátora, pak může v reálném čase ovlivnit relaci. Na základě své logiky může gsmSCP nařídit SGSN povolit, zamítnout nebo upravit žádost o PDP kontext. Může také uplatnit specifické instrukce pro účtování, například připojit datovou relaci k online účtovacímu systému založenému na CAMEL pro řízení kreditu v reálném čase, nebo použít funkce řízení přístupu (gating) pro kontrolu povolených IP toků.

Tento mechanismus umožňuje sofistikované, na předplatitele specifické zacházení s datovými službami. Lze jej například použít k implementaci předplacených datových tarifů, kde gsmSCP sleduje objem dat v reálném čase a může relaci ukončit při vyčerpání kreditu. Umožňuje sponzorované datové služby, kde je provoz ke konkrétním aplikačním serverům (APN) účtován nulově. Také umožňuje politiky citlivé na službu, jako je aplikace různých profilů QoS nebo směrování pro různé aplikace iniciované stejným předplatitelem. SGSN funguje jako CAMEL Service Switching Function (gsmSSF) pro GPRS, rozhraním s gsmSCP provádí toto externí řízení.

## K čemu slouží

CSI GPRS bylo vyvinuto za účelem rozšíření schopností inteligentní sítě (IN) architektury CAMEL, původně navržené pro okruhově spínané hovory, do paketově spínané domény GPRS a později datových služeb 3G/4G. Před jeho zavedením bylo řízení a účtování datových relací relativně statické, založené na profilech předplatného v HLR a místních politikách v SGSN/Gateway GPRS Support Node (GGSN). To postrádalo flexibilitu pro interaktivní řízení služeb v reálném čase, vyžadovanou pro inovativní datové nabídky, jako je předplacený internet, účtování založené na obsahu a integrace partnerských služeb.

Jeho vytvoření bylo motivováno komerční potřebou operátorů zavádět pokročilé, přizpůsobitelné datové služby, které by mohly být dynamicky řízeny z centrální platformy s logikou služeb. Vyřešilo problém aplikace komplexní, stavové logiky služeb (jako jsou kontroly výdajových limitů, denní příděl nebo politiky specifické pro aplikaci) na inherentně bezestavové IP datové toky. Využitím zavedené architektury CAMEL poskytlo standardizovaný, mezi dodavateli interoperabilní způsob zavedení inteligentního řízení, což umožnilo nové obchodní modely pro mobilní data v éře 2.5G a 3G. Tvořilo základ pro pozdější architektury Policy and Charging Control (PCC), překlenující propast mezi tradičními IN a plně IP sítěmi.

## Klíčové vlastnosti

- Definuje spouštěče CAMEL pro procedury PDP kontextu GPRS
- Umožňuje interakci v reálném čase mezi SGSN (gsmSSF) a gsmSCP
- Podporuje online účtování založené na CAMEL pro předplacené a datové služby v reálném čase
- Umožňuje gsmSCP ovlivnit aktivaci, modifikaci a ukončení PDP kontextu
- Poskytuje provedení logiky služeb specifické pro předplatitele pro paketové datové relace
- Ukládá se jako součást profilu předplatitele v HLR/HSS

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 22.060** (Rel-19) — GPRS Stage 1 Service Description
- **TS 22.100** (Rel-4) — UMTS Service Requirements Phase 1
- **TS 22.112** (Rel-8) — USAT Gateway System Specification
- **TS 22.228** (Rel-19) — IP Multimedia Service Requirements
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- … a dalších 66 specifikací

---

📖 **Anglický originál a plná specifikace:** [GPRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/gprs/)
