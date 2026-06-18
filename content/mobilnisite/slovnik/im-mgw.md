---
slug: "im-mgw"
url: "/mobilnisite/slovnik/im-mgw/"
type: "slovnik"
title: "IM-MGW – IP Multimedia Media Gateway Function"
date: 2025-01-01
abbr: "IM-MGW"
fullName: "IP Multimedia Media Gateway Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/im-mgw/"
summary: "IM-MGW je mediální brána v rámci IMS, která provádí mediální překlad a zpracování mezi různými typy sítí a kodeky. Umožňuje spolupráci mezi paketově přepínanými sítěmi IMS a okruhově přepínanými sítěm"
---

IM-MGW je mediální brána v rámci IMS, která provádí překlad a zpracování mezi paketově přepínanými a okruhově přepínanými sítěmi a zajišťuje funkce jako je transkódování pro multimediální relace.

## Popis

Funkce IP multimediální mediální brány (IM-MGW) je klíčová funkční entita v architektuře IP multimediální podsystému (IMS) zodpovědná za veškeré zpracování médií v uživatelské rovině. Je řízena funkcí řízení mediální brány ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo v novějších architekturách řadičem multimediálních prostředků ([MRFC](/mobilnisite/slovnik/mrfc/)) za použití protokolů jako H.248 (Megaco). Primární úlohou IM-MGW je poskytovat interoperabilitu mezi paketově přepínanou doménou IMS (používající [RTP](/mobilnisite/slovnik/rtp/)/[RTCP](/mobilnisite/slovnik/rtcp/) přes IP) a staršími okruhově přepínanými sítěmi, jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) nebo starší mobilní sítě (používající přenosové proudy [TDM](/mobilnisite/slovnik/tdm/) nebo [ATM](/mobilnisite/slovnik/atm/)). Nachází se na hranici mezi těmito doménami a v reálném čase převádí mediální proudy.

Funkčně IM-MGW provádí několik klíčových úloh zpracování médií. Základní funkcí je transkódování, které převádí audio a video kodeky mezi různými formáty (např. z [AMR-NB](/mobilnisite/slovnik/amr-nb/) používaného v okruhově přepínaném hovoru na G.711 nebo EVS používané v IMS VoIP hovoru). Dále provádí potlačení ozvěn, generování a detekci tónů (např. DTMF), přehrávání hlášení a podporuje konferenční hovory mísením více mediálních proudů. Pro hovor mezi účastníkem IMS a účastníkem PSTN nastaví MGCF signalizaci hovoru a poté prostřednictvím H.248 nařídí IM-MGW vytvořit kontext s ukončeními: jedno ukončení směřující do sítě IMS (na bázi IP RTP) a druhé směřující do PSTN (TDM časový slot). IM-MGW pak tyto ukončení propojí a provede potřebnou obousměrnou konverzi médií.

Architektonicky je IM-MGW součástí širší rodiny mediálních bran (MGW) v 3GPP, ale je specificky určena pro služby IMS. Rozhraní má k MGCF pro řízení související s hovory, k MRFC pro pokročilé mediální služby jako konferenční hovory a hlášení a k funkci řízení přestupové brány (BGCF) pro rozhodování o směrování. Její vnitřní komponenty zahrnují procesory digitálních signálů (DSP) pro zpracování médií, rozhraní IP sítí a rozhraní starších sítí (např. E1/T1 trunky). Centralizací funkcí zpracování médií umožňuje IM-MGW, aby jádro IMS zůstalo čistě na bázi SIP a nezávislé na podkladové přenosové technologii, což umožňuje bezproblémové poskytování služeb napříč heterogenními sítěmi.

## K čemu slouží

IM-MGW byla vytvořena, aby vyřešila základní problém spolupráce mezi novou, plně IP sítí IMS zavedenou ve verzi 5 a rozsáhlou instalovanou základnou starších okruhově přepínaných sítí (PSTN a 2G/3G PLMN). Koncové body IMS komunikují pomocí SIP a RTP přes IP, zatímco starší sítě používají ISUP/TDM nebo jiné okruhově přepínané protokoly. Bez mediální brány by byly hlasové a video hovory mezi těmito doménami nemožné, což by vážně omezilo přijetí IMS.

Její vytvoření bylo motivováno potřebou plynulé, postupné migrace na IMS. Operátoři nemohli okamžitě nahradit všechny starší ústředny a koncová zařízení. IM-MGW, řízená MGCF, poskytla most, který umožnil účastníkům IMS volat komukoli v PSTN a naopak, čímž chránila stávající investice a zajišťovala kontinuitu služeb. Řešila omezení dřívějších VoIP bran, které nebyly integrovány s řídicí architekturou IMS (CSCFs, HSS). IM-MGW je specificky navržena tak, aby byla řízena standardními protokoly (H.248) řídicími funkcemi IMS, což umožňuje sofistikované propojování služeb a manipulaci s médii na základě politik.

Dále IM-MGW vyřešila problém požadavků na mediální prostředky v rámci IMS. I pro čistě IMS-IMS hovory služby jako konferenční hovory, transkódování mezi různými IMS kodeky a přehrávání hlášení vyžadují vyhrazené prostředky pro zpracování médií. IM-MGW pod řízením MRFC poskytuje tyto prostředky jako sdílený, škálovatelný fond pro celou síť IMS. Tím odděluje zpracování médií od řízení hovorů, což následuje princip IMS vrstevnaté architektury, což zvyšuje flexibilitu, škálovatelnost a zjednodušuje zavádění nových mediálních funkcí.

## Klíčové vlastnosti

- Provádí mediální transkódování mezi IMS kodeky (např. AMR-WB, EVS) a staršími kodeky (např. G.711, AMR-NB)
- Zajišťuje spolupráci mezi paketově přepínanými (IP/RTP) a okruhově přepínanými (TDM/ATM) přenosovými sítěmi
- Provádí funkce zpracování médií jako potlačení ozvěn, manipulace s tóny a konferenční propojení
- Řízena MGCF nebo MRFC pomocí řídicího protokolu H.248 (Megaco)
- Podporuje zákonné odposlechy mediálních proudů podle požadavků
- Slouží jako centralizovaný prostředek pro mediální služby IMS, což umožňuje škálovatelné nasazení služeb

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TR 23.981** (Rel-19) — IPv4 IMS Interworking and Migration Study
- **TS 26.454** (Rel-19) — EVS Codec Mapping for 3G CS Networks
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.235** (Rel-19) — SIP-I CS Core Network Interworking
- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions

---

📖 **Anglický originál a plná specifikace:** [IM-MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-mgw/)
