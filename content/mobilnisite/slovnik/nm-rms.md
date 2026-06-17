---
slug: "nm-rms"
url: "/mobilnisite/slovnik/nm-rms/"
type: "slovnik"
title: "NM-RMS – Network Management layer RMS"
date: 2025-01-01
abbr: "NM-RMS"
fullName: "Network Management layer RMS"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/nm-rms/"
summary: "NM-RMS (Root Mean Square – střední kvadratická odchylka na vrstvě síťového managementu) je statistická metrika používaná v rámci síťového managementu 3GPP pro kvantifikaci výkonnostních odchylek. Posk"
---

NM-RMS je statistická metrika používaná v síťovém managementu 3GPP pro měření odchylky klíčových ukazatelů výkonnosti od jejich cílových hodnot za účelem přesného hodnocení výkonu.

## Popis

NM-RMS (Network Management layer Root Mean Square – střední kvadratická odchylka na vrstvě síťového managementu) je koncept definovaný ve specifikacích 3GPP pro správu výkonnosti. Nejde o fyzickou entitu, ale o matematickou funkci aplikovanou na data z měření výkonnosti. Výpočet RMS poskytuje jedinou skalární hodnotu, která reprezentuje velikost souboru odchylek, typicky rozdílů mezi naměřenými klíčovými ukazateli výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)) a jejich cílovými nebo očekávanými hodnotami. Tato metrika je klíčová pro kvantifikaci 'chyby' nebo 'rozptylu' ve výkonu sítě statisticky robustním způsobem, protože před zprůměrováním odmocňuje součet čtverců odchylek, čímž dává větší váhu větším chybám.

Z architektonického hlediska je funkce NM-RMS implementována ve vrstvě síťového managementu ([NM](/mobilnisite/slovnik/nm/)), která je součástí Operations Support System ([OSS](/mobilnisite/slovnik/oss/)). Funguje na datech o výkonnosti shromážděných ze sítě prostřednictvím rozhraní Itf-N nebo jiných rozhraní pro management. Data proudí od síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) nebo systémů pro správu prvků ([EMS](/mobilnisite/slovnik/ems/)) do systému NM, kde aplikace pro správu výkonnosti počítají různé metriky, včetně hodnot RMS pro předdefinované KPI. Výpočet se typicky provádí po stanovenou dobu měření a s určitou granularitou definovanou v úloze správy výkonnosti.

Úlohou NM-RMS v síti je poskytnout konsolidované, kvantitativní měřítko souladu s požadavky na výkon nebo odchylky od nich. Lze ji například použít k posouzení, jak blízko se naměřená latence, propustnost nebo dostupnost služby shodují s cíli definovanými ve smlouvě o úrovni služeb (SLA). Použitím RMS namísto prostého průměru odchylek mohou operátoři sítí lépe identifikovat a stanovit prioritu problémů, kde je výkon výrazně mimo cílové hodnoty, protože velké odchylky mají neúměrně vysoký dopad na hodnotu RMS. To podporuje analýzu hlavní příčiny a nápravná opatření v cyklech optimalizace sítě.

## K čemu slouží

Metrika NM-RMS byla zavedena, aby řešila potřebu nuancejšího a lépe využitelného hodnocení výkonu ve složitých sítích 3GPP. Jednoduché průměrné odchylky mohou zakrýt dopad závažných, sporadických výkonnostních problémů, protože kladné a záporné odchylky se mohou vzájemně vyrušit. Výpočet RMS to řeší tím, že uvažuje druhou mocninu odchylek, čímž zajišťuje, že všechny rozptyly přispívají kladně k výsledné metrice a že větší odlehlé hodnoty jsou řádně zdůrazněny.

Historicky se síťový management spoléhal na alarmy založené na prahových hodnotách a jednoduché průměry, což mohlo být nedostatečné pro proaktivní správu výkonnosti a ověřování souladu se SLA. Zavedení standardizovaných statistických metrik, jako je RMS, v rámci frameworku managementu 3GPP umožňuje konzistentní, automatizované vyhodnocování výkonnostních trendů a účinnosti optimalizačních akcí. Poskytuje společný jazyk pro definování výkonnostních cílů v manažerských specifikacích a umožňuje sofistikovanější analýzy a reportování v rámci [OSS](/mobilnisite/slovnik/oss/).

## Klíčové vlastnosti

- Standardizovaná statistická metrika pro výkonnostní odchylku definovaná v 3GPP TS 28.304 a 28.305
- Vypočítá střední kvadratickou odchylku rozdílů mezi naměřenými KPI a cílovými hodnotami
- Poskytuje jedinou hodnotu kvantifikující velikost výkonnostního rozptylu
- Zdůrazňuje větší odchylky díky operaci umocňování ve svém výpočtu
- Používá se v aplikacích pro hodnocení výkonnosti ve vrstvě síťového managementu (NM)
- Podporuje monitorování souladu se SLA a procesy optimalizace sítě

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)

## Definující specifikace

- **TS 28.304** (Rel-19) — PEE Parameters Control & Monitoring Requirements
- **TS 28.305** (Rel-19) — PEE Control & Monitoring IRP Information Service

---

📖 **Anglický originál a plná specifikace:** [NM-RMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/nm-rms/)
