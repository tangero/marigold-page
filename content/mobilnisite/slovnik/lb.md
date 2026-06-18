---
slug: "lb"
url: "/mobilnisite/slovnik/lb/"
type: "slovnik"
title: "LB – Load Balancing"
date: 2025-01-01
abbr: "LB"
fullName: "Load Balancing"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lb/"
summary: "Funkce správy sítě, která distribuuje provoz, uživatele nebo relace mezi více buněk, frekvencí nebo síťových uzlů za účelem optimalizace využití prostředků a předcházení zahlcení. Zvyšuje kapacitu sít"
---

LB (Load Balancing) je funkce správy sítě, která distribuuje provoz, uživatele nebo relace mezi více prostředků za účelem optimalizace vytížení, předcházení zahlcení a zvýšení kapacity a spolehlivosti.

## Popis

Load Balancing (LB) v systémech 3GPP představuje komplexní soubor algoritmů a procedur navržených k rovnoměrnému rozložení síťového zatížení mezi dostupné prostředky. Toto zatížení může odkazovat na připojení uživatelských zařízení (UE), využití rádiových prostředků, výpočetní zátěž síťových funkcí nebo datový provoz. Primárním cílem je zabránit přetížení jednotlivých buněk, nosných nebo síťových prvků, zatímco jiné jsou nedostatečně využity, čímž se maximalizuje celková kapacita a efektivita sítě. LB funguje napříč více doménami: v rádiové přístupové síti (RAN) mezi buňkami, mezi nosnými (frekvenčními vrstvami), mezi technologiemi rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)) a v jádru sítě mezi instancemi virtualizovaných síťových funkcí.

V RAN je Load Balancing typicky řízen eNodeB v LTE nebo gNodeB v NR, často s koordinací od centrální entity, jako je systém Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)) nebo RAN Intelligent Controller (RIC) v pokročilejších architekturách. Proces zahrnuje nepřetržité sledování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), jako je využití bloků prostředků, počet připojených UE, využití [PRB](/mobilnisite/slovnik/prb/) a zatížení hardwaru. Když je detekována nerovnováha zatížení – například když je jedna buňka nad prahem vysokého využití, zatímco sousední buňka je pod prahem nízkého využití – algoritmus LB spustí akce. Nejběžnější akcí je vyrovnávání zatížení založené na předávání (handover), při kterém síť iniciuje předání vybraných UE z přetížené buňky do nedostatečně zatížené sousední buňky. Toto je známé jako Mobility Load Balancing (MLB).

Mechanismy LB jsou sofistikované a zohledňují více faktorů, aby se předešlo ping-pong efektům a degradaci služeb. Algoritmy používají hysterezi, prahové hodnoty a filtrování pro zajištění stability. Také zohledňují schopnosti UE, podmínky rádiového kanálu a požadavky QoS aktivních přenosových toků, aby vybraly vhodná UE k předání. Například UE s přenosovým tokem typu non-GBR na okraji buňky může být pro vyrovnávací předání upřednostněno před UE s přenosovým tokem typu [GBR](/mobilnisite/slovnik/gbr/) v dobrých podmínkách. Ve scénářích s agregací nosných může LB také zahrnovat úpravu politik přidávání/odebírání skupiny sekundárních buněk (SCell). Dále v prostředích s více RAT (např. LTE-NR dual connectivity, LTE-WiFi) může meziratové vyrovnávání zatížení (Inter-RAT Load Balancing) přesměrovávat provoz nebo UE v nečinném režimu na nejvhodnější RAT na základě zatížení a schopností.

V jádru sítě, zejména u cloud-nativního 5G Core (5GC), je Load Balancing klíčové pro bezstavové a škálovatelné síťové funkce ([NF](/mobilnisite/slovnik/nf/)). Funkce Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) usnadňuje objevování služeb a vyrovnávání zatížení mezi více instancemi daného typu NF (např. více instancemi [AMF](/mobilnisite/slovnik/amf/)). Když se UE registruje nebo NF vyžaduje službu, konzument NF dotazuje NRF, který může vrátit seznam instancí producenta NF filtrovaný a seřazený podle jejich aktuálního zatížení, kapacity a lokality. Tím je zajištěno, že žádná jednotlivá instance NF se nestane úzkým hrdlem. Celkově je Load Balancing dynamický, vícevrstvý optimalizační proces, který je zásadní pro automatizovaný, efektivní a odolný provoz moderních sítí 3GPP.

## K čemu slouží

Load Balancing bylo zavedeno, aby vyřešilo inherentní neefektivitu a zhoršování výkonu způsobené nerovnoměrnou distribucí provozu v celulárních sítích. Rané celulární systémy často zažívaly 'horké' buňky v hustě obydlených městských oblastech nebo během událostí, což vedlo k zahlcení, vysokým míram blokování a špatnému uživatelskému zážitku, zatímco sousední buňky zůstávaly nedostatečně využity. Tato nerovnováha vznikala z nerovnoměrného rozložení uživatelů, geografických faktorů a různých konfigurací buněk. Bez LB je síťová kapacita efektivně omezena nejvíce přetíženou buňkou, což plýtvá kapitálovou investicí do nedostatečně využívané infrastruktury.

Primárním účelem LB je maximalizovat využití všech nasazených síťových prostředků, čímž se zvyšuje celková kapacita a propustnost systému. Proaktivním přesunem uživatelů z přetížených oblastí do méně vytížených LB zmírňuje zahlcení, snižuje počet spadlých hovorů a selhání přístupu a zlepšuje celkovou kvalitu služeb (QoS) a kvalitu uživatelského zážitku (QoE) pro všechny uživatele. Přeměňuje skupinu jednotlivých buněk na koordinovaný, elastický fond prostředků. To je obzvláště kritické s příchodem heterogenních sítí (HetNets) obsahujících makro buňky, malé buňky a různá frekvenční pásma, kde je manuální optimalizace distribuce provozu nepraktická.

Dále LB zvyšuje robustnost a spolehlivost sítě. Funguje jako preventivní opatření proti selhání uzlů tím, že se vyhýbá extrémním podmínkám přetížení, které by mohly vést k softwarovým nebo hardwarovým selháním. V kontextu síťového řezání (network slicing) LB zajišťuje, že prostředky jsou spravedlivě přidělovány mezi řezy podle jejich SLA. S přechodem na cloud-nativní, softwarově založené sítě 5G jádra je LB nezbytné pro automatické škálování a elasticitu. Umožňuje síti dynamicky se přizpůsobovat vzorcům provozu, což umožňuje efektivní využití cloudových prostředků a podporuje charakter služeb 5G na vyžádání. Stručně řečeno, Load Balancing je klíčovým prvkem pro vysokokapacitní, samooptymalizující se a spolehlivé sítě vyžadované pro moderní mobilní širokopásmový přístup a kritické komunikace.

## Klíčové vlastnosti

- Sleduje metriky zatížení v reálném čase (počet UE, využití prostředků, zatížení hardwaru).
- Provádí Mobility Load Balancing (MLB) prostřednictvím síťově iniciovaných předání mezi buňkami.
- Podporuje vícevrstvé vyvažování napříč nosnými, RAT a instancemi jádra sítě.
- Používá konfigurovatelné prahové hodnoty, hysterezi a filtrování pro zajištění stability algoritmu.
- Integruje se se systémy OAM a RAN Intelligent Controllers pro centralizovanou optimalizaci.
- Zohledňuje kontext UE (QoS, rádiové podmínky) pro výběr optimálních UE k akcím vyrovnávání zatížení.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 28.627** (Rel-19) — SON Policy NRM IRP: Requirements
- **TS 28.628** (Rel-19) — SON Policy NRM IRP Information Service
- **TS 28.861** (Rel-16) — SON for 5G Networks Management
- **TS 32.521** (Rel-11) — SON Policy NRM IRP Requirements
- **TS 32.522** (Rel-11) — SON Policy NRM IRP Information Service
- **TS 34.109** (Rel-19) — UE Conformance Test Functions for UMTS
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.509** (Rel-17) — EPC Special UE Conformance Testing Functions
- **TS 37.852** (Rel-12) — RAN Enhancements for UMTS/HSPA and LTE Interworking
- **TS 38.509** (Rel-18) — Special conformance testing functions for UE

---

📖 **Anglický originál a plná specifikace:** [LB na 3GPP Explorer](https://3gpp-explorer.com/glossary/lb/)
