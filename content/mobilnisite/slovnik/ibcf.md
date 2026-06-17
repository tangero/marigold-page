---
slug: "ibcf"
url: "/mobilnisite/slovnik/ibcf/"
type: "slovnik"
title: "IBCF – Interconnection Border Control Functions"
date: 2025-01-01
abbr: "IBCF"
fullName: "Interconnection Border Control Functions"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ibcf/"
summary: "Interconnection Border Control Function (IBCF) je základní prvek sítě v rámci IP Multimedia Subsystem (IMS), který slouží jako zabezpečená brána pro signalizaci založenou na protokolu SIP mezi sítěmi"
---

IBCF je základní prvek sítě IMS, který funguje jako bezpečná brána pro signalizaci SIP mezi sítěmi různých operátorů. Poskytuje skrytí topologie, propojení protokolů (interworking) a zabezpečení pro komunikaci mezi doménami.

## Popis

Interconnection Border Control Function (IBCF) je klíčová funkční entita v architektuře 3GPP IP Multimedia Subsystem (IMS), speciálně navržená pro správu hranice mezi IMS sítí operátora a externími sítěmi. Jejím hlavním úkolem je zpracovávat signalizaci protokolů Session Initiation Protocol (SIP) a Session Description Protocol (SDP) pro multimediální relace (jako hlas, video), které překračují hranice sítí. Umístěná na okraji sítě slouží IBCF jako první kontaktní bod pro příchozí signalizaci z jiných sítí a jako poslední bod pro odchozí signalizaci, čímž vynucuje interkonekční politiky operátora.

Z architektonického hlediska se IBCF nachází v rámci jádra IMS a uvnitř sítě rozhraní s Serving-Call Session Control Function (S-CSCF) a Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)). Navenek se připojuje k jiným sítím prostřednictvím rozhraní IBCF-Interconnection Border Control Function (IBCF) (Ic) nebo k ne-IMS sítím, jako je veřejná telefonní síť (PSTN), prostřednictvím rozhraní IBCF-TrGW (Transition Gateway) (Ic). Klíčovou komponentou často spojovanou s IBCF je Transition Gateway (TrGW), který zpracovává mediální rovinu. IBCF řídí TrGW pro funkce jako překlad síťových adres a portů ([NAPT](/mobilnisite/slovnik/napt/)) a propojení IPv4/IPv6.

IBCF plní několik zásadních funkcí. Za prvé poskytuje skrytí topologie tím, že odstraňuje nebo zastírá informace o vnitřní síti (jako názvy uzlů a IP adresy) ze zpráv SIP před jejich opuštěním domovské sítě, což zvyšuje bezpečnost. Za druhé provádí propojení protokolů (interworking), což může zahrnovat překlad mezi různými profily SIP (např. IMS SIP versus SIP-I pro PSTN) nebo mezi IPv4 a IPv6. Za třetí funguje jako Session Border Controller (SBC) pro signalizační rovinu, poskytuje řízení přístupu, kontrolu intenzity SIP provozu a ověřování formátu zpráv SIP. Za čtvrté autorizuje zřizování mediálních bearerů prostřednictvím řízení přidruženého TrGW. Nakonec může generovat záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) pro mezidoménové relace. Centralizací těchto hraničních funkcí IBCF zjednodušuje síťovou architekturu, zlepšuje zabezpečení a zajišťuje spolehlivé poskytování služeb mezi operátory.

## K čemu slouží

IBCF byla vytvořena, aby řešila základní výzvy spojené se zabezpečeným a spolehlivým propojováním sítí založených na IMS, a to jak s jinými IMS sítěmi, tak se staršími sítěmi s přepojováním okruhů. Před érou IMS bylo propojení operátorů pro hlasové služby z velké části zvládáno bránami pro přepojování okruhů (jako [GMSC](/mobilnisite/slovnik/gmsc/)) s relativně jednoduchou, ne-IP signalizací. Přechod na plně IP, SIP-bázované jádro pro multimediální služby přinesl nové komplikace: vystavení vnitřní topologie sítě prostřednictvím hlaviček SIP, bezpečnostní hrozby z nedůvěryhodných IP sítí, nutnost propojení různých verzí IP a potřeba sofistikovaného řízení relací a médií na hranici sítě.

IBCF tyto problémy řeší tím, že funguje jako standardizovaná, zabezpečená brána. Chrání vnitřní síťovou infrastrukturu operátora před vnějšími hrozbami a zabraňuje úniku informací. Umožňuje bezproblémové poskytování služeb mezi operátory používajícími potenciálně různé implementace IMS nebo profily SIP. Dále, když sítě přecházely z IPv4 na IPv6, se její funkce propojení protokolů stala nezbytnou pro udržení konektivity. Její zavedení ve specifikaci Release 7 spolu s kompletní architekturou IMS bylo klíčové pro to, aby se IMS stala životaschopnou technologií pro komerční, multioperatorní nabídky služeb, jako je Voice over LTE (VoLTE) a Rich Communication Services (RCS), což zajistilo, že příslib interoperabilních, IP-bázovaných multimédií může být realizován přes administrativní a technologické hranice.

## Klíčové vlastnosti

- Funguje jako signalizační brána SIP pro propojení mezi IMS sítěmi a mezi IMS a staršími sítěmi
- Poskytuje skrytí topologie odstraňováním informací o vnitřní síti ze zpráv SIP
- Provádí propojení protokolů (např. mezi IMS SIP a SIP-I, IPv4/IPv6)
- Řídí přidružený Transition Gateway (TrGW) pro funkce v mediální rovině, jako je NAPT
- Vynucuje bezpečnostní politiky a politiky řízení přístupu na síťové hranici
- Generuje záznamy o účtování pro mezidoménové relace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [BGCF – Breakout Gateway Control Function](/mobilnisite/slovnik/bgcf/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.849** (Rel-11) — Study on IMS Roaming Media Optimization
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.405** (Rel-7) — Conference Service Protocol Description
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.410** (Rel-8) — Protocol Description of HOLD Services
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- … a dalších 30 specifikací

---

📖 **Anglický originál a plná specifikace:** [IBCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/ibcf/)
