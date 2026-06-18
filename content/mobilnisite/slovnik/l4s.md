---
slug: "l4s"
url: "/mobilnisite/slovnik/l4s/"
type: "slovnik"
title: "L4S – Low Latency, Low Loss, and Scalable Throughput"
date: 2026-01-01
abbr: "L4S"
fullName: "Low Latency, Low Loss, and Scalable Throughput"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/l4s/"
summary: "L4S je architektura pro dosažení extrémně nízké latence a minimálních ztrát paketů v IP sítích, která umožňuje škálovatelnou propustnost pro aplikace jako komunikace v reálném čase a AR/VR. Umožňuje p"
---

L4S je architektura pro dosažení extrémně nízké latence, minimálních ztrát paketů a škálovatelné propustnosti v IP sítích tím, že umožňuje citlivému na latenci koexistovat se standardním provozem bez nutnosti samostatných front.

## Popis

Low Latency, Low Loss, and Scalable Throughput (L4S) je architektura kvality služeb (QoS) standardizovaná organizacemi 3GPP a [IETF](/mobilnisite/slovnik/ietf/), která umožňuje extrémně nízké frontové zpoždění a téměř nulové ztráty paketů v IP sítích, zejména pro 5G a další generace. Funguje na principu modifikace chování koncových bodů i síťových uzlů za účelem signalizace a správy provozu kritického na latenci. Základní mechanismus spočívá v použití pole Explicit Congestion Notification ([ECN](/mobilnisite/slovnik/ecn/)) v hlavičce IP s novým L4S kódovým bodem ([ECT](/mobilnisite/slovnik/ect/)(1) nebo [CE](/mobilnisite/slovnik/ce/)) k rozlišení paketů vyžadujících nízkolatencní zacházení. Když síťový uzel (jako router nebo [UPF](/mobilnisite/slovnik/upf/)) zaznamená počínající zahlcení, může označit tyto L4S pakety kódovým bodem CE při velmi nízkém prahu frontového zpoždění, místo aby je zahazoval nebo čekal na zaplnění hlubokých front. Tato okamžitá zpětná vazba umožňuje odesílateli (např. UE nebo serveru) reagovat téměř okamžitě pomocí škálovatelných algoritmů řízení zahlcení, jako je TCP Prague nebo ekvivalentní protokoly pro přenos v reálném čase, a snížit tak rychlost odesílání dříve, než dojde k výraznému nárůstu front.

Z architektonického hlediska vyžaduje L4S podporu na celé end-to-end cestě: odesílatel musí generovat pakety s L4S ECN kódovým bodem a používat škálovatelný algoritmus řízení zahlcení, který reaguje na jednotlivé označené pakety multiplikativním snížením. Příjemce musí označení ECN zpětně potvrdit odesílateli prostřednictvím potvrzení na transportní vrstvě. Klíčové je, že síťové uzly musí implementovat mechanismus vázaného AQM (Active Queue Management) s dvojitou frontou, jako je Dual-Queue Coupled AQM (DQCA) nebo podobný. Ten zahrnuje dvě fronty: Classic frontu pro standardní provoz (např. tradiční TCP) a L4S frontu pro provoz citlivý na latenci. AQM aplikuje na L4S frontu velmi mělké prahy (např. mikrosekundy frontového zpoždění) a označuje pakety při prvním náznaku zahlcení, zatímco Classic fronta používá hlubší prahy. Fronty jsou vázány tak, aby L4S provoz nevyhladověl Classic provoz, a byla tak zachována spravedlnost.

V systému 3GPP je L4S integrováno do 5G Core (5GC) a User Plane Function (UPF), aby bylo zajištěno nízkolatencní zacházení v celé mobilní síti. Specifikace definují QoS toky a pravidla pro detekci paketů ([PDR](/mobilnisite/slovnik/pdr/)) k identifikaci a označení L4S provozu, často s mapováním na hodnoty [5QI](/mobilnisite/slovnik/5qi/) určené pro nízkou latenci. UPF funguje jako L4S síťový uzel, implementuje vázaný AQM s dvojitou frontou a odpovídajícím způsobem označuje pakety. To umožňuje aplikacím, jako je rozšířená realita ([AR](/mobilnisite/slovnik/ar/)), virtuální realita (VR), cloudové hraní a průmyslové řízení, dosáhnout konzistentní latence pod 10 ms i při zatížení, což je klíčové pro imerzní zážitky a automatizaci v reálném čase. L4S tak přeměňuje best-effort IP sítě na předvídatelné platformy s nízkou latencí bez nutnosti nadměrného poskytování kapacit nebo vyhrazených fyzických prostředků.

## K čemu slouží

L4S bylo vytvořeno, aby řešilo základní omezení tradičního internetového řízení zahlcení a správy front při podpoře aplikací s extrémně nízkou latencí. Historicky byly TCP a standardní Active Queue Management (např. RED, CoDel) navrženy pro efektivitu propustnosti a spravedlnost, ale způsobují latenci kvůli bufferbloatu – velkým frontám v síťových vyrovnávacích pamětech, které způsobují zpoždění. Zatímco řešení jako DiffServ poskytovala prioritní fronty, vyžadovala složitou konfiguraci, mohla vyhladovět provoz na pozadí a neškálovala dobře. Vzestup 5G a náročných případů užití, jako je hmatový internet, autonomní vozidla a holografie v reálném čase, si vyžádaly nový přístup, který by mohl zajistit konzistentní latenci na úrovni mikrosekund bez obětování propustnosti nebo spravedlnosti.

Motivace pro L4S vychází z potřeby škálovatelné nízké latence: protože stále více aplikací vyžaduje nízké zpoždění, sítě musí zvládnout mnoho takových toků současně bez degradace výkonu. Předchozí pokusy, jako použití samostatných front s vysokou prioritou, vedly k problémům s izolací a režií správy. L4S to řeší tím, že umožňuje nízkolatencnímu a klasickému provozu efektivně sdílet stejnou kapacitu linky prostřednictvím vázaného řízení zahlcení. Využívá a rozšiřuje Explicit Congestion Notification (ECN), které bylo nedostatečně využíváno, aby poskytlo okamžitou zpětnou vazbu. To umožňuje algoritmům řízení zahlcení reagovat v rámci jednoho času oběhu (RTT), čímž se minimalizují frontová zpoždění. Standardizací v 3GPP Release 18 a novějších L4S zajišťuje, že mobilní sítě mohou podporovat přísné požadavky budoucích služeb, což operátorům umožňuje ekonomickou škálovatelnost a zároveň poskytuje vynikající uživatelský zážitek.

## Klíčové vlastnosti

- Používá ECN s vyhrazeným L4S kódovým bodem (ECT(1)/CE) pro okamžitou signalizaci zahlcení
- Vyžaduje vázaný AQM s dvojitou frontou v síťových uzlech k oddělení L4S a Classic provozu s mělkými prahy
- Používá škálovatelné algoritmy řízení zahlcení (např. TCP Prague), které reagují na jednotlivé označené pakety
- Poskytuje extrémně nízké frontové zpoždění (pod 1 ms) a téměř nulové ztráty paketů při zahlcení
- Zachovává spravedlnost mezi L4S a Classic provozem prostřednictvím vázaného řízení zahlcení
- Integruje se s rámcem QoS pro 5G prostřednictvím 5QI a označování paketů v UPF

## Související pojmy

- [ECN – Explicit Congestion Notification](/mobilnisite/slovnik/ecn/)
- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 28.541** (Rel-20) — 5G Network Resource Model (NRM) Stage 2/3
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3

---

📖 **Anglický originál a plná specifikace:** [L4S na 3GPP Explorer](https://3gpp-explorer.com/glossary/l4s/)
