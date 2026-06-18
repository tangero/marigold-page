---
slug: "mepp"
url: "/mobilnisite/slovnik/mepp/"
type: "slovnik"
title: "MEPP – MCPTT Emergency Private Priority"
date: 2025-01-01
abbr: "MEPP"
fullName: "MCPTT Emergency Private Priority"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mepp/"
summary: "MEPP je priorizační mechanismus v rámci služby Mission Critical Push-to-Talk (MCPTT), který umožňuje nouzovým hovorům přerušit probíhající komunikaci a zajistit soukromé kanály. Zajišťuje spolehlivou,"
---

MEPP je priorizační mechanismus v rámci služby MCPTT, který umožňuje nouzovým hovorům přerušit probíhající komunikaci a zajistit soukromé kanály pro záchranné složky.

## Popis

[MCPTT](/mobilnisite/slovnik/mcptt/) Emergency Private Priority (MEPP) je sofistikovaná funkce na úrovni služby definovaná v rámci standardů 3GPP pro služby kritické pro misi, konkrétně pro Push-to-Talk (MCPTT). Funguje jako vrstvený priorizační mechanismus nad standardní architekturou MCPTT, která je sama postavena na jádru IP Multimedia Subsystem (IMS). Systém zahrnuje několik klíčových komponent: MCPTT klienta na uživatelském zařízení (UE), MCPTT server (který může být součástí aplikačního serveru v IMS) a podkladovou síť LTE nebo 5G poskytující konektivitu a QoS přenosy. MEPP funguje tak, že autorizovanému uživateli umožní zahájit nouzový hovor se specifickou, nejvyšší úrovní priority. Jeho aktivace spustí řadu síťových akcí. Nejprve MCPTT server rozpozná indikátor nouzové priority ze signalizace zahajování relace (např. pomocí protokolů [SIP](/mobilnisite/slovnik/sip/)). Server následně spravuje mediální rovinu, aby zajistil přidělení prostředků pro nouzový hovor. To často zahrnuje přerušení nebo snížení priority stávajících, níže prioritních skupinových nebo privátních hovorů MCPTT na stejném skupinovém kanálu. Klíčové je, že MEPP také zajišťuje, aby byl hovor v kontextu nouzové situace navázán jako 'privátní', což typicky znamená bod-bod nebo spojení s konkrétním dispečerem, čímž se obchází standardní arbitráž řečníka ve skupině, a zaručuje se tak okamžitá a jasná komunikace pro iniciátora nouzové situace.

Úloha MEPP v síti spočívá v poskytování deterministické, vysoce jisté komunikace pro uživatele z oblasti veřejné bezpečnosti a služeb kritických pro misi. Jeho provoz je těsně integrován s rámcem QoS sítí 3GPP. MCPTT server komunikuje s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v 5G za účelem zřízení vyhrazených QoS toků se zaručenou přenosovou rychlostí ([GBR](/mobilnisite/slovnik/gbr/)) pro nouzová média. To zajišťuje nízkou latenci a vysokou spolehlivost pro hlasové pakety. Dále je aspekt 'privátnosti' MEPP vynucován na aplikační vrstvě MCPTT serverem, který řídí správu práva mluvit a distribuci médií, čímž zajišťuje, že pouze nouzový volající a určený příjemce (příjemci) jsou v aktivní relaci. Tím se zabrání přerušování kritického dialogu ostatními členy skupiny. Tato funkce je klíčovým kamenem pro to, aby se sítě LTE a 5G staly vhodnou náhradou za tradiční systémy pozemní mobilní rádiové komunikace ([LMR](/mobilnisite/slovnik/lmr/)), neboť replikuje kritickou funkci 'nouzového tlačítka' s přidanými výhodami širokopásmových médií a síťové integrace.

## K čemu slouží

MEPP byl vytvořen, aby řešil základní požadavek v profesionální a bezpečnostní komunikaci: garantovanou schopnost zahájit vysoce prioritní, nerušený hovor během život ohrožující nebo kritické události. Před jeho standardizací v 3GPP Release 13 komerční mobilní sítě postrádaly standardizované mechanismy pro přerušující nouzové hlasové služby v kontextu skupinové komunikace. Tradiční systémy [LMR](/mobilnisite/slovnik/lmr/) měly vyhrazená hardwarová tlačítka (nouzové poplachy), která okamžitě obsadila kanál. Motivací pro MEPP bylo přenést tuto nezbytnou funkcionalitu do IP-bazovaného ekosystému 3GPP jako součást širší sady služeb [MCPTT](/mobilnisite/slovnik/mcptt/), což umožnilo uživatelům služeb kritických pro misi přejít ze starších systémů LMR na moderní širokopásmové sítě bez obětování operačních schopností.

Vývoj byl řízen globálními organizacemi pro veřejnou bezpečnost a normalizačními orgány, jako jsou 3GPP a Evropský institut pro telekomunikační standardy (ETSI) pro kritickou komunikaci (TCCA). Omezení předchozích přístupů, včetně základního VoIP nebo komerčních PTT aplikací, spočívala v nedostatku síťově asistované priority, náchylnosti k zahlcení a neschopnosti přerušit stávající hovory. MEPP tyto problémy řeší využitím standardizovaných mechanismů priority a QoS sítí 3GPP, čímž zajišťuje, že nouzový hovor je rozpoznán a obsluhován jádrem sítě a aplikačními servery s nejvyšší předností. Poskytuje technický základ pro spolehlivou koordinaci nouzového zásahu, což je zásadní pro bezpečnost záchranných složek i veřejnosti.

## Klíčové vlastnosti

- Přerušení s nejvyšší prioritou pro nouzové hovory v rámci skupin MCPTT
- Vytváření privátních přenosových cest během nouzových scénářů
- Integrace s rámcem QoS 3GPP pro zaručené přenosové prostředky
- Řízení práva mluvit na aplikační vrstvě pro izolaci nouzového komunikátora
- Standardizovaná signalizace využívající SIP a protokoly specifické pro MCPTT
- Podpora v architekturách sítí LTE (EPS) i 5G (5GS)

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- **TS 36.579** — 3GPP TR 36.579
- **TS 37.579** (Rel-18) — Mission Critical services conformance testing

---

📖 **Anglický originál a plná specifikace:** [MEPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mepp/)
