---
slug: "gsi"
url: "/mobilnisite/slovnik/gsi/"
type: "slovnik"
title: "GSI – Green Standard Interface"
date: 2025-01-01
abbr: "GSI"
fullName: "Green Standard Interface"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/gsi/"
summary: "Rozhraní Green Standard Interface (GSI) je řídicí rozhraní definované 3GPP pro standardizaci monitorování a reportování metrik energetické účinnosti a dopadu na životní prostředí pro síťová zařízení."
---

GSI je rozhraní Green Standard Interface definované 3GPP pro standardizaci monitorování a reportování metrik energetické účinnosti a dopadu na životní prostředí, jako je spotřeba energie a uhlíková stopa, v síťových zařízeních.

## Popis

Rozhraní Green Standard Interface (GSI) je standardizované severojižní rozhraní specifikované v rámci architektury Management and Orchestration ([MANO](/mobilnisite/slovnik/mano/)) 3GPP, primárně dokumentované v TS 32.972. Jeho hlavní funkcí je poskytovat jednotný datový model a protokol pro výměnu informací o energetickém a environmentálním výkonu mezi síťovými prvky (jako jsou základnové stanice, funkce jádra sítě) a řídicími systémy operátora, jako jsou Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)). Rozhraní je navrženo jako technologicky neutrální, podporující jak tradiční, tak virtualizované síťové funkce, a typicky využívá protokoly jako NETCONF/YANG nebo RESTful [API](/mobilnisite/slovnik/api/) pro přenos strukturovaných dat.

Architektonicky GSI definuje sadu spravovaných objektů, atributů a notifikací, které reprezentují ukazatele ekologického výkonu. Klíčové datové body zahrnují aktuální a historickou spotřebu energie (často členěnou podle komponent, jako je rádiová jednotka, základní pásmo, chlazení), metriky využití (např. zatížení provozem vs. spotřebovaná energie), teplotní údaje a odvozené metriky, jako je Energy Consumption Rating (ECR) nebo emise ekvivalentu oxidu uhličitého (CO2e) založené na profilech zdrojů energie. Síťové prvky fungují jako agenti, kteří tato data sbírají z hardwarových senzorů a softwarových čítačů, a zpřístupňují je prostřednictvím GSI. Řídicí systém funguje jako manažer, který tato data dotazuje nebo k nim přihlašuje odběr pro centralizovanou analýzu, reportování a potenciálně pro spouštění politik úspory energie.

Role GSI v síti je klíčová pro provozní udržitelnost. Přesouvá správu energie z proprietární, izolované činnosti na standardizovanou, integrovanou součást síťových operací. Poskytnutím společného jazyka pro 'zelené' metriky umožňuje operátorům porovnávat zařízení od různých dodavatelů, provádět přesné energetické audity v celé síti a ověřovat účinnost funkcí pro úsporu energie, jako jsou režimy hlubokého spánku nebo vypínání buněk. Dále podporuje dodržování regulatorních požadavků tím, že umožňuje standardizované reportování o dopadu na životní prostředí, což je stále častěji vyžadováno vládami a průmyslovými organizacemi. V podstatě GSI poskytuje základní telemetrickou vrstvu nezbytnou pro inteligentní, daty řízenou správu energie v moderních mobilních sítích.

## K čemu slouží

Rozhraní Green Standard Interface bylo vytvořeno, aby řešilo rostoucí potřebu operátorů mobilních sítí snížit své provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a dopad na životní prostředí. Náklady na energii tvoří významnou část síťových OPEX a společenský tlak na boj proti změně klimatu učinil energetickou účinnost klíčovým strategickým cílem. Před zavedením GSI byl sběr energetických dat velmi fragmentovaný; každý dodavatel poskytoval pro své zařízení proprietární rozhraní a datové formáty, což operátorům extrémně ztěžovalo získání uceleného a přesného pohledu na spotřebu energie v celé síti. Tento nedostatek standardizace bránil efektivní správě energie, srovnávání a automatizaci opatření pro úsporu energie.

Motivováno těmito výzvami, zavedlo 3GPP GSI ve verzi 15 jako součást širší iniciativy 'Green Networks'. Jeho vytvoření bylo hnací silou potřeby dodavatelsky neutrálního, standardy založeného přístupu ke správě energie. Rozhraní řeší problém datových izolací definováním společného informačního modelu a komunikační metody. To umožňuje řídicím systémům operátora bezproblémově sbírat, korelovat a analyzovat energetická data z více-dodavatelských sítí. Také zajišťuje budoucí kompatibilitu sítí tím, že poskytuje škálovatelný rámec pro začlenění nových energetických metrik a možností správy, jak jsou vyvíjeny v následujících vydáních 3GPP, čímž podporuje dlouhodobé cíle dekarbonizace odvětví.

## Klíčové vlastnosti

- Standardizovaný informační model pro data o energetickém a environmentálním výkonu
- Dodavatelsky neutrální rozhraní podporující jak fyzické, tak virtualizované síťové funkce
- Podpora pro monitorování v reálném čase a sběr historických dat o spotřebě energie
- Definice klíčových ukazatelů výkonnosti (KPI), jako je Energy Consumption Rating (ECR)
- Mechanismy pro notifikaci událostí (např. upozornění na překročení prahové hodnoty výkonu)
- Umožňuje síťové srovnávání energetické účinnosti a regulatorní reportování

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [MANO – Management and Orchestration](/mobilnisite/slovnik/mano/)
- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks

---

📖 **Anglický originál a plná specifikace:** [GSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/gsi/)
