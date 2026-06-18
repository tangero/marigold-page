---
slug: "tecu"
url: "/mobilnisite/slovnik/tecu/"
type: "slovnik"
title: "TECU – TEC Units"
date: 2025-01-01
abbr: "TECU"
fullName: "TEC Units"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tecu/"
summary: "TEC jednotky (jednotky charakterizace časové chyby) jsou standardizované měřící jednotky používané pro charakterizaci časové chyby v 3GPP polohovacích systémech. Poskytují společnou, kvantifikovatelno"
---

TECU je standardizovaná jednotka pro měření časových chyb v 3GPP polohovacích systémech, která poskytuje společnou metriku pro hodnocení výkonu metod jako OTDOA a RTT.

## Popis

[TEC](/mobilnisite/slovnik/tec/) jednotky (jednotky charakterizace časové chyby) jsou základním konceptem definovaným ve specifikaci 3GPP 37.355 za účelem standardizace měření a hlášení časových chyb v rámci polohovacích architektur, zejména pro LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR Positioning Protocol A (NRPPa). Slouží jako normalizovaná bezrozměrná jednotka, která kvantifikuje chybu v časových měřeních, jež jsou klíčová pro metody jako Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) a Round-Trip Time ([RTT](/mobilnisite/slovnik/rtt/)). Převodem nezpracovaných časových měření (např. v nanosekundách) na TECU systém abstrahuje od hardwarově specifických variací a poskytuje konzistentní škálu pro posuzování chyb napříč různými síťovými prvky a implementacemi UE.

Fungování TECU je integrováno do rámce hlášení polohovacích měření. Když uživatelské zařízení (UE) nebo funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) vypočítá časové měření pro polohování, vypočítá také přidruženou časovou chybu. Tato chyba je následně vyjádřena v TECU na základě předdefinovaných konverzních vzorců nebo tabulek, které dávají do vztahu fyzickou nejistotu časování (ovlivněnou faktory jako poměr signálu k šumu, šířka pásma a vícecestné šíření) se standardizovanou jednotkou. LMF nebo jiné síťové funkce používají tyto hodnoty TECU k posouzení kvality polohových určení, aplikaci algoritmů pro zmírnění chyb a k rozhodování o výběru polohovací metody nebo fúzi hybridních dat.

Klíčové komponenty spojené s TECU zahrnují polohovací protokoly (LPP/NRPPa), které přenášejí hlášení chyb kvantifikovaných v TECU, motory polohovacích měření v UE a gNB/ng-eNB, které generují nezpracovaná časová data, a polohovací servery (LMF), která tato hlášení zpracovávají. Úlohou TECU je umožnit interoperabilitu a srovnávání výkonnosti. Umožňují síťovým operátorům nastavovat prahové hodnoty kvality, porovnávat výkon polohování napříč různými releasy nebo nasazeními a usnadňovat pokročilé funkce, jako jsou vylepšené služby založené na poloze a nouzové polohování se známými mezemi přesnosti. Bez takové standardizované jednotky by hlášení chyb záviselo na konkrétní implementaci, což by bránilo optimalizaci sítě a smlouvám o úrovni služeb.

## K čemu slouží

[TEC](/mobilnisite/slovnik/tec/) jednotky byly zavedeny v 3GPP Release 16, aby řešily rostoucí potřebu standardizovaných a kvantifikovatelných metrik přesnosti v celulárních polohovacích systémech. Jak služby založené na poloze, nouzové volání (např. E911) a průmyslové IoT aplikace začaly vyžadovat vyšší přesnost, omezení proprietárního nebo nejednoznačného hlášení chyb se stala zjevnými. Předchozí přístupy se často spoléhaly na indikátory specifické pro dodavatele nebo nezpracované statistické hodnoty (jako je rozptyl), které bylo obtížné porovnávat napříč různými čipsety UE nebo síťovou infrastrukturou, což komplikovalo plánování sítě, odstraňování problémů a zajištění služeb.

Vytvoření TECU bylo motivováno požadavkem na podporu pokročilých polohovacích technik v 5G NR a vyvinutém LTE, jako je multi-RTT a polohování založené na úhlu, kde je přesnost časování prvořadá. Definováním společné jednotky 3GPP umožnilo konzistentní hodnocení výkonu, certifikační testování a minimalizaci problémů s interoperabilitou. Řeší problém nejednoznačné kvality služby (QoS) polohování tím, že poskytuje jasnou metriku, kterou lze použít v parametrech QoS pro polohování, což umožňuje síti požadovat polohování s konkrétním cílem přesnosti vyjádřeným v TECU. Tato standardizace je zásadní pro splnění regulatorních požadavků na nouzové služby a pro umožnění komerčních aplikací založených na poloze, které závisí na spolehlivých informacích o přesnosti.

## Klíčové vlastnosti

- Standardizovaná bezrozměrná jednotka pro hlášení časové chyby
- Umožňuje konzistentní hodnocení výkonu polohování napříč dodavateli a releasy
- Integrována do hlášení polohovacích měření protokolů LPP a NRPPa
- Podporuje převod z fyzikálních nejistot časování (např. v důsledku SNR, šířky pásma)
- Usnadňuje správu QoS polohování a nastavování cílů přesnosti
- Nezbytná pro optimalizaci sítě a srovnávání výkonnosti polohovacích algoritmů

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [TECU na 3GPP Explorer](https://3gpp-explorer.com/glossary/tecu/)
