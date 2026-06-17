---
slug: "dsmip"
url: "/mobilnisite/slovnik/dsmip/"
type: "slovnik"
title: "DSMIP – Dual Stack Mobile IP"
date: 2025-01-01
abbr: "DSMIP"
fullName: "Dual Stack Mobile IP"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dsmip/"
summary: "DSMIP je protokol pro správu mobility, který umožňuje plynulý přechod (handover) zařízení s duálním zásobníkem IPv4 a IPv6 v sítích 3GPP. Rozšiřuje Mobile IP o podporu obou verzí IP současně, což zaří"
---

DSMIP je protokol pro správu mobility, který umožňuje plynulý přechod (handover) zařízení s duálním zásobníkem IPv4 a IPv6 v sítích 3GPP rozšířením Mobile IP o podporu obou verzí IP současně.

## Popis

Dual Stack Mobile IP (DSMIP) je síťový protokol pro mobilitu standardizovaný 3GPP a [IETF](/mobilnisite/slovnik/ietf/), navržený pro podporu zařízení pracujících s adresami IPv4 i IPv6 současně. Jde o rozšíření Mobile IPv6 (MIPv6) a Mobile IPv4, které umožňuje uživatelskému zařízení (UE) zachovat probíhající relace při pohybu mezi různými přístupovými sítěmi bez ohledu na používanou verzi IP. Architektura zahrnuje klíčové entity: mobilní uzel ([MN](/mobilnisite/slovnik/mn/), tj. UE), domácí agenta ([HA](/mobilnisite/slovnik/ha/)) a případně cizího agenta ([FA](/mobilnisite/slovnik/fa/)) v kontextech IPv4. DSMIP funguje tak, že umožňuje MN mít dvě přechodné adresy (care-of addresses) – jednu pro IPv4 a jednu pro IPv6 – registrované u HA. HA pak tuneluje pakety na aktuální polohu MN a zajišťuje zapouzdření i rozbalení pro obě rodiny IP. Tento přístup s duálním zásobníkem zajišťuje, že MN může komunikovat s protistranami pomocí IPv4 nebo IPv6, přičemž mobilita je pro aplikace vyšších vrstev transparentní.

Při provozu, když se UE s podporou DSMIP připojí k síti, získá místní IP adresy (přechodné adresy) prostřednictvím mechanismů jako DHCPv4 nebo bezstavová autokonfigurace IPv6. Následně odešle aktualizace vazby (binding updates) svému domácímu agentovi, který udržuje vyrovnávací paměť vazeb (binding cache) asociující domácí adresu(y) MN s jeho aktuálními přechodnými adresami. Pro provoz IPv6 používá HA tunelování IPv6-in-IPv6; pro provoz IPv4 používá tunelování IPv4-in-IPv4 nebo IPv4-in-IPv6 v závislosti na scénáři. DSMIP také podporuje optimalizaci směrování pro snížení latence tím, že umožňuje přímou komunikaci mezi MN a protistranami po počáteční signalizaci. Protokol je specifikován v dokumentech 3GPP jako TS 33.107 a TS 33.108, které se zaměřují na bezpečnostní aspekty a integraci s autentizačními rámci 3GPP.

Úloha DSMIP v sítích 3GPP spočívá v usnadnění plynulé mobility mezi heterogenními přístupovými technologiemi (např. mezi LTE a Wi-Fi) při současné podpoře koexistence IPv4 a IPv6. Integruje se s Evolved Packet Core (EPC) 3GPP prostřednictvím rozhraní jako S2a a S2b pro důvěryhodný a nedůvěryhodný přístup mimo 3GPP. Klíčové komponenty zahrnují klienta DSMIP na UE, HA v domácí síti a [AAA](/mobilnisite/slovnik/aaa/) servery pro autentizaci. Protokol zvládá přechody (handovery) aktualizací vazeb během pohybu, čímž minimalizuje ztrátu paketů a narušení relace. Jeho význam vzrostl s přechodem na IPv6, protože umožňuje operátorům zavádět sítě IPv6 při zachování služeb pro starší IPv4, čímž zajišťuje kontinuitu pro zařízení s duálním zásobníkem v mobilním prostředí.

## K čemu slouží

DSMIP byl vytvořen, aby řešil výzvy IP mobility v prostředích s duálním zásobníkem, kde sítě a zařízení podporují IPv4 i IPv6 současně. S rostoucím nasazením IPv6 vznikla potřeba mobilních řešení, která by dokázala plynule zvládat oba protokoly bez nutnosti samostatných mechanismů pro každou verzi IP. Předchozí přístupy jako MIPv4 a MIPv6 fungovaly nezávisle, což vedlo ke složitosti a neefektivitě pro zařízení s duálním zásobníkem. DSMIP to řeší sjednocením správy mobility, což umožňuje zařízením roamovat mezi sítěmi při zachování relací přes kteroukoli z rodin IP.

Historicky byl DSMIP představen v 3GPP Release 8 jako součást System Architecture Evolution (SAE) a Evolved Packet Core (EPC), motivován blížícím se vyčerpáním adres IPv4 a přechodem na IPv6. Umožnil mobilním operátorům zavádět sítě s podporou IPv6 při zajištění zpětné kompatibility se stávající infrastrukturou a zařízeními IPv4. Protokol zaplnil mezeru tím, že poskytl standardizovaný způsob podpory mobility pro UE s duálním zásobníkem, zejména pro integraci přístupu mimo 3GPP (např. Wi-Fi offload), kde je heterogenita verzí IP běžná.

Zavedením DSMIP chtělo 3GPP usnadnit hladkou migraci na IPv6, snížit provozní náklady a zlepšit uživatelský zážitek s nepřerušeným připojením. Řeší omezení dřívějších verzí Mobile IP tím, že zjednodušuje správu vazeb a snižuje signalizační režii pro operace s duálním zásobníkem. To umožnilo funkce jako síťově řízená správa mobility (PMIP) ve spojení s DSMIP, což podpořilo škálovatelná nasazení v LTE a dalších technologiích. V konečném důsledku hrál DSMIP klíčovou roli v zajištění, že mobilní služby se mohou vyvíjet spolu s trendy v IP síťování, a podpořil tak dlouhodobý růst mobilních dat.

## Klíčové vlastnosti

- Podporuje současnou správu mobility pro IPv4 a IPv6 prostřednictvím registrace dvou přechodných adres (dual care-of address)
- Integruje se s 3GPP EPC pro plynulý přechod (handover) mezi sítěmi 3GPP a přístupy mimo 3GPP
- Využívá tunelovací mechanismy (např. IPv6-in-IPv6, IPv4-in-IPv4) pro přeposílání paketů mezi domácím agentem (HA) a mobilním uzlem (MN)
- Obsahuje optimalizaci směrování pro snížení latence tím, že umožňuje přímou komunikaci s protistranou
- Zahrnuje bezpečnostní prvky jako IPsec a autentizaci 3GPP pro aktualizace vazeb (binding updates)
- Umožňuje zpětnou kompatibilitu a hladký přechod z IPv4 na IPv6 v mobilních sítích

## Definující specifikace

- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [DSMIP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dsmip/)
