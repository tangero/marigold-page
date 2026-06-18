---
slug: "apn"
url: "/mobilnisite/slovnik/apn/"
type: "slovnik"
title: "APN – Access Point Name"
date: 2026-01-01
abbr: "APN"
fullName: "Access Point Name"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/apn/"
summary: "Access Point Name (APN) je síťový identifikátor používaný mobilním zařízením pro připojení ke konkrétní paketové datové síti (PDN), jako je internet nebo privátní firemní síť. Určuje bránu (GGSN/PGW)"
---

APN je síťový identifikátor používaný mobilním zařízením pro připojení ke konkrétní paketové datové síti, který určuje bránu a způsob přidělení IP adresy pro směrování provozu a aplikaci služeb.

## Popis

Access Point Name (APN) je klíčový konfigurační parametr v paketově přepínaných sítích 3GPP, který slouží jako referenční bod k paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)). Strukturně je APN plně kvalifikovaný doménový název ([FQDN](/mobilnisite/slovnik/fqdn/)) složený ze dvou částí: APN Network Identifier (povinný), který specifikuje externí PDN, a APN Operator Identifier (volitelný), který identifikuje síť operátora. Když uživatelské zařízení (UE) iniciuje aktivaci [PDP](/mobilnisite/slovnik/pdp/) kontextu v 3G/UMTS nebo připojení k PDN v 4G/5G, zahrne APN. Síť použije tento APN k výběru příslušné brány Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) v UMTS nebo brány Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPS/5GC, která slouží jako kotvící bod k externí síti.

Po přijetí aktivační žádosti s APN provede Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v UMTS nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) v EPS/5GC DNS dotaz. Tento dotaz přeloží APN FQDN na IP adresu(y) vhodné brány (GGSN/PGW). Proces výběru zohledňuje profily účastníka, síťové politiky a vyrovnávání zátěže. Vybraná brána následně zřídí datovou relaci, přidělí UE IP adresu (často pomocí DHCP) a nastaví přenašeče uživatelské roviny pro datový provoz. APN tedy přímo určuje směrovací cestu, dosažitelnou externí síť a profil kvality služby (QoS) aplikovaný na připojení.

Role APN přesahuje pouhé připojení. Je vnitřně propojen s řízením politik a účtováním. Hodnota APN je používána funkcí Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF) k určení, která pravidla politiky a účtování se vztahují na datovou relaci účastníka. To operátorům umožňuje nabízet diferencované služby – například vyhrazené APN pro internet, MMS, IMS nebo podnikové VPN – každou s odlišnými limity šířky pásma, bezpečnostními nastaveními a modely účtování. V 5G se tento koncept vyvíjí s parametrem Data Network Name (DNN), který je funkčně ekvivalentní APN a poskytuje připojení ke konkrétní datové síti při současné integraci s dělením sítě a rozšířenými rámci politik.

## K čemu slouží

APN bylo zavedeno k řešení základního problému připojování mobilních účastníků k více různým paketovým datovým sítím mimo jádro mobilního operátora. V raném GPRS by bez takového identifikátoru byl veškerý datový provoz homogenně směrován do jediné externí sítě (jako je veřejný internet), což by znemožňovalo diferenciaci služeb, zabezpečený podnikový přístup a specializované služby jako WAP nebo MMS. APN poskytuje potřebné logické oddělení, které umožňuje síti vybírat různé brány a aplikovat specifické politiky na základě zamýšlené služby.

Historicky, před standardizovanými APN, bylo obtížné implementovat a spravovat datové služby s přidanou hodnotou. Mechanismus APN vytvořil škálovatelný, uživatelem konfigurovatelný způsob směrování relací. Vyřešil omezení ve směrování, účtování a kvalitě služby tím, že umožnil síti identifikovat cílovou PDN během zřizování relace. To bylo klíčové pro komerční úspěch mobilních dat, protože umožnilo operátorům nabízet služby ve vrstvách, spolupracovat s poskytovateli obsahu a podporovat zabezpečené podnikové připojení prostřednictvím vyhrazených APN s privátní adresací.

APN je navíc ústřední pro vynucování politik a účtování. Spojením relace s konkrétním APN mohou operátorů nasadit odlišná pravidla politiky pro tvarování provozu, řízení přístupu a kvalitu služby. Umožňuje přesné účtování – například dat použité na APN 'internet' se účtuje jinak než data na APN 'mms'. Tato flexibilita motivovala jeho vytvoření a trvalý vývoj a vytvořila základ pro pokročilejší parametr DNN v systémech 5G, který tuto roli nadále plní v rámci dělení sítě a architektur založených na službách.

## Klíčové vlastnosti

- Identifikuje externí paketovou datovou síť (PDN) pro směrování relace
- Používá se sítí k výběru příslušné brány (GGSN/PGW)
- Určuje metodu přidělení IP adresy pro UE
- Spouští specifická pravidla řízení politik a účtování (PCC)
- Umožňuje diferencované služby, QoS a účtování podle datové služby
- Konfigurováno na UE a ověřováno proti profilu účastníka v HSS/UDM

## Související pojmy

- [DNN – Data Network Name](/mobilnisite/slovnik/dnn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.234** (Rel-13) — 3GPP-WLAN Interworking Index Specification
- **TR 22.802** (Rel-14) — Study on Need for Multiple APNs in MTC
- **TR 22.934** (Rel-13) — 3GPP-WLAN Interworking Feasibility Study
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.180** (Rel-19) — MC services support in IOPS mode
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.327** (Rel-13) — 3GPP-WLAN Mobility Stage 2 Description
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- … a dalších 43 specifikací

---

📖 **Anglický originál a plná specifikace:** [APN na 3GPP Explorer](https://3gpp-explorer.com/glossary/apn/)
