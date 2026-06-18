---
slug: "rab"
url: "/mobilnisite/slovnik/rab/"
type: "slovnik"
title: "RAB – Radio Access Bearer"
date: 2025-01-01
abbr: "RAB"
fullName: "Radio Access Bearer"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rab/"
summary: "Radio Access Bearer (RAB) je logický kanál zřízený mezi uživatelským zařízením (UE) a Core Network (CN) přes Radio Access Network (RAN). Definuje konkrétní charakteristiky QoS pro přenos uživatelských"
---

RAB je logický kanál mezi UE a Core Network, který definuje konkrétní QoS pro přenos uživatelských dat přes rozhraní rádiového rozhraní.

## Popis

Radio Access Bearer (RAB) je základním konceptem v UMTS a raných fázích LTE, představujícím službu poskytovanou Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/) nebo [E-UTRAN](/mobilnisite/slovnik/e-utran/)) pro přenos uživatelských dat mezi uživatelským zařízením (UE) a Core Network (CN). Nejde o fyzický kanál, ale o logickou asociaci definující sadu parametrů kvality služby (QoS) pro konkrétní datový tok. RAB je v podstatě zřetězením Radio Bearer ([RB](/mobilnisite/slovnik/rb/)) přes rozhraní Uu (vzduch) a Iu Bearer (pro UMTS) nebo S1 Bearer (pro LTE) přes příslušné rozhraní RAN-CN.

Zřízení, modifikaci a uvolnění RAB řídí Core Network, konkrétně Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v UMTS nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v LTE, prostřednictvím protokolů [RANAP](/mobilnisite/slovnik/ranap/) (rozhraní Iu) nebo S1-AP (rozhraní S1). Když je v CN aktivován [PDP](/mobilnisite/slovnik/pdp/) Context (UMTS) nebo EPS Bearer (LTE), spustí se zřízení odpovídajícího RAB. CN signalizuje RAN požadovaný profil QoS (např. třídu provozu, garantovaný přenosový výkon, maximální přenosový výkon, přenosové zpoždění). Funkce správy rádiových prostředků (RRM) v RAN, konkrétně Radio Admission Control (RAC), následně určí, zda jsou k dispozici dostatečné rádiové prostředky pro podporu požadovaného profilu. Pokud je žádost přijata, RAN nakonfiguruje příslušné transportní kanály a fyzické kanály k realizaci části Radio Bearer pro RAB.

Jedno UE může mít současně více RAB, z nichž každý podporuje jinou službu s vlastními požadavky na QoS. Například jeden RAB může být pro konverzační hlasový hovor (vysoká priorita, nízké zpoždění), zatímco jiný pro přenos e-mailů na pozadí (nízká priorita). Vrstva RAB v protokolovém zásobníku je zodpovědná za mapování paketů dat z vyšších vrstev na nakonfigurované transportní kanály při respektování atributů QoS. To zahrnuje funkce jako kontrola provozu (traffic policing), priorita plánování a zpracování transparentních vs. netransparentních režimů přenosu dat. RAB je tedy klíčovou entitou, která umožňuje síti UMTS/LTE nabízet diferencované služby přes sdílené rádiové médium.

## K čemu slouží

RAB byl vytvořen, aby poskytoval standardizovaný mechanismus s podporou QoS pro přenos uživatelských dat přes radio access network, což byl významný vývoj oproti převážně best-effort povaze 2G GPRS. Řešil problém, jak efektivně podporovat různé služby (hlas, streamování videa, prohlížení webu) s výrazně odlišnými požadavky na jedné, paketově přepínané infrastruktuře. Koncept RAB umožňuje síti zacházet s různými datovými toky od stejného uživatele s odpovídající prioritou a alokací prostředků.

Historicky vyčleňovaly sítě s přepojováním okruhů pro hlasový hovor fyzický kanál (časový slot), což garantovalo kvalitu, ale plýtvalo prostředky během ticha. Paketově přepínané sítě 2.5G zavedly mobilitu, ale postrádaly sofistikovanou QoS. RAB, představený s UMTS, byl základním kamenem vize All-IP, umožňující skutečnou multimediální konvergenci. Poskytuje smluvní rozhraní mezi Core Network, který zná služební profil účastníka, a Radio Access Network, který spravuje omezené a proměnlivé rádiové prostředky. Definováním jasných parametrů QoS umožňuje efektivní řízení přístupu k rádiovému rozhraní (Radio Admission Control), plánování a procedury předávání hovoru, které udržují kontinuitu služby. Jeho evoluce do modelu EPS Bearer v LTE/EPC tento koncept dále upřesnila s přísnějším vázáním na IP toky.

## Klíčové vlastnosti

- Logický kanál s definovaným profilem QoS (třída provozu, přenosové výkony, zpoždění, BER).
- Zřizován, modifikován a uvolňován signalizací z Core Network (RANAP/S1-AP).
- Skládá se z Radio Bearer (přes Uu) a Iu/S1 Bearer (přes rozhraní RAN-CN).
- Podporuje více současných instancí na jedno UE pro provoz s více službami.
- Umožňuje řízení přístupu k rádiovému rozhraní (RAC) a plánování rádiových prostředků na základě QoS.
- Základní pro diferenciaci služeb a garantovaný výkon přes rádiové rozhraní.

## Související pojmy

- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- … a dalších 28 specifikací

---

📖 **Anglický originál a plná specifikace:** [RAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/rab/)
