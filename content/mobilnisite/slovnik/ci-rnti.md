---
slug: "ci-rnti"
url: "/mobilnisite/slovnik/ci-rnti/"
type: "slovnik"
title: "CI-RNTI – Cancellation Indication Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "CI-RNTI"
fullName: "Cancellation Indication Radio Network Temporary Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ci-rnti/"
summary: "CI-RNTI je identifikátor specifický pro UE používaný v 5G NR k indikaci zrušení uplinkového přenosu. Umožňuje dynamické řízení zdrojů tím, že gNB může signalizovat UE, aby zrušila naplánované uplinkov"
---

CI-RNTI je identifikátor specifický pro UE používaný v 5G NR k signalizaci UE, aby zrušila naplánované uplinkové přenosy, což umožňuje dynamické řízení zdrojů a snižuje interference.

## Popis

Cancellation Indication Radio Network Temporary Identifier (CI-RNTI) je specializovaný typ [RNTI](/mobilnisite/slovnik/rnti/) zavedený v 5G NR pro podporu mechanismů dynamického zrušení uplinkových přenosů. Na rozdíl od konvenčních RNTI, které plánují přenosy, CI-RNTI funguje v opačném směru – poskytuje síti mechanismus k dynamickému zrušení již naplánovaných uplinkových přenosů od UE. Tento identifikátor je konfigurován pro každé UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) jako součást konfigurace Physical Uplink Shared Channel ([PUSCH](/mobilnisite/slovnik/pusch/)), konkrétně v informačním elementu PUSCH-Config, kde pole ci-RNTI nese 16bitovou hodnotu.

Pokud je nakonfigurován, CI-RNTI umožňuje gNB vysílat Downlink Control Information ([DCI](/mobilnisite/slovnik/dci/)) formátu 2_4 na Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Tento DCI formát obsahuje indikaci zrušení, která se vztahuje na specifické časově-frekvenční zdroje. UE monitoruje PDCCH pro DCI formát 2_4 zakódovaný (scrambled) s jejím přiřazeným CI-RNTI. Po úspěšném dekódování UE extrahuje indikaci zrušení, která specifikuje, které z jejích naplánovaných uplinkových přenosů mají být zrušeny. Indikace zahrnuje parametry jako počáteční symbol, délku ve symbolech a postižené frekvenční zdroje, což umožňuje přesné zrušení částí naplánovaných PUSCH nebo [PUCCH](/mobilnisite/slovnik/pucch/) přenosů.

Mechanismus zrušení funguje prostřednictvím bitmapového pole v DCI formátu 2_4, kde každý bit odpovídá specifické sadě časově-frekvenčních zdrojů. Mapování mezi bity a zdroji je konfigurováno prostřednictvím parametrů vyšší vrstvy, což poskytuje flexibilitu pro různé scénáře nasazení. Když UE obdrží platnou indikaci zrušení, musí ukončit přenos v indikovaných zdrojích, čímž je efektivně uvolní pro jiné využití. Tento proces vyžaduje přesné časové zarovnání, přičemž indikace zrušení je typicky vysílána dostatečně před postiženým uplinkovým slotem, aby UE měla čas na zpracování a přerušení přípravy přenosu.

CI-RNTI hraje klíčovou roli v pokročilých funkcích 5G, jako je dynamické Time Division Duplex ([TDD](/mobilnisite/slovnik/tdd/)) a operace s více Transmission Reception Points ([TRP](/mobilnisite/slovnik/trp/)). V dynamickém TDD může síť rychle přizpůsobit měnícím se vzorcům provozu převodem naplánovaných uplinkových zdrojů na downlinkové, když je to potřeba. Pro nasazení s více TRP pomáhá CI-RNTI řídit interferenci mezi různými TRP zrušením uplinkových přenosů, které by způsobily škodlivou interferenci souběžným downlinkovým přenosům z jiných TRP. 16bitová struktura identifikátoru odpovídá standardnímu formátu RNTI, což zajišťuje kompatibilitu se stávajícími postupy monitorování PDCCH a dekódování DCI a zároveň přidává tuto specializovanou funkci zrušení.

## K čemu slouží

CI-RNTI bylo zavedeno k řešení rostoucí potřeby dynamičtějšího a efektivnějšího řízení rádiových zdrojů v sítích 5G, zejména pro pokročilé scénáře nasazení, jako jsou dynamické TDD a operace s více TRP. Předchozí systémy LTE postrádaly standardizovaný mechanismus, kterým by síť mohla zrušit již naplánované uplinkové přenosy, což omezovalo schopnost sítě rychle se přizpůsobit měnícím se podmínkám provozu a interferenčním vzorcům. To se stalo obzvláště problematickým v 5G, kde jsou struktury subrámců flexibilnější a vzorce provozu dynamičtější.

Primární motivací pro CI-RNTI bylo umožnit efektivnější využití časově-frekvenčních zdrojů v dynamických TDD systémech. V tradičních statických nebo semi-statických TDD konfiguracích jsou vzorce uplink-downlink pevné nebo se mění pomalu, ale 5G zavedlo podporu pro dynamické TDD, kde síť může rychle přizpůsobit směr přenosu na základě okamžitých požadavků provozu. Bez mechanismu zrušení zůstávaly uplinkové zdroje, jednou naplánované pro UE, přiděleny, i když downlinkový provoz náhle vzrostl, což vedlo k neefektivnímu využití zdrojů. CI-RNTI to řeší tím, že umožňuje gNB zrušit naplánované uplinkové přenosy a tyto zdroje přerozdělit pro downlinkové využití.

Dalším klíčovým problémem, který CI-RNTI řeší, je řízení interference v nasazeních s více TRP. Ve scénářích, kde více přenosových bodů obsluhuje různá UE v překrývajících se oblastech, mohou uplinkové přenosy od jednoho UE interferovat s downlinkovými přenosy k jinému UE z jiného TRP. Předchozí systémy se spoléhaly na pečlivou koordinaci plánování, která byla často suboptimální a pomalá k přizpůsobení. CI-RNTI umožňuje rychlé zrušení uplinkových přenosů, které by způsobily škodlivou interferenci, čímž zlepšuje celkový výkon sítě a umožňuje agresivnější frekvenční reutilizaci. Tato schopnost je obzvláště cenná v hustých městských nasazeních a scénářích průmyslového IoT, kde více TRP pracuje v těsné blízkosti.

## Klíčové vlastnosti

- Umožňuje dynamické zrušení naplánovaných uplinkových přenosů PUSCH/PUCCH
- Konfigurováno pro každé UE prostřednictvím signalizace RRC v PUSCH-Config
- Používá se k zakódování (scrambling) DCI formátu 2_4 na PDCCH pro indikace zrušení
- Podporuje přesnou specifikaci časově-frekvenčních zdrojů prostřednictvím bitmapových polí
- Kritické pro provoz dynamického TDD a řízení interference v nasazeních s více TRP
- Dodržuje standardní 16bitový formát RNTI pro kompatibilitu se stávajícími postupy

## Související pojmy

- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [CI-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ci-rnti/)
