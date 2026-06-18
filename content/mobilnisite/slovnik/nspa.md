---
slug: "nspa"
url: "/mobilnisite/slovnik/nspa/"
type: "slovnik"
title: "NSPA – Network Slice Performance and Analytics"
date: 2025-01-01
abbr: "NSPA"
fullName: "Network Slice Performance and Analytics"
category: "Network Slicing"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nspa/"
summary: "Rámec pro monitorování a analýzu výkonu síťových řezů. Shromažďuje výkonnostní data a poskytuje analytiku pro zajištění plnění Smluv o úrovni služeb (SLA) pro jednotlivé řezy. To je klíčové pro správu"
---

NSPA je rámec 3GPP pro monitorování, analýzu a zajišťování výkonu síťových řezů vůči SLA prostřednictvím sběru dat a poskytování analytiky.

## Popis

Network Slice Performance and Analytics (NSPA) je komplexní rámec definovaný ve standardech 3GPP, který usnadňuje monitorování, měření a analytické vyhodnocování síťových řezů. Síťový řez je logická, koncová síť přizpůsobená specifickým požadavkům služby a NSPA poskytuje mechanismy pro zajištění, že tyto řezy fungují podle očekávání. Rámec funguje definováním úloh měření výkonu, které sbírají data z různých síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) zapojených do instance řezu, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Tato data zahrnují klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je latence, propustnost, spolehlivost a využití zdrojů, které jsou agregovány a zpracovávány pro posouzení stavu řezu a jeho souladu s jeho Smlouvou o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)).

Architektura NSPA zahrnuje několik funkčních komponent, především Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) a řídicí funkce jako Network Slice Management Function ([NSMF](/mobilnisite/slovnik/nsmf/)) a Communication Service Management Function (CSMF). NWDAF hraje ústřední roli tím, že shromažďuje výkonnostní data ze síťových funkcí a dalších zdrojů, aplikuje analytické modely a generuje poznatky, jako jsou predikce výkonu, detekce anomálií a analýza hlavní příčiny. Tyto analytické výstupy jsou následně využívány řídicími systémy k umožnění automatizovaných akcí správy životního cyklu řezu, jako je škálování zdrojů, rekonfigurace parametrů nebo spouštění nápravných opatření k zabránění porušení SLA.

NSPA funguje prostřednictvím kontinuálního cyklu sběru dat, analytiky a zpětné vazby. Úlohy měření jsou konfigurovány a aktivovány na základě požadavků řezu. Sběraná nezpracovaná data jsou zpracována a korelována za účelem vytvoření holistického pohledu na výkon řezu z perspektivy sítě i služby. To umožňuje operátorům přejít od reaktivního řešení problémů k proaktivnímu a prediktivnímu zajišťování. Díky poskytnutí hlubokého přehledu o chování řezů je NSPA zásadní pro naplnění příslibu síťového řezování v 5G, kde musí na sdílené fyzické infrastruktuře koexistovat více logických sítí s různými výkonnostními charakteristikami při zachování striktní izolace a garantovaného výkonu.

## K čemu slouží

NSPA bylo vytvořeno k řešení kritické výzvy zajišťování výkonu v síťovém řezování 5G. Tradiční nástroje pro správu výkonu sítě byly navrženy pro monolitické, univerzální sítě a nemohly poskytnout potřebnou podrobnou viditelnost na úrovni jednotlivých izolovaných logických řezů. Bez NSPA by operátoři nemohli ověřit, zda síťový řez vyhrazený například pro ultra-spolehlivou komunikaci s nízkou latencí (URLLC) pro tovární automatizaci skutečně splňuje své přísné cíle pro latenci a spolehlivost, což by vedlo k potenciálním výpadkům služeb a porušení SLA.

Motivace vychází z vize 5G podporovat širokou škálu služeb – rozšířené mobilní širokopásmové připojení (eMBB), hromadný internet věcí (mIoT) a kritické komunikace – z nichž každá má zcela odlišné požadavky. Síťové řezování je klíčovým enablerem pro tuto vizi, ale zároveň zavádí složitost do správy. NSPA poskytuje potřebnou inteligenci a automatizaci pro správu této složitosti. Řeší problém neprůhledného výkonu uvnitř řezů tím, že poskytuje analytiku vedoucí k akcím, umožňuje efektivní využití zdrojů, automatizovanou optimalizaci a v konečném důsledku komerční životaschopnost nabídky řezu jako služby pro podnikové zákazníky.

## Klíčové vlastnosti

- Definuje standardizované úlohy měření výkonu pro síťové řezy
- Shromažďuje a koreluje KPI z více síťových funkcí (NF)
- Integruje se s Network Data Analytics Function (NWDAF) pro pokročilou analytiku
- Podporuje jak monitorování výkonu v reálném čase, tak historické
- Umožňuje ověřování souladu se SLA a prediktivní zajišťování
- Poskytuje vstupy pro uzavřenou smyčku automatizace v řízení životního cyklu řezu

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [SLA – Spending-Limit-Answer](/mobilnisite/slovnik/sla/)
- [NSMF – Network Slice Management Function](/mobilnisite/slovnik/nsmf/)

## Definující specifikace

- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios

---

📖 **Anglický originál a plná specifikace:** [NSPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/nspa/)
