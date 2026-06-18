---
slug: "gdr"
url: "/mobilnisite/slovnik/gdr/"
type: "slovnik"
title: "GDR – Gradual Decoding Refresh"
date: 2025-01-01
abbr: "GDR"
fullName: "Gradual Decoding Refresh"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gdr/"
summary: "Gradual Decoding Refresh (GDR) je technika kódování videa používaná v kodeku Enhanced Voice Services (EVS) a video kodecích 3GPP, která umožňuje plynulé přepínání mezi různými mediálními proudy nebo o"
---

GDR je technika kódování videa používaná v kodecích 3GPP, která umožňuje dekodéru postupně obnovit svůj obrazový buffer pomocí speciálních snímků, což umožňuje plynulé přepínání datových proudů nebo obnovu ze ztráty paketů bez nutnosti úplného klíčového snímku.

## Popis

Gradual Decoding Refresh (GDR) je mechanismus implementovaný ve video a hlasových kodecích pro postupné, nikoli okamžité, obnovení stavu dekodéru. V tradičním prediktivním kódování videa (např. H.264/[AVC](/mobilnisite/slovnik/avc/), H.265/[HEVC](/mobilnisite/slovnik/hevc/)) se dekodér spoléhá na referenční snímky uložené v Decoded Picture Buffer ([DPB](/mobilnisite/slovnik/dpb/)). Pokud jsou pakety ztraceny nebo pokud se nový divák připojí k proudu (bodem "náhodného přístupu"), mohou se referenční buffery dekodéru poškodit nebo přestat odpovídat stavu kodéru, což vede k přetrvávajícím obrazovým artefaktům. Typickou metodou obnovy je snímek Instantaneous Decoding Refresh ([IDR](/mobilnisite/slovnik/idr/)), což je velký intra-kódovaný snímek, který kompletně resetuje stav dekodéru, avšak za cenu vysokého datového toku a potenciální latence.

GDR funguje tak, že zakóduje sekvenci snímků specifickým způsobem, který umožňuje dekodéru postupně vytvořit čistý referenční snímek. Namísto jediného velkého IDR snímku rozprostře kodér informaci pro obnovu napříč několika po sobě jdoucími snímky. Jedna běžná technika zahrnuje rozdělení snímku na řezy nebo oblasti a zakódování každé oblasti jako intra-kódovaného bloku (I-bloku) v průběhu několika snímků cyklickým způsobem. Například během cyklu N snímků může každý snímek obnovit 1/N celkové obrazové plochy intra kódováním, zatímco zbytek obrazu je kódován prediktivně (pomocí P nebo B snímků). Jak dekodér tyto snímky přijímá, postupně nahrazuje poškozené nebo staré části svého referenčního snímku novými intra-kódovanými bloky. Po přijetí kompletního cyklu N snímků je referenční snímek dekodéru plně obnoven intra-kódovanými daty, čímž dosáhne stavu ekvivalentního dekódování IDR snímku, ale bez velké okamžité špičky datového toku.

V rámci 3GPP je GDR specifikováno pro video služby a je klíčovou vlastností kodeku Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)), jak je dokumentováno v TS 26.906 (EVS Codec) a TS 26.926 (EVS Codec test sequences). Pro EVS, který zpracovává super-wideband a full-band řeč, jsou GDR podobné mechanismy aplikovány na parametrické domény hlasového kodeku, aby umožnily plynulé obnovení ze ztráty paketů a hladké přepínání mezi různými provozními režimy (např. mezi detekcí hlasové aktivity ([VAD](/mobilnisite/slovnik/vad/)) a nepřetržitým přenosem). Kodek může postupně aktualizovat svůj vnitřní stav (např. koeficienty [LPC](/mobilnisite/slovnik/lpc/) filtru) namísto vynucení náhlého resetu, což zachovává vyšší percepční kvalitu řeči při narušení sítě nebo při předávání hovoru. U video služeb GDR umožňuje efektivnější adaptivní streamování s proměnným datovým tokem a zlepšenou odolnost proti chybám v mobilním prostředí, kde jsou ztráty paketů a zpoždění běžné, což přímo přispívá k lepší uživatelské kvalitě zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

## K čemu slouží

GDR bylo vyvinuto k řešení základního kompromisu mezi efektivitou náhodného přístupu/obnovy z chyb a efektivitou kódování v prediktivním kódování médií. Klasické řešení, IDR snímek, poskytuje bod čistého resetu dekodéru, ale je extrémně neefektivní z hlediska datového toku. Ve scénářích nízkolatenční komunikace v reálném čase (RTC), jako jsou mobilní videohovory nebo voice-over-LTE (VoLTE), by časté odesílání velkých IDR snímků pro potlačení ztráty paketů spotřebovalo nadměrnou šířku pásma a způsobilo znatelné poklesy kvality nebo latenci. Naopak, neodesílání IDR snímků dostatečně často vede k dlouhotrvajícímu poškození obrazu nebo desynchronizaci mezi kodérem a dekodérem po ztrátě paketů. GDR poskytuje střední cestu, která umožňuje dekodéru se postupně zotavit bez velké okamžité penalizace datového toku.

Historický kontext vychází z vývoje komprese videa pro streamování a vysílání, kde jsou doby přepínání kanálů a odolnost proti chybám kritické. Starší standardy jako MPEG-2 používaly periodické intra-snímky (I-snímky), které jsou podobné IDR snímkům. Mechanismy GDR byly zdokonaleny v pozdějších kodecích jako H.264 a získaly na významu s nástupem internetového a bezdrátového přenosu videa, kde je šířka pásma proměnlivá a ztráty časté. Pro 3GPP bylo přijetí GDR ve specifikacích, jako jsou ty pro EVS, motivováno potřebou robustních, vysoce kvalitních hlasových a video služeb přes sítě LTE a 5G NR. Tyto sítě, ačkoli vysokokapacitní, stále zažívají variace rádiového spojení, předávání hovorů a dočasné přetížení.

Konkrétně pro kodek EVS představený v 3GPP Release 12 řeší techniky GDR výzvu přepínání režimů a obnovy ze ztráty paketů způsobem šetrným k šířce pásma. EVS podporuje širokou škálu datových toků a provozních režimů (např. řeč, hudba, smíšený obsah). Přepínání mezi těmito režimy nebo obnova ze série ztracených paketů vyžaduje resynchronizaci vnitřního stavu dekodéru. Úplný reset by způsobil slyšitelné zkreslení. GDR umožňuje, aby k této synchronizaci došlo plynule během několika snímků, a zachovává tak přirozenost hlasu. GDR tedy řeší problém udržení kontinuálního, vysoce kvalitního přenosu médií v dynamických a potenciálně ztrátových podmínkách mobilních sítí, což umožňuje službám jako VoLTE a ViLTE splňovat uživatelská očekávání ohledně srozumitelnosti a spolehlivosti.

## Klíčové vlastnosti

- Umožňuje obnovení stavu dekodéru bez úplného snímku okamžité obnovy dekódování (IDR)
- Rozprostírá intra-kódovanou informaci napříč více po sobě jdoucími video snímky nebo hlasovými pakety
- Snižuje požadavky na špičkový datový tok ve srovnání s periodickými IDR snímky, čímž zlepšuje efektivitu využití šířky pásma
- Poskytuje plynulý náhodný přístup a obnovu z chyb, minimalizuje obrazové nebo sluchové artefakty
- Integrální součást kodeku 3GPP Enhanced Voice Services (EVS) pro robustní přenos řeči
- Zvyšuje odolnost proti chybám a uživatelskou kvalitu zážitku (QoE) v náchylných mobilních sítích

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G

---

📖 **Anglický originál a plná specifikace:** [GDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/gdr/)
