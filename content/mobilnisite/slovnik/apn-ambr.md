---
slug: "apn-ambr"
url: "/mobilnisite/slovnik/apn-ambr/"
type: "slovnik"
title: "APN-AMBR – Access Point Name Aggregate Maximum Bit Rate"
date: 2025-01-01
abbr: "APN-AMBR"
fullName: "Access Point Name Aggregate Maximum Bit Rate"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/apn-ambr/"
summary: "APN-AMBR je parametr QoS, který omezuje celkovou maximální přenosovou rychlost na všech non-GBR přenosech spojených s konkrétním APN pro UE. Zajišťuje spravedlivé rozdělení zdrojů mezi více datovými t"
---

APN-AMBR je parametr QoS, který omezuje celkovou maximální přenosovou rychlost na všech non-GBR přenosech spojených s konkrétním Access Point Name pro uživatelské zařízení.

## Popis

APN-AMBR (Access Point Name Aggregate Maximum Bit Rate) je základní parametr kvality služeb (QoS) v architektuře Evolved Packet System (EPS) dle 3GPP, který řídí agregovanou datovou propustnost pro všechny přenosy nezaručené přenosové rychlosti (non-GBR) spojené s konkrétním Access Point Name ([APN](/mobilnisite/slovnik/apn/)) pro uživatelské zařízení (UE). Na rozdíl od parametrů QoS na úrovni přenosu, jako je [QCI](/mobilnisite/slovnik/qci/) (QoS Class Identifier) a [ARP](/mobilnisite/slovnik/arp/) (Allocation and Retention Priority), APN-AMBR působí na úrovni APN a uplatňuje kumulativní limit napříč více připojeními nebo přenosy Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)), které sdílejí stejný kontext APN. Tento agregovaný přístup je nezbytný, protože jediné UE může současně navázat více datových relací (např. internetový prohlížeč, streamování videa a korporátní [VPN](/mobilnisite/slovnik/vpn/)) přes stejný APN, každou potenciálně na samostatných přenosech EPS.

Parametr je vynucován ve dvou klíčových síťových uzlech: ve funkci User Plane Function ([UPF](/mobilnisite/slovnik/upf/)) v 5G Core nebo v Packet Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC a v gNodeB v 5G nebo eNodeB v LTE. Hlavní vynucení provádí uzel základní sítě (UPF/PGW), který zajišťuje, aby agregovaný provoz ve směru uplink a downlink pro všechny non-GBR přenosy náležející danému APN nepřekročil hodnoty předplaceného APN-AMBR. Současně uzel rádiové přístupové sítě (RAN) uplatňuje limit APN-AMBR přes rozhraní vzduchu, ale může rychlost dále omezovat na základě dostupných rádiových zdrojů a algoritmů plánování. Toto dvojí vynucení zajišťuje konzistentní tvarování provozu napříč segmenty základní i rádiové sítě.

APN-AMBR je definován dvěma samostatnými hodnotami: APN-AMBR pro uplink a APN-AMBR pro downlink, které jsou konfigurovány nezávisle. Tyto hodnoty jsou typicky součástí uživatelského předplatitelského profilu uloženého v Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo Home Subscriber Server (HSS) a jsou sděleny Session Management Function (SMF) nebo PGW během zřizování relace. SMF/PGW pak tyto limity předává UPF/PGW k vynucení a Access and Mobility Management Function (AMF) nebo Mobility Management Entity (MME), která následně informuje RAN. Důležité je, že APN-AMBR se uplatňuje pouze na non-GBR přenosy; přenosy GBR mají své vlastní vyhrazené zaručené přenosové rychlosti a jsou z tohoto agregovaného limitu vyloučeny.

Z pohledu technické implementace zahrnuje vynucení APN-AMBR algoritmy typu token bucket nebo leaky bucket v UPF/PGW ke sledování a tvarování agregovaného datového toku. Když agregovaná přenosová rychlost dosáhne limitu APN-AMBR, pakety mohou být podle síťových politik řízení zahlcení buffrovány, zpožděny nebo zahozeny. Tento mechanismus brání tomu, aby jediný APN spotřebovával nepřiměřené síťové zdroje, čímž chrání stabilitu sítě a zajišťuje rovnoměrné poskytování služeb všem uživatelům. Ve scénářích s více APN (kde se UE připojuje k různým APN, jako je 'internet' a 'IMS') má každý APN svůj vlastní nezávislý APN-AMBR, což umožňuje diferencované řízení služeb na základě typu aplikace nebo služby.

## K čemu slouží

APN-AMBR byl zaveden v 3GPP Release 8 spolu s EPS, aby řešil omezení dřívějších 3GPP architektur v řízení agregované spotřeby uživatelských dat. Před LTE/EPC mechanismy QoS v sítích 2G/3G primárně fungovaly na úrovni kontextu PDP (Packet Data Protocol) bez robustních agregovaných kontrol napříč více datovými relacemi. S vývojem smartphonů a mobilních aplikací začali uživatelé současně využívat více datově náročných služeb (např. streamování videa, sociální média a cloudová synchronizace) přes jediný síťový přístupový bod. Bez agregovaného limitu by tyto souběžné toky mohly společně přetížit síťové zdroje, což by vedlo k zahlcení, zhoršenému výkonu pro ostatní uživatele a nepředvídatelným scénářům fakturace.

Primární problém, který APN-AMBR řeší, je potřeba podrobného, na předplatném založeného řízení šířky pásma, které je v souladu jak s uživatelskými služebními plány, tak s plánováním kapacity sítě. Zavedením agregovaného stropu na APN mohou operátoři vynucovat politiky spravedlivého používání, předcházet zneužívání sítě a implementovat vrstvené nabídky služeb (např. rozlišování mezi prémiovými a standardními datovými plány). Například uživatel se základním předplatným může mít nižší APN-AMBR než uživatel s prémiovým plánem, i když oba používají stejné aplikace. Tato schopnost je klíčová pro monetizaci a diferenciaci služeb.

APN-AMBR navíc umožňuje efektivnější využití zdrojů rádiové i základní sítě. Řízením agregované propustnosti na APN může síť lépe spravovat priority plánování, snižovat zahlcení a udržovat celkovou stabilitu systému. Poskytuje také mechanismus pro implementaci politik uvědomujících si službu; například operátor může nastavit vyšší APN-AMBR pro vyhrazený APN 'video streaming' ve srovnání s obecným APN 'internet'. Tento historický vývoj od QoS na úrovni přenosu k zahrnutí agregovaných kontrol na úrovni APN odráží posun odvětví k sofistikovanějšímu řízení provozu tváří v tvář explodující poptávce po mobilních datech a různorodým požadavkům na služby.

## Klíčové vlastnosti

- Agregované omezení šířky pásma na všech non-GBR přenosech pro konkrétní APN
- Nezávislé vynucení maximální přenosové rychlosti pro uplink a downlink
- Dvojí vynucení jak v uzlech základní sítě (UPF/PGW), tak v uzlech rádiové přístupové sítě (RAN)
- Parametr založený na předplatném, uložený v UDM/HSS a uplatňovaný během zřizování relace
- Vyloučení GBR přenosů z agregovaného limitu za účelem zachování zaručených služebních toků
- Podpora více souběžných APN na UE s nezávislými hodnotami APN-AMBR na APN

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1

---

📖 **Anglický originál a plná specifikace:** [APN-AMBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/apn-ambr/)
