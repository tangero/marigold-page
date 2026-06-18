---
slug: "csi-im"
url: "/mobilnisite/slovnik/csi-im/"
type: "slovnik"
title: "CSI-IM – CSI-Interference Measurement"
date: 2025-01-01
abbr: "CSI-IM"
fullName: "CSI-Interference Measurement"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/csi-im/"
summary: "CSI-IM je referenční signál v LTE a NR, který umožňuje UE měřit rušení ze sousedních buněk. Je klíčový pro přesné hlášení informace o stavu kanálu (CSI), na jehož základě základnová stanice rozhoduje"
---

CSI-IM je referenční signál v LTE a NR, který umožňuje uživatelskému zařízení měřit rušení ze sousedních buněk pro přesné hlášení informace o stavu kanálu.

## Popis

CSI-IM (CSI-Interference Measurement) je klíčový mechanismus fyzické vrstvy definovaný ve specifikacích 3GPP pro LTE a 5G NR. Jedná se o sadu prvků prostředků ([RE](/mobilnisite/slovnik/re/)) v časově-frekvenční mřížce, které jsou sítí konfigurovány tak, aby na nich nebyl přenášen žádný požadovaný signál z obsluhující buňky. Uživatelské zařízení (UE) měří výkon přijatý na těchto specifických RE, který se primárně skládá z rušení a šumu z jiných buněk, uživatelů na stejném kanálu nebo jiných zdrojů šumu. Tato naměřená úroveň rušení je klíčovým vstupem pro výpočet informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) v UE, která zahrnuje metriky jako indikátor kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)), indikátor předkodovací matice ([PMI](/mobilnisite/slovnik/pmi/)) a indikátor hodnosti ([RI](/mobilnisite/slovnik/ri/)). Architektura pro CSI-IM zahrnuje konfiguraci prostředku CSI-IM pro UE ze strany základnové stanice ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR) pomocí signalizace vyšší vrstvy ([RRC](/mobilnisite/slovnik/rrc/)). Tato konfigurace specifikuje periodicitu, časový posun a frekvenční umístění (např. konkrétní bloky prostředků a [OFDM](/mobilnisite/slovnik/ofdm/) symboly) prostředku CSI-IM. Konfigurace je sladěna s prostředkem CSI-RS (Channel State Information Reference Signal) pro měření požadovaného signálu, což umožňuje UE vypočítat CSI na základě odhadů signálu i rušení z koordinovaných prostředků. Fyzická vrstva UE následně provádí měření během konfigurovaných výskytů CSI-IM, typicky za použití technik jako je odhad lineárního minimálního středního kvadratického výběru (LMMSE) nebo jednoduššího průměrování výkonu. Naměřené rušení je pak použito v algoritmu výpočtu CSI, který často zahrnuje vyhledávací tabulku nebo vzorec pro mapování odhadnutého poměru signálu k rušení a šumu (SINR) na doporučenou hodnotu CQI. Konečná zpráva CSI, která zahrnuje toto měření zohledňující rušení, je pak odeslána zpět základnové stanici přes PUCCH nebo PUSCH. V síti plánovač na základnové stanici používá tuto zprávu CSI k inteligentnímu rozhodování o modulačním a kódovém schématu (MCS), prostorových vrstvách (hodnosti) a předkódování pro downlinkové přenosy k danému UE. Díky přesné znalosti podmínek rušení se plánovač může vyvarovat příliš agresivního výběru MCS, který by vedl k vysoké chybovosti bloků, nebo naopak příliš konzervativního výběru, který plýtvá spektrální účinností. Tato dynamická adaptace je zásadní pro maximalizaci propustnosti a spolehlivosti, zejména v hustých nasazeních, heterogenních sítích (HetNets) a scénářích koordinovaného multipointu (CoMP), kde je rušení dynamické a významné. Dále, u pokročilých funkcí jako je potlačení a zrušení rušení s podporou sítě (NAICS), může měření CSI-IM pomoci UE identifikovat specifické rušivé signály.

## K čemu slouží

CSI-IM byl zaveden, aby řešil základní omezení starších verzí LTE (před Rel-11), kde hlášení CSI bylo primárně založeno na měření výkonu požadovaného signálu (pomocí CRS nebo později CSI-RS), ale spoléhalo se na implicitní nebo zastaralý předpoklad o úrovních rušení. Před zavedením CSI-IM bylo rušení často odhadováno z běžných referenčních signálů (CRS), které nesly signály jak požadované, tak rušivé buňky, což ztěžovalo izolaci složky rušení, zejména ve scénářích s téměř prázdnými podrámci (ABS) nebo dynamickým výběrem bodu. To vedlo k nepřesným hlášením CQI, kvůli kterým základnová stanice volila suboptimální modulační a kódová schémata, což mělo za následek buď promrhanou kapacitu (při příliš konzervativním přístupu), nebo vysokou míru retransmisí (při příliš agresivním přístupu). Vytvoření CSI-IM bylo motivováno potřebou vylepšeného řízení rušení v sítích LTE-Advanced, zejména pro funkce jako vylepšená koordinace mezibuněčného rušení (eICIC), dále vylepšená ICIC (FeICIC) a koordinovaný multipoint (CoMP). Tyto funkce vytvářely dynamické vzorce rušení, které tradiční metody nedokázaly přesně sledovat. CSI-IM poskytuje vyhrazený, konfigurovatelný prostředek, kde obsluhující buňka záměrně utlumí svůj přenos, což umožňuje UE získat čisté měření převládajícího rušení. To umožňuje přesnější adaptaci spojení a plánování, což přímo zlepšuje spektrální účinnost a uživatelský komfort na okraji buňky a v heterogenních topologiích sítě. Jeho zavedení bylo klíčovým krokem k tomu, aby se buněčné sítě staly robustnějšími a účinnějšími v kontextu rostoucí hustoty nasazení a poptávky po přenosu dat.

## Klíčové vlastnosti

- Poskytuje síťově konfigurované prostředky pro explicitní měření rušení
- Umožňuje přesný odhad SINR pro výpočet CSI (CQI/PMI/RI)
- Podporuje dynamické techniky koordinace rušení jako eICIC a CoMP
- Konfigurovatelné v čase, frekvenci a periodicitě pomocí RRC signalizace
- Nezbytné pro pokročilé schopnosti přijímače, jako je NAICS
- Základní pro plánování MU-MIMO a přidělování prostředků zohledňující rušení

## Související pojmy

- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [NAICS – Network-Assisted Interference Cancellation and Suppression](/mobilnisite/slovnik/naics/)

## Definující specifikace

- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CSI-IM na 3GPP Explorer](https://3gpp-explorer.com/glossary/csi-im/)
