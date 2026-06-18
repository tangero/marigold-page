---
slug: "smn"
url: "/mobilnisite/slovnik/smn/"
type: "slovnik"
title: "SMN – Shared MBMS Network"
date: 2025-01-01
abbr: "SMN"
fullName: "Shared MBMS Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/smn/"
summary: "Síťová architektura, ve které je infrastruktura služby Multimedia Broadcast Multicast Service (MBMS) sdílena mezi více operátory veřejných pozemních mobilních sítí (PLMN). Umožňuje operátorům spolupra"
---

SMN je síťová architektura, ve které více operátorů mobilních sítí sdílí infrastrukturu MBMS pro společné nasazení vysílacích služeb, jako je mobilní TV, čímž optimalizuje náklady a využití spektra.

## Popis

Sdílená síť [MBMS](/mobilnisite/slovnik/mbms/) (SMN) je architektonický koncept 3GPP, ve kterém síťové prvky a zdroje potřebné pro službu Multimedia Broadcast Multicast Service (MBMS) společně využívají dva nebo více účastnických operátorů veřejných pozemních mobilních sítí ([PLMN](/mobilnisite/slovnik/plmn/)). Samotná služba MBMS je služba typu point-to-multipoint navržená pro efektivní doručování identického obsahu (např. video streamů, softwarových aktualizací, nouzových výstrah) více uživatelům současně. SMN tuto efektivitu rozšiřuje na provozní úroveň tím, že umožňuje operátorům sdílet kapitálové a provozní výdaje spojené s infrastrukturou MBMS.

Architektonicky SMN zahrnuje sdílenou základnovou síť a sdílenou rádiovou přístupovou síť pro provoz MBMS. Mezi klíčové sdílené prvky patří Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), což je vstupní bod pro poskytovatele obsahu, a MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)), který zajišťuje IP multicast distribuci a řízení relací. V RAN sdílené buňky (např. buňky [E-UTRAN](/mobilnisite/slovnik/e-utran/) nakonfigurované pro [MBSFN](/mobilnisite/slovnik/mbsfn/) – Multicast-Broadcast Single Frequency Network) vysílají stejný obsah, který mohou přijímat koncová zařízení (UE) předplacená u kteréhokoli z účastnických PLMN. SMN je logicky samostatný, sdílený PLMN pro účely MBMS s vlastní identitou PLMN.

SMN funguje na základě vzájemné důvěry a koordinace mezi účastnickými operátory. Koncové zařízení (UE) přistupuje k SMN na základě konfigurace poskytnuté jeho domovskou sítí PLMN ([HPLMN](/mobilnisite/slovnik/hplmn/)). Při aktivaci služby MBMS zahájí BM-SC v SMN relaci. MBMS-GW použije IP multicast k distribuci dat do sdílených uzlů RAN (např. eNodeB v LTE). Tyto uzly se synchronizují, aby vysílaly identické signály v oblasti MBSFN, čímž vytvoří jednofrekvenční síť, která zlepšuje pokrytí a spektrální účinnost. Koncová zařízení (UE) od libovolného účastnického operátora mohou tento vysílání přijímat naladěním na sdílenou nosnou frekvenci MBMS a použitím služebních klíčů poskytnutých jejich příslušnými HPLMN pro dešifrování.

Jejím účelem je učinit MBMS ekonomicky životaschopnou pro služby, které mají široký dosah, ale potenciálně nízkou individuální účast na jednoho operátora, jako je mobilní televize, streamování živých událostí nebo rozsáhlé systémy varování veřejnosti. Sdílením infrastruktury operátoři snižují duplicitní investice potřebné pro celostátní vysílací vrstvu. Koncept SMN je zvláště relevantní pro vysílání založené na LTE (eMBMS) a byl dále zvažován v kontextu služeb multicast a broadcast v 5G NR, což umožňuje efektivní doručování médií a skupinovou komunikaci.

## K čemu slouží

Koncepce SMN byla vytvořena, aby překonala hlavní překážku nasazení [MBMS](/mobilnisite/slovnik/mbms/): vysoké náklady na infrastrukturu pro službu s nejistým nebo sdíleným obchodním modelem. Jednotliví operátoři mobilních sítí váhali s investicí do vyhrazené celostátní vysílací sítě (vyžadující samostatný BM-SC, MBMS-GW a spektrum pro MBSFN), když byly výnosy z vysílacích služeb, jako je mobilní TV, nejisté a uživatelská základna mohla být rozdělena mezi konkurenty. SMN poskytuje model spolupráce pro sdílení těchto nákladů a rizik.

Řeší problém ekonomické životaschopnosti služeb typu point-to-multipoint. Tím, že umožňuje více PLMN sdílet jedinou síť MBMS, se náklady na jednoho operátora dramaticky snižují. To umožňuje nasadit MBMS pro aplikace, které prospívají široké populaci bez ohledu na jejich síťové předplatné, jako jsou nouzové výstrahy od vládních orgánů, volně přijímatelné televizní kanály nebo rozsáhlá distribuce obsahu během významných událostí. Také podporuje efektivní využití vzácného spektra vyhrazeného pro vysílání.

Motivace vycházela z touhy plně využít potenciál eMBMS v LTE, s poučením z omezeného komerčního přijetí MBMS v 3G. Hnacími silami byla potřeba nákladově efektivní platformy pro komunikaci v oblasti veřejné bezpečnosti (jako jsou varování před zemětřesením nebo tsunami), příležitost pro nové vysílací mediální služby a požadavek na podporu služeb Mission Critical (MCx) pro profesionální skupiny. SMN, standardizovaná ve vydání 14, poskytla potřebný architektonický rámec a procedury (včetně předplatného, autentizace a objevování služeb), aby se MBMS změnila z technologie pro jednoho operátora na multi-operatorní utilitu.

## Klíčové vlastnosti

- Sdílená základnová síť MBMS (BM-SC, MBMS-GW) a RAN mezi více PLMN
- Funguje jako logicky samostatný sdílený PLMN pro MBMS s vlastní identitou PLMN (PLMN ID)
- Podporuje provoz MBSFN ve sdílených buňkách pro efektivní vysílání
- Umožňuje koncovým zařízením (UE) od účastnických operátorů přistupovat ke službám pomocí přihlašovacích údajů z domovské sítě
- Snižuje nasazovací a provozní náklady prostřednictvím sdílení infrastruktury
- Umožňuje celostátní služby, jako je varování veřejnosti nebo mobilní TV

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description

---

📖 **Anglický originál a plná specifikace:** [SMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/smn/)
