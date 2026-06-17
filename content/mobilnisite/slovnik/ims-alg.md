---
slug: "ims-alg"
url: "/mobilnisite/slovnik/ims-alg/"
type: "slovnik"
title: "IMS-ALG – IMS Application Level Gateway"
date: 2025-01-01
abbr: "IMS-ALG"
fullName: "IMS Application Level Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ims-alg/"
summary: "Síťová funkce usnadňující interoperabilitu protokolů SIP a SDP mezi sítěmi IPv4 a IPv6 v rámci IMS. Řeší problémy s průchodem přes NAT pro SIP multimediální relace a zajišťuje bezproblémovou komunikac"
---

IMS-ALG je síťová funkce v IMS, která zajišťuje interoperabilitu protokolů SIP a SDP mezi sítěmi IPv4 a IPv6 a řeší problémy s průchodem přes NAT pro multimediální relace.

## Popis

IMS Application Level Gateway (IMS-ALG) je klíčová funkce pro interoperabilitu definovaná v architektuře 3GPP IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je umožnit SIP multimediální relace mezi uživatelským zařízením (UE) a aplikačními servery nacházejícími se v různých doménách IP adres, konkrétně v sítích IPv4 a IPv6. IMS-ALG pracuje na aplikační vrstvě, kontroluje a upravuje zprávy protokolu Session Initiation Protocol (SIP) a Session Description Protocol (SDP) za účelem překladu IP adres a portů zabudovaných v signalizaci. Tento proces je zásadní, protože zprávy SIP a SDP nesou informace síťové vrstvy (jako IP adresy v hlavičkách Contact a v řádcích SDP 'c=' a 'm='), které musí být konzistentní a směrovatelné pro oba koncové body.

Architektonicky je IMS-ALG často nasazována společně s Transition Gateway (TrGW), která zajišťuje překlad na mediální rovině. IMS-ALG ovládá TrGW přes rozhraní Iq a instruuje ji k vytváření, úpravám nebo mazání vazeb pro mediální překlad. Tato rozdělená architektura odděluje zpracování signalizace a médií, což umožňuje škálovatelné a efektivní řešení průchodu přes [NAT](/mobilnisite/slovnik/nat/) a firewally. IMS-ALG spolupracuje s dalšími prvky IMS jádra, jako je Proxy-Call Session Control Function ([P-CSCF](/mobilnisite/slovnik/p-cscf/)) a Serving-Call Session Control Function (S-CSCF), aby se vložila do signalizační cesty pro relace vyžadující interoperabilitu.

Jeho činnost zahrnuje několik klíčových procesů. Během navazování relace IMS-ALG analyzuje SIP požadavky INVITE a odpovědi. Identifikuje privátní IPv4 adresy nebo IPv6 adresy, které nejsou globálně směrovatelné z druhé síťové domény, a nahrazuje je vhodnými globálně směrovatelnými adresami ze své vlastní domény. Také aktualizuje příslušné SIP hlavičky a atributy SDP, aby zachovala konzistenci relace. Dále IMS-ALG spravuje vazbu signalizačních a mediálních toků, což zajišťuje, že následné SIP zprávy (jako re-INVITE nebo UPDATE) a s nimi spojené mediální proudy jsou správně korelovány a přeloženy. To zajišťuje kontinuitu relace a mediální konektivitu od konce ke konci navzdory heterogenitě podkladových síťových adres.

V širším ekosystému IMS je IMS-ALG základním kamenem pro umožnění přechodu z IPv4 na IPv6 a pro podporu scénářů, kdy starší zařízení pouze s IPv4 potřebují komunikovat s moderními IMS službami podporujícími IPv6. Řeší kritický problém aplikačních bran (ALG) zabudovaných v zařízeních NAT, které nejsou obeznámeny se specifickým použitím SIP a SDP v IMS, což často přerušuje multimediální relace. Jako standardizovaná, síťová ALG uvnitř důvěryhodné domény IMS poskytuje spolehlivé a operátorem řízené řešení pro IP interoperabilitu, které je zásadní pro nasazení plně IP sítí a dlouhodobou životnost IMS služeb napříč vyvíjející se internetovou infrastrukturou.

## K čemu slouží

IMS-ALG byla vytvořena, aby vyřešila základní problém interoperability IP verzí a průchodu přes Network Address Translator ([NAT](/mobilnisite/slovnik/nat/)) pro SIP služby v IMS. Jak se sítě 3GPP vyvíjely směrem k plně IP architekturám ve verzi 5 a dále, IMS bylo navrženo tak, aby bylo nezávislé na IP verzi. Dlouhá koexistence sítí IPv4 a IPv6 však vytvořila scénář, kdy UE v síti IPv6 může potřebovat komunikovat s aplikačním serverem nebo jiným UE v síti IPv4 a naopak. Standardní zařízení NAT, která provádějí překlad IP adres a portů na síťové vrstvě, jsou typicky 'neuvědomující si SIP'. Nedokáží přeložit IP adresy a čísla portů zabudovaná v aplikační části dat SIP a SDP zpráv, což způsobuje selhání navázání relace.

Historicky řešení zahrnovala mechanismy na straně klienta (jako STUN, TURN, [ICE](/mobilnisite/slovnik/ice/)) nebo proprietární ALG v hraničních směrovačích. Ty byly nedostatečné pro nasazení IMS na úrovni operátora vyžadující škálovatelnost, bezpečnost a kontrolu operátora. IMS-ALG standardizuje síťové řešení uvnitř architektury IMS. Byla zavedena, aby poskytla spolehlivou, standardizovanou metodu, jak může síť pomoci při navazování relací napříč různými doménami adres, což je nezbytné pro globální nasazení IMS služeb bez omezení IP verzí přístupové sítě.

K jejímu vytvoření vedla potřeba zajistit zpětnou kompatibilitu a hladkou cestu přechodu, jak se internet přesouval z IPv4 na IPv6. Řeší omezení 'slepých' NATů tím, že je plně obeznámena s protokoly SIP a SDP, což jí umožňuje provádět potřebné překlady na aplikační vrstvě koordinovaným způsobem s překladem médií (přes TrGW). To zajišťuje, že IMS může poskytovat bezproblémové multimediální služby (hlas, video) napříč jakoukoli kombinací sítí IPv4 a IPv6, což je klíčové pro naplnění slibu univerzální konektivity IMS.

## Klíčové vlastnosti

- Překlad na aplikační vrstvě pro SIP a SDP
- Interoperabilita IPv4/IPv6 pro signalizaci IMS
- Ovládání Media Transition Gateway (TrGW) přes rozhraní Iq
- Asistence s průchodem přes NAT a firewally pro SIP relace
- Úprava SIP hlaviček (např. Via, Contact, Route) a atributů SDP
- Podpora stavovosti SIP dialogů a transakcí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)
- [NAT – Network Address Translation](/mobilnisite/slovnik/nat/)

## Definující specifikace

- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 33.328** (Rel-19) — IMS Media Plane Security Specification

---

📖 **Anglický originál a plná specifikace:** [IMS-ALG na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims-alg/)
