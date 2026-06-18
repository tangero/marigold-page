---
slug: "nop"
url: "/mobilnisite/slovnik/nop/"
type: "slovnik"
title: "NOP – Network Operator"
date: 2026-01-01
abbr: "NOP"
fullName: "Network Operator"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nop/"
summary: "Subjekt (společnost nebo organizace), který vlastní, spravuje a poskytuje komerční služby mobilní sítě účastníkům. NOP je zodpovědný za nasazení, provoz, údržbu sítě a obchodní vztahy a tvoří jádro ek"
---

NOP je subjekt, který vlastní, spravuje a poskytuje komerční služby mobilní sítě účastníkům a je zodpovědný za nasazení, provoz a údržbu sítě.

## Popis

Provozovatel sítě (NOP) je právní a komerční subjekt, který má licenci k využívání rádiového spektra a provozování veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). V architektuře 3GPP není NOP technickým protokolem, ale nadřazeným obchodním a provozním subjektem, který nasazuje a spravuje technickou infrastrukturu definovanou standardy 3GPP. Tato infrastruktura zahrnuje rádiovou přístupovou síť (RAN) s jejími základnovými stanicemi (eNodeB, gNB), síť jádra (EPC, 5GC) a všechny přidružené správní systémy. NOP vlastní klíčový kód mobilní sítě ([MNC](/mobilnisite/slovnik/mnc/)), který v kombinaci s kódem mobilní země ([MCC](/mobilnisite/slovnik/mcc/)) jednoznačně identifikuje jeho PLMN na celém světě. Toto PLMN ID je vysíláno každou buňkou a používá se uživatelským zařízením (UE) pro výběr sítě, připojení a roaming.

Role NOP zahrnuje několik klíčových provozních oblastí. Z obchodního hlediska získává licence na spektrum od národních regulátorů, definuje tarify služeb, spravuje vztahy se zákazníky (často prostřednictvím značkových poskytovatelů služeb) a uzavírá roamingové dohody s dalšími NOP. Technicky je provozní tým NOP zodpovědný za plánování sítě (získávání lokalit pro buňky, plánování kapacity), nasazení (instalace a uvedení do provozu síťových prvků), každodenní provoz (monitorování stavu a výkonu sítě) a údržbu (softwarové aktualizace, opravy hardwaru, optimalizace). To je usnadněno systémy pro provoz, správu a údržbu ([OAM](/mobilnisite/slovnik/oam/)), které jsou standardizovány ve specifikacích 3GPP, například v řadě TS 32 pro správu telekomunikací.

Dále NOP implementuje pravidla řízení politiky a účtování, která řídí přístup účastníků a fakturaci. Konfiguruje funkci pro pravidla politiky a účtování ([PCRF](/mobilnisite/slovnik/pcrf/) v EPC, [PCF](/mobilnisite/slovnik/pcf/) v 5GC), aby vynucovala politiky kvality služeb (QoS), limity datového využití a účtovací modely. NOP také spravuje data účastníků v domácím registru účastníků ([HSS](/mobilnisite/slovnik/hss/)) nebo v jednotné správě dat ([UDM](/mobilnisite/slovnik/udm/)). V moderních architekturách, zejména s dělením sítě (network slicing) v 5G, se role NOP rozšiřuje o vytváření, orchestraci a správu izolovaných logických sítí (řezů) přizpůsobených pro různé segmenty zákazníků (např. masivní IoT, rozšířené mobilní širokopásmové připojení, kritické komunikace) na sdílené fyzické infrastruktuře.

## K čemu slouží

Koncept provozovatele sítě je základním stavebním kamenem struktury mobilního průmyslu a existuje proto, aby vlastnil a spravoval komplexní, kapitálově náročnou infrastrukturu vyžadovanou pro plošné bezdrátové komunikace. Řeší problém poskytování spolehlivé, všudypřítomné a standardizované služby veřejnosti a podnikům. Bez licencovaného NOP by nebyl žádný centralizovaný subjekt, který by zajišťoval pokrytí sítě, interoperabilitu, zabezpečení a soulad s národními předpisy. Model NOP motivuje k rozsáhlým investicím do síťových technologií, které pohánějí inovace a rozšiřování mobilních služeb.

Historicky se tato role vyvinula ze státních telefonních monopolů do konkurenčního prostředí s více operátory, které vidíme dnes. Standardy 3GPP jsou navrženy tak, aby tento ekosystém umožnily tím, že zajistí interoperabilitu UE s jakoukoli kompatibilní sítí, což podporuje konkurenci a možnost volby pro spotřebitele. NOP řeší omezení izolovaných proprietárních sítí dodržováním společných standardů, které umožňují klíčové funkce v celém odvětví, jako je mezinárodní roaming. Kontinuální vývoj prostřednictvím vydání 3GPP (od Rel-8 do Rel-20) odráží potřebu NOP spravovat stále složitější služby – od základního hlasu a SMS ve 2G/3G po vysokorychlostní data, IoT a ultra-spolehlivé komunikace s nízkou latencí v 4G a 5G – a to vše při zachování provozní efektivity a zkoumání nových obchodních modelů, jako je síť jako služba a dělení sítě.

## Klíčové vlastnosti

- Držitel licencovaného identifikátoru PLMN (MCC+MNC)
- Vlastník a správce fyzické a logické síťové infrastruktury
- Zodpovědný za nasazení, provoz, údržbu a optimalizaci sítě
- Subjekt, který uzavírá roamingové dohody s dalšími operátory
- Konfiguruje a řídí síťové politiky, účtování a správu dat účastníků
- Může vytvářet a spravovat více síťových řezů pro různé typy služeb v 5G

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)

## Definující specifikace

- **TS 23.434** (Rel-20) — Service Enabler Architecture for Verticals
- **TS 23.435** (Rel-19) — Network Slice Capability Exposure Procedures
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 28.530** (Rel-19) — Network Slicing Concepts & Requirements
- **TR 28.808** (Rel-17) — 5G satellite integration management study
- **TR 28.812** (Rel-17) — Study on Intent Driven Management Services
- **TR 28.824** (Rel-18) — Technical Report on Network Slice Capability Exposure
- **TR 28.841** (Rel-18) — Technical Report on IoT NTN Enhancements
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TS 28.879** (Rel-19) — OAM for Service Management Exposure Study
- **TR 32.847** (Rel-18) — Technical Report
- **TS 34.131** (Rel-19) — SIM API C Language Test Specification

---

📖 **Anglický originál a plná specifikace:** [NOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nop/)
