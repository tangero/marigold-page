---
slug: "vid"
url: "/mobilnisite/slovnik/vid/"
type: "slovnik"
title: "VID – VLAN Identifier"
date: 2026-01-01
abbr: "VID"
fullName: "VLAN Identifier"
category: "Interface"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vid/"
summary: "12bitové pole v rámcích Ethernet používané k identifikaci virtuálních lokálních sítí (VLAN), které umožňuje segmentaci sítě a izolaci provozu. V 3GPP se používá v sítích 5G k oddělení provozu v uživat"
---

VID je 12bitové pole v rámcích Ethernet sloužící k identifikaci virtuálních sítí LAN (VLAN) pro segmentaci sítě. V sítích 3GPP 5G odděluje provoz v uživatelské rovině pro různé řezy nebo služby na rozhraních typu Ethernet.

## Popis

VID ([VLAN](/mobilnisite/slovnik/vlan/) Identifier) je 12bitový identifikátor definovaný ve standardech [IEEE](/mobilnisite/slovnik/ieee/) 802.1Q a přijatý ve specifikacích 3GPP pro sítě 5G. Používá se k označování rámců Ethernet příslušností k VLAN, což umožňuje koexistenci více logických sítí na stejné fyzické infrastruktuře. V kontextu 3GPP se VID používá na rozhraních uživatelské a řídicí roviny, jako jsou N3, N6 a N9, k oddělení provozu náležejícího různým síťovým řezům, tokům QoS nebo uživatelským relacím. To umožňuje efektivní využití síťových zdrojů, zvýšenou bezpečnost a zjednodušenou správu díky izolaci datových proudů na základě požadavků služeb nebo administrativních domén.

Z architektonického hlediska VID funguje v rámci hlavičky rámce Ethernet, konkrétně v tagu 802.1Q, který obsahuje 12bitové pole VID a 3bitový Priority Code Point ([PCP](/mobilnisite/slovnik/pcp/)) pro QoS. Při přenosu paketu přes rozhraní Ethernet v síti 5G je VID přiřazeno na základě politik definovaných funkcí pro výběr síťového řezu nebo funkcí správy relací. Například v jádru 5G (5GC) může funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) aplikovat VLAN tagy na pakety určené pro různá jména datových sítí ([DNN](/mobilnisite/slovnik/dnn/)) nebo instance síťových řezů. VID umožňuje přepínačům a směrovačům v přenosové síti přeposílat rámce pouze na porty, které jsou členy příslušné VLAN, čímž efektivně vytváří izolované broadcastové domény a zabraňuje neoprávněnému provozu mezi nimi.

Mechanismus přiřazování a zpracování VID zahrnuje několik síťových funkcí. Během navazování relace může funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) nakonfigurovat UPF pravidly pro označování VLAN, včetně hodnot VID, které se mají použít pro konkrétní [PDU](/mobilnisite/slovnik/pdu/) relace nebo toky QoS. Tato pravidla uplatňuje UPF při zpracování provozu v uživatelské rovině. Dále mohou na přiřazení VID mít vliv funkce [NEF](/mobilnisite/slovnik/nef/) (Network Exposure Function) nebo PCF (Policy Control Function) na základě profilů předplatného nebo požadavků služeb. Na přijímací straně síťové prvky, jako je gNB nebo další UPF, používají VID k identifikaci příslušného kontextu zpracování, například pro mapování na konkrétní síťový řez nebo aplikaci politik QoS. Tím je zajištěno, že provoz je správně směrován a řízen podle charakteristik řezu, jako je latence, šířka pásma nebo úroveň zabezpečení.

V sítích 5G hraje VID klíčovou roli při podpoře síťového řezování, což je klíčová vlastnost pro umožnění různorodých služeb, jako je rozšířené mobilní širokopásmové připojení (eMBB), ultra-spolehlivá komunikace s nízkou latencí (URLLC) a hromadný IoT. Pomocí VLAN mohou operátoři vytvářet logické sítě, které jsou od sebe izolované, a poskytovat vyhrazené zdroje a přizpůsobený výkon pro každý řez. Tato izolace je nezbytná pro splnění přísných požadavků různých služeb, jako je zajištění nízké latence pro autonomní vozidla nebo vysoké šířky pásma pro streamování videa. Kromě toho VID usnadňuje správu provozu a zjednodušuje síťové operace tím, že umožňuje centralizovanou správu politik specifických pro řez prostřednictvím standardizovaných rozhraní, jako je N4 mezi SMF a UPF.

## K čemu slouží

Zavedení VLAN Identifier (VID) ve specifikacích 3GPP počínaje Release 15 bylo motivováno potřebou efektivní segregace provozu a síťového řezování v systémech 5G. Před 5G používaly mobilní sítě pro oddělení uživatelské roviny primárně tunely GTP, což přidávalo režii a složitost v transportní vrstvě. S přechodem na cloud-nativní architektury a přenosové cesty typu fronthaul/midhaul/backhaul založené na Ethernetu vzrostla poptávka po odlehčenějších mechanismech pro izolaci provozu pro různé služby nebo klienty. VID poskytuje standardizovaný způsob využití stávajících možností VLAN v Ethernetu, které jsou široce podporovány v síťových zařízeních, k dosažení této izolace bez zavádění proprietárních protokolů.

Historicky se VLAN používaly v podnikových a datacentrových sítích po desetiletí k segmentaci broadcastových domén a zlepšení zabezpečení. V kontextu 5G zavedení VID řeší omezení předchozích mobilních jádrových sítí, kde se diferenciace provozu často řešila na IP vrstvě nebo prostřednictvím vyhrazených tunelů, což mohlo být neefektivní pro rozsáhlá nasazení s různorodými požadavky služeb. Začleněním VID do standardů 3GPP mohou operátoři znovu využít svou stávající infrastrukturu Ethernetu a znalosti, čímž snižují náklady na nasazení a urychlují zavádění služeb 5G. To také odpovídá trendu konvergence mobilních a pevných sítí, kde je Ethernet běžnou transportní technologií.

Dále VID řeší problém škálovatelného síťového řezování tím, že poskytuje jednoduchou, ale účinnou metodu pro identifikaci a izolaci provozu specifického pro řez. V sítích 4G a starších často vyžadovalo vytvoření samostatných logických sítí složité konfigurace více tunelů GTP nebo instancí virtuálního směrování. S VID může jediné fyzické rozhraní přenášet provoz pro více řezů, z nichž každý je identifikován jedinečným VID, což zjednodušuje návrh a správu sítě. To je zvláště důležité pro případy použití 5G, jako je síť jako služba, kde operátoři potřebují nabízet přizpůsobené řezy různým vertikálním odvětvím. Použití VID také zvyšuje bezpečnost tím, že zabraňuje úniku provozu mezi řezy, což je kritické pro aplikace s přísnými požadavky na důvěrnost, jako jsou zdravotnictví nebo finanční služby.

## Klíčové vlastnosti

- 12bitový identifikátor pro označování VLAN v Ethernetu podle IEEE 802.1Q
- Umožňuje izolaci provozu pro síťové řezy v uživatelské rovině 5G
- Podporuje diferenciaci QoS prostřednictvím přidruženého Priority Code Point (PCP)
- Používá se na rozhraních 5G jako N3, N6 a N9 pro segmentaci transportu
- Usnadňuje efektivní využití zdrojů multiplexováním řezů na sdílených spojích
- Integruje se se správou relací 5G pro dynamické přiřazování VLAN

## Související pojmy

- [VLAN – Virtual Local Area Network](/mobilnisite/slovnik/vlan/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [VID na 3GPP Explorer](https://3gpp-explorer.com/glossary/vid/)
