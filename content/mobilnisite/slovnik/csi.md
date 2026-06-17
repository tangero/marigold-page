---
slug: "csi"
url: "/mobilnisite/slovnik/csi/"
type: "slovnik"
title: "CSI – Combined CS and IMS Services"
date: 2025-01-01
abbr: "CSI"
fullName: "Combined CS and IMS Services"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi/"
summary: "CSI je servisní architektura 3GPP, která umožňuje bezproblémovou integraci a poskytování jak telefonních služeb okruhového přepojování (CS), tak multimediálních služeb založených na IP multimediálním"
---

CSI je servisní architektura 3GPP, která umožňuje bezproblémovou integraci a poskytování jak přepojovaných telefonních služeb okruhového přepojování (Circuit-Switched), tak paketově přepojovaných služeb IP multimediální podsystému (IMS) přes jedinou mobilní síť.

## Popis

CSI je komplexní servisní architektura definovaná 3GPP, která překlenuje propast mezi tradičními službami domény okruhového přepojování ([CS](/mobilnisite/slovnik/cs/)), především hlasem a SMS, a službami nově vznikající domény IP multimediálního podsystému (IMS), které zahrnují multimediální telefonii, videohovory a pokročilé komunikační služby (RCS). Architektura je navržena tak, aby tyto dva odlišné platformy pro poskytování služeb mohly koexistovat a vzájemně spolupracovat a představovaly účastníkovi jednotnou servisní logiku a uživatelský zážitek. Toho dosahuje prostřednictvím souboru standardizovaných funkčních entit a referenčních bodů, které koordinují provádění služeb mezi jádrem sítě CS ([MSC](/mobilnisite/slovnik/msc/)) a jádrem IMS ([CSCF](/mobilnisite/slovnik/cscf/)).

V jádru CSI zavádí koncept interakce a koordinace služeb. Když účastník s podporou CSI zahájí nebo přijme relaci, síť musí rozhodnout, jak směrovat a zpracovat jednotlivé komponenty služby. U hlasového hovoru to může být zpracováno nativně doménou CS pro širokoplošnou spolehlivost, zatímco doplňkové služby nebo souběžné multimediální relace (jako video nebo přenos souborů) jsou ukotveny a spravovány IMS. Architektura definuje mechanismy, jako je rozhraní IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)) a vylepšení protokolu [CAMEL](/mobilnisite/slovnik/camel/) (Customised Applications for Mobile network Enhanced Logic), které tuto koordinaci usnadňují. Klíčovou funkční komponentou je aplikační server CSI ([AS](/mobilnisite/slovnik/as/)) uvnitř IMS, který hostuje kombinovanou servisní logiku a komunikuje jak s Serving-CSCF (S-CSCF) přes rozhraní ISC, tak nepřímo s doménou CS, aby orchestroval tok služby.

Technický provoz zahrnuje procedury navazování a řízení relace. Pro odchozí mobilní relaci CSI s podporou CSI indikuje uživatelské zařízení (UE) svou schopnost CSI. Síť, často na základě rozhodnutí o politice v IMS, může rozdělit mediální komponenty: hlas v reálném čase je směrován přes nosič CS pomocí tradičního řízení hovoru (např. přes MSC), zatímco jiné mediální proudy (např. video) jsou navázány jako samostatné IP toky přes nosič paketového přepojování (PS) řízený IMS pomocí protokolu Session Initiation Protocol (SIP). IMS funguje jako kotva servisního řízení, zajišťuje, že účtování, doplňkové služby (jako přidržení hovoru nebo přesměrování) a servisní logika jsou konzistentně aplikovány napříč oběma doménami. To vyžaduje těsnou synchronizaci mezi signalizací SIP v IMS a signalizací [ISUP](/mobilnisite/slovnik/isup/)/BICC v jádru CS.

Role CSI v síti je zásadně přechodová a integrační. Slouží jako klíčový faktor umožňující síťovým operátorům migraci z architektur 2G/3G orientovaných na CS k plně IP sítím 4G/5G založeným na IMS a VoLTE/VoNR. Tím, že umožňuje síti CS fungovat jako spolehlivý nosič hlasového média, zatímco IMS poskytuje pokročilé servisní řízení, CSI chrání investice do starší infrastruktury a zajišťuje dostupnost služeb během migračního období. Také umožňuje časné zavedení multimediálních služeb založených na IMS pro účastníky, kteří ještě nemusí mít plně IMS-kompatibilní zařízení nebo rádiový přístup, čímž urychluje adopci nových služeb generujících příjmy.

## K čemu slouží

CSI bylo vytvořeno k řešení základní výzvy ve vývoji mobilních sítí: přechodu od přepojovaných sítí dominovaných hlasem k paketově přepojovaným, multimediálním plně IP sítím. Na počátku 2000. let, se standardizací IMS v 3GPP Release 5, čelili operátoři dilematu. IMS slibovalo budoucnost bohatých, integrovaných multimediálních služeb, ale vyžadovalo zcela novou architekturu jádra sítě. Mezitím stávající síť [CS](/mobilnisite/slovnik/cs/) představovala masivní, spolehlivou a všudypřítomnou investici pro hlasovou telefonii, hlavní zdroj příjmů. „Velký třesk“ – náhlá výměna – byla ekonomicky a technicky neproveditelná. CSI bylo koncipováno k vyřešení tohoto problému tím, že umožnilo oběma doménám spolupracovat a umožnilo postupnou, rizikově řízenou migrační cestu.

Primární problém, který CSI řeší, je fragmentace služeb a zhoršení uživatelského zážitku během přechodu. Bez CSI by síť zavádějící IMS vytvořila dvě oddělená úložiště služeb: základní hlas/SMS v síti CS a pokročilé multimédia v IMS, s minimální nebo žádnou interakcí mezi nimi. Účastník by mohl mít dvě samostatné identity, adresáře a servisní profily. CSI toto eliminuje poskytnutím jednotné servisní vrstvy. Umožňuje operátorům zavádět servisní inovace založené na IMS – jako kombinaci hlasu s okamžitými zprávami nebo videem – a zároveň stále využívat zralý, kvalitní hlasový nosič sítě CS. To bylo obzvláště důležité pro zajištění bezproblémového pokrytí služeb a interoperability se staršími sítěmi a zařízeními.

Historicky CSI řešilo omezení před-IMS servisních architektur, které byly buď čistě založené na CS (postrádaly multimediální flexibilitu), nebo rané pokusy o PS multimédia, které byly nestandardizované a postrádaly robustní řízení relace. Standardizací interakce poskytlo CSI jasný plán pro dodavatele a operátory. Motivovalo to vytvoření hybridního modelu poskytování služeb, který maximalizoval využití aktiv, zajistil zpětnou kompatibilitu a připravil cestu pro eventuální úplnou migraci na IMS-based Voice over LTE (VoLTE) a Voice over NR (VoNR), kde je nosič CS konečně vyřazen ve prospěch plné služby IP Multimedia Telephony přes paketové jádro.

## Klíčové vlastnosti

- Jednotné řízení služeb napříč doménami CS a IMS
- Současná podpora hlasové relace CS a multimediální relace IMS
- Kontinuita služeb a konzistentní uživatelský zážitek během síťového přechodu
- Opětovné využití stávající infrastruktury CS pro spolehlivý hlasový nosič
- Servisní inovace založené na IMS a hostování aplikačních serverů
- Standardizované koordinační mechanismy (např. vylepšený CAMEL, rozhraní ISC)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.978** (Rel-4) — CAMEL Control of VoIP Services Feasibility Study
- **TS 23.279** (Rel-19) — Combined CS and IMS Services (CSI) Architecture
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.235** (Rel-12) — Default Codecs for 3GPP IP Multimedia Subsystem
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.278** (Rel-19) — CAMEL Application Part (CAP) for IMS Phase 4
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- … a dalších 33 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi/)
