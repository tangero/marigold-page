---
slug: "paa"
url: "/mobilnisite/slovnik/paa/"
type: "slovnik"
title: "PAA – PDN Address Allocation"
date: 2025-01-01
abbr: "PAA"
fullName: "PDN Address Allocation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/paa/"
summary: "PDN Address Allocation (PAA) je parametr v protokolech 3GPP, který specifikuje IP adresu přidělenou UE pro připojení k Packet Data Network (PDN), například IPv4, IPv6 nebo obojí. Je přenášen v signali"
---

PAA je parametr protokolu 3GPP, který specifikuje IP adresu přidělenou UE pro připojení k PDN a je přenášen v signalizačních zprávách během navazování spojení.

## Popis

[PDN](/mobilnisite/slovnik/pdn/) Address Allocation (PAA) je klíčový informační element definovaný ve specifikacích 3GPP, konkrétně v TS 29.274 pro [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), který slouží k předání IP adresy přidělené uživatelskému zařízení (UE) pro připojení k Packet Data Network (PDN). Když se UE připojí k síti a vyžádá si PDN konektivitu – například pro přístup k internetu nebo službě IMS – jádro sítě přidělí IP adresu a sdělí ji UE prostřednictvím parametru PAA. Tento parametr je obsažen v [GTP-C](/mobilnisite/slovnik/gtp-c/) (GTP Control Plane) zprávách, jako jsou Create Session Request/Response, které si vyměňují Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)), Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v 4G nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v 5G. PAA obsahuje skutečné hodnoty adres, což může být IPv4 adresa, IPv6 prefix nebo obojí (dual-stack), spolu s dalšími poli, jako je typ adresy a délka.

Technicky PAA funguje jako součást procedury navazování PDN konektivity. Na žádost UE PGW/SMF spolupracuje se servery dynamického hostitelského konfiguračního protokolu ([DHCP](/mobilnisite/slovnik/dhcp/)) nebo interními fondy adres, aby přidělil IP adresu na základě předplatitelských dat a síťových politik. Přidělená adresa je poté zapouzdřena do pole PAA v GTP zprávě odeslané SGW/UPF, která ji přepošle Mobility Management Entity (MME) nebo Access and Mobility Management Function (AMF). Nakonec je doručena UE prostřednictvím NAS (Non-Access Stratum) signalizace, což UE umožní nakonfigurovat své síťové rozhraní. PAA zajišťuje, že jak UE, tak síťové uzly (např. PGW, SGW) mají konzistentní informace o adrese pro nastavení tunelů uživatelské roviny (GTP-U) a správné směrování datových paketů.

Role PAA v síti je zásadní pro správu IP adres v mobilním broadbandu. Umožňuje bezproblémovou mobilitu tím, že zajišťuje, aby UE zachovalo svou IP adresu během předávání hovoru, což je podporováno procedurami přenosu GTP kontextu. PAA také podporuje pokročilé funkce, jako jsou vícečetná PDN připojení na jedno UE, kde každé připojení může mít jiný PAA pro oddělené služby (např. internet a IMS). V systémech 5G je PAA adaptován v rámci Packet Forwarding Control Protocol (PFCP) a rozhraní založených na službách, ale koncept zůstává podobný. Integruje se s řízením politik (PCRF/PCF) pro přidělování adres na základě profilů QoS nebo požadavků síťového řezání, což zajišťuje, že konkrétní řezy obdrží odpovídající rozsahy adres.

Navíc PAA usnadňuje překlad síťových adres (NAT) a průchod firewallem tím, že poskytuje externí IP adresu přidělenou UE. Bezpečnostní aspekty zahrnují ochranu proti falšování adres, protože síť ověřuje konzistenci PAA během správy relací. Parametr je také používán v záznamech pro účtování, aby bylo možné asociovat využití dat s konkrétními IP adresami pro účely fakturace. Celkově je PAA základním kamenem IP konektivity v sítích 3GPP, který překlenuje propast mezi mobilní signalizací a infrastrukturou Internet Protocol.

## K čemu slouží

PAA byl zaveden za účelem standardizace metody přidělování a sdělování IP adres UE v paketově přepínaných mobilních sítích, čímž řeší problém dynamického přidělování adres v mobilním prostředí. Před jeho definicí v 3GPP Release 8 s EPS (Evolved Packet System) byly mechanismy přidělování adres méně sjednocené a spoléhaly se na výrobcem specifická rozšíření nebo samostatné protokoly, jako je DHCP over the air, což mohlo vést k problémům s interoperabilitou a neefektivní správou zdrojů. Motivací pro PAA byl přechod na plně IP sítě v LTE, kde každá datová relace vyžaduje pro směrování jedinečnou IP adresu a síť musí zvládat nedostatek adres (zejména IPv4) a zároveň podporovat migraci na IPv6.

Historicky, v systémech 2G/3G GPRS, bylo přidělování IP adres řešeno přes GGSN a aktivaci PDP kontextu, ale signalizace nebyla tak efektivní. PAA řešil tato omezení vložením informací o adrese přímo do GTP-C zpráv, čímž snížil signalizační režii a umožnil rychlejší nastavení relace. To bylo klíčové pro podporu trvalé konektivity a bezproblémové kontinuity služeb, protože UE mohly rychle obnovit PDN připojení s konzistentními adresami během událostí mobility. Také řešilo výzvu dual-stack provozu, umožňující současné přidělení IPv4 a IPv6 adres, aby se usnadnil přechod na IPv6 bez narušení stávajících služeb.

Dále PAA umožňuje síťovým operátorům implementovat sofistikované politiky správy adres, jako je přidělování adres z různých fondů na základě APN (Access Point Name), úrovně předplatitele nebo síťového řezu. To podporuje segregaci provozu, zvýšenou bezpečnost a efektivní využití adresního prostoru. Standardizací PAA napříč síťovými elementy zajistilo 3GPP, že nasazení s více výrobci mohou spolehlivě spolupracovat, což snižuje náklady a složitost. Jeho vývoj v následujících releasech zahrnoval vylepšení pro 5G, jako je integrace s architekturou založenou na službách, čímž si zachoval svou roli klíčového enableru pro IP konektivitu v moderních mobilních sítích.

## Klíčové vlastnosti

- Přenáší přidělenou IP adresu (IPv4, IPv6 nebo dual-stack) v GTP signalizaci
- Používá se během procedur navazování a modifikace PDN konektivity
- Podporuje dynamické přidělování adres ze síťových fondů nebo DHCP
- Umožňuje bezproblémové zachování IP adresy během mobility
- Integruje se s řízením politik pro přidělování adres na základě předplatného
- Usnadňuje účtování a fakturaci prostřednictvím asociace adres v záznamech

## Související pojmy

- [PDN – Packet Data Network](/mobilnisite/slovnik/pdn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [PAA na 3GPP Explorer](https://3gpp-explorer.com/glossary/paa/)
