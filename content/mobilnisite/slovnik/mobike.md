---
slug: "mobike"
url: "/mobilnisite/slovnik/mobike/"
type: "slovnik"
title: "MOBIKE – IKEv2 Mobility and Multihoming Protocol"
date: 2025-01-01
abbr: "MOBIKE"
fullName: "IKEv2 Mobility and Multihoming Protocol"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mobike/"
summary: "MOBIKE je rozšíření protokolu Internet Key Exchange verze 2 (IKEv2), které umožňuje asociaci zabezpečení IPsec (SA) přežít změny základních IP adres koncových bodů. Je klíčové pro mobilní klienty VPN,"
---

MOBIKE je rozšíření protokolu IKEv2, které umožňuje asociaci zabezpečení IPsec přežít změny IP adres koncových bodů, což je klíčové pro plynulé připojení mobilních VPN při přechodech mezi sítěmi.

## Popis

MOBIKE (IKEv2 Mobility and Multihoming Protocol) je standardizovaný protokol definovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý v systémech 3GPP. Rozšiřuje základní protokol IKEv2, který je zodpovědný za vzájemnou autentizaci a vytváření asociací zabezpečení [IPsec](/mobilnisite/slovnik/ipsec/) (SA). Primární funkcí MOBIKE je umožnit, aby zavedená IKEv2 relace a s ní spojené podřízené asociace IPsec (Child SA) zůstaly aktivní i při změně IP adres jednoho nebo obou koncových bodů. Toho je dosaženo prostřednictvím odlehčeného aktualizačního mechanismu namísto úplného přerestartování.

Z architektonického hlediska MOBIKE funguje v rámci zásobníku protokolu IKEv2. Partnerské uzly s podporou MOBIKE si vyměňují nové informační datové bloky, konkrétně notifikaci UPDATE_SA_ADDRESSES. Když mobilní uzel zjistí změnu své IP adresy (např. kvůli přechodu mezi sítěmi), odešle tuto zprávu UPDATE_SA_ADDRESSES svému partnerovi a informuje jej o nové adrese. Partner aktualizaci potvrdí a obě strany následně přesměrují IPsec provoz ([ESP](/mobilnisite/slovnik/esp/)/[AH](/mobilnisite/slovnik/ah/)) na nové zdrojové/cílové adresy. Samotná IKEv2 SA, která obsahuje kryptografické klíče a identity, zůstává nezměněna. Tento proces zachovává stav relace a vyhýbá se výpočetní režii a přerušení služby spojenému s úplnou výměnou [IKE](/mobilnisite/slovnik/ike/)_SA_INIT a IKE_AUTH.

Klíčovými komponentami v transakci MOBIKE jsou iniciátor a respondent IKEv2 s podporou MOBIKE. Protokol zahrnuje mechanismy pro testování cesty (pomocí kontrol návratové dosažitelnosti) za účelem ověření, zda je nová adresa dosažitelná, a pro prevenci útoků zaplavením. Podporuje také scénáře překladu síťových adres ([NAT](/mobilnisite/slovnik/nat/)). V rámci 3GPP je MOBIKE zvláště relevantní pro scénáře jako je integrace přístupu mimo 3GPP (např. nedůvěryhodná WLAN) s jádrem 5G, kde UE používá IPsec tunely přes [N3IWF](/mobilnisite/slovnik/n3iwf/). Když se UE pohybuje, MOBIKE umožňuje, aby byl IPsec tunel mezi UE a N3IWF plynule udržován i při změnách IP adres, což zajišťuje nepřetržitý zabezpečený přístup ke službám jádra 5G sítě.

## K čemu slouží

MOBIKE byl vytvořen k vyřešení zásadního problému tradičních VPN s [IPsec](/mobilnisite/slovnik/ipsec/): jsou křehké v mobilním prostředí. Standardní IKEv2 váže asociace zabezpečení (SA) na konkrétní IP adresy. Pokud se IP adresa klienta změní – což je běžné u zařízení přecházejících mezi Wi-Fi sítěmi nebo při přechodu v mobilní síti – stávající IPsec SA se stanou neplatnými a připojení VPN se přeruší. To vynutí úplné nové připojení VPN, což způsobí přerušení služby, zvýšenou signalizační zátěž a špatný uživatelský zážitek.

Protokol řeší omezení předchozích přístupů tím, že odděluje asociaci zabezpečení IKEv2 od konkrétních IP adres koncových bodů. Před MOBIKE řešení zahrnovala použití stabilních virtuálních IP adres nebo Mobile IP, což přidávalo složitost. MOBIKE integruje podporu mobility přímo do IKEv2 a poskytuje standardizované, odlehčené řešení. Jeho přijetí v 3GPP, zejména od vydání 8 pro rané architektury EPS/SAE a posílené v pozdějších vydáních pro 5G, bylo motivováno potřebou zabezpečené a plynulé mobility napříč heterogenními přístupovými sítěmi. Umožňuje trvale zapnutá VPN pro firemní přístup a je nezbytné pro konvergenci přístupu 3GPP a mimo 3GPP v architektuře 5G, což umožňuje UE udržovat trvalé zabezpečené připojení k jádru sítě bez ohledu na změny přístupové technologie.

## Klíčové vlastnosti

- Umožňuje přežití asociace zabezpečení IPsec při změnách IP adres
- Používá odlehčenou signalizaci UPDATE_SA_ADDRESSES namísto úplného přerestartování IKE
- Zahrnuje kontroly návratové dosažitelnosti pro ověření zabezpečení a dosažitelnosti
- Podporuje scénáře překladu síťových adres (NAT)
- Udržuje stav relace IKEv2 a kryptografické klíče během mobility
- Nezbytné pro plynulou mobilitu při propojování 3GPP a mimo 3GPP (např. přes N3IWF)

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)
- [N3IWF – Non-3GPP access InterWorking Function](/mobilnisite/slovnik/n3iwf/)

## Definující specifikace

- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 33.822** (Rel-8) — Security Architecture for Inter-Access Mobility
- **TR 33.938** (Rel-19) — 3GPP Cryptographic Inventory for 5G

---

📖 **Anglický originál a plná specifikace:** [MOBIKE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mobike/)
