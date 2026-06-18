---
slug: "mrru"
url: "/mobilnisite/slovnik/mrru/"
type: "slovnik"
title: "MRRU – Maximum Reconstructed Reception Unit"
date: 2025-01-01
abbr: "MRRU"
fullName: "Maximum Reconstructed Reception Unit"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mrru/"
summary: "Maximum Reconstructed Reception Unit (MRRU) je parametr ve specifikacích 3GPP GPRS, který definuje největší povolenou velikost znovusložené datové jednotky protokolu (PDU) vyšší vrstvy po dekompresi h"
---

MRRU je maximální povolená velikost znovusložené datové jednotky vyšší vrstvy po dekompresi. Slouží jako klíčové omezení pro RLC vrstvu při správě segmentace a znovuskládání paketů v 3GPP GPRS.

## Popis

Maximum Reconstructed Reception Unit (MRRU) je parametr definovaný v technické specifikaci 3GPP TS 44.065 pro vrstvu řízení rádiového spoje ([RLC](/mobilnisite/slovnik/rlc/)) v sítích [GPRS](/mobilnisite/slovnik/gprs/) a [EDGE](/mobilnisite/slovnik/edge/). Působí v kontextu podsoubory protokolu konvergence paketových dat ([PDCP](/mobilnisite/slovnik/pdcp/)), konkrétně pro kompresi hlaviček a dat. MRRU nedefinuje fyzickou jednotku, ale logický limit. Udává maximální povolenou velikost v oktetech pro rekonstruovanou datovou jednotku protokolu ([PDU](/mobilnisite/slovnik/pdu/)) vyšší vrstvy poté, co přijímací entita provedla dekompresní operace na hlavičkové i datové části přenášených bloků.

Role MRRU je klíčová v procesu segmentace a znovuskládání. Když je PDU vyšší vrstvy (např. IP paket) předán RLC vrstvě k přenosu, může být větší než maximální velikost povolená pro jeden RLC datový blok přes rádiové rozhraní. RLC vrstva tento velký PDU segmentuje na menší RLC datové bloky. Pokud je aktivní komprese, tyto bloky obsahují komprimované hlavičky a případně komprimovaná datová pole. Po přijetí protistojná RLC entita tyto bloky znovu složí a předá je dekompresní entitě. Dekompresní entita vydá rekonstruovaný PDU. MRRU je dohodnutý limit mezi vysílací a přijímací stranou pro velikost tohoto výsledného, rekonstruovaného PDU. Zajišťuje, že přijímač má dostatečné vyrovnávací paměti (buffer) pro zpracování největšího možného PDU po dekompresi, který může být výrazně větší než komprimované bloky přijaté přes rozhraní.

Z architektonického hlediska se MRRU vyjednává během vytváření kontextu paketového datového protokolu ([PDP](/mobilnisite/slovnik/pdp/)) nebo rádiového přenosového kanálu jako součást parametrů protokolu vrstvy 2. Komunikuje se mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a podpůrným uzlem GPRS ([SGSN](/mobilnisite/slovnik/sgsn/)). Hodnota se volí na základě schopností MS a konfigurace sítě, což vyvažuje efektivitu odesílání velkých paketů (minimalizace režie segmentace) s paměťovými a výpočetními omezeními zařízení. MRRU funguje ve spojení s dalšími parametry, jako je Maximum Receive Unit (MRU) pro vrstvu řízení logického spoje (LLC) a maximální velikost RLC bloku.

Během provozu, pokud dekompresní proces vyústí v PDU překračující MRRU, je to považováno za chybový stav, který typicky vede k zahození PDU. Vysílací strana proto musí zajistit, že jakýkoli PDU, který předá k přenosu, po zohlednění potenciální expanze během komprese (některé kompresní algoritmy mají malý expanzní faktor), nepřekročí na přijímači dohodnuté MRRU. Tento parametr je klíčovým prvkem pro řízení efektivity rádiových zdrojů a zajištění spolehlivého přenosu dat, zejména pro služby používající robustní kompresi hlaviček (ROHC) nebo jiné kompresní techniky šetřící šířku pásma, které však vyžadují pečlivé řízení velikosti vyrovnávacích pamětí přijímače.

## K čemu slouží

MRRU bylo zavedeno, aby vyřešilo specifickou technickou výzvu v sítích GPRS/EDGE související s interakcí mezi kompresí a segmentací. Kompresní algoritmy, zejména komprese hlaviček, se používají ke snížení režie protokolových hlaviček (jako TCP/IP) přes rádiové spoje s omezenou šířkou pásma. Komprese však nevede vždy k deterministickému zmenšení velikosti; v některých případech nebo v určitých stavech kompresního algoritmu mohou být dekomprimovaná data větší než přijatá komprimovaná data. Bez definovaného maxima pro rekonstruovanou entitu by byl přijímač nucen alokovat nadměrně velké nebo neomezené vyrovnávací paměti, což by vedlo k vyčerpání paměti a nestabilitě zařízení.

Před formální definicí bylo zacházení s velkými pakety po znovusložení a dekompresi méně řízené. MRRU poskytuje jasnou, dohodnutou smlouvu mezi sítí a mobilním zařízením. Řeší problém správy zdrojů na přijímači stanovením známé horní meze. To umožňuje výrobcům zařízení navrhovat jejich RLC a dekompresní vyrovnávací paměti se známou velikostí pro nejhorší případ, což zlepšuje spolehlivost a předvídatelnost výkonu.

Vznik MRRU byl motivován potřebou podporovat efektivní přístup k internetu přes GPRS, kde jsou běžné IP pakety proměnné a potenciálně velké velikosti. Umožňuje efektivní využití komprese k úspoře rádiových zdrojů a zároveň chrání přijímač před přetečením vyrovnávací paměti v důsledku útoků nebo prostě před poškozenými pakety, které se dekomprimují na obrovskou velikost. Je základní součástí správy QoS a rádiových přenosových kanálů, která zajišťuje, že datové toky s různými charakteristikami (např. prohlížení webu vs. e-mail) mohou být omezenými zdroji zařízení zpracovány odpovídajícím způsobem.

## Klíčové vlastnosti

- Definuje maximální povolenou velikost znovusloženého PDU po úplné dekompresi na přijímači.
- Vyjednává se mezi mobilní stanicí a sítí během aktivace PDP kontextu.
- Zabraňuje přetečení vyrovnávací paměti přijímače tím, že poskytuje známou horní mez pro alokaci paměti.
- Funguje ve spojení s funkcemi segmentace a znovuskládání na RLC vrstvě.
- Zásadní pro bezpečný provoz algoritmů komprese hlaviček a dat.
- Zajišťuje spolehlivý přenos dat definováním jasného chybového stavu pro rekonstruované PDU překračující povolenou velikost.

## Definující specifikace

- **TS 44.065** (Rel-19) — GPRS SNDCP Specification

---

📖 **Anglický originál a plná specifikace:** [MRRU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mrru/)
