---
slug: "wwt"
url: "/mobilnisite/slovnik/wwt/"
type: "slovnik"
title: "WWT – Work Waiting Time"
date: 2025-01-01
abbr: "WWT"
fullName: "Work Waiting Time"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wwt/"
summary: "Výkonnostní metrika definovaná 3GPP pro měření doby, po kterou úloha nebo proces čeká ve frontě před zpracováním síťovým prvkem. Používá se při správě a optimalizaci sítě k posouzení efektivity systém"
---

WWT je výkonnostní metrika 3GPP, která měří dobu, po kterou úloha čeká ve frontě před zpracováním síťovým prvkem; používá se k hodnocení efektivity a identifikaci úzkých míst.

## Popis

Work Waiting Time (WWT, doba čekání úlohy) je klíčový výkonnostní ukazatel ([KPI](/mobilnisite/slovnik/kpi/)) definovaný ve standardech 3GPP, zejména v TS 21.905 (slovníku specifikací 3GPP), který kvantifikuje zpoždění, jež zaznamenávají pracovní položky nebo úlohy v telekomunikační síti předtím, než je obslouží zpracovatelský subjekt. V síťových operacích mohou úlohy zahrnovat signalizační zprávy, datové pakety, řídicí operace nebo výpočetní úkoly, které vyžadují zpracování síťovými funkcemi, jako jsou základnové stanice, uzly jádra sítě nebo systémy správy. WWT měří interval od příchodu úlohy do fronty nebo bufferu do zahájení jejího aktivního zpracování, nezahrnuje však samotnou dobu provádění. Tato metrika je klíčová pro pochopení latence systému, zahlcení a využití zdrojů a poskytuje vhled do reaktivity a efektivity síťových komponent.

Z architektonického hlediska je WWT použitelná napříč více vrstvami systému 3GPP, od rádiové přístupové sítě (RAN) přes jádro sítě (CN) až po rovinu správy. Například v RAN může WWT odkazovat na dobu, po kterou uživatelská data čekají v bufferu na eNodeB/gNB před naplánováním přenosu přes rozhraní vzduchu. V jádře sítě může měřit zpoždění pro zprávy Diameter nebo [HTTP](/mobilnisite/slovnik/http/)/2 ve signalizačním směrovači před jejich předáním cílovému uzlu. Měření je typicky implementováno pomocí čítačů a časových razítek v rámci síťového softwaru, kde jsou zaznamenávány události příchodu a zahájení zpracování. Systémy správy, jako je Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)), shromažďují WWT data prostřednictvím rozhraní jako Itf-N nebo pomocí protokolů jako [SNMP](/mobilnisite/slovnik/snmp/), což umožňuje monitorování a analýzu výkonu.

Při provozu se WWT vypočítá odečtením časového razítka příchodu úlohy od časového razítka zahájení zpracování. To vyžaduje synchronizovaný čas napříč síťovými prvky, čehož se často dosahuje pomocí protokolů jako [NTP](/mobilnisite/slovnik/ntp/) (Network Time Protocol) nebo vestavěné synchronizace hodin v systémech 5G. Vysoké hodnoty WWT indikují zahlcení, nedostatečnou kapacitu zpracování nebo neefektivní plánovací algoritmy, což může zhoršit uživatelský zážitek zvýšením celkové latence pro služby jako hlasové hovory, streamování videa nebo IoT komunikace. Síťoví operátoři využívají trendy WWT k spouštění optimalizačních akcí, jako je vyvažování zátěže, navyšování kapacity nebo ladění parametrů. Například v Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) může nadměrná WWT pro žádosti o připojení signalizovat potřebu dalších instancí nebo lepší alokace zdrojů.

Klíčové komponenty spojené s WWT zahrnují síťové prvky, které metriku generují (např. gNB, SMF, UPF), systémy správy, které ji shromažďují a analyzují, a standardizaci, která definuje její metodiku měření. Úlohou WWT je poskytnout detailní pohled na doby čekání, čímž doplňuje další KPI, jako je propustnost, ztrátovost paketů a jitter. Je obzvláště důležitá v 5G a novějších sítích, kde ultra-spolehlivá nízkolatenční komunikace (URLLC) a komunikace s masivním počtem zařízení (mMTC) vyžadují přísné záruky latence. Monitorováním WWT mohou operátoři zajistit, že síťové funkce splňují smlouvy o úrovni služeb (SLA) a udržují kvalitu služeb (QoS) napříč různými případy použití, od rozšířeného mobilního širokopásmového připojení až po kritické IoT aplikace.

## K čemu slouží

WWT byla zavedena ve 3GPP Release 4 jako součást širšího rámce pro správu a optimalizaci výkonu sítě. Před její standardizací síťovým operátorům chyběla konzistentní metrika pro měření čekacích dob uvnitř síťových prvků, což ztěžovalo diagnostiku problémů s latencí a optimalizaci alokace zdrojů. Jak se mobilní sítě vyvíjely od přepojování okruhů pro hlas k přepojování paketů pro datové služby, rostla složitost síťových funkcí, což vedlo k možným úzkým místům ve signalizaci a zpracování dat. WWT tento problém řeší tím, že poskytuje standardizovaný způsob kvantifikace doby čekání, což operátorům umožňuje identifikovat neefektivity, plánovat kapacitu a zlepšovat celkovou reaktivitu systému.

Historicky se první mobilní sítě (2G/3G) soustředily na základní konektivitu a monitorování výkonu bylo omezeno na metriky, jako je míra přerušení hovorů a síla signálu. S příchodem 3GPP Release 4 a zavedením plně IP sítí však vzrostla potřeba jemnějších nástrojů správy pro podporu datových služeb a zajištění kvality uživatelského zážitku. WWT se objevila jako řešení pro měření zpoždění ve frontách zpracování, která jsou kritická pro aplikace v reálném čase a spolehlivost signalizace. Řeší omezení předchozích přístupů, které často přehlížely vnitřní doby čekání a soustředily se spíše na celkovou latenci, což mohlo maskovat konkrétní místa zahlcení.

Definováním WWT umožňuje 3GPP proaktivní správu sítě, což operátorům dovoluje detekovat a řešit problémy dříve, než ovlivní uživatele. Podporuje vývoj směrem k automatizovaným a samoopravným sítím (SON), kde mohou WWT data vstupovat do algoritmů pro dynamické úpravy zdrojů. WWT v podstatě existuje pro zvýšení efektivity a spolehlivosti sítě, řeší problém skrytých zpoždění v prostředích s více dodavateli a zajišťuje, že mobilní sítě mohou uspokojovat rostoucí požadavky na nízkou latenci a vysoký výkon napříč releasy od 4G přes 5G a dále.

## Klíčové vlastnosti

- Standardizovaný KPI pro měření čekacích dob úloh v prvcích sítě 3GPP
- Použitelný napříč RAN, jádrem sítě a systémy správy pro komplexní analýzu výkonu
- Podporuje synchronizované časové razítkování pomocí protokolů jako NTP pro přesné měření
- Umožňuje detekci zahlcení a úzkých míst pro usnadnění optimalizace sítě
- Integruje se se systémy správy (NMS/EMS) pro monitorování a reportování v reálném čase
- Kritický pro zajištění nízkolatenčního výkonu ve scénářích 5G URLLC a mMTC

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [WWT na 3GPP Explorer](https://3gpp-explorer.com/glossary/wwt/)
