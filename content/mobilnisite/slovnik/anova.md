---
slug: "anova"
url: "/mobilnisite/slovnik/anova/"
type: "slovnik"
title: "ANOVA – Analysis of Variance"
date: 2025-01-01
abbr: "ANOVA"
fullName: "Analysis of Variance"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/anova/"
summary: "ANOVA je statistická metoda používaná v řízení sítí 3GPP k analýze rozptylu výkonnostních dat. Pomáhá identifikovat významné rozdíly mezi skupinami síťových prvků, což napomáhá detekci chyb a optimali"
---

ANOVA je statistická metoda používaná v řízení sítí 3GPP k analýze rozptylu výkonnostních dat, která pomáhá identifikovat významné rozdíly mezi skupinami síťových prvků pro detekci chyb a optimalizaci.

## Popis

Analýza rozptylu (ANOVA) je statistická technika standardizovaná v rámci 3GPP pro řízení a optimalizaci výkonu sítě. Funguje tak, že rozkládá celkový pozorovaný rozptyl v souboru výkonnostních měřicích dat na složky připisitelné různým zdrojům variability. V telekomunikačním kontextu tyto zdroje typicky zahrnují variace mezi různými síťovými prvky (např. základnovými stanicemi, buňkami), variace v čase a náhodnou chybu. Základní metodologie zahrnuje výpočet součtů čtverců pro tyto různé zdroje, odvození středních čtverců a následné výpočet F-statistiky k testování nulové hypotézy, že průměry skupin (např. výkonnostní metriky z různých buněk) jsou stejné.

Z architektonického hlediska se ANOVA uplatňuje v rámci frameworku Operations, Administration, and Maintenance (OAM), konkrétně ve funkcích Performance Management (PM). Síťové prvky sbírají Klíčové ukazatele výkonnosti (KPIs) a Výkonnostní měření (PMs), která jsou následně předávána systémům Network Management Systems ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management Systems ([EMS](/mobilnisite/slovnik/ems/)). Algoritmus ANOVA zpracovává tato agregovaná data. Klíčovými součástmi analýzy jsou definovaný faktor (nezávislá proměnná, která se testuje, například 'Cell ID' nebo 'Time Period'), závislá proměnná (závislá výkonnostní metrika, jako 'Call Drop Rate' nebo 'Throughput') a výsledný F-test, který určuje statistickou významnost.

Její role v síti je diagnostická a analytická. Provedením ANOVA mohou operátoři sítí objektivně určit, zda jsou pozorované rozdíly ve výkonu mezi například shlukem buněk statisticky významné, nebo jsou pouze důsledkem náhodných fluktuací. To informuje analýzu hlavní příčiny pro správu chyb. Například, pokud ANOVA pro metriku 'Uplink Block Error Rate' napříč několika sektory ukáže významnou F-statistiku, indikuje to, že alespoň jeden sektor funguje mimo očekávaný rozsah, což vyvolá cílené šetření. Tato technika je podrobně popsána v specifikacích jako 3GPP TS 26.935 pro Codec Specific Performance Metrics a 3GPP TS 46.008 pro Half Rate Speech Traffic Channels, kde se používá k analýze rozptylu metrik kvality hovoru za různých síťových podmínek.

## K čemu slouží

ANOVA byla zavedena, aby poskytla operátorům sítí robustní, standardizovaný statistický nástroj pro analýzu výkonnostních dat. Před jejím formálním zařazením se operátoři spoléhali na jednodušší alarmy založené na prahových hodnotách nebo ad-hoc porovnávání dat, což mohlo vést k falešně pozitivním výsledkům (označení normální náhodné variability jako problému) nebo k přehlédnutím (přehlédnutí jemných, ale systematických degradací). Nedostatek statistického frameworku ztěžoval rozlišení mezi variabilitou společných příčin, která je vlastní každému systému, a variabilitou zvláštních příčin, která indikuje skutečnou chybu nebo degradaci.

Hlavním problémem, který ANOVA řeší, je objektivní, kvantitativní posouzení, zda jsou rozdíly ve výkonnostních metrikách napříč síťovými prvky nebo časovými obdobími významné. To je klíčové ve velkých, heterogenních sítích, kde tisíce prvků generují obrovské objemy výkonnostních dat. Ruční třídění těchto dat je nepraktické. ANOVA automatizuje počáteční testování hypotéz a zvýrazňuje oblasti, kde je lidská inženýrská pozornost nejvíce potřebná. Její vznik byl motivován potřebou inteligentnějšího, daty řízeného řízení sítí, jak sítě rostly v komplexitě od 3G k 4G a dále, což znamenalo posun od jednoduchého monitorování k prediktivním a proaktivním paradigmatům údržby.

## Klíčové vlastnosti

- Statistické testování hypotéz pro výkonnostní data
- Rozklad rozptylu na meziskupinovou a vnitroskupinovou složku
- Výpočet F-statistiky pro určení významnosti pozorovaných rozdílů
- Integrace s datovými modely 3GPP Performance Management (PM)
- Aplikace na specifické KPIs jako metriky kvality hovoru a míry blokových chyb
- Podpora analýzy hlavní příčiny v pracovních postupech správy chyb

## Definující specifikace

- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 46.008** (Rel-19) — GSM Half Rate Speech Codec Performance

---

📖 **Anglický originál a plná specifikace:** [ANOVA na 3GPP Explorer](https://3gpp-explorer.com/glossary/anova/)
