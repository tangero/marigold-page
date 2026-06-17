---
slug: "ack"
url: "/mobilnisite/slovnik/ack/"
type: "slovnik"
title: "ACK – Acknowledgement"
date: 2025-01-01
abbr: "ACK"
fullName: "Acknowledgement"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ack/"
summary: "ACK je signál kladného potvrzení používaný v protokolech hybridního automatického opakování (HARQ) k potvrzení úspěšného příjmu datového paketu. Umožňuje spolehlivý přenos dat přes bezdrátové kanály t"
---

ACK je signál kladného potvrzení používaný v protokolech hybridního automatického opakování (HARQ) k potvrzení úspěšného příjmu datového paketu.

## Popis

ACK (Acknowledgement) je základní řídicí signál v rámci systému hybridního automatického opakování (HARQ) 3GPP, který funguje především na fyzické vrstvě. V kontextu downlinkového přenosu, když uživatelské zařízení (UE) úspěšně dekóduje přenosový blok (TB) přijatý přes fyzický downlinkový sdílený kanál (PDSCH), vyšle ACK na fyzický uplinkový řídicí kanál (PUCCH) nebo, v některých konfiguracích, na fyzický uplinkový sdílený kanál (PUSCH). Tento signál informuje gNB (v 5G) nebo eNB (v LTE), že data byla přijata správně, což umožňuje vysílači pokračovat v odesílání dalšího naplánovaného datového paketu. Časový vztah mezi příjmem PDSCH a odpovídajícím přenosem ACK/NACK je striktně definován časováním HARQ, které se liší v závislosti na numerologii a duplexním režimu (FDD nebo TDD).

Generování ACK zahrnuje více vrstev. Na vrstvě řízení přístupu k médiu (MAC) úspěšná verifikace kontrolního součtu cyklickou redundancí (CRC) dekódovaného TB spustí generování kladného potvrzení. Tato indikace z MAC vrstvy je poté předána fyzické vrstvě, která ji naformátuje pro přenos. Ve scénářích zahrnujících více kódových slov (např. při použití MIMO) může být generováno více ACK bitů, které jsou následně svázány nebo multiplexovány. Fyzická vrstva mapuje tyto ACK bity na konkrétní zdrojové prvky v rámci formátu PUCCH (např. Formát 1, 2, 3 nebo 4 v LTE; různé formáty v NR) nebo je vkládá do dat sdíleného uplinkového kanálu. Zvolený formát závisí na faktorech, jako je počet současných ACK/NACK bitů, současné hlášení CSI a na tom, zda je nakonfigurován současný přenos PUCCH a PUSCH.

Role ACK přesahuje rámec prostého potvrzení; je nedílnou součástí principu zastav a čekej procesů HARQ. Každý proces HARQ udržuje vyrovnávací paměť a stav. Po přijetí ACK může proces vyprázdnit svou vyrovnávací paměť pro daný konkrétní TB a zpřístupnit proces pro nová data. Síť plánuje přenosy na základě zpětné vazby ACK/NACK, což přímo ovlivňuje propustnost a latenci. V pokročilých implementacích, jako je LTE-Advanced a 5G NR, byly zavedeny funkce jako prostorové svazování (pro více komponentních nosných při agregaci nosných) a vylepšená zpětná vazba s více bity (pro podporu zvýšeného počtu TB nebo kódových bloků). Spolehlivost samotného signálu ACK je prvořadá, protože ztracený nebo chybně interpretovaný ACK může vést k zbytečným retransmisím nebo ztrátě paketů a degradovat výkon systému. Proto je fyzický kanál přenášející ACK navržen s dostatečnou robustností, často s využitím technik jako výběr sekvence nebo kódování zdrojů.

V širší systémové architektuře je zpětná vazba ACK klíčovou součástí smyčky přizpůsobení spojení. Zatímco hlášení indikátoru kvality kanálu (CQI) poskytují dlouhodobé informace o stavu kanálu, vzorec ACK a NACK poskytuje bezprostřední zpětnou vazbu o úspěšnosti zvoleného schématu modulace a kódování (MCS). Trvalý proud NACK může vést plánovač k výběru robustnějšího MCS. Navíc ve scénářích víceuživatelského MIMO (MU-MIMO) je přesná zpětná vazba ACK/NACK kritická pro správu interference mezi vrstvami určenými pro různé uživatele. Efektivní návrh signalizace ACK, včetně její režie, latence a spolehlivosti, je proto klíčovým aspektem návrhu rozhraní vzduchu všech systémů 3GPP od LTE dále.

## K čemu slouží

Primárním účelem signálu ACK je umožnit spolehlivý přenos dat přes inherentně nespolehlivé a časově proměnné bezdrátové rádiové kanály. Před širokým přijetím HARQ se zpětnou vazbou ACK/NACK v systémech 3GPP (plně realizováno v LTE) se řízení chyb více spoléhalo na kódování pro opravu chyb (FEC) a protokoly ARQ na vyšších vrstvách, jako je potvrzovaný režim řízení rádiového spoje (RLC). Ačkoli byly účinné, tyto přístupy měly omezení: samotné FEC vyžaduje v podmínkách špatného kanálu nadměrnou redundanci, což plýtvá šířkou pásma, zatímco RLC ARQ zavádí významnou latenci kvůli své činnosti na vyšší protokolové vrstvě s delšími časy obratu.

HARQ se svým mechanismem ACK/NACK na fyzické/MAC vrstvě byl zaveden, aby tyto problémy vyřešil. Poskytuje rychlou zpětnou vazbu na bázi přenosového časového intervalu (TTI), což umožňuje mnohem rychlejší retransmise (řádově milisekundy). Toto těsné propojení FEC (prostřednictvím turbokódů nebo LDPC kódů) a ARQ (prostřednictvím smyčky ACK/NACK) vytváří výkonný adaptivní systém. ACK konkrétně informuje vysílač o úspěchu, což mu umožňuje zastavit opakované vysílání daného paketu a efektivně využívat rádiové zdroje pro nová data nebo jiné uživatele. To přímo zvyšuje spektrální účinnost a uživatelskou propustnost a zároveň snižuje latenci pro paketové datové služby, což byl klíčový požadavek projektu 3GPP Long Term Evolution (LTE) zaměřeného na výkonnou, plně IP paketovou síť.

Mechanismus ACK navíc umožňuje pokročilejší funkce. Je základní zpětnou vazbou, která činí efektivním HARQ s přírůstkovou redundancí (IR) – kde retransmise posílají různě zakódované bity. Znalost, že předchozí přenos nebyl potvrzen (implicitně prostřednictvím NACK nebo absence zpětné vazby), umožňuje přijímači kombinovat měkké bity z více pokusů o přenos, což výrazně zlepšuje úspěšnost dekódování v kanálech s útlumy. ACK tedy není pouhým potvrzovacím signálem, ale klíčovým prvkem umožňujícím sofistikované, adaptivní a efektivní protokoly na úrovni spojení, které definují moderní systémy buněčných dat.

## Klíčové vlastnosti

- Signál kladné zpětné vazby v rámci protokolu HARQ potvrzující úspěšné dekódování paketu
- Přenášený na uplinkových řídicích kanálech (PUCCH) nebo sdílených kanálech (PUSCH) se striktním časovým zarovnáním
- Umožňuje efektivní fungování HARQ podle principu zastav a čekej, čímž uvolňuje vyrovnávací paměti vysílače pro nová data
- Nedílná součást smyčky přizpůsobení spojení, ovlivňuje budoucí výběr MCS
- Podporuje svazování a multiplexování pro scénáře s více kódovými slovy MIMO a agregací nosných
- Fyzický přenos navržený pro vysokou spolehlivost, aby se zabránilo šíření chyb zpětné vazby

## Definující specifikace

- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.116** (Rel-19) — E-UTRA Relay RF Requirements
- **TS 36.117** (Rel-19) — E-UTRA Relay RF Test Methods & Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements

---

📖 **Anglický originál a plná specifikace:** [ACK na 3GPP Explorer](https://3gpp-explorer.com/glossary/ack/)
