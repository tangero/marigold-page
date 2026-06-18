---
slug: "ppch"
url: "/mobilnisite/slovnik/ppch/"
type: "slovnik"
title: "PPCH – Packet Paging Channel"
date: 2025-01-01
abbr: "PPCH"
fullName: "Packet Paging Channel"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ppch/"
summary: "PPCH (Packet Paging Channel) je přenosový kanál v downlinku v sítích GPRS a UMTS používaný pro paging mobilních zařízení při příchozích paketově přepínaných datech. Upozorňuje uživatelská zařízení (UE"
---

PPCH je přenosový kanál v downlinku v sítích GPRS a UMTS používaný pro paging mobilních zařízení při příchozích paketově přepínaných datech, který upozorňuje nečinná uživatelská zařízení (UE) a umožňuje tak efektivní úsporu energie.

## Popis

Packet Paging Channel (PPCH) je klíčový přenosový kanál v downlinku definovaný v systémech 2.5G [GPRS](/mobilnisite/slovnik/gprs/) a 3G UMTS pro paketově přepínané služby. Funguje v rámci rádiové přístupové sítě a slouží k upozornění uživatelského zařízení (UE) na příchozí datové relace nebo signalizační zprávy, když je UE v paketovém nečinném režimu nebo podobných stavech s nízkou aktivitou. Kanál je vysílán z základnové stanice ([BTS](/mobilnisite/slovnik/bts/) v GSM/GPRS, Node B v UMTS) do všech UE v buňce nebo pagingové oblasti, přičemž využívá specifické rádiové prostředky vyhrazené pro paging.

Jeho funkce spočívá v tom, že paketová řídicí jednotka sítě určí, že data je třeba doručit k UE, jehož přesná poloha v buňce nemusí být známa. Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v jádru sítě odešle pagingový požadavek příslušnému Radio Network Controlleru ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo Base Station Controlleru ([BSC](/mobilnisite/slovnik/bsc/)) v GPRS, který následně naplánuje pagingovou zprávu na PPCH. Tato zpráva obsahuje identifikátory, jako je Packet-Temporary Mobile Subscriber Identity ([P-TMSI](/mobilnisite/slovnik/p-tmsi/)) nebo International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)), pro adresování konkrétního UE. Uživatelské zařízení, které se periodicky probouzí, aby monitorovalo předdefinované pagingové bloky nebo rámce podle své přiřazené pagingové skupiny, dekóduje PPCH. Pokud rozpozná svůj identifikátor, iniciuje žádost o kanál, aby navázalo dočasný blokový tok (v GPRS) nebo připojení řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) (v UMTS) pro příjem dat.

Klíčové komponenty zahrnují strukturu pagingové zprávy, algoritmus pagingové skupiny (který určuje, kdy UE naslouchá na základě parametrů odvozených od IMSI) a přidružené řídicí kanály, jako je Packet Associated Control Channel (PACCH) pro následnou signalizaci. V architektuře je PPCH mapován na fyzické kanály, jako je Packet Data Channel (PDCH) v GPRS (který využívá časové sloty), nebo Secondary Common Control Physical Channel (S-CCPCH) v UMTS. Kanál využívá cykly nespojitého příjmu (DRX), což umožňuje uživatelským zařízením vypínat přijímače mezi pagingovými okamžiky a významně tak šetřit životnost baterie.

Jeho úlohou je propojit paketovou doménu jádra sítě s rádiovou přístupovou sítí a umožnit tak efektivní správu mobility pro paketové služby. Tím, že upozorňuje UE pouze v případě potřeby, minimalizuje využití rádiových prostředků pro zařízení, která aktivně nekomunikují, a snižuje signalizační zatížení. PPCH zajišťuje, že uživatelská zařízení zůstanou dosažitelná pro příchozí IP datové relace bez nutnosti udržovat trvalé rádiové připojení, což je zásadní pro vždy připojené paketové služby, jako je push e-mail nebo instant messaging v sítích před 4G.

## K čemu slouží

PPCH byl vytvořen, aby rozšířil funkci pagingu z okruhově přepínaných hlasových služeb na vznikající paketově přepínané datové služby v GPRS a UMTS. Před GPRS byl paging v GSM určen výhradně pro hlasové hovory prostřednictvím Paging Channel (PCH), ale trhaná povaha paketových dat vyžadovala samostatný, optimalizovaný mechanismus. PPCH řeší potřebu upozornit mobilní datové uživatele na příchozí IP pakety a zároveň přizpůsobit odlišné charakteristiky provozu a omezení zdrojů paketových sítí.

Řeší problém dosažitelnosti UE bez nutnosti trvalého rádiového připojení, což je zásadní pro zařízení napájená bateriemi. Díky implementaci paketového pagingu mohou uživatelská zařízení přecházet do stavů s nízkou spotřebou v nečinnosti a periodicky pouze monitorovat PPCH, což výrazně prodlužuje životnost baterie ve srovnání s trvalým připojením. To byl klíčový předpoklad pro rané mobilní datové aplikace, které vyžadovaly doručování dat na pozadí. Navíc umožňuje síti efektivně spravovat rádiové prostředky, protože vyhrazené kanály jsou alokovány pouze při skutečném přenosu dat, na rozdíl od trvale zapojených okruhových spojů.

Historický kontext zahrnuje přechod od hlasově orientovaných sítí 2G k systémům 2.5G/3G s datovými schopnostmi. Omezení použití stávajícího pagingového kanálu pro okruhově přepínaná data pro paketová data zahrnovala neefektivitu při zpracování mnoha malých datových transakcí a nedostatečnou integraci s paketovými uzly jádra sítě, jako je SGSN. PPCH jako součást paketově přepínané domény poskytl přizpůsobené řešení, které komunikovalo přímo s prvky jádra GPRS a podporovalo funkce jako aktualizace směrovací oblasti nebo služební požadavky iniciované sítí. Toto oddělení umožnilo nezávislý vývoj paketových a okruhových služeb a připravilo cestu pro plně IP architektury 4G a 5G.

## Klíčové vlastnosti

- Přenosový kanál v downlinku pro paketově přepínaný paging v GPRS/UMTS
- Pro adresování konkrétních UE používá identifikátory jako P-TMSI nebo IMSI
- Podporuje nespojitý příjem (DRX) pro úsporu energie uživatelských zařízení (UE)
- Vysílán v rámci buňky nebo směrovací/pagingové oblasti
- Po odezvě UE spouští navázání prostředků pro paketová data
- Mapován na fyzické kanály, jako je PDCH v GPRS nebo S-CCPCH v UMTS

## Související pojmy

- [PCH – Paging Channel](/mobilnisite/slovnik/pch/)
- [P-TMSI – Packet-Temporary Mobile Subscriber Identity](/mobilnisite/slovnik/p-tmsi/)
- [DRX – Discontinuous Reception](/mobilnisite/slovnik/drx/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [PPCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppch/)
