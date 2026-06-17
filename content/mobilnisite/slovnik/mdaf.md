---
slug: "mdaf"
url: "/mobilnisite/slovnik/mdaf/"
type: "slovnik"
title: "MDAF – Management Data Analytics Function"
date: 2026-01-01
abbr: "MDAF"
fullName: "Management Data Analytics Function"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mdaf/"
summary: "Síťová funkce v jádru 5G, která poskytuje analytické služby pro manažerská data. Shromažďuje, koreluje a analyzuje data z různých zdrojů, aby generovala poznatky pro automatizaci, optimalizaci a zajiš"
---

MDAF je funkce jádra sítě 5G, která shromažďuje, koreluje a analyzuje manažerská data za účelem generování poznatků pro automatizaci, optimalizaci a zajištění (assurance) sítě.

## Popis

Management Data Analytics Function (MDAF) je standardizovaná síťová funkce 3GPP zavedená ve vydání 16 jako součást frameworku pro správu a orchestraci 5G. Je klíčovou součástí architektury datové analýzy, navrženou k poskytování analýz jako služby dalším manažerským funkcím, síťovým funkcím a externím aplikacím. MDAF funguje tak, že shromažďuje nezpracovaná nebo předzpracovaná data z široké škály zdrojů, včetně síťových funkcí (NFs) prostřednictvím jejich vystavených analytik, funkce Network Data Analytics Function (NWDAF) a různých úložišť manažerských dat. Na tato data následně aplikuje analytickou logiku, která může zahrnovat modely strojového učení, statistickou analýzu a korelační enginy, za účelem vytvoření prakticky využitelných poznatků, predikcí nebo doporučení.

Z architektonického hlediska je MDAF definována sadou rozhraní založených na službách, primárně službou Nmdf_ManagementDataAnalytics, což umožňuje konzumentům žádat o konkrétní analýzy. Podporuje jak model doručování analýz na požádání, tak model předplatného (kontinuálního). Mezi klíčové vnitřní komponenty patří moduly pro příjem dat, analytický engine schopný hostovat a provádět analytické úlohy a modul pro distribuci výsledků. Samotné analytické úlohy mohou být poskytnuty operátorem nebo třetími stranami, což nabízí flexibilitu. Úlohou MDAF je centralizovat a standardizovat analytické zpracování pro úlohy řídicí roviny, oddělující analytickou logiku od bodů sběru a spotřeby dat.

Její činnost zahrnuje několik kroků: nejprve se analytický konzument (jako například Network Slice Management Function nebo funkce Self-Organizing Network) přihlásí k odběru určitého typu analýzy. MDAF následně identifikuje potřebné zdroje vstupních dat, data shromáždí a spustí nakonfigurovaný analytický model. Výstup, jako je například predikce zatížení síťového řezu nebo zpráva o detekci anomálií, je poté doručen konzumentovi. To umožňuje případy užití jako prediktivní škálování síťových zdrojů, analýzu hlavní příčiny poruch a zajištění kvality služeb. Tím, že poskytuje vyhrazenou, škálovatelnou funkci pro manažerskou analýzu, MDAF snižuje složitost pro jednotlivé NFs a manažerské systémy, které již nemusí obsahovat rozsáhlé analytické schopnosti.

## K čemu slouží

MDAF byla vytvořena, aby řešila rostoucí složitost a rozsah sítí 5G, které vyžadují vysoký stupeň automatizace a inteligence pro efektivní provoz. Tradiční systémy správy sítě byly často reaktivní, izolované a spoléhaly na manuální analýzu, což se stalo neudržitelným s dynamickou povahou služeb 5G, jako jsou síťové řezy a ultra-spolehlivá nízkolatenční komunikace (URLLC). Objevila se jasná potřeba proaktivního, daty řízeného přístupu ke správě.

Před zavedením MDAF byly analýzy pro účely správy buď vestavěny do jednotlivých manažerských aplikací, nebo prováděny externími, nestandardizovanými systémy. To vedlo k duplikaci snah o sběr dat, nekonzistentním analytickým výsledkům a vázanosti na dodavatele. MDAF standardizuje analytickou funkci v rámci architektury 3GPP a poskytuje společný framework pro vývoj, nasazování a využívání analytických služeb. Řeší problém fragmentované inteligence tím, že nabízí centralizovaný, ale flexibilní analytický uzel pro řídicí rovinu.

K jejímu vzniku motivovala vize automatizace v uzavřené smyčce, kde se síť může sama konfigurovat, optimalizovat a léčit na základě poznatků v reálném čase. MDAF poskytuje 'mozek' pro takové operace v doméně správy, spotřebovává obrovské množství provozních a výkonnostních dat, aby generovala inteligenci potřebnou pro autonomní rozhodování dalších manažerských funkcí, čímž snižuje provozní náklady ([OPEX](/mobilnisite/slovnik/opex/)) a zlepšuje agilitu a spolehlivost sítě.

## Klíčové vlastnosti

- Standardizované rozhraní založené na službách (Nmdf) pro využívání analýz
- Podpora jak doručování analýz na požádání, tak na základě předplatného
- Schopnost hostovat a provádět analytické modely specifické pro dodavatele nebo operátora
- Integrace s více zdroji dat včetně NWDAF, NFs a úložišť manažerských dat
- Generování poznatků pro případy užití jako prediktivní údržba, plánování kapacity a zajištění služeb
- Prvek umožňující automatizaci řídicí roviny v uzavřené smyčce a síťování založené na záměru (intent-based networking)

## Definující specifikace

- **TS 28.104** (Rel-19) — Management Data Analytics (MDA)
- **TS 28.561** (Rel-20) — Management and Orchestration; Network Digital Twin
- **TS 28.890** (Rel-16) — ONAP-3GPP 5G Management Compatibility Study
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows

---

📖 **Anglický originál a plná specifikace:** [MDAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mdaf/)
