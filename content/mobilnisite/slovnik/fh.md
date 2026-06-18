---
slug: "fh"
url: "/mobilnisite/slovnik/fh/"
type: "slovnik"
title: "FH – Frequency Hopping"
date: 2025-01-01
abbr: "FH"
fullName: "Frequency Hopping"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fh/"
summary: "Technika rozprostřeného spektra, při níž se přenosový kmitočet rychle přepíná mezi mnoha kanály podle pseudonáhodné posloupnosti. Zvyšuje odolnost vůči rušení, útlumu (fading) a odposlechu, čímž zlepš"
---

FH je rozprostřené spektrum (spread-spectrum) technika, při níž se přenosový kmitočet rychle přepíná mezi mnoha kanály za účelem zvýšení odolnosti vůči rušení, útlumu (fading) a odposlechu, čímž se zlepšuje spolehlivost spoje a spektrální účinnost.

## Popis

Frequency Hopping (FH, přeskakování kmitočtů) je základní technika fyzické vrstvy v bezdrátových komunikacích, při níž se nosný kmitočet vysílaného signálu rychle mění v širokém pásmu podle předem stanovené pseudonáhodné posloupnosti známé vysílači i přijímači. Tento proces probíhá na úrovni časového slotu nebo symbolu v závislosti na implementaci systému (např. pomalé přeskakování kmitočtů v GSM mění kmitočet na [TDMA](/mobilnisite/slovnik/tdma/) rámec, zatímco rychlé přeskakování mění kmitočet vícekrát za symbol). Jádrový mechanismus zahrnuje kmitočtový syntetizér na straně vysílače, který je řízen algoritmem generujícím posloupnost přeskakování, často odvozeným od parametrů specifických pro buňku, jako je Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)) a Absolute Radio Frequency Channel Number ([ARFCN](/mobilnisite/slovnik/arfcn/)). Přijímač, synchronizovaný se stejnou posloupností, musí odpovídajícím způsobem naladit svůj lokální oscilátor, aby mohl signál demodulovat.

Z architektonického hlediska je FH integrován do základnové pásmo (baseband) a rádiové kmitočtové ([RF](/mobilnisite/slovnik/rf/)) podsystémů jak základnové stanice (např. [BTS](/mobilnisite/slovnik/bts/) v GSM, [eNB](/mobilnisite/slovnik/enb/) v LTE), tak uživatelského zařízení (UE). Mezi klíčové komponenty patří generátor posloupnosti přeskakování, kmitočtový syntetizér a jednotka časové synchronizace. Posloupnost přeskakování je navržena tak, aby byla ortogonální nebo téměř ortogonální mezi různými uživateli ve stejné buňce, a tím se minimalizovalo ko-kanálové rušení. V GSM je například tato posloupnost definována v 3GPP TS 45.002 a využívá parametry jako Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)) a Mobile Allocation Index Offset (MAIO) k přiřazení jedinečných vzorů přeskakování různým provozním kanálům.

Role FH v síti je mnohostranná. Především poskytuje kmitočtovou diverzitu, čímž bojuje proti kmitočtově selektivnímu útlumu (fading) tím, že zajišťuje, aby hluboký útlum ovlivňující jeden kmitočtový kanál nezhoršoval trvale celý přenos. Tím se zlepšuje výkonnost Bit Error Rate (BER) bez zvýšení vysílacího výkonu. Za druhé poskytuje průměrování rušení, rozkládá rušení od úzkopásmových zdrojů nebo z jiných buněk přes celé šířky pásma, což zvyšuje celkovou kapacitu systému a kvalitu služeb (QoS). Za třetí poskytuje základní úroveň bezpečnosti přenosu prostřednictvím utajení posloupnosti, protože odposlouchávající zařízení bez znalosti posloupnosti přeskakování nemohou komunikaci snadno zachytit. V LTE a novějších technologiích, ačkoli širokopásmový OFDMA inherentně poskytuje kmitočtovou diverzitu, jsou principy FH stále aplikovány v konkrétních kontextech, jako je přeskakování na Physical Uplink Shared Channel (PUSCH) v LTE, pro další optimalizaci výkonnosti.

## K čemu slouží

Frequency Hopping byl vytvořen k řešení kritických výzev v raných celulárních systémech, konkrétně rušení, vícecestného útlumu (multipath fading) a omezené spektrální účinnosti. V období před 2G používaly analogové systémy jako AMPS pevné kmitočtové přidělení, což je činilo velmi náchylnými ke ko-kanálovému rušení a hlubokým útlumům, což vedlo ke špatné kvalitě hovorů a přerušeným spojením. Motivací pro FH byly vojenské komunikace s rozprostřeným spektrem vyvinuté během druhé světové války, které prokázaly odolnost proti rušení a odposlechu. 3GPP standardizovalo FH v GSM (Release 5), aby využilo těchto výhod v komerčních sítích.

Primární problém, který FH řeší, je zmírnění kmitočtově selektivního útlumu, kdy se útlum signálu výrazně liší napříč kmitočtovým pásmem v důsledku vícecestného šíření. Přeskakováním mezi kmitočty se přenos vyhne uvíznutí ve spektrálním nulovém bodě a průměruje poruchy přenosového kanálu. Řeší také problém „blízko-daleko“ a mezibuněčné rušení v celulárních nasazeních tím, že náhodně rozloží vzorec rušení, což umožňuje těsnější vzorce opakovaného využití kmitočtů a zvýšení kapacity sítě. Bez FH by systémy vyžadovaly větší faktory opakovaného využití kmitočtů (např. 7 nebo 12) pro udržení přijatelné úrovně rušení, což by drasticky snížilo spektrální účinnost.

Historicky umožnilo FH GSM dosáhnout jeho charakteristické kvality hlasu a spolehlivosti s faktorem opakovaného využití až 3 nebo 4. Vyřešilo omezení pevného přidělování kanálů tím, že učinilo rušení statisticky rovnoměrným, což zjednodušilo plánování sítě a zlepšilo odolnost v nepředvídatelných rádiových prostředích. Zatímco novější technologie jako LTE a 5G NR využívají širokopásmové přenosy a pokročilé plánování, které inherentně poskytují kmitočtovou diverzitu, zůstávají principy FH relevantní pro konkrétní případy použití, jako jsou nasazení IoT (např. NB-IoT) a uplinkové přenosy, kde je klíčová energetická účinnost a odolnost vůči rušení.

## Klíčové vlastnosti

- Poskytuje kmitočtovou diverzitu pro potlačení vícecestného útlumu (multipath fading)
- Průměruje a randomizuje ko-kanálové a sousední kanálové rušení
- Umožňuje těsnější opakované využití kmitočtů, čímž zvyšuje kapacitu sítě
- Poskytuje základní bezpečnost přenosu prostřednictvím utajení pseudonáhodné posloupnosti
- Implementováno jako pomalé přeskakování (na rámec) nebo rychlé přeskakování (na symbol)
- Ortogonální posloupnosti přeskakování minimalizují rušení uvnitř buňky

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 26.975** (Rel-19) — AMR Speech Codec Performance Background
- **TR 26.978** (Rel-19) — AMR Noise Suppression Selection Phase Technical Report
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [FH na 3GPP Explorer](https://3gpp-explorer.com/glossary/fh/)
