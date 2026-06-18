---
slug: "racs"
url: "/mobilnisite/slovnik/racs/"
type: "slovnik"
title: "RACS – UE Radio Capability Signalling optimization"
date: 2026-01-01
abbr: "RACS"
fullName: "UE Radio Capability Signalling optimization"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/racs/"
summary: "Funkce optimalizující signalizaci rádiových schopností UE vůči síti, která snižuje režii a latenci. Umožňuje síti uložit informace o rádiových schopnostech UE a vyžádat si aktualizaci pouze v případě"
---

RACS je funkce optimalizující signalizaci tím, že síť uloží informace o rádiových schopnostech UE a vyžádá si jejich aktualizaci pouze v případě potřeby, čímž snižuje režii a latenci při navazování spojení a při mobilitě.

## Popis

Optimalizace signalizace rádiových schopností UE (UE Radio Capability Signalling optimization – RACS) je síťová funkce navržená k minimalizaci signalizační režie spojené s přenosem informací o rádiových schopnostech uživatelského zařízení (UE). Rádiové schopnosti UE představují komplexní soubor parametrů popisujících podporované funkce, pásma, kmitočtové rozsahy a technické limity (např. maximální počet nosných, podporované modulační schémata). Tradičně jsou tyto informace, obsažené v UE Radio Capability ID (UECapabilityInformation), odesílány z UE do sítě během počáteční registrace a potenciálně při každém sestavování spojení nebo mobilitě mezi přístupovými technologiemi (inter-RAT), což vede k významné signalizační zátěži, zejména u rozsáhlých kontejnerů schopností pokročilých UE.

RACS funguje tak, že umožňuje jádrové síti (konkrétně funkci pro správu přístupu a mobility, [AMF](/mobilnisite/slovnik/amf/), v 5GC nebo [MME](/mobilnisite/slovnik/mme/) v EPS) uložit si informace o rádiových schopnostech UE po jejich prvním úspěšném získání. Síť těmto uloženým informacím přiřadí UE Radio Capability ID. Následně může síť pro signalizaci používat toto mnohem kratší ID namísto toho, aby UE přenášelo celý soubor schopností. AMF/MME poskytne toto ID uzlu přístupové rádiové sítě (RAN) (gNB nebo [eNB](/mobilnisite/slovnik/enb/)). Pokud RAN uzel nemá odpovídající data o schopnostech uložena lokálně v mezipaměti, může pomocí ID požádat jádrovou síť o úplné informace.

Architektura zahrnuje koordinaci mezi UE, RAN a jádrovou sítí. Klíčové signalizační zprávy jsou upraveny tak, aby přenášely UE Radio Capability ID. Například v 5G zahrnuje AMF `UE Radio Capability ID` ve zprávách `INITIAL CONTEXT SETUP REQUEST` nebo `UE RADIO CAPABILITY CHECK REQUEST` odesílaných gNB. gNB zkontroluje svou lokální úložiště. Pokud data chybí nebo jsou potenciálně zastaralá (např. po aktualizaci software), může gNB požádat AMF o poskytnutí úplných `UE Radio Capability Information` prostřednictvím procedury získání. Síť také spravuje životní cyklus těchto uložených dat, včetně mechanismů pro detekci případné změny schopností (např. na základě indikace od UE nebo obnovy řízené časovačem).

Tato optimalizace významně snižuje velikost signalizačních zpráv na rádiovém rozhraní (Uu) a na rozhraních [NG](/mobilnisite/slovnik/ng/)/E1. Je zvláště přínosná pro procedury citlivé na latenci, jako je obnovení spojení ze stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE, a pro UE s rozsáhlými seznamy schopností, například ta podporující mnoho NR a LTE pásem, kombinace agregace nosných a funkce jako duální konektivita. Minimalizací množství přenášených dat RACS zlepšuje dobu sestavení spojení, snižuje spotřebu baterie UE na signalizaci a snižuje zatížení síťových uzlů spojené se zpracováním.

## K čemu slouží

RACS byla zavedena, aby řešila rostoucí problém signalizační režie způsobené stále složitějšími rádiovými schopnostmi UE. S vývojem standardů 3GPP přes LTE-Advanced až po 5G explodoval počet podporovaných kmitočtových pásem, kombinací agregace nosných a volitelných funkcí. Přenos úplné, rozsáhlé zprávy `UECapabilityInformation` během každé relevantní procedury se stal významným zdrojem latence a spotřebovával cenné rádiové prostředky.

Hlavním problémem, který RACS řeší, je neefektivní opakování přenosu rozsáhlých, statických datových souborů. Jádrové rádiové schopnosti UE se mění zřídka, typicky pouze po aktualizaci software nebo významné hardwarové změně. Opakovaný přenos tohoto bloku o velikosti několika kilobytů byl plýtváním. Před zavedením RACS neměla síť standardizovaný, efektivní způsob, jak se tomuto opakování vyhnout, což vedlo k delší době sestavování hovorů a zvýšené signalizační kongesci, zejména v hustých sítích.

Její vytvoření bylo motivováno potřebou optimalizovat výkon sítě pro nasazení masivního IoT a scénáře rozšířeného mobilního širokopásmového přístupu, kde je rychlé sestavení spojení kritické. Přechodem na model založený na ID se RACS přizpůsobuje obecným principům optimalizace sítí, jako je ukládání do mezipaměti a nepřímý odkaz. Také připravuje systém do budoucna pro ještě složitější definice schopností v systémech po 5G, a zajišťuje tak efektivní škálování signalizace bez ohledu na to, jak podrobné schopnosti UE budou.

## Klíčové vlastnosti

- Ukládání rádiových schopností UE v jádrové síti (AMF/MME)
- Použití kompaktního UE Radio Capability ID pro signalizaci namísto úplných dat
- Na požádání získání úplných schopností z jádrové sítě RANem
- Snížení velikosti signalizačních zpráv na rádiovém rozhraní (Uu)
- Podpora detekce zastaralých informací o schopnostech
- Použitelnost pro procedury sestavení spojení, mobility a obnovení

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NGAP – Next Generation Application Protocol](/mobilnisite/slovnik/ngap/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 29.421** (Rel-8) — IMS Interworking with External IP Networks
- **TS 29.675** (Rel-19) — UE Radio Capability Provisioning Service
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)

---

📖 **Anglický originál a plná specifikace:** [RACS na 3GPP Explorer](https://3gpp-explorer.com/glossary/racs/)
