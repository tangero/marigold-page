---
slug: "sabs"
url: "/mobilnisite/slovnik/sabs/"
type: "slovnik"
title: "SABS – Service Area Broadcast Service"
date: 2025-01-01
abbr: "SABS"
fullName: "Service Area Broadcast Service"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sabs/"
summary: "SABS je služba 3GPP, která využívá protokol SABP k doručování vysílacích zpráv, jako jsou veřejná varování nebo komerční informace, všem UE v definované servisní oblasti. Představuje funkční servisní"
---

SABS je funkční servisní vrstva 3GPP, která využívá protokol SABP k vysílání zpráv, jako jsou veřejná varování, všem uživatelským zařízením v definované geografické oblasti v sítích UMTS a LTE.

## Popis

Service Area Broadcast Service (SABS) je nadřazená servisní schopnost v systémech 3GPP, která umožňuje vysílání informací všem uživatelským zařízením (UE) nacházejícím se v konkrétní geografické oblasti, známé jako Servisní oblast. Je to servisní realizace, která využívá podpůrný Service Area Broadcast Protocol ([SABP](/mobilnisite/slovnik/sabp/)) pro řízení a správu. SABS je primárně spojována se službou Cell Broadcast Service ([CBS](/mobilnisite/slovnik/cbs/)), ale formalizuje koncept doručování založeného na servisní oblasti jako síťovou funkci. Služba zahrnuje síťové entity, jako je Cell Broadcast Centre ([CBC](/mobilnisite/slovnik/cbc/)), Core Network a Radio Access Network (RAN), které spolupracují na efektivním rozesílání zpráv.

Architektonicky SABS funguje napříč rozhraním Iu-BC v UMTS a rozhraním S1-mb v LTE (ačkoli se protokol v LTE vyvíjí na SBcP). CBC jako iniciátor služby definuje obsah vysílané zprávy a cílovou Servisní oblast, což je typicky soubor buněk, lokalizačních oblastí ([LA](/mobilnisite/slovnik/la/)) nebo směrovacích oblastí ([RA](/mobilnisite/slovnik/ra/)). Tato definice Servisní oblasti je klíčovou součástí, která umožňuje flexibilní geografické cílení, od jedné buňky přes celou síť až po konkrétní region, jako je město. RAN ([RNC](/mobilnisite/slovnik/rnc/) v UMTS, [eNB](/mobilnisite/slovnik/enb/) v LTE) přijímá vysílací instrukce prostřednictvím SABP/SBcP a je zodpovědné za vlastní rádiový přenos zprávy na vysílacích kanálech, což zajišťuje, že ji mohou přijmout všechna UE v oblasti bez individuálního pagingu.

Jak SABS funguje, zahrnuje koordinovaný postup. CBC zahájí požadavek na vysílání s uvedením parametrů, jako je identifikátor zprávy, obsah, plán opakování a Servisní oblast. Tento požadavek je přenášen pomocí SABP k příslušným RNC. Každé RNC pak namapuje logickou Servisní oblast na fyzické buňky pod svou kontrolou a začne vysílat zprávu na určených společných kanálech. UE tato vysílací kanály nepřetržitě monitorují a mohou zprávy filtrovat a zobrazovat na základě identifikátorů a uživatelských nastavení. SABS podporuje jak nouzové služby (např. Earthquake and Tsunami Warning System - ETWS, Commercial Mobile Alert System - [CMAS](/mobilnisite/slovnik/cmas/)), tak komerční služby, čímž poskytuje univerzální platformu pro komunikaci typu jeden-všem. Služba zahrnuje mechanismy pro stanovení priority zpráv, vytěsnění vysílání s nižší prioritou a zajištění spolehlivého doručení prostřednictvím potvrzení a hlášení stavu na úrovni protokolu.

## K čemu slouží

SABS byl vyvinut, aby poskytl standardizovanou, síťově efektivní metodu pro doručování vysílacích zpráv do definovaných geografických oblastí, která splňuje jak regulační požadavky na systémy veřejného varování, tak komerční potřeby služeb poskytujících informace založené na poloze. Řešil neefektivitu používání SMS typu point-to-point pro hromadná oznámení, která by mohla přetížit signalizaci sítě. Vytvořením vyhrazené vysílací servisní vrstvy umožnilo 3GPP současné doručení potenciálně milionům zařízení bez režie jednotlivých transakcí.

Vznik SABS byl motivován vývojem od základního vysílání v buňkách v GSM ke složitějším službám založeným na oblasti v 3G/4G. Vyřešil problém geograficky cíleného vysílání, což operátorům umožnilo odesílat varování relevantní pouze pro konkrétní regiony (např. varování před povodněmi). To byl významný pokrok oproti vysílání pouze v celostátním měřítku. SABS jako servisní koncept zajistil, že vysílací schopnosti byly nedílnou, spravovanou součástí síťové architektury, podporující kritické aplikace pro ochranu života a umožňující nové služby generující příjmy, jako je reklama založená na poloze nebo dopravní aktualizace.

## Klíčové vlastnosti

- Doručuje vysílací zprávy všem UE v konfigurovatelné geografické Servisní oblasti
- Podporuje jak nouzová varování (ETWS, CMAS), tak komerční informační služby
- Využívá definice Servisní oblasti založené na buňkách, lokalizačních oblastech (LA) nebo směrovacích oblastech (RA)
- Umožňuje stanovení priority zpráv a vytěsnění pro kritická varování
- Poskytuje spolehlivou správu služeb prostřednictvím podpůrných protokolů (SABP/SBcP)
- Umožňuje CBC plánování, opakování a zrušení zpráv

## Definující specifikace

- **TS 25.414** (Rel-19) — UTRAN Iu Interface User Plane Transport Protocols

---

📖 **Anglický originál a plná specifikace:** [SABS na 3GPP Explorer](https://3gpp-explorer.com/glossary/sabs/)
