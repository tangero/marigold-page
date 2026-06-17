---
slug: "fds"
url: "/mobilnisite/slovnik/fds/"
type: "slovnik"
title: "FDS – Fraud Detection System"
date: 2025-01-01
abbr: "FDS"
fullName: "Fraud Detection System"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/fds/"
summary: "Síťový systém, který monitoruje vzorce chování účastníků a signalizační události za účelem identifikace a potlačení podvodných aktivit, jako je podvodná registrace, klonování nebo zneužívání služeb s"
---

FDS je síťový systém, který monitoruje využívání služeb účastníky a signalizační provoz za účelem identifikace a potlačení podvodných aktivit, jako je podvodná registrace nebo klonování SIM karet, pomocí pravidel, analytiky a strojového učení na ochranu výnosů operátora.

## Popis

Fraud Detection System (FDS) je v kontextu 3GPP podsystém zabezpečení sítě a ochrany výnosů, který funguje uvnitř nebo ve spojení s jádrem sítě za účelem identifikace, upozornění a někdy i automatické reakce na podvodné využívání telekomunikačních služeb. Přestože je jeho detailní implementace často dodavatelsky specifická, specifikace 3GPP definují požadavky na službu, architektonické principy a rozhraní pro podávání zpráv o podvodech. FDS nepřetržitě shromažďuje záznamy o podrobnostech hovorů ([CDR](/mobilnisite/slovnik/cdr/)), signalizační data (např. z rozhraní Diameter, [MAP](/mobilnisite/slovnik/map/) nebo [HTTP](/mobilnisite/slovnik/http/)/2) a informace o profilech účastníků z různých síťových funkcí, jako je Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)), Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a entity správy relací. Tato data tvoří vstup pro analýzu podvodů.

Jádrem FDS je jeho detekční engine, který používá vícevrstvý přístup. První vrstvu tvoří detekce založená na pravidlech, kde předdefinované scénáře (např. náhlý nárůst délky mezinárodních hovorů, souběžné používání stejného [IMSI](/mobilnisite/slovnik/imsi/) v geograficky vzdálených lokalitách nebo rychlé posílání SMS na prémiová čísla) spouštějí upozornění. Druhá vrstva zahrnuje statistické profilování, kdy systém vytváří behaviorální základní profily pro jednotlivé účastníky nebo skupiny (např. typické časy hovorů, objemy dat, destinace) a označuje výrazné odchylky. Moderní implementace FDS obsahují třetí vrstvu využívající algoritmy strojového učení k detekci složitých a vyvíjejících se podvodných vzorců, které by systémy založené na pravidlech mohly přehlédnout. Když je detekován potenciální podvodný případ, FDS vygeneruje poplach na nástěnce správy podvodů (Fraud Management dashboard) s detaily o identifikátoru účastníka, typu podezřelého podvodu, úrovni důvěryhodnosti a relevantních důkazech.

Z architektonického hlediska může být FDS integrován prostřednictvím standardizovaných rozhraní. Například 3GPP TS 23.035 specifikuje technickou realizaci Fraud Information Gathering Systems ([FIGS](/mobilnisite/slovnik/figs/)), což je komponenta FDS. Systém může komunikovat se sítí za účelem provedení zmírňujících akcí. To lze provést prostřednictvím northbound rozhraní k Operations Support System (OSS) pro manuální zásah nebo přímo prostřednictvím rozhraní k síťovým řídicím funkcím. Například při detekci podvodné registrace s vysokou mírou jistoty může FDS vyslat signál HSS k dočasnému pozastavení účastníka nebo instruovat PCF k aplikaci restriktivní politiky, čímž blokuje další využívání služeb do doby prošetření případu. Tato možnost uzavřené smyčky je klíčová pro minimalizaci finančních ztrát. FDS je kritickým prvkem obrany operátora proti široké škále typů podvodů, včetně International Revenue Share Fraud (IRSF), Wangiri (one-ring) podvodů, SIM box bypass podvodů a krádeže identity.

## K čemu slouží

FDS byl vyvinut jako reakce na významné a rostoucí finanční ztráty, které operátoři mobilních sítí čelili kvůli telekomunikačním podvodům. Jak se mobilní sítě vyvíjely od jednoduchých hlasových služeb ke komplexním digitálním ekosystémům s prémiovými SMS, datovými službami a mezinárodním roamováním, příležitosti ke zneužití se množily. Rané podvody, jako je klonování SIM karet nebo podvodná registrace, mohly způsobit masivní ztráty, než byly manuálně odhaleny pomocí anomálií v účtování. Primárním účelem FDS je poskytovat proaktivní, automatizovaný dohled nad síťovou aktivitou za účelem identifikace podvodu v době jeho výskytu nebo krátce poté, čímž se omezí škody.

Historicky byla detekce podvodů manuální, dodatečnou analýzou záznamů o účtování, což znamenalo, že podvod mohl pokračovat týdny před odhalením. Formalizace požadavků na FDS ve standardech 3GPP, počínaje Release 4, poskytla rámec pro interoperabilní monitorování v reálném čase. Vyřešila omezení reaktivních přístupů definováním mechanismů pro síťové funkce, aby hlásily relevantní události pro analýzu podvodů. Tento posun byl motivován potřebou chránit nejen výnosy operátora, ale také integritu sítě a zkušenosti řádných účastníků, protože podvody často spotřebovávají nadměrné síťové prostředky.

Vývoj FDS odráží vývoj samotných podvodů. Jak byly základní podvody potírány, objevily se sofistikovanější útoky, což vyžadovalo inteligentnější detekční systémy. Specifikace 3GPP zajistily, aby jádrová síť produkovala potřebná podrobná data (např. podrobné CDR s lokalizací, specifiky využití služby) pro zásobování těchto pokročilých systémů. V éře 5G, se síťovým slicingem, edge computingem a řadou služeb IoT, se potenciální prostor pro útoky dále rozšířil. FDS nyní musí zohledňovat podvody ve využívání síťových řezů, zneužívání API a kompromitaci IoT zařízení, čímž je jeho role v bezpečnosti a ochraně výnosů důležitější než kdy dříve. Řeší základní problém převodu obrovského množství síťových signalizačních a uživatelských dat na použitelnou inteligenci k prevenci finanční kriminality.

## Klíčové vlastnosti

- Monitorování CDR a signalizačních dat v reálném čase a téměř v reálném čase
- Detekce využívající více metod (založená na pravidlech, statistické profilování, algoritmy strojového učení)
- Rozhraní k jádrovým síťovým funkcím (HSS, CDF, PCF) pro sběr dat
- Schopnost spouštět automatizované zmírňující akce (např. pozastavení účastníka)
- Generování podrobných upozornění na podvody a správa případů pro vyšetřovatele
- Podpora pro detekci různých typů podvodů (podvodná registrace, IRSF, Wangiri, SIM box)

## Související pojmy

- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 22.031** (Rel-19) — Fraud Information Gathering System (FIGS) Stage 1
- **TS 23.031** (Rel-19) — Fraud Information Gathering System (FIGS) - Stage 2
- **TS 23.035** (Rel-19) — Immediate Service Termination (IST) Stage 2
- **TS 41.031** (Rel-19) — Fraud Information Gathering System (FIGS) Requirements

---

📖 **Anglický originál a plná specifikace:** [FDS na 3GPP Explorer](https://3gpp-explorer.com/glossary/fds/)
