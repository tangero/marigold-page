---
slug: "peips"
url: "/mobilnisite/slovnik/peips/"
type: "slovnik"
title: "PEIPS – Paging Early Indication with Paging Subgrouping"
date: 2025-01-01
abbr: "PEIPS"
fullName: "Paging Early Indication with Paging Subgrouping"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/peips/"
summary: "Mechanismus pro snížení spotřeby energie UE během režimu idle/inactive odesláním signálu předčasné indikace volání (PEI). Umožňuje UE dekódovat zprávy volání pouze pro jejich přiřazenou podskupinu, co"
---

PEIPS je mechanismus pro úsporu energie podle 3GPP, kde signál předčasné indikace volání umožňuje UE v režimu idle/inactive dekódovat volání pouze pro přiřazenou podskupinu, čímž se snižuje spotřeba energie.

## Popis

PEIPS je funkce pro úsporu energie zavedená ve specifikaci 3GPP Release 17 pro 5G New Radio (NR). Funguje tak, že rozděluje UE v okamžiku volání do více podskupin. Před odesláním úplné zprávy volání vysílá síť signál Předčasné indikace volání ([PEI](/mobilnisite/slovnik/pei/)) v určeném okamžiku PEI. Tento PEI je kompaktní signál s nízkou složitostí, který indikuje, zda v následujícím okamžiku volání bude následovat zpráva volání pro konkrétní podskupinu. UE, nakonfigurovaná s konkrétním identifikátorem podskupiny, musí pouze sledovat PEI pro svou podskupinu. Pokud PEI indikuje 'volání přítomno' pro její podskupinu, UE poté probudí svůj hlavní přijímač, aby dekódovala úplné [DCI](/mobilnisite/slovnik/dci/) pro volání a zprávu volání na kanálu [PDSCH](/mobilnisite/slovnik/pdsch/). Pokud PEI indikuje 'žádné volání' pro její podskupinu, může UE okamžitě přejít zpět do hlubokého spánku a vynechat energeticky náročnější dekódování celého kanálu volání. Architektura zahrnuje koordinaci mezi funkcí [AMF](/mobilnisite/slovnik/amf/) v jádru sítě, která volání iniciuje, a gNB v RAN, které plánuje a vysílá PEI a zprávy volání. Přiřazení podskupiny je typicky odvozeno od [5G-S-TMSI](/mobilnisite/slovnik/5g-s-tmsi/) UE, což zajišťuje deterministické mapování. Tento mechanismus je klíčový pro správu zatížení voláním a je specifikován napříč protokoly RAN a jádra sítě, včetně [NGAP](/mobilnisite/slovnik/ngap/) (38.413), XnAP (38.423), [F1AP](/mobilnisite/slovnik/f1ap/) (38.473) a [NAS](/mobilnisite/slovnik/nas/) protokolu (24.501).

## K čemu slouží

PEIPS byl vytvořen, aby řešil kritickou výzvu spotřeby energie uživatelského zařízení (UE), zejména pro zařízení hromadné komunikace strojového typu (mMTC) a 'vždy zapnuté' mobilní telefony. V předchozích verzích 5G muselo UE ve stavu RRC_IDLE nebo RRC_INACTIVE periodicky probouzet, aby monitorovalo úplné okamžiky volání, což zahrnuje dekódování PDCCH pro DCI formát 1_0 skramblovaný s P-RNTI. Tento proces spotřebovává značnou energii baterie, i když pro dané UE není určena žádná zpráva volání. Problém se zhoršuje s růstem IoT, kde zařízení mohou potřebovat fungovat roky na jedno nabití baterie. PEIPS to řeší zavedením dvoustupňového filtrovacího procesu. Lehký PEI signál funguje jako 'signál k probuzení' pouze pro podmnožinu UE. To dramaticky snižuje počet případů, kdy se UE musí plně aktivovat své vysokoenergetické rádiové komponenty. Motivace vychází z průmyslového tlaku na extrémní energetickou účinnost v 5G-Advanced a dalších technologiích, což umožňuje nové případy užití pro nízkopříkonové senzory a nositelná zařízení a zároveň zlepšuje výdrž baterie smartphonů. Přímo řeší klíčové omezení staršího postupu volání, kde se energie plýtvala na dekódování nepodstatných informací o volání.

## Klíčové vlastnosti

- Filtrování volání na základě podskupin, které snižuje monitorovací aktivitu UE
- Vysílání signálu Předčasné indikace volání (PEI) s nízkou složitostí
- Deterministické přiřazení UE do podskupin na základě 5G-S-TMSI
- Podpora více sad a konfigurací zdrojů PEI prostřednictvím RRC
- Snižuje spotřebu energie UE ve stavech RRC_IDLE a RRC_INACTIVE
- Zpětně kompatibilní provoz s UE, která PEIPS nepodporují

## Související pojmy

- [WUS – Wake Up Signal](/mobilnisite/slovnik/wus/)
- [PEI – Permanent Equipment Identifier](/mobilnisite/slovnik/pei/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [PEIPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/peips/)
