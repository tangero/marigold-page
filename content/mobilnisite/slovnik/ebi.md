---
slug: "ebi"
url: "/mobilnisite/slovnik/ebi/"
type: "slovnik"
title: "EBI – EPS Bearer Identity"
date: 2026-01-01
abbr: "EBI"
fullName: "EPS Bearer Identity"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ebi/"
summary: "Jedinečný číselný identifikátor přiřazený každému EPS přenosovému kanálu (bearer) v sítích LTE a 5G. Síťové uzly jej používají ke správě a rozlišení datových toků pro jedno uživatelské zařízení (UE),"
---

EBI je jedinečný číselný identifikátor přiřazený každému EPS přenosovému kanálu (bearer) v sítích LTE a 5G, který síťové uzly používají ke správě, rozlišení a zajištění správného zacházení s QoS pro datové toky uživatelského zařízení (UE).

## Popis

Identita EPS přenosového kanálu (EBI) je základním identifikátorem v architektuře Evolved Packet System (EPS), klíčovým pro správu přenosových kanálů v LTE a zachovaným i v 5GS. Jedná se o jedinečnou celočíselnou hodnotu, typicky v rozsahu 5 až 15, kterou přiřazuje [MME](/mobilnisite/slovnik/mme/) při zřizování dedikovaného kanálu nebo jako součást nastavení výchozího kanálu. EBI není pouze lokální značka; jde o globálně významný identifikátor v kontextu připojení UE k [PDN](/mobilnisite/slovnik/pdn/), používaný napříč více síťovými rozhraními včetně [S1-MME](/mobilnisite/slovnik/s1-mme/), S11 a S5/S8. Jeho primární úlohou je poskytnout jednoznačnou referenci pro síťové entity – jako jsou MME, Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)), Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)) a samotné UE – k identifikaci konkrétního přenosového kanálu a s ním spojeného QoS profilu, šablon datových toků ([TFT](/mobilnisite/slovnik/tft/)) a účtovacích pravidel.

Z provozní perspektivy je EBI přenášeno v klíčových signalizačních zprávách. Například při aktivaci dedikovaného kanálu iniciuje proceduru P-GW a navržené EBI zahrne do požadavku Create Bearer Request odeslaného S-GW a MME. MME jej následně předá eNodeB a UE. Všechny následné modifikace, jako je změna prostředků kanálu nebo jeho deaktivace, odkazují na konkrétní kanál právě pomocí tohoto EBI. To zajišťuje, že příkazy, jako je aktualizace parametru QoS nebo ukončení konkrétního datového toku, jsou provedeny na správné logické cestě. EBI je také úzce spojeno s kontextem EPS kanálu uloženým v UE a síťových uzlech, propojujíc rádiový kanál ([DRB](/mobilnisite/slovnik/drb/)), S1 kanál a S5/S8 kanál v souvislý end-to-end přenosový okruh.

V architektuře 5G Core (5GC) se koncept vyvíjí s QoS tokem, ale EBI zůstává klíčové pro scénáře vzájemného propojení a pro UE připojená přes [E-UTRAN](/mobilnisite/slovnik/e-utran/) k 5GC (nestandalone režim nebo EPS fallback). 5GC mapuje 5G QoS toky na EPS kanály při rozhraní s LTE RAN nebo EPC a EBI se používá k identifikaci těchto namapovaných kanálů. Porozumění EBI je proto nezbytné pro správu mobility a kontinuity relací mezi sítěmi 4G a 5G, protože slouží jako společný referenční bod pro operace na úrovni přenosových kanálů napříč různými generacemi jádrových sítí.

## K čemu slouží

EBI bylo zavedeno, aby vyřešilo kritickou potřebu jednoznačné identifikace a správy přenosových kanálů v all-IP architektuře EPS v LTE. Předchozí systémy 3GPP, jako UMTS, používaly RAB (Radio Access Bearer) ID, ale plošší a zjednodušenější architektura EPS vyžadovala nový, standardizovaný identifikátor, který by mohl být konzistentně používán od UE přes RAN až k bránám jádrové sítě. Bez jedinečného identifikátoru, jako je EBI, by síťové uzly nemohly koordinovat zřizování, modifikaci a ukončování více současných kanálů pro jedno UE, což by vedlo k potenciálnímu chybnému směrování provozu, nesprávné aplikaci QoS a chybám v účtování.

Vznik EBI byl motivován přechodem k více souběžným dedikovaným kanálům na jedno PDN připojení, což je funkce umožňující sofistikovanou diferenciaci služeb (např. samostatné kanály pro hlas, video a datový provoz typu best-effort). Každý z těchto kanálů vyžaduje nezávislou správu. EBI poskytuje nástroj pro tuto správu, umožňující síti instruovat UE a eNodeB, aby aplikovaly specifické paketové filtry a QoS charakteristiky na konkrétní sadu IP toků. Je to základní kámen pro umožnění slibovaných QoS schopností LTE, jako jsou kanály se zaručenou přenosovou rychlostí (GBR) pro služby v reálném čase.

Historicky je jeho návrh zajištěn pro zpětnou kompatibilitu a budoucí flexibilitu. Rozsah hodnot je rezervován, aby se předešlo konfliktům s již existujícími identifikátory. Jeho trvalost v síti umožňuje efektivní signalizaci; namísto odesílání plných kontextů kanálů v každé zprávě mohou uzly odkazovat na kompaktní EBI. Tím se snižuje signalizační režie a zjednodušuje správa stavu, což je klíčové pro škálování sítí na podporu milionů zařízení a jejich komplexních požadavků na služby.

## Klíčové vlastnosti

- Jedinečný číselný identifikátor pro EPS přenosový kanál v kontextu PDN připojení UE
- Globálně významný napříč rozhraními UE, eNodeB, MME, S-GW a P-GW
- Používaný ve všech signalizačních procedurách souvisejících s kanály (aktivace, modifikace, deaktivace)
- Přiřazovaný MME, často na základě požadavku od P-GW (PCRF)
- Nezbytné pro mapování mezi QoS profily, TFT a skutečnými prostředky kanálu
- Kritické pro vzájemné propojení architektur 4G EPS a 5G Core sítě

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [EBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ebi/)
