---
slug: "iari"
url: "/mobilnisite/slovnik/iari/"
type: "slovnik"
title: "IARI – IMS Application Reference Identifier"
date: 2026-01-01
abbr: "IARI"
fullName: "IMS Application Reference Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/iari/"
summary: "Globálně unikátní identifikátor pro aplikaci v IMS, který umožňuje síti a uživatelskému zařízení (UE) identifikovat a spravovat konkrétní služby, jako je hlas, video nebo zasílání zpráv. Je klíčový pr"
---

IARI je globálně unikátní identifikátor pro aplikaci v IMS, který umožňuje síti a uživatelskému zařízení identifikovat a spravovat konkrétní služby.

## Popis

IMS Application Reference Identifier (IARI) je základním identifikátorem v architektuře IP Multimedia Subsystem (IMS), standardizovaným organizací 3GPP. Slouží jako trvalý, globálně unikátní identifikátor pro konkrétní aplikaci v IMS, jako je například určitý klient pro hlasové služby přes LTE (VoLTE), služba videokonferencí nebo aplikace pro pokročilé komunikační služby ([RCS](/mobilnisite/slovnik/rcs/)). IARI není vázán na konkrétní instanci aplikace na zařízení, ale na aplikaci jako takovou, což umožňuje síti rozpoznat a uplatnit konzistentní politiky bez ohledu na uživatelské zařízení (UE) nebo relaci. Jedná se o řetězcový identifikátor, často strukturovaný hierarchicky, který může být přidělen standardizačními orgány, poskytovateli služeb nebo vývojáři třetích stran v rámci registračního procesu zajišťujícího globální unikátnost.

Z architektonického hlediska se IARI používá během procedur registrace v IMS a navazování relace. Když UE zahájí registraci v IMS, může v požadavku [SIP](/mobilnisite/slovnik/sip/) REGISTER nebo během vyjednávání značek vlastností (feature tag negotiation) uvést hodnoty IARI, aby indikovalo podporované aplikace. IARI zpracovávají funkce Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) v jádru IMS. Tyto síťové elementy používají IARI k identifikaci aplikace a vyvolání příslušné servisní logiky, například spuštění konkrétních aplikačních serverů ([AS](/mobilnisite/slovnik/as/)) nebo uplatnění služebně specifických politik prostřednictvím funkce Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)). To síti umožňuje rozlišit například mezi základním hlasovým hovorem a podnikovým videokonferenčním službami, a zajistit tak, aby každá z nich obdržela správnou kvalitu služeb (QoS), způsob účtování a zabezpečení.

IARI hraje klíčovou roli při objevování služeb a zajišťování interoperability. Umožňuje UE zjistit, které služby založené na IMS jsou v síti dostupné, a podle toho se nakonfigurovat. Například během počátečního zřizování nebo po změně sítě může UE pomocí informace o IARI určit, zda jsou podporovány funkce jako videohovory nebo přenos souborů. IARI je navíc nezbytný pro Generic Bootstrapping Architecture ([GBA](/mobilnisite/slovnik/gba/)), kde může být použit k odvození aplikací specifických bezpečnostních klíčů, což zajišťuje, že autentizace a šifrování jsou přizpůsobeny konkrétní službě. Tento identifikátor je také referencován v manažerských specifikacích, například pro správu dat účastníků v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) a pro systémy účtování, což umožňuje propojit využití služby s konkrétními aplikacemi pro přesné účtování a reportování.

## K čemu slouží

IARI byl zaveden, aby řešil rostoucí složitost a diverzitu aplikací v ekosystému IMS. Před jeho standardizací byla identifikace a správa různých služeb IMS obtížná, často se spoléhala na ad-hoc metody nebo proprietární identifikátory, což bránilo interoperabilitě a škálovatelnému nasazení služeb. Jak se IMS vyvíjelo z platformy primárně pro hlas na prostředí pro více služeb podporující video, zasílání zpráv a další multimediální aplikace, byl potřebný standardizovaný mechanismus pro jednoznačnou a globální identifikaci každé aplikace. To umožňuje síťovým operátorům, výrobcům zařízení a vývojářům aplikací zajistit konzistentní fungování služeb napříč různými sítěmi a zařízeními.

Vytvoření IARI bylo motivováno potřebou lepší kontroly služeb a vynucování politik. Bez unikátního identifikátoru nemohla síť snadno rozlišovat mezi různými typy provozu nebo uplatňovat diferencované politiky pro účtování, QoS nebo zabezpečení. Například operátor může chtít upřednostnit aplikace pro nouzové služby nebo uplatnit nulové účtování (zero-rating) pro konkrétní aplikaci pro zasílání zpráv. IARI to umožňuje tím, že poskytuje jasnou, standardizovanou značku, kterou může infrastruktura pro řízení politik (jako PCRF) použít pro rozhodování. Také usnadňuje integraci služeb třetích stran tím, že poskytuje registrovaný jmenný prostor, což umožňuje externím vývojářům vytvářet aplikace kompatibilní s IMS, které síť může rozpoznat a spravovat.

Historicky se zavedení IARI ve 3GPP Release 7 časově shodovalo s širším nasazením IMS jako jádra pro konvergenci pevných a mobilních sítí a pro všechny-IP služby. Vyřešilo omezení dřívějších přístupů, kdy byla identifikace služeb často implicitní nebo vázaná na specifické protokolové elementy, což ztěžovalo zavádění nových služeb bez významných síťových upgradů. Oddělením identity aplikace od základního transportu IARI zajistil budoucí vývoj architektury IMS a podpořil dlouhodobou evoluci směrem k bohaté, na služby citlivé síti schopné hostit širokou škálu multimediálních aplikací od různých poskytovatelů.

## Klíčové vlastnosti

- Globálně unikátní řetězcový identifikátor pro aplikace v IMS
- Používán v signalizaci SIP pro identifikaci služby během registrace a navazování relace
- Umožňuje síťové řízení politik a diferenciaci účtování podle aplikace
- Usnadňuje objevování služeb a konfiguraci UE pro dostupné služby IMS
- Podporuje odvození aplikací specifických bezpečnostních klíčů v Generic Bootstrapping Architecture (GBA)
- Referencován v systémech pro správu dat účastníků a účtování pro přesné fakturace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [GBA – Generic Bootstrapping Architecture](/mobilnisite/slovnik/gba/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 31.111** (Rel-19) — USIM Application Toolkit (USAT) Specification
- **TS 31.829** (Rel-13) — ISIM Conformance Requirements Technical Report
- **TS 32.850** (Rel-14) — IMS Charging Correlation Methods Study

---

📖 **Anglický originál a plná specifikace:** [IARI na 3GPP Explorer](https://3gpp-explorer.com/glossary/iari/)
