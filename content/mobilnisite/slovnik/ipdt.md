---
slug: "ipdt"
url: "/mobilnisite/slovnik/ipdt/"
type: "slovnik"
title: "IPDT – IP Data Termination"
date: 2025-01-01
abbr: "IPDT"
fullName: "IP Data Termination"
category: "Core Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/ipdt/"
summary: "IP Data Termination (IPDT) je funkční prvek v paketově orientované jádrové síti 3GPP, který slouží jako koncový bod pro IP datový provoz uživatele. Je zodpovědný za správu datové cesty, včetně směrová"
---

IPDT je funkční prvek v jádrové síti 3GPP, který ukončuje IP datový provoz uživatele a spravuje datovou cestu včetně směrování, přeposílání a vynucování politik.

## Popis

IP Data Termination (IPDT) je funkce jádrové sítě definovaná v paketové doméně (PS) 3GPP. Působí jako architektonický kotvící bod a bod ukončení služby pro IP datové pakety pocházející od nebo směřující k uživatelskému zařízení (UE). Koncepčně se IPDT nachází v rámci uzlu Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) v sítích 3G UMTS a později se vyvinul v Packet Data Network Gateway (PGW) v 4G EPS a v Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) / User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G. Jeho primární role je rozhraní mezi jádrovou sítí mobilního operátora a externími paketovými datovými sítěmi (PDN), jako je veřejný internet nebo privátní podnikové sítě.

Architektonicky je IPDT zodpovědný za vytváření a správu přenosové cesty v uživatelské rovině. Když UE aktivuje kontext Packet Data Protocol (PDP) v 3G nebo naváže připojení PDN v 4G/5G, signalizace zahrnuje nastavení logického tunelu (např. [GTP-U](/mobilnisite/slovnik/gtp-u/) tunelu) mezi bránou rádiové přístupové sítě (SGSN/SGW) a IPDT. IPDT přiděluje UE IP adresu, typicky přes [DHCP](/mobilnisite/slovnik/dhcp/) nebo z lokálního poolu, a stává se výchozím směrovačem pro IP provoz UE. Provádí klíčové funkce jako směrování a přeposílání paketů, kontrolu provozu a často integruje funkce Policy and Charging Control (PCC) pro detekci datových toků služby, jejich povolování/zakazování a vynucování kvality služeb (QoS).

Z protokolového hlediska IPDT ukončuje GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) na rozhraní Gn (3G) nebo S5/S8 (4G) ze strany jádrové sítě. Na svém externím rozhraní (Gi v 3G/4G, N6 v 5G) používá standardní IP směrovací protokoly. Může také implementovat schopnosti Deep Packet Inspection (DPI), aplikovat pravidla firewallu a shromažďovat data pro účtovací záznamy ([CDR](/mobilnisite/slovnik/cdr/)). Výkon a škálovatelnost IPDT jsou klíčové pro celkovou propustnost dat sítě a uživatelský zážitek.

V širší síťové architektuře je IPDT centrálním uzlem pro správu mobility. V 3G/4G slouží jako kotvící bod pro předávání mezi SGSN nebo mezi SGW, čímž zajišťuje kontinuitu IP relace. Jeho vývoj v PGW v EPS a SMF/UPF v systému 5G odráží jeho trvalou roli bodu konvergence, kde se setkávají politiky mobilní sítě s IP světem, a spravuje most mezi mobilně specifickými transportními protokoly a univerzální IP vrstvou.

## K čemu slouží

IPDT byl vytvořen, aby poskytl standardizovaný, škálovatelný a řiditelný koncový bod pro IP provoz v architektuře paketového jádra 3GPP. Před érou 3G a formalizací PS domény ve vydání 99 byly datové služby často řešeny ad-hoc s omezenou integrací. Zavedení IPDT ve vydání 5, spolu s plnou architekturou IMS, bylo motivováno potřebou spolehlivě a efektivně podporovat širokou škálu IP multimediálních služeb.

Vyřešil problém, jak bezproblémově integrovat mobilní účastníky do IP sítí. Bez vyhrazené, standardizované funkce ukončení by bylo mimořádně náročné konzistentně spravovat přidělování IP adres, účastnické politiky, směrování a účtování napříč různými síťovými dodavateli a operátory. IPDT poskytl tento společný referenční bod, což umožnilo interoperabilitu a vývoj pokročilých datových služeb.

IPDT navíc abstrahoval složitosti rádiové přístupové sítě od externího IP světa. Zpracovával mobilitu (udržování konstantní IP adresy UE během předávání), přizpůsoboval parametry QoS mezi rádiovou a jádrovou doménou a sloužil jako přirozený bod pro aplikaci operátorských politik a zákonného odposlechu. Jeho vytvoření byl zásadní krok v přechodu mobilních sítí z primárních přenašečů hovorů v okruhově orientovaném režimu na skutečné poskytovatele širokopásmových IP služeb.

## Klíčové vlastnosti

- Koncový bod pro GTP tunely z jádrové sítě (rozhraní Gn/S5/S8)
- Přidělování a správa IP adres pro uživatelské zařízení (UE)
- Kotvící bod pro mobilitu, zajišťující kontinuitu relace během předávání
- Rozhraní k externím paketovým datovým sítím (PDN) přes rozhraní Gi/N6
- Integrační bod pro vynucování pravidel Policy and Charging Control (PCC)
- Generování účtovacích datových záznamů (CDR) pro datové relace uživatele

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements

---

📖 **Anglický originál a plná specifikace:** [IPDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipdt/)
