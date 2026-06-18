---
slug: "lwipep"
url: "/mobilnisite/slovnik/lwipep/"
type: "slovnik"
title: "LWIPEP – LWIP Encapsulation Protocol"
date: 2025-01-01
abbr: "LWIPEP"
fullName: "LWIP Encapsulation Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lwipep/"
summary: "LWIPEP je protokolová entita zodpovědná za generování a zpracování LWIP PDUs v rámci funkce LTE-WLAN Radio Level Integration with IPsec Tunnel. Je umístěna v UE a eNB a zajišťuje enkapsulaci a dekapsu"
---

LWIPEP je protokolová entita v UE a eNB, která zajišťuje enkapsulaci a dekapsulaci uživatelských dat do PDUs zabezpečených IPsec pro přenos přes nedůvěryhodnou WLAN v rámci integrace LTE-WLAN na rádiové úrovni.

## Popis

[LWIP](/mobilnisite/slovnik/lwip/) Encapsulation Protocol (LWIPEP) je funkční entita definovaná 3GPP pro funkci LTE [WLAN](/mobilnisite/slovnik/wlan/) Radio Level Integration with [IPsec](/mobilnisite/slovnik/ipsec/) Tunnel (LWIP). Jedná se o klíčovou protokolovou vrstvu v uživatelské rovině, která funguje jak v uživatelském zařízení (UE), tak v eNodeB ([eNB](/mobilnisite/slovnik/enb/)). Hlavní úlohou LWIPEP je připravit uživatelská data pro bezpečný přenos přes nedůvěryhodnou WLAN přístupovou síť vytvořením specifické LWIP Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)). Logicky se nachází nad IP vrstvou odpovědnou za IPsec tunel a pod vyššími vrstvami, které poskytují původní IP pakety (nebo Ethernetové rámce) z aplikací.

Ve směru vysílání (např. uplink z UE) entita LWIPEP v UE přijme IP paket z aplikačních vrstev. Jejím úkolem je sestavit payload, který bude chráněn IPsec Encapsulating Security Payload ([ESP](/mobilnisite/slovnik/esp/)). To může zahrnovat enkapsulaci původního IP paketu uvnitř Ethernetového rámce, pokud to vyžaduje podkladový WLAN spoj (závisí na konfiguraci sítě). Tento sestavený payload (buď původní IP paket, nebo Ethernetový rámec, který jej obsahuje) je pak předán IP vrstvě, která se stane zdrojem pro IPsec ESP tunel. Výsledný zabezpečený IP paket, což je LWIP PDU, je následně odeslán přes WLAN rozhraní. V eNB přijímající entita LWIPEP provede inverzní operaci poté, co IPsec tunel zpracuje a dešifruje paket: extrahuje původní payload (IP paket nebo Ethernetový rámec) z LWIP PDU a vhodně jej přepošle směrem k rozhraní [S1-U](/mobilnisite/slovnik/s1-u/) do core sítě.

Činnost protokolu je přísně řízena eNB pomocí [RRC](/mobilnisite/slovnik/rrc/) signalizace. eNB nakonfiguruje UE LWIP parametry, včetně bezpečnostních parametrů pro IPsec tunel a pokynů, jak má LWIPEP provádět enkapsulaci. Neexistuje samostatná hlavička LWIPEP; enkapsulace je definována strukturou payloadu předaného IPsec. Funkce LWIPEP je tedy procedurální, nikoli založená na hlavičce. Její role je klíčová pro to, aby se WLAN spoj jevil jako bezpečný virtuální layer-2 kanál k eNB, což umožňuje eNB provádět řízení provozu a agregaci na úrovni bearerů mezi LTE a WLAN rádiovými rozhraními bez zapojení core sítě do cesty uživatelské roviny.

## K čemu slouží

LWIPEP byla vytvořena jako nezbytná součást pro realizaci cíle funkce LWIP, kterým je bezpečná integrace WLAN na rádiové úrovni. Řeší problém potřeby standardizované metody pro formátování uživatelských dat pro bezpečný přenos přes IPsec tunel končící v eNB. Bez LWIPEP by nebyl definován postup, jak se UE a eNB dohodnout na enkapsulaci různých typů uživatelského provozu (IPv4, IPv6, Ethernet) do jednotného payloadu pro IPsec tunel, což je nezbytné pro interoperabilitu a správné zpracování na obou koncích.

Před LWIP řešení pro nedůvěryhodný WLAN přístup, jako je ePDG, končila IPsec tunel v core síti, čímž oddělovala rádiové řízení (eNB) od bezpečnostního koncového bodu. LWIPEP umožňuje, aby koncovým bodem bylo samo eNB, což je klíčová inovace. Tím se řeší problém latence a zpoždění řízení, protože eNB nyní může okamžitě rozhodovat o směrování a přímo spravovat rádiové prostředky LTE i WLAN. Motivací pro definici LWIPEP bylo poskytnout jasný, normativní popis zpracování v uživatelské rovině vyžadovaného na obou koncích IPsec tunelu, což zajišťuje, že LTE bearery mohou být bezproblémově a bezpečně rozšířeny přes jakoukoli WLAN infrastrukturu, čímž se zvyšuje kapacita sítě a datové rychlosti uživatelů při zvýšené bezpečnosti.

## Klíčové vlastnosti

- Funkční entita odpovědná za sestavení payloadu pro LWIP IPsec tunel
- Definuje proceduru enkapsulace uživatelských IP paketů (nebo Ethernetových rámců) do LWIP PDU
- Funguje jak v UE, tak v eNB jako symetrická protokolová entita
- Konfigurována eNB pomocí RRC signalizace pro parametry, jako je režim enkapsulace
- Spolupracuje s IPsec ESP pro zajištění end-to-end bezpečnosti mezi UE a eNB přes WLAN
- Umožňuje eNB zacházet s WLAN spojem jako s bezpečnou layer-2 přenosovou cestou pro LTE bearery

## Související pojmy

- [LWIP – LTE WLAN Radio Level Integration with IPsec Tunnel](/mobilnisite/slovnik/lwip/)
- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [ESP – Efficiency Speed Percentage product](/mobilnisite/slovnik/esp/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [EPDG – Evolved Packet Data Gateway](/mobilnisite/slovnik/epdg/)

## Definující specifikace

- **TS 36.361** (Rel-19) — LWIP Encapsulation Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [LWIPEP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwipep/)
