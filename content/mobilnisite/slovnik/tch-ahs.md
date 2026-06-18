---
slug: "tch-ahs"
url: "/mobilnisite/slovnik/tch-ahs/"
type: "slovnik"
title: "TCH/AHS – Traffic Channel / Adaptive Multi-Rate Half Rate Speech"
date: 2025-01-01
abbr: "TCH/AHS"
fullName: "Traffic Channel / Adaptive Multi-Rate Half Rate Speech"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tch-ahs/"
summary: "Kanál pro přenos hovorů v síti GSM, který využívá poloviční rychlostní adaptivní vírychlostní hovorový kodek (AMR) pro přenos hlasu. Dynamicky přizpůsobuje kvalitu řeči a kódování kanálu pro optimaliz"
---

TCH/AHS je kanál pro přenos hovorů v síti GSM, který využívá poloviční rychlostní adaptivní vírychlostní hovorový kodek (Adaptive Multi-Rate half-rate speech codec) pro přenos hlasu, dynamicky přizpůsobuje kvalitu a kódování pro optimalizaci kapacity a odolnosti, čímž zdvojnásobuje hlasovou kapacitu buňky ve srovnání s kanálem s plnou rychlostí.

## Popis

[TCH](/mobilnisite/slovnik/tch/)/[AHS](/mobilnisite/slovnik/ahs/) je základní logický kanál v systému GSM určený pro přenos uživatelského hlasového provozu. Funguje v konfiguraci s poloviční rychlostí, což znamená, že využívá pouze polovinu fyzického zdroje standardního kanálu pro přenos hovorů v GSM (jeden časový slot každý druhý rámec) pro přenos hovoru. Klíčovou technologií, která to umožňuje, je adaptivní vírychlostní hovorový kodek ([AMR](/mobilnisite/slovnik/amr/)). Kodek AMR není jediný s pevnou přenosovou rychlostí; místo toho definuje sadu osmi režimů zdrojového kodeku s přenosovými rychlostmi v rozsahu od 4,75 kbit/s do 12,2 kbit/s. Kanál TCH/AHS spáruje tyto zdrojové rychlosti s odpovídajícími schématy kódování kanálu, čímž vytváří sadu 'režimů kodeku' optimalizovaných pro různé podmínky na kanálu.

Provoz TCH/AHS je charakterizován mechanismy adaptace spoje a adaptace režimu kodeku. Adaptace spoje vybírá nejodolnější kombinaci kódování řeči a kódování kanálu na základě měření kvality kanálu v reálném čase, jako je například bitová chybovost ([BER](/mobilnisite/slovnik/ber/)). Při špatných rádiových podmínkách se použije nižší zdrojová rychlost (např. 4,75 kbit/s), čímž se uvolní více bitů pro výkonné kódování kanálu (např. konvoluční kódování) k ochraně hlasových dat. Při výborných podmínkách lze použít vyšší zdrojovou rychlost (např. 7,95 kbit/s) pro dosažení lepší kvality řeči. Adaptaci režimu kodeku může na základě měření a vytížení sítě řídit síť.

Z architektonického hlediska je TCH/AHS mapován na fyzické kanály v [TDMA](/mobilnisite/slovnik/tdma/) struktuře GSM. Používá 26rámcový multirámec, kde jsou specifické rámce přiděleny pro provoz s poloviční rychlostí a další pro přidružené řídicí kanály ([SACCH](/mobilnisite/slovnik/sacch/)) a nečinné rámce. Kanál podporuje jak detekci hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)), tak nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)), což dále šetří životnost baterie mobilního terminálu a snižuje celkový rušení v síti tím, že přenos probíhá pouze, když uživatel hovoří. TCH/AHS je klíčovou součástí strategie správy rádiových zdrojů v GSM, která umožňuje operátorům sítí dynamicky měnit poměr mezi kvalitou řeči a zvýšenou kapacitou sítě.

## K čemu slouží

TCH/AHS byl zaveden za účelem významného zvýšení hlasové kapacity sítí GSM bez nutnosti dodatečného spektra nebo nových stanic. Před zavedením AMR používalo GSM kodeky s pevnou rychlostí, jako například kodek s plnou rychlostí (FR) a kodek s poloviční rychlostí (HR), které nabízely binární volbu mezi dobrou kvalitou (FR) nebo dvojnásobnou kapacitou s výrazně nižší kvalitou (HR). Pevný HR kodek často vedl ke špatné kvalitě řeči, která byla pro mnoho uživatelů nepřijatelná, což omezovalo jeho praktické nasazení.

Zavedení adaptivního vírychlostního kodeku a následně kanálu TCH/AHS tento kompromis vyřešilo. Motivací byla potřeba inteligentnějšího systému schopného přizpůsobit se rádiovým podmínkám. Primární problém, který řeší, je spektrální účinnost pro hlasové služby. Použitím fyzického kanálu s poloviční rychlostí a adaptivního kodeku efektivně zdvojnásobuje počet současných hovorů na rádiovém nosiči ve srovnání s TCH s plnou rychlostí. Jeho adaptivní povaha navíc zajišťuje, že tento zisk kapacity není vykoupen trvalým snížením kvality; za dobrých rádiových podmínek se kvalita řeči může blížit kvalitě kanálu s plnou rychlostí, zatímco za špatných podmínek udržuje integritu hovoru díky silnější ochraně proti chybám. To umožnilo operátorům efektivněji zvládat rostoucí základnu účastníků a špičkové vytížení.

## Klíčové vlastnosti

- Využívá adaptivní vírychlostní hovorový kodek (AMR) s osmi zdrojovými přenosovými rychlostmi od 4,75 do 12,2 kbit/s.
- Funguje na fyzickém kanálu s poloviční rychlostí, čímž zdvojnásobuje hlasovou kapacitu ve srovnání s TCH s plnou rychlostí.
- Používá adaptaci spoje pro dynamický výběr optimálního režimu kodeku na základě kvality rádiového kanálu.
- Podporuje detekci hlasové aktivity (VAD) a nespojitý přenos (DTX) pro snížení rušení a úsporu energie.
- Používá 26rámcovou TDMA strukturu multirámce s vyhrazenými sloty pro provoz a přidružené řídicí signalizace.
- Umožňuje síťově řízenou adaptaci režimu kodeku pro vyvažování zátěže a správu kvality.

## Související pojmy

- [TCH/F – Traffic Channel / Full Rate](/mobilnisite/slovnik/tch-f/)
- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [TCH/AHS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-ahs/)
