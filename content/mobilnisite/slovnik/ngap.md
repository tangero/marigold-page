---
slug: "ngap"
url: "/mobilnisite/slovnik/ngap/"
type: "slovnik"
title: "NGAP – Next Generation Application Protocol"
date: 2026-01-01
abbr: "NGAP"
fullName: "Next Generation Application Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ngap/"
summary: "NGAP je signalizační protokol mezi 5G páteřní sítí (5GC) a rádiovou přístupovou sítí nové generace (NG-RAN). Je nezbytný pro zřizování, správu a uvolňování kontextů koncového zařízení (UE), pro řízení"
---

NGAP je signalizační protokol mezi 5G páteřní sítí (5G Core) a rádiovou přístupovou sítí nové generace (NG-RAN), nezbytný pro zřizování, správu a uvolňování kontextů koncového zařízení (UE), pro řízení mobility a pro přenos zpráv NAS.

## Popis

Protokol aplikací nové generace (Next Generation Application Protocol - NGAP) je klíčový signalizační protokol definovaný konsorciem 3GPP pro rozhraní mezi 5G páteřní sítí (5GC) a rádiovou přístupovou sítí nové generace (NG-RAN), konkrétně gNB nebo ng-eNB. Funguje nad transportní vrstvou [SCTP](/mobilnisite/slovnik/sctp/) na rozhraní [NG](/mobilnisite/slovnik/ng/) ([N2](/mobilnisite/slovnik/n2/) pro řídicí rovinu). NGAP je zodpovědný za veškerou signalizaci řídicí roviny mezi těmito dvěma doménami, což umožňuje páteřní síti spravovat RAN a naopak. Mezi jeho primární funkce patří zřizování, modifikace a uvolňování kontextu koncového zařízení (UE) v RAN, což je zásadní pro jakoukoliv datovou nebo signalizační relaci. NGAP také zajišťuje přenos signalizačních zpráv nezávislých na přístupové vrstvě (Non-Access Stratum - [NAS](/mobilnisite/slovnik/nas/)) mezi koncovým zařízením (UE) a funkcí [AMF](/mobilnisite/slovnik/amf/), což znamená, že RAN tyto zprávy transparentně přeposílá bez jejich interpretace. Dále protokol řídí procedury mobility koncového zařízení, jako jsou přechody (handover) uvnitř 5G systému a z předchozích systémů, a podporuje iniciování hromadného vyhledávání (Paging) z páteřní sítě do RAN. Protokol je navržen jako modulární a s ohledem na budoucí kompatibilitu, s modelem založeným na procedurách, kde je každá elementární procedura ([EP](/mobilnisite/slovnik/ep/)) definována buď jako třída 1 (vyžadující odpověď), nebo třída 2 (bez odpovědi). Mezi klíčové zprávy NGAP patří INITIAL UE MESSAGE, DOWNLINK NAS TRANSPORT, UPLINK NAS TRANSPORT, HANDOVER REQUIRED a PAGING. Jeho architektura odděluje správu uživatelské roviny (zajišťovanou jinými protokoly na rozhraní N3) a signalizaci řídicí roviny, čímž poskytuje čistý, efektivní a škálovatelný mechanismus pro řízení sítě. NGAP je základním kamenem architektury 5G založené na službách (Service-Based Architecture - [SBA](/mobilnisite/slovnik/sba/)), umožňuje flexibilní interakci síťových funkcí a podporuje pokročilé funkce, jako je síťové dělení (network slicing), přenosem informací o řezech mezi RAN a páteří.

## K čemu slouží

NGAP byl vytvořen, aby poskytl jednotný, efektivní a budoucím vývoji odolný signalizační protokol pro 5G systém, který nahrazuje a rozšiřuje funkčnost protokolů jako S1-AP ze 4G EPS. Přechod na 5G přinesl novou architekturu páteře založenou na službách (5GC) a nové požadavky na RAN, jako je podpora síťového dělení (network slicing), komunikace s ultra-spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)) a hromadného internetu věcí (IoT). Starší protokol S1-AP nebyl navržen tak, aby nativně přenášel informační prvky potřebné pro tyto nové služby a architektonické paradigmy. NGAP tento problém řeší tím, že je od základu navržen pro 5G, s explicitní podporou asistenčních informací pro výběr síťového řezu (NSSAI), více PDU relací na jedno koncové zařízení (UE) a diferencovaných toků QoS. Odstraňuje omezení předchozích přístupů tím, že nabízí větší flexibilitu, lepší efektivitu pro řídicí signalizaci a inherentní podporu pro oddělení řídicí a uživatelské roviny, což je klíčový princip 5G architektury. Jeho vytvoření bylo motivováno potřebou protokolu, který by dokázal škálovat pro podporu výrazně zvýšeného počtu připojených zařízení, různorodých požadavků služeb a cloud-nativních síťových funkcí, čímž umožňuje naplnění celé vize 5G.

## Klíčové vlastnosti

- Spravuje zřizování, modifikaci a uvolňování kontextu koncového zařízení (UE) v RAN
- Transparentně přenáší signalizační zprávy NAS mezi koncovým zařízením (UE) a funkcí AMF
- Řídí procedury mobility koncového zařízení včetně přechodů (handover) uvnitř systému a mezi systémy
- Iniciuje hromadné vyhledávání (Paging) koncových zařízení z páteřní sítě do RAN
- Přenáší klíčové informace pro výběr síťového řezu (NSSAI)
- Podporuje zřizování a správu více PDU relací na jedno koncové zařízení (UE)

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 29.214** (Rel-19) — Policy and Charging Control over Rx
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 33.836** (Rel-16) — Security Study for Advanced V2X Services
- **TR 33.847** (Rel-17) — 5G Proximity Services Security Study
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.414** (Rel-19) — NG Interface User Plane Protocol
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification

---

📖 **Anglický originál a plná specifikace:** [NGAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ngap/)
