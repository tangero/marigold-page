---
slug: "bid"
url: "/mobilnisite/slovnik/bid/"
type: "slovnik"
title: "BID – Binding Identification Number"
date: 2025-01-01
abbr: "BID"
fullName: "Binding Identification Number"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bid/"
summary: "Binding Identification Number (BID) je jedinečný identifikátor používaný v sítích 3GPP k asociaci IP adresy uživatele s konkrétním Packet Data Protocol (PDP) kontextem nebo PDN připojením. Je klíčový"
---

BID je jedinečný identifikátor používaný v sítích 3GPP k asociaci IP adresy uživatele s konkrétním PDP kontextem nebo PDN připojením pro mobilitu IP toků a připojení s více přístupy.

## Popis

Binding Identification Number (BID) je základní komponenta v architektuře 3GPP pro správu mobility IP toků a připojení s více přístupy. Funguje v rámci definovaném pro Evolved Packet Core (EPC) a později pro 5G Core (5GC), konkrétně ve scénářích zahrnujících funkce IP Flow Mobility and Seamless Offload ([IFOM](/mobilnisite/slovnik/ifom/)) a Multi-Access Packet Data Network (PDN) Connectivity ([MAPCON](/mobilnisite/slovnik/mapcon/)). BID slouží jako jedinečný ukazatel nebo referenční číslo, které váže konkrétní IP tok nebo skupinu toků k určitému připojení přístupové sítě (např. konkrétní PDN připojení přes LTE nebo důvěryhodný přístup Wi-Fi non-3GPP). Toto vázání je spravováno síťovými entitami, především Policy and Charging Rules Function (PCRF) v EPC nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v 5GC, ve spolupráci s User Equipment (UE).

Architektonicky je BID používán v signalizačních zprávách mezi UE a jádrem sítě. Když je UE schopno se připojit k více přístupovým sítím současně (např. LTE a WLAN), může navázat více PDN připojení nebo přenosových kanálů. Každému z těchto připojení je přiřazen jedinečný BID. UE a síť (PCRF/PCF) používají BID ke korelaci rozhodnutí o politice, tarifních pravidel a směrovacích informací pro IP toky s konkrétním přístupovým přenosovým kanálem, který používají. Například tok videostreamování může být vázán prostřednictvím BID k připojení Wi-Fi, zatímco tok hlasového hovoru je vázán prostřednictvím jiného BID k připojení LTE, což umožňuje optimalizované směrování provozu na základě politiky.

Role BID je nedílnou součástí procedur IP Flow Mobility (IFOM) definovaných ve specifikacích 3GPP. IFOM umožňuje přesun konkrétních IP datových toků z jedné přístupové cesty na druhou bez narušení aplikace. BID poskytuje potřebný identifikátor pro sledování, který tok je namapován na kterou přístupovou cestu během těchto událostí předávání nebo vykládání. Síť používá BID spolu s dalšími parametry, jako je Traffic Flow Template (TFT), k instalaci příslušných paketových filtrů v UE a síťových branách (např. PGW v EPC, [UPF](/mobilnisite/slovnik/upf/) v 5GC), aby zajistila správné směrování paketů. Tento mechanismus umožňuje plynulý uživatelský zážitek a efektivní využití síťových zdrojů napříč heterogenními přístupovými sítěmi.

V systému 5G se koncept vyvíjí, ale zachovává si podobné principy. BID může být použit v kontextu [ATSSS](/mobilnisite/slovnik/atsss/) (Access Traffic Steering, Switching, and Splitting) pro správu připojení s více přístupy. Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a PCF používají identifikátory analogické BID ke směrování konkrétních deskriptorů provozu přes různé typy přístupu (3GPP vs. non-3GPP). BID tedy představuje trvalé logické vázání, které abstrahuje podrobnosti specifické pro přístup, a poskytuje stabilní referenci pro vynucování politiky a správu mobility napříč různými releasy 3GPP a generacemi sítí.

## K čemu slouží

BID byl vytvořen pro řešení rostoucí potřeby plynulé mobility a správy provozu mezi různorodými přístupovými technologiemi. Když mobilní operátoři začali integrovat Wi-Fi a další non-3GPP přístupové sítě do své buněčné infrastruktury, byl vyžadován mechanismus, který by umožnil jedinému UE udržovat simultánní připojení a inteligentně směrovat konkrétní aplikační toky na nejvhodnější přístup. Před standardizovanými mechanismy, jako jsou [IFOM](/mobilnisite/slovnik/ifom/) a [MAPCON](/mobilnisite/slovnik/mapcon/), bylo vykládání na Wi-Fi často jednoduché, vše-nebo-nic přepínání typu 'přeruš a pak vytvoř', které mohlo narušit probíhající služby. BID poskytuje základní identifikátor pro umožnění mobility toků typu 'vytvoř před přerušením', což zlepšuje uživatelský zážitek.

Historický kontext vychází z 3GPP Release 10 a práce na síťové mobilitě a vykládání. Primárním řešeným problémem je kontinuita služeb během přepínání přístupu. Například uživatel zahajující videohovor na LTE mohl mít video tok plynule předán na Wi-Fi síť po vstupu do jejího pokrytí, aniž by hovor spadl, protože vázání (prostřednictvím BID) umožňuje síti přesměrovat konkrétní IP tok. Tím se řeší omezení dřívějších přístupů, kdy by se muselo přesunout celé PDN připojení (a všechny jeho IP toky), nebo kde simultánní připojení s více přístupy nebylo efektivně spravováno. BID umožňuje detailní řízení politiky na úrovni toků.

Dále BID podporuje pokročilé účtování a vynucování politik. Vázáním toků na specifické přístupy identifikované BID mohou operátoři aplikovat různé tarifní sazby nebo politiky kvality služeb (QoS) na tok a typ přístupu. Tato granularita nebyla možná s dřívějšími modely centrickými na přenosové kanály, kde veškerý provoz na kanálu dostával jednotné zacházení. Vytvoření BID bylo tedy motivováno potřebou jemnější síťové kontroly, efektivního využití spektra prostřednictvím vykládání provozu a komerční flexibility pro vytváření diferencovaných služeb na základě přístupové technologie.

## Klíčové vlastnosti

- Jedinečně identifikuje vazbu mezi IP tokem a konkrétním připojením přístupové sítě
- Umožňuje IP Flow Mobility (IFOM) pro plynulé předávání jednotlivých toků mezi přístupy 3GPP a non-3GPP
- Podporuje Multi-Access PDN Connectivity (MAPCON) pro simultánní připojení přes více přístupů
- Používá se PCRF/PCF pro aplikaci pravidel politiky a účtování specifických pro přístup na vázané toky
- Usnadňuje správu Traffic Flow Template (TFT) a instalaci paketových filtrů v UE a síťových branách
- Poskytuje stabilní referenci pro správu relací a mobility napříč heterogenními přístupovými sítěmi

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.261** (Rel-19) — IP Flow Mobility between 3GPP and WLAN
- **TS 24.303** (Rel-19) — Dual-Stack MIPv6 Mobility Management
- **TS 24.327** (Rel-12) — Mobility between I-WLAN and GPRS

---

📖 **Anglický originál a plná specifikace:** [BID na 3GPP Explorer](https://3gpp-explorer.com/glossary/bid/)
