---
slug: "ap"
url: "/mobilnisite/slovnik/ap/"
type: "slovnik"
title: "AP – Application Processor"
date: 2026-01-01
abbr: "AP"
fullName: "Application Processor"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ap/"
summary: "Aplikační procesor (AP) je univerzální výpočetní platforma ve vybavení uživatele (UE), která provádí operační systém zařízení a uživatelské aplikace. Je oddělen od modemového procesoru (který zajišťuj"
---

AP je univerzální výpočetní platforma v mobilním zařízení, která provádí operační systém a uživatelské aplikace, odděleně od modemového procesoru zajišťujícího rádiovou komunikaci.

## Popis

V terminologii 3GPP označuje aplikační procesor (AP) hlavní výpočetní jednotku ve vybavení uživatele (UE), která je zodpovědná za běh vysokoúrovňového operačního systému (např. Android, iOS) a všech aplikací pro koncového uživatele. Je architektonicky oddělen od modemového procesoru (často nazývaného základnový procesor nebo [CP](/mobilnisite/slovnik/cp/) – komunikační procesor), který je vyhrazen pro provádění protokolového zásobníku 3GPP ([L1](/mobilnisite/slovnik/l1/)/[L2](/mobilnisite/slovnik/l2/)/[L3](/mobilnisite/slovnik/l3/)) pro buněčnou konektivitu (2G/3G/4G/5G). Toto oddělení je logickým a často i fyzikálním konstrukčním principem. AP komunikuje s modemem prostřednictvím standardizovaných nebo proprietárních interních rozhraní (např. sady AT příkazů, QMI, MBIM nebo integrovanějších vysokorychlostních sběrnic), aby mohl požadovat služby buněčných sítí, jako jsou datové relace, [SMS](/mobilnisite/slovnik/sms/) nebo hlasová volání.

Úlohou AP je poskytovat bohaté aplikační prostředí. Spravuje paměť zařízení, úložiště, displej, dotykový vstup, senzory a další periferie. Když aplikace potřebuje síťovou konektivitu, předá protokolový zásobník AP (např. [TCP/IP](/mobilnisite/slovnik/tcp-ip/)) data subsystému modemu přes definované rozhraní. AP je také zodpovědný za implementaci vyšších vrstev služeb definovaných 3GPP, jako je klient IMS pro VoLTE/VoNR, klient [SUPL](/mobilnisite/slovnik/supl/) pro [A-GNSS](/mobilnisite/slovnik/a-gnss/) nebo API pro zpřístupnění schopností zařízení. V mnoha moderních návrzích systému na čipu (SoC) mohou být AP a modem integrovány na stejném křemíkovém čipu, ale zůstávají logicky odděleny se zabezpečenou komunikací mezi procesory.

Z pohledu standardů 3GPP specifikace často odkazují na AP v kontextech týkajících se architektury zařízení, zabezpečení a implementace služeb. Například specifikace pro služby blízkosti (ProSe) nebo komunikaci vozidlo-se-vším (V2X) definují, jak zásobník V2X aplikací na AP interaguje se zásobníkem V2X protokolů v modemu. Specifikace zabezpečení podrobně popisují hranice důvěry mezi AP a modemem, zejména pro funkce jako zabezpečený start, ukládání přihlašovacích údajů na univerzální integrovaný obvodovou kartu (UICC) a ochrana integrity komunikace mezi oběma procesory.

Výkon a schopnosti AP přímo ovlivňují uživatelský zážitek, ale jsou z velké části mimo rozsah standardizace přístupu k rádiové síti nebo jádra sítě 3GPP. Nicméně 3GPP specifikuje požadavky na to, jak musí aplikace hostované na AP a modem spolupracovat, aby splnily síťové politiky, řídily spotřebu energie, podporovaly funkci dvojité SIM a umožňovaly funkce jako povědomí o síťovém dělení na zařízení. Vývoj směrem k výkonnějším AP byl klíčovým faktorem pro sofistikované mobilní služby, od streamování videa ve vysokém rozlišení po komplexní aplikace rozšířené reality, které všechny spoléhají na podkladovou konektivitu řízenou modemem.

## K čemu slouží

Architektonické oddělení aplikačního procesoru od modemového procesoru bylo motivováno potřebou specializace, nezávislé inovace a flexibility dodavatelského řetězce. Rané mobilní telefony používaly integrované procesory, kde byla komunikace a základní aplikační logika těsně propojeny. Jak se mobilní zařízení vyvinula v chytré telefony, výpočetní nároky grafického uživatelského rozhraní, multimédií a aplikací třetích stran prudce vzrostly. Bylo nutné zavést univerzální AP optimalizovaný pro vysoký výkon CPU/GPU a energetickou účinnost ve výpočetních úlohách. Mezitím modemový procesor vyžaduje hlubokou specializaci na zpracování signálu v reálném čase, přísné časování protokolů a řízení RF komponent. Jejich oddělení umožňuje každý z nich navrhovat, vyrábět a aktualizovat (např. prostřednictvím firmwaru) nezávisle.

Toto oddělení řeší kritické problémy ve vývoji a certifikaci zařízení. Modemové procesory procházejí rozsáhlou a nákladnou regulační a síťovou certifikací operátora pro rádiovou shodu. Izolací modemu lze AP a zbytek softwaru zařízení aktualizovat často (např. aktualizace OS) bez nutnosti přecertifikace rádiového hardwaru, za předpokladu, že rozhraní k modemu zůstává stabilní. Také to umožňuje ekosystém více dodavatelů, kde výrobci zařízení mohou integrovat AP od jednoho dodavatele (např. Qualcomm, Apple, Samsung) s modemy od jiného, což podporuje konkurenci a inovace.

Historicky zavedení této jasné demarkační linie v diskusích 3GPP kolem vydání 99 a pozdějších se časově shodovalo s nástupem otevřených OS platforem jako Symbian a později Android. Řešilo to omezení monolitických návrhů, které byly nepružné a zpomalovaly tempo aplikačních inovací. Architektura AP-modem je nyní základní, podporuje vše od levných IoT zařízení s jednoduchými AP až po vlajkové chytré telefony s vícejádrovými AP, které se všechny připojují prostřednictvím standardizovaných buněčných sítí.

## Klíčové vlastnosti

- Provádí operační systém zařízení a všechny uživatelské aplikace
- Architektonicky oddělen od modemového/základnového procesoru pro buněčné protokoly
- Komunikuje s modemem prostřednictvím interních příkazových/datových rozhraní (např. AT příkazy, QMI)
- Hostí klienty vyšších vrstev služeb 3GPP (např. IMS pro hlas, SUPL pro určování polohy)
- Spravuje prostředky zařízení: displej, senzory, paměť a nekabelovou konektivitu (Wi-Fi, Bluetooth)
- Umožňuje nezávislý vývoj a certifikaci aplikačního softwaru a rádiového firmwaru

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.935** (Rel-13) — LCS Feasibility Study for 3GPP-WLAN Interworking
- **TS 23.234** (Rel-13) — 3GPP-WLAN Interworking Index
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.423** (Rel-8) — PSTN/ISDN Simulation Services XCAP Protocol
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.611** (Rel-19) — Anonymous Communication Rejection & Barring
- **TS 24.623** (Rel-19) — XCAP Protocol for Supplementary Services
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [AP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ap/)
