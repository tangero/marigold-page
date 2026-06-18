---
slug: "mg-mgw"
url: "/mobilnisite/slovnik/mg-mgw/"
type: "slovnik"
title: "MG/MGW – Media Gateway"
date: 2025-01-01
abbr: "MG/MGW"
fullName: "Media Gateway"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mg-mgw/"
summary: "Síťový prvek, který převádí mediální toky mezi různými přenosovými formáty a protokoly, například mezi hlasovými službami s přepojováním okruhů (PSTN, 2G/3G CS) a hlasovými službami s přepojováním pak"
---

MG/MGW je síťový prvek, který převádí mediální toky mezi různými přenosovými formáty a protokoly, například mezi přepojováním okruhů a přepojováním paketů v hlasových sítích.

## Popis

Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) je základní síťový prvek odpovědný za přenosovou transformaci uživatelské roviny médií (především hlasu a videa) v reálném čase mezi doménou s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) tradičních telekomunikačních sítí a doménou s přepojováním paketů ([PS](/mobilnisite/slovnik/ps/)) IP sítí, jako jsou IMS, LTE a 5G Core. Funguje jako překladatelský most, který zpracovává vlastní přenosový provoz. Funkčně ukončuje přenosové kanály ze sítě s přepojováním okruhů (např. [TDM](/mobilnisite/slovnik/tdm/) trunky z [PSTN](/mobilnisite/slovnik/pstn/) nebo staršího [MSC](/mobilnisite/slovnik/msc/)) a mediální toky z paketové sítě (např. [RTP](/mobilnisite/slovnik/rtp/)/[UDP](/mobilnisite/slovnik/udp/)/IP toky ze sítě IMS) a provádí mezi těmito formáty nezbytný překódování, přešifrování a paketizaci/depaketizaci.

Z architektonického hlediska je v kontextu IMS a rozvinutého paketového jádra MGW typicky řízen samostatným řídicím prvkem, nejvýznamněji funkcí řízení mediální brány (MGCF) pro vzájemnou spolupráci SIP-ISUP nebo MSC Serverem v architektuře 3GPP CS. Toto oddělení odpovídá modelu rozdělení řídicí a přenosové roviny. Řadič (MGCF) zpracovává signalizaci hovorů (SIP, ISUP) a používá protokoly jako H.248 (Megaco) nebo MGCP, jak je definováno ve specifikacích 3GPP jako 29.332, k ovládání MGW. MGCF dává MGW pokyny k vytváření, úpravám a mazání ukončení (logických koncových bodů) a kontextů (asociací mezi ukončeními), specifikuje kodeky, IP adresy, čísla portů a parametry potlačení ozvěn. MGW následně tyto příkazy provádí a nastavuje fyzické nebo logické prostředky k propojení mediální cesty.

Klíčové vnitřní komponenty MGW zahrnují digitální signálové procesory (DSP) pro překódování mezi kodeky (např. z G.711 PCM na AMR-NB), potlačovače ozvěn, generátory/detektory tónů a vyrovnávací paměti pro přehrávání pro zvládání chvění z paketové sítě. Jeho role přesahuje pouhou konverzi formátu. V IMS je zásadní pro poskytnutí přístupu ke starším CS sítím (PSTN/PLMN), což umožňuje službám jako VoLTE a VoNR volat na tradiční telefonní čísla. Hraje také roli v zákonném odposlechu tím, že poskytuje přístup k provozu v uživatelské rovině na pokyn z řídicí roviny. V 5G Core existují podobné funkce vzájemné spolupráce, ačkoli architektonické prvky mohou mít jiné názvy (např. funkce IMS-ALG/TrGW), základní koncept mediálně zpracovávající brány zůstává.

## K čemu slouží

Media Gateway byl vytvořen, aby umožnil postupnou a ekonomicky životaschopnou migraci ze starších sítí s přepojováním okruhů založených na časovém multiplexu (TDM) na plně IP sítě s přepojováním paketů. Bez MGW by byly nové služby založené na IP, jako je VoIP v IMS, izolovanými ostrovy, neschopnými komunikovat s rozsáhlou instalovanou základnou tradičních telefonů a mobilních telefonů v sítích 2G/3G CS. MGW řeší tento problém vzájemné spolupráce tím, že zvládá komplexní překlad skutečného hlasového média v reálném čase, což umožňuje hovorům plynule procházet oběma technologickými doménami.

Jeho vývoj byl poháněn vznikem architektury softswitch a později IMS na počátku roku 2000, které prosazovaly oddělení řízení hovorů (inteligence) od přenosu médií (nosiče). To umožnilo flexibilnější návrh sítě, nezávislé škálování řídicích a mediálních prostředků a zavádění nových služeb bez nutnosti nahrazovat celou infrastrukturu mediální cesty. MGW ztělesňuje 'hloupý' prvek přenosové roviny, který může být prostřednictvím standardizovaných řídicích protokolů (H.248) přizpůsoben pro různé účely, což umožňuje interoperabilitu mezi různými dodavateli a chrání investice operátorů do přenosové infrastruktury během dlouhého přechodu na plně IP.

## Klíčové vlastnosti

- Provádí překódování mezi hlasovými kodeky pro přepojování okruhů (např. G.711) a přepojování paketů (např. AMR, EVS)
- Provádí funkce zpracování médií pod řízením MGCF nebo MSC Serveru pomocí protokolu H.248/Megaco
- Ukončuje starší TDM trunky (E1/T1) a propojuje je s rozhraními IP sítě (RTP toky)
- Poskytuje základní mediální funkce, jako je potlačení ozvěn, generování tónů a správa vyrovnávací paměti pro přehrávání
- Umožňuje klíčovou síťovou interoperabilitu mezi IMS/VoLTE/VoNR a staršími sítěmi PSTN/CS mobilních sítí
- Podporuje zákonný odposlech provozu v uživatelské rovině podle požadavků regulatorních orgánů

## Související pojmy

- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 29.332** (Rel-19) — MGCF-IM-MGW Interface Protocol (Mn)
- **TS 29.424** (Rel-8) — H.248 Profile for Trunking Media Gateways

---

📖 **Anglický originál a plná specifikace:** [MG/MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/mg-mgw/)
