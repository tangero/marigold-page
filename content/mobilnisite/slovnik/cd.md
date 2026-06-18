---
slug: "cd"
url: "/mobilnisite/slovnik/cd/"
type: "slovnik"
title: "CD – Capacity Deallocation"
date: 2026-01-01
abbr: "CD"
fullName: "Capacity Deallocation"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cd/"
summary: "Capacity Deallocation (CD) je funkce správy sítě pro efektivní zpětné získání a přepřidělení síťových prostředků, jako je přenosová kapacita nebo výpočetní kapacita, které již služba nebo uživatel nep"
---

CD je funkce správy sítě pro zpětné získání a přepřidělení síťových prostředků, jako je přenosová kapacita, které již nejsou potřeba, za účelem zajištění optimálního využití a zabránění vyhladovění prostředků.

## Popis

Capacity Deallocation (CD) je základní mechanismus správy prostředků v sítích 3GPP, navržený pro dynamické uvolnění přidělených síťových prostředků, když již nejsou aktivně potřeba. Tento proces je nedílnou součástí frameworku Operation, Administration, and Maintenance ([OAM](/mobilnisite/slovnik/oam/)), konkrétně v doménách Performance Management ([PM](/mobilnisite/slovnik/pm/)) a Fault Management ([FM](/mobilnisite/slovnik/fm/)). Funguje tak, že monitoruje skutečné využití prostředků – jako jsou rádiové přenosové kanály, přenosová kapacita transportní sítě nebo procesní prvky jádra sítě – ve vztahu k jejich přiděleným kvótám. Když je detekováno trvalé nevyužívání nebo je ukončena servisní relace, funkce CD spustí řízený proces uvolnění. Ten zahrnuje signalizaci mezi síťovými funkcemi (např. mezi RAN a Core Network) za účelem zrušení rezervovaných prostředků, aktualizaci interních stavových tabulek a zpřístupnění kapacity pro jiné služby nebo uživatele.

Architektura podporující CD je distribuována napříč síťovými elementy. V Radio Access Network (RAN) zahrnuje Node B (pro UMTS) nebo eNodeB/gNB (pro LTE/5G), které uvolňují bloky rádiových prostředků a transportní kanály. V Core Network spravují entity jako Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)), Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) uvolňování [PDP](/mobilnisite/slovnik/pdp/) kontextů, paketových toků nebo PDU relací. Proces je řízen politikami definovanými v Policy and Charging Rules Function (PCRF) nebo Policy Control Function (PCF), které stanovují podmínky pro uvolnění na základě profilů účastníků, typů služeb a zatížení sítě.

Klíčové pro jeho fungování je koordinace mezi rezervací a uvolňováním prostředků, aby nedocházelo k přerušení služby. CD musí být pečlivě synchronizována s mobilními událostmi (jako je předávání spojení) a mechanismy kontinuity relací, aby se zabránilo předčasnému uvolnění stále používaných prostředků. Používá časovače a prahové hodnoty k rozlišení mezi dočasnými obdobími nečinnosti a skutečným ukončením poptávky. Uvolněné prostředky jsou pak vráceny do sdíleného fondu, což umožňuje zisky ze statistického multiplexování a zlepšuje celkovou kapacitu sítě. Toto dynamické řízení je zásadní pro podporu různorodých vzorců provozu, od nárazových datových relací po trvalé IoT připojení, a zajišťuje, že síť může efektivně škálovat.

Z pohledu technické implementace jsou postupy CD specifikovány v různých 3GPP Technical Specifications (TS). Například v kontextu GTP tunelů zahrnuje uvolnění zprávy pro smazání tunelů a aktualizaci stavů přeposílání. V radio resource control (RRC) zahrnuje přechod uživatelského zařízení do nižších stavů spojení a uvolnění vyhrazených kanálů. Funkce je úzce spojena s účtovacími systémy, protože za uvolněné prostředky přestávají být účtovány poplatky za využití. Efektivní CD snižuje provozní náklady minimalizací nadměrného poskytování kapacit a zlepšuje uživatelský zážitek tím, že uvolňuje kapacitu pro nové požadavky, čímž snižuje pravděpodobnost zahlcení a blokování.

## K čemu slouží

Capacity Deallocation existuje proto, aby řešila kritický problém plýtvání prostředky v telekomunikačních sítích. Starší systémy mobilní komunikace často přidělovaly prostředky na celou dobu trvání hovoru nebo relace, dokonce i během období ticha nebo po jejich efektivním dokončení, což vedlo k neefektivnímu využití. Jak se sítě vyvíjely, aby podporovaly paketově přepínané datové služby s vysoce variabilními požadavky na přenosovou kapacitu, stala se statická alokace neudržitelnou. CD byla zavedena, aby umožnila dynamickou správu prostředků, což sítím dovoluje přizpůsobit se podmínkám provozu v reálném čase a obsloužit více uživatelů se stejnou fyzickou infrastrukturou.

Vytvoření CD bylo motivováno potřebou nákladově efektivního škálování a zlepšené Quality of Service (QoS). Bez efektivního uvolňování by sítě trpěly vyčerpáním prostředků, kdy kapacita zůstává blokována neaktivními relacemi, což brání zřizování nových relací. To je obzvláště problematické pro služby orientované na data, běžné od 3G (UMTS) dále. CD řeší omezení předchozích přístupů typu 'přidělit a držet' zavedením inteligence do životního cyklu prostředků, což zajišťuje, že prostředky jsou drženy pouze tehdy, když jsou skutečně potřeba. To je základní pro implementaci pokročilých funkcí QoS, tvarování provozu a politik spravedlivého využití napříč sdílenou sítí.

Historicky, jak se standardy 3GPP vyvíjely od R99 (první verze UMTS) přes následující verze, význam CD rostl s rostoucí komplexitou služeb. Stala se nedílnou součástí řízení nárazové povahy internetového provozu a podpory trvalého připojení bez trvalého vyčleňování prostředků. V moderních 5G sítích, s network slicing a massive IoT, je CD nezbytná pro rychlé přepřidělování prostředků mezi řezy nebo IoT zařízeními se sporadickou aktivitou, což umožňuje síti být jak efektivní, tak flexibilní.

## Klíčové vlastnosti

- Dynamické uvolňování nevyužívaných rádiových přenosových kanálů a transportních prostředků
- Politikami řízené uvolňování založené na podmínkách účastníka, služby a sítě
- Koordinace se správou mobility pro zajištění kontinuity relace během předávání spojení
- Integrace s účtovacími systémy pro zastavení účtování po uvolnění prostředků
- Mechanismy založené na časovačích a prahových hodnotách pro rozlišení stavů nečinnosti od konce relace
- Podpora statistického multiplexování vrácením kapacity do sdíleného fondu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.072** (Rel-19) — Call Deflection (CD) Supplementary Service
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TR 22.980** (Rel-19) — Network Composition Feasibility Study
- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP
- **TS 23.097** (Rel-19) — Multiple Subscriber Profile (MSP) Phase 2
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- … a dalších 18 specifikací

---

📖 **Anglický originál a plná specifikace:** [CD na 3GPP Explorer](https://3gpp-explorer.com/glossary/cd/)
