---
slug: "srm"
url: "/mobilnisite/slovnik/srm/"
type: "slovnik"
title: "SRM – Service Resource Manager"
date: 2025-01-01
abbr: "SRM"
fullName: "Service Resource Manager"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/srm/"
summary: "Funkční entita v rámci IP Multimedia Subsystem (IMS), která spravuje a řídí mediální zdroje, jako jsou konferenční mosty, hlášení a transkódovací jednotky. Funguje jako zprostředkovatel mezi aplikační"
---

SRM je funkční entita v rámci IMS, která spravuje mediální zdroje, jako jsou konferenční mosty, a funguje jako zprostředkovatel mezi aplikačními servery a funkcemi pro mediální zdroje.

## Popis

Service Resource Manager (SRM) je logická funkce definovaná v architektuře 3GPP IMS (IP Multimedia Subsystem), odpovědná za správu a zprostředkování mediálních zdrojů. Funguje jako zprostředkovatel mezi aplikačními servery ([AS](/mobilnisite/slovnik/as/)), které poskytují služby (jako konferenční hovory, hlášení nebo interaktivní hlasová odezva), a funkcí pro mediální zdroje ([MRF](/mobilnisite/slovnik/mrf/)), která je rozdělena na řídicí rovinu ([MRFC](/mobilnisite/slovnik/mrfc/) – Media Resource Function Controller) a uživatelskou rovinu ([MRFP](/mobilnisite/slovnik/mrfp/) – Media Resource Function Processor). SRM poskytuje vyšší, službám přizpůsobené rozhraní pro alokaci, řízení a uvolňování mediálních zdrojů. Když AS potřebuje využít mediální zdroj (např. pro přidání účastníka do konference nebo přehrání hlášení), odešle požadavek na SRM pomocí protokolu [SIP](/mobilnisite/slovnik/sip/) nebo proprietárního rozhraní. SRM tento požadavek interpretuje, vybere vhodný MRFC/MRFP na základě dostupnosti zdrojů, shody schopností (např. požadované kodeky) a zásad a přepošle potřebné řídicí příkazy.

Z architektonického hlediska SRM zvyšuje flexibilitu a škálovatelnost mediálních služeb v IMS. Odstiňuje detaily podkladové infrastruktury MRF od servisní logiky. To umožňuje dynamické sdílení fondu zdrojů MRF napříč více aplikacemi a službami. SRM může provádět vyvažování zátěže mezi více MRFC, spravovat rezervace zdrojů a řešit složité scénáře, jako jsou vnořené služby nebo konflikty zdrojů. Typicky udržuje informace o stavu alokovaných zdrojů a jejich přiřazení k probíhajícím servisním relacím. Komunikace mezi SRM a MRFC může používat protokol H.248 (Megaco) nebo jiné protokoly pro řízení médií, jak stanovuje 3GPP a ovlivňují je schopnosti MRFP.

Při provozu hraje SRM klíčovou roli při umožňování pokročilých služeb komunikace v reálném čase. Pro multimediální konferenci by AS požádal SRM o konferenční zdroj. SRM by alokoval konferenční most MRFP, poskytl AS potřebné informace o připojení (např. [SDP](/mobilnisite/slovnik/sdp/) nabídku pro mediální rovinu) a spravoval životní cyklus tohoto zdroje. Podobně pro službu personalizovaného vyzváněcího tónu by SRM spravoval zdroj MRFP, který míchá hovorový zvuk volajícího s médii tónu. Díky centralizaci této správy SRM zabraňuje tomu, aby jednotlivá AS potřebovala podrobné znalosti topologie MRF, podporuje efektivní využití zdrojů a zjednodušuje zavádění nových služeb náročných na média.

## K čemu slouží

SRM byl zaveden, aby řešil výzvy spojené se správou a škálováním mediálních zdrojů v prostředí IMS bohatém na služby. V raných nasazeních IMS nebo před-IMS multimediálních systémech měly aplikační servery často přímé, bod-bod vztahy se specifickými mediálními servery. Tento přístup vedl k neefektivnímu využití zdrojů (uvázlá kapacita), složitosti ve vývoji služeb (každé [AS](/mobilnisite/slovnik/as/) potřebovalo logiku pro řízení médií) a obtížím při vyvažování zátěže a redundanci. Nebyla zde žádná centralizovaná entita, která by zprostředkovávala požadavky a optimalizovala využití nákladných zdrojů pro zpracování médií v celé síti.

Jeho specifikace, počínaje Release 6 s dozráním IMS, poskytla standardizované řešení pro orchestraci mediálních zdrojů. Vyřešila problém izolovaných mediálních zdrojů zavedením funkce zprostředkovatele. To umožňuje síťovým operátorům nasadit fond mediálních zdrojů ([MRF](/mobilnisite/slovnik/mrf/)), které lze dynamicky alokovat na požádání pro jakoukoli službu. Vytvoření SRM bylo motivováno vizí živého ekosystému aplikačních serverů třetích stran; SRM poskytuje jednotné, řízené rozhraní, přes které tyto AS přistupují k síťovým mediálním schopnostem, aniž by byla odhalena vnitřní síťová architektura. Umožňuje pokročilé funkce, jako je správa interakcí služeb (např. řešení konfliktů, když dvě služby požadují stejný mediální stream uživatele), a podporuje efektivnější síťové plánování prostřednictvím statistického multiplexování zdrojů.

## Klíčové vlastnosti

- Zprostředkovává požadavky na mediální zdroje od aplikačních serverů k funkcím pro mediální zdroje
- Odstiňuje topologii a schopnosti MRF od servisní logiky
- Umožňuje dynamické sdílení a vyvažování zátěže napříč fondem zdrojů MRF
- Spravuje životní cyklus (alokaci, modifikaci, uvolnění) mediálních zdrojů
- Podporuje alokaci zdrojů a řešení konfliktů na základě zásad
- Poskytuje standardizované rozhraní pro službám přizpůsobené řízení médií v IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)
- [MRFP – Multimedia Resource Function Processor](/mobilnisite/slovnik/mrfp/)

## Definující specifikace

- **TS 23.877** (Rel-6) — Speech Recognition Framework Analysis
- **TR 23.958** (Rel-19) — EDGEAPP alignment with ETSI MEC and GSMA OP
- **TR 26.918** (Rel-19) — Virtual Reality Relevance Study for 3GPP

---

📖 **Anglický originál a plná specifikace:** [SRM na 3GPP Explorer](https://3gpp-explorer.com/glossary/srm/)
